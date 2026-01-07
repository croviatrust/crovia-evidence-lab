#!/usr/bin/env bash
set -euo pipefail

HERE="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
DATE=""
RUN_ID=""

usage() {
  echo "Usage: $0 --date YYYY-MM-DD"
  exit 1
}

while [[ $# -gt 0 ]]; do
  case "$1" in
    --date) DATE="${2:-}"; shift 2;;
    *) usage;;
  esac
done

[[ -n "$DATE" ]] || usage

RUN_ID="CEPT_$(date -u +%Y%m%dT%H%M%SZ)"
BASE="$HERE/runs/$DATE"

mkdir -p "$BASE"/{sources,tmp,logs,records,proofs,meta}

echo "$RUN_ID" > "$BASE/meta/RUN_ID.txt"
date -u +"%Y-%m-%dT%H:%M:%SZ" > "$BASE/meta/CREATED_AT_UTC.txt"

# Requirements
command -v curl >/dev/null 2>&1 || { echo "curl missing"; exit 1; }
command -v w3m  >/dev/null 2>&1 || { echo "w3m missing (apt-get install w3m)"; exit 1; }
command -v pdftotext >/dev/null 2>&1 || { echo "poppler-utils missing (apt-get install poppler-utils)"; exit 1; }
command -v jq >/dev/null 2>&1 || { echo "jq missing (apt-get install jq)"; exit 1; }
command -v python3 >/dev/null 2>&1 || { echo "python3 missing"; exit 1; }

# Official sources list (closed list)
cat > "$BASE/sources/sources_official.tsv" <<'TSV'
#kind	id	url
dataset	LAION-5B	https://laion.ai/blog/laion-5b/
datasetrepo	LAION-5B	https://github.com/LAION-AI/laion5b
dataset	CommonCrawl	https://commoncrawl.org/the-data/
datasetroot	CommonCrawl	https://commoncrawl.org

modelcard	LLaMA-2	https://ai.meta.com/llama/
paper	LLaMA-2	https://arxiv.org/abs/2307.09288

modelpage	GPT-4	https://openai.com/research/gpt-4
systemcard	GPT-4	https://cdn.openai.com/papers/gpt-4-system-card.pdf
policy	OpenAI	https://openai.com/transparency
TSV

# Fetch sources
while IFS=$'\t' read -r kind id url; do
  [[ -z "$kind" || "$kind" =~ ^# ]] && continue
  safe_id="$(echo "$id" | tr ' /' '__')"
  ext="html"
  [[ "$url" =~ \.pdf($|\?) ]] && ext="pdf"
  out="$BASE/sources/${kind}__${safe_id}.${ext}"
  echo "[GET] $kind $id -> $url"
  curl -L --max-time 60 -A "crovia-cept/0.1" -o "$out" "$url" || echo "[WARN] download failed: $url"
done < "$BASE/sources/sources_official.tsv"

# Extract text
for f in "$BASE"/sources/*.html "$BASE"/sources/*.htm; do
  [[ -f "$f" ]] || continue
  w3m -dump "$f" > "$BASE/tmp/$(basename "$f").txt"
done 2>/dev/null

for f in "$BASE"/sources/*.pdf; do
  [[ -f "$f" ]] || continue
  pdftotext "$f" "$BASE/tmp/$(basename "$f").txt"
done 2>/dev/null

# Terms
cat > "$BASE/meta/terms.txt" <<'TERMS'
LAION
LAION-5B
Common Crawl
commoncrawl
crawl
WARC
WET
dataset
training data
data sources
TERMS

# Observation log (NDJSON with snippets)
export BASE="$BASE"
python3 - <<'PY'
import glob, json, os, re, datetime

base = os.environ["BASE"]
terms_path = f"{base}/meta/terms.txt"
out_path   = f"{base}/logs/observation_log.ndjson"

terms = [t.strip() for t in open(terms_path, "r", encoding="utf-8") if t.strip()]
files = sorted(glob.glob(f"{base}/tmp/*.txt"))

def snippets(text, term, limit=3, ctx=70):
    hits=[]
    for m in re.finditer(re.escape(term), text, flags=re.IGNORECASE):
        a=max(0, m.start()-ctx); b=min(len(text), m.end()+ctx)
        hits.append(text[a:b].replace("\n"," "))
        if len(hits)>=limit: break
    return hits

now = datetime.datetime.now(datetime.timezone.utc).isoformat().replace("+00:00","Z")
os.makedirs(os.path.dirname(out_path), exist_ok=True)

with open(out_path, "w", encoding="utf-8") as out:
    for fp in files:
        text = open(fp, "r", encoding="utf-8", errors="replace").read()
        rec = {
            "schema": "crovia.observation_log.v1",
            "observed_at": now,
            "source_file": os.path.basename(fp),
            "terms": []
        }
        lower = text.lower()
        for term in terms:
            rec["terms"].append({
                "term": term,
                "found": term.lower() in lower,
                "snippets": snippets(text, term)
            })
        out.write(json.dumps(rec, ensure_ascii=False) + "\n")

print("[OK] files scanned:", len(files))
PY

# Build derived records
python3 - <<'PY'
import json, os, datetime

base = os.environ["BASE"]
log_path = f"{base}/logs/observation_log.ndjson"
out_dir  = f"{base}/records"
os.makedirs(out_dir, exist_ok=True)

rows=[json.loads(l) for l in open(log_path) if l.strip()]

MODEL_FILES = {
    "LLaMA-2": ["modelcard__LLaMA-2", "paper__LLaMA-2"],
    "GPT-4":   ["modelpage__GPT-4", "systemcard__GPT-4", "policy__OpenAI"],
}
DATASET_TARGETS = {
    "LAION-5B": ["LAION", "LAION-5B"],
    "Common Crawl": ["Common Crawl", "commoncrawl"],
}
now = datetime.datetime.now(datetime.timezone.utc).isoformat().replace("+00:00","Z")

def belongs(source_file, prefixes):
    return any(source_file.startswith(p) for p in prefixes)

def build_record(model_id, provider, model_type, dataset_id):
    prefixes = MODEL_FILES[model_id]
    targets  = DATASET_TARGETS[dataset_id]
    sources_checked=[]
    evidence_found=False

    for r in rows:
        if not belongs(r["source_file"], prefixes):
            continue
        found=[t["term"] for t in r["terms"] if t["term"] in targets and t["found"]]
        sources_checked.append({"source_file": r["source_file"], "found_terms": found})
        if found:
            evidence_found=True

    return {
        "schema": "crovia.evidence_presence.v1",
        "observed_at": now,
        "observer": {"engine":"crovia-manual-run","mode":"public_observation_only"},
        "model": {"id":model_id,"provider":provider,"type":model_type},
        "dataset": {"id":dataset_id,"category":"public_core"},
        "evidence": {"present": evidence_found, "independently_verifiable": False},
        "sources_checked": sources_checked,
        "claims": {"training_inferred": False, "intent_inferred": False, "compliance_inferred": False}
    }

pairs = [
    ("LLaMA-2","Meta","open","LAION-5B","llama2__laion5b.json"),
    ("GPT-4","OpenAI","closed","LAION-5B","gpt4__laion5b.json"),
    ("LLaMA-2","Meta","open","Common Crawl","llama2__commoncrawl.json"),
    ("GPT-4","OpenAI","closed","Common Crawl","gpt4__commoncrawl.json"),
]

for mid, prov, mtype, ds, fname in pairs:
    rec = build_record(mid, prov, mtype, ds)
    with open(os.path.join(out_dir, fname), "w", encoding="utf-8") as f:
        json.dump(rec, f, ensure_ascii=False, indent=2)

print("[OK] records:", len(pairs))
PY

# Canon NDJSON
cat "$BASE/records/"*.json | jq -c . > "$BASE/records/evidence_records.ndjson"

# Seal: hash-chains
python3 "$HERE/vendor/hashchain_writer.py" --source "$BASE/logs/observation_log.ndjson" --out "$BASE/proofs/hashchain_observation_log.txt" --chunk 200
python3 "$HERE/vendor/hashchain_writer.py" --source "$BASE/records/evidence_records.ndjson" --out "$BASE/proofs/hashchain_evidence_records.txt" --chunk 50

# Sign records (demo key)
: "${CROVIA_HMAC_KEY:=demo-key-do-not-use-in-prod}"
export CROVIA_HMAC_KEY
python3 "$HERE/vendor/sign_receipts_hmac.py" --in "$BASE/records/evidence_records.ndjson" --out "$BASE/records/evidence_records.signed.ndjson" --env CROVIA_HMAC_KEY

# MANIFEST sha256
sha256sum \
  "$BASE/sources/"* \
  "$BASE/tmp/"* \
  "$BASE/logs/observation_log.ndjson" \
  "$BASE/records/evidence_records.ndjson" \
  "$BASE/records/evidence_records.signed.ndjson" \
  "$BASE/proofs/hashchain_observation_log.txt" \
  "$BASE/proofs/hashchain_evidence_records.txt" \
  > "$BASE/proofs/MANIFEST.sha256"

# Run index
cat > "$BASE/meta/run_index.json" <<RUNEOF
{
  "schema": "crovia.cept_run_index.v1",
  "run_id": "$(cat "$BASE/meta/RUN_ID.txt")",
  "created_at_utc": "$(cat "$BASE/meta/CREATED_AT_UTC.txt")",
  "results": { "pairs_total": 4 },
  "artifacts": {
    "observation_log": "logs/observation_log.ndjson",
    "records_canon": "records/evidence_records.ndjson",
    "records_signed": "records/evidence_records.signed.ndjson",
    "hashchain_log": "proofs/hashchain_observation_log.txt",
    "hashchain_records": "proofs/hashchain_evidence_records.txt",
    "manifest_sha256": "proofs/MANIFEST.sha256",
    "sources_dir": "sources/",
    "extracted_text_dir": "tmp/"
  }
}
RUNEOF

echo "[DONE] CEPT run created at: $BASE"
