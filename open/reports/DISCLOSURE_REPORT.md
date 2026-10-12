# 📊 Crovia Disclosure Transparency Report

> **Week 2026-W42** | Generated 2026-10-12 10:28:15 UTC
>
> *This is observational data only. No inference, judgment, or accusation.*

---

## 📈 Coverage

| Metric | Value |
|--------|-------|
| **Targets Monitored** | 8829 |
| Models | 7954 |
| Datasets | 875 |

---

## 🔍 Disclosure Observations

| Field | Present | Absent | % Present |
|-------|---------|--------|-----------|
| **Training Section** | 1598 | 7231 | **18.1%** |
| **Declared Datasets** | 1944 | 6885 | **22.0%** |
| **License** | 6328 | 2501 | **71.7%** |
| **README Accessible** | 7267 | 1562 | **82.3%** |

---

## 📥 Popularity Observations

- **Targets with download data:** 7754
- **Gated targets:** 329 (3.7%)

### Top Targets by Downloads

| Target | Type | Downloads | Training Section | Declared Datasets |
|--------|------|-----------|------------------|-------------------|
| `sentence-transformers/all-MiniLM-L6-v2` | model | **221.2M** | PRESENT | 21 |
| `cross-encoder/ms-marco-MiniLM-L6-v2` | model | **79.5M** | ABSENT | 1 |
| `BAAI/bge-small-en-v1.5` | model | **60.1M** | ABSENT | 0 |
| `sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2` | model | **48.0M** | ABSENT | 0 |
| `google/electra-base-discriminator` | model | **45.3M** | ABSENT | 0 |
| `google-bert/bert-base-uncased` | model | **34.8M** | PRESENT | 2 |
| `BAAI/bge-m3` | model | **32.9M** | PRESENT | 0 |
| `Qwen/Qwen3-0.6B` | model | **30.6M** | ABSENT | 0 |
| `google-t5/t5-small` | model | **23.8M** | PRESENT | 1 |
| `Comfy-Org/MiniMax-H3` | model | **23.6M** | ABSENT | 0 |

### High-Download Targets Without Training Section

*Factual observation: these targets have >10K downloads and no detected training section.*

| Target | Downloads | README |
|--------|-----------|--------|
| `cross-encoder/ms-marco-MiniLM-L6-v2` | **79.5M** | OK |
| `BAAI/bge-small-en-v1.5` | **60.1M** | OK |
| `sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2` | **48.0M** | OK |
| `google/electra-base-discriminator` | **45.3M** | OK |
| `Qwen/Qwen3-0.6B` | **30.6M** | OK |
| `Comfy-Org/MiniMax-H3` | **23.6M** | OK |
| `timm/mobilenetv3_small_100.lamb_in1k` | **21.2M** | OK |
| `openai/clip-vit-base-patch32` | **19.0M** | OK |
| `BAAI/bge-reranker-v2-m3` | **16.2M** | OK |
| `jonatasgrosman/wav2vec2-large-xlsr-53-japanese` | **15.7M** | OK |

---

## 🏢 By Organization

| Organization | Targets | Training Section | Declared Datasets | License |
|--------------|---------|------------------|-------------------|---------|
| **mradermacher** | 238 | 0 (0%) | 71 (30%) | 197 (83%) |
| **facebook** | 185 | 25 (14%) | 74 (40%) | 175 (95%) |
| **Qwen** | 179 | 4 (2%) | 0 (0%) | 176 (98%) |
| **google** | 170 | 61 (36%) | 47 (28%) | 161 (95%) |
| **nvidia** | 160 | 88 (55%) | 60 (38%) | 152 (95%) |
| **microsoft** | 143 | 44 (31%) | 20 (14%) | 119 (83%) |
| **allenai** | 130 | 6 (5%) | 76 (58%) | 109 (84%) |
| **openbmb** | 116 | 5 (4%) | 43 (37%) | 80 (69%) |
| **tiiuae** | 112 | 22 (20%) | 21 (19%) | 104 (93%) |
| **Salesforce** | 111 | 32 (29%) | 20 (18%) | 108 (97%) |
| **EleutherAI** | 109 | 84 (77%) | 100 (92%) | 106 (97%) |
| **BAAI** | 109 | 11 (10%) | 19 (17%) | 102 (94%) |
| **apple** | 106 | 20 (19%) | 15 (14%) | 106 (100%) |
| **internlm** | 106 | 1 (1%) | 22 (21%) | 102 (96%) |
| **bigscience** | 105 | 15 (14%) | 23 (22%) | 41 (39%) |

---

## 📉 Drift Observations

| Metric | Value |
|--------|-------|
| **Changes (7 days)** | 95 |
| **Changes (30 days)** | 284 |
| **Targets with changes** | 233 |

---

## ℹ️ Methodology

This report aggregates publicly observable data from HuggingFace:

- **Training Section**: Detected via `## Training` heading in README
- **Declared Datasets**: From `cardData.datasets` in model/dataset card
- **License**: From `cardData.license`
- **Downloads/Likes**: From HuggingFace API

**What this report does NOT do:**
- Make accusations
- Infer compliance or non-compliance
- Judge quality or intent
- Assign scores or rankings

---

*Report fingerprint: `22056f9d4bce9a09...`*

*Source: [Crovia Training Provenance Registry](https://registry.croviatrust.com)*