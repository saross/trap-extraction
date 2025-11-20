# Phase 2b PDF Extraction Instructions for Claude Code

## Overview
This document provides instructions for extracting walker/team member information from TRAP survey PDFs using vision capabilities in Claude Code.

## Context
The TRAP data extraction pipeline needs walker (team member) information for 179 date/team combinations that are currently missing this data. This information exists in scanned PDF forms but requires vision-based extraction due to handwritten content.

## Input Data
A CSV file will be provided listing the date/team combinations that need walker data:
- Location: `claude_extraction/outputs/missing_walkers.csv`
- Columns: `Date, Team`
- Example: `2010-03-17, B`

## PDF Types and Extraction Targets

### Type 1: Daily Progress Forms
**Location Pattern**: `*/Project Records/Team */FieldRecords/*Summary.pdf` or `*/Field Records/Day_*.pdf`

**Layout**: 3 forms per page (stacked vertically)

**Extraction Targets** (for each form on each page):
1. **Team Letter**: Upper right corner of form
2. **Date**: Immediately to the left of team letter (format: DD/MM/YYYY or similar)
3. **Team Leader**: Just below the team letter
4. **Walkers**: Box labeled "Walkers" in upper right area - extract all names/initials
5. **Author**: Field labeled "Author" - extract name

**Test File**: `Kazanluk/2010/Project Records/Team B/FieldRecords/B_2010Summary.pdf`

### Type 2: Survey Unit Forms
**Location Pattern**: `*/Project Records/Team */FieldRecords/*.pdf` or `*/*/{YYYYMMDD}.pdf`

**Layout**: Multiple survey unit forms per file, may be rotated

**Extraction Targets**:
1. **Date**: Extract from filename (YYYYMMDD format, e.g., `B_20100317.pdf` → `2010-03-17`)
2. **Team**: Extract from folder path (`Team B` → `B`)
3. **Walker Initials**: Bottom-most data entry grid, lower left corner (bottom row)
   - Usually 5 small boxes for initials
   - Sometimes fewer walkers (empty boxes)
   - Sometimes more walkers (initials written outside boxes)
   - **Important**: Combine initials from ALL pages in the file (they should be the same)

**Test File**: `Kazanluk/2010/Project Records/Team B/FieldRecords/B_20100317.pdf`

## Extraction Strategy

### Priority Order
1. **First**: Try Daily Progress Forms (more structured, includes dates)
2. **Second**: Try Survey Unit Forms (fallback, requires filename date matching)

### For Each Missing Date/Team Combination:
1. Search for matching PDF files:
   - Daily Progress: Look for files in `Team {X}/FieldRecords/` or `Team {X}/Field Records/`
   - Survey Unit: Look for `{YYYYMMDD}.pdf` files matching the date
2. Extract walker information using vision
3. Record the source PDF filename

## Output Format

Create a CSV file: `claude_extraction/outputs/phase2b_pdf_walkers.csv`

**Columns**:
```
Date,Team,Walkers,Team_Leader,Author,PDF_Source,Extraction_Notes
```

**Example Row**:
```
2010-03-17,B,"Martin | Petra | Nadja | Ljubo | Adela",Adela,Petra,B_20100317.pdf,"Extracted from survey unit forms, pages 1-3"
```

## Extraction Guidelines

### Name/Initial Extraction
- Extract names and initials as written
- Separate multiple names with ` | ` (space-pipe-space)
- Preserve capitalization
- If handwriting is unclear, note in `Extraction_Notes`

### Date Handling
- Normalize all dates to ISO format: `YYYY-MM-DD`
- Daily Progress Forms: Extract from form itself
- Survey Unit Forms: Extract from filename

### Team Handling
- Normalize to single uppercase letter: `A`, `B`, `C`, `D`, `E`

### Notes Field
- Record any extraction uncertainties
- Note if initials were unclear or ambiguous
- Note which type of form was used
- Note page numbers if helpful

## Quality Checks

For each extraction:
1. Verify date is in 2009-2011 range
2. Verify team is A-E
3. Verify at least some walker data was extracted
4. Note if extraction confidence is low

## Handling Edge Cases

### Multiple Forms Per File
- Daily Progress: Extract from each form (3 per page)
- Survey Unit: Combine initials from all pages

### Rotated Pages
- Survey unit forms may be rotated 90° or 180°
- Use vision to identify orientation

### Unclear Handwriting
- Extract best guess
- Note uncertainty in `Extraction_Notes`
- Mark with `[?]` if very uncertain, e.g., `"JD | [?]MT | SR"`

### Missing Information
- If walkers box is empty, leave `Walkers` field empty
- If form is illegible, note in `Extraction_Notes`

## Example Workflow

1. Load `missing_walkers.csv`
2. For first row (e.g., `2010-03-17, B`):
   - Search for `Team B` PDFs from March 2010
   - Find `B_20100317.pdf`
   - Open PDF with vision
   - Extract initials from bottom grids on all pages
   - Combine: `"VP | IN | ART"` (example)
   - Write to output CSV
3. Repeat for all rows
4. Save `phase2b_pdf_walkers.csv`

## Files to Process

The script `generate_missing_walkers_list.py` will create the input file with all date/team combinations needing walker data.

## Success Criteria

- Extract walker data for as many of the 179 missing records as possible
- Provide source PDF filename for each extraction
- Note any uncertainties or issues in the Notes field
- Output valid CSV that can be merged with existing data
