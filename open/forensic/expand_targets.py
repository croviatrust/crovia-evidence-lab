#!/usr/bin/env python3
import json
import hashlib
from datetime import datetime, timezone
from pathlib import Path

WATCHLIST = Path("open/canon/targets_watchlist.jsonl")
OUT = Path("open/signal/presence_latest.jsonl")

def key_for(hint: str) -> str:
    return hashlib.sha256(hint.encode("utf-8")).hexdigest()[:16]

now = datetime.now(timezone.utc).isoformat()

records = []
if OUT.exists():
    with OUT.open("r", encoding="utf-8") as f:
        for line in f:
            records.append(json.loads(line))

existing = {r["project_key"] for r in records}

new = []

with WATCHLIST.open("r", encoding="utf-8") as f:
    for line in f:
        o = json.loads(line)
        pk = key_for(o["project_hint"])
        if pk in existing:
            continue
        new.append({
            "schema": "crovia.open.presence.v1",
            "ts": now,
            "project_key": pk,
            "verdict": "RED",
            "artefacts": []
        })

if new:
    with OUT.open("a", encoding="utf-8") as f:
        for r in new:
            f.write(json.dumps(r) + "\n")

print(f"[CROVIA] targets added: {len(new)}")
