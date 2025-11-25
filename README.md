# TRAP Archaeological Survey Attribution Data Extraction (2009-2011)

[![License](https://img.shields.io/badge/License-Apache%202.0%20%2F%20CC--BY%204.0-blue.svg)](LICENSE)
[![FAIR Compliance](https://img.shields.io/badge/FAIR-Compliant-green.svg)](STANDARDS-COMPLIANCE.md)

Extraction and curation of field walker attribution data from the Tundzha Regional Archaeological Project (TRAP) survey records covering the 2009, 2010, and 2011 Kazanluk field seasons.

**Project Status:** ✅ **COMPLETE** - 100% walker data coverage achieved (268/268 records), 89.18% survey unit coverage (239/268 records)

**Completion Date:** 23 November 2025 (walker data), 24 November 2025 (survey units)

**GitHub Repository:** https://github.com/saross/trap-extraction

---

## Quick Links

- [Data Dictionary](DATA-DICTIONARY.md) - Complete data model documentation
- [FAIR Compliance](STANDARDS-COMPLIANCE.md) - FAIR/FAIR4RS principles alignment
- [Data Quality Report](archive/reports/final/data-quality-summary.md) - Comprehensive quality assessment
- [Extraction Resolution Report](archive/reports/final/failed-extractions-resolution-report.md) - How 100% coverage was achieved
- [Citation File](CITATION.cff) - How to cite this dataset
- [Contributing Guidelines](CONTRIBUTING.md) - How to contribute improvements

---

## Project Summary

This project systematically extracted field walker (team member) attribution data from heterogeneous archaeological field documentation to enable proper credit for survey participants. Through automated diary extraction, manual narrative analysis, and rigorous quality assurance, we achieved **100% walker data coverage** across all 268 survey records.

### Final Results

| Metric | Value | Notes |
|--------|-------|-------|
| **Total survey day records** | **268** | Across 3 field seasons (2009, 2010, 2011) |
| **Walker data coverage** | **268/268 (100%)** | ✅ Complete |
| **Leader coverage** | **268/268 (100%)** | All team leaders documented |
| **Non-survey days** | **3** | Flagged with activities |
| **Data sources processed** | **15+ diaries** | English and Bulgarian |
| **Python scripts created** | **51 total** | 6 key extraction/QA scripts |
| **Date corrections applied** | **2** | Errors identified and fixed |

### Coverage Improvement

| Stage | Walker Coverage | Progress |
|-------|----------------|----------|
| Initial extraction | 202/269 (75.1%) | Baseline |
| After date error corrections | 204/268 (76.1%) | +1.0% |
| After diary extraction & QA | **268/268 (100%)** | **+23.9%** ✅ |

---

## Dataset Metadata (FAIR Compliance)

### Temporal Coverage
- **Start date:** 2009-03-03 (ISO 8601)
- **End date:** 2011-11-29 (ISO 8601)
- **Field seasons:** 5 survey campaigns across 3 years

### Spatial Coverage
- **Region:** Kazanluk Valley, Stara Zagora Province, Bulgaria
- **Survey type:** Intensive pedestrian field survey
- **Survey teams:** 5 teams (A, B, C, D, E)

### Data Collection Methodology
Field walker attribution data extracted from:
1. **Primary sources:** Team-specific English and Bulgarian diaries (15+ documents)
2. **Secondary sources:** Excel survey summaries, PDF daily progress forms
3. **Tertiary sources:** Scanned field forms, project reports

Extraction methods:
- Automated text extraction and regex pattern matching
- Manual narrative analysis for non-structured entries
- Quality assurance validation against source documents
- Leader standardisation policy (leaders are always walkers)

### Known Limitations
1. **Role data incomplete:** PDA operator, paper recorder, and other role fields have <50% coverage due to limited source documentation
2. **Survey units incomplete:** 29 records (10.82%) without survey unit numbers - 239/268 (89.18%) coverage: 28 records explained (alternative survey methodologies, weather cancellations, non-survey days), 1 record pending renumbering investigation (six-digit to five-digit unit conversion)
3. **Pre-FAIR project:** TRAP predates FAIR principles; this extraction applies retrospective data curation

See [DATA-DICTIONARY.md](DATA-DICTIONARY.md) for complete data model documentation.

---

## Primary Output

**Main deliverable:** `outputs/attribution.csv`

CSV file with 21 columns documenting 268 survey day records:
- **Core fields:** Date, Team, Start Unit, End Unit
- **Personnel fields:** Leader, Walkers (Original + Transliterated), PDA Operator, Paper Recorder, Data Editor, GPS Operator, Photographer, Author
- **Source fields:** XLS Source, PDF Source, Extraction Notes, QA Notes

See [DATA-DICTIONARY.md](DATA-DICTIONARY.md) for complete column definitions, controlled vocabularies, and expected coverage.

---

## Field Seasons Covered

### 2009 Spring (Kazanluk)
- **Dates:** 3-27 March 2009
- **Teams:** A, B, C, D, E
- **Records:** 63

### 2009 Autumn (Kazanluk)
- **Dates:** 14 October - 14 November 2009
- **Teams:** A, B, C
- **Records:** 11

### 2010 Spring (Kazanluk)
- **Dates:** 21 March - 15 April 2010
- **Teams:** A, B, C, D
- **Records:** 46

### 2010 Autumn (Kazanluk)
- **Dates:** 22-24 October, 2-15 November 2010
- **Teams:** A, B
- **Records:** 19

### 2011 Autumn (Kazanluk)
- **Dates:** 14-29 October, 1-29 November 2011
- **Teams:** A, B, C, D
- **Records:** 129

**Total:** 268 survey day records

---

## Key Extraction Scripts

Six core Python scripts perform extraction and quality assurance:

1. **`extract_team_a_diary.py`** - Extract Team A walker data from English diaries
2. **`extract_team_b_diary_new.py`** - Extract Team B walker data (2010-2011)
3. **`update_team_a_attribution.py`** - Update attribution CSV with Team A data
4. **`standardize_leader_as_walker.py`** - Ensure leaders included in walker lists (139 records updated)
5. **`clean_stale_missing_walker_flags.py`** - Remove obsolete QA flags (11 cleaned)
6. **`check_current_failed_extractions.py`** - Analyse extraction status

See [scripts/README.md](scripts/README.md) for installation instructions, usage examples, and troubleshooting.

**Note:** 39 additional utility scripts in `scripts/` directory support various data extraction and QA tasks.

---

## Data Quality Achievements

### Walker Data Extraction (100% Complete)

**Major improvements:**
1. **Leader standardisation (Session 2025-11-23-k)**
   - Updated 139 records (52%) to include team leaders in walker lists
   - Applied consistent policy: leaders are always walkers

2. **2011-11-29 Team B resolution**
   - Confirmed legitimate survey day with team leader
   - Identified all 4 walkers from scanned forms
   - Resolved final diary coverage gap

3. **Stale flag cleanup**
   - Removed 11 obsolete "MISSING: Walkers" flags
   - Reduced QA flagged records from 32 to 21

### Date Corrections Applied

Two date errors identified and corrected:

1. **2010-04-08 Team C** (was incorrectly recorded as 2010-03-08)
   - Evidence: Team C diary shows no March 8 entry, April 8 entry present
   - Unit sequence confirms April 8 timing

2. **2011-10-21 Team D** (was incorrectly recorded as 2011-11-10)
   - Evidence: Team D diary covers only 14 Oct - 2 Nov (no November entries)
   - Unit sequence: 41088-41152 falls between Oct 20 and Oct 22

See [archive/reports/final/data-quality-summary.md](archive/reports/final/data-quality-summary.md) for comprehensive quality documentation.

---

## Data Sources

### Primary Sources (Team Diaries)

**English Language Diaries:**
- A_2009Diary_En.docx
- A_2010Diary_En.docx
- B_2009Diary_En.docx
- B_2010Diary_En.docx
- B_2011Diary_En.docx
- Team B Diary new.docx (2010, corrected version)

**Bulgarian Language Diaries:**
- A_2010Diary_BG.docx
- A_2011Diary_BG.docx
- B_2011Diary_BG.docx
- C_2009Diary_BG.doc
- C_2010Diary_BG.doc
- D_2011Diary_BG.docx

**Other Team Diaries:**
- The Diary of Team C.doc (2009)
- Team D 2010 Kazanluk.docx

### Secondary Sources

**Excel Summaries:**
- Kaz09_SurveySummary.xls
- Kaz10_SurveySummary.xlsx
- Kaz11_SurveySummary.xlsx

**PDF Summary Forms:**
- A_2011Summary.pdf
- B_2011Summary.pdf
- C_2011Summary.pdf
- D_2011Summary.pdf

**Scanned Survey Forms:**
- B_20111129.pdf (critical for final gap resolution)

See [outputs/source-inventory.md](outputs/source-inventory.md) for complete source documentation.

---

## Installation and Usage

### Prerequisites
- Python 3.9 or higher
- pip package manager
- Virtual environment (recommended)

### Setup

```bash
# Clone repository
git clone https://github.com/saross/trap-extraction.git
cd trap-extraction

# Create virtual environment
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Verify installation
python -c "import pandas; print('Dependencies installed successfully')"
```

### Running Scripts

```bash
# Check extraction status
python scripts/check_current_failed_extractions.py
# Expected output: "268/268 records have walker data (100.0%)"

# Extract Team A walker data
python scripts/extract_team_a_diary.py

# Standardise leader inclusion
python scripts/standardize_leader_as_walker.py
```

See [scripts/README.md](scripts/README.md) for detailed usage instructions and troubleshooting.

---

## Project Structure

```text
trap-extraction/
├── README.md                           # This file
├── LICENSE                             # Apache 2.0 (code) / CC-BY 4.0 (data)
├── CITATION.cff                        # Citation metadata
├── CHANGELOG.md                        # Project milestones
├── DATA-DICTIONARY.md                  # Complete data model
├── STANDARDS-COMPLIANCE.md             # FAIR/FAIR4RS alignment
├── CONTRIBUTING.md                     # Contribution guidelines
├── requirements.txt                    # Python dependencies
├── codemeta.json                       # Software metadata
├── scripts/
│   ├── README.md                       # Script documentation
│   ├── extract_team_a_diary.py         # Team A extraction
│   ├── extract_team_b_diary_new.py     # Team B extraction
│   ├── update_team_a_attribution.py    # CSV update script
│   ├── standardize_leader_as_walker.py # Leader standardisation
│   ├── clean_stale_missing_walker_flags.py  # QA flag cleanup
│   ├── check_current_failed_extractions.py  # Status analysis
│   └── [39 additional utility scripts]
├── outputs/
│   ├── attribution.csv                 # PRIMARY OUTPUT (268 records)
│   ├── name-mapping.csv                # Canonical name mappings (698 entries)
│   └── source-inventory.md             # Source documentation
├── planning/
│   ├── akb-submission-todo.md          # AKB submission checklist
│   └── follow-up-actions.md            # Future work recommendations
├── archive/
│   ├── outputs/
│   │   ├── backups/                    # 17 timestamped backups
│   │   └── documentation/              # Historical docs
│   ├── reports/
│   │   ├── extraction/                 # 5 extraction reports
│   │   └── final/                      # 2 comprehensive reports
│   ├── cc-interactions/                # Claude Code session transcripts
│   ├── supersession-project/           # Source priority corrections
│   ├── name-disambiguation/            # Name mapping work
│   ├── diary-extraction/               # Extraction methodology
│   └── project-summaries/              # Field season summaries
└── inputs/                             # Source diaries and forms
```

---

## FAIR/FAIR4RS Compliance

This repository follows FAIR principles for data and FAIR4RS principles for research software:

### FAIR Data Principles
- ✅ **Findable:** GitHub URL, structured metadata (CITATION.cff)
- ✅ **Accessible:** Open repository, clear licence, standard protocols
- ✅ **Interoperable:** CSV format, documented data model, controlled vocabularies
- ✅ **Reusable:** Complete provenance, clear licence, comprehensive documentation

### FAIR4RS Software Principles
- ✅ **Findable:** Software metadata (codemeta.json), version control
- ✅ **Accessible:** Open repository, Apache 2.0 licence
- ✅ **Interoperable:** Standard formats, documented dependencies (requirements.txt)
- ✅ **Reusable:** Installation instructions, usage examples, contribution guidelines

See [STANDARDS-COMPLIANCE.md](STANDARDS-COMPLIANCE.md) for complete compliance documentation.

**Pragmatic approach:** TRAP is a pre-FAIR archaeological project. This extraction applies retrospective data curation while acknowledging limitations in achieving full domain standard alignment.

---

## Licence

This repository uses a dual licence approach:

- **Code and scripts** (`scripts/*.py`): [Apache License 2.0](https://www.apache.org/licenses/LICENSE-2.0)
- **Data and documentation** (`outputs/*.csv`, `*.md` files): [Creative Commons Attribution 4.0 International (CC-BY 4.0)](https://creativecommons.org/licenses/by/4.0/)

See [LICENSE](LICENSE) for complete licence text.

---

## Citation

If you use this dataset or scripts, please cite as:

```bibtex
@dataset{trap_attribution_2025,
  title = {TRAP Archaeological Survey Attribution Data (2009-2011)},
  author = {Ross, Shawn and Sobotkova, Adela},
  year = {2025},
  month = {11},
  version = {1.0.0},
  url = {https://github.com/saross/trap-extraction},
  note = {Data extraction assisted by Claude (Anthropic)}
}
```

See [CITATION.cff](CITATION.cff) for structured citation metadata.

---

## Project History

This extraction project was developed collaboratively with Claude Code (Anthropic) across multiple sessions in November 2025:

**Key milestones:**
- **20 Nov 2025:** Initial automated extraction work
- **21 Nov 2025:** Manual extraction phase for narrative diary entries
- **22 Nov 2025:** Failed extraction analysis and resolution
- **23 Nov 2025:** Leader standardisation (139 records updated)
- **23 Nov 2025:** Date error corrections (2 errors fixed)
- **23 Nov 2025:** 100% walker coverage achieved (final 64 records completed)
- **23 Nov 2025:** FAIR/FAIR4RS compliance documentation created

See [CHANGELOG.md](CHANGELOG.md) for detailed project timeline.

**Session transcripts:** Complete Claude Code interaction history preserved in `archive/cc-interactions/`

---

## Future Work

Recommended enhancements documented in [planning/follow-up-actions.md](planning/follow-up-actions.md):

1. ~~**Role data extraction:**~~ ✅ **Completed** - 76 role fields populated (24 Nov 2025)
2. **Survey unit completion:** 29 records without survey units (28 explained, 1 pending renumbering investigation)
3. ~~**Name standardisation:**~~ ✅ **Completed** - 698 name mappings applied to all personnel columns (25 Nov 2025)
4. **DOI registration:** Register persistent identifier via Zenodo for long-term citability
5. **Publication links:** Add bibtex references to published TRAP papers
6. **Secondary QA:** Independent quality review by another LLM (Gemini 3)
7. **Participant research:** Identify remaining uncertain participants (Lizzy, Sharon, Yavor L)

See [planning/akb-submission-todo.md](planning/akb-submission-todo.md) for AKB submission preparation checklist.

---

## Documentation Files

| File | Description |
|------|-------------|
| [README.md](README.md) | This file - project overview |
| [DATA-DICTIONARY.md](DATA-DICTIONARY.md) | Complete data model with controlled vocabularies |
| [STANDARDS-COMPLIANCE.md](STANDARDS-COMPLIANCE.md) | FAIR/FAIR4RS principles alignment |
| [CHANGELOG.md](CHANGELOG.md) | Project milestones and timeline |
| [CITATION.cff](CITATION.cff) | Structured citation metadata |
| [LICENSE](LICENSE) | Dual licence text (Apache 2.0 / CC-BY 4.0) |
| [CONTRIBUTING.md](CONTRIBUTING.md) | How to contribute improvements |
| [scripts/README.md](scripts/README.md) | Script installation and usage |
| [outputs/source-inventory.md](outputs/source-inventory.md) | Source documentation |
| [planning/follow-up-actions.md](planning/follow-up-actions.md) | Future work recommendations |
| [archive/reports/final/data-quality-summary.md](archive/reports/final/data-quality-summary.md) | Comprehensive quality report |
| [archive/reports/final/failed-extractions-resolution-report.md](archive/reports/final/failed-extractions-resolution-report.md) | How 100% coverage was achieved |

---

## Contact and Maintainers

**Project Lead:** Dr. Adela Sobotkova (Macquarie University)
**Data Custodian:** Dr. Shawn Ross (Macquarie University)
**Data Extraction:** Claude Code (Anthropic) - AI assistant

**TRAP Project:** Tundzha Regional Archaeological Project
**Institution:** Macquarie University, Sydney, Australia
**Partner Institution:** Archaeological Institute with Museum (AKB), Bulgarian Academy of Sciences

**GitHub Repository:** https://github.com/saross/trap-extraction
**Issues/Questions:** Please open an issue on GitHub

---

**Last Updated:** 25 November 2025
**Version:** 1.0.0
**Status:** ✅ Complete - 100% walker data coverage achieved, names standardised
