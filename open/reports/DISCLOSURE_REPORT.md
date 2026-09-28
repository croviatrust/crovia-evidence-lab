# 📊 Crovia Disclosure Transparency Report

> **Week 2026-W40** | Generated 2026-09-28 12:19:40 UTC
>
> *This is observational data only. No inference, judgment, or accusation.*

---

## 📈 Coverage

| Metric | Value |
|--------|-------|
| **Targets Monitored** | 8844 |
| Models | 7961 |
| Datasets | 883 |

---

## 🔍 Disclosure Observations

| Field | Present | Absent | % Present |
|-------|---------|--------|-----------|
| **Training Section** | 1605 | 7239 | **18.1%** |
| **Declared Datasets** | 1956 | 6888 | **22.1%** |
| **License** | 6320 | 2524 | **71.5%** |
| **README Accessible** | 7270 | 1574 | **82.2%** |

---

## 📥 Popularity Observations

- **Targets with download data:** 7767
- **Gated targets:** 333 (3.8%)

### Top Targets by Downloads

| Target | Type | Downloads | Training Section | Declared Datasets |
|--------|------|-----------|------------------|-------------------|
| `sentence-transformers/all-MiniLM-L6-v2` | model | **242.7M** | PRESENT | 21 |
| `cross-encoder/ms-marco-MiniLM-L6-v2` | model | **86.5M** | ABSENT | 1 |
| `BAAI/bge-small-en-v1.5` | model | **63.3M** | ABSENT | 0 |
| `google/electra-base-discriminator` | model | **46.3M** | ABSENT | 0 |
| `sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2` | model | **45.5M** | ABSENT | 0 |
| `google-bert/bert-base-uncased` | model | **41.7M** | PRESENT | 2 |
| `BAAI/bge-m3` | model | **36.3M** | PRESENT | 0 |
| `Qwen/Qwen3-0.6B` | model | **29.3M** | ABSENT | 0 |
| `google-t5/t5-small` | model | **24.1M** | PRESENT | 1 |
| `Comfy-Org/MiniMax-H3` | model | **21.9M** | ABSENT | 0 |

### High-Download Targets Without Training Section

*Factual observation: these targets have >10K downloads and no detected training section.*

| Target | Downloads | README |
|--------|-----------|--------|
| `cross-encoder/ms-marco-MiniLM-L6-v2` | **86.5M** | OK |
| `BAAI/bge-small-en-v1.5` | **63.3M** | OK |
| `google/electra-base-discriminator` | **46.3M** | OK |
| `sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2` | **45.5M** | OK |
| `Qwen/Qwen3-0.6B` | **29.3M** | OK |
| `Comfy-Org/MiniMax-H3` | **21.9M** | OK |
| `openai/clip-vit-base-patch32` | **21.7M** | OK |
| `timm/mobilenetv3_small_100.lamb_in1k` | **20.3M** | OK |
| `Qwen/Qwen3-VL-8B-Instruct` | **18.0M** | OK |
| `FacebookAI/xlm-roberta-base` | **17.9M** | OK |

---

## 🏢 By Organization

| Organization | Targets | Training Section | Declared Datasets | License |
|--------------|---------|------------------|-------------------|---------|
| **mradermacher** | 237 | 0 (0%) | 70 (30%) | 196 (83%) |
| **facebook** | 190 | 26 (14%) | 75 (39%) | 179 (94%) |
| **Qwen** | 180 | 4 (2%) | 0 (0%) | 178 (99%) |
| **google** | 168 | 61 (36%) | 47 (28%) | 159 (95%) |
| **nvidia** | 160 | 88 (55%) | 61 (38%) | 152 (95%) |
| **microsoft** | 144 | 45 (31%) | 20 (14%) | 118 (82%) |
| **allenai** | 135 | 6 (4%) | 76 (56%) | 111 (82%) |
| **openbmb** | 115 | 4 (3%) | 42 (37%) | 79 (69%) |
| **tiiuae** | 112 | 22 (20%) | 21 (19%) | 104 (93%) |
| **Salesforce** | 111 | 32 (29%) | 20 (18%) | 108 (97%) |
| **EleutherAI** | 110 | 84 (76%) | 100 (91%) | 107 (97%) |
| **BAAI** | 109 | 11 (10%) | 19 (17%) | 102 (94%) |
| **apple** | 106 | 20 (19%) | 15 (14%) | 106 (100%) |
| **internlm** | 106 | 1 (1%) | 22 (21%) | 102 (96%) |
| **bigscience** | 105 | 15 (14%) | 23 (22%) | 41 (39%) |

---

## 📉 Drift Observations

| Metric | Value |
|--------|-------|
| **Changes (7 days)** | 80 |
| **Changes (30 days)** | 282 |
| **Targets with changes** | 223 |

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

*Report fingerprint: `2dd08ee53fe96f2f...`*

*Source: [Crovia Training Provenance Registry](https://registry.croviatrust.com)*