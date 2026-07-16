# CRM — Sync to Attio

Remember every lead with full context so nothing falls through and stages stay in sync.

## Goal

Push enriched leads into Attio, mapped to a list, with stage tracking.

## Process

1. **Map fields** — name, email, company/community, member count, calculated LTV.
2. **Check duplicates** — query Attio for an existing record by email before creating.
3. **Create / update record** — POST to the Attio API with all attributes.
4. **Add to list** — assign to the campaign list (e.g. "💰 Skool Money") with a stage.

```bash
$ attio import enriched.csv
✅ 133 leads added to Attio
```

## Reference numbers (Money campaign)

| Metric | Value |
|--------|-------|
| Emails found | 142 |
| Imported to CRM | 133 leads |
| List | "💰 Skool Money" |

## Stage model

```
Prospecting → Researching → Launched Sequence → (Risk Level)
```

Update the stage as the lead moves through the pipeline so the agent always knows what
has and hasn't been done.

## Field map

| Attio attribute | source |
|-----------------|--------|
| name | owner_name |
| email | email |
| company | community_name |
| member_count | member_count |
| calculated_ltv | calculated_ltv |
| stage | pipeline stage |

## Config

Attio API key lives in `configs/.attio-config.json`. See config.md.
