# SCRAPE — Lead Generation

Find and qualify targets. Output: a structured `leads.csv` ready for enrichment.

## Goal

Extract community owners / course creators from Skool (or LinkedIn) and calculate the
opportunity value for each, so downstream stages prioritize the best leads.

## Process

1. **Pick a target niche** (e.g. `"Money"`, `"Fitness"`, `"Agency"`).
2. **Search Skool** — query the category, paginate through 5+ pages of results.
3. **Extract profiles** — for each community capture:
 - community name
 - owner name
 - member count
 - pricing (monthly)
4. **Calculate LTV / opportunity**:
 ```
 opportunity = members × monthly_price × avg_retention_months
 ```
 This becomes the "money on the table" number you cite in the cold email.
5. **Export** to `leads.csv` with a stable schema for the ENRICH stage.

## Example (CLI mental model)

```bash
$ scrape skool "money" --pages 5
🔍 Scraping Skool communities...
📊 Found 357 communities
💾 Saved to leads.csv
```

## Reference numbers (Money campaign, actual run)

| Metric | Value |
|--------|-------|
| Total scraped | 357 leads |
| Passed to enrich | 357 |

## leads.csv schema

| column | example |
|--------|---------|
| community_name | "Skool Money Makers" |
| owner_name | "Alex R." |
| member_count | 267000 |
| monthly_price | 99 |
| calculated_ltv | 79200 |
| niche | money |
| source_url | https://www.skool.com/... |

## Notes

- YouTube-only for social scraping downstream (skip Twitter/LinkedIn scraping to save
 cost — decided during the real campaign).
- Batch size for downstream research: **20 leads at a time**.
- Implementation can be a Python Skool scraper or an Apify actor; keep the CSV schema
 identical so the rest of the pipeline is source-agnostic.
