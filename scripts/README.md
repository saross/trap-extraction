# TRAP Attribution Extraction Scripts

**Last Updated:** 23 November 2025
**Python Version:** 3.9+
**Dependencies:** pandas>=1.3.0

This directory contains Python scripts for extracting field survey attribution data from TRAP (Tundzha Regional Archaeological Project) diaries and field documentation covering 2009-2011 Kazanluk field seasons.

---

## Overview

The scripts in this directory were developed iteratively over a 4-day intensive extraction effort (20-23 November 2025) using a collaborative human-AI workflow. Scripts are organised by extraction phase, data type, and purpose.

**Total Scripts:** 45+ Python scripts
**Lines of Code:** ~10,000+ lines
**Extraction Coverage:** 100% walker data (268/268 records)

---

## Directory Structure

```
scripts/
├── Core Extraction Scripts       # Main extraction workflow
├── Data Correction Scripts       # Date and name corrections
├── Diary Extraction Scripts      # Diary-specific parsers
├── Name Disambiguation Scripts   # Name resolution
├── Analysis & QA Scripts         # Quality assurance
└── Utility Scripts               # Helper functions
```

---

## Core Extraction Scripts

### Phase-Based Extraction (Original Workflow)

These scripts represent the initial multi-phase extraction approach:

**extract_phase1.py**
- Initial extraction from Excel SurveySummary files
- Creates baseline attribution.csv with 76.1% coverage
- Usage: `python extract_phase1.py`

**extract_phase2.py**
- Adds role data from PDF sources
- Standardises leader entries
- Usage: `python extract_phase2.py`

**extract_phase2b_walkers.py**
- Extracts walker names from PDF files
- Supplements Excel data with PDF sources
- Usage: `python extract_phase2b_walkers.py`

**extract_phase3.py**
- Data cleaning and standardisation
- Applies name mappings
- Usage: `python extract_phase3.py`

### Modern Extraction Scripts (Diary-Based)

These scripts superseded the phase-based approach by extracting directly from diary sources:

**extract_diary_walkers.py** ⭐ (Primary extraction script)
- Extracts walker data from structured diary entries
- Handles both Bulgarian and English diaries
- Includes Bulgarian Cyrillic to Latin transliteration
- Supports multiple diary formats (Day X, date headers, narrative)
- Usage: `python extract_diary_walkers.py`
- **Most versatile and frequently used script**

**extract_narrative_walkers.py**
- Extracts walker data from narrative diary sections
- Used for general project narratives (e.g., Kazanluk 2009)
- Pattern matching for walker lists in prose
- Usage: `python extract_narrative_walkers.py`

**extract_kazanluk_2009.py**
- Specialised extractor for Kazanluk 2009 general diary
- Handles narrative format with team assignments
- Usage: `python extract_kazanluk_2009.py`

**extract_kazanluk_2010.py**
- Specialised extractor for Kazanluk 2010 diaries
- Processes Team C diary with date-based entries
- Usage: `python extract_kazanluk_2010.py`

---

## Data Correction Scripts

### Date Error Corrections

**correct_date_error.py**
- Corrects 2010-03-08 → 2010-04-08 date error
- Transfers survey units to correct date
- Creates timestamped backup
- Usage: `python correct_date_error.py`

**correct_kazanluk_2011_date_error.py**
- Corrects 2011-11-10 → 2011-10-21 date error (Team D)
- Updates walker list with missing participant
- Evidence-based correction using diary Day 8 entry
- Creates multiple backups with investigation report
- Usage: `python correct_kazanluk_2011_date_error.py`

### Name Corrections

**apply_name_corrections.py**
- Applies canonical name mappings from name-mapping.csv
- 111 replacements across 73 records
- Handles multiple variants per canonical name
- Creates backup before applying changes
- Usage: `python apply_name_corrections.py`

**standardize_leader_as_walker.py**
- Ensures leaders are included in walker lists
- Applied to 139 records (52% of dataset)
- Standardisation for consistency
- Usage: `python standardize_leader_as_walker.py`

---

## Diary Extraction Scripts

### Team-Specific Extractors

**extract_team_a_diary.py**
- Extracts Team A walker data from Elhovo 2010 diary
- Handles structured daily entries
- Usage: `python extract_team_a_diary.py`

**extract_team_b_diary_new.py**
- Extracts Team B walker data from Elhovo 2010 diary
- PRIMARY source for supersession project
- Usage: `python extract_team_b_diary_new.py`

### Diary Parsers

**parse_diaries.py**
- General-purpose diary parser
- Handles multiple date formats
- Usage: `python parse_diaries.py`

**parse_bulgarian_diaries_2011.py**
- Specialised parser for 2011 Bulgarian diaries
- Cyrillic text handling
- Usage: `python parse_bulgarian_diaries_2011.py`

**parse_team_c_diary.py**
- Team C diary parser (2009)
- Usage: `python parse_team_c_diary.py`

**parse_team_a_2011.py**
- Team A diary parser (2011)
- Usage: `python parse_team_a_2011.py`

---

## Name Disambiguation Scripts

**disambiguate_petra.py**
- Disambiguates Petra Janouchová vs Petra Tušlová
- Uses seasonal attendance patterns
- Usage: `python disambiguate_petra.py`

**apply_petra_manual_disambiguation.py**
- Applies manual Petra disambiguation decisions
- Usage: `python apply_petra_manual_disambiguation.py`

**prioritise_ambiguous_names.py**
- Analyses name-mapping.csv for ambiguous entries
- Generates priority list for manual review
- Usage: `python prioritise_ambiguous_names.py`

---

## Analysis & QA Scripts

### Coverage Analysis

**analyse_coverage.py**
- Calculates walker data coverage statistics
- Identifies records with missing data
- Usage: `python analyse_coverage.py`

**check_current_failed_extractions.py**
- Identifies records where extraction failed
- Cross-references with source inventory
- Usage: `python check_current_failed_extractions.py`

**generate_missing_walkers_list.py**
- Creates CSV of records missing walker data
- Prioritises for manual extraction
- Usage: `python generate_missing_walkers_list.py`

### Quality Assurance

**qa_validation.py**
- Comprehensive data validation checks
- Verifies data integrity and consistency
- Usage: `python qa_validation.py`

**qa_name_mapping_sources.py**
- Validates name-mapping.csv pdf_sources field
- Cross-checks against available PDFs
- Usage: `python qa_name_mapping_sources.py`

### Data Cleaning

**data_cleanup.py**
- General data cleaning operations
- Standardises formats and removes duplicates
- Usage: `python data_cleanup.py`

**clean_stale_missing_walker_flags.py**
- Removes outdated "MISSING: Walkers" QA flags
- Used after successful extractions
- Usage: `python clean_stale_missing_walker_flags.py`

---

## PDF Extraction Scripts

**extract_authors_all_pdfs.py**
- Batch extracts walker names from all PDFs
- OCR text processing
- Usage: `python extract_authors_all_pdfs.py`

**extract_authors_pdf_kaz2009.py**
- Kazanluk 2009 PDF extraction
- Usage: `python extract_authors_pdf_kaz2009.py`

**extract_authors_pdf_kaz2010.py**
- Kazanluk 2010 PDF extraction
- Usage: `python extract_authors_pdf_kaz2010.py`

**interactive_pdf_extraction.py**
- Manual interactive PDF extraction tool
- User prompts for verification
- Usage: `python interactive_pdf_extraction.py`

**test_pdf_extraction.py**
- Tests PDF extraction functionality
- Usage: `python test_pdf_extraction.py`

---

## Role Extraction Scripts

**extract_roles_kaz2010.py**
- Extracts role data (PDA operator, etc.) from Kazanluk 2010 PDFs
- Limited coverage due to source constraints
- Usage: `python extract_roles_kaz2010.py`

**extract_roles_elh2010.py**
- Extracts role data from Elhovo 2010 PDFs
- Usage: `python extract_roles_elh2010.py`

---

## Update Scripts

**update_manual_extractions.py**
- Applies manual extraction corrections
- Batch updates from manual review files
- Usage: `python update_manual_extractions.py`

**update_team_a_attribution.py**
- Updates Team A entries with diary data
- Supersession project script
- Usage: `python update_team_a_attribution.py`

**update_team_c_entries.py**
- Updates Team C entries
- Usage: `python update_team_c_entries.py`

**update_kaz2010_walkers.py**
- Updates Kazanluk 2010 walker data
- Usage: `python update_kaz2010_walkers.py`

---

## Utility Scripts

**utils.py**
- Shared utility functions
- Date parsing, name standardisation, file I/O helpers
- Imported by other scripts
- **Do not run directly**

**consolidate.py**
- Consolidates extraction results from multiple sources
- Merges data with conflict resolution
- Usage: `python consolidate.py`

**consolidate_v2.py**
- Updated version of consolidation script
- Enhanced conflict handling
- Usage: `python consolidate_v2.py`

**run_extraction.py**
- Master script for running full extraction pipeline
- Executes phases sequentially
- Usage: `python run_extraction.py`

---

## Maintenance Scripts

**fix_diary_filenames.py**
- Standardises diary filename conventions
- Renames files to consistent format
- Usage: `python fix_diary_filenames.py`

**test_extraction.py**
- Unit tests for extraction functions
- Usage: `python test_extraction.py`

---

## Common Usage Patterns

### Full Extraction Pipeline (Historical)

```bash
# Phase-based extraction (original approach)
python extract_phase1.py          # Baseline from Excel
python extract_phase2.py          # Add roles from PDFs
python extract_phase2b_walkers.py # Add walkers from PDFs
python extract_phase3.py          # Clean and standardise
```

### Diary-Based Extraction (Modern Approach)

```bash
# Extract from diaries (superseded phase approach)
python extract_diary_walkers.py   # Primary extraction
python extract_narrative_walkers.py  # Narrative sections
python extract_kazanluk_2009.py   # Season-specific
python extract_kazanluk_2010.py   # Season-specific
```

### Data Corrections

```bash
# Apply corrections
python correct_date_error.py                    # Fix 2010 date
python correct_kazanluk_2011_date_error.py      # Fix 2011 date
python apply_name_corrections.py                # Canonical names
python standardize_leader_as_walker.py          # Leader standardisation
```

### Quality Assurance

```bash
# Check data quality
python analyse_coverage.py                      # Coverage statistics
python check_current_failed_extractions.py      # Failed extractions
python qa_validation.py                         # Data validation
```

---

## Script Development Philosophy

### Coding Standards

All scripts follow these conventions (defined in `.claude/CLAUDE.md`):

1. **UK/Australian spelling** in all comments and documentation
2. **Verbose comments** - Header blocks, docstrings, inline comments
3. **PEP 8 compliance** - Python style guide adherence
4. **Type hints** - Function signatures annotated
5. **Pathlib** - Modern path handling (not os.path)
6. **Maximum line length:** 100 characters

### Common Patterns

**Backup Creation:**
```python
from pathlib import Path
import shutil
from datetime import datetime

def create_backup(file_path: Path) -> Path:
    """Create timestamped backup of file."""
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    backup_path = file_path.with_suffix(f".csv.backup_{timestamp}")
    shutil.copy2(file_path, backup_path)
    return backup_path
```

**CSV Reading/Writing:**
```python
import pandas as pd

# Read with explicit encoding for Cyrillic text
df = pd.read_csv(file_path, encoding='utf-8')

# Write with consistent parameters
df.to_csv(output_path, index=False, encoding='utf-8')
```

**Date Parsing:**
```python
from datetime import datetime

def parse_date(date_str: str) -> str:
    """Parse date string to ISO 8601 format."""
    # Handle multiple input formats
    for fmt in ['%d.%m.%Y', '%Y-%m-%d', '%d/%m/%Y']:
        try:
            dt = datetime.strptime(date_str, fmt)
            return dt.strftime('%Y-%m-%d')  # ISO 8601
        except ValueError:
            continue
    raise ValueError(f"Could not parse date: {date_str}")
```

**Bulgarian Transliteration:**
```python
CYRILLIC_TO_LATIN = {
    'А': 'A', 'Б': 'B', 'В': 'V', 'Г': 'G', 'Д': 'D',
    'Е': 'E', 'Ж': 'Zh', 'З': 'Z', 'И': 'I', 'Й': 'Y',
    'К': 'K', 'Л': 'L', 'М': 'M', 'Н': 'N', 'О': 'O',
    'П': 'P', 'Р': 'R', 'С': 'S', 'Т': 'T', 'У': 'U',
    'Ф': 'F', 'Х': 'Kh', 'Ц': 'Ts', 'Ч': 'Ch', 'Ш': 'Sh',
    'Щ': 'Sht', 'Ъ': 'A', 'Ь': 'Y', 'Ю': 'Yu', 'Я': 'Ya',
    # Lowercase mappings...
}

def transliterate(text: str) -> str:
    """Transliterate Bulgarian Cyrillic to Latin script."""
    result = []
    for char in text:
        result.append(CYRILLIC_TO_LATIN.get(char, char))
    return ''.join(result)
```

---

## Dependencies

**Required:**
- Python 3.9+
- pandas>=1.3.0

**Standard Library (No Installation):**
- csv (data reading/writing)
- re (regular expressions)
- pathlib (file path handling)
- datetime (date manipulation)
- shutil (file operations)
- sys, os (system operations)

**Installation:**
```bash
pip install -r ../requirements.txt
```

---

## Testing

**Unit Tests:**
- `test_extraction.py` - Tests extraction functions
- `test_pdf_extraction.py` - Tests PDF extraction

**Run Tests:**
```bash
python test_extraction.py
python test_pdf_extraction.py
```

**Manual Testing:**
- `interactive_pdf_extraction.py` - Interactive verification

---

## Known Limitations

1. **PDF OCR Quality:** Some PDFs have poor OCR requiring manual correction
2. **Name Variants:** Multiple spellings require name mapping (handled by name-mapping.csv)
3. **Diary Format Variability:** Different teams used different diary structures
4. **Role Data Coverage:** <50% due to limited source documentation
5. **Survey Units:** 6.7% of records missing units (not in source data)

---

## Archival Status

**Active Scripts:** Scripts used in final extraction (Nov 20-23, 2025)

**Superseded Scripts:** Early phase-based scripts retained for provenance

**No scripts deleted:** All development history preserved for reproducibility

---

## Script Authorship

**Primary Developer:** Shawn Ross (Macquarie University)
**AI Assistant:** Claude Code (Anthropic)
**Development Period:** 20-23 November 2025
**Methodology:** Collaborative human-AI development with manual verification

**Development Process:**
1. User defines extraction requirements
2. Claude Code drafts script
3. User tests and provides feedback
4. Claude Code refines based on results
5. Iterate until 100% coverage achieved

---

## Future Enhancements

Potential script improvements for future versions:

1. **Unit Test Coverage:** Expand test coverage for all extraction functions
2. **Type Checking:** Add mypy type checking to pre-commit hooks
3. **Logging:** Replace print statements with proper logging framework
4. **Configuration Files:** Move hardcoded paths to config files
5. **CLI Interface:** Add argparse for command-line arguments
6. **Documentation:** Generate API documentation with Sphinx

---

## Contact

**Maintainer:** Shawn Ross (Macquarie University)
**Email:** shawn.ross@mq.edu.au
**Project:** TRAP (Tundzha Regional Archaeological Project)

---

## License

**Code License:** Apache License 2.0 (see ../LICENSE)

```
Copyright 2025 Shawn Ross

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0
```

---

**Last Updated:** 23 November 2025
**Version:** 1.0.0
**Status:** Production (100% walker coverage achieved)
