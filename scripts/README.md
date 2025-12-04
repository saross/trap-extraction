# TRAP Attribution Extraction Scripts

**Last Updated:** 4 December 2025
**Python Version:** 3.9+
**Dependencies:** pandas>=1.3.0

This directory contains the core Python scripts for processing and validating TRAP attribution data. One-off extraction scripts have been archived to `archive/scripts/`.

---

## Overview

The scripts in this directory represent the essential, reusable tools for working with the TRAP attribution dataset. These scripts were developed collaboratively (20 November - 4 December 2025) using a human-AI workflow.

**Active Scripts:** 8 core scripts
**Archived Scripts:** ~40 one-off extraction scripts (see `archive/scripts/`)
**Data Coverage:** 100% walker data (274/274 records)

---

## Active Scripts

```text
scripts/
├── analyse_coverage.py      # Coverage analysis tool
├── apply_qa_corrections.py  # Apply QA corrections from manifest
├── consolidate_v2.py        # Core data consolidation (current version)
├── data_cleanup.py          # Reusable data cleanup utilities
├── qa_validation.py         # Data validation checks
├── run_extraction.py        # Main extraction orchestration
├── utils.py                 # Shared utility functions
├── verify-survey-unit-coverage.py  # Survey unit verification
└── README.md                # This file
```

---

## Script Descriptions

### analyse_coverage.py

Coverage analysis tool for attribution data.

- Calculates walker data coverage statistics
- Identifies records with missing data
- Usage: `python analyse_coverage.py`

### apply_qa_corrections.py

Applies QA corrections from the corrections manifest.

- Reads corrections from `qa-corrections-manifest-comprehensive.json`
- Applies CORRECTION and ADD_RECORD types to attribution.csv
- Creates backup before applying changes
- Usage: `python apply_qa_corrections.py`
- **May be needed for future corrections**

### consolidate_v2.py

Core consolidation logic for merging extraction results.

- Consolidates data from multiple extraction sources
- Enhanced conflict handling and resolution
- Usage: `python consolidate_v2.py`
- **Note:** Supersedes `consolidate.py` (archived)

### data_cleanup.py

Reusable data cleaning utilities.

- General data cleaning operations
- Standardises formats and removes duplicates
- Usage: `python data_cleanup.py`

### qa_validation.py

Comprehensive data validation checks.

- Verifies data integrity and consistency
- Checks unit presence/continuity, walker/leader presence
- R1 validation (role holders in walkers)
- R2 validation (leader in walkers)
- Usage: `python qa_validation.py`

### run_extraction.py

Main orchestration script for extraction pipeline.

- Executes extraction phases sequentially
- Coordinates other extraction scripts
- Usage: `python run_extraction.py`

### utils.py

Shared utility functions used by other scripts.

- Date parsing and formatting
- Name standardisation helpers
- File I/O operations
- **Do not run directly - imported by other scripts**

### verify-survey-unit-coverage.py

Survey unit coverage verification tool.

- Checks survey unit data completeness
- Identifies missing unit numbers
- Usage: `python verify-survey-unit-coverage.py`

---

## Archived Scripts

~40 one-off extraction scripts have been archived to `archive/scripts/`. These include:

- **Extraction scripts:** `extract_*.py` - Team and season-specific extraction
- **Parsing scripts:** `parse_*.py` - Diary parsing utilities
- **Correction scripts:** `apply_*.py`, `correct_*.py` - One-off data corrections
- **Update scripts:** `update_*.py` - Batch data updates
- **Test scripts:** `test_*.py` - Testing utilities
- **Superseded:** `consolidate.py` - Replaced by consolidate_v2.py

These scripts were used during the initial extraction phase (20-23 November 2025) and are preserved for provenance and reproducibility. See `archive/scripts/` for the full list.

---

## Common Usage

### Quality Assurance

```bash
# Run validation checks
python qa_validation.py

# Check coverage statistics
python analyse_coverage.py

# Verify survey unit coverage
python verify-survey-unit-coverage.py
```

### Apply Corrections

```bash
# Apply corrections from manifest (if needed in future)
python apply_qa_corrections.py
```

---

## Dependencies

**Required:**

- Python 3.9+
- pandas>=1.3.0

**Installation:**

```bash
pip install -r ../requirements.txt
```

---

## Coding Standards

All scripts follow these conventions (defined in `.claude/CLAUDE.md`):

1. **UK/Australian spelling** in all comments and documentation
2. **Verbose comments** - Header blocks, docstrings, inline comments
3. **PEP 8 compliance** - Python style guide adherence
4. **Type hints** - Function signatures annotated
5. **Pathlib** - Modern path handling (not os.path)
6. **Maximum line length:** 100 characters

---

## Contact

**Maintainer:** Shawn Ross (Macquarie University)
**Email:** shawn.ross@mq.edu.au
**Project:** TRAP (Tundzha Regional Archaeological Project)

---

## Licence

**Code Licence:** Apache License 2.0 (see ../LICENSE)

---

**Last Updated:** 4 December 2025
**Version:** 1.1.0
**Status:** Production (274/274 records verified)
