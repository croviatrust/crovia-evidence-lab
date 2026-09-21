# 📊 Crovia Disclosure Transparency Report

> **Week 2026-W39** | Generated 2026-09-21 11:20:27 UTC
>
> *This is observational data only. No inference, judgment, or accusation.*

---

## 📈 Coverage

| Metric | Value |
|--------|-------|
| **Targets Monitored** | 8851 |
| Models | 7959 |
| Datasets | 892 |

---

## 🔍 Disclosure Observations

| Field | Present | Absent | % Present |
|-------|---------|--------|-----------|
| **Training Section** | 1610 | 7241 | **18.2%** |
| **Declared Datasets** | 1970 | 6881 | **22.3%** |
| **License** | 6270 | 2581 | **70.8%** |
| **README Accessible** | 7219 | 1631 | **81.6%** |

---

## 📥 Popularity Observations

- **Targets with download data:** 7774
- **Gated targets:** 326 (3.7%)

### Top Targets by Downloads

| Target | Type | Downloads | Training Section | Declared Datasets |
|--------|------|-----------|------------------|-------------------|
| `sentence-transformers/all-MiniLM-L6-v2` | model | **251.0M** | PRESENT | 21 |
| `cross-encoder/ms-marco-MiniLM-L6-v2` | model | **88.6M** | ABSENT | 1 |
| `BAAI/bge-small-en-v1.5` | model | **64.4M** | ABSENT | 0 |
| `google/electra-base-discriminator` | model | **48.1M** | ABSENT | 0 |
| `google-bert/bert-base-uncased` | model | **46.1M** | PRESENT | 2 |
| `sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2` | model | **45.7M** | ABSENT | 0 |
| `BAAI/bge-m3` | model | **37.6M** | PRESENT | 0 |
| `google-t5/t5-small` | model | **24.7M** | PRESENT | 1 |
| `Qwen/Qwen3-0.6B` | model | **23.7M** | ABSENT | 0 |
| `amazon/chronos-2` | model | **22.5M** | PRESENT | 2 |

### High-Download Targets Without Training Section

*Factual observation: these targets have >10K downloads and no detected training section.*

| Target | Downloads | README |
|--------|-----------|--------|
| `cross-encoder/ms-marco-MiniLM-L6-v2` | **88.6M** | OK |
| `BAAI/bge-small-en-v1.5` | **64.4M** | OK |
| `google/electra-base-discriminator` | **48.1M** | OK |
| `sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2` | **45.7M** | OK |
| `Qwen/Qwen3-0.6B` | **23.7M** | OK |
| `openai/clip-vit-base-patch32` | **21.9M** | OK |
| `FacebookAI/xlm-roberta-base` | **20.9M** | OK |
| `Comfy-Org/MiniMax-H3` | **20.7M** | OK |
| `Qwen/Qwen3-VL-8B-Instruct` | **19.7M** | OK |
| `timm/mobilenetv3_small_100.lamb_in1k` | **18.5M** | OK |

---

## 🏢 By Organization

| Organization | Targets | Training Section | Declared Datasets | License |
|--------------|---------|------------------|-------------------|---------|
| **mradermacher** | 239 | 0 (0%) | 73 (31%) | 198 (83%) |
| **facebook** | 189 | 26 (14%) | 75 (40%) | 179 (95%) |
| **Qwen** | 181 | 4 (2%) | 0 (0%) | 178 (98%) |
| **google** | 169 | 61 (36%) | 47 (28%) | 160 (95%) |
| **nvidia** | 155 | 86 (55%) | 60 (39%) | 147 (95%) |
| **microsoft** | 143 | 44 (31%) | 20 (14%) | 117 (82%) |
| **allenai** | 132 | 6 (5%) | 76 (58%) | 109 (83%) |
| **openbmb** | 114 | 3 (3%) | 41 (36%) | 78 (68%) |
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
| **Changes (7 days)** | 17 |
| **Changes (30 days)** | 271 |
| **Targets with changes** | 217 |

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

*Report fingerprint: `ef2035b257936219...`*

*Source: [Crovia Training Provenance Registry](https://registry.croviatrust.com)*