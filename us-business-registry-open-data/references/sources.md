# Sources

All record counts from live `count(*)` queries; all license terms verified on the dataset landing pages (June 2026).

## Enabled datasets

| State | Dataset | Landing page | License |
|---|---|---|---|
| New York | `n9v6-gdp6` | https://data.ny.gov/Government-Finance/Active-Corporations-Beginning-1800/n9v6-gdp6 | NY Open Data, commercial OK |
| New York (filings) | `63wc-4exh` | https://data.ny.gov/Government-Finance/Corporation-and-Business-Entity-Filings-Beginning-/63wc-4exh | NY Open Data, commercial OK |
| Colorado | `4ykn-tg5h` | https://data.colorado.gov/Business/Business-Entities-in-Colorado/4ykn-tg5h | Public Domain |
| Pennsylvania | `xvd7-5r2c` | https://data.pa.gov/Government-That-Works/Registered-Businesses-in-PA-Current-Monthly-County/xvd7-5r2c | Public Domain |
| Oregon | `tckn-sxa6` | https://data.oregon.gov/Business/Active-Businesses-ALL/tckn-sxa6 | Public record |
| Connecticut | `n7gp-d28j` | https://data.ct.gov/Business/Connecticut-Business-Registry-Business-Master/n7gp-d28j | Public Domain |

## Deferred / unavailable

- **Hawaii** — `9k54-ztb8` on data.honolulu.gov (~442k, statewide DCCA registry). No explicit license tag; disabled until commercial terms are confirmed.
- **Iowa** — legacy Socrata dataset `ez5t-3qay` 404s after migration to "Iowa Data Hub". License CC BY 4.0.
- **Ohio** — monthly bulk files at ohiosos.gov/business/business-reports (second Saturday), behind a bot wall.
- **Florida** — Sunbiz FTP, fixed-width flat files (free, needs a non-Socrata parser).
- **California / Texas / Delaware** — bulk registry access is paid (CA, TX) or nonexistent at any price (DE).

## API documentation

- Socrata SODA API: https://dev.socrata.com/docs/queries/
- App tokens (higher rate-limit tier): https://dev.socrata.com/docs/app-tokens
- Dataset metadata / column field names: `https://<portal>/api/views/<dataset-id>.json` → `columns[].fieldName`
