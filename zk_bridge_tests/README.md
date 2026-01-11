# CROVIA ZK-Bridge Evidence Tests
=================================

Test reali del ZK-Bridge con modelli e dataset reali.

## Test Cases

### 1. Compliance Preview Test
```bash
# Test con modello reale
crovia bridge preview meta-llama/Llama-3-8B

# Expected: Score 40-60% → 90-95% con PRO
```

### 2. Evidence Generation Test
```python
# Test con dati reali
from croviapro.zk_bridge import UniversalEvidenceGenerator

generator = create_evidence_generator(use_turbo=True)
evidence = generator.generate_universal_evidence_pack(
    model_id="test-model-2025",
    training_data=["hash1", "hash2", "hash3"],
    opt_out_data=["copyright1", "copyright2"],
    architecture_info={"layers": 12, "params": "7B"},
    provider_info=[{"id": "provider1", "type": "data"}]
)
```

### 3. Global Standards Test
```python
# Test mapping standard globali
from croviapro.zk_bridge.global_standards import get_regulation_registry

registry = get_regulation_registry()
frameworks = get_supported_frameworks()
requirements = get_universal_requirements_for_frameworks(frameworks)
```

## Results Documentation

I risultati dei test vengono documentati qui:
- `results/compliance_scores.json` - Score per modello testati
- `results/evidence_packs/` - Evidence packs generati
- `results/global_coverage/` - Copertura per regolamentazione

## Validation Criteria

✅ **Pass Criteria:**
- Compliance preview funziona per tutti i modelli
- Evidence generation completa senza errori
- Global standards mapping copre 5+ regolamentazioni
- Bridge commands CLI funzionanti

❌ **Fail Criteria:**
- Import errors o missing dependencies
- Evidence generation fallisce
- Score calculation errato
- CLI commands non funzionano
