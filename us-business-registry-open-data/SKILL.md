---
name: us-business-registry-open-data
description: "Activate when: user needs US company registration data (LLCs, corporations, formation dates, registered agents) in bulk — lead lists by state, formation-trend analysis, entity matching, TAM sizing from registries; user asks 'where can I get company registration data,' 'Secretary of State data,' 'business registry API,' or hits OpenCorporates pricing walls. Do NOT activate when: user needs business *license* data, SEC filings, or non-US registries; user needs Delaware/California/Texas bulk data (paid or unavailable — this skill explains why, then stops)."
---

# US Business Registry Open Data

## Overview

Several US states publish their **entire business registry** — every LLC, corporation, and nonprofit ever registered — as open data on Socrata portals, explicitly in the public domain or licensed for commercial use. Five states (New York, Colorado, Pennsylvania, Oregon, Connecticut) yield **~12.4 million entities** with names, entity types, formation dates, addresses, and registered agents, for free, via a documented API. Most people assume this data is locked behind OpenCorporates pricing or state paywalls; for these states, it isn't.

This skill contains the verified dataset registry (endpoints, record counts, license terms), a working config-driven fetcher (`scripts/fetch_us_business_entities.py`, Python stdlib, no dependencies), the measured rate-limit realities nobody documents, and the gotchas that silently corrupt naive pulls.

## When to Use

**Use when:** you need bulk US company registration data with commercial-use rights; building lead lists, formation-trend analysis, registered-agent market maps, entity matching, or cohort survival studies; evaluating whether to pay OpenCorporates or a data vendor (check the free floor first).

**Skip when:** you need business *license* data (different registries — Washington and Illinois publish licenses, not registrations); you need SEC filings or officers/UBO data beyond what states expose; you need full national coverage including Delaware/California/Texas — no free path exists, budget for a vendor.

## The Process

1. **Pick states from the dataset registry below.** Only use entries with an explicit public-domain or commercial-OK license. Gate: a dataset with no license tag is OFF until terms are confirmed — a portal listing is not a license.
2. **Verify the dataset is alive** with a `count(*)` query: `https://<portal>/resource/<id>.json?$select=count(*) as cnt`. Portals migrate (Iowa's Socrata endpoints all 404 now); never trust a months-old dataset ID without this check.
3. **Pull with plain `$limit`/`$offset` pagination ordered by `:id`.** Do not use `$select=:*,*` keyset pagination and do not use the CSV export endpoint — both measured dramatically slower (see Rate-limit realities).
4. **Normalize onto a unified schema** (`state / entity_id / name / entity_type / status / formation_date / city / region / postal / agent_name`), keeping the raw row under `_raw`. Each state names columns differently; the fetcher's `SOURCES` dict is the mapping.
5. **Dedup by entity ID before counting anything.** Oregon is row-per-associated-name and Pennsylvania is row-per-officer — naive row counts overcount entities 2–3×.
6. **Resume on failure by line count.** Rows already on disk are the first N in `:id` order, so a rerun continues from offset N in append mode. Flush per page so the file is always a valid resume point.
7. **For a full pull, register a free Socrata app token** and send it as `X-App-Token` — anonymous throughput (~500 rows/sec) makes 13M rows a 7–8 hour job; the token tier is the fix.

## The dataset registry (verified June 2026)

| State | Dataset | Records | License |
|---|---|---|---|
| New York | `n9v6-gdp6` on data.ny.gov (active corps, beginning **1800**) | 4.22M | NY Open Data, commercial OK |
| Colorado | `4ykn-tg5h` on data.colorado.gov | 3.06M | Public Domain |
| Pennsylvania | `xvd7-5r2c` on data.pa.gov (officer-level rows) | 2.31M entities | Public Domain |
| Oregon | `tckn-sxa6` on data.oregon.gov (row per associated name) | 1.56M | Public record |
| Connecticut | `n7gp-d28j` on data.ct.gov (master table) | 1.28M | Public Domain |

New York also has a companion dataset (`63wc-4exh`) with **20.6M raw filing records** if you want full filing history rather than current state.

Run the bundled fetcher: `python3 scripts/fetch_us_business_entities.py --sample` validates all five states in a minute; `--state co` pulls one state; no dependencies beyond Python 3.

## Rate-limit realities (measured, anonymous tier)

- **Plain offset pagination: ~500 rows/sec — the best you'll do anonymously.** Deep offsets are NOT the problem: offset 1,000,000 returns in ~3 seconds. The bottleneck is per-page transfer, not offset depth, so the classic "keyset beats offset" instinct is wrong here.
- **Keyset via `$select=:*,*` is a dead end:** forcing system-field computation made a single 50k page take 200+ seconds, then time out.
- **CSV bulk export (`/api/views/{id}/rows.csv`) is worse:** generated server-side on demand; measured 1,229 rows in 30 seconds — ~12× slower than JSON offset paging.

## Gotchas that silently corrupt data

- **Row granularity differs per state.** Oregon = one row per associated name; Pennsylvania = one row per officer. Dedup on `registry_number` / `filing_number` is mandatory before any entity-level count.
- **CSV column labels ≠ API field names.** Connecticut's CSV export says `Business_City`; the SODA API says `billingcity`. If you mix formats, map through dataset metadata (`/api/views/{id}.json` → `columns[].fieldName`), never by header string.
- **Connecticut splits agents into companion datasets.** The master table has no agent columns; registered agents and principals live in separate Agent Details / Principal Details datasets joined on `accountnumber`.
- **NY's address is the DOS service-of-process address**, not necessarily the principal office.

## What you can't get (and why)

- **California, Texas, Delaware:** bulk registry data is paid. Delaware — the incorporation capital — has no bulk product and no API at any price; selling that data is part of the state's business model.
- **Florida:** free, but a fixed-width flat file on an FTP server (Sunbiz) — needs its own parser, not the Socrata adapter.
- **Ohio:** monthly bulk files exist but the SoS site sits behind an aggressive bot wall.
- **Iowa:** migrated off Socrata to "Iowa Data Hub"; documented legacy endpoints 404. License is CC BY 4.0 — revisit when the new API is documented.
- **Hawaii:** full statewide registry (~442k) exists on data.honolulu.gov but carries no explicit license tag — stays off until commercial terms are confirmed.
- **Washington, Illinois:** publish business *license* data, not the registration registry.

## Legality and ethics

Everything enabled here is official government open data with explicit public-domain or commercial-OK terms — no scraping of search UIs, no ToS gray zones. The discipline: a state publishing its registry on an open-data portal is an invitation; a state putting it behind a paywall or bot wall is an answer, and the answer is no. Datasets without a clear license tag stay disabled until terms are confirmed.

## Verification

- [ ] Every enabled dataset has an explicit public-domain or commercial-OK license verified on its portal page (not assumed from being publicly visible)
- [ ] Record counts come from live `count(*)` queries, not row counts of the pulled file
- [ ] Entity counts are deduplicated by entity ID where the dataset is row-per-name or row-per-officer
- [ ] The pull uses `$order=:id` so resume-by-line-count is deterministic
- [ ] Column mapping went through SODA field names (or dataset metadata), never CSV header strings

---

*Part of **deciqAI Knowledge Skills** — 223 open-source thinking skills that make rigor executable for AI agents. The same skills power every deciqAI agent, which runs them autonomously to operate your company. **See it run → https://www.deciqai.com/s/us-business-registry-open-data** · Built by deciqAI · github.com/deciqAI · Contributions welcome.*
