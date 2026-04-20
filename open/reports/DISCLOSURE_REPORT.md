# 📊 Crovia Disclosure Transparency Report

> **Week 2026-W17** | Generated 2026-04-20 08:09:29 UTC
>
> *This is observational data only. No inference, judgment, or accusation.*

---

## 📈 Coverage

| Metric | Value |
|--------|-------|
| **Targets Monitored** | 4288 |
| Models | 3442 |
| Datasets | 846 |

---

## 🔍 Disclosure Observations

| Field | Present | Absent | % Present |
|-------|---------|--------|-----------|
| **Training Section** | 684 | 3604 | **16.0%** |
| **Declared Datasets** | 866 | 3422 | **20.2%** |
| **License** | 3280 | 1008 | **76.5%** |
| **README Accessible** | 3692 | 596 | **86.1%** |

---

## 📥 Popularity Observations

- **Targets with download data:** 4118
- **Gated targets:** 171 (4.0%)

### Top Targets by Downloads

| Target | Type | Downloads | Training Section | Declared Datasets |
|--------|------|-----------|------------------|-------------------|
| `sentence-transformers/all-MiniLM-L6-v2` | model | **203.9M** | PRESENT | 21 |
| `google-bert/bert-base-uncased` | model | **60.4M** | PRESENT | 2 |
| `Qwen/Qwen3-VL-2B-Instruct` | model | **51.7M** | ABSENT | 0 |
| `google/electra-base-discriminator` | model | **47.1M** | ABSENT | 0 |
| `Falconsai/nsfw_image_detection` | model | **36.6M** | PRESENT | 0 |
| `sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2` | model | **34.4M** | ABSENT | 0 |
| `sentence-transformers/all-mpnet-base-v2` | model | **33.4M** | PRESENT | 21 |
| `cross-encoder/ms-marco-MiniLM-L6-v2` | model | **24.1M** | ABSENT | 1 |
| `FacebookAI/roberta-large` | model | **21.4M** | PRESENT | 2 |
| `BAAI/bge-small-en-v1.5` | model | **21.1M** | ABSENT | 0 |

### High-Download Targets Without Training Section

*Factual observation: these targets have >10K downloads and no detected training section.*

| Target | Downloads | README |
|--------|-----------|--------|
| `Qwen/Qwen3-VL-2B-Instruct` | **51.7M** | OK |
| `google/electra-base-discriminator` | **47.1M** | OK |
| `sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2` | **34.4M** | OK |
| `cross-encoder/ms-marco-MiniLM-L6-v2` | **24.1M** | OK |
| `BAAI/bge-small-en-v1.5` | **21.1M** | OK |
| `openai/clip-vit-large-patch14` | **21.0M** | OK |
| `openai/clip-vit-base-patch32` | **20.2M** | OK |
| `FacebookAI/xlm-roberta-base` | **17.8M** | OK |
| `laion/clap-htsat-fused` | **17.0M** | OK |
| `timm/mobilenetv3_small_100.lamb_in1k` | **16.2M** | OK |

---

## 🏢 By Organization

| Organization | Targets | Training Section | Declared Datasets | License |
|--------------|---------|------------------|-------------------|---------|
| **Qwen** | 160 | 3 (2%) | 0 (0%) | 158 (99%) |
| **facebook** | 109 | 16 (15%) | 44 (40%) | 103 (94%) |
| **google** | 93 | 32 (34%) | 24 (26%) | 90 (97%) |
| **timm** | 88 | 0 (0%) | 68 (77%) | 88 (100%) |
| **microsoft** | 86 | 23 (27%) | 13 (15%) | 69 (80%) |
| **nvidia** | 82 | 39 (48%) | 34 (41%) | 78 (95%) |
| **allenai** | 71 | 3 (4%) | 31 (44%) | 61 (86%) |
| **unsloth** | 65 | 4 (6%) | 1 (2%) | 63 (97%) |
| **OpenMed** | 53 | 0 (0%) | 0 (0%) | 53 (100%) |
| **Salesforce** | 52 | 11 (21%) | 6 (12%) | 51 (98%) |
| **lmstudio-community** | 51 | 0 (0%) | 4 (8%) | 51 (100%) |
| **MaziyarPanahi** | 47 | 2 (4%) | 0 (0%) | 6 (13%) |
| **bigscience** | 45 | 7 (16%) | 8 (18%) | 18 (40%) |
| **BAAI** | 45 | 7 (16%) | 9 (20%) | 41 (91%) |
| **deepseek-ai** | 45 | 0 (0%) | 0 (0%) | 37 (82%) |

---

## 📉 Drift Observations

| Metric | Value |
|--------|-------|
| **Changes (7 days)** | 57 |
| **Changes (30 days)** | 796 |
| **Targets with changes** | 427 |

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

*Report fingerprint: `e7d2497754f51ab2...`*

*Source: [Crovia Training Provenance Registry](https://registry.croviatrust.com)*