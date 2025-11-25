# Changelog

All notable changes to the TRAP Attribution Extraction project are documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [1.0.0] - 2025-11-23

### Project Completion

**Walker Data Extraction:** ✅ 100% Complete (268/268 records)

This release marks the completion of walker data extraction from all TRAP 2009-2011 Kazanluk field season documentation, achieving full attribution coverage.

### Added

#### Documentation (FAIR/FAIR4RS Compliance)
- **DATA-DICTIONARY.md** - Comprehensive data model documentation for 17 CSV columns
- **STANDARDS-COMPLIANCE.md** - FAIR/FAIR4RS principles compliance assessment
- **requirements.txt** - Python dependency specification (pandas>=1.3.0)
- **codemeta.json** - CodeMeta 2.0 structured software metadata
- **CITATION.cff** - Citation File Format for structured citations
- **LICENSE** - Dual licence: Apache 2.0 (code) + CC-BY 4.0 (data)
- **CHANGELOG.md** - Version history and notable changes
- **README.md** - Complete rewrite with FAIR metadata and 100% completion status

#### Archive Documentation
- **archive/README.md** - Enhanced with final reports section and completion status
- **archive/supersession-project/README.md** - Added obsolete file documentation
- **archive/cc-interactions/** - 15+ conversation transcripts from collaborative extraction

#### Scripts
- **scripts/correct_kazanluk_2011_date_error.py** - Date correction (2011-11-10 → 2011-10-21)
- **scripts/apply_name_corrections.py** - Canonical name standardisation (111 replacements)

### Changed

#### Data Quality Improvements
- **outputs/attribution.csv** - Updated to 268 records (100% walker coverage)
  - Corrected 2 date errors (2010-03-08 → 2010-04-08, 2011-11-10 → 2011-10-21)
  - Applied 111 canonical name replacements across 73 records
  - Standardised 139 leader entries (52% of records)
  - Extracted walker data from 10 diary sources (49 names added)
  - Resolved all 22 XLS-only records (10 successful extractions, 12 documented failures)

#### Documentation Updates
- **outputs/source-inventory.md** - Added completion status header
- **outputs/follow-up-actions.md** - Updated with completion status and outstanding enhancements
- **outputs/name-mapping.csv** - Updated status for all 283 entries (58 corrected, 6 invalid, 2 uncertain)

### Fixed

#### Date Corrections
- **2010-03-08 → 2010-04-08** (Kazanluk 2010, Team C)
  - Evidence: Diary begins 17 March, no 08 March entry; 08 April PDF exists
  - Impact: Corrected 1 record, transferred 32 survey units to correct date
  - Backup: `attribution.csv.backup_date_correction`

- **2011-11-10 → 2011-10-21** (Kazanluk 2011, Team D)
  - Evidence: Team D diary ends 2 November; Day 8 entry explicitly states 21.10.2011 with units 41088-41152
  - Impact: Corrected 1 record, added missing walker (А. Антонов)
  - Backup: `attribution.csv.backup_kazanluk2011_dateerror_*`
  - Documentation: `outputs/kazanluk-2011-date-error-report.md`

#### Name Standardisation
- Applied 111 canonical name replacements across 73 attribution records
- Resolved ambiguities:
  - **Helena vs Elena** - Standardised to "Elena" (confirmed in participant list)
  - **Petra** - Disambiguated Janouchová vs Tušlová based on season
  - **Adela** - Disambiguated Sobotkova vs Dorňáková in 2010-autumn records
  - **Julia** - Distinguished older (Kourilova) vs younger (Šašinková)
- Marked 6 OCR false positives as invalid (H., Hun, M, P, Olga, X)
- Identified 2 uncertain entries (Lizzy/Lisi - real person, full name being researched)

#### Source Corrections
- Updated 14 records with PRIMARY diary sources (supersession project)
- Verified and corrected pdf_sources in name-mapping.csv
- Documented non-survey days with activity descriptions

### Removed

#### Archival Actions
- Moved obsolete files to archive:
  - **CLAUDE_CODE_INSTRUCTIONS.md** → `archive/supersession-project/`
  - **CLAUDE_CODE_PROMPT.md** → `archive/supersession-project/`
  - Reason: Early PDF extraction approach superseded by diary-based method

### Data Quality Metrics (v1.0.0)

| Metric | Coverage | Count |
|--------|----------|-------|
| **Total records** | 100% | 268 |
| **Walker data** | 100% | 268/268 |
| **Leader data** | 100% | 268/268 |
| **Survey units** | 93.3% | 250/268 |
| **Date coverage** | 100% | 268/268 |
| **Team assignment** | 100% | 268/268 |
| **Source documentation** | 100% | 268/268 |
| **Role data (PDA, etc.)** | <50% | Limited by sources |

### Known Limitations (Documented)

1. **Role data incomplete** - PDA operator, paper recorder <50% coverage (source limitation)
2. **Survey units missing** - 18 records (6.7%) have no unit numbers (not in sources)
3. **Pre-FAIR project** - TRAP 2009-2011 predates FAIR principles; retrospective curation applied
4. **No persistent DOI** - Zenodo registration deferred to future release
5. **Publications not linked** - BibTeX available but not integrated into metadata

### Outstanding Tasks (Documented in follow-up-actions.md)

#### High Priority
- Cascade Excel date corrections to other data copies (2010, 2011 source files)
- Participant list updates (Silvia Ivanova, Lizzy, Jiří Musil)

#### Medium Priority
- Investigate 12 failed diary extractions for alternative extraction methods

#### Low Priority
- Name format standardisation (full names vs initials)
- Role field enhancement (if additional sources discovered)

### Git Repository Status

- **Commits:** 69+ commits documenting extraction progress
- **Backups:** 17 timestamped attribution.csv backups in archive
- **Conversations:** 15+ CC interaction transcripts archived
- **Branch:** master (main development branch)

### Provenance

**Extraction Period:** 20-23 November 2025 (4-day intensive collaborative effort)

**Collaborators:**
- **Shawn Ross** (Macquarie University) - Project lead, manual verification
- **Claude Code** (Anthropic AI assistant) - Script development, extraction automation

**Source Material:**
- 15+ field diaries (Bulgarian and English, 2009-2011)
- 39 survey unit PDFs (daily field records)
- Excel survey summaries (Kaz09, Kaz10, Kaz11)
- 104-person participant list (TRAP-Participants.csv)

**Methodology:**
- Diary-based extraction with Bulgarian transliteration
- PDF cross-verification for ambiguous cases
- PRIMARY source preference (diary > PDF > Excel)
- Git version control with comprehensive commit messages
- Automated name standardisation with manual review

---

## [Post-v1.0.0 Updates] - 2025-11-24

### Survey Unit Number Extraction Completion

**Survey Unit Coverage:** ✅ 89.18% Complete (239/268 records)

Following the v1.0.0 release (100% walker data), this update documents the completion of survey unit number extraction, achieving 89.18% coverage with 100% documentation of all remaining gaps.

### Changed

#### Data Quality Improvements
- **outputs/attribution.csv** - Updated to 239 records with survey units (89.18% coverage)
  - Extracted 54 survey unit numbers from Bulgarian diaries and PDF Daily Progress Forms
  - Added explanatory QA_Notes for 28 records without units (alternative survey methods, weather cancellations, non-survey days)
  - Documented 1 record pending investigation (six-digit to five-digit unit renumbering for 2009-03-12 Team C)
  - Coverage improvement: +54 records (+20.2% from initial 69.0% to 89.18%)

#### Documentation Updates
- **outputs/survey-unit-number-extraction-report.md** - Comprehensive report documenting survey unit extraction phase completion
- **outputs/extraction-report.md** - Updated with final ambiguous date investigation results
- **outputs/task-completion-final-summary.md** - Updated with 239/268 coverage statistics
- **outputs/follow-up-actions.md** - Updated header with 89.18% completion status
- **planning/akb-submission-todo.md** - Task 1 completion statistics updated
- **README.md** - Updated with dual completion dates and survey unit coverage
- **CHANGELOG.md** - This incremental update

### Added

#### Archive Structure
- **archive/investigation-runsheets/** - New directory for completed investigation runsheets
- **archive/reports/survey-unit-extraction/** - New directory for interim survey unit extraction reports

#### Investigation Documentation (Archived)
- **archive/investigation-runsheets/ambiguous-dates-investigation-runsheet.md** - Final investigation of 3 ambiguous dates with Bulgarian diary translations (completed 24 November 2025)
- **archive/investigation-runsheets/missing-dates-diary-investigation.md** - Initial investigation template
- **archive/reports/survey-unit-extraction/extraction-completion-summary.md** - Point-in-time extraction results
- **archive/reports/survey-unit-extraction/missing-dates-investigation-findings.md** - Detailed diary investigation with excerpts
- **archive/reports/survey-unit-extraction/missing-dates-final-summary.md** - Comprehensive analysis of dates without units

### Survey Unit Extraction Results

**Extraction phase (54 records):**
- Bulgarian field diaries (2009): 29 records extracted
- PDF Daily Progress Forms (2009): 25 records extracted
- Excel SurveySummary files: 0 records (fields empty for missing records)

**Investigation phase (29 records):**
- Alternative survey methods: 5 records (mound documentation, transect surveys, object recording)
- No autumn survey seasons: 11 records (2009-2010 diaries end in March/April)
- Weather cancellations: 3 records (rain days verified in diaries)
- Non-survey activities: 3 records (base cleanup, remote sensing, grading)
- Gap days: 3 records (between survey sessions)
- Team not working: 3 records (no diary entries)
- Pending investigation: 1 record (six-digit to five-digit unit renumbering for Team C 2009-03-12)

### Key Discoveries

#### Alternative Survey Methodologies
Investigation revealed that many "missing" survey units represent **legitimate alternative survey methods** rather than missing data:

- **Team C specialisation:** Intensive site investigations (mound documentation, transect surveys, object recording) rather than systematic unit-based surveys
- **Team C lower coverage explained:** 79.45% coverage due to focus on intensive archaeological recording rather than extensive survey
- **Examples:** 2009-03-11 (burial mound necropolis DS 052 with 3 mounds documented), 2009-03-25 (transect survey for site GCh-060), 2009-03-27 (9 mounds documented for site GCh-061)

#### Six-Digit to Five-Digit Unit Renumbering Issue
- **Discovery:** Old six-digit survey units (300003-300009, skip 300008) found on 2009-03-12 Team C Daily Progress Form
- **Problem:** Team C initially used six-digit numbering (300xxx) later retroactively changed to five-digit (30xxx) format
- **Status:** Pending investigation of GIS databases, unit cards, or project metadata for renumbering mapping
- **Documented in:** outputs/follow-up-actions.md Medium Priority #1

#### Data Entry Error Resolution
- **2009-04-05 Team B:** PDF form had Start/End Unit and Start/End Time fields swapped - units 20808-20812 clearly visible in wrong fields, successfully extracted

### Data Quality Metrics (Post-v1.0.0 Update)

| Metric | Coverage | Count | Change from v1.0.0 |
|--------|----------|-------|--------------------|
| **Total records** | 100% | 268 | No change |
| **Walker data** | 100% | 268/268 | No change |
| **Leader data** | 100% | 268/268 | No change |
| **Survey units** | 89.18% | 239/268 | +54 records extracted |
| **Survey units explained** | 10.82% | 28/268 | +28 explanations added |
| **Survey units pending** | 0.37% | 1/268 | 1 renumbering investigation |
| **Date coverage** | 100% | 268/268 | No change |
| **Team assignment** | 100% | 268/268 | No change |
| **Source documentation** | 100% | 268/268 | Enhanced with extraction provenance |

### Methodology

**Text extraction:**
- antiword for Bulgarian .doc files (Cyrillic script)
- pandoc for English .docx files
- Python regex for 5-digit unit number pattern matching

**Vision-based extraction:**
- Claude vision (multimodal LLM) for reading scanned PDF Daily Progress Forms
- Manual transcription and validation

**NLP analysis:**
- Bulgarian diary translation and interpretation (~100+ pages examined)
- Cross-referencing across 11 diary files (2009-2011)
- Narrative analysis for alternative survey methods

### Outstanding Tasks

From outputs/follow-up-actions.md:

#### High Priority
- Cascade Excel date corrections to other data copies
- Participant list updates (Silvia Ivanova, Lizzy, Jiří Musil)

#### Medium Priority
- Six-digit to five-digit unit renumbering investigation (2009-03-12 Team C Kazanluk)
- Review 12 failed diary extractions for alternative methods

#### Low Priority
- Create comprehensive archive README files (added 24 November 2025)
- Name format standardisation (full names vs initials)
- Role field enhancement (if additional sources discovered)

### Provenance

**Survey Unit Extraction Period:** 23-24 November 2025 (2-day focused effort following walker data completion)

**Sources examined:**
- 2010-2011 Excel SurveySummary files (Kaz10, Kaz11)
- 5 Bulgarian field diaries (Team A, B, C, D, E 2009)
- 8+ PDF Daily Progress Form compilations (Teams A, B, C, D, E 2009)
- 11 team diaries for investigation (English and Bulgarian, 2009-2011)

**Tools used:**
- antiword, pandoc (text extraction)
- Claude vision (PDF form reading)
- Claude NLP (Bulgarian diary analysis)
- pandas, Python (data processing and validation)

---

## [Post-v1.0.0 Updates] - 2025-11-25

### Name Standardisation and Repository Cleanup

**Name Standardisation:** ✅ Complete (698 name mappings applied)

Following the survey unit extraction completion, this update documents comprehensive name standardisation across all personnel columns and repository housekeeping.

### Added

#### Name Standardisation Scripts
- **scripts/standardise-walkers.py** - Walker name standardisation (268 records)
- **scripts/standardise-leaders-roles.py** - Leader and role column standardisation (593 values)

#### Standardisation Reports
- **outputs/walker-standardisation-report.md** - Walker standardisation outcomes
- **outputs/leader-role-standardisation-report.md** - Leader/role standardisation report

### Changed

#### Data Quality Improvements
- **outputs/attribution.csv** - Comprehensive name standardisation applied:
  - Walkers_Standardised column created with canonical "First Last" names
  - Leader column: 253 values standardised
  - Role columns: 593 values standardised across 6 columns (PDA_Operator, Paper_Recorder, Data_Editor, GPS_Operator, Photographer, Author)
  - Metadata entries cleared from role columns (Images, Track Log, Diary)
  - Placeholders cleared (No, Note, Hm, Vitaha)
  - Only 2 unmapped names remain (Lizzy - uncertain identity)

- **outputs/name-mapping.csv** - Expanded to 698 entries (from 283)
  - 22 new entries for leader/role standardisation
  - Invalid entries mapped for clearing

#### Repository Reorganisation
- **archive/planning/** - Completed planning documents archived:
  - name-standardisation-plan.md
  - role-extraction-checklist.md
  - leader-verification-plan.md
- **archive/intermediate-data/role-extractions/** - 8 role extraction CSVs archived
- **archive/intermediate-data/diary-extracts/** - 6 diary extract text files archived

#### Documentation Updates
- **planning/akb-submission-todo.md** - Updated: Tasks 1-4, 7-8 marked complete
- **planning/follow-up-actions.md** - Updated with completed tasks and outstanding items
- **README.md** - Fixed broken links, updated Future Work section, corrected statistics
- **PROJECT-COMPLETION.md** - Updated Outstanding Tasks with completed items

### Fixed

#### Path Corrections
- Fixed `outputs/follow-up-actions.md` → `planning/follow-up-actions.md`
- Fixed `claude_extraction/akb-submission-todo.md` → `planning/akb-submission-todo.md`

#### Statistics Corrections
- Survey unit coverage: Corrected from 93.3% to 89.18% (239/268)
- Script count: Corrected from 45 to 51

### Data Quality Metrics (25 November 2025)

| Metric | Coverage | Count | Change |
|--------|----------|-------|--------|
| **Walker standardisation** | 100% | 268/268 | NEW |
| **Leader standardisation** | 99.6% | 267/268 | 253 values updated |
| **Role columns standardised** | Variable | 593 values | All 6 columns |
| **Name mappings** | - | 698 entries | +415 entries |
| **Intermediate files archived** | - | 14 files | Outputs cleaned |
| **Planning docs archived** | - | 3 files | Completed plans |

### Provenance

**Standardisation Period:** 25 November 2025

**Work completed:**
- Walker name standardisation
- Leader name standardisation
- Role column standardisation (6 columns)
- Repository cleanup and documentation updates

---

## [0.8.0] - 2025-11-22 (Phase 4 Completion)

### Added
- Supersession project completion: 14 records updated with PRIMARY diary sources
- Team A and Team B diary extraction scripts
- Comprehensive supersession reports and analysis

### Changed
- Updated 14 XLS-only records with walker data from diary sources
- Verified and corrected source references across attribution.csv

---

## [0.6.0] - 2025-11-22 (Phase 3 Completion)

### Added
- Name mapping file with 283 entries (canonical names, variants, OCR errors)
- Name disambiguation reports (Petra, Adela, Helena/Elena, Julia)
- Name mapping QA validation report

### Changed
- Applied systematic name corrections across attribution dataset
- Standardised leader entries (139 records updated)

---

## [0.5.0] - 2025-11-21 (Phase 2 Completion)

### Added
- Diary extraction planning framework
- Source inventory with tier classification (Tier 1-4)
- Diary search results catalogue

### Changed
- Classified all sources by reliability (PRIMARY/SECONDARY/SUPPLEMENTAL)
- Documented diary availability and extraction priorities

---

## [0.3.0] - 2025-11-21 (Phase 1 Completion)

### Added
- Initial attribution.csv with 269 records (76.1% walker coverage)
- Manual extraction guide documenting methodology
- Phase 1 extraction reports and validation

### Changed
- Baseline extraction from Excel, PDF, and initial diary sources

---

## [0.1.0] - 2025-11-20 (Project Initiation)

### Added
- Project structure and documentation framework
- Initial data assessment and extraction planning
- Git repository initialisation

---

## Version Numbering

**Version Format:** MAJOR.MINOR.PATCH

- **MAJOR:** Significant data model changes or complete project milestones
- **MINOR:** New features, substantial data additions, or phase completions
- **PATCH:** Bug fixes, minor corrections, or documentation updates

**v1.0.0 Release Criteria:**
- ✅ 100% walker data coverage (268/268 records)
- ✅ All known date errors corrected
- ✅ FAIR/FAIR4RS documentation complete
- ✅ Comprehensive data dictionary and standards compliance
- ✅ Dual licensing applied (Apache 2.0 + CC-BY 4.0)
- ✅ Git repository with full provenance history

---

## Future Releases

### [1.1.0] - Planned

**Focus:** Zenodo archival publication

- [ ] Register repository with Zenodo
- [ ] Obtain persistent DOI for software and data
- [ ] Update all metadata files with DOI
- [ ] Create versioned release with citation metadata

### [1.2.0] - Planned

**Focus:** Publication integration

- [ ] Add publication DOIs to CITATION.cff
- [ ] Create BibTeX file with structured citations
- [ ] Link attribution data to published analyses
- [ ] Document record-to-publication mappings

### [2.0.0] - Future

**Focus:** Spatial integration and Open Context publication

- [ ] Calculate bounding box for survey area
- [ ] Add GeoJSON spatial metadata
- [ ] Link attribution.csv to GIS survey unit polygons
- [ ] Prepare for Open Context publication pathway

---

**Changelog Maintenance:** This file is updated with each significant change to the project. For detailed commit-level changes, see Git history.

**License:** This changelog is licensed under CC-BY 4.0 International.

**Maintainer:** Shawn Ross (Macquarie University)
