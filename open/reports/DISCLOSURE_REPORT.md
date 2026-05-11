# 📊 Crovia Disclosure Transparency Report

> **Week 2026-W20** | Generated 2026-05-11 08:11:46 UTC
>
> *This is observational data only. No inference, judgment, or accusation.*

---

## 📈 Coverage

| Metric | Value |
|--------|-------|
| **Targets Monitored** | 4324 |
| Models | 3481 |
| Datasets | 843 |

---

## 🔍 Disclosure Observations

| Field | Present | Absent | % Present |
|-------|---------|--------|-----------|
| **Training Section** | 673 | 3651 | **15.6%** |
| **Declared Datasets** | 864 | 3460 | **20.0%** |
| **License** | 3330 | 994 | **77.0%** |
| **README Accessible** | 3749 | 575 | **86.7%** |

---

## 📥 Popularity Observations

- **Targets with download data:** 4148
- **Gated targets:** 172 (4.0%)

### Top Targets by Downloads

| Target | Type | Downloads | Training Section | Declared Datasets |
|--------|------|-----------|------------------|-------------------|
| `sentence-transformers/all-MiniLM-L6-v2` | model | **253.6M** | PRESENT | 21 |
| `Qwen/Qwen3-VL-2B-Instruct` | model | **187.0M** | ABSENT | 0 |
| `google-bert/bert-base-uncased` | model | **62.9M** | PRESENT | 2 |
| `google/electra-base-discriminator` | model | **53.4M** | ABSENT | 0 |
| `cross-encoder/ms-marco-MiniLM-L6-v2` | model | **46.9M** | ABSENT | 1 |
| `sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2` | model | **46.9M** | ABSENT | 0 |
| `BAAI/bge-small-en-v1.5` | model | **38.6M** | ABSENT | 0 |
| `sentence-transformers/all-mpnet-base-v2` | model | **36.1M** | PRESENT | 21 |
| `openai/clip-vit-large-patch14` | model | **28.3M** | ABSENT | 0 |
| `BAAI/bge-m3` | model | **22.8M** | PRESENT | 0 |

### High-Download Targets Without Training Section

*Factual observation: these targets have >10K downloads and no detected training section.*

| Target | Downloads | README |
|--------|-----------|--------|
| `Qwen/Qwen3-VL-2B-Instruct` | **187.0M** | OK |
| `google/electra-base-discriminator` | **53.4M** | OK |
| `cross-encoder/ms-marco-MiniLM-L6-v2` | **46.9M** | OK |
| `sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2` | **46.9M** | OK |
| `BAAI/bge-small-en-v1.5` | **38.6M** | OK |
| `openai/clip-vit-large-patch14` | **28.3M** | OK |
| `openai/clip-vit-base-patch32` | **21.5M** | OK |
| `laion/clap-htsat-fused` | **20.0M** | OK |
| `FacebookAI/xlm-roberta-base` | **19.4M** | OK |
| `timm/mobilenetv3_small_100.lamb_in1k` | **18.7M** | OK |

---

## 🏢 By Organization

| Organization | Targets | Training Section | Declared Datasets | License |
|--------------|---------|------------------|-------------------|---------|
| **Qwen** | 167 | 3 (2%) | 0 (0%) | 165 (99%) |
| **facebook** | 114 | 19 (17%) | 45 (39%) | 108 (95%) |
| **google** | 96 | 33 (34%) | 24 (25%) | 93 (97%) |
| **microsoft** | 91 | 26 (29%) | 13 (14%) | 73 (80%) |
| **nvidia** | 85 | 42 (49%) | 34 (40%) | 81 (95%) |
| **timm** | 84 | 0 (0%) | 65 (77%) | 84 (100%) |
| **allenai** | 72 | 3 (4%) | 32 (44%) | 62 (86%) |
| **unsloth** | 72 | 5 (7%) | 1 (1%) | 70 (97%) |
| **OpenMed** | 53 | 0 (0%) | 0 (0%) | 53 (100%) |
| **Salesforce** | 50 | 11 (22%) | 6 (12%) | 49 (98%) |
| **lmstudio-community** | 49 | 0 (0%) | 4 (8%) | 49 (100%) |
| **BAAI** | 47 | 7 (15%) | 9 (19%) | 43 (91%) |
| **MaziyarPanahi** | 47 | 2 (4%) | 0 (0%) | 6 (13%) |
| **bigscience** | 46 | 7 (15%) | 8 (17%) | 19 (41%) |
| **deepseek-ai** | 46 | 0 (0%) | 0 (0%) | 38 (83%) |

---

## 📉 Drift Observations

| Metric | Value |
|--------|-------|
| **Changes (7 days)** | 53 |
| **Changes (30 days)** | 730 |
| **Targets with changes** | 395 |

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

*Report fingerprint: `f81a9bb6bd08f80e...`*

*Source: [Crovia Training Provenance Registry](https://registry.croviatrust.com)*