# TRAP Walker Attribution Data

**Prepared for:** Archaeological Institute with Museum (AIM-BAS), Bulgarian Academy of Sciences

**Prepared by:** Dr. Adela Sobotkova, Macquarie University

**Date:** November 2025

---

## Overview

This dataset contains team composition and attribution data extracted from the Tundzha Regional Archaeological Project (TRAP) field survey records for the 2009-2011 seasons.

The data enables proper credit attribution for all survey participants in the project archives and future publications.

---

## Data File

**Filename:** `final_attribution_v2_cleaned_edited.csv`

**Format:** UTF-8 encoded CSV (Comma-Separated Values)

**Records:** 269 survey day entries

---

## Coverage Summary

| Metric | Value |
|--------|-------|
| Total survey day records | 269 |
| Leader coverage | 267/269 (99.3%) |
| Walker coverage | 223/269 (82.9%) |
| Author coverage | 209/269 (77.7%) |
| PDA Operator coverage | 23/269 (8.6%) |
| GPS Operator coverage | 18/269 (6.7%) |
| Paper Recorder coverage | 9/269 (3.3%) |

### By Season

| Season | Records | Walker Coverage |
|--------|---------|-----------------|
| 2009 | 125 | 80.8% |
| 2010 | 77 | 81.8% |
| 2011 | 67 | 88.1% |

---

## Column Descriptions

| Column | Description | Example |
|--------|-------------|---------|
| Date | Survey date (M-DD-YY format) | 3-16-09 |
| Team | Team letter (A-E) | B |
| Start Unit | First survey unit number | 40001 |
| End Unit | Last survey unit number | 40025 |
| Leader | Team leader name | Adela |
| Walkers_Original | Team members (may include Cyrillic) | Н. Кечева \| В. Генчева |
| Walkers_Transliterated | Latin script version | N. Kecheva \| V. Gencheva |
| PDA_Operator | Personal Digital Assistant (PDA) operator | Nadja |
| Paper_Recorder | Paper form recorder | Vera |
| Data_Editor | Geographic Information System (GIS) / data editor | - |
| Author | Form author | Petra |
| XLS_Source | Source Excel file | ELH09 SurveySummary.xls |
| PDF_Source | Source PDF / diary file | B_2010Summary.pdf |
| Extraction_Notes | Extraction quality notes | Extracted from diary |
| QA_Notes | Quality assessment notes | Complete |

---

## Data Sources

The attribution data was extracted from:

- **Excel Survey Summaries:** ELH09, KAZ10, YAM10, KAZ11 SurveySummary files
- **English Diaries:** Team diaries from 2009 Elhovo and Kazanlak seasons
- **Bulgarian Diaries:** Team diaries across all seasons (Cyrillic text transliterated)
- **PDF Daily Progress Forms:** Scanned field forms with team compositions

---

## Name Conventions

Walker names appear in various forms across source documents:

- **Full names:** Adela Sobotkova
- **First names:** Adela
- **Initials:** A.S.
- **Diminutives:** Bara (for Barbora)
- **Cyrillic:** Н. Кечева (transliterated in Walkers_Transliterated column)

A separate name mapping file (`name-mapping-draft.csv`) documents 282 name variants and their canonical forms.

---

## Known Limitations

1. **46 records** (17%) lack walker data due to unavailable source documentation (XLS-only records)

2. **Role fields** (PDA_Operator, GPS_Operator, Paper_Recorder) have limited coverage (3-9%) as this information was only recorded in select diary sources (primarily Elhovo 2010 Team B and Kazanlak 2010 Teams A-B)

3. **Name standardisation** is partial; the data preserves original name forms from source documents

---

## Usage Notes

- The pipe character (`|`) separates multiple walker names
- Empty cells indicate data not available in source documents
- The `[unclear]` notation indicates illegible handwriting in source documents

---

## Contact

**Dr. Adela Sobotkova**
Macquarie University
adela.sobotkova@mq.edu.au

---

## Acknowledgements

Data extraction performed collaboratively with Claude Code (Anthropic), November 2025.

All field survey participants from 2009-2011 are credited in this dataset for their contributions to the TRAP project.
