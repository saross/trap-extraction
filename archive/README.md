# TRAP Attribution Extraction - Archive

**Project Completion:** 23 November 2025
**Walker Data Coverage:** ✅ 100% Complete (268/268 records)

This directory contains completed work from the collaborative TRAP attribution data extraction project.

## Archive Structure

```
archive/
├── cc-interactions/          # Exported Claude Code conversation transcripts (15+ sessions)
├── supersession-project/     # Source supersession review and corrections (COMPLETED)
├── name-disambiguation/      # Name variant analysis and mappings (COMPLETED)
├── diary-extraction/         # Diary extraction planning documents (COMPLETED)
├── project-summaries/        # Interim status reports and tracking documents
├── outputs/
│   ├── backups/              # 17 timestamped attribution.csv backups
│   └── documentation/        # 2 historical documentation files
└── reports/
    ├── extraction/           # 5 extraction reports from various phases
    ├── final/                # 2 comprehensive final reports
    └── phase1-extraction/    # Initial extraction phase documentation
```

## Complete Archive Manifest

```
archive/
├── cc-interactions/                          # Claude Code conversation exports
│   ├── 2025-11-20-a.txt                      # Initial project conversations
│   ├── 2025-11-21-[a-f].txt                  # 21 Nov work sessions (6 files)
│   ├── 2025-11-22-[a-c].txt                  # 22 Nov work sessions (3 files)
│   └── 2025-11-23-[a-e].txt                  # 23 Nov work sessions (5 files)
│
├── supersession-project/                     # ✅ COMPLETED (23 Nov 2025)
│   ├── README.md                             # Project documentation and outcomes
│   ├── superseded-sources-comprehensive-review.md  # Main project report
│   ├── elhovo-2010-team-b-diary-comparison.md     # Initial Team B analysis
│   ├── team-b-supersession-report.md         # Detailed Team B comparison
│   ├── team-b-diary-new-extraction.csv       # Team B PRIMARY source data
│   ├── team-a-supersession-report.md         # Detailed Team A comparison
│   └── team-a-diary-extraction.csv           # Team A PRIMARY source data
│
├── name-disambiguation/                      # ✅ COMPLETED (Nov 2025)
│   ├── README.md                             # Project documentation and outcomes
│   ├── ambiguous-names-review.md             # Comprehensive ambiguity analysis
│   ├── name-corrections-report.md            # Systematic correction documentation
│   ├── name-mapping.csv                      # Canonical name mappings (282 entries)
│   ├── name-mapping-qa-report.md             # Quality assurance review
│   └── petra-disambiguation-report.md        # "Petra" variant analysis
│
├── diary-extraction/                         # ✅ COMPLETED (Nov 2025)
│   ├── README.md                             # Project documentation
│   ├── diary-extraction-plan.md              # Comprehensive extraction strategy
│   ├── diary-extraction-report.md            # Diary availability and priorities
│   └── diary-search-results.md               # Catalogue of available sources
│
├── project-summaries/                        # Interim status and tracking
│   ├── README.md                             # Section documentation
│   ├── work-summary.md                       # Status snapshot (21 Nov 2025)
│   ├── follow-up-actions.md                  # Outstanding actions tracker
│   └── date-discrepancy-analysis.md          # Date inconsistency analysis
│
├── intermediate-data/                        # Intermediate CSV files
│   ├── manual-extraction-work.csv            # Manual extraction working file
│   ├── final_attribution_v2_cleaned.csv      # Cleaned v2 attribution
│   ├── missing_walkers.csv                   # Missing walker records
│   ├── phase1_summary.csv                    # Phase 1 summary data
│   ├── phase2b_pdf_walkers.csv               # Phase 2b PDF walker data
│   ├── phase2_roles.csv                      # Phase 2 role data
│   ├── phase3_cleaned.csv                    # Phase 3 cleaned data
│   └── team_c_2009_diary_parsed.csv          # Team C 2009 diary parsing
│
├── outputs/                                  # Superseded output files
│   ├── final_attribution.csv                 # Early attribution version
│   ├── final_attribution_v2.csv              # Attribution v2
│   └── final_attribution_v2_cleaned.ods      # LibreOffice cleaned version
│
└── reports/                                  # Completed analysis reports
    ├── extraction-accuracy-report.md         # Accuracy analysis
    └── phase1-extraction/                    # Phase 1 extraction documentation
        ├── extraction-summary-report.md      # Phase 1 summary
        ├── narrative-cleanup-summary.md      # Narrative cleanup work
        ├── qa-validation-report.md           # QA validation
        ├── submission-checklist.md           # Submission checklist
        └── submission-readme.md              # Phase 1 submission readme
```

**Total archived files:** 49 files across 10 directories

## Archive Organisation Principles

Files are archived when they represent:
1. **Completed projects/phases** - Work that has been finished and verified
2. **Superseded outputs** - Files replaced by updated versions
3. **Interim snapshots** - Status reports from specific points in time
4. **Historical documentation** - Records of decisions and analyses

## Current Working Files

The following files remain in `outputs/` as active working documents:
- `attribution.csv` - Main attribution data (current version)
- `manual-extraction-guide.md` - Extraction methodology reference
- `source-inventory.md` - Source catalogue and status tracker
- `submission-readme.md` - Current submission documentation

## Major Completed Projects

### Supersession Project (23 November 2025)
- **Location:** `archive/supersession-project/`
- **Scope:** Systematic review and correction of 14 records using PRIMARY sources
- **Status:** COMPLETED - All identified issues resolved
- **See:** `supersession-project/README.md`

### Name Disambiguation (November 2025)
- **Location:** `archive/name-disambiguation/`
- **Scope:** Review and resolution of ambiguous walker names
- **Status:** COMPLETED - 79% resolved, 21% documented for review
- **See:** `name-disambiguation/README.md`

### Diary Extraction Planning (November 2025)
- **Location:** `archive/diary-extraction/`
- **Scope:** Planning framework for diary-based data extraction
- **Status:** COMPLETED - Foundation for supersession project
- **See:** `diary-extraction/README.md`

### Final Reports (23 November 2025)
- **Location:** `archive/reports/final/`
- **Scope:** Comprehensive data quality and extraction resolution documentation
- **Status:** COMPLETED - Project conclusion documentation
- **Key files:**
  - `data-quality-summary.md` - Complete quality assessment (100% walker coverage)
  - `failed-extractions-resolution-report.md` - How all extraction gaps were resolved
- **Significance:** Documents achievement of 100% walker data coverage and all quality improvements

### Attribution CSV Backups (20-23 November 2025)
- **Location:** `archive/outputs/backups/`
- **Scope:** 17 timestamped backups documenting extraction progress
- **Status:** Archived - Preserved for provenance
- **Key backups:**
  - Phase 1 baseline (76.1% coverage)
  - Phase 2 improvements (139 leader standardisations)
  - Date error corrections (2 corrections applied)
  - Final state (100% coverage achieved)

## Archive Maintenance

When archiving files:
1. Create appropriate subdirectory with README.md explaining context
2. Document completion status and key outcomes
3. Reference related files still in active use
4. Update this top-level README with new archive sections

## Notes

- 17 timestamped backups of `attribution.csv` archived in `outputs/backups/`
- CC conversation exports are dated in format `YYYY-MM-DD-[a-z].txt`
- Each archive subdirectory contains a README explaining its contents
- Final reports in `reports/final/` document 100% walker coverage achievement

---

**Total archived files:** 70+ files across 10 subdirectories
**Project completion:** 23 November 2025
**GitHub Repository:** https://github.com/saross/trap-extraction
