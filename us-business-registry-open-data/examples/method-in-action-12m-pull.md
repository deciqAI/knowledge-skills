# Method in Action: Pulling 12.4M Registrations Across Five States (June 2026)

A real pull, walked through the skill's own steps — including the two mistakes the process exists to catch.

## Step 1–2: Registry check and liveness

The starting assumption was that US registration data required OpenCorporates (capped free tier, commercial license in "contact sales" territory) or per-state scraping. Checking state open-data portals directly instead surfaced five full registries with explicit public-domain or commercial-OK terms.

Liveness checks mattered immediately: Iowa's documented Socrata dataset (`ez5t-3qay`) returned 404 on every legacy endpoint — the state had migrated platforms. Without the `count(*)` gate, the pull would have been configured against a dead source. Hawaii's registry (~442k records) was alive but carried **no license tag**, so it stayed disabled — being publicly downloadable is not a commercial-use grant.

## Step 3: The pagination decision — measured, not assumed

Standard advice for large Socrata extracts is keyset pagination on system fields (`$select=:*,*` then page on `:id`). Measured on these datasets, that advice failed:

| Method | Measured throughput |
|---|---|
| Plain `$limit`/`$offset` ordered by `:id` | ~500 rows/sec |
| Keyset via `$select=:*,*` | one 50k page: 200+ sec, then timeout |
| CSV export `/api/views/{id}/rows.csv` | 1,229 rows in 30 sec (~40 rows/sec) |

The counter-intuitive finding: a query at offset 1,000,000 returned in ~3 seconds — barely slower than offset 0. Per-page transfer is the bottleneck, not offset depth, so plain offset paging wins. At ~500 rows/sec the full ~13M rows is a 7–8 hour anonymous pull; a free app token raises the tier.

## Step 5: The dedup gotcha, caught

Pennsylvania's raw file had far more rows than the state plausibly has businesses. Cause: the dataset is one row per *officer*, so one filing number spans multiple rows. Oregon similarly is one row per *associated name*. Naive row counts overcounted entities 2–3×; deduplicating on `filing_number` / `registry_number` produced the honest totals (2.31M PA entities, 1.56M OR).

## Step 6: Resume in practice

Multi-hour anonymous pulls die — network blips, throttling. Because every page was flushed and rows are ordered by `:id`, a rerun counted lines already on disk and continued from that offset in append mode. A sample run's 1,000 rows are a valid prefix of the full pull; nothing was ever re-fetched or lost.

## Result

~12.4M normalized entities across NY (4.22M), CO (3.06M), PA (2.31M), OR (1.56M), CT (1.28M) — names, entity types, formation dates, addresses, registered agents — at zero data cost, with clean commercial-use provenance for every enabled source.

**Sources:** dataset landing pages and license terms in [references/sources.md](../references/sources.md); throughput figures are direct measurements from this pull (June 2026, anonymous tier).
