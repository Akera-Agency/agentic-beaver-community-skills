# ENRICH — Find Verified Emails

Turn scraped profiles into contactable leads. Output: `enriched.csv` with emails.

## Primary: FullEnrich

- Upload `leads.csv` to FullEnrich.
- It returns verified business emails.
- **Real hit rate: ~39.8%** (142 emails from 357 leads on the Money campaign).
- Track credit balance — enrichment is metered.

```bash
$ enrich leads.csv --fullenrich
📧 Enriching 357 leads...
✅ Found 142 emails (39.8%)
```

## Fallback: Lemlist bulk enrich

If FullEnrich credits run low or coverage is poor, fall back to the Lemlist enrich API:

```
POST /enrich # single lead
POST /enrich/bulk # batch, 500 max
```

## Reference numbers (Money campaign)

| Metric | Value |
|--------|-------|
| Total scraped | 357 |
| Emails found | 142 (39.8%) |
| FullEnrich credits used | ~ tracked per run |

## enriched.csv schema (adds to scrape schema)

| column | example |
|--------|---------|
| email | owner@example.com |
| email_status | verified / risky / not_found |
| enriched_at | 2026-03-24 |

## Rules

- **Never** proceed to SEND with `risky`/`not_found` emails — they tank deliverability.
- Keep enrichment provider keys in `configs/.fullenrich-config.json` (see config.md).
- Dedupe by email before pushing to CRM.
