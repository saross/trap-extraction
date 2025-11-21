# TRAP Data Extraction Pipeline

Automated extraction of team composition and attribution data from TRAP (Tundzha Regional Archaeology Project) survey records, 2009-2011.

## Project Summary

This pipeline extracted walker (team member) attribution data from heterogeneous archaeological field documentation to enable proper credit for survey participants. The extraction processed 23 source documents across multiple formats and languages, achieving **91.1% extraction accuracy** after QA validation.

### Final Results

| Metric | Value |
|--------|-------|
| Total survey day records | 212 |
| Leader coverage | 210/212 (99.1%) |
| Walker coverage | 155/212 (73.1%) |
| Author coverage | 124/212 (58.5%) |
| PDA_Operator coverage | 7/212 (3.3%) |
| Data_Editor coverage | 6/212 (2.8%) |
| Paper_Recorder coverage | 2/212 (0.9%) |
| Extraction accuracy | 91.1% |

### Output

**Primary deliverable:** `outputs/final_attribution_v2_cleaned_edited.csv`

Submission package prepared for the Archaeological Institute with Museum (AKB), Bulgarian Academy of Sciences.

---

## Extraction Pipeline

### Phase 1: Excel Survey Summaries

Extracted team leaders, dates, and survey unit ranges from SurveySummary spreadsheets.

**Sources:** `ELH09 SurveySummary.xls`, `KAZ10 SurveySummary.xlsx`, etc.

**Script:** `scripts/extract_phase1.py`

### Phase 2: English Diaries (2009 Elhovo)

Extracted walker names from narrative diary entries.

**Sources:** `Diary Team A.doc`, `Diary Team B.doc`, `Diary Team C.doc`

**Scripts:** `scripts/extract_phase2.py`, `scripts/parse_diaries.py`

### Phase 2b: PDF Summaries and Bulgarian Diaries

Extended extraction to cover gaps from Phase 1 and 2.

**PDF Sources:** Daily Progress Forms (`B_2010Summary.pdf`, `C_2011Summary.pdf`, etc.)

**Bulgarian Diary Sources:** `A_2011Diary_BG.doc`, `B_2011Diary_BG.docx`, `D_2011Diary_BG.doc`

**Scripts:**
- `scripts/extract_phase2b_walkers.py` - PDF form extraction
- `scripts/parse_bulgarian_diaries_2011.py` - Bulgarian diary parsing
- `scripts/parse_team_a_2011.py` - Team A narrative format parser

### Phase 3: NLP Cleaning

Natural language processing to clean extracted names and remove noise.

**Script:** `scripts/extract_phase3.py`

### Consolidation

Merged all phases with intelligent priority rules (Phase 2b > Phase 2 > Phase 1).

**Script:** `scripts/consolidate_v2.py`

### QA Validation

Comprehensive quality assurance including:
- Duplicate detection and merging
- Narrative text removal (English and Bulgarian)
- Name pattern validation
- Spot-check sampling
- Cyrillic-to-Latin transliteration

**Scripts:** `scripts/qa_validation.py`, `scripts/data_cleanup.py`

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

## Output Format

The final CSV contains 15 columns:

| Column | Description | Example |
|--------|-------------|---------|
| Date | Survey date (M-DD-YY format) | 3-16-09 |
| Team | Team letter (A-D) | B |
| Start Unit | First survey unit number | 40001 |
| End Unit | Last survey unit number | 40025 |
| Leader | Team leader name | Adela |
| Walkers_Original | Team members (may include Cyrillic) | Н. Кечева \| В. Генчева |
| Walkers_Transliterated | Latin script version | N. Kecheva \| V. Gencheva |
| PDA_Operator | PDA operator if identified | Nadja |
| Paper_Recorder | Paper form recorder if identified | Vera |
| Data_Editor | GIS/data editor if identified | - |
| Author | Form author if identified | Petra |
| XLS_Source | Source Excel file | ELH09 SurveySummary.xls |
| PDF_Source | Source PDF/diary file | B_2010Summary.pdf |
| Extraction_Notes | Extraction quality notes | Extracted from diary |
| QA_Notes | Quality assessment notes | Complete |

---

## Directory Structure

```text
claude_extraction/
├── scripts/
│   ├── extract_phase1.py          # Excel extraction
│   ├── extract_phase2.py          # English diary extraction
│   ├── extract_phase2b_walkers.py # PDF/extended extraction
│   ├── extract_phase3.py          # NLP cleaning
│   ├── parse_diaries.py           # Diary parsing utilities
│   ├── parse_bulgarian_diaries_2011.py
│   ├── parse_team_a_2011.py       # Team A narrative parser
│   ├── consolidate_v2.py          # Data merging
│   ├── qa_validation.py           # Quality assurance
│   ├── data_cleanup.py            # Narrative text removal
│   └── run_extraction.py          # Main orchestration
├── outputs/
│   ├── final_attribution_v2_cleaned_edited.csv  # FINAL OUTPUT
│   ├── extraction-accuracy-report.md
│   ├── extraction-summary-report.md
│   ├── narrative-cleanup-summary.md
│   ├── qa-validation-report.md
│   ├── submission-readme.md
│   └── submission-checklist.md
└── venv/                          # Python virtual environment
```

---

## Installation

```bash
cd claude_extraction
python3 -m venv venv
./venv/bin/pip install pandas openpyxl xlrd python-docx
```

Additional system dependencies for document conversion:
- `antiword` - for .doc files
- `pandoc` - for .docx files

---

## Known Limitations

1. **Name Variations:** Mix of full names, initials, and diminutives across sources. Some entries contain "[unclear]" where handwriting was illegible.

2. **Role Data:** PDA operator and paper recorder fields are sparsely populated (<5% coverage) due to limited source documentation.

3. **Bulgarian Diary Parsing:** Narrative-style entries required specialised parsers. Some location descriptions were initially captured as names and required cleanup.

4. **Missing Data:** 57 survey days (27%) lack walker data due to unavailable source documentation.

---

## Quality Assurance

### Extraction Accuracy: 91.1%

Post-extraction manual review identified:
- **14 entries** with narrative text fragments incorrectly captured as names
- **1 entry** with misread handwriting

All issues corrected in final output. See `outputs/extraction-accuracy-report.md` for details.

### Validation Checks Performed

- No duplicate Date+Team combinations
- All dates in valid format
- All team values valid (A-D)
- No narrative text in walker names
- Cyrillic names transliterated to Latin script
- Spot-check sampling (10 random records)

---

## Documentation

| File | Description |
|------|-------------|
| `outputs/submission-readme.md` | Complete package documentation for AKB |
| `outputs/submission-checklist.md` | Submission sign-off checklist |
| `outputs/extraction-accuracy-report.md` | Accuracy analysis after manual review |
| `outputs/extraction-summary-report.md` | Technical extraction methodology |
| `outputs/narrative-cleanup-summary.md` | Log of narrative text cleanup |
| `outputs/qa-validation-report.md` | QA validation results |

---

## Development History

This extraction pipeline was developed collaboratively with Claude Code (Anthropic) over multiple sessions:

1. **Initial pipeline:** Phase 1 (Excel) and Phase 2 (English diaries) extraction
2. **Phase 2b extension:** PDF summaries and Bulgarian diary extraction
3. **Consolidation:** Intelligent merging of all data sources
4. **QA and cleanup:** Narrative text removal, transliteration, validation
5. **Manual review:** Final corrections and accuracy assessment

**Extraction accuracy achieved:** 91.1% (154/169 entries correct before manual review)

---

## Contact

**Project Lead:** Dr. Adela Sobotkova
**Extraction Pipeline:** Claude Code (Anthropic)
**Completion Date:** November 2025
