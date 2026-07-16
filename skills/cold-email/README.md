# Cold Email 📧

A **packaged agent skill** for running an end-to-end cold outbound sales pipeline —
from finding leads to sending sequenced, personalized cold emails and handling replies.

> ChatGPT is a calculator. This skill turns your agent into a **coworker** that runs the
> whole outreach machine: **SCRAPE → ENRICH → CRM → RESEARCH → WRITE → SEND**.

Built by the Akera team and demoed live in the Agentic Beaver / OCPlatform Q&A session.

---

## What's inside

```
cold-email/
├── SKILL.md # main skill — pipeline orchestration + writing rules
├── README.md
├── .gitignore
├── references/
│ ├── pipeline-scrape.md # 🔍 lead generation
│ ├── pipeline-enrich.md # 📧 email enrichment (FullEnrich)
│ ├── pipeline-crm.md # 💾 Attio CRM sync
│ ├── pipeline-research.md # 🔬 deep prospect briefing (Tavily + YouTube)
│ ├── pipeline-send.md # 🚀 Lemlist campaigns
│ ├── frameworks.md # ✍️ PAS / QVC / BAB / AIDA + 75-word rules
│ ├── examples.md # worked cold-email examples
│ ├── examples/instantly-deal.md
│ ├── strategies.md
│ ├── email-writer-prompt.md
│ ├── reply-and-objections.md # 💬 reply + objection handling playbook
│ └── config.md # credential/config file shapes
├── scripts/
│ ├── word-count.sh # enforce the 75-word limit
│ └── enrich_stub.py # enrichment helper skeleton
└── docs/
 ├── OVERVIEW.md # the session story + metrics
 └── ARCHITECTURE.md # data flow + n8n workflows
```

## Install

Drop the `cold-email/` folder into your agent's skills directory (e.g.
`.agents/skills/` or `workspace/skills/`). The agent reads `SKILL.md` and loads the
relevant reference on demand.

## Quick start

1. Create the config files listed in [`references/config.md`](references/config.md)
 (keep real keys out of git).
2. Ask the agent things like:
 - "Scrape 5 pages of Skool 'money' leads and enrich them."
 - "Research this prospect and write me a 75-word cold email."
 - "Handle this reply — the prospect says their community will build it for free."
 - "Launch the sequence in Lemlist."

## Core writing rules

- 75 words max · no generic openers · specific > vague · one clear CTA · pattern interrupt.
- When booking a call, always offer **2 specific timeslots in the prospect's timezone**.

## Proven results

357 leads scraped · 39.8% email hit rate · 133 leads in CRM (Money campaign).

---

*Secrets never live in this repo. See `references/config.md` for the expected config
shapes and env-var fallbacks.*
