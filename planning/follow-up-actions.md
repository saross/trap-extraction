# TRAP Data Extraction - Follow-up Actions

**Created:** November 2025
**Last Updated:** 25 November 2025
**Walker Data Extraction Status:** ✅ **100% COMPLETE** (268/268 records)
**Survey Unit Extraction Status:** ✅ **89.18% COMPLETE** (239/268 with units, 28/268 explained, 1/268 pending renumbering)
**Project Completion:** 23 November 2025 (walker data), 24 November 2025 (survey unit number extraction)

This file tracks outstanding actions that fall outside the core walker data extraction work, which has been completed.

**Note:** All walker extraction tasks have been completed. This document now tracks remaining enhancement and data quality tasks for AKB submission preparation.

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

4. **Sharon** (Шарон)
   - Unidentified participant appearing once in 2011-11-02 Team D
   - Clearly written as Шарон in Bulgarian diary (`D_2011Diary_BG.doc`)
   - **Not** Shawn Ross (confirmed by Shawn - he was leading Team C that day)
   - Appears only once across all TRAP diaries
   - Possibly a missing participant or day visitor
   - Research needed: Check photographs, project communications, or other records from November 2011

5. **Yavor L** (YL)
   - Unidentified participant appearing once in 2010-11-06 Team B (Elhovo)
   - Clearly written as "Yavor L" on scanned daily progress form (`Day_06.pdf`)
   - **Not** Yavor Rusev (who would be "YR" and was primarily at Kazanlak)
   - Appears only once across all TRAP diaries
   - Research needed: Check photographs, project communications, or other records from November 2010

6. **Asen** (Асен)
   - Unidentified participant appearing in 2010-03-27 and 2010-03-28 Team C (Kazanlak)
   - BG diary (`C_2010Diary_BG.doc`) team roster lists "Асен ....." with surname missing
   - BG diary entries: "Екип: Елена, Бара, Соня, Яна, Асен" (Mar 27, 28)
   - CSV incorrectly has "Todor" instead of "Asen" for these dates
   - Missing surname indicates visitor not known to team
   - Research needed: Check photographs, project communications from March 2010 Kazanlak

7. **Rebecca**
   - Unidentified participant appearing in 2010-04-13 Team C (Kazanlak)
   - DPF Summary (`C_2010Summary.pdf`) Day 19 shows "Rebecca" as one of 5 walkers
   - Walker list: Adela, Bara, Sonja, Lindsay, Rebecca
   - **Not found** in TRAP-Participants.csv (104 participants checked)
   - BG diary ended Apr 11, so no diary confirmation available
   - Units: 30801-30809 (Day 19, final survey day of season)
   - Research needed: Check photographs, project communications from April 2010 Kazanlak
   - Possible candidate: Day visitor or late-season addition not recorded in master list

**Action required:**
- [ ] Research and verify full identity of Lizzy
- [x] ~~Verify Silvia Ivanova's participation in TRAP 2009~~ - Added to TRAP-Participants.csv (25 Nov 2025)
- [ ] Check if Jiří Musil is in participant list, verify participation dates
- [ ] Investigate Sharon identity (2011-11-02 Team D)
- [ ] Investigate Rebecca identity (2010-04-13 Team C Kazanluk)
- [ ] Investigate Yavor L identity (2010-11-06 Team B Elhovo)
- [ ] Add remaining participants to `inputs/TRAP-Participants.csv` in single batch update with complete details

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

### 4. Walker Discrepancy 2010-04-09 Team B

**Status:** Pending investigation

**Context:** Identified during leader and role standardisation (25 November 2025). The walker list in `attribution.csv` does not match diary/form sources.

**Discrepancy:**
- **CSV shows:** Adela | Petra Tušlová | Peter
- **Diary/form shows:** Adela, Dasha, Pesho, Stana

**Source:** Discovered when investigating Data_Editor "Hm" entry (OCR artefact - cleared).

**Action required:**
- [ ] Verify correct walker list from original sources (diary, daily progress form)
- [ ] Correct `attribution.csv` Walkers_Original and Walkers_Standardised columns for 2010-04-09 Team B
- [ ] Investigate source of discrepancy (possible extraction error or source confusion)

---

## Medium Priority

### 1. Map Six-Digit to Five-Digit Survey Unit Numbers (Kazanlak 2009 Team C - Multiple Dates)

**Status:** Pending investigation

**Context:** During QA of Kazanlak 2009 Team C records (24 November 2025, expanded 2 December 2025), old six-digit survey unit numbers were discovered that were later retroactively renumbered to five-digit format. No simple mapping exists between the old and new numbering systems.

**Study area:** Kazanluk
**Season:** 2009 spring (March)
**Team:** Team C

**Problem:**
Team C initially used a **six-digit "mountain survey" numbering system (300xxx)** for extended transect/polygon survey work in mountainous terrain. This was separate from the **five-digit intensive survey units (30xxx)** used for standard field walking. At some point, the six-digit numbers were supposed to be retroactively converted to five-digit format to match the project-wide convention (Team A: 10xxx, Team B: 20xxx, Team C: 30xxx, Team D: 40xxx, Team E: 50xxx), but the mapping is not documented.

**CRITICAL:** Do NOT guess at five-digit equivalents. Preserve the original six-digit numbers until the official mapping is found.

---

#### Affected Dates and Six-Digit Numbers

| Date | DPF Page | Six-Digit Range | Total | Work Type | Notes |
|------|----------|-----------------|-------|-----------|-------|
| 2009-03-06 | 1 | 300000-300002 | 3 | Mountain polygons | In Comments section; needs separate CSV line |
| 2009-03-12 | 2 | 300003-300009 (skip 300008) | 6 | Mountain polygons | In Comments: "MOUNTAIN POLYS" |
| 2009-03-20 | 3 | 300030-300033 | 4 | Mountain polygons | Mountain survey only (no intensive units this day) |
| 2009-03-23 | 4 | 300012-300020 | 9 | Mountain survey | Separate DPF form; needs separate CSV line |

**Note on Mar 23:** This date has TWO separate DPF forms:
1. **Intensive survey:** 30065-30097 (33 units) - five-digit, normal format ✓
2. **Mountain survey:** 300012-300020 (9 units) - six-digit, requires mapping

These should be recorded as SEPARATE lines in attribution.csv until reconciled.

---

#### Source Documentation

| Date | Source | Evidence |
|------|--------|----------|
| Mar 6 | C_2009Summary.pdf p.1 | Comments: "MOUNTAIN POLYGONS 300,000-002" |
| Mar 12 | C_2009Summary.pdf p.2 | Comments: "MOUNTAIN POLYS - 300,003-7, 300,009" |
| Mar 20 | C_2009Summary.pdf p.3 | Start Unit: 300030, End Unit: 300033 (mountain polygons only) |
| Mar 23 | C_2009Summary.pdf p.4 | Separate form labelled "MOUNTAIN SURVEY" with 300012-300020 |
| All | C_Diary_BG.doc | Bulgarian diary describes mountain polygon methodology |

---

#### Action Required

- [ ] Investigate project records for six-digit to five-digit unit renumbering documentation
- [ ] Potential sources to check:
  - GIS databases (may contain both old and new unit numbers)
  - Project metadata or conversion tables
  - Unit card files (may show both numbering systems)
  - Survey leader notes or correspondence about the renumbering
  - Elena Bozhinova (Team C leader) may have records of the conversion
- [ ] Once mapping is found:
  - [ ] Convert all six-digit numbers to their five-digit equivalents
  - [ ] Update attribution.csv with converted units
  - [ ] Merge mountain survey lines with intensive survey lines where appropriate
- [ ] If mapping cannot be found:
  - [ ] Document as known limitation
  - [ ] Keep six-digit numbers in a separate "Legacy_Units" column
  - [ ] Exclude from unit coverage statistics

---

#### Current Workaround

1. **For attribution.csv:**
   - Preserve original six-digit numbers in records
   - Do NOT convert to five-digit guesses
   - For dates with both intensive and mountain survey (e.g., Mar 23), maintain separate lines

2. **For QA runsheets:**
   - Flag six-digit numbers as "Pending renumbering investigation"
   - Do not mark as errors - these are valid historical data

3. **For coverage statistics:**
   - Records with six-digit numbers count as "explained" but not "with units" until mapping is resolved

**Impact:**
- Multiple Team C records affected (at least 4 dates)
- Coverage statistics may be affected once fully mapped
- This is a systematic issue, not individual record errors

---

### 2. Unit Number Overlaps and Discontinuities

**Status:** Documented for reference (2 December 2025)

**Context:** Analysis of attribution.csv revealed 9 unit number overlaps and 22 gaps. Some are expected (inter-season gaps, legitimate resurveys), while others may warrant investigation.

---

#### Confirmed Unit Number Errors

##### ⚠️ ELH10A-OV1: Elhovo A Unit 61549 (CONFIRMED ERROR)

**Status:** CONFIRMED duplicate unit number (2 December 2025)

| Field | Value |
|-------|-------|
| Season | Elhovo 2010 |
| Team | A |
| Overlap unit | **61549** |
| Date 1 | 2010-10-24 (end unit) |
| Date 2 | 2010-11-02 (start unit) |

**Investigation findings:**
- DPF Day_03.pdf shows Oct 24 ending at 61549
- DPF Day_05.pdf shows Nov 2 starting at 61549
- Diary Nov 2 says "First unit: 61553" but lists 61549 in unit samples
- **Individual SU forms verified:** Unit 61549 appears on forms for BOTH Oct 24 AND Nov 2

**Conclusion:** This is a genuine field recording error where the same unit number was used twice. The unit was likely surveyed once but recorded on two different DPFs.

**Impact:** Unit 61549 attribution is ambiguous (could be Oct 24 or Nov 2 team composition).

**Action required:**
- [ ] Decide which date to assign unit 61549 to (recommend Oct 24 as it appears at end of continuous sequence)
- [ ] Update attribution.csv: change Nov 2 Start Unit from 61549 to 61550
- [ ] Document decision in QA_Notes field

---

##### ✓ ELH09C-OV1: Elhovo C Unit 80939 (RESOLVED - CSV ERROR)

**Status:** RESOLVED - CSV corrected (2 December 2025)

| Field | Value |
|-------|-------|
| Season | Elhovo 2009 |
| Team | C |
| Apparent overlap unit | 80939 |
| Date 1 | 2009-11-12 (end unit in CSV was 80939) |
| Date 2 | 2009-11-13 (start unit) |

**Investigation findings:**
- Diary said Nov 12 ended at 80938, but CSV had 80939
- QA D022 had flagged discrepancy but accepted CSV value
- **Individual SU forms verified (definitive):**
  - Unit 80938 = Nov 12 (last unit of the day)
  - Unit 80939 = Nov 13 (first unit of the day)

**Root cause:** CSV/Excel transcription error (80938 entered as 80939)

**Corrections applied:**
- Nov 12 End Unit: 80939 → **80938**
- Nov 14 End Unit: 81002 → **81008** (also discovered during SU form review)

**Anomaly noted:** Unit 80916 is dated Nov 11 on SU form but falls within Nov 12 sequence (80910-80938). Likely a form dating error - unit filed with Nov 12 batch.

**Result:** Overlap resolved - sequence is now continuous.

---

##### ✓ KAZ10D-OV1: Kazanlak D Units 40424-40432 (RESOLVED - DPF ERROR)

**Status:** RESOLVED - CSV corrected (2 December 2025)

| Field | Value |
|-------|-------|
| Season | Kazanlak 2010 |
| Team | D |
| Apparent overlap | 40424-40432 (9 units) |
| Date 1 | 2010-03-20 (DPF showed end unit 40432) |
| Date 2 | 2010-03-21 (start unit 40424) |

**Investigation findings:**
- DPF (D_2010Summary.pdf) showed Mar 20 ending at 40432
- CSV matched DPF, so QA runsheet marked as "not an error - both sources agree"
- **Individual SU forms verified (definitive):**
  - Mar 20 last unit = **40423**
  - Mar 21 first unit = **40424**

**Root cause:** DPF form error - Mar 20 end unit was written as 40432 instead of 40423 (+9 error)

**Correction applied:**
- Mar 20 End Unit: 40432 → **40423**

**Result:** Overlap resolved - sequence is now continuous (40423 → 40424).

---

##### ✓ KAZ09A-OV1: Kazanlak A Units 10386-10387 (RESOLVED - QA ERROR)

**Status:** RESOLVED - CSV corrected (2 December 2025)

| Field | Value |
|-------|-------|
| Season | Kazanlak 2009 |
| Team | A |
| Apparent overlap | 10386-10387 (2 units) |
| Date 1 | 2009-03-19 (CSV had end unit 10387) |
| Date 2 | 2009-03-20 (start unit 10386) |

**Investigation findings:**
- DPF (A_2009Summary.pdf) clearly showed Mar 19: 10370-10385, Mar 20: 10386-10444
- Diary had Mar 19 ending at 10387
- QA runsheet (D006) noted the discrepancy but chose diary value over DPF
- **DPF confirmed as correct** - continuous sequence with no overlap

**Root cause:** QA process incorrectly followed diary over DPF for unit numbers. Guidelines should specify that DPF supersedes diary for unit range data.

**Correction applied:**
- Mar 19 End Unit: 10387 → **10385**

**Result:** Overlap resolved - sequence is now continuous (10385 → 10386).

---

##### ✓ KAZ09B-OV1: Kazanlak B Unit 20808 (RESOLVED - DATE + UNIT ERROR)

**Status:** RESOLVED - CSV corrected (2 December 2025)

| Field | Value |
|-------|-------|
| Season | Kazanlak 2009 |
| Team | B |
| Apparent overlap | 20808 (1 unit) |
| Date 1 | 2009-03-27 (CSV had this date) |
| Date 2 | 2009-04-05 (start unit was 20808) |

**Investigation findings:**
- User examined DPF and SU forms (B_20090403.pdf) with Gemini vision model
- DPF date written as "04 03 09" (American format) = April 3rd
- QA runsheet incorrectly read p.15 date as "27-Mar" when it was actually "3-Apr"
- SU form analysis revealed unit 20784 was pre-filled on Mar 26 form but survey ended at 20783
- Apr 3 correctly started at 20784 and ended at 20808
- Apr 4 was Object/Feature recording only (no 20000-series units; some 50000-series work)
- Apr 5 started at 20809 (not 20808)

**Root cause:** Two errors compounded:
1. QA misread DPF date "04 03 09" as "27.3.09" (April 3 vs March 27)
2. CSV had Apr 5 Start Unit as 20808 instead of 20809

**Corrections applied:**
- Date: 2009-03-27 → **2009-04-03**
- Apr 5 Start Unit: 20808 → **20809**

**Result:** Overlap resolved - sequence is now continuous:
- Mar 26: 20733-20783
- Apr 3: 20784-20808
- Apr 5: 20809-20812

---

#### Unit Number Overlaps (9 total - 1 confirmed error, 4 resolved, 4 under investigation)

These overlaps may indicate resurveys, site-focused work, or data errors:

| Team | Date 1 | End Unit | Date 2 | Start Unit | Overlap | Size | Notes |
|------|--------|----------|--------|------------|---------|------|-------|
| Elhovo A | 2010-10-24 | 61549 | 2010-11-02 | 61549 | 61549 | 1 unit | **CONFIRMED ERROR** - see above |
| Elhovo C | 2009-11-12 | 80939 | 2009-11-13 | 80939 | 80939 | 1 unit | **RESOLVED** - CSV error, see ELH09C-OV1 |
| Kazanlak A | 2009-03-19 | 10385 | 2009-03-20 | 10386 | — | — | **RESOLVED** - QA error, see KAZ09A-OV1 |
| Kazanlak B | 2009-04-03 | 20808 | 2009-04-05 | 20809 | — | — | **RESOLVED** - date + unit error, see KAZ09B-OV1 |
| Kazanlak C | 2009-03-04 | 30024 | 2009-03-26 | 30021 | 30021-30024 | 4 units | |
| Kazanlak C | 2009-03-26 | 30029 | 2009-03-06 | 30025 | 30025-30029 | 5 units | Date ordering issue? |
| Kazanlak C | 2011-11-17 | 31335 | 2011-11-18 | 31335 | 31335 | 1 unit | Possible resurvey |
| Kazanlak D | 2009-03-25 | 40214 | 2009-03-26 | 40212 | 40212-40214 | 3 units | Site-focused work (noted in QA runsheet) |
| Kazanlak D | 2010-03-20 | 40432 | 2010-03-21 | 40424 | 40424-40432 | 9 units | **RESOLVED** - DPF error, see KAZ10D-OV1 |

---

#### Intra-Season Gaps (May Warrant Investigation)

| Team | Date 1 | End | Date 2 | Start | Gap | Size | Notes |
|------|--------|-----|--------|-------|-----|------|-------|
| Elhovo C | 2009-10-29 | 80794 | 2009-11-09 | 80796 | 80795 | 1 unit | |
| Kazanlak A | 2010-03-26 | 11035 | 2010-03-28 | 11037 | 11036 | 1 unit | |
| Kazanlak A | 2010-04-07 | 11089 | 2010-04-08 | 11091 | 11090 | 1 unit | |
| Kazanlak B | 2010-03-26 | 21407 | 2010-03-28 | 21410 | 21408-21409 | 2 units | |
| Kazanlak B | 2011-11-10 | 22198 | 2011-11-12 | 22206 | 22199-22205 | 7 units | |
| Kazanlak B | 2011-11-15 | 22282 | 2011-11-17 | 22321 | 22283-22320 | 38 units | Large gap |
| Kazanlak B | 2011-11-22 | 22542 | 2011-11-29 | 22600 | 22543-22599 | 57 units | Large gap |
| Kazanlak C | 2010-04-07 | 30740 | 2010-04-08 | 30742 | 30741 | 1 unit | |
| Kazanlak C | 2011-11-18 | 31342 | 2011-11-20 | 31344 | 31343 | 1 unit | |
| Kazanlak D | 2009-03-04 | 40023 | 2009-03-07 | 40031 | 40024-40030 | 7 units | Documented in QA runsheet |
| Kazanlak D | 2009-03-07 | 40032 | 2009-03-15 | 40039 | 40033-40038 | 6 units | Documented in QA runsheet |
| Kazanlak D | 2009-03-15 | 40065 | 2009-03-19 | 40069 | 40066-40068 | 3 units | Documented in QA runsheet |
| Kazanlak D | 2009-03-23 | 40104 | 2009-03-24 | 40112 | 40105-40111 | 7 units | Documented in QA runsheet |
| Kazanlak D | 2009-03-26 | 40214 | 2009-03-27 | 40218 | 40215-40217 | 3 units | |

---

#### Inter-Season Gaps (Expected)

These gaps occur between survey seasons and are normal:

| Team | Gap Range | Size | Between |
|------|-----------|------|---------|
| Elhovo A | 61345-61399 | 55 units | 2009 → 2010 |
| Elhovo B | 71464-71469 | 6 units | 2009 → 2010 |
| Kazanlak A | 10743-10749 | 7 units | 2009 → 2010 |
| Kazanlak A | 11204-11205 | 2 units | 2010 → 2011 |
| Kazanlak B | 20813-20849 | 37 units | 2009 → 2010 |
| Kazanlak C | 30171-30199 | 29 units | 2009 → 2010 |
| Kazanlak C | 30810-30820 | 11 units | 2010 → 2011 |

---

#### Action Required

- [ ] Investigate Kazanlak D 2010-03-20/21 overlap (9 units) - largest overlap in dataset
- [ ] Review Kazanlak C overlaps (dates appear out of order in some cases)
- [ ] Investigate large Kazanlak B gaps in November 2011 (38 and 57 units)
- [ ] Document any overlaps confirmed as legitimate resurveys

**Note:** Kazanlak D 2009 gaps are documented in the QA runsheet as reflecting actual non-contiguous survey areas per the DPF records.

---

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

### 3. Investigate XLS-only Records

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

### 7. Create Archive README Files

**Status:** Pending

**Context:** Following the 24 November 2025 housekeeping update, new archive directories were created with structured organisation:
- `archive/investigation-runsheets/` - Completed investigation runsheets
- `archive/reports/survey-unit-extraction/` - Interim survey unit extraction reports

**Action required:**
- [ ] Create `archive/investigation-runsheets/README.md`:
  - Explain purpose of runsheets (procedural documents for systematic investigation)
  - List archived runsheets with completion dates
  - Note that findings are incorporated into main extraction-report.md
- [ ] Create `archive/reports/survey-unit-extraction/README.md`:
  - Catalogue archived survey unit extraction reports
  - Document timeline of reports (extraction → investigation → final)
  - Explain report supersession
  - Guide readers to which report to consult for what information

**Note:** This task was deferred during the 24 November 2025 housekeeping to focus on core updates and archiving. Archive structure is in place; READMEs can be added incrementally.

---

## QA Process Lessons Learned

### Issue: DPF vs Diary Source Priority Not Consistently Applied

**Discovered:** 2 December 2025 during overlap investigation

**Case study: KAZ09A-OV1 (Kazanlak A, 2009-03-19)**

The QA runsheet documented a source divergence:
- DPF: End Unit = 10385
- Diary: End Unit = 10387
- CSV followed diary value (10387)

The runsheet noted this as "minor DPF/diary unit divergence" with status CONFIRMED, but did **not** flag it as a correction.

**What went wrong:**

1. The guidelines (qa-guidance.md) clearly state:
   - Line 27: "DPF scans — PRIMARY source; more accurate for numeric/factual data"
   - Line 38: "DPF scans take precedence for basic info when conflicting with diaries"
   - Line 174 (O1): "Always prefer DPF scan for Start Unit / End Unit values"

2. The Cross-Check rule (lines 56-60) states: "If diary creates a gap/overlap but DPF scan doesn't → confirms DPF scan as PRIMARY"

3. In this case:
   - DPF value (10385) creates continuity: Mar 19 ends at 10385 → Mar 20 starts at 10386 ✓
   - Diary value (10387) creates overlap: Mar 19 ends at 10387 but Mar 20 starts at 10386 ✗

4. The Cross-Check rule should have confirmed DPF as correct, but instead the diary value was kept.

**Root cause:** QA process treated DPF/diary divergences as "minor" informational notes rather than applying the mandatory source priority rule.

**Recommended guideline updates:**

1. **Make source priority mandatory, not advisory:** Change wording from "DPF scans take precedence" to "DPF scans **must** be used for unit numbers when they conflict with diaries"

2. **Flag divergences as issues:** Any DPF/diary divergence for Start/End Units should generate a QA issue requiring resolution, not just a note in the Source Divergences table

3. **Add explicit decision tree:**
   ```
   For Start_Unit / End_Unit conflicts:
   1. Check if DPF value maintains unit continuity with adjacent days
   2. Check if diary value maintains unit continuity
   3. If DPF maintains continuity and diary doesn't → USE DPF (mandatory)
   4. If both maintain continuity → USE DPF (per source priority)
   5. If neither maintains continuity → FLAG for SU form verification
   ```

4. **Require explicit source attribution:** Each corrected value should note which source it came from (e.g., "End Unit: 10385 (from DPF; diary had 10387)")

**Action items:**
- [x] Update qa-guidance.md with clearer mandatory language (2 December 2025)
- [x] Add decision tree for DPF/diary conflicts (2 December 2025)
- [ ] Review other QA runsheets for similar "minor divergence" cases that should have been corrections

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
- Six-digit to five-digit survey unit renumbering mapping (2009-03-12 Team C Kazanluk)

**Data quality observations:**
- **Tereza Blažková — 2009 autumn presence unexplained:** TRAP-Participants.csv marks her as present in 2009 autumn (column 10 = "x"), but she does not appear in any walker records for that season. Tereza Dobrovodská is clearly documented on Team C (Oct 12-22) and Team A (Oct 26-29 as Eric's substitute). T. Blažková may have had a specialist role (ceramics, bioarchaeology, finds processing) rather than field walking that season. No action required unless participant list accuracy review is undertaken. (Discovered during D016 QA, 26 Nov 2025)

**Last updated:** 2 December 2025 (added unit number overlaps and discontinuities documentation)

---

**GitHub Repository:** https://github.com/saross/trap-extraction
