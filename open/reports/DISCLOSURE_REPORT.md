# 📊 Crovia Disclosure Transparency Report

> **Week 2026-W08** | Generated 2026-02-16 07:03:55 UTC
>
> *This is observational data only. No inference, judgment, or accusation.*

---

## 📈 Coverage

| Metric | Value |
|--------|-------|
| **Targets Monitored** | 2111 |
| Models | 1582 |
| Datasets | 529 |

---

## 🔍 Disclosure Observations

| Field | Present | Absent | % Present |
|-------|---------|--------|-----------|
| **Training Section** | 313 | 1798 | **14.8%** |
| **Declared Datasets** | 406 | 1705 | **19.2%** |
| **License** | 1617 | 494 | **76.6%** |
| **README Accessible** | 1844 | 267 | **87.4%** |

---

## 📥 Popularity Observations

- **Targets with download data:** 2106
- **Gated targets:** 85 (4.0%)

### Top Targets by Downloads

| Target | Type | Downloads | Training Section | Declared Datasets |
|--------|------|-----------|------------------|-------------------|
| `sentence-transformers/all-MiniLM-L6-v2` | model | **159.1M** | PRESENT | 21 |
| `google-bert/bert-base-uncased` | model | **49.7M** | PRESENT | 2 |
| `google/electra-base-discriminator` | model | **44.6M** | ABSENT | 0 |
| `Falconsai/nsfw_image_detection` | model | **41.7M** | PRESENT | 0 |
| `sentence-transformers/all-mpnet-base-v2` | model | **23.7M** | PRESENT | 21 |
| `timm/mobilenetv3_small_100.lamb_in1k` | model | **22.4M** | ABSENT | 1 |
| `Qwen/Qwen2.5-VL-3B-Instruct` | model | **21.4M** | ABSENT | 0 |
| `FacebookAI/xlm-roberta-base` | model | **21.0M** | ABSENT | 0 |
| `laion/clap-htsat-fused` | model | **18.7M** | ABSENT | 0 |
| `sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2` | model | **18.2M** | ABSENT | 0 |

### High-Download Targets Without Training Section

*Factual observation: these targets have >10K downloads and no detected training section.*

| Target | Downloads | README |
|--------|-----------|--------|
| `google/electra-base-discriminator` | **44.6M** | OK |
| `timm/mobilenetv3_small_100.lamb_in1k` | **22.4M** | OK |
| `Qwen/Qwen2.5-VL-3B-Instruct` | **21.4M** | OK |
| `FacebookAI/xlm-roberta-base` | **21.0M** | OK |
| `laion/clap-htsat-fused` | **18.7M** | OK |
| `sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2` | **18.2M** | OK |
| `openai/clip-vit-base-patch32` | **17.3M** | OK |
| `pyannote/wespeaker-voxceleb-resnet34-LM` | **15.5M** | OK |
| `dima806/fairface_age_image_detection` | **14.2M** | OK |
| `pyannote/segmentation-3.0` | **13.8M** | FORBIDDEN |

---

## 🏢 By Organization

| Organization | Targets | Training Section | Declared Datasets | License |
|--------------|---------|------------------|-------------------|---------|
| **Qwen** | 123 | 4 (3%) | 0 (0%) | 122 (99%) |
| **timm** | 74 | 0 (0%) | 58 (78%) | 74 (100%) |
| **facebook** | 61 | 12 (20%) | 22 (36%) | 57 (93%) |
| **microsoft** | 61 | 13 (21%) | 8 (13%) | 49 (80%) |
| **google** | 56 | 21 (38%) | 16 (29%) | 55 (98%) |
| **MaziyarPanahi** | 47 | 2 (4%) | 0 (0%) | 6 (13%) |
| **OpenMed** | 39 | 0 (0%) | 0 (0%) | 39 (100%) |
| **lmstudio-community** | 36 | 0 (0%) | 4 (11%) | 36 (100%) |
| **nvidia** | 31 | 14 (45%) | 16 (52%) | 31 (100%) |
| **brightonzen17** | 30 | 0 (0%) | 0 (0%) | 0 (0%) |
| **sentence-transformers** | 28 | 9 (32%) | 9 (32%) | 23 (82%) |
| **unsloth** | 27 | 2 (7%) | 0 (0%) | 26 (96%) |
| **allenai** | 22 | 0 (0%) | 2 (9%) | 19 (86%) |
| **deepseek-ai** | 22 | 0 (0%) | 0 (0%) | 21 (95%) |
| **Helsinki-NLP** | 21 | 2 (10%) | 0 (0%) | 21 (100%) |

---

## 📉 Drift Observations

| Metric | Value |
|--------|-------|
| **Changes (7 days)** | 866 |
| **Changes (30 days)** | 1331 |
| **Targets with changes** | 958 |

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

*Report fingerprint: `ef72080b0a2b3701...`*

*Source: [Crovia Training Provenance Registry](https://registry.croviatrust.com)*