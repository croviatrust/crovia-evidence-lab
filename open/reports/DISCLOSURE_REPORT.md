# 📊 Crovia Disclosure Transparency Report

> **Week 2026-W09** | Generated 2026-02-23 07:56:40 UTC
>
> *This is observational data only. No inference, judgment, or accusation.*

---

## 📈 Coverage

| Metric | Value |
|--------|-------|
| **Targets Monitored** | 3812 |
| Models | 3135 |
| Datasets | 677 |

---

## 🔍 Disclosure Observations

| Field | Present | Absent | % Present |
|-------|---------|--------|-----------|
| **Training Section** | 625 | 3187 | **16.4%** |
| **Declared Datasets** | 828 | 2984 | **21.7%** |
| **License** | 2910 | 902 | **76.3%** |
| **README Accessible** | 3302 | 510 | **86.6%** |

---

## 📥 Popularity Observations

- **Targets with download data:** 3667
- **Gated targets:** 150 (3.9%)

### Top Targets by Downloads

| Target | Type | Downloads | Training Section | Declared Datasets |
|--------|------|-----------|------------------|-------------------|
| `sentence-transformers/all-MiniLM-L6-v2` | model | **168.5M** | PRESENT | 21 |
| `google-bert/bert-base-uncased` | model | **53.0M** | PRESENT | 2 |
| `google/electra-base-discriminator` | model | **43.6M** | ABSENT | 0 |
| `Falconsai/nsfw_image_detection` | model | **36.5M** | PRESENT | 0 |
| `sentence-transformers/all-mpnet-base-v2` | model | **24.5M** | PRESENT | 21 |
| `FacebookAI/xlm-roberta-base` | model | **22.8M** | ABSENT | 0 |
| `timm/mobilenetv3_small_100.lamb_in1k` | model | **22.7M** | ABSENT | 1 |
| `FacebookAI/roberta-large` | model | **20.5M** | PRESENT | 2 |
| `sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2` | model | **18.8M** | ABSENT | 0 |
| `laion/clap-htsat-fused` | model | **18.6M** | ABSENT | 0 |

### High-Download Targets Without Training Section

*Factual observation: these targets have >10K downloads and no detected training section.*

| Target | Downloads | README |
|--------|-----------|--------|
| `google/electra-base-discriminator` | **43.6M** | OK |
| `FacebookAI/xlm-roberta-base` | **22.8M** | OK |
| `timm/mobilenetv3_small_100.lamb_in1k` | **22.7M** | OK |
| `sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2` | **18.8M** | OK |
| `laion/clap-htsat-fused` | **18.6M** | OK |
| `openai/clip-vit-base-patch32` | **18.0M** | OK |
| `Qwen/Qwen2.5-VL-3B-Instruct` | **15.9M** | OK |
| `Qwen/Qwen2.5-7B-Instruct` | **15.7M** | OK |
| `pyannote/wespeaker-voxceleb-resnet34-LM` | **14.8M** | OK |
| `pyannote/segmentation-3.0` | **14.0M** | FORBIDDEN |

---

## 🏢 By Organization

| Organization | Targets | Training Section | Declared Datasets | License |
|--------------|---------|------------------|-------------------|---------|
| **Qwen** | 141 | 4 (3%) | 0 (0%) | 137 (97%) |
| **facebook** | 104 | 17 (16%) | 44 (42%) | 98 (94%) |
| **microsoft** | 86 | 22 (26%) | 12 (14%) | 69 (80%) |
| **google** | 83 | 31 (37%) | 23 (28%) | 80 (96%) |
| **timm** | 83 | 0 (0%) | 65 (78%) | 83 (100%) |
| **allenai** | 71 | 3 (4%) | 32 (45%) | 61 (86%) |
| **nvidia** | 65 | 30 (46%) | 28 (43%) | 61 (94%) |
| **Salesforce** | 51 | 11 (22%) | 6 (12%) | 50 (98%) |
| **OpenMed** | 51 | 0 (0%) | 0 (0%) | 51 (100%) |
| **MaziyarPanahi** | 47 | 2 (4%) | 0 (0%) | 6 (13%) |
| **bigscience** | 45 | 7 (16%) | 8 (18%) | 18 (40%) |
| **mradermacher** | 44 | 0 (0%) | 8 (18%) | 35 (80%) |
| **BAAI** | 43 | 7 (16%) | 9 (21%) | 39 (91%) |
| **NousResearch** | 43 | 8 (19%) | 15 (35%) | 35 (81%) |
| **deepseek-ai** | 43 | 0 (0%) | 0 (0%) | 35 (81%) |

---

## 📉 Drift Observations

| Metric | Value |
|--------|-------|
| **Changes (7 days)** | 430 |
| **Changes (30 days)** | 1092 |
| **Targets with changes** | 806 |

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

*Report fingerprint: `f65a069dc991670d...`*

*Source: [Crovia Training Provenance Registry](https://registry.croviatrust.com)*