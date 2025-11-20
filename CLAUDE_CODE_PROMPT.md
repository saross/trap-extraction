# Prompt for Claude Code: TRAP PDF Walker Extraction

Hi Claude Code! I need your help extracting walker (team member) information from scanned PDF forms using your vision capabilities.

## Quick Start

1. **Read the instructions**: `claude_extraction/CLAUDE_CODE_INSTRUCTIONS.md`
2. **Load the input**: `claude_extraction/outputs/missing_walkers.csv` (179 date/team combinations)
3. **Process PDFs**: Use vision to extract walker names/initials from the PDFs
4. **Output**: Create `claude_extraction/outputs/phase2b_pdf_walkers.csv`

## What You're Looking For

### Daily Progress Forms (Priority 1)
- **Location**: `*/Team */FieldRecords/*Summary.pdf` or `*/Field Records/Day_*.pdf`
- **Layout**: 3 forms per page
- **Extract**: "Walkers" box in upper right area of each form
- **Test file**: `Kazanluk/2010/Project Records/Team B/FieldRecords/B_2010Summary.pdf`

### Survey Unit Forms (Fallback)
- **Location**: `*/Team */FieldRecords/{YYYYMMDD}.pdf`
- **Layout**: Multiple forms per file, may be rotated
- **Extract**: Initials from bottom-most data entry grid, lower left corner (bottom row)
- **Test file**: `Kazanluk/2010/Project Records/Team B/FieldRecords/B_20100317.pdf`

## Output Format

CSV with columns:
```
Date,Team,Walkers,Team_Leader,Author,PDF_Source,Extraction_Notes
```

Example:
```
2010-03-17,B,"Martin | Petra | Nadja | Ljubo | Adela",Adela,Petra,B_20100317.pdf,"Extracted from survey unit forms, pages 1-3"
```

## Tips

- Separate multiple names with ` | ` (space-pipe-space)
- Combine initials from all pages in the same PDF file
- Note any uncertainties in `Extraction_Notes`
- If handwriting is unclear, make your best guess and note it

## Questions?

The full instructions in `CLAUDE_CODE_INSTRUCTIONS.md` have all the details. Good luck!
