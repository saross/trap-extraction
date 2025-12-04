# TRAP Data Extraction Walkthrough

## Overview
This walkthrough documents the process of extracting team composition and roles from TRAP survey data files (.xls, .xlsx, .doc, .docx).

## Work Directory
All work is located in: `/media/shawn/191c3b96-5fa5-4d0d-8805-0cf05d3d8468/synology/Adela/TRAP-WD-2020-04/DataExtractionWork/`

## Steps Taken

### 1. Environment Setup
- Created a virtual environment in `venv/`.
- Installed dependencies: `pandas`, `openpyxl`, `xlrd`, `python-docx`, `pdfminer.six`.

### 2. Data Extraction Script (`scripts/extract_data.py`)
- **Phase 1**: Parsed `SurveySummary` Excel files to extract Date, Team, Leader, and Unit ranges.
    - *Refinement*: Added flexible column matching for "Start SU" / "End SU".
- **Phase 2**: Parsed `Diary` Word files (.docx and .doc) to extract Team Members and Roles.
    - *Refinement*: Implemented NLP/Regex to extract only names/initials.
    - *Refinement*: Added 'Geospatial Data Editor' role extraction.
- **Phase 3**: Consolidated data into a single CSV.
    - *Refinement*: Filtered for 2009-2011.
    - *Refinement*: Cleaned up column names (`SurveySummary_Source`, `Diary_Source`).

### 3. Execution
Run the script from the `scripts` directory:
```bash
../venv/bin/python3 extract_data.py
```

### 4. Outputs
Generated CSV files in `outputs/`:
- `phase1_summary.csv`: Data from Excel summaries.
- `phase2_roles.csv`: Data from Diaries.
- `final_attribution.csv`: Consolidated data.

## Verification
- Verified that `final_attribution.csv` contains merged data from both sources.
- Confirmed dates are within 2009-2011.
- Confirmed Units are populated.
- Confirmed Names are extracted cleanly.

## Next Steps
- Review `final_attribution.csv` for any missing or misaligned data.
