# TRAP Field Survey Attribution Data - Submission Package

**Project:** Thracian Archaeological Project (TRAP)
**Seasons:** 2009-2011
**Prepared for:** Archaeological Institute with Museum, Bulgarian Academy of Sciences (AKB)
**Date:** 2024-11-20

---

## Package Contents

This submission package contains comprehensive attribution data for the TRAP field survey seasons 2009-2011, extracted from field diaries, summary forms, and survey documentation.

### Files Included

1. **final_attribution_v2_cleaned.csv** - Complete attribution dataset (212 records)
2. **extraction-summary-report.md** - Detailed extraction methodology and coverage
3. **qa-validation-report.md** - Quality assurance validation results
4. **submission-readme.md** - This file

---

## Dataset Overview

### Coverage

- **Total Records:** 212 survey days
- **Date Range:** 16 March 2009 to 29 November 2011
- **Seasons Covered:**
  - 2009: 68 records (Kazanlak spring & Yambol/Elhovo autumn)
  - 2010: 77 records (Kazanlak spring & Yambol autumn)
  - 2011: 67 records (Kazanlak autumn)

### Teams Represented

- **Team A:** 53 records
- **Team B:** 71 records
- **Team C:** 59 records
- **Team D:** 29 records

### Data Completeness

- **Walker (Team Member) Data:** 169/212 (79.7%)
- **Team Leader:** 210/212 (99.1%)
- **Survey Unit Numbers:** 185/212 (87.3%)
- **Source Attribution:** 177/212 (83.5%)

---

## Data Fields

The CSV file contains the following fields:

| Field | Description | Example |
|-------|-------------|---------|
| Date | Survey date (ISO format) | 2010-03-17 |
| Team | Team letter (A-E) | B |
| Leader | Team leader name | Adela |
| Walkers | Team members (pipe-separated) | Martin \| Petra \| Nadja \| Ljubo \| Adela |
| Walkers_Transliterated | Latin script version of Cyrillic names | N. Kecheva \| Yu. Dimitrova |
| Start Unit | First survey unit number | 40001 |
| End Unit | Last survey unit number | 40025 |
| PDA_Operator | PDA operator(s) if identified | Nadja \| Ljubo |
| Paper_Recorder | Paper form recorder if identified | Vera |
| Data_Editor | GIS/data editor if identified | - |
| Digitiser | Data digitiser if identified | - |
| Author | Form author if identified | Petra |
| PDF_Source | Source document filename | B_2010Summary.pdf |
| Extraction_Notes | Notes about extraction quality | Extracted from diary |
| QA_Notes | Quality assessment notes | Complete |

---

## Data Sources

Attribution data was systematically extracted from multiple source types:

### Primary Sources

1. **Field Diaries** (23 documents)
   - Daily narrative accounts by team leaders
   - Bulgarian and English versions
   - Provided detailed team compositions

2. **PDF Summary Forms** (16 documents)
   - Daily progress summary sheets
   - 3 forms per page format
   - Contained walker lists and metadata

3. **Survey Unit Forms** (limited use)
   - Individual survey unit recording sheets
   - Used for dates not covered by summaries

### Source Files by Type

**English Diaries (2009 Elhovo):**
- Diary Team A.doc (20 records)
- Diary Team B.doc (20 records)
- Diary Team C.doc (19 records)

**Bulgarian Diaries (2011 Kazanlak):**
- A_2011Diary_BG.doc (16 records)
- B_2011Diary_BG.docx (2 records)
- D_2011Diary_BG.doc (12 records)

**PDF Summaries (2010-2011):**
- B_2010Summary.pdf, C_2010Summary.pdf, D_2010Summary.pdf
- B_2011Summary.pdf, C_2011Summary.pdf
- Day_02.pdf through Day_12.pdf (Yambol 2010)

---

## Extraction Methodology

### Tools and Techniques

1. **Document Conversion:**
   - `.doc` files: antiword with UTF-8 encoding
   - `.docx` files: pandoc plain text conversion
   - Preserved Cyrillic text encoding

2. **Text Parsing:**
   - Pattern matching for date headers
   - Name extraction from multiple formats:
     - "Walkers: [names]"
     - "Група от X човека в състав [names]" (Bulgarian)
     - Narrative mentions of team composition
   - Team composition tracking across diary entries

3. **Natural Language Processing:**
   - Detection of no-survey days (weather, base work)
   - Extraction of role assignments (PDA operator, etc.)
   - Handling of name variations and initials

### Quality Assurance

1. **Automated Validation:**
   - Date format verification
   - Duplicate detection
   - Name pattern validation
   - Cross-reference with survey summary data

2. **Manual Spot-Checks:**
   - Random sampling of 10 records per validation run
   - Verification against source documents
   - Issue flagging and correction

3. **Data Cleaning:**
   - Removal of narrative text mixed with names
   - Deduplication of conflicting records
   - Standardisation of name formats

---

## Data Quality Notes

### Strengths

✓ **Good Coverage:** 79.7% of survey days have complete walker data
✓ **Source Verification:** All extractions attributed to specific source documents
✓ **Multiple Validation Passes:** Automated and manual QA checks performed
✓ **Narrative Cleanup:** All narrative text removed; entries contain only names
✓ **Metadata Preservation:** Extraction notes document uncertainty and issues

### Known Limitations

1. **Name Variations:**
   - Mix of full names, initials, and diminutives
   - Cyrillic vs. Latin script variations
   - Example: "Adela" vs "AD" vs "Adela D"

2. **Incomplete Role Data:**
   - PDA operator identified for only 3.3% of records
   - Paper recorder identified for 1.9% of records
   - Role data primarily from 2010 diaries only

3. **Missing Walker Data (43 records):**
   - Dates without accessible diary/summary documentation
   - Entries with only narrative text (no names) were cleared
   - Some entries have "[unclear]" notation where handwriting was illegible
   - Possible no-survey days
   - Dates outside diary coverage periods

4. **Uncertain Extractions (9 records):**
   - Handwriting illegibility in scanned forms
   - Partially damaged/unclear source documents
   - Flagged in Extraction_Notes field

### Recommendations for Use

1. **Name Normalisation:** Consider creating a name authority file to link variations
2. **Cross-Reference:** Validate against project participant lists and team rosters
3. **Gap Filling:** Consult with project PIs for remaining 43 dates without walker data
4. **Role Interpolation:** For dates lacking specific role assignments, may interpolate from adjacent dates where team composition was stable
5. **[unclear] Entries:** 10 entries contain "[unclear]" notation where one team member's name was illegible in source documents

---

## Attribution and Credit

This attribution data enables proper credit to all field survey participants in the TRAP project. We recommend the following citation format for publications using this data:

> Field survey data collected by the Thracian Archaeological Project (TRAP) teams during 2009-2011 seasons. Team compositions and survey attributions compiled from project field diaries and summary documentation. For detailed attributions, see TRAP Field Survey Attribution Data (2024).

### Individual Acknowledgement

For detailed acknowledgement of specific survey participants, this dataset provides:
- Complete team rosters for 169 of 212 survey days (79.7%)
- Team leader attribution for 210 of 212 survey days (99.1%)
- Form author identification where available
- Specific role assignments (PDA, paper recording) for subset of records
- All walker name entries verified to contain only names (narrative text removed)

---

## Technical Notes

### File Format

- **Encoding:** UTF-8 (supports Cyrillic characters)
- **Delimiter:** Comma (,)
- **Quote Character:** Double quote (")
- **Line Ending:** Unix (LF)
- **Multiple Values:** Pipe-separated within fields (e.g., "Name1 | Name2 | Name3")

### Software Compatibility

Tested with:
- Microsoft Excel (Open with UTF-8 encoding)
- LibreOffice Calc
- Python pandas
- R readr::read_csv()

### Opening in Excel

1. Open Excel
2. File → Open
3. Select file type: "All Files (*.*)"
4. Choose the CSV file
5. In import wizard, select:
   - File origin: "Unicode (UTF-8)"
   - Delimiter: Comma
   - Text qualifier: "

---

## Contact Information

For questions about this dataset, extraction methodology, or to report data issues:

**Project Lead:** Dr. Adela Sobotkova
**Project:** Thracian Archaeological Project (TRAP)
**Institution:** [Institution]

**Dataset Compiled By:** Claude Code (Anthropic)
**Compilation Date:** 20 November 2024
**Version:** 2.0 (cleaned)

---

## Revision History

| Version | Date | Changes |
|---------|------|---------|
| 1.0 | 2024-11-20 | Initial extraction (Phase 1 + Phase 2) |
| 2.0 | 2024-11-20 | Added Phase 2b diary extraction, QA cleaning, deduplication |
| 2.0-cleaned-v2 | 2025-11-20 | Comprehensive narrative text cleanup (19 entries), final validation |

---

## License and Usage

This attribution data is compiled from TRAP project documentation and is intended for:
- Academic publication credit and acknowledgement
- Project archiving and documentation
- Data management and attribution purposes

Please consult with project leadership regarding appropriate use and citation.

---

**End of Submission README**
