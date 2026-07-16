# Config & Credentials

**Never hard-code secrets in the skill.** All keys live in workspace config files (or
env vars). This file documents the expected shape of each.

## Files

```
configs/.attio-config.json
configs/.lemlist-config.json
configs/.fullenrich-config.json
configs/.tavily-config.json
configs/.apify-config.json
```

## Shapes

`.attio-config.json`
```json
{ "apiKey": "attio_...", "defaultListId": "..." }
```

`.lemlist-config.json`
```json
{ "apiKey": "lemlist_...", "baseUrl": "https://api.lemlist.com/api" }
```

`.fullenrich-config.json`
```json
{ "apiKey": "fe_...", "creditsWarnThreshold": 50 }
```

`.tavily-config.json`
```json
{ "apiKey": "tvly-...", "searchDepth": "advanced", "includeAnswer": true }
```

`.apify-config.json`
```json
{
 "apiKey": "apify_...",
 "channelActor": "streamers~youtube-channel-scraper",
 "transcriptActor": "dz_omar~youtube-transcript-metadata-extractor"
}
```

## Env-var fallbacks

If a config file is absent, fall back to env vars:

```
ATTIO_API_KEY LEMLIST_API_KEY FULLENRICH_API_KEY TAVILY_API_KEY APIFY_API_KEY
```

## Rules

- Config files must be `.gitignore`d — never commit real keys.
- On missing credentials, tell the user which config file to create; do not invent keys.
