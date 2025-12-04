# Comprehensive Superseded Sources Review

**Date:** 23 November 2025
**Purpose:** Identify all cases where SECONDARY sources were extracted when PRIMARY sources exist

---

## Summary

After comprehensive review of the source inventory and attribution CSV, I identified **2 supersession cases** where data extraction used SECONDARY or lower-tier sources when PRIMARY sources exist:

1. **Yambol 2010 Team B** - Diary superseded by corrected version
2. **Yambol 2010 Team A** - PDFs superseded by diary

---

## Case 1: Yambol 2010 Team B - Corrected Diary Supersedes Original

### Issue

Data was extracted from SECONDARY sources when a PRIMARY source with post-season corrections exists.

### Sources Involved

- **PRIMARY (should use):** `Team B Diary new.docx` (26 KB, March 2011)
  - Location: `Elhovo 2010-12-12/2010/Project Records/Team B/`
  - Contains post-season data quality corrections
  - Covers dates: 2010-11-02, 03, 04, 05, 06, 12, 14, 15
  - Status in inventory: Not extracted [ ]

- **SECONDARY (currently used):** Multiple sources
  - `Team B Diary.docx` (25 KB, December 2010) - Original field version
  - `Day_02.pdf`, `Day_04.pdf`, `Day_08.pdf`, `Day_10.pdf`, `Day_12.pdf` - Scanned daily forms
  - Status in inventory: Extracted [x]

### Impact

**8 records need updating** with data from PRIMARY source:
- 2010-11-02, 03, 04, 05, 12, 14, 15 Team B

**1 record is missing** from attribution CSV:
- 2010-11-06 Team B

### Key Improvements from PRIMARY Source

1. **More complete role data:** GPS and Paper Recorder roles specified
2. **Correct leader names:** PDFs show "Shawn Ross Ross" (OCR error), diary shows "Dr. Ross"
3. **Consistent walker names:** Diary uses standard initials throughout
4. **Post-season corrections:** March 2011 version includes data quality fixes
5. **Author attribution:** Diary explicitly states who wrote each entry

### Detailed Comparison

See: `team-b-supersession-report.md` (already created)

### Status

- [x] PRIMARY source data extracted
- [x] Comparison report created
- [x] Attribution CSV updated ✅ **DONE**
- [x] Extraction notes added ✅ **DONE**

---

## Case 2: Yambol 2010 Team A - Diary Supersedes PDFs

### Issue

Data was extracted from Tier 3 PDFs (scanned daily forms) when a Tier 2 PRIMARY diary exists.

### Sources Involved

- **PRIMARY (should use):** `A_Diary.docx` (EN)
  - Location: `Elhovo 2010-12-12/2010/Project Records/Team A/`
  - Tier 2 source (diaries) - more reliable than PDFs
  - Status in inventory: Not extracted [ ]
  - Coverage: Unknown (needs extraction to determine)

- **SECONDARY (currently used):** PDF files
  - `Day_03.pdf`, `Day_05.pdf` - Scanned daily progress forms
  - Tier 3 source - prone to OCR errors, less complete
  - Used for dates: 2010-10-22, 23, 24, 2010-11-02, 03

### Impact

**5+ records need updating** (full diary coverage unknown):
- 2010-10-22, 23, 24 Team A
- 2010-11-02, 03 Team A
- Possibly additional dates covered by diary

### Priority Rules (from source inventory)

Per Tier Structure (lines 26-32 of source-inventory.md):
- **Tier 1:** Excel SurveySummary - Authoritative for dates, teams, leaders, units
- **Tier 2:** Diaries - **PRIMARY source for walker names and roles**
- **Tier 3:** Scanned PDFs - **SECONDARY verification source, OCR-prone**

Data conflicts: **Tier 2 (diaries) > Tier 3 (scanned PDFs)** for walker accuracy

### Status

- [x] PRIMARY source data extracted ✅ **DONE**
- [x] Comparison with existing PDF data ✅ **DONE**
- [x] Attribution CSV updated ✅ **DONE**
- [x] Coverage determination ✅ **DONE** (5 records: 2010-10-22, 23, 24, 11-02, 03)

---

## Other Sources Reviewed: No Supersession Issues

### Language Variants (BG vs EN): Not Supersession

The following cases involve PRIMARY vs SECONDARY designations for language variants, where both were extracted for completeness or reference:

#### Kazanlak 2009
- **Team A:** BG PRIMARY (198 KB, [x]) and EN SECONDARY (88 KB, [x]) - both extracted
- **Team B:** BG PRIMARY (152 KB, [x]) and EN SECONDARY (62 KB, [x]) - both extracted
- **Team C:** BG PRIMARY (215 KB, [x]) - extracted; EN SECONDARY not extracted
- **Team D:** BG PRIMARY (222 KB, [x]) - extracted; EN SECONDARY not extracted
- **Team E:** BG PRIMARY only (no EN exists, [x]) - extracted

**Status:** PRIMARY sources correctly used for all teams. SECONDARY EN versions extracted for Teams A & B likely for reference/comparison, not supersession.

#### Kazanlak 2010
- **Team A:** BG PRIMARY (86 KB, [x]) - extracted; EN SECONDARY also extracted for roles [x] [x]
- **Team B:** EN PRIMARY (108 KB, [x] [x]) - correctly extracted (unusual case where EN > BG)
- **Team C:** BG PRIMARY (214 KB, [x]) - extracted; EN SECONDARY not extracted
- **Team D:** BG PRIMARY (127 KB, [x]) - extracted; EN SECONDARY not extracted

**Status:** PRIMARY sources correctly prioritised.

**Note on Team A:** Manual-extraction-guide.md (lines 165-181) documents that Team A's BG diary (PRIMARY) ends at 28 March 2010, but the EN diary (SECONDARY) contains entries for 7 April and 8 April 2010. The guide recommends using the EN diary for those specific dates and promoting it to co-PRIMARY status with a coverage note.

#### Kazanlak 2011
- **Team A:** BG PRIMARY only (no EN, [x]) - extracted
- **Team B:** EN PRIMARY (63 KB, [x]) and BG SECONDARY (42 KB, [x]) - both extracted
- **Team C:** EN PRIMARY (70 KB, [x]) and BG SECONDARY (18 KB, [x]) - both extracted
- **Team D:** BG PRIMARY only (no EN, [x]) - extracted

**Status:** PRIMARY sources correctly prioritised.

### PDF Finalized vs Scans: Correctly Used

From source inventory lines 189-193:
- **Kazanlak 2009 Team B:** Finalized (PRIMARY) vs Scans (SECONDARY)
- **Kazanlak 2009 Team D:** Finalized (PRIMARY) vs Scans (SECONDARY)

Verified from `extract_authors_pdf_kaz2009.py:7`:
```python
- TeamB/Finalized/B_2009Summary.pdf
```

**Status:** PRIMARY (Finalized) versions correctly used.

### Elhovo 2009: PRIMARY Diaries Used

- **Team A:** `Diary Team A.doc` (PRIMARY) - used for October 2009 records (lines 65-76 of CSV)
- **Team B:** `DiaryTeamB.doc` (PRIMARY) - extracted
- **Team C:** `The Diary of Team C.doc` (PRIMARY) - used for October 2009 records

**Note:** Source inventory shows [ ] (not extracted) but CSV confirms these PRIMARY sources were actually used. Inventory extraction markers may be inaccurate for Elhovo 2009.

---

## Recommended Action Plan

### Phase 1: Team B Correction (HIGH PRIORITY) ✅ **COMPLETED**

1. **Update attribution CSV** with data from `team-b-diary-new-extraction.csv` ✅
   - [x] Update 8 existing records (2010-11-02, 03, 04, 05, 12, 14, 15)
   - [x] Add 1 missing record (2010-11-06)
   - [x] Change PDF_Source column to reference "Team B Diary new.docx"
   - [x] Add extraction notes: "Updated from PRIMARY source (March 2011 corrected version)"

2. **Update source inventory** (Deferred to Phase 3)
   - [ ] Change Team B Diary new.docx markers from [ ] [ ] to [x] [x]
   - [ ] Add note documenting supersession and update date

### Phase 2: Team A Extraction (MEDIUM PRIORITY) ✅ **COMPLETED**

1. **Extract walker data** from `A_Diary.docx` ✅
   - [x] Determine date coverage (5 records found)
   - [x] Extract walker names and roles for all dates
   - [x] Compare with existing PDF data

2. **Update attribution CSV** with diary data ✅
   - [x] Replace PDF sources with diary source for covered dates
   - [x] Add extraction notes

3. **Update source inventory** (Deferred to Phase 3)
   - [ ] Change A_Diary.docx markers from [ ] [ ] to [x] [x]
   - [ ] Document extraction and supersession

### Phase 3: Source Inventory Audit (LOW PRIORITY) - NOT STARTED

1. **Verify extraction markers** [x] for Elhovo 2009 Teams A, C
   - [ ] CSV shows these were extracted, but inventory shows [ ]
   - [ ] Update inventory markers to match actual usage

2. **Document Kazanlak 2010 Team A** EN diary co-PRIMARY status
   - [ ] Add note explaining coverage differences (BG: March, EN: April)
   - [ ] Recommend EN diary extraction for 7-8 April 2010

---

## Conclusion

**Total supersession cases requiring action: 2**

1. **Team B (HIGH):** 9 records affected, corrected source exists, extraction complete
2. **Team A (MEDIUM):** 5+ records affected, PRIMARY diary not yet extracted

**No other supersession issues identified.** Other PRIMARY/SECONDARY distinctions involve:
- Language variants (both intentionally extracted for completeness)
- PDF quality tiers (PRIMARY Finalized versions correctly used)
- Complementary sources (different date coverage, both needed)

---

## Corrective Actions Completed

**Completion date:** 23 November 2025

### Phase 1: Team B Corrections ✅

**Execution summary:**
- Created extraction script: `scripts/extract_team_b_diary_new.py`
- Extracted PRIMARY source data: `outputs/team-b-diary-new-extraction.csv`
- Created detailed comparison: `outputs/team-b-supersession-report.md`
- Updated `outputs/attribution.csv` (backup created: `attribution.csv.backup_phase1_*`)

**Records updated:** 9 total
- 8 records updated from SECONDARY to PRIMARY source
- 1 missing record added (2010-11-06)
- 1 record retained PDF source (2010-11-11 - no diary entry exists)

**Verification results:**
```
✅ ALL 9 TEAM B RECORDS VERIFIED SUCCESSFULLY
   - 8 records updated to PRIMARY source (Team B Diary new.docx)
   - 1 new record added (2010-11-06)
   - 1 record retained PDF source (2010-11-11)
```

**Key improvements:**
1. Leader names corrected ("Dr. Ross" instead of OCR errors like "Shawn Ross Ross")
2. GPS operator roles added (were missing from PDFs)
3. Paper recorder roles added (were missing from PDFs)
4. Consistent walker name formatting (standard initials)
5. Post-season data quality corrections applied (March 2011 version)

**Files created:**
- `scripts/extract_team_b_diary_new.py` (extraction script)
- `outputs/team-b-diary-new-extraction.csv` (extracted data)
- `outputs/team-b-supersession-report.md` (detailed comparison)
- `outputs/attribution.csv.backup_phase1_20251123_123200` (backup)

**Data location:** `outputs/attribution.csv:193-203`

---

### Phase 2: Team A Corrections ✅

**Execution summary:**
- Read PRIMARY source: `A_Diary.docx` (26 KB, March 2011)
- Created extraction script: `scripts/extract_team_a_diary.py`
- Extracted PRIMARY source data: `outputs/team-a-diary-extraction.csv`
- Created detailed comparison: `outputs/team-a-supersession-report.md`
- Updated `outputs/attribution.csv` (backup created: `attribution.csv.backup_phase2_*`)

**Records updated:** 5 total
- 2010-10-22, 23, 24 (Team A diary entries by Adela D.)
- 2010-11-02, 03 (Team A diary entries by Petra)

**Verification results:**
```
✅ ALL 5 TEAM A RECORDS VERIFIED SUCCESSFULLY
   - All records updated to PRIMARY source (A_Diary.docx)
   - PDA and GPS operator roles added
   - Walker lists corrected and standardised
   - Authors corrected
```

**Key improvements:**
1. Role data added - PDA and GPS operators now recorded (were blank in PDFs)
2. Walker lists corrected - Fixed OCR errors and incorrect names from PDFs
   - 2010-10-22: Removed duplicates (AD, Adela Dorňáková appeared twice)
   - 2010-11-02: Fixed incorrect names (Elena, Bistra → Bara, Emma)
3. Consistent formatting - All walker names now use standard initials
4. Authors corrected - Diary authors instead of photographers
5. PRIMARY source referenced - All now use A_Diary.docx (March 2011)

**Files created:**
- `scripts/extract_team_a_diary.py` (extraction script)
- `outputs/team-a-diary-extraction.csv` (extracted data)
- `outputs/team-a-supersession-report.md` (detailed comparison)
- `outputs/attribution.csv.backup_phase2_*` (backup)

**Data location:** `outputs/attribution.csv:190-192,194-195`

---

### Overall Impact Summary

**Total records corrected:** 14
- Team B: 8 updated + 1 added = 9 records
- Team A: 5 updated

**Data quality improvements:**
1. **Role completeness:** Added missing PDA/GPS operator data for 14 records
2. **Name accuracy:** Corrected walker names, removed OCR errors and duplicates
3. **Source reliability:** Upgraded from Tier 3 (PDFs) to Tier 2 (diaries) for Team A
4. **Source currency:** Applied post-season corrections (March 2011) for both teams
5. **Author attribution:** Diary authors now correctly recorded

**Backups created:**
- `attribution.csv.backup_phase1_20251123_123200` (before Team B updates)
- `attribution.csv.backup_phase2_*` (before Team A updates)

**Supersession resolution status:**
- ✅ Case 1 (Team B): **RESOLVED** - All 9 records using PRIMARY source
- ✅ Case 2 (Team A): **RESOLVED** - All 5 records using PRIMARY source
- ⏸️ Phase 3 (Inventory audit): **DEFERRED** - Low priority administrative updates

**All identified supersession issues have been successfully resolved.**

---

**Document created:** 23 November 2025
**Document updated:** 23 November 2025 (completion report added)
**Review status:** ✅ **COMPLETED** - Phases 1 and 2 executed and verified
**Remaining work:** Phase 3 (source inventory markers) - low priority administrative updates
