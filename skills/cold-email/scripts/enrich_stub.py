#!/usr/bin/env python3
"""
enrich_stub.py — enrichment helper skeleton for the ENRICH stage.

Reads leads.csv, calls the enrichment provider (FullEnrich primary, Lemlist fallback),
writes enriched.csv. Fill in the provider calls with your keys from configs/.

This is a SKELETON: it validates the CSV schema and shows the intended flow.
Do not hard-code API keys — load them from configs/ or env vars.
"""
import csv
import json
import os
import sys
from pathlib import Path

REQUIRED_IN = ["community_name", "owner_name", "member_count", "monthly_price", "niche"]
OUT_COLS = REQUIRED_IN + ["email", "email_status", "calculated_ltv"]


def load_key(config_name: str, env_var: str) -> str | None:
    cfg = Path("configs") / config_name
    if cfg.exists():
        try:
            return json.loads(cfg.read_text()).get("apiKey")
        except Exception:
            pass
    return os.environ.get(env_var)


def calc_ltv(members: float, price: float, retention_months: float = 6.0) -> float:
    return round(members * price * retention_months, 2)


def enrich_row(row: dict, fe_key: str | None) -> dict:
    """TODO: call FullEnrich here with fe_key. Placeholder marks as not_found."""
    row.setdefault("email", "")
    row.setdefault("email_status", "not_found")
    return row


def main(inp="leads.csv", outp="enriched.csv"):
    fe_key = load_key(".fullenrich-config.json", "FULLENRICH_API_KEY")
    if not fe_key:
        print("⚠️  No FullEnrich key found (configs/.fullenrich-config.json or "
              "FULLENRICH_API_KEY). Running in dry mode.", file=sys.stderr)

    with open(inp, newline="") as f:
        rows = list(csv.DictReader(f))

    missing = [c for c in REQUIRED_IN if rows and c not in rows[0]]
    if missing:
        sys.exit(f"❌ leads.csv missing columns: {missing}")

    out = []
    for r in rows:
        r["calculated_ltv"] = calc_ltv(
            float(r.get("member_count", 0) or 0),
            float(r.get("monthly_price", 0) or 0),
        )
        out.append(enrich_row(r, fe_key))

    with open(outp, "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=OUT_COLS, extrasaction="ignore")
        w.writeheader()
        w.writerows(out)

    found = sum(1 for r in out if r.get("email_status") == "verified")
    print(f"✅ Wrote {outp}: {len(out)} rows, {found} verified emails "
          f"({(found/len(out)*100 if out else 0):.1f}%)")


if __name__ == "__main__":
    main(*sys.argv[1:3])
