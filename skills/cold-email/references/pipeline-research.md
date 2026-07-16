# RESEARCH — Deep Prospect Briefing

Replaces manual Gemini sessions. Produces a strategic briefing with actionable hooks so
the cold email is hyper-personalized, not boilerplate.

> Rule: always run research on **Opus** (or Claude Max) — this is the highest-leverage
> stage. A great hook makes the 75-word email write itself.

## Input

```yaml
lead_name: "Alex Hormozi"
company: "Acquisition.com"
youtube_url: "@AlexHormozi"
context: "AI retention for course creators"
```

## Process

1. **Tavily search** (`search_depth: "advanced"`, `include_answer: true`) — background,
 news, interviews.
2. **YouTube scrape** (Apify) — recent videos + transcripts from their channel.
3. **Content analysis** (Claude) — extract values, philosophy, communication style, quotes.
4. **Hook generation** — 3+ actionable openers, plus explicit anti-patterns ("don't say").

## Apify actors

- `streamers~youtube-channel-scraper` — channel video list
- `dz_omar~youtube-transcript-metadata-extractor` — transcripts

## Output: Strategic Briefing (template)

```markdown
# Alex Hormozi — Account Briefing

## Philosophy
"Give away the secrets, sell the implementation"
Anti-guru, proof-focused, aggressive transparency

## Top Hooks
1. Reference "$100M Offers" framework
2. Lead with numbers (he respects data)
3. Connect to "volume negates luck"

## Don't Say
- Fluffy language, vague promises
- "Just wanted to reach out"
- Generic AI buzzwords

## Quote to Use
"Most people need to hear you're not working hard enough"

## Suggested Opener
"Your breakdown on retention curves — most programs we see: 15% finish rate..."
```

## Handoff

The briefing feeds directly into the WRITE stage: pull the top 3 hooks + the
personalization points, pick a framework, write.

## Config

- Tavily key → `configs/.tavily-config.json`
- Apify key → `configs/.apify-config.json`
