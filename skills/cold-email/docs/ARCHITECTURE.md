# Architecture & Data Flow

## Data flow

```
# Lead Gen
Skool → scrape → leads.csv
leads.csv → FullEnrich → emails
emails → Attio → CRM

# Outreach
lead → Tavily + YouTube → briefing
briefing → cold-email → copy
copy → Lemlist → send
```

## n8n workflows

Two workflows productionize the pipeline:

### "Cold Outreach Stuff" (main)
`form trigger → process leads → emails → report`

The end-to-end orchestrator. A form kicks it off, leads are processed, emails generated,
and a report is produced/notified (e.g. to a Discord GTM channel).

### "Scrape His Socials" (sub-workflow)
Apify YouTube scraping for transcripts. Called by the research stage.

Apify actors:
- `streamers~youtube-channel-scraper`
- `dz_omar~youtube-transcript-metadata-extractor`

## Suggested workspace structure

```
workspace/
├── AGENTS.md # agent instructions
├── MEMORY.md # pipeline state
│
├── skills/
│ └── cold-email/
│ ├── SKILL.md
│ ├── references/
│ ├── scripts/
│ └── docs/
│
├── configs/
│ ├── .attio-config.json
│ ├── .lemlist-config.json
│ ├── .fullenrich-config.json
│ ├── .tavily-config.json
│ └── .apify-config.json
│
└── memory/
 └── lead-gen-workflow-session.md
```

## Orchestration model

The agent reads `SKILL.md`, then loads only the reference for the stage it's working on.
State (which leads are at which stage) lives in the CRM + MEMORY.md, so any fresh session
can resume the pipeline without re-deriving context.
