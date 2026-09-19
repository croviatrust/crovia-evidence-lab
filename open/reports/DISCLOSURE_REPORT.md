# 📊 Crovia Disclosure Transparency Report

> **Week 2026-W38** | Generated 2026-09-14 10:33:22 UTC
>
> *This is observational data only. No inference, judgment, or accusation.*

---

## 📈 Coverage

| Metric | Value |
|--------|-------|
| **Targets Monitored** | 8862 |
| Models | 7966 |
| Datasets | 896 |

---

## 🔍 Disclosure Observations

| Field | Present | Absent | % Present |
|-------|---------|--------|-----------|
| **Training Section** | 1608 | 7254 | **18.1%** |
| **Declared Datasets** | 1965 | 6897 | **22.2%** |
| **License** | 6266 | 2596 | **70.7%** |
| **README Accessible** | 7215 | 1645 | **81.4%** |

---

## 📥 Popularity Observations

- **Targets with download data:** 7783
- **Gated targets:** 328 (3.7%)

### Top Targets by Downloads

| Target | Type | Downloads | Training Section | Declared Datasets |
|--------|------|-----------|------------------|-------------------|
| `sentence-transformers/all-MiniLM-L6-v2` | model | **252.8M** | PRESENT | 21 |
| `cross-encoder/ms-marco-MiniLM-L6-v2` | model | **87.5M** | ABSENT | 1 |
| `BAAI/bge-small-en-v1.5` | model | **64.0M** | ABSENT | 0 |
| `google/electra-base-discriminator` | model | **59.0M** | ABSENT | 0 |
| `google-bert/bert-base-uncased` | model | **46.4M** | PRESENT | 2 |
| `sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2` | model | **45.4M** | ABSENT | 0 |
| `BAAI/bge-m3` | model | **37.6M** | PRESENT | 0 |
| `google-t5/t5-small` | model | **24.6M** | PRESENT | 1 |
| `sentence-transformers/all-mpnet-base-v2` | model | **23.5M** | PRESENT | 21 |
| `amazon/chronos-2` | model | **22.8M** | PRESENT | 2 |

### High-Download Targets Without Training Section

*Factual observation: these targets have >10K downloads and no detected training section.*

| Target | Downloads | README |
|--------|-----------|--------|
| `cross-encoder/ms-marco-MiniLM-L6-v2` | **87.5M** | OK |
| `BAAI/bge-small-en-v1.5` | **64.0M** | OK |
| `google/electra-base-discriminator` | **59.0M** | OK |
| `sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2` | **45.4M** | OK |
| `FacebookAI/xlm-roberta-base` | **21.9M** | OK |
| `openai/clip-vit-base-patch32` | **21.3M** | OK |
| `Qwen/Qwen3-0.6B` | **20.0M** | OK |
| `Comfy-Org/MiniMax-H3` | **19.2M** | OK |
| `BAAI/bge-reranker-v2-m3` | **18.1M** | OK |
| `timm/mobilenetv3_small_100.lamb_in1k` | **17.2M** | OK |

---

## 🏢 By Organization

| Organization | Targets | Training Section | Declared Datasets | License |
|--------------|---------|------------------|-------------------|---------|
| **mradermacher** | 239 | 0 (0%) | 73 (31%) | 198 (83%) |
| **facebook** | 189 | 26 (14%) | 75 (40%) | 179 (95%) |
| **Qwen** | 176 | 4 (2%) | 0 (0%) | 173 (98%) |
| **google** | 170 | 61 (36%) | 47 (28%) | 161 (95%) |
| **nvidia** | 155 | 87 (56%) | 60 (39%) | 147 (95%) |
| **microsoft** | 143 | 44 (31%) | 20 (14%) | 117 (82%) |
| **allenai** | 131 | 6 (5%) | 76 (58%) | 109 (83%) |
| **openbmb** | 112 | 1 (1%) | 39 (35%) | 76 (68%) |
| **tiiuae** | 112 | 22 (20%) | 21 (19%) | 104 (93%) |
| **EleutherAI** | 110 | 84 (76%) | 100 (91%) | 107 (97%) |
| **Salesforce** | 110 | 32 (29%) | 20 (18%) | 107 (97%) |
| **BAAI** | 109 | 11 (10%) | 19 (17%) | 102 (94%) |
| **apple** | 106 | 20 (19%) | 15 (14%) | 106 (100%) |
| **internlm** | 106 | 1 (1%) | 22 (21%) | 102 (96%) |
| **bigscience** | 105 | 15 (14%) | 23 (22%) | 41 (39%) |

---

## 📉 Drift Observations

| Metric | Value |
|--------|-------|
| **Changes (7 days)** | 59 |
| **Changes (30 days)** | 1160 |
| **Targets with changes** | 1071 |

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

*Report fingerprint: `e1957a23f4eba630...`*

*Source: [Crovia Training Provenance Registry](https://registry.croviatrust.com)*