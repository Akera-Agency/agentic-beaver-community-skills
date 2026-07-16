# Contributing a skill

Skills in this registry are **self-contained folders**. An agent installs one by
copying its folder and reading its `SKILL.md` — so everything a skill needs must live
inside its own directory.

## 1. Create the folder

```
skills/<your-skill-id>/
├── SKILL.md          ← REQUIRED. The entrypoint.
├── README.md         ← optional, human-facing overview
├── docs/             ← optional, architecture/overview notes
├── references/       ← optional, per-topic reference files (load on demand)
└── scripts/          ← optional, helper scripts
```

- `<your-skill-id>` must be lowercase, `a-z0-9-` only (e.g. `cold-email`).
- Keep the folder **portable**: no absolute paths, no dependency on files outside it.

## 2. Write `SKILL.md`

Start with YAML frontmatter so agents know when to use it:

```markdown
---
name: your-skill-id
description: >
  One paragraph: what it does and WHEN to trigger it. Include concrete trigger
  phrases the user might say.
metadata:
  version: 1.0.0
  maintainer: "Your name / team"
---

# Skill title

...the actual instructions...
```

Write references so an agent can **load only the stage it needs**, not the whole skill.

## 3. Register it

Add an entry to [`registry.json`](./registry.json) under `skills[]`:

```json
{
  "id": "your-skill-id",
  "name": "Human Readable Name",
  "path": "skills/your-skill-id",
  "entrypoint": "SKILL.md",
  "version": "1.0.0",
  "description": "Short description.",
  "triggers": ["phrase one", "phrase two"],
  "tags": ["category"],
  "maintainer": "Your name / team",
  "source": "https://github.com/... (optional origin repo)"
}
```

Bump the registry `version` and `updated` date, and add a row to the README table.

## 4. Validate

- `registry.json` conforms to [`registry.schema.json`](./registry.schema.json).
- The skill folder runs standalone (SKILL.md references only its own files).

Open a PR. Keep skills focused — one job, done well.
