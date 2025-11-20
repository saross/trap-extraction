# TRAP Data Extraction Pipeline

This directory contains scripts to extract team composition and role attribution data from TRAP (Tundzha Regional Archaeology Project) survey records from 2009-2011.

## Overview

The extraction pipeline processes:
- **Excel files**: SurveySummary spreadsheets with team leaders, dates, and survey units
- **Word documents**: Team diaries with team composition and role information
- **PDF files** (fallback): Scanned Daily Progress Forms (only when data is missing from other sources)

## Installation

The virtual environment and dependencies are already set up. If you need to recreate:

```bash
cd /media/shawn/191c3b96-5fa5-4d0d-8805-0cf05d3d8468/synology/Adela/TRAP-WD-2020-04/claude_extraction
python3 -m venv venv
./venv/bin/pip install pandas openpyxl xlrd python-docx pdf2image pytesseract Pillow
```

## Usage

### Run Complete Pipeline

```bash
cd /media/shawn/191c3b96-5fa5-4d0d-8805-0cf05d3d8468/synology/Adela/TRAP-WD-2020-04/claude_extraction
./venv/bin/python3 scripts/run_extraction.py
```

This runs all phases in sequence:
1. Phase 1: Extract from Excel files
2. Phase 2: Extract from Word diaries
3. Consolidation: Merge and produce final CSV

### Run Individual Phases

```bash
# Phase 1 only (Excel extraction)
./venv/bin/python3 scripts/extract_phase1.py

# Phase 2 only (Diary extraction)
./venv/bin/python3 scripts/extract_phase2.py

# Consolidation only (requires Phase 1 & 2 outputs)
./venv/bin/python3 scripts/consolidate.py
```

## Output Format

The final output is `outputs/final_attribution.csv` with the following columns:

| Column | Description | Example |
|--------|-------------|---------|
| Date | ISO format YYYY-MM-DD | 2009-10-12 |
| Team | Letter designation | A |
| Start Unit | 5-digit survey unit number | 60000 |
| End Unit | 5-digit survey unit number | 60038 |
| Leader | Team leader name/initials | Adela |
| Walkers | All team members (pipe-separated) | Adela \| Martin \| Petra |
| PDA operator | Person who operated PDA in field | Adela |
| Paper recorder | Person who filled paper forms | Martin |
| Data editor | Person who edited polygons in GIS | Adela |
| Digitiser | Person who digitized paper forms | Petra |
| Notes | Interpolation suggestions and data quality notes | Missing walker data - consider PDF fallback |
| SurveySummary_Source | Source Excel file | ELH09 SurveySummary.xls |
| Diary_Source | Source diary file | A_Diary_En.docx |

## Directory Structure

```
claude_extraction/
├── scripts/
│   ├── utils.py              # Shared utility functions
│   ├── extract_phase1.py     # Excel extraction
│   ├── extract_phase2.py     # Diary extraction
│   ├── consolidate.py        # Data merging
│   └── run_extraction.py     # Main orchestration
├── outputs/
│   ├── phase1_summary.csv    # Phase 1 output
│   ├── phase2_roles.csv      # Phase 2 output
│   └── final_attribution.csv # FINAL OUTPUT
├── logs/
│   ├── phase1_extraction.log
│   ├── phase2_extraction.log
│   ├── consolidation.log
│   └── run_extraction.log
└── venv/                     # Python virtual environment
```

## Known Limitations

1. **Name Extraction**: Uses regex/NLP heuristics to extract names from free text. May occasionally include noise or miss names in unusual formats. Manual review recommended.

2. **KAZ09_SurveySummary.xls**: This file is poorly structured. Extraction attempts are made but results should be verified carefully.

3. **Diary Parsing**: Only English diaries are processed (`*_En.doc`, `*_En.docx`). Bulgarian diaries are skipped.

4. **Role Information**: Role data (PDA operator, Paper recorder, etc.) is sparse in diaries. Many entries will have empty role fields. The Notes column suggests where interpolation might help.

5. **PDF Extraction**: Not yet implemented. Currently, PDF fallback is noted in the Notes column but not automatically executed.

## Troubleshooting

### No output generated

Check the log files in `logs/` for error messages. Common issues:
- Missing source files
- Corrupted Excel/Word files
- Permission issues

### Names contain noise words

The `extract_names()` function in `utils.py` filters common noise words. If you find additional noise patterns, add them to the `noise_patterns` list.

### Dates not parsing correctly

The `normalize_date()` function handles multiple date formats. If you encounter a new format, add a pattern to the function.

### Missing data

Check the Notes column in the final output for suggestions on where data is missing and might be interpolated or extracted from PDFs.

## Version Control

This project uses git for version control. To commit your work:

```bash
cd /media/shawn/191c3b96-5fa5-4d0d-8805-0cf05d3d8468/synology/Adela/TRAP-WD-2020-04
git add claude_extraction/
git commit -m "Your commit message"
```

## Contact

For questions about the extraction pipeline, refer to the implementation plan in the Antigravity artifacts.
