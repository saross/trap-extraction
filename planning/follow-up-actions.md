# TRAP Data Extraction - Follow-up Actions

**Created:** November 2025
**Last Updated:** 3 December 2025
**Walker Data Extraction Status:** ✅ **100% COMPLETE** (268/268 records)
**Survey Unit Extraction Status:** ✅ **89.18% COMPLETE** (239/268 with units, 28/268 explained, 1/268 pending renumbering)
**Project Completion:** 23 November 2025 (walker data), 24 November 2025 (survey unit number extraction)

This file tracks outstanding actions that fall outside the core walker data extraction work, which has been completed.

**Note:** All walker extraction tasks have been completed. This document now tracks remaining enhancement and data quality tasks for AKB submission preparation.

---

# CRUCIAL ACTIONS

These items require resolution before data submission.

---

## 1. Unknown Walkers / Names Missing from TRAP-Participants

**Status:** Research required

**Context:** Several participants appear in field records but are not in the 104-person TRAP-Participants.csv master list. Original TRAP-Participants.csv is a historical artefact and should NOT be modified; a new participant list will be generated after all corrections are complete.

### Unidentified Participants

| Name | Season | Team | Date(s) | Source | Notes |
|------|--------|------|---------|--------|-------|
| **Lizzy** | 2009 Autumn | B | Nov 9-13 | Diary | Czech volunteer; full name unknown |
| **Sharon** (Шарон) | 2011 Autumn | D | Nov 2 | BG Diary | NOT Shawn Ross (confirmed); single appearance |
| **Yavor L** (YL) | 2010 Autumn | B | Nov 6 | DPF | NOT Yavor Rusev (would be "YR"); single appearance |
| **Asen** (Асен) | 2010 Spring | C | Mar 27-28 | BG Diary | Surname missing ("Асен ....."); visitor |
| **Rebecca** | 2010 Spring | C | Apr 13 | DPF | Final survey day; not in participant list |
| **Silvia Ivanova** | 2009 Spring | E | Multiple | BG Diary | Not in 104-person list |
| **Jiří Musil** | 2010 Spring | C | Apr 7+ | DPF | May be missing from participant list |

### Action Required

- [ ] Research and verify full identity of Lizzy (Czech volunteer, 2009 autumn)
- [ ] Investigate Sharon identity (2011-11-02 Team D) - check photographs, project communications
- [ ] Investigate Yavor L identity (2010-11-06 Team B Elhovo) - check photographs, project communications
- [ ] Research Asen surname (Mar 2010 Kazanlak visitor)
- [ ] Investigate Rebecca identity (2010-04-13 Team C Kazanlak)
- [ ] Verify Silvia Ivanova's participation in TRAP 2009
- [ ] Check if Jiří Musil is in participant list, verify participation dates
- [ ] Generate new participant list after all corrections complete

---

## 2. Unit Number Discontinuities

**Status:** Partially resolved (3 December 2025)

**Context:** Analysis of attribution.csv revealed unit number overlaps (duplicates) and gaps. Overlaps are problematic as they create ambiguous unit attribution. Gaps are less critical once documented.

---

### ⚠️ OVERLAPS / DUPLICATES (Require Action)

#### ELH10A-OV1: Elhovo A Unit 61549 (CONFIRMED DUPLICATE)

**Status:** ⚠️ REQUIRES DECISION

| Field | Value |
|-------|-------|
| Season | Elhovo 2010 |
| Team | A |
| Duplicate unit | **61549** |
| Date 1 | 2010-10-24 (end unit) |
| Date 2 | 2010-11-02 (start unit) |

**Investigation findings:**
- DPF Day_03.pdf shows Oct 24 ending at 61549
- DPF Day_05.pdf shows Nov 2 starting at 61549
- **Individual SU forms verified:** Unit 61549 appears on forms for BOTH dates

**Conclusion:** Genuine field recording error - same unit number used twice.

**Action required:**
- [ ] Decide which date to assign unit 61549 to (recommend Oct 24 as it appears at end of continuous sequence)
- [ ] Update attribution.csv: change Nov 2 Start Unit from 61549 to 61550
- [ ] Document decision in QA_Notes field

---

#### Documented Duplicates (For Reference)

| ID | Team | Season | Unit(s) | Notes |
|----|------|--------|---------|-------|
| F006 | Kazanlak D | 2009 Spring | 40100 | Two distinct SU forms on Mar 23 ("Near village" vs "Pine trees") |
| F009 | Kazanlak A | 2010 Spring | 11142 | Two forms on Apr 8 (Page 13 top, Page 14 bottom) |

These are documented field anomalies - no CSV correction needed, but noted for data quality.

---

### ✓ RESOLVED OVERLAPS

| ID | Team | Season | Issue | Resolution |
|----|------|--------|-------|------------|
| ELH09C-OV1 | Elhovo C | 2009 | Unit 80939 | CSV error corrected |
| KAZ09A-OV1 | Kazanlak A | 2009 | Units 10386-10387 | QA error corrected |
| KAZ09B-OV1 | Kazanlak B | 2009 | Unit 20808 | Date + unit error corrected |
| KAZ09C-OV1 | Kazanlak C | 2009 | Units 30021-30029 | Was 6-digit mountain survey |
| KAZ10D-OV1 | Kazanlak D | 2010 | Units 40424-40432 | DPF error corrected |
| KAZ11C-OV1 | Kazanlak C | 2011 | Unit 31335 | OCR error corrected |

---

### DOCUMENTED FIELD GAPS (No Action Required)

These gaps have been verified as genuine field numbering gaps - the units were never assigned.

| ID | Team | Season | Missing Units | Count | Verified |
|----|------|--------|---------------|-------|----------|
| F007 | Kazanlak D | 2009 Spring | 40218 | 1 | 3 Dec 2025 |
| F008 | Kazanlak A | 2010 Spring | 11090 | 1 | 3 Dec 2025 |
| F010 | Kazanlak B | 2011 Autumn | 22199-22205 | 7 | 3 Dec 2025 (numbering error) |
| F011 | Kazanlak B | 2011 Autumn | 22543-22599 | 57 | 3 Dec 2025 (week-long break) |

---

### Inter-Season Gaps (Expected - No Action Required)

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

## 3. Records Missing Team Leader

**Status:** To be verified

**Action required:**
- [ ] Query attribution.csv for records where Leader field is empty
- [ ] Cross-reference with diaries/DPFs to identify leaders
- [ ] Update records with verified leader names

---

# OTHER ACTIONS

These items are important but not blocking for data submission.

---

## Source Data Corrections (Cascade Required)

### Cascade Excel Date Correction to Other Data Copies

**Status:** Pending user action

**Context:** On 23 November 2025, a date error was discovered in the Kazanlak 2010 Survey Summary:
- **Incorrect**: Row 45 had date 2010-03-08
- **Correct**: Should be 2010-04-08

**Correction applied to attribution.csv.** Source files need updating:
- [ ] Identify all copies of TRAP 2010 data (outside regular backup pipeline)
- [ ] Apply the date correction (03-08 → 04-08) to each copy
- [ ] `Kaz10_SurveySummary.xls` (original Excel file)

---

### Correct Kazanluk 2011 Date Error in Source Data

**Status:** ✅ CORRECTED IN ATTRIBUTION.CSV - Source data requires update

**Context:** Date error in Kazanluk 2011 Survey Summary:
- **Incorrect**: 2011-11-10 Team D, units 41088-41152
- **Correct**: 2011-10-21 Team D, units 41088-41152

**Action required:**
- [ ] Contact data custodian to correct source file `Kaz11_SurveySummary.xlsx`

---

## Six-Digit Mountain Survey Units (Kazanlak 2009 Team C)

**Status:** Pending investigation

**Context:** Team C used six-digit "mountain survey" numbering (300xxx) for extended transect work. No mapping to five-digit format exists.

**CRITICAL:** Do NOT guess at five-digit equivalents. Preserve original six-digit numbers.

| Date | Six-Digit Range | Total | Work Type |
|------|-----------------|-------|-----------|
| 2009-03-06 | 300000-300002 | 3 | Mountain polygons |
| 2009-03-12 | 300003-300009 (skip 300008) | 6 | Mountain polygons |
| 2009-03-20 | 300030-300033 | 4 | Mountain polygons |
| 2009-03-23 | 300012-300020 | 9 | Mountain survey |
| 2009-03-26 | 300021-300029 | 9 | Tumuli documentation |

**Action required:**
- [ ] Investigate project records for six-digit to five-digit unit renumbering documentation
- [ ] Check GIS databases, project metadata, Elena Bozhinova's records

---

## Walker Discrepancy 2010-04-09 Team B

**Status:** Pending investigation

**Discrepancy:**
- **CSV shows:** Adela | Petra Tušlová | Peter
- **Diary/form shows:** Adela, Dasha, Pesho, Stana

**Action required:**
- [ ] Verify correct walker list from original sources
- [ ] Correct attribution.csv if needed

---

## Low Priority Items

### Standardise Name Formats

**Status:** Deferred

Mixed formats exist (full names, first names, initials, diminutives). Consider standardisation approach.

### Role Field Enhancement

**Status:** Deferred

PDA_Operator, Paper_Recorder, Data_Editor fields have <5% coverage.

### Create Archive README Files

**Status:** Deferred

READMEs needed for `archive/investigation-runsheets/` and `archive/reports/survey-unit-extraction/`.

---

## QA Process Lessons Learned

### Issue: DPF vs Diary Source Priority Not Consistently Applied

**Discovered:** 2 December 2025

**Summary:** QA process sometimes followed diary values over DPF values for unit numbers, creating overlaps. Guidelines updated to make DPF priority mandatory for unit data.

**Action items:**
- [x] Update qa-guidance.md with clearer mandatory language (2 December 2025)
- [x] Add decision tree for DPF/diary conflicts (2 December 2025)
- [ ] Review other QA runsheets for similar "minor divergence" cases

---

## Completed Actions

- [x] Extract Kazanlak 2009 team compositions from diaries
- [x] Resolve Helena/Elena ambiguity
- [x] Resolve Julia older/younger distinction
- [x] Create comprehensive name mapping file (283 entries)
- [x] Review and process all 66 `review_needed` entries (22 November 2025)
- [x] Apply 58 valid name corrections to attribution.csv
- [x] Disambiguate Petra (Janouchová vs Tušlová)
- [x] Disambiguate Adela (Sobotkova vs Dorňáková) in 2010-autumn records
- [x] Resolve Excel date error: 2010-03-08 → 2010-04-08 (23 November 2025)
- [x] Resolve Kazanluk 2011 date error: 2011-11-10 → 2011-10-21 (23 November 2025)
- [x] Resolve all unit number overlaps except ELH10A-OV1 (3 December 2025)
- [x] Document all within-season gaps (3 December 2025)

---

## Notes

**Data quality observations:**
- **Tereza Blažková — 2009 autumn presence unexplained:** TRAP-Participants.csv marks her as present in 2009 autumn, but she does not appear in any walker records. May have had specialist role rather than field walking.

**Last updated:** 3 December 2025

---

**GitHub Repository:** https://github.com/saross/trap-extraction
