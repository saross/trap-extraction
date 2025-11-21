# TRAP Data Extraction - Work Summary

**Collaborative work between Dr. Adela Sobotkova and Claude Code**

**Completion Date:** November 2025

---

## Project Overview

This document summarises the collaborative extraction of walker (team member) attribution data from the Tundzha Regional Archaeological Project (TRAP) field survey records, covering the 2009-2011 seasons.

### Objective

Extract team composition data from heterogeneous archaeological field documentation to enable proper credit attribution for survey participants in the project archives and future publications.

### Outcome

- **212 survey day records** extracted and validated
- **91.1% extraction accuracy** achieved
- **23 source documents** processed across multiple formats and languages

---

## Extraction Pipeline Phases

### Phase 1: Excel Survey Summaries

Extracted team leaders, dates, and survey unit ranges from SurveySummary spreadsheets.

- **Sources:** 4 Excel files (ELH09, KAZ10, YAM10, KAZ11)
- **Records:** 192 initial records
- **Script:** `extract_phase1.py`

### Phase 2: English Diaries (2009 Elhovo)

Extracted walker names from narrative diary entries using pattern matching.

- **Sources:** 3 diary files (Team A, B, C)
- **Records:** 59 records enhanced
- **Scripts:** `extract_phase2.py`, `parse_diaries.py`

### Phase 2b: PDF Summaries and Bulgarian Diaries

Extended extraction to cover gaps from earlier phases.

- **PDF Sources:** 16 Daily Progress Forms
- **Bulgarian Diaries:** 4 files (Teams A, B, D - 2011)
- **Records:** 179 records from PDF/diary sources
- **Scripts:** `extract_phase2b_walkers.py`, `parse_bulgarian_diaries_2011.py`, `parse_team_a_2011.py`

### Phase 3: NLP Cleaning

Natural language processing to clean extracted names and remove noise.

- **Records cleaned:** 68
- **Script:** `extract_phase3.py`

### Consolidation

Merged all phases with intelligent priority rules (Phase 2b > Phase 2 > Phase 1).

- **Final merged records:** 213
- **Script:** `consolidate_v2.py`

### QA and Cleanup

Comprehensive quality assurance including:

- Duplicate detection and merging (213 → 212 records)
- Narrative text removal (English and Bulgarian)
- Name pattern validation
- Cyrillic-to-Latin transliteration (28 entries)
- Spot-check sampling (10 random records)

**Scripts:** `qa_validation.py`, `data_cleanup.py`

---

## Final Data Coverage

| Field | Count | Percentage |
|-------|-------|------------|
| Leader specified | 210/212 | 99.1% |
| Walkers specified | 155/212 | 73.1% |
| Author specified | 124/212 | 58.5% |
| PDA_Operator specified | 7/212 | 3.3% |
| Data_Editor specified | 6/212 | 2.8% |
| Paper_Recorder specified | 2/212 | 0.9% |

---

## Extraction Accuracy Assessment

After the automated extraction pipeline completed, Dr. Sobotkova performed manual review of the output, identifying 15 corrections needed:

| Error Type | Count | Description |
|------------|-------|-------------|
| Narrative fragments | 14 | Sentence fragments from Team A 2009 diary incorrectly captured as names |
| Misread text | 1 | Unclear handwriting misinterpreted ("Bulgaria mi" → "[unclear]") |

**Final extraction accuracy:** 91.1% (154/169 walker entries correct before manual review)

---

## Key Technical Challenges Solved

### 1. Multi-format Document Processing

- `.doc` files: Converted via `antiword` with UTF-8 encoding
- `.docx` files: Converted via `pandoc` plain text extraction
- `.pdf` files: Extracted using specialised form parsers
- `.xls/.xlsx` files: Processed with `pandas` + `openpyxl`/`xlrd`

### 2. Bilingual Content

- English diaries: Standard regex pattern matching
- Bulgarian diaries: Cyrillic text extraction with transliteration to Latin script
- Mixed content: Language detection and appropriate parsing

### 3. Narrative vs. Structured Data

- Diary entries: Narrative text parsing with name extraction
- PDF forms: Structured field extraction
- Challenge: Distinguishing walker names from surrounding narrative text

### 4. Name Variations

- Full names, initials, and diminutives across sources
- Cyrillic vs. Latin script representations
- Solution: `Walkers_Transliterated` column for standardised Latin script

---

## Source Documents Processed

| Type | Count | Records |
|------|-------|---------|
| English Diaries | 3 | 59 |
| Bulgarian Diaries | 4 | 30 |
| PDF Summaries | 16 | 91 |
| **Total** | **23** | **180** |

### Coverage by Season

- **2009 (Kazanlak spring, Yambol/Elhovo autumn):** 68 records
- **2010 (Kazanlak spring, Yambol autumn):** 77 records
- **2011 (Kazanlak autumn):** 67 records

---

## Deliverables

### Primary Output

`outputs/final_attribution_v2_cleaned_edited.csv`

- 212 records across 15 columns
- UTF-8 encoded CSV
- Ready for AKB submission

### Documentation

| File | Description |
|------|-------------|
| `README.md` | Project overview and pipeline documentation |
| `extraction-accuracy-report.md` | Accuracy analysis after manual review |
| `extraction-summary-report.md` | Technical extraction methodology |
| `qa-validation-report.md` | Quality assurance results |
| `narrative-cleanup-summary.md` | Log of narrative text cleanup |
| `submission-readme.md` | Package documentation for AKB |
| `submission-checklist.md` | Submission sign-off checklist |

---

## Lessons Learned

### What Worked Well

1. **Phased approach:** Breaking extraction into distinct phases allowed targeted solutions for each document type
2. **Priority-based consolidation:** Later phases (with better data) correctly overrode earlier extractions
3. **Automated QA validation:** Caught duplicates, format issues, and data quality problems early
4. **Iterative cleanup:** Multiple passes through the data improved quality progressively

### Areas for Improvement

1. **Diary parsing:** The Team A 2009 English diary's narrative style caused 14/15 extraction errors - source-specific parsers recommended for similar documents
2. **Name validation:** Stricter pattern matching to reject entries not matching expected name formats
3. **Role data coverage:** PDA operator and paper recorder fields remained sparsely populated (<5%) due to limited source documentation

---

## Acknowledgements

This extraction pipeline was developed collaboratively by:

- **Dr. Adela Sobotkova** - Project Lead, TRAP
- **Claude Code (Anthropic)** - Extraction pipeline development and automation

The extracted data enables proper attribution of field survey work to all TRAP project participants across the 2009-2011 seasons.

---

**Report generated:** November 2025
