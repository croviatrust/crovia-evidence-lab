# 📊 Crovia Disclosure Transparency Report

> **Week 2026-W07** | Generated 2026-02-09 06:22:49 UTC
>
> *This is observational data only. No inference, judgment, or accusation.*

---

## 📈 Coverage

| Metric | Value |
|--------|-------|
| **Targets Monitored** | 2077 |
| Models | 1567 |
| Datasets | 510 |

---

## 🔍 Disclosure Observations

| Field | Present | Absent | % Present |
|-------|---------|--------|-----------|
| **Training Section** | 298 | 1779 | **14.3%** |
| **Declared Datasets** | 257 | 1820 | **12.4%** |
| **License** | 1246 | 831 | **60.0%** |
| **README Accessible** | 1827 | 250 | **88.0%** |

---

## 📥 Popularity Observations

- **Targets with download data:** 1624
- **Gated targets:** 62 (3.0%)

### Top Targets by Downloads

| Target | Type | Downloads | Training Section | Declared Datasets |
|--------|------|-----------|------------------|-------------------|
| `sentence-transformers/all-MiniLM-L6-v2` | model | **151.4M** | PRESENT | 21 |
| `Falconsai/nsfw_image_detection` | model | **59.2M** | PRESENT | 0 |
| `timm/mobilenetv3_small_100.lamb_in1k` | model | **24.7M** | ABSENT | 1 |
| `sentence-transformers/all-mpnet-base-v2` | model | **23.1M** | PRESENT | 21 |
| `Qwen/Qwen2.5-VL-3B-Instruct` | model | **21.5M** | ABSENT | 0 |
| `FacebookAI/roberta-large` | model | **19.9M** | PRESENT | 2 |
| `sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2` | model | **17.9M** | ABSENT | 0 |
| `FacebookAI/xlm-roberta-base` | model | **17.8M** | ABSENT | 0 |
| `openai/clip-vit-base-patch32` | model | **16.7M** | ABSENT | 0 |
| `colbert-ir/colbertv2.0` | model | **15.5M** | PRESENT | 0 |

### High-Download Targets Without Training Section

*Factual observation: these targets have >10K downloads and no detected training section.*

| Target | Downloads | README |
|--------|-----------|--------|
| `timm/mobilenetv3_small_100.lamb_in1k` | **24.7M** | OK |
| `Qwen/Qwen2.5-VL-3B-Instruct` | **21.5M** | OK |
| `sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2` | **17.9M** | OK |
| `FacebookAI/xlm-roberta-base` | **17.8M** | OK |
| `openai/clip-vit-base-patch32` | **16.7M** | OK |
| `pyannote/wespeaker-voxceleb-resnet34-LM` | **15.4M** | OK |
| `pyannote/segmentation-3.0` | **13.5M** | FORBIDDEN |
| `pyannote/speaker-diarization-3.1` | **12.7M** | FORBIDDEN |
| `autogluon/chronos-bolt-small` | **12.0M** | OK |
| `Bingsu/adetailer` | **11.9M** | OK |

---

## 🏢 By Organization

| Organization | Targets | Training Section | Declared Datasets | License |
|--------------|---------|------------------|-------------------|---------|
| **Qwen** | 126 | 3 (2%) | 0 (0%) | 124 (98%) |
| **timm** | 74 | 0 (0%) | 58 (78%) | 74 (100%) |
| **facebook** | 59 | 11 (19%) | 0 (0%) | 1 (2%) |
| **google** | 59 | 22 (37%) | 0 (0%) | 1 (2%) |
| **microsoft** | 59 | 14 (24%) | 8 (14%) | 49 (83%) |
| **MaziyarPanahi** | 50 | 2 (4%) | 0 (0%) | 6 (12%) |
| **OpenMed** | 43 | 0 (0%) | 0 (0%) | 43 (100%) |
| **lmstudio-community** | 35 | 0 (0%) | 4 (11%) | 35 (100%) |
| **nvidia** | 33 | 16 (48%) | 17 (52%) | 33 (100%) |
| **sentence-transformers** | 28 | 9 (32%) | 9 (32%) | 23 (82%) |
| **unsloth** | 28 | 2 (7%) | 0 (0%) | 0 (0%) |
| **brightonzen17** | 22 | 0 (0%) | 0 (0%) | 0 (0%) |
| **Helsinki-NLP** | 21 | 2 (10%) | 0 (0%) | 21 (100%) |
| **deepseek-ai** | 21 | 0 (0%) | 0 (0%) | 0 (0%) |
| **allenai** | 20 | 0 (0%) | 1 (5%) | 17 (85%) |

---

## 📉 Drift Observations

| Metric | Value |
|--------|-------|
| **Changes (7 days)** | 465 |
| **Changes (30 days)** | 465 |
| **Targets with changes** | 410 |

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

*Report fingerprint: `3d322599b29dc463...`*

*Source: [Crovia Training Provenance Registry](https://registry.croviatrust.com)*