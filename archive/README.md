# TRAP Attribution Extraction - Archive

**Project Completion:** 23 November 2025
**QA Verification Complete:** 4 December 2025
**Last Reorganised:** 4 December 2025
**Walker Data Coverage:** ✅ 100% Complete (274/274 records)

This directory contains completed work from the collaborative TRAP attribution data extraction project.

## Archive Structure

```text
archive/
├── backups/                  # Attribution.csv backups organised by date
│   ├── 20251122-20251124/    # 20 backups from initial extraction phases
│   ├── 20251125/             # 3 backups from name standardisation
│   └── attribution.csv.backup_pre_qa_corrections_20251202
├── cc-interactions/          # Claude Code session transcripts (20 Nov - 4 Dec)
├── diary-extraction/         # Diary extraction planning documents (COMPLETED)
├── docs/                     # Archived working documentation
├── extraction-reports/       # Older extraction phase reports (6 files)
├── intermediate-data/        # Working data files from extraction phases
│   ├── diary-extracts/       # 6 text extracts from team diaries
│   └── role-extractions/     # 8 role extraction CSV files
├── investigation-runsheets/  # Investigation tracking documents
├── logs/                     # Script execution logs (6 files)
├── name-disambiguation/      # Name variant analysis and mappings (COMPLETED)
├── old-versions/             # Superseded output files and documentation
│   └── documentation/        # Historical documentation files
├── planning/                 # Completed planning documents (5 files)
├── project-summaries/        # Status reports and tracking documents
├── qa-automation/            # QA automation templates and queues (6 files)
├── qa-automation-test/       # QA automation test output
├── qa-runsheets/             # Individual team QA runsheets (17 files)
├── reports/                  # Analysis reports by project phase
│   ├── extraction/           # 5 extraction reports
│   ├── final/                # 2 comprehensive final reports
│   ├── phase1-extraction/    # Initial extraction documentation
│   └── survey-unit-extraction/ # Survey unit extraction work
├── scripts/                  # One-off extraction/processing scripts (~40 files)
└── supersession-project/     # Source supersession review (COMPLETED)
```

## Directory Contents

### backups/

Attribution.csv backups organised into dated subdirectories:

- **20251122-20251124/** - 20 backups from initial extraction phases
  - Phase 1/2 baselines, date corrections, diary extraction, leader standardisation
- **20251125/** - 3 backups from name standardisation work
- **attribution.csv.backup_pre_qa_corrections_20251202** - Pre-QA corrections backup

### cc-interactions/

Claude Code session transcripts documenting the entire project:

- `2025-11-20-a.txt` - Initial project setup
- `2025-11-21-[a-f].txt` - 6 sessions
- `2025-11-22-[a-c].txt` - 3 sessions
- `2025-11-23-[a-n].txt` - 14 sessions (100% coverage achieved)
- `2025-11-24-[a-i].txt` - 9 sessions (survey unit extraction)
- `2025-11-25-[a-d].txt` - 4 sessions (name standardisation, cleanup)
- `2025-12-01-[a-g].txt` - 7 sessions (QA verification)

### docs/

Archived working documentation:

- `qa-discrepancies-log.md` - QA discrepancy tracking during extraction
- `plan-su-form-role-scan.md` - Survey unit form role scanning plan
- `qa-issue-template.md` - Template for QA issues
- `qa-guidance.md` - QA process guidance documentation

### extraction-reports/

Older extraction phase reports:

- `leader-role-standardisation-report.md` - Leader role standardisation details
- `missing-survey-units-extracted.csv` - Missing survey units analysis
- `survey-unit-number-extraction-report.md` - Survey unit extraction report
- `task-completion-final-summary.md` - Task completion summary
- `walker-standardisation-report.md` - Walker standardisation details
- `name-mapping-qa-report.md` - Name mapping QA report

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

- `akb-submission-todo.md` - AKB submission checklist (completed)
- `qa-automation-plan.md` - QA automation planning (completed)
- `qa-pilot-plan.md` - QA pilot approach planning (completed)
- `source-observations-enhancement.md` - Source observation improvements
- `source-observations-test-plan.md` - Test plan for source observations
- `name-standardisation-plan.md` - Name standardisation strategy (completed)
- `role-extraction-checklist.md` - Role extraction checklist (completed)
- `leader-verification-plan.md` - Leader verification plan (deferred to QA)
- `documentation-update-plan.md` - Documentation update planning

### qa-automation/

QA automation templates and configuration (QA phase complete):

- `qa-queue.yaml` - Team QA queue configuration
- `qa-verification-queue.yaml` - Final verification queue
- `qa-corrections.md` - Corrections documentation
- `qa-prompt-template.md` - QA prompt template
- `qa-runsheet-template.md` - Runsheet template
- `known-corrections-reference.md` - Known corrections reference (89 corrections)

### qa-runsheets/

Individual team QA runsheets (17 files):

**Kazanlak 2009 Spring:** Teams A, B, C, D, E
**Kazanlak 2010 Spring:** Teams A, B, D
**Kazanlak 2011 Autumn:** Teams A, B, C, D
**Elhovo 2009 Autumn:** Teams A, B, C
**Elhovo 2010 Autumn:** Teams A, combined

### reports/

Analysis reports organised by project phase:

- **extraction/** - Season-specific extraction reports (Kazanluk 2009/2010/2011, Elhovo 2009)
- **final/** - Comprehensive quality summary and resolution report
- **phase1-extraction/** - Initial extraction phase documentation
- **survey-unit-extraction/** - Survey unit extraction work (24 Nov 2025)

### scripts/

One-off extraction and processing scripts (~40 files):

**Extraction scripts:** `extract_*.py` - Team/season-specific extraction
**Parsing scripts:** `parse_*.py` - Diary parsing utilities
**Correction scripts:** `apply_*.py`, `correct_*.py` - Data corrections
**Update scripts:** `update_*.py` - Batch data updates
**Test scripts:** `test_*.py` - Testing utilities
**Superseded:** `consolidate.py` - Superseded by consolidate_v2.py

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

### QA Verification (27 November - 4 December 2025)

- **Location:** `qa-automation/`, `qa-runsheets/`
- **Scope:** Comprehensive QA verification of all 274 records across 5 field seasons
- **Status:** COMPLETED - 89 corrections verified and applied
- **Output:** `outputs/qa-final-report.md`, `outputs/qa-final-verification.md`
- **Key results:**
  - All seasons verified: Kazanlak 2009/2010/2011, Elhovo 2009/2010
  - 89 corrections documented and applied
  - 2 FLAG_ONLY issues remain (pending project-level resolution)

## Current Working Files

Active files remain in repository root directories:

- `outputs/attribution.csv` - Main attribution data (274 records)
- `outputs/name-mapping.csv` - Authoritative name mappings (698 entries)
- `outputs/source-inventory.md` - Source catalogue
- `outputs/qa-final-report.md` - Final QA verification report
- `outputs/qa-final-verification.md` - Detailed verification summary
- `outputs/qa-corrections-manifest-comprehensive.json` - All corrections manifest
- `planning/follow-up-actions.md` - Future work requiring external evidence
- `scripts/` - 8 core scripts (consolidate_v2.py, apply_qa_corrections.py, etc.)

## Archive Maintenance

When archiving files:

1. Create appropriate subdirectory with README.md explaining context
2. Document completion status and key outcomes
3. Reference related files still in active use
4. Update this top-level README with new archive sections

---

**Total archived files:** ~200 files across 25+ directories
**Project completion:** 23 November 2025
**QA verification:** 4 December 2025
**Last updated:** 4 December 2025
**GitHub Repository:** https://github.com/saross/trap-extraction
