# TRAP Data Extraction - Follow-up Actions

**Created:** November 2025

This file tracks outstanding actions that fall outside the core data extraction work.

---

## High Priority

### 1. Cascade Excel Date Correction to Other Data Copies

**Status:** Pending user action

**Context:** On 23 November 2025, a date error was discovered in the Kazanlak 2010 Survey Summary:
- **Incorrect**: Row 45 had date 2010-03-08
- **Correct**: Should be 2010-04-08
- Survey units 30742-30773 were associated with the wrong date

**Correction applied:**
- Created corrected file: `Kaz10_SurveySummary-NEW-2025-correction.xlsx`
- Updated `attribution.csv`:
  - Deleted 2010-03-08 Team C entry
  - Added survey units 30742-30773 to 2010-04-08 Team C entry
  - Verified 2010-03-18 Team C entry is correct
- Total records: 269 → 268

**Action required:**
- [ ] Identify all copies of TRAP 2010 data (outside regular backup pipeline)
- [ ] Apply the date correction (03-08 → 04-08) to each copy
- [ ] Document locations of corrected copies
- [ ] Verify data consistency across all copies

**Files to update in other locations:**
- `Kaz10_SurveySummary.xls` (original Excel file)
- Any derived CSV or database files containing this data
- Any analysis outputs that reference the incorrect date

---

### 2. Correct Kazanluk 2011 Date Error in Source Data

**Status:** ✅ CORRECTED IN ATTRIBUTION.CSV - Source data requires update

**Context:** On 23 November 2025, a critical date error was discovered in the Kazanluk 2011 Survey Summary during Phase 4 extraction planning:
- **Incorrect**: Row with date 2011-11-10 Team D, units 41088-41152
- **Correct**: Should be 2011-10-21 Team D, units 41088-41152
- Source file: `Kaz11_SurveySummary.xlsx`

**Evidence:**
- Team D diary (`D_2011Diary_BG.doc`) covers only 14 Oct - 2 Nov 2011 (no November entries)
- Day 8 entry (21.10.2011) explicitly states: "Направени са 4 трансекти (полигони с номера 41088 до 41152)" [4 transects were made (polygons numbered 41088 to 41152)]
- Unit sequence confirms: 41008-41087 (Oct 20) → 41088-41152 (Oct 21) → 41153-41197 (Oct 22)
- Team B was actually working on 10 November (already correctly recorded in attribution.csv)

**Correction applied to attribution.csv (Option A):**
- [x] Deleted erroneous record: 2011-11-10 Team D
- [x] Updated 2011-10-21 Team D with complete data:
  - Units: 41088-41152
  - Leader: NK (Nadya Kecheva)
  - Walkers: Н. Кечева | В. Генчева | Е. Дакашев | Е. Тонкова | А. Антонов (5 walkers)
  - Added missing walker: А. Антонов (A. Antonov)
  - Source: D_2011Diary_BG.doc
- [x] Created backup: `attribution.csv.backup_kazanluk2011_dateerror_*`
- [x] Documented investigation: `outputs/kazanluk-2011-date-error-report.md`
- [x] Documented correction: `outputs/kazanluk-2011-date-correction-applied.md`
- Total records: 269 → 268 (1 erroneous record deleted)

**Action required:**
- [ ] Contact data custodian to correct source file `Kaz11_SurveySummary.xlsx`
- [ ] Change date from 2011-11-10 to 2011-10-21 for Team D units 41088-41152
- [ ] Verify no other date errors exist in Kaz11_SurveySummary.xlsx
- [ ] Document correction in source file metadata

**Root cause:** Date entry error in source Excel file where 2011-10-21 was incorrectly entered as 2011-11-10 (possible manual transcription error or Excel date conversion issue)

**Files modified:**
- `outputs/attribution.csv` - Date corrected
- `scripts/correct_kazanluk_2011_date_error.py` - Correction script

---

### 3. Participant List Updates

**Status:** Deferred - batch update required

**Context:** Three participants need to be verified and potentially added to `inputs/TRAP-Participants.csv`:

1. **Silvia Ivanova (Силвия Иванова)**
   - Appears in Team E 2009 Bulgarian diary
   - Not in the 104-person participant list
   - Location: `name-mapping.csv` lines 234 and 269
   - Season: 2009 spring

2. **Lizzy**
   - Czech volunteer, 2009-autumn
   - Full name being researched
   - Currently in attribution.csv as "Lizzy" (uncertain identity)
   - Once identified, add to participant list

3. **Jiří Musil**
   - Appears in attribution.csv (2010-04-07, line 181)
   - Note in name-mapping: "Add: Spring 2010 Kazanlak"
   - Not confirmed if missing from participant list
   - Season: 2010 spring

**Action required:**
- [ ] Research and verify full identity of Lizzy
- [ ] Verify Silvia Ivanova's participation in TRAP 2009
- [ ] Check if Jiří Musil is in participant list, verify participation dates
- [ ] Add all three to `inputs/TRAP-Participants.csv` in single batch update with complete details

---

### 2. Resolve Excel Date Error (2010-03-08 → 2010-04-08)

**Status:** ✅ COMPLETED (23 November 2025)

**Context:** Excel SurveySummary contained an incorrect date that cascaded into attribution.csv:
- Row 45 showed 2010-03-08 but should have been 2010-04-08
- Row 30 with 2010-03-18 was correct and matched diary/PDF sources
- The 08 March date was before the survey season started (diary begins 17 March)

**Completed actions:**
- [x] User created corrected Excel file: `Kaz10_SurveySummary-NEW-2025-correction.xlsx`
- [x] Verified diary sources:
  - 18 March entry exists in `C_2010Diary_BG.doc` with walkers
  - 08 March entry does NOT exist (season started 17 March)
  - 08 April diary entry missing but PDF exists (`C_20100408.pdf`)
- [x] Applied corrections to `attribution.csv`:
  - Deleted incorrect 2010-03-08 Team C entry
  - Transferred survey units (30742-30773) to correct 2010-04-08 entry
  - Verified 2010-03-18 entry already correct with walker data
- [x] Created backup: `attribution.csv.backup_date_correction`
- [x] Updated documentation with cascade task (see High Priority #1)

**Results:**
- Total records: 269 → 268 (1 duplicate removed)
- 2010-04-08 Team C now has complete data (units + walkers from PDF)
- 2010-03-18 Team C confirmed correct with walker data from diary

---

### 3. Disambiguate Adela (Sobotkova vs Dorňáková)

**Status:** ✅ COMPLETED (22 November 2025)

**Context:** Two different people named Adela participated in TRAP:
- **Adela Sobotkova** - Project leader, attended multiple seasons (2009-2011)
- **Adéla Dorňáková** - Field walker, attended 2010-autumn only

**Completed actions:**
- [x] Searched attribution.csv for all "Adela" entries in 2010-autumn
- [x] Cross-referenced with team compositions and dates
- [x] Verified Dorňáková is correctly identified in her season (Oct 22-24 as "AD" team leader)
- [x] Updated ambiguous "Adela" entries with full names (Nov 2-3 confirmed as Sobotkova via Day_05.pdf review)

**Results:**
- 5 records identified in 2010-autumn:
  - Oct 22: Both Adelas explicitly named in same record
  - Oct 23-24: Both identified with initials (AD = Dorňáková, AS = Sobotkova)
  - Nov 2-3: Generic "Adela" updated to "Adela Sobotkova" after PDF verification
- All Adela entries in 2010-autumn now correctly disambiguated

---

## Medium Priority

### 3. Review Remaining Name Mappings

**Status:** ✅ COMPLETED (22 November 2025)

**Context:** The name mapping file contains 283 entries. All entries have been reviewed and processed.

**Completed actions:**
- [x] Reviewed all 66 `review_needed` entries in `outputs/name-mapping.csv`
- [x] Applied 58 valid corrections to `attribution.csv` (canonical names)
- [x] Marked 6 entries as `invalid` (OCR false positives: H., Hun, M, P, Olga, X [leader])
- [x] Marked 2 entries as `uncertain` (Lizzy/Lisi - Czech volunteer, identity being researched)
- [x] Updated status for all entries to `corrected`, `invalid`, or `uncertain`

**Results:**
- 111 name replacements made across 73 attribution records
- 126 invalid OCR entries cleared from data
- Detailed report: `outputs/name-corrections-report.md`
- Scripts: `scripts/apply_name_corrections.py`

**Current status distribution:**
- `confident`: 84 entries
- `mapped`: 126 entries
- `corrected`: 58 entries
- `confirmed`: 6 entries
- `uncertain`: 2 entries (Lizzy/Lisi - real person, full name being researched)
- `invalid`: 6 entries (OCR false positives)
- `disambiguated`: 1 entry (Petra)

---

### 4. Investigate XLS-only Records

**Status:** ✅ PARTIALLY COMPLETED (22 November 2025)

**Context:** Research identified 22 XLS-only records (8.2% of 269 total) that had diary sources but weren't previously extracted. Comprehensive source investigation and extraction were performed.

**Completed actions:**
- [x] Investigated all 22 XLS-only records for diary sources
- [x] Updated source-inventory.md with corrections and Tier 4 (39 survey unit PDFs)
- [x] Developed extraction script for multiple diary formats (EN/BG, narrative/structured)
- [x] Executed extraction: 10/22 records successfully extracted (49 walker names added)
- [x] Generated detailed extraction report: diary-extraction-report.md

**Results:**
- 10 records now have complete walker data (Kazanlak 2010-2011, Elhovo 2009)
- 12 records failed extraction due to diary format limitations (no daily walker lists)
- Backup created: attribution.csv.backup_diary_extraction

**Remaining work:**
- [ ] Investigate 12 failed extractions - diaries may have overall walker lists rather than daily breakdowns
- [ ] Manual extraction may be needed for records with non-standard diary formats
- [ ] Remaining 54 records (76 - 22) still need source investigation

**Note:** Date discrepancy flagged for 2010-03-08 (diary shows 18.03.2010) - requires user review

---

## Low Priority

### 5. Standardise Name Formats

**Status:** Deferred

**Context:** The attribution data contains a mix of:
- Full names (e.g., "Adela Sobotkova")
- First names only (e.g., "Adela")
- Initials (e.g., "A.S.")
- Diminutives (e.g., "Bara" for "Barbora")

**Action required:**
- [ ] Decide on preferred standardisation approach
- [ ] Apply name mapping to create standardised walker column
- [ ] Consider separate columns for original vs. standardised names

---

### 6. Role Field Enhancement

**Status:** Deferred

**Context:** PDA_Operator, Paper_Recorder, and Data_Editor fields have <5% coverage due to limited source documentation.

**Action required:**
- [ ] Determine if this data exists in other sources
- [ ] If not recoverable, document as known limitation

---

## Completed Actions

- [x] Extract Kazanlak 2009 team compositions from diaries
- [x] Resolve Helena/Elena ambiguity
- [x] Resolve Julia older/younger distinction
- [x] Create comprehensive name mapping file (283 entries)
- [x] Archive point-in-time reports
- [x] Review and process all 66 `review_needed` entries (22 November 2025)
- [x] Apply 58 valid name corrections to attribution.csv
- [x] Mark 6 invalid OCR entries
- [x] Disambiguate Petra (Janouchová vs Tušlová)
- [x] Verify and correct all pdf_sources in name-mapping.csv
- [x] Fix Lizzy/Lisi typo and clarify identity
- [x] Disambiguate Adela (Sobotkova vs Dorňáková) in 2010-autumn records
- [x] Update source-inventory.md with Tier 4 and source preferences (PRIMARY/SECONDARY/SUPPLEMENTAL)
- [x] Develop diary walker extraction script with Bulgarian transliteration
- [x] Extract walker data from 22 XLS-only records (10/22 successful, 49 names added)
- [x] Resolve Excel date error: Correct 2010-03-08 → 2010-04-08 in attribution.csv (23 November 2025)
- [x] Resolve Kazanluk 2011 date error: Correct 2011-11-10 → 2011-10-21 Team D in attribution.csv (23 November 2025)

---

## Notes

This file should be updated as actions are completed or new items are identified.

**Outstanding research:**
- Batch participant list update: Lizzy (full name research), Silvia Ivanova (verify participation), Jiří Musil (verify participation and dates)

**Last updated:** 23 November 2025 (after Kazanluk 2011 date error correction)
