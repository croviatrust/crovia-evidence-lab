# 📊 Crovia Disclosure Transparency Report

> **Week 2026-W19** | Generated 2026-05-04 08:10:31 UTC
>
> *This is observational data only. No inference, judgment, or accusation.*

---

## 📈 Coverage

| Metric | Value |
|--------|-------|
| **Targets Monitored** | 4321 |
| Models | 3474 |
| Datasets | 847 |

---

## 🔍 Disclosure Observations

| Field | Present | Absent | % Present |
|-------|---------|--------|-----------|
| **Training Section** | 673 | 3648 | **15.6%** |
| **Declared Datasets** | 864 | 3457 | **20.0%** |
| **License** | 3320 | 1001 | **76.8%** |
| **README Accessible** | 3735 | 586 | **86.4%** |

---

## 📥 Popularity Observations

- **Targets with download data:** 4149
- **Gated targets:** 172 (4.0%)

### Top Targets by Downloads

| Target | Type | Downloads | Training Section | Declared Datasets |
|--------|------|-----------|------------------|-------------------|
| `sentence-transformers/all-MiniLM-L6-v2` | model | **236.3M** | PRESENT | 21 |
| `Qwen/Qwen3-VL-2B-Instruct` | model | **186.8M** | ABSENT | 0 |
| `google-bert/bert-base-uncased` | model | **59.8M** | PRESENT | 2 |
| `google/electra-base-discriminator` | model | **54.4M** | ABSENT | 0 |
| `sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2` | model | **44.3M** | ABSENT | 0 |
| `cross-encoder/ms-marco-MiniLM-L6-v2` | model | **38.8M** | ABSENT | 1 |
| `sentence-transformers/all-mpnet-base-v2` | model | **36.3M** | PRESENT | 21 |
| `BAAI/bge-small-en-v1.5` | model | **32.5M** | ABSENT | 0 |
| `openai/clip-vit-large-patch14` | model | **24.7M** | ABSENT | 0 |
| `Falconsai/nsfw_image_detection` | model | **23.2M** | PRESENT | 0 |

### High-Download Targets Without Training Section

*Factual observation: these targets have >10K downloads and no detected training section.*

| Target | Downloads | README |
|--------|-----------|--------|
| `Qwen/Qwen3-VL-2B-Instruct` | **186.8M** | OK |
| `google/electra-base-discriminator` | **54.4M** | OK |
| `sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2` | **44.3M** | OK |
| `cross-encoder/ms-marco-MiniLM-L6-v2` | **38.8M** | OK |
| `BAAI/bge-small-en-v1.5` | **32.5M** | OK |
| `openai/clip-vit-large-patch14` | **24.7M** | OK |
| `timm/mobilenetv3_small_100.lamb_in1k` | **22.7M** | OK |
| `openai/clip-vit-base-patch32` | **21.2M** | OK |
| `Qwen/Qwen3-0.6B` | **19.4M** | OK |
| `FacebookAI/xlm-roberta-base` | **18.2M** | OK |

---

## 🏢 By Organization

| Organization | Targets | Training Section | Declared Datasets | License |
|--------------|---------|------------------|-------------------|---------|
| **Qwen** | 165 | 3 (2%) | 0 (0%) | 163 (99%) |
| **facebook** | 111 | 18 (16%) | 44 (40%) | 105 (95%) |
| **google** | 96 | 32 (33%) | 24 (25%) | 93 (97%) |
| **microsoft** | 90 | 25 (28%) | 13 (14%) | 72 (80%) |
| **timm** | 85 | 0 (0%) | 66 (78%) | 85 (100%) |
| **nvidia** | 84 | 41 (49%) | 34 (40%) | 80 (95%) |
| **unsloth** | 73 | 5 (7%) | 1 (1%) | 71 (97%) |
| **allenai** | 71 | 3 (4%) | 32 (45%) | 61 (86%) |
| **OpenMed** | 53 | 0 (0%) | 0 (0%) | 53 (100%) |
| **lmstudio-community** | 53 | 0 (0%) | 4 (8%) | 53 (100%) |
| **Salesforce** | 52 | 11 (21%) | 6 (12%) | 51 (98%) |
| **MaziyarPanahi** | 47 | 2 (4%) | 0 (0%) | 6 (13%) |
| **BAAI** | 46 | 7 (15%) | 9 (20%) | 42 (91%) |
| **bigscience** | 46 | 7 (15%) | 8 (17%) | 19 (41%) |
| **deepseek-ai** | 46 | 0 (0%) | 0 (0%) | 38 (83%) |

---

## 📉 Drift Observations

| Metric | Value |
|--------|-------|
| **Changes (7 days)** | 43 |
| **Changes (30 days)** | 752 |
| **Targets with changes** | 405 |

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

*Report fingerprint: `6e65c9076e0d6b13...`*

*Source: [Crovia Training Provenance Registry](https://registry.croviatrust.com)*