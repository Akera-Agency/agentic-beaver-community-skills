# Overview — The Cold Email

*From the Agentic Beaver / OCPlatform live-demo Q&A session: "AI Agents in Production —
from chatbot to coworker."*

## The Problem

**ChatGPT is a calculator. You need a coworker.**

AI chatbots answer questions. But a business needs something that can:

- 📅 **Schedule & remember** — set reminders, check calendars, follow up without being asked.
- 🔧 **Use your tools** — connect to CRMs, email, Slack, GitHub — actually do work.
- 🔄 **Run workflows** — execute multi-step processes: research → enrich → write → send → follow up.
- 🧠 **Learn & adapt** — remember context, preferences, and history across sessions.

## The Solution

An AI operating system that gives Claude (or any LLM) a *body* — tools, memory, and
agency. This skill is the outbound-sales expression of that: a full cold-email pipeline
run by an agent.

```
🔍 SCRAPE → 📧 ENRICH → 💾 CRM → 🔬 RESEARCH → ✍️ WRITE → 🚀 SEND
```

## Real Metrics (Money campaign)

| Metric | Value |
|--------|-------|
| Leads scraped | 357 |
| Email hit rate | 39.8% (142 emails) |
| Research time per lead | ~5 min |
| Leads in CRM | 133 |

## Phase 1 — Lead Generation

Skills that find and qualify targets.

- **scrape** ✅ — Skool scraper. 357 leads from the Money category. Extracts community
 name, member count, owner info, pricing.
- **enrich** ✅ — FullEnrich integration, 39.8% hit rate. Falls back to Lemlist bulk enrich.
- **add-to-crm** ✅ — Attio API. 133 leads imported to "💰 Skool Money"; syncs member
 count, LTV, stage.

## Phase 2 — Personalized Outreach

Skills that research, write, and send.

- **research** — deep research via Tavily + YouTube scraping (Apify). Produces a
 strategic briefing with hooks.
- **cold-email** ✅ — copy frameworks (PAS/QVC/BAB/AIDA), 50–75-word templates, A/B
 built in, pattern-interrupt openers.
- **send (Lemlist)** — campaign creation, lead upload, sequence steps, launch.

## Why an Agent (not a script)

- 🧠 **Persistent memory** — remembers campaign state, lead status, what's been sent.
- 🔌 **Hot-swappable skills** — drop a SKILL.md, the agent learns a capability instantly.
- ⚡ **Model routing** — Opus for research, Sonnet for writing, Haiku for simple ops.
- 📱 **Multi-channel** — command it via Discord, Slack, Telegram — wherever you are.

## The Stack

Attio (CRM) · Lemlist (sequences) · FullEnrich (email finding) · Clay (enrichment) ·
Tavily (web research) · Apify (YouTube) · n8n (workflow automation) — all orchestrated
by the agent.
