#!/usr/bin/env python3
import json
from pathlib import Path
from datetime import datetime, timezone
from huggingface_hub import HfApi

WATCHLIST = Path("open/canon/targets_watchlist.jsonl")
WATCHLIST.parent.mkdir(parents=True, exist_ok=True)

api = HfApi()

# How many to fetch (tunable)
LIMIT = 120

# Pull public datasets from HF (broad, neutral)
datasets = api.list_datasets(limit=LIMIT)

# Load existing hints to avoid duplicates
existing = set()
if WATCHLIST.exists():
    with WATCHLIST.open("r", encoding="utf-8") as f:
        for line in f:
            try:
                o = json.loads(line)
                existing.add(o.get("project_hint"))
            except Exception:
                pass

now = datetime.now(timezone.utc).isoformat()
added = 0

with WATCHLIST.open("a", encoding="utf-8") as f:
    for d in datasets:
        did = getattr(d, "id", None)
        if not did:
            continue
        hint = f"hf:dataset:{did}"
        if hint in existing:
            continue
        row = {
            "source": "hf",
            "ref": "datasets/list",
            "project_hint": hint,
            "note": "public dataset"
        }
        f.write(json.dumps(row, ensure_ascii=False) + "\n")
        existing.add(hint)
        added += 1

print(f"[CROVIA] hf targets appended: {added}")
