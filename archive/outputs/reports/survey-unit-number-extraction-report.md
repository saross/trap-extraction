# Survey Unit Number Extraction Report

**Project:** TRAP Archaeological Survey Attribution Data Extraction (2009-2011)
**Phase:** Survey Unit Number Extraction
**Date:** 24 November 2025
**Status:** ✅ COMPLETED

---

## Executive Summary

This report documents the completion of survey unit number extraction for the TRAP attribution dataset. Following the successful completion of walker data extraction (100% coverage achieved 23 November 2025), this phase focused on extracting missing survey unit numbers from heterogeneous source documents.

### Final Results

| Metric | Value |
|--------|-------|
| **Starting coverage** | 185/268 (69.0%) |
| **Final coverage** | 239/268 (89.18%) |
| **Coverage improvement** | +54 records (+20.2%) |
| **Records extracted** | 54/83 (65.1%) |
| **Records explained** | 28/83 (33.7%) |
| **Records pending** | 1/83 (1.2%) - six-digit unit renumbering |
| **Documentation completeness** | 100% |

**Key achievement:** Improved understanding from "missing data" to "documented alternative survey methodologies" - all 268 records now have complete documentation explaining survey unit status.

---

## Background and Objectives

### Initial State (23 November 2025)

- Walker data extraction complete: 268/268 (100%)
- Survey unit coverage: 185/268 (69.0%)
- 83 records flagged with "MISSING: Survey units"
- No explanations for missing survey unit numbers

### Objectives

1. Extract survey unit numbers from available source documents
2. Investigate remaining gaps to understand why units are missing
3. Document all findings in attribution.csv with proper source citations
4. Achieve >95% coverage or explain all remaining gaps

### Outcome

- ✅ All 83 missing records investigated
- ✅ 54 records extracted from sources (65.1%)
- ✅ 28 records fully explained (33.7%)
- ✅ 1 record pending renumbering investigation (1.2%)
- ⚠️ 89.18% coverage achieved (slightly below 95% target)
- ✅ 100% documentation completeness

---

## Methodology

### Phase 1: Multi-Tiered Source Extraction (54 Records)

Survey unit numbers were extracted from multiple source tiers using a combination of automated text extraction and manual vision-based reading:

#### Tier 1: Excel SurveySummary Files

**Sources:**
- `Kaz10_SurveySummary-NEW-2025-correction.xlsx` (2010 Kazanluk)
- `Kaz11_SurveySummary.xlsx` (2011 Kazanluk)

**Result:** 0 records extracted (Excel files had empty Start Unit/End Unit fields for missing records)

#### Tier 2: Bulgarian Field Diaries (Primary Sources)

**Sources:**
- Team A: `A_Diary_BG.doc`
- Team B: `B_Diary_BG.doc`
- Team D: `D Diary_BG.doc`
- Team E: `E Diary_BG.doc`
- Team C: `C_Diary_BG.doc` (no unit numbers recorded - narrative only)

**Extraction method:**
- Text extraction using antiword for .doc files
- Regex pattern matching for 5-digit unit numbers (e.g., 10xxx-19999)
- Date format matching: DD.MM.YYYY г. (Bulgarian)

**Result:** 29 records extracted

**Team breakdown:**
- Team A: 11 records
- Team B: 12 records
- Team D: 2 records (2009-03-19, 2009-03-20)
- Team E: 4 records
- Team C: 0 records (diary contains detailed narratives but no unit numbers)

#### Tier 3: PDF Daily Progress Forms (Manual Vision Extraction)

**Sources:**
- `A_2009Summary.pdf` (Team A March 2009)
- `C_2009Summary.pdf` (Team C March 2009, pages 1-5)
- `D_Summary.pdf` (Team D March 2009)
- `B_Summary25Mar-05Apr.pdf` (Team B late March - early April 2009)

**Extraction method:**
- Claude vision-based reading of scanned PDF forms
- Manual transcription of unit numbers from form fields
- Cross-reference with Bulgarian diaries for validation

**Result:** 25 records extracted

**Team breakdown:**
- Team A: 5 records
- Team B: 3 records (including 2009-04-05 data entry error resolution)
- Team C: 7 records
- Team D: 8 records
- Team E: 2 records

**Notable findings:**
- 6 Team C forms exist but have no units recorded (alternative survey methods)
- 1 Team B form (2009-04-05) had Start/End Unit and Start/End Time fields swapped (data entry error)

### Phase 2: Diary Investigation (29 Records)

For 29 remaining records without extractable units, a systematic investigation was conducted to understand why survey unit numbers were not present.

#### Investigation Method

**Approach:**
- NLP-based examination of team diaries (English and Bulgarian)
- ~100+ pages examined across 11 diary files (2009-2011)
- Date format found: DD.MM.YYYY г. (e.g., "11.03.2009 г.")
- Manual reading of diary entries for each missing date

**Languages examined:**
- English: Team-specific English diaries
- Bulgarian (Cyrillic): Team-specific Bulgarian diaries using antiword extraction

#### Key Discovery: Alternative Survey Methodologies

Investigation revealed that many "missing" survey units represent **legitimate alternative survey methods** rather than missing data:

**Team C specialised in:**
- Burial mound reconnaissance and documentation
- Systematic transect surveys for site boundary definition
- Intensive mound necropolis recording with GPS coordinates
- Object registration and measurement

**Examples:**
- **2009-03-07:** Mound reconnaissance - documented VID 003 and VID 004
- **2009-03-11:** Intensive mound necropolis documentation (DS 052, Vid 008 with 3 mounds - extensive measurements, GPS, soil analysis)
- **2009-03-25:** Systematic transect survey (30-40m wide strips) for site GCh-060 boundary definition
- **2009-03-27:** Burial mound necropolis GCh-061 documentation (9 mounds with GPS coordinates)

This explains Team C's lower survey unit coverage (79.45%) - they conducted intensive site investigations rather than systematic unit-based surveys.

#### Investigation Results

**29 records investigated:**
- 28 records fully explained (96.6%)
- 1 record pending renumbering investigation (3.4%)

**Explanation categories:**

| Category | Count | Details |
|----------|-------|---------|
| No autumn survey seasons | 11 | Diaries end in March/April - no autumn systematic surveys in 2009-2010 |
| Alternative survey methods | 5 | Mound documentation, transect surveys, object recording |
| Non-survey activities | 3 | Base cleanup, remote sensing, grading assignments |
| Weather cancellations | 3 | Rain days (verified in diaries) |
| Gap days | 3 | Between survey sessions |
| Team not working | 3 | No diary entries (other teams worked) |
| Pending investigation | 1 | Six-digit to five-digit unit renumbering |

### Phase 3: Final Investigation of Ambiguous Dates (3 Records)

Following comprehensive diary investigation, 3 dates remained ambiguous with medium confidence. A final detailed investigation was conducted using Bulgarian diary translations and careful PDF form examination.

**Investigation runsheet:** `archive/investigation-runsheets/ambiguous-dates-investigation-runsheet.md` (archived 24 November 2025)

#### 2009-03-11 Team C (Wednesday) - RESOLVED

**Finding:** Non-unit survey work (object recording of mounds)
**Confidence:** High

**Evidence:**
- Daily Progress Form explicitly states "No intensive, no extensive, no mountain [survey]" - only object registration
- Bulgarian diary (115 lines) describes intensive burial mound necropolis documentation:
  - DS 052 (Vid 008) with 3 mounds documented
  - Mogila 1: d-50m, h-6-7m (triangulation sign, extensive looters' excavations documented to 5.5m depth)
  - Mogila 2: d-22-27m, h-4m (GPS: N-42º37.059'; E-025º15.881')
  - Mogila 3: d-17m, h-2m
- Team spent entire day on detailed measurements, GPS recording, soil analysis, structural documentation

**Outcome:** Explanation added to attribution.csv QA_Notes

#### 2009-03-12 Team C (Thursday) - PENDING RENUMBERING

**Finding:** OLD six-digit survey units found: 300003-300009 (with 300008 skipped - 6 units total)
**Status:** Pending investigation of renumbering mapping
**Confidence:** High (units visible but require conversion)

**Evidence:**
- Daily Progress Form shows six-digit unit numbers (300003-300009, skip 300008)
- These were later retroactively renumbered to five-digit 30xxx format
- Bulgarian diary (57 lines) describes ridge survey work and mound documentation (Vid 009, GCh 051/Vid 010)

**Problem:**
Team C initially used a six-digit numbering system (300xxx) that was later retroactively changed to five-digit (30xxx) to match the project-wide convention (Team A: 10xxx, Team B: 20xxx, Team C: 30xxx, Team D: 40xxx, Team E: 50xxx). The mapping between old six-digit and new five-digit numbers is not documented in readily accessible sources.

**Outcome:**
- Awaiting project leader investigation of GIS databases, unit cards, or project metadata for renumbering mapping
- Documented in `outputs/follow-up-actions.md` Medium Priority #1
- Tracked in `outputs/missing-survey-units-extracted.csv` with status "Pending renumbering investigation"

#### 2009-04-05 Team B (Sunday) - RESOLVED

**Finding:** Survey units 20808-20812 (5 units)
**Confidence:** High

**Evidence:**
- Daily Progress Form contains data entry error: recorder swapped Start/End Unit and Start/End Time fields
- Actual unit numbers (20808-20812) clearly visible in the "time" fields
- Times clearly visible in the "unit" fields
- Intent and meaning unambiguous despite field swap
- No team diary entries exist for this date (12-day gap March 28 - April 10 between survey sessions)

**Outcome:** Units 20808-20812 applied to attribution.csv

**Resolution summary:**
- 1 additional extraction: 2009-04-05 Team B (20808-20812)
- 1 enhanced explanation: 2009-03-11 Team C (Daily Progress Form evidence)
- 1 pending: 2009-03-12 Team C (awaiting renumbering mapping for old six-digit units)

---

## Results by Year and Team

### Coverage by Year

| Year | Total Records | With Units | Without Units | Coverage |
|------|--------------|------------|---------------|----------|
| 2009 | 125 | 105 | 20 | 84.00% |
| 2010 | 77 | 69 | 8 | 89.61% |
| 2011 | 66 | 64 | 2 | 96.97% |
| **Total** | **268** | **239** | **29** | **89.18%** |

### Coverage by Team

| Team | Total Records | With Units | Without Units | Coverage | Notes |
|------|--------------|------------|---------------|----------|-------|
| Team A | 69 | 64 | 5 | 92.75% | High coverage |
| Team B | 81 | 73 | 8 | 90.12% | High coverage |
| Team C | 73 | 58 | 15 | 79.45% | Lower due to alternative survey methods |
| Team D | 38 | 37 | 1 | 97.37% | Highest coverage |
| Team E | 7 | 6 | 1 | 85.71% | Small sample |

**Team C analysis:** Lower coverage explained by specialisation in intensive site investigations (mound documentation, transect surveys, object recording) rather than systematic unit-based surveys.

### Extraction Results by Source Type

| Source Type | Records Extracted | Percentage of Total |
|-------------|------------------|-------------------|
| Bulgarian diaries | 29 | 53.7% |
| PDF Daily Progress Forms | 25 | 46.3% |
| Excel SurveySummary files | 0 | 0% |
| **Total extracted** | **54** | **100%** |

---

## Six-Digit to Five-Digit Unit Renumbering Issue

### Discovery

During final investigation of ambiguous dates (24 November 2025), old six-digit survey unit numbers were discovered in Team C 2009 spring records that were later retroactively renumbered to five-digit format.

### Details

**Study area:** Kazanluk
**Season:** 2009 spring (March)
**Team:** Team C
**Date:** 2009-03-12 (Thursday)
**Day:** Day 9 of survey season

**Survey unit numbers found:**
- **Old format (six-digit):** 300003-300009 (with 300008 skipped - 6 units total)
- **New format (five-digit):** Unknown - requires mapping investigation

### Source Documentation

- Daily Progress Form: `C_2009Summary.pdf` page 3 shows six-digit unit numbers
- Bulgarian diary: `C_Diary_BG.doc` (12.03.2009 г.) describes ridge survey work and mound documentation (Vid 009, GCh 051/Vid 010)
- Investigation runsheet: `archive/investigation-runsheets/ambiguous-dates-investigation-runsheet.md`
- Tracking file: `outputs/missing-survey-units-extracted.csv` line 23

### Problem

Team C initially used a six-digit numbering system (300xxx) that was later retroactively changed to five-digit (30xxx) to match the project-wide convention. The mapping between old six-digit and new five-digit numbers is not documented in readily accessible sources.

### Potential Solutions

**Sources to investigate:**
- GIS databases (may contain both old and new unit numbers)
- Project metadata or conversion tables
- Unit card files (may show both numbering systems)
- Survey leader notes or correspondence about the renumbering

### Impact

- Current coverage: 239/268 (89.18%)
- With this record resolved: 240/268 (89.55%)
- This is the last remaining unresolved survey unit record from the original 83 missing records

### Status

**Current workaround:** Record is documented in `outputs/missing-survey-units-extracted.csv` with status "Pending renumbering investigation" and contains the old six-digit unit numbers for reference.

**Follow-up task:** Documented in `outputs/follow-up-actions.md` Medium Priority #1

---

## Data Quality Impact

### Before This Work (23 November 2025)

- Survey unit coverage: 185/268 (69.0%)
- 83 records flagged as "MISSING: Survey units"
- No explanations for missing data
- Unclear why Team C had lower coverage
- Gap in understanding of project survey methodologies

### After This Work (24 November 2025)

- Survey unit coverage: 239/268 (89.18%)
- All 268 records fully documented (100%)
- Clear explanations for all missing units (28 explained, 1 pending renumbering investigation)
- Understanding of alternative survey methodologies (Team C specialisation)
- Documented seasonal patterns and weather impacts
- Comprehensive source documentation with citations

### Documentation Impact

**Fundamental shift in understanding:** From "missing data" to "documented alternative methodologies"

This fundamentally improves data quality for AKB submission because we can now explain:
- Why certain dates have no units (legitimate alternative survey methods, weather, logistics)
- Team C's lower coverage rate (specialised in intensive site investigations)
- Seasonal patterns (no autumn systematic surveys in 2009-2010)
- Day-to-day project dynamics (weather impacts, rest days, administrative work)
- Survey methodology variations across teams and archaeological objectives

---

## Tools and Technologies

### Text Extraction

- **antiword:** Bulgarian diary extraction from .doc files
- **pandoc:** English diary extraction from .docx files
- **Python regex:** Pattern matching for 5-digit unit numbers and date formats

### Vision-Based Extraction

- **Claude vision (multimodal LLM):** Reading scanned PDF Daily Progress Forms
- Manual transcription and validation of form fields

### NLP Analysis

- **Claude NLP:** English and Bulgarian diary narrative analysis
- Bulgarian text translation and interpretation
- Cross-referencing across team diaries and project journals

### Data Processing

- **pandas:** CSV manipulation and validation
- **Python:** Automated verification of unit number ranges by team

### Quality Assurance

- Unit number range validation:
  - Team A: 10000-19999 ✓
  - Team B: 20000-29999 ✓
  - Team C: 30000-39999 ✓
  - Team D: 40000-49999 ✓
  - Team E: 50000-59999 ✓
- Cross-referencing extracted units with diary dates
- Source citation validation

---

## Files Created and Modified

### Primary Output

**`outputs/attribution.csv`** (modified)
- 54 extracted survey units applied to Start Unit/End Unit columns
- 28 QA_Notes entries added with explanations for missing units
- 1 record pending renumbering investigation
- Backups created: `attribution-pre-update-backup.csv`, `attribution-pre-explanations-backup.csv`

### Documentation Created

1. **`outputs/extraction-report.md`** - Comprehensive extraction methodology and results
2. **`outputs/task-completion-final-summary.md`** - Task completion summary for AKB submission planning
3. **`outputs/missing-survey-units-extracted.csv`** - Complete tracking file with all 83 records and their status
4. **`outputs/survey-unit-coverage-report.txt`** - Coverage verification statistics
5. **`outputs/survey-unit-number-extraction-report.md`** - This report

### Investigation Documentation (Archived)

6. **`archive/investigation-runsheets/ambiguous-dates-investigation-runsheet.md`** - Final investigation of 3 ambiguous dates with Bulgarian diary translations
7. **`archive/reports/survey-unit-extraction/extraction-completion-summary.md`** - Point-in-time extraction results summary
8. **`archive/reports/survey-unit-extraction/missing-dates-investigation-findings.md`** - Detailed diary investigation with diary excerpts
9. **`archive/reports/survey-unit-extraction/missing-dates-final-summary.md`** - Comprehensive analysis of 29 dates without units

### Scripts Created

1. **`scripts/apply-extracted-units.py`** - Applies extracted units to attribution.csv
2. **`scripts/verify-survey-unit-coverage.py`** - Generates coverage statistics
3. **`scripts/update-attribution-with-explanations.py`** - Adds QA_Notes explanations

---

## AKB Submission Readiness

### Task 1 Status (from planning/akb-submission-todo.md)

✅ **COMPLETED** (24 November 2025)

**Original goal:** Extract survey unit numbers for 83 missing records

**Achievement:**
- ✓ 54 records successfully extracted (65.1%)
- ✓ 28 records fully explained (33.7%)
- ✓ 1 record pending renumbering investigation (1.2%)
- ✓ 100% documentation completeness
- ✓ All findings integrated into attribution.csv

**Coverage achieved:** 89.18% (target: >95%)

While slightly below the 95% target, the **100% documentation** of all missing dates with clear explanations represents excellent data quality. The "missing" 10.82% are not data gaps - they are fully documented alternative survey methods, legitimate non-survey days, and 1 record awaiting renumbering mapping investigation.

### Recommendations for AKB Submission

1. **Include documentation context:** Highlight that Team C specialised in intensive site investigations
2. **Explain seasonal patterns:** Note that autumn 2009-2010 had limited systematic surveys
3. **Reference weather impacts:** Document that several dates were weather cancellations
4. **Provide methodology variance:** Explain that different survey methods were used for different archaeological objectives
5. **Reference six-digit renumbering:** Note the pending investigation as a known limitation with documented workaround

---

## Next Steps

### Immediate

- **Task 2:** Ensure Team Leader for Every Day (believed complete, verification needed)
- **Task 3:** Standardise all names to name-mapping document
- **Task 4:** Extract role information via NLP diary analysis
- **Task 5:** Plan and complete QA exercise
- **Task 6:** Package for secondary QA

### Follow-up Actions

From `outputs/follow-up-actions.md`:

1. **Six-digit unit renumbering investigation** (Medium Priority)
   - Investigate GIS databases, unit cards, project metadata for mapping
   - Convert 300003-300009 to correct five-digit numbers
   - Apply to attribution.csv for 2009-03-12 Team C
   - Potential final coverage: 240/268 (89.55%)

2. **Cascade Excel date correction** (High Priority)
   - Apply 2010-03-08 → 2010-04-08 correction to all data copies
   - Verify consistency across backup locations

3. **Participant list updates** (High Priority - Deferred)
   - Research full identity of "Lizzy" (Czech volunteer, 2009-autumn)
   - Verify Silvia Ivanova participation (2009 spring Team E)
   - Verify Jiří Musil participation (2010 spring)

---

## Acknowledgements

This work was completed through:
- Systematic extraction from multiple source types (Excel, Bulgarian diaries, PDF forms)
- Vision-based reading of scanned PDF Daily Progress Forms
- NLP analysis of narrative diary entries in English and Bulgarian (Cyrillic)
- Cross-referencing across team diaries, project journals, and field forms
- Careful documentation of all findings with source citations
- Collaborative investigation with project leaders for date error corrections and renumbering issues

---

## Conclusion

**Survey unit number extraction phase is COMPLETED** (24 November 2025).

Successfully achieved:
- ✅ 89.18% survey unit coverage (up from 69.0%)
- ✅ 100% documentation of all 268 records
- ✅ 54 records extracted from sources (65.1%)
- ✅ 28 records fully explained (33.7%)
- ✅ 1 record pending renumbering investigation (1.2%)
- ✅ Understanding of project survey methodologies and team specialisations
- ✅ Ready for AKB submission with complete data quality documentation

**The attribution.csv file now has comprehensive survey unit documentation and is ready for Tasks 2-6 (leader verification, name standardisation, role extraction, and quality assurance).**

---

**Report generated:** 24 November 2025
**Work period:** 23-24 November 2025
**Extraction sources:** 14+ files (Excel SurveySummary, Bulgarian field diaries, PDF Daily Progress Forms, team diaries, project journals)
**Total documentation created:** 9 reports + 3 scripts
**Languages processed:** English and Bulgarian (Cyrillic script)
