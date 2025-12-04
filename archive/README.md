# TRAP Attribution Extraction - Archive

**Project Completion:** 23 November 2025
**QA Verification Complete:** 4 December 2025
**Archive Reorganised:** 4 December 2025
**Walker Data Coverage:** 100% Complete (274/274 records)

This directory contains completed work from the collaborative TRAP attribution data extraction project.

## Archive Structure

```text
archive/
├── project-management/       # Project planning, summaries, and session logs
│   ├── planning/             # Planning documents (9 files)
│   ├── summaries/            # Project summaries and status reports
│   └── cc-interactions/      # Claude Code session transcripts (59 files)
├── extraction-activities/    # Core extraction work by activity domain
│   ├── diary-extraction/     # Diary extraction planning (COMPLETED)
│   ├── name-disambiguation/  # Name mapping work (COMPLETED)
│   ├── supersession/         # PRIMARY source substitution (COMPLETED)
│   └── investigations/       # Data issue investigations
├── quality-assurance/        # ALL QA documentation consolidated
│   ├── guidance/             # QA standards, templates, pilot plan
│   ├── runsheets/            # All team verification runsheets (17+)
│   ├── automation/           # Automation infrastructure and test outputs
│   └── discrepancies/        # Issue tracking and discrepancy logs
├── outputs/                  # Extraction reports and data outputs
│   ├── reports/              # All extraction reports by phase
│   └── data/                 # Intermediate data and snapshots
├── infrastructure/           # Scripts, logs, and backups
│   ├── scripts/              # Python extraction scripts (~51 files)
│   ├── logs/                 # Script execution logs
│   └── backups/              # Attribution.csv backups by date
└── superseded/               # Deprecated and historical work
    ├── old-versions/         # Superseded output files
    └── legacy-work/          # Old extraction work (antigravity)
```

---

## Directory Contents

### project-management/

Project coordination and documentation:

- **planning/** - Completed planning documents including:
  - `akb-submission-todo.md` - AKB submission checklist (completed)
  - `name-standardisation-plan.md` - Name standardisation strategy (completed)
  - `role-extraction-checklist.md` - Role extraction checklist (completed)
  - `leader-verification-plan.md` - Leader verification plan
  - `documentation-update-plan.md` - Documentation update planning

- **summaries/** - Project status reports:
  - `work-summary.md` - Overall work summary
  - `date-discrepancy-analysis.md` - Date discrepancy analysis
  - `repo-migration.md` - Repository migration notes

- **cc-interactions/** - Claude Code session transcripts (20 Nov - 4 Dec 2025)
  - 59 session transcripts documenting the entire project

### extraction-activities/

Core extraction work organised by activity domain:

- **diary-extraction/** - Diary extraction planning (COMPLETED)
  - `diary-extraction-plan.md`, `diary-search-results.md`

- **name-disambiguation/** - Name variant analysis and mappings (COMPLETED)
  - 698 mappings in authoritative file
  - `name-mapping.csv` here is historical (282 entries)
  - Authoritative version at `outputs/name-mapping.csv`

- **supersession/** - PRIMARY source substitution review (COMPLETED)
  - Team A and B supersession reports
  - Source comparison documentation

- **investigations/** - Data issue investigation runsheets
  - `ambiguous-dates-investigation-runsheet.md`
  - `missing-dates-diary-investigation.md`

### quality-assurance/

**All QA documentation consolidated in one location:**

- **guidance/** - QA standards and templates:
  - `qa-guidance.md` - QA process guidance (primary reference)
  - `qa-issue-template.md` - Template for QA issues
  - `qa-pilot-plan.md` - QA pilot approach planning

- **runsheets/** - Team verification runsheets (17+ files):
  - Kazanlak 2009 Spring: Teams A, B, C, D, E
  - Kazanlak 2010 Spring: Teams A, B, D
  - Kazanlak 2011 Autumn: Teams A, B, C, D
  - Elhovo 2009 Autumn: Teams A, B, C
  - Elhovo 2010 Autumn: Teams A, combined
  - Plus QA reports: `name-mapping-qa-report.md`, `extraction-accuracy-report.md`

- **automation/** - QA automation infrastructure:
  - `qa-automation-plan.md` - Automation planning
  - `qa-queue.yaml`, `qa-verification-queue.yaml` - Queue configuration
  - `qa-prompt-template.md`, `qa-runsheet-template.md` - Templates
  - `known-corrections-reference.md` - 89 known corrections
  - **test-outputs/** - Test run outputs and validation reports

- **discrepancies/** - Issue tracking:
  - `qa-discrepancies-log.md` - Discrepancy tracking during extraction

### outputs/

Extraction reports and data outputs:

- **reports/** - Analysis reports by project phase:
  - `extraction/` - Season-specific extraction reports
  - `final/` - Comprehensive quality summary and resolution report
  - `phase1-extraction/` - Initial extraction phase documentation
  - `survey-unit-extraction/` - Survey unit extraction work

- **data/** - Intermediate data files:
  - `intermediate/` - Working data from extraction phases
    - `diary-extracts/` - 6 text files from team diaries
    - `role-extractions/` - 8 role extraction CSV files
  - `snapshots/` - Point-in-time data snapshots

### infrastructure/

Scripts, logs, and backups:

- **scripts/** - One-off extraction and processing scripts (~51 files):
  - Extraction: `extract_*.py` - Team/season-specific
  - Parsing: `parse_*.py` - Diary parsing utilities
  - Corrections: `apply_*.py`, `correct_*.py` - Data corrections
  - Updates: `update_*.py` - Batch data updates

- **logs/** - Script execution logs

- **backups/** - Attribution.csv backups:
  - `20251122-20251124/` - 20 backups from initial extraction
  - `20251125/` - 3 backups from name standardisation
  - Pre-QA corrections backup

### superseded/

Deprecated and historical work:

- **old-versions/** - Superseded output files:
  - Earlier attribution.csv versions
  - Historical documentation

- **legacy-work/** - Old extraction work (antigravity project):
  - Scripts, logs, outputs from earlier approach

---

## Current Working Files

Active files remain in repository root directories:

- `outputs/attribution.csv` - Main attribution data (274 records)
- `outputs/name-mapping.csv` - Authoritative name mappings (698 entries)
- `outputs/source-inventory.md` - Source catalogue
- `outputs/qa-final-report.md` - Final QA verification report
- `outputs/qa-final-verification.md` - Detailed verification summary
- `planning/follow-up-actions.md` - Future work requiring external evidence
- `scripts/` - 8 core scripts (consolidate_v2.py, apply_qa_corrections.py, etc.)

---

## Archive Maintenance

When archiving files:

1. Place in appropriate category directory
2. Document completion status and key outcomes
3. Reference related files still in active use
4. Update this README with new sections

---

**Total archived files:** ~200 files across 6 top-level directories
**Project completion:** 23 November 2025
**QA verification:** 4 December 2025
**Last reorganised:** 4 December 2025
**GitHub Repository:** https://github.com/saross/trap-extraction
