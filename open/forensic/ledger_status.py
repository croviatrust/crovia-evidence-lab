#!/usr/bin/env python3
import json
from datetime import datetime, timezone, timedelta
from pathlib import Path

PRESENCE = Path("open/signal/presence_latest.jsonl")
ABSENCE = Path("open/forensic/absence_receipts_7d.jsonl")
OUT = Path("open/signal/ledger_status_latest.json")

now = datetime.now(timezone.utc)

targets = set()
events_24h = 0

if PRESENCE.exists():
    with PRESENCE.open("r", encoding="utf-8") as f:
        for line in f:
            o = json.loads(line)
            targets.add(o["project_key"])

if ABSENCE.exists():
    with ABSENCE.open("r", encoding="utf-8") as f:
        for line in f:
            o = json.loads(line)
            ts = datetime.fromisoformat(o["observed_at"].replace("Z","+00:00"))
            if now - ts < timedelta(hours=24):
                events_24h += 1

coverage = len(targets)
level = "LOW" if coverage < 25 else "MEDIUM" if coverage < 100 else "HIGH"

status = {
    "schema": "crovia.open.ledger_status.v1",
    "ts": now.isoformat(),
    "targets_observed": coverage,
    "events_24h": events_24h,
    "coverage_level": level,
    "note": "Silence is now observed under high coverage conditions."
}

OUT.parent.mkdir(parents=True, exist_ok=True)
with OUT.open("w", encoding="utf-8") as f:
    json.dump(status, f, indent=2)

print("[CROVIA] ledger status updated")
