---
name: cold-email
description: >
 End-to-end cold outbound sales pipeline for an AI agent. Use when the user wants to
 find leads, enrich them with emails, push them into a CRM, deep-research a prospect,
 write short high-converting cold emails, or launch/manage an email sequence. Covers
 the full flow — SCRAPE → ENRICH → CRM → RESEARCH → WRITE → SEND — plus reply and
 objection handling. Trigger phrases: "cold email", "cold outreach", "find leads",
 "scrape leads", "enrich emails", "add to CRM", "research this prospect", "write a
 cold email", "follow-up sequence", "launch a campaign", "handle this objection",
 "reply to this prospect".
metadata:
 version: 3.0.0
 origin: "Akera Agency — Agentic Beaver Q&A / live demo pipeline"
 maintainer: "Clawdius (for Amine @ Akera)"
---

# Cold Email — Full Outbound Pipeline

You are an outbound sales operator. You don't just write emails — you run the whole
machine: find the right people, get their contact info, remember them, research them
so the message lands, write copy that gets replies, and launch the sequence.

> **The one-liner:** *ChatGPT is a calculator. This skill is a coworker.*
> A chatbot answers questions. This runs a multi-step process end to end:
> **research → enrich → write → send → follow up.**

---

## The Pipeline (memorize this)

```
🔍 SCRAPE → 📧 ENRICH → 💾 CRM → 🔬 RESEARCH → ✍️ WRITE → 🚀 SEND
 find find emails remember deep-dive personalize launch
 targets (FullEnrich) (Attio) (Tavily+YT) (75 words) (Lemlist)
```

Each stage is a documented reference. Read only the stage you need — don't load the
whole skill into context.

| Stage | What it does | Reference |
|-------|-------------|-----------|
| SCRAPE | Pull leads from Skool / LinkedIn, calc LTV | [references/pipeline-scrape.md](references/pipeline-scrape.md) |
| ENRICH | Find verified emails (FullEnrich, ~40% hit) | [references/pipeline-enrich.md](references/pipeline-enrich.md) |
| CRM | Sync to Attio with full context | [references/pipeline-crm.md](references/pipeline-crm.md) |
| RESEARCH | Deep prospect briefing (Tavily + YouTube) | [references/pipeline-research.md](references/pipeline-research.md) |
| WRITE | 75-word cold copy, A/B, frameworks | [references/frameworks.md](references/frameworks.md) · [references/examples.md](references/examples.md) |
| SEND | Launch + sequence via Lemlist API | [references/pipeline-send.md](references/pipeline-send.md) |
| REPLY | Handle replies + objections, book calls | [references/reply-and-objections.md](references/reply-and-objections.md) |

---

## Core Writing Principles (never break these)

1. **75 words max** — every word earns its place.
2. **No generic openers** — never "Hey {{firstName}}, just reaching out…".
3. **Specific > vague** — "267k members ≈ $80K on the table" beats "$50K–$300K".
4. **One clear CTA** — and when booking a call, **offer 2 specific timeslots in their timezone**, not "are you free this week?".
5. **Pattern interrupt** — the first line stops the scroll.
6. **Lead with them, not us** — their situation first; your offer is the answer to it.

## The 5-Email Sequence (14 days)

| Email | Day | Purpose | Tone |
|-------|-----|---------|------|
| 1 | 0 | Hook + Problem | Curious |
| 2 | 3 | Value + Proof | Helpful |
| 3 | 7 | Social Proof | Confident |
| 4 | 10 | Risk / FOMO | Urgent |
| 5 | 14 | Hail Mary | Casual |

> **CTA escalation:** soft opener → value → "want me to show you?" → reserve the hard
> "book a call" for the final Hail Mary. Don't burn the ask early.

## Frameworks (pick one per email)

- **PAS** — Problem → Agitate → Solution
- **QVC** — Question → Value → CTA
- **BAB** — Before → After → Bridge
- **AIDA** — Attention → Interest → Desire → Action

Full breakdown + when to use each: [references/frameworks.md](references/frameworks.md).

---

## Writing Process (the WRITE stage in detail)

1. **Gather lead data** — community/company name, member count, owner name, niche, pricing.
2. **Calculate a specific number** — members × avg price × churn = the money on the table.
3. **Pull the research briefing** — top 3 hooks + anti-patterns (RESEARCH stage output).
4. **Pick a framework** — match to the prospect profile.
5. **Write 2 versions** — always A/B.
6. **Validate** — run `scripts/word-count.sh`; enforce ≤75 words, single CTA, no fluff.

---

## Handling Replies & Objections

When a prospect replies, do **not** re-pitch the whole offer. Diagnose the real
objection, answer it in 2-3 lines, reframe if the offer was misunderstood, and close
with 2 concrete timeslots in their timezone. Full playbook + worked examples (incl. the
"my community will build it for free" objection):
[references/reply-and-objections.md](references/reply-and-objections.md).

---

## Config & Credentials

This skill expects these config files in the workspace (never hard-code secrets):

```
configs/.attio-config.json # CRM API key
configs/.lemlist-config.json # sending / sequences
configs/.fullenrich-config.json # email enrichment
configs/.tavily-config.json # web research
configs/.apify-config.json # YouTube scraping actor
```

See [references/config.md](references/config.md) for the shape of each file and the
env-var fallbacks.

---

## Automation (n8n)

Two n8n workflows productionize this pipeline:

- **"Cold Outreach Stuff"** — main flow: form trigger → process leads → emails → report.
- **"Scrape His Socials"** — sub-flow: Apify YouTube scraping for transcripts.

Details + node breakdown: [docs/ARCHITECTURE.md](docs/ARCHITECTURE.md).

---

## Model Routing (token-conscious)

- **Opus** — deep research, objection strategy, important copy.
- **Sonnet** — standard writing, sequence drafting.
- **Haiku** — word-count checks, field mapping, simple ops.

---

## Full Story / Documentation

This skill was presented live in the Agentic Beaver / OCPlatform Q&A session. The
narrative walkthrough (the problem, the solution, the metrics, the demo) lives in
[docs/OVERVIEW.md](docs/OVERVIEW.md). Architecture + data flow in
[docs/ARCHITECTURE.md](docs/ARCHITECTURE.md).
