# TRAP Attribution Extraction - Archive

**Project Completion:** 23 November 2025
**Last Reorganised:** 25 November 2025
**Walker Data Coverage:** ✅ 100% Complete (268/268 records)

This directory contains completed work from the collaborative TRAP attribution data extraction project.

## Archive Structure

```text
archive/
├── backups/                  # Attribution.csv backups organised by date
│   ├── 20251122-20251124/    # 20 backups from initial extraction phases
│   └── 20251125/             # 3 backups from name standardisation
├── cc-interactions/          # 37 Claude Code session transcripts (20-25 Nov)
├── diary-extraction/         # Diary extraction planning documents (COMPLETED)
├── intermediate-data/        # Working data files from extraction phases
│   ├── diary-extracts/       # 6 text extracts from team diaries
│   └── role-extractions/     # 8 role extraction CSV files
├── investigation-runsheets/  # Investigation tracking documents
├── logs/                     # Script execution logs (6 files)
├── name-disambiguation/      # Name variant analysis and mappings (COMPLETED)
├── old-versions/             # Superseded output files and documentation
│   └── documentation/        # Historical documentation files
├── planning/                 # Completed planning documents
├── project-summaries/        # Status reports and tracking documents
├── reports/                  # Analysis reports by project phase
│   ├── extraction/           # 5 extraction reports
│   ├── final/                # 2 comprehensive final reports
│   ├── phase1-extraction/    # Initial extraction documentation
│   └── survey-unit-extraction/ # Survey unit extraction work
└── supersession-project/     # Source supersession review (COMPLETED)
```

## Directory Contents

### backups/

Attribution.csv backups organised into dated subdirectories:

- **20251122-20251124/** - 20 backups from initial extraction phases
  - Phase 1/2 baselines, date corrections, diary extraction, leader standardisation
- **20251125/** - 3 backups from name standardisation work

### cc-interactions/

37 Claude Code session transcripts documenting the entire extraction project:

- `2025-11-20-a.txt` - Initial project setup
- `2025-11-21-[a-f].txt` - 6 sessions
- `2025-11-22-[a-c].txt` - 3 sessions
- `2025-11-23-[a-n].txt` - 14 sessions (100% coverage achieved)
- `2025-11-24-[a-i].txt` - 9 sessions (survey unit extraction)
- `2025-11-25-[a-d].txt` - 4 sessions (name standardisation, cleanup)

### intermediate-data/

Working data files from extraction phases:

- **diary-extracts/** - 6 text files extracted from team diaries (2009)
- **role-extractions/** - 8 CSV files from role extraction work
- Various CSV files from extraction pipeline phases

### old-versions/

Superseded output files replaced by current versions:

- `final_attribution.csv`, `final_attribution_v2.csv` - Earlier attribution versions
- `final_attribution_v2_cleaned.ods` - LibreOffice cleaned version
- **documentation/** - Historical extraction guides

### planning/

Completed planning documents:

- `name-standardisation-plan.md` - Name standardisation strategy (completed)
- `role-extraction-checklist.md` - Role extraction checklist (completed)
- `leader-verification-plan.md` - Leader verification plan (deferred to QA)
- `documentation-update-plan.md` - Documentation update planning

### reports/

Analysis reports organised by project phase:

- **extraction/** - Season-specific extraction reports (Kazanluk 2009/2010/2011, Elhovo 2009)
- **final/** - Comprehensive quality summary and resolution report
- **phase1-extraction/** - Initial extraction phase documentation
- **survey-unit-extraction/** - Survey unit extraction work (24 Nov 2025)

## Major Completed Projects

### Supersession Project (23 November 2025)

- **Location:** `supersession-project/`
- **Scope:** Systematic review and correction using PRIMARY diary sources
- **Status:** COMPLETED
- **See:** `supersession-project/README.md`

### Name Disambiguation (22-25 November 2025)

- **Location:** `name-disambiguation/`
- **Scope:** Review and resolution of ambiguous walker names
- **Status:** COMPLETED - 698 mappings in authoritative file
- **Note:** `name-mapping.csv` here is historical (282 entries); authoritative version at `outputs/name-mapping.csv`
- **See:** `name-disambiguation/README.md`

### Diary Extraction Planning (November 2025)

- **Location:** `diary-extraction/`
- **Scope:** Planning framework for diary-based data extraction
- **Status:** COMPLETED
- **See:** `diary-extraction/README.md`

### Final Reports (23 November 2025)

- **Location:** `reports/final/`
- **Key files:**
  - `data-quality-summary.md` - Complete quality assessment (100% walker coverage)
  - `failed-extractions-resolution-report.md` - How all extraction gaps were resolved

## Current Working Files

Active files remain in repository root directories:

- `outputs/attribution.csv` - Main attribution data (268 records)
- `outputs/name-mapping.csv` - Authoritative name mappings (698 entries)
- `outputs/source-inventory.md` - Source catalogue
- `planning/akb-submission-todo.md` - AKB submission checklist
- `planning/follow-up-actions.md` - Future work requiring external evidence

## Archive Maintenance

When archiving files:

1. Create appropriate subdirectory with README.md explaining context
2. Document completion status and key outcomes
3. Reference related files still in active use
4. Update this top-level README with new archive sections

---

**Total archived files:** 144 files across 21 directories
**Project completion:** 23 November 2025
**Last updated:** 25 November 2025
**GitHub Repository:** https://github.com/saross/trap-extraction
