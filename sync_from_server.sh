#!/usr/bin/env bash
# ============================================================================
# sync_from_server.sh — Auto-push fresh evidence to GitHub
# Runs hourly on Hetzner, triggered after autonomous_observer completes
#
# What it syncs:
#   open/         → observations, drift, forensic, reports
#   snapshots/    → latest registry state (JSON)
#   badges/       → SVG trust badges
#   cep-capsules/ → cryptographic evidence packages
#
# Requires: GITHUB_TOKEN in /etc/crovia/tpr.env
# ============================================================================
set -eu

EVIDENCE_LAB="/opt/crovia/repos/crovia-evidence-lab"
HF_DATASET="/opt/crovia/hf_datasets/global-ai-training-omissions"
PRO_ENGINE="/opt/crovia/CROVIA_DEV/crovia-pro-engine"
LOG="/var/log/crovia/evidence_lab_sync.log"
TIMESTAMP=$(date -u +"%Y-%m-%dT%H:%M:%SZ")

log() { echo "[${TIMESTAMP}] $*" >> "${LOG}"; }

log "=== EVIDENCE LAB SYNC START ==="

# Load env
set -a; source /etc/crovia/tpr.env 2>/dev/null || true; set +a

# Ensure repo exists
if [ ! -d "${EVIDENCE_LAB}/.git" ]; then
    log "ERROR: evidence-lab repo not found at ${EVIDENCE_LAB}"
    exit 1
fi

cd "${EVIDENCE_LAB}"

# Pull latest to avoid conflicts
git pull --rebase --autostash origin main >> "${LOG}" 2>&1 || true

# ---- Sync open/ data ----
mkdir -p open/{drift,forensic,reports,canon,signal,temporal}

# Drift snapshots
cp -f "${HF_DATASET}/open/drift/"*.jsonl open/drift/ 2>/dev/null || true

# Forensic receipts
cp -f "${HF_DATASET}/open/forensic/"*.jsonl open/forensic/ 2>/dev/null || true
cp -f "${HF_DATASET}/open/forensic/"*.json open/forensic/ 2>/dev/null || true

# Reports
cp -f "${HF_DATASET}/open/reports/"*.json open/reports/ 2>/dev/null || true
cp -f "${HF_DATASET}/open/reports/"*.md open/reports/ 2>/dev/null || true

# Canon watchlist
cp -f "${HF_DATASET}/open/canon/"*.jsonl open/canon/ 2>/dev/null || true

# Signal
cp -f "${HF_DATASET}/open/signal/"*.jsonl open/signal/ 2>/dev/null || true

# Temporal
cp -f "${HF_DATASET}/open/temporal/"*.jsonl open/temporal/ 2>/dev/null || true

# ---- Sync snapshots ----
mkdir -p snapshots
# Export latest stats from registry API (try local nginx first, then direct backend)
curl -sf http://127.0.0.1:8080/api/registry/stats > snapshots/registry_stats.json 2>/dev/null \
    || curl -sf http://localhost:8000/api/registry/stats > snapshots/registry_stats.json 2>/dev/null || true
curl -sf http://127.0.0.1:8080/api/registry/merkle > snapshots/merkle_proof.json 2>/dev/null \
    || curl -sf http://localhost:8000/api/registry/merkle > snapshots/merkle_proof.json 2>/dev/null || true
curl -sf http://127.0.0.1:8080/api/registry/recent > snapshots/recent_observations.json 2>/dev/null \
    || curl -sf http://localhost:8000/api/registry/recent > snapshots/recent_observations.json 2>/dev/null || true

# Global ranking
cp -f "${HF_DATASET}/global_ranking.json" snapshots/ 2>/dev/null || true
cp -f "${HF_DATASET}/snapshot_latest.json" snapshots/ 2>/dev/null || true

# ---- Sync badges ----
mkdir -p badges
cp -f "${HF_DATASET}/badges/"*.svg badges/ 2>/dev/null || true

# ---- Sync CEP capsules ----
mkdir -p cep-capsules
cp -f "${HF_DATASET}/cep-capsules/"*.json cep-capsules/ 2>/dev/null || true

# ---- Generate summary ----
OBS_COUNT=$(python3 -c "
import json, sys
try:
    d = json.load(open('snapshots/registry_stats.json'))
    print(d.get('total_observations', '?'))
except: print('?')
" 2>/dev/null || echo "?")

TARGETS_COUNT=$(python3 -c "
import json, sys
try:
    d = json.load(open('snapshots/registry_stats.json'))
    print(d.get('unique_targets', '?'))
except: print('?')
" 2>/dev/null || echo "?")

# Update sync timestamp
cat > SYNC_STATUS.json << EOF
{
  "last_sync": "${TIMESTAMP}",
  "total_observations": "${OBS_COUNT}",
  "unique_targets": "${TARGETS_COUNT}",
  "source": "hetzner_observer",
  "sync_method": "auto_hourly"
}
EOF

log "Synced: ${OBS_COUNT} observations, ${TARGETS_COUNT} targets"

# ---- Commit and push ----
git add -A
if git diff --cached --quiet; then
    log "No changes to push"
else
    git commit -m "auto-sync: ${OBS_COUNT} obs, ${TARGETS_COUNT} targets [${TIMESTAMP}]" >> "${LOG}" 2>&1
    git push origin main >> "${LOG}" 2>&1
    log "Pushed to GitHub"
fi

log "=== EVIDENCE LAB SYNC DONE ==="
