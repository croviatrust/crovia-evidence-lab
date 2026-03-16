# 📊 Crovia Disclosure Transparency Report

> **Week 2026-W12** | Generated 2026-03-16 08:13:45 UTC
>
> *This is observational data only. No inference, judgment, or accusation.*

---

## 📈 Coverage

| Metric | Value |
|--------|-------|
| **Targets Monitored** | 4135 |
| Models | 3304 |
| Datasets | 831 |

---

## 🔍 Disclosure Observations

| Field | Present | Absent | % Present |
|-------|---------|--------|-----------|
| **Training Section** | 651 | 3484 | **15.7%** |
| **Declared Datasets** | 843 | 3292 | **20.4%** |
| **License** | 3112 | 1023 | **75.3%** |
| **README Accessible** | 3534 | 600 | **85.5%** |

---

## 📥 Popularity Observations

- **Targets with download data:** 3958
- **Gated targets:** 159 (3.8%)

### Top Targets by Downloads

| Target | Type | Downloads | Training Section | Declared Datasets |
|--------|------|-----------|------------------|-------------------|
| `sentence-transformers/all-MiniLM-L6-v2` | model | **205.3M** | PRESENT | 21 |
| `google-bert/bert-base-uncased` | model | **69.7M** | PRESENT | 2 |
| `google/electra-base-discriminator` | model | **50.3M** | ABSENT | 0 |
| `Falconsai/nsfw_image_detection` | model | **41.8M** | PRESENT | 0 |
| `sentence-transformers/all-mpnet-base-v2` | model | **28.4M** | PRESENT | 21 |
| `timm/mobilenetv3_small_100.lamb_in1k` | model | **24.6M** | ABSENT | 1 |
| `sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2` | model | **24.0M** | ABSENT | 0 |
| `laion/clap-htsat-fused` | model | **23.5M** | ABSENT | 0 |
| `Qwen/Qwen2.5-7B-Instruct` | model | **22.8M** | ABSENT | 0 |
| `FacebookAI/roberta-large` | model | **21.4M** | PRESENT | 2 |

### High-Download Targets Without Training Section

*Factual observation: these targets have >10K downloads and no detected training section.*

| Target | Downloads | README |
|--------|-----------|--------|
| `google/electra-base-discriminator` | **50.3M** | OK |
| `timm/mobilenetv3_small_100.lamb_in1k` | **24.6M** | OK |
| `sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2` | **24.0M** | OK |
| `laion/clap-htsat-fused` | **23.5M** | OK |
| `Qwen/Qwen2.5-7B-Instruct` | **22.8M** | OK |
| `FacebookAI/xlm-roberta-base` | **20.2M** | OK |
| `openai/clip-vit-base-patch32` | **19.3M** | OK |
| `Bingsu/adetailer` | **19.3M** | OK |
| `cross-encoder/ms-marco-MiniLM-L6-v2` | **14.8M** | OK |
| `pyannote/wespeaker-voxceleb-resnet34-LM` | **14.3M** | OK |

---

## 🏢 By Organization

| Organization | Targets | Training Section | Declared Datasets | License |
|--------------|---------|------------------|-------------------|---------|
| **Qwen** | 159 | 4 (3%) | 0 (0%) | 155 (97%) |
| **facebook** | 106 | 16 (15%) | 44 (42%) | 99 (93%) |
| **timm** | 86 | 0 (0%) | 67 (78%) | 86 (100%) |
| **google** | 85 | 33 (39%) | 23 (27%) | 82 (96%) |
| **microsoft** | 85 | 22 (26%) | 12 (14%) | 68 (80%) |
| **allenai** | 72 | 3 (4%) | 31 (43%) | 61 (85%) |
| **nvidia** | 70 | 34 (49%) | 31 (44%) | 66 (94%) |
| **unsloth** | 58 | 4 (7%) | 1 (2%) | 55 (95%) |
| **OpenMed** | 53 | 0 (0%) | 0 (0%) | 53 (100%) |
| **Salesforce** | 51 | 11 (22%) | 6 (12%) | 50 (98%) |
| **MaziyarPanahi** | 47 | 2 (4%) | 0 (0%) | 6 (13%) |
| **bigscience** | 46 | 7 (15%) | 8 (17%) | 19 (41%) |
| **BAAI** | 45 | 7 (16%) | 9 (20%) | 41 (91%) |
| **EleutherAI** | 43 | 31 (72%) | 38 (88%) | 43 (100%) |
| **NousResearch** | 43 | 8 (19%) | 15 (35%) | 35 (81%) |

---

## 📉 Drift Observations

| Metric | Value |
|--------|-------|
| **Changes (7 days)** | 37 |
| **Changes (30 days)** | 551 |
| **Targets with changes** | 524 |

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

*Report fingerprint: `c55d77772531dd5d...`*

*Source: [Crovia Training Provenance Registry](https://registry.croviatrust.com)*