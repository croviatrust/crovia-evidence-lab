#!/usr/bin/env python3
"""
Crovia Badge Generator v1.0.0
=============================

Generates dynamic SVG badges for AI model trust scores.
Embeddable anywhere - the "shields.io" for AI Trust.

Usage:
    python badge_generator.py --model "meta-llama/Llama-3-8B"
    python badge_generator.py --all  # Generate for all analyzed models

Output:
    badges/meta-llama__Llama-3-8B.svg

Author: Crovia Engineering
License: Apache-2.0
"""

import json
import hashlib
from pathlib import Path
from datetime import datetime, timezone
from typing import Dict, Any, Optional, List

# Paths
ROOT = Path(__file__).parent.parent.parent
EVIDENCE = ROOT / "EVIDENCE.json"
RANKING = ROOT / "v0.1" / "global_ranking.jsonl"
CARDS_DIR = ROOT / "cards"
BADGES_DIR = ROOT / "badges"
CANON = ROOT / "canon" / "necessities.v1.yaml"

# Badge colors
COLORS = {
    "GOLD": "#F59E0B",
    "SILVER": "#94A3B8", 
    "BRONZE": "#D97706",
    "UNVERIFIED": "#EF4444",
    "CLEAN": "#22C55E",
}

# SVG Template - Clean, professional design
SVG_TEMPLATE = '''<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="28" viewBox="0 0 {width} 28">
  <defs>
    <linearGradient id="bg" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" style="stop-color:#1a1a2e"/>
      <stop offset="100%" style="stop-color:#16161a"/>
    </linearGradient>
    <filter id="shadow">
      <feDropShadow dx="0" dy="1" stdDeviation="1" flood-opacity="0.3"/>
    </filter>
  </defs>
  <rect width="{width}" height="28" rx="6" fill="url(#bg)" filter="url(#shadow)"/>
  <rect x="1" y="1" width="{width_inner}" height="26" rx="5" fill="none" stroke="#333" stroke-width="1"/>
  
  <!-- Crovia Logo Section -->
  <rect x="0" y="0" width="70" height="28" rx="6" fill="#8B5CF6"/>
  <text x="35" y="18" font-family="system-ui,-apple-system,sans-serif" font-size="11" font-weight="700" fill="white" text-anchor="middle">CROVIA</text>
  
  <!-- Score Section -->
  <rect x="70" y="0" width="50" height="28" fill="{score_bg}"/>
  <text x="95" y="18" font-family="system-ui,-apple-system,sans-serif" font-size="12" font-weight="700" fill="white" text-anchor="middle">{score}</text>
  
  <!-- Badge Section -->
  <text x="135" y="18" font-family="system-ui,-apple-system,sans-serif" font-size="10" font-weight="600" fill="{badge_color}" text-anchor="start">{badge}</text>
  
  <!-- Violations (if any) -->
  <text x="{viol_x}" y="18" font-family="monospace" font-size="9" fill="#9CA3AF" text-anchor="start">{violations}</text>
</svg>'''

# Compact badge for inline use
SVG_COMPACT = '''<svg xmlns="http://www.w3.org/2000/svg" width="120" height="20" viewBox="0 0 120 20">
  <rect width="120" height="20" rx="4" fill="#1a1a2e"/>
  <rect x="0" y="0" width="50" height="20" rx="4" fill="#8B5CF6"/>
  <text x="25" y="14" font-family="system-ui" font-size="10" font-weight="700" fill="white" text-anchor="middle">CROVIA</text>
  <circle cx="65" cy="10" r="5" fill="{badge_color}"/>
  <text x="95" y="14" font-family="system-ui" font-size="11" font-weight="600" fill="white" text-anchor="middle">{score}</text>
</svg>'''


def load_evidence() -> Dict[str, Any]:
    """Load main evidence file."""
    if EVIDENCE.exists():
        with open(EVIDENCE, 'r', encoding='utf-8') as f:
            return json.load(f)
    return {}


def load_rankings() -> List[Dict[str, Any]]:
    """Load ranking data."""
    rankings = []
    if RANKING.exists():
        with open(RANKING, 'r', encoding='utf-8') as f:
            for line in f:
                try:
                    rankings.append(json.loads(line))
                except:
                    pass
    return rankings


def compute_shadow_score(violations: List[str]) -> int:
    """Compute shadow score from violations."""
    severity_map = {
        "NEC#1": 75, "NEC#2": 80, "NEC#7": 45,
        "NEC#10": 40, "NEC#13": 70, "NEC#14": 35,
        "NEC#5": 30, "NEC#15": 25, "NEC#18": 20, "NEC#11": 15
    }
    total = sum(severity_map.get(v, 30) for v in violations)
    return max(0, min(100, 100 - int(total * 0.15)))


def get_badge(score: int) -> tuple:
    """Get badge name and color from score."""
    if score >= 90:
        return "GOLD", COLORS["GOLD"]
    elif score >= 75:
        return "SILVER", COLORS["SILVER"]
    elif score >= 60:
        return "BRONZE", COLORS["BRONZE"]
    else:
        return "UNVERIFIED", COLORS["UNVERIFIED"]


def generate_badge_svg(
    model_id: str,
    score: int,
    violations: List[str],
    compact: bool = False
) -> str:
    """Generate SVG badge for a model."""
    badge_name, badge_color = get_badge(score)
    
    if compact:
        return SVG_COMPACT.format(
            score=score,
            badge_color=badge_color
        )
    
    # Full badge
    viol_str = " ".join(violations[:3]) if violations else "CLEAN"
    
    # Calculate width based on content
    base_width = 180
    extra = len(viol_str) * 5
    width = base_width + extra
    
    return SVG_TEMPLATE.format(
        width=width,
        width_inner=width - 2,
        score=score,
        score_bg=badge_color,
        badge=badge_name,
        badge_color=badge_color,
        viol_x=175,
        violations=viol_str
    )


def generate_oracle_card(model_id: str, violations: List[str]) -> Dict[str, Any]:
    """Generate Oracle Card JSON for a model."""
    score = compute_shadow_score(violations)
    badge_name, badge_color = get_badge(score)
    
    # Severity
    if not violations:
        severity = "CLEAN"
    elif score >= 75:
        severity = "LOW"
    elif score >= 60:
        severity = "MEDIUM"
    elif score >= 40:
        severity = "HIGH"
    else:
        severity = "CRITICAL"
    
    return {
        "schema": "crovia_oracle_card.v1",
        "model_id": model_id,
        "shadow_score": score,
        "badge": badge_name,
        "badge_color": badge_color,
        "severity": severity,
        "violations": violations,
        "violation_count": len(violations),
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "evidence_hash": hashlib.sha256(f"{model_id}:{score}".encode()).hexdigest()[:16],
        "oracle_version": "2.0.0"
    }


def save_badge(model_id: str, svg: str, compact: bool = False):
    """Save badge SVG to file."""
    BADGES_DIR.mkdir(exist_ok=True)
    filename = model_id.replace("/", "__")
    if compact:
        filename += "_compact"
    filepath = BADGES_DIR / f"{filename}.svg"
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(svg)
    return filepath


def save_oracle_card(model_id: str, card: Dict[str, Any]):
    """Save Oracle Card JSON."""
    CARDS_DIR.mkdir(exist_ok=True)
    filename = model_id.replace("/", "__") + ".json"
    filepath = CARDS_DIR / filename
    with open(filepath, 'w', encoding='utf-8') as f:
        json.dump(card, f, indent=2, ensure_ascii=False)
    return filepath


def generate_all_from_evidence():
    """Generate badges and cards for all models in evidence."""
    evidence = load_evidence()
    top_omissions = evidence.get("top_omissions", [])
    
    # Map NEC# to models (simplified - in real system would have model mappings)
    # For now, generate example badges
    example_models = [
        ("meta-llama/Llama-3-8B", ["NEC#1", "NEC#2"]),
        ("mistralai/Mistral-7B-v0.3", ["NEC#7"]),
        ("google/gemma-2-9b", []),
        ("microsoft/Phi-3-mini-4k", ["NEC#13"]),
        ("bigscience/bloom", ["NEC#1", "NEC#2", "NEC#7"]),
    ]
    
    generated = []
    for model_id, violations in example_models:
        # Generate card
        card = generate_oracle_card(model_id, violations)
        card_path = save_oracle_card(model_id, card)
        
        # Generate badges
        svg_full = generate_badge_svg(model_id, card["shadow_score"], violations)
        svg_compact = generate_badge_svg(model_id, card["shadow_score"], violations, compact=True)
        
        badge_path = save_badge(model_id, svg_full)
        save_badge(model_id, svg_compact, compact=True)
        
        generated.append({
            "model_id": model_id,
            "score": card["shadow_score"],
            "badge": card["badge"],
            "card_path": str(card_path),
            "badge_path": str(badge_path)
        })
        
        print(f"✓ {model_id}: {card['shadow_score']}/100 {card['badge']}")
    
    # Generate index
    index = {
        "schema": "crovia_badges_index.v1",
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "count": len(generated),
        "badges": generated
    }
    
    with open(BADGES_DIR / "index.json", 'w', encoding='utf-8') as f:
        json.dump(index, f, indent=2)
    
    print(f"\n✅ Generated {len(generated)} badges and cards")
    return generated


if __name__ == "__main__":
    import sys
    
    print("=" * 50)
    print("CROVIA BADGE GENERATOR v1.0.0")
    print("=" * 50)
    
    if "--all" in sys.argv or len(sys.argv) == 1:
        generate_all_from_evidence()
    elif "--model" in sys.argv:
        idx = sys.argv.index("--model")
        if idx + 1 < len(sys.argv):
            model_id = sys.argv[idx + 1]
            # Would fetch real data from HF API
            card = generate_oracle_card(model_id, ["NEC#1"])
            save_oracle_card(model_id, card)
            svg = generate_badge_svg(model_id, card["shadow_score"], ["NEC#1"])
            save_badge(model_id, svg)
            print(f"Generated badge for {model_id}")
