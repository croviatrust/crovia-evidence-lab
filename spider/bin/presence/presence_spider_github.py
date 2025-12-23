import json
import os
import time
import hashlib
import requests
from datetime import datetime, timezone

# ---------------------------------------------------------------------
# CROVIA · Presence Spider (GitHub)
# Passive presence / absence observer
# ---------------------------------------------------------------------

REPOS = [
    "croviatrust/crovia-wedge",
    "croviatrust/crovia-core-engine",
    "huggingface/transformers",
    "openai/evals",
    "mlflow/mlflow",
    "pytorch/pytorch",
    "tensorflow/tensorflow",
]

ARTEFACTS = [
    "EVIDENCE.pointer.json",
    "EVIDENCE.json",
    "trust_bundle.v1.json",
    "cep_capsule.v1.json",
    "gaps/gap_index.jsonl",
]

OUT_RAW = "raw/presence/github_presence_raw.jsonl"
OUT_DATA = "data/presence/github_presence_v1.jsonl"

HEADERS = {
    "User-Agent": "CroviaPresenceSpider/1.0 (passive; open-data)"
}

# ---------------------------------------------------------------------

def now():
    return datetime.now(timezone.utc).isoformat()

def project_key(repo: str) -> str:
    # Internal stable key (OPEN plane will be salted later)
    return hashlib.sha256(repo.encode()).hexdigest()[:16]

def fetch_tree(repo: str):
    url = f"https://api.github.com/repos/{repo}/git/trees/HEAD?recursive=1"
    r = requests.get(url, headers=HEADERS, timeout=20)
    if r.status_code != 200:
        return None, r.status_code
    return r.json(), 200

# ---------------------------------------------------------------------

os.makedirs("raw/presence", exist_ok=True)
os.makedirs("data/presence", exist_ok=True)

with open(OUT_RAW, "a", encoding="utf-8") as raw_f, open(OUT_DATA, "a", encoding="utf-8") as data_f:
    for repo in REPOS:
        print(f"[PRESENCE] scanning {repo}")
        tree, status = fetch_tree(repo)

        artefacts_found = []
        verdict = "RED"

        if tree and "tree" in tree:
            paths = [x.get("path", "") for x in tree["tree"]]
            for a in ARTEFACTS:
                if a in paths:
                    artefacts_found.append(a)

            if artefacts_found:
                verdict = "GREEN"

        raw_entry = {
            "schema": "crovia.presence.raw.v1",
            "ts": now(),
            "repo": repo,
            "http_status": status,
            "artefacts_found": artefacts_found,
            "verdict": verdict,
        }

        data_entry = {
            "schema": "crovia.presence.v1",
            "ts": raw_entry["ts"],
            "project_key": project_key(repo),
            "verdict": verdict,
            "artefacts": artefacts_found,
        }

        raw_f.write(json.dumps(raw_entry) + "\n")
        data_f.write(json.dumps(data_entry) + "\n")

        time.sleep(2)

print("[PRESENCE] scan complete")
