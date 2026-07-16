# Agentic Beaver — Community Skills

A registry of **installable, self-contained agent skills** for Agentic Beaver.

Each skill is a self-contained folder under [`skills/`](./skills): a `SKILL.md`
(the entrypoint the agent reads) plus optional `docs/`, `references/`, and
`scripts/`. Nothing outside its own folder is required to run it.

---

## For agents: how to install a skill

1. **Read [`registry.json`](./registry.json)** — the machine-readable index of every
   available skill (id, path, version, triggers, description).
2. **Pick a skill** by `id` (e.g. `cold-email`).
3. **Copy its folder** `skills/<path>/` into your own skills directory, e.g.:
   ```
   cp -a skills/cold-email  <your-agent>/skills/cold-email
   ```
   or sparse-clone just that path:
   ```
   git clone --depth 1 --filter=blob:none --sparse \
     https://github.com/Akera-Agency/agentic-beaver-community-skills.git
   cd agentic-beaver-community-skills
   git sparse-checkout set skills/cold-email
   ```
4. **Read `SKILL.md`** inside the copied folder and follow it. That file's YAML
   frontmatter (`name`, `description`, trigger phrases) tells you when to use it.

> Rule of thumb: load only the reference file for the stage you need — skills are
> written so you don't have to pull the whole thing into context.

---

## Available skills

| id | what it does | version |
|----|--------------|---------|
| [`cold-email`](./skills/cold-email) | End-to-end cold outbound pipeline — scrape → enrich → CRM → research → write → send, plus reply/objection handling | 3.0.0 |

_(The table mirrors [`registry.json`](./registry.json); the JSON is the source of truth.)_

---

## Repository layout

```
agentic-beaver-community-skills/
├── README.md              ← you are here
├── registry.json          ← machine-readable index (agents read this first)
├── registry.schema.json   ← JSON Schema for registry.json
├── CONTRIBUTING.md         ← how to add a new skill
├── LICENSE                ← MIT
└── skills/
    └── cold-email/        ← one self-contained skill
        ├── SKILL.md       ← entrypoint
        ├── README.md
        ├── docs/
        ├── references/
        └── scripts/
```

## Adding a skill

See [`CONTRIBUTING.md`](./CONTRIBUTING.md). In short: drop a self-contained folder
under `skills/<id>/` with a `SKILL.md`, then add an entry to `registry.json`.

---

Maintained by [Akera Agency](https://github.com/Akera-Agency). MIT licensed.
