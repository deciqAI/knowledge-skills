#!/usr/bin/env python3
"""
Fetch US state business-entity registries from official open-data portals (Socrata SODA API).

Config-driven: each state is one entry in SOURCES with its Socrata dataset endpoint and a
field map onto a normalized schema. Adding another Socrata open-data state = one more entry.

Only states whose bulk data is FREE and COMMERCIALLY usable are enabled. States behind
paywalls, bot-walls, or platform migrations are listed as deferred and skipped.

Output: ./data/us-business-entities/<state>_entities.jsonl  (one normalized record per line;
override the directory with OUT_DIR=/path)

Usage:
  python3 fetch_us_business_entities.py --sample          # 1000 rows/state, quick validate
  python3 fetch_us_business_entities.py                    # full pull, all enabled states
  python3 fetch_us_business_entities.py --state co         # one state, full
  python3 fetch_us_business_entities.py --state co --limit 5000
  APP_TOKEN=xxxx python3 fetch_us_business_entities.py     # optional Socrata token (higher rate limits)
"""

import argparse
import json
import os
import sys
import time
import urllib.request
import urllib.parse
from pathlib import Path

OUT_DIR = Path(os.environ.get("OUT_DIR", "data/us-business-entities"))
PAGE_SIZE = 50000  # Socrata max per request without paging tricks
APP_TOKEN = os.environ.get("APP_TOKEN", "").strip()

# --- Source registry -------------------------------------------------------
# resource: Socrata SODA JSON endpoint (paginated with $limit/$offset/$order=:id)
# fields:   normalized_key -> source column name (None = not available for that state)
# license / commercial: documented terms (verified 2026-06-05)
SOURCES = {
    "co": {
        "name": "Colorado",
        "enabled": True,
        "resource": "https://data.colorado.gov/resource/4ykn-tg5h.json",
        "landing": "https://data.colorado.gov/Business/Business-Entities-in-Colorado/4ykn-tg5h",
        "license": "Public Domain",
        "fields": {
            "entity_id": "entityid",
            "name": "entityname",
            "entity_type": "entitytype",
            "status": "entitystatus",
            "formation_date": "entityformdate",
            "city": "principalcity",
            "region": "principalstate",
            "postal": "principalzipcode",
            "agent_org": "agentorganizationname",
            "agent_first": "agentfirstname",
            "agent_last": "agentlastname",
        },
    },
    "or": {
        "name": "Oregon",
        "enabled": True,
        "resource": "https://data.oregon.gov/resource/tckn-sxa6.json",
        "landing": "https://data.oregon.gov/Business/Active-Businesses-ALL/tckn-sxa6",
        "license": "Public record (no restriction)",
        # NOTE: Oregon is row-per-associated-name; multiple rows share one registry_number.
        # We keep rows as-is here; grouping by entity_id is a downstream concern.
        "fields": {
            "entity_id": "registry_number",
            "name": "business_name",
            "entity_type": "entity_type",
            "status": None,  # dataset is "Active Businesses - ALL" -> implicitly active
            "formation_date": "registry_date",
            "city": "city",
            "region": "state",
            "postal": "zip",
            "agent_org": None,
            "agent_first": "first_name",
            "agent_last": "last_name",
        },
    },
    "ct": {
        "name": "Connecticut",
        "enabled": True,
        "resource": "https://data.ct.gov/resource/n7gp-d28j.json",
        "landing": "https://data.ct.gov/Business/Connecticut-Business-Registry-Business-Master/n7gp-d28j",
        "license": "Public Domain",
        # Master/account table only. Registered-agent + principals live in companion
        # datasets (Agent Details / Principal Details) joined on accountnumber.
        "fields": {
            "entity_id": "accountnumber",
            "name": "name",
            "entity_type": "business_type",
            "status": "status",
            "formation_date": "date_registration",
            "city": "billingcity",
            "region": "billingstate",
            "postal": "billingpostalcode",
            "agent_org": None,
            "agent_first": None,
            "agent_last": None,
        },
    },
    "ny": {
        "name": "New York",
        "enabled": True,
        "resource": "https://data.ny.gov/resource/n9v6-gdp6.json",
        "landing": "https://data.ny.gov/Government-Finance/Active-Corporations-Beginning-1800/n9v6-gdp6",
        "license": "NY State Open Data (commercial OK)",
        # Active entity-level file. city/region/zip below are the DOS process
        # (service-of-process) address, not necessarily the principal office.
        "fields": {
            "entity_id": "dos_id",
            "name": "current_entity_name",
            "entity_type": "entity_type",
            "status": None,  # "Active Corporations" file -> active
            "formation_date": "initial_dos_filing_date",
            "city": "dos_process_city",
            "region": "dos_process_state",
            "postal": "dos_process_zip",
            "agent_org": "dos_process_name",
            "agent_first": None,
            "agent_last": None,
        },
    },
    "pa": {
        "name": "Pennsylvania",
        "enabled": True,
        "resource": "https://data.pa.gov/resource/xvd7-5r2c.json",
        "landing": "https://data.pa.gov/Government-That-Works/Registered-Businesses-in-PA-Current-Monthly-County/xvd7-5r2c",
        "license": "Public Domain",
        # Officer-level: multiple rows per filing_number (party_type = officer role).
        # No separate person-name column, so agent_name stays empty here.
        "fields": {
            "entity_id": "filing_number",
            "name": "business_name",
            "entity_type": "typeofbusinessregistration",
            "status": None,  # current registry
            "formation_date": "creationdate",
            "city": "city",
            "region": "state",
            "postal": "zip",
            "agent_org": None,
            "agent_first": None,
            "agent_last": None,
        },
    },
    # --- Deferred (free + commercial-OK, but not pullable today) -------------
    "hi": {
        "name": "Hawaii",
        "enabled": False,
        "resource": "https://data.honolulu.gov/resource/9k54-ztb8.json",
        "reason": "Statewide DCCA registry (~442k, full) lives on data.honolulu.gov. Schema ready "
                  "(fileno/name/business_type/status/registration_date/agent_name). Dataset has NO "
                  "explicit license tag -> confirm commercial terms before enabling.",
    },
    "ia": {
        "name": "Iowa",
        "enabled": False,
        "reason": "Migrated to 'Iowa Data Hub'; legacy Socrata endpoints 404 (dataset ez5t-3qay). "
                  "License CC BY 4.0 (attribution). Revisit once new platform API is documented.",
    },
    "oh": {
        "name": "Ohio",
        "enabled": False,
        "reason": "ohiosos.gov behind a bot/maintenance wall; monthly bulk files at "
                  "ohiosos.gov/business/business-reports (2nd Saturday). Fetch from an unblocked "
                  "network/browser to capture literal file URLs, then add a non-Socrata adapter.",
    },
}


def http_get_json(url, timeout=60, retries=6):
    headers = {"User-Agent": "Mozilla/5.0", "Accept": "application/json"}
    if APP_TOKEN:
        headers["X-App-Token"] = APP_TOKEN
    last_err = None
    for attempt in range(retries):
        try:
            req = urllib.request.Request(url, headers=headers)
            with urllib.request.urlopen(req, timeout=timeout) as resp:
                return json.loads(resp.read().decode())
        except Exception as e:
            last_err = e
            # Exponential backoff capped at 30s — rides out DNS blips / throttling.
            time.sleep(min(30, 3 * (attempt + 1)))
    raise RuntimeError("GET failed after %d retries: %s (%s)" % (retries, url, last_err))


def count_lines(path):
    if not path.exists():
        return 0
    with open(path, "rb") as f:
        return sum(1 for _ in f)


def count_rows(resource):
    url = "%s?%s" % (resource, urllib.parse.urlencode({"$select": "count(*) as cnt"}))
    data = http_get_json(url)
    return int(data[0]["cnt"]) if data else 0


def normalize(row, fields, state_code):
    """Map a raw Socrata row onto the normalized schema. Keep raw for fidelity."""
    out = {"state": state_code.upper()}
    for key, col in fields.items():
        out[key] = row.get(col) if col else None
    # Compose a single agent_name from whatever agent fields exist.
    org = (out.pop("agent_org", None) or "").strip()
    first = (out.pop("agent_first", None) or "").strip()
    last = (out.pop("agent_last", None) or "").strip()
    person = (" ".join(p for p in [first, last] if p)).strip()
    out["agent_name"] = org or person or None
    out["_raw"] = row
    return out


def fetch_state(code, src, limit=None):
    resource = src["resource"]
    fields = src["fields"]
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    out_path = OUT_DIR / ("%s_entities.jsonl" % code)

    try:
        total = count_rows(resource)
    except Exception as e:
        print("  [%s] count failed: %s" % (code, e))
        total = None
    target = min(total, limit) if (total and limit) else (limit or total)

    # $offset pagination ordered by :id. Resume: rows already on disk are the first
    # N by that order, so we continue from offset N in append mode (a sample run's
    # 1000 rows are a valid prefix of the full pull). Deep-offset queries stay usable
    # here (offset=1M returns in ~3s); the bottleneck is per-page transfer, not depth.
    resume = count_lines(out_path)
    if target and resume >= target:
        print("  [%s] %s -> %s already complete (%d rows), skipping" % (
            code, src["name"], out_path.name, resume))
        return resume
    mode = "a" if resume else "w"
    print("  [%s] %s -> %s (total=%s, fetching=%s, resume_from=%d)" % (
        code, src["name"], out_path.name, total, target if target else "all", resume))

    written = resume
    offset = resume
    t0 = time.time()
    with open(out_path, mode, encoding="utf-8") as f:
        while True:
            page = min(PAGE_SIZE, (target - written)) if target else PAGE_SIZE
            if page <= 0:
                break
            params = {"$limit": page, "$offset": offset, "$order": ":id"}
            url = "%s?%s" % (resource, urllib.parse.urlencode(params))
            rows = http_get_json(url)
            if not rows:
                break
            for row in rows:
                f.write(json.dumps(normalize(row, fields, code), ensure_ascii=False) + "\n")
            f.flush()  # durable at each page boundary so resume is clean
            written += len(rows)
            offset += len(rows)
            rate = (written - resume) / max(time.time() - t0, 0.001)
            print("    ...%d rows (%.0f/s)" % (written, rate), end="\r", flush=True)
            if len(rows) < page:
                break
    print("    ...%d rows written -> %s%s" % (written, out_path, " " * 10))
    return written


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--state", help="single state code (co/or/ct/ny/pa)")
    ap.add_argument("--limit", type=int, help="max rows per state")
    ap.add_argument("--sample", action="store_true", help="shortcut for --limit 1000")
    args = ap.parse_args()

    limit = 1000 if args.sample else args.limit
    codes = [args.state.lower()] if args.state else list(SOURCES.keys())

    print("US business-entity fetch | app_token=%s | limit=%s" % (
        "yes" if APP_TOKEN else "no", limit if limit else "full"))
    grand = 0
    for code in codes:
        src = SOURCES.get(code)
        if not src:
            print("  [%s] unknown state, skipping" % code)
            continue
        if not src.get("enabled"):
            print("  [%s] %s DEFERRED: %s" % (code, src["name"], src.get("reason", "")))
            continue
        try:
            grand += fetch_state(code, src, limit)
        except Exception as e:
            # One state's network failure must not abort the others. Partial output
            # stays on disk; a re-run resumes that state from where it stopped.
            print("\n  [%s] FAILED (will resume on re-run): %s" % (code, e))
    print("\nDone. %d total records across enabled states." % grand)


if __name__ == "__main__":
    main()
