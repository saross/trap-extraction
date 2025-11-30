# QA Runsheet: Elhovo 2009 Autumn Team B

**Study Area/Season:** Elhovo 2009 Autumn
**Team:** B
**QA Date:** 2025-11-27
**QA Performed By:** Claude Code (automated test)
**Records:** 20 (in original CSV)
**Date Range:** 2009-10-12 - 2009-11-13

---

## Sources Consulted

| Type | File | Location | Role |
|------|------|----------|------|
| EN Diary | DiaryTeamB.doc | Elhovo 2010-12-12/2009/Project Records/Team B/ | PRIMARY (EN, detailed daily entries) |
| BG Diary | TeamB_Dnevnik Ross.doc | .../Team B/ | SECONDARY (BG) |
| Excel | ELH09 SurveySummary.xls | .../Master Records/ | Unit ranges |

**Note:** No DPF scans exist for ELH 2009 (season-wide gap S004). Diary is primary source for all verification.

---

## Team Composition

### Phase 1: Oct 12-29 (Standard composition)
- **Leader:** Shawn Ross
- **Walkers:** Scott Jackson, Vera Doležálková, Shawn Ross, Yavor Rusev, Stanislav Marchovski
- **Note:** Stefan Bakardzhiev joined from Oct 15, Martin temporarily on Oct 23

### Phase 2: Nov 2-13 (Roster changes)
- **Leader:** Shawn Ross
- **Walkers:** Core team plus various (Dasha, Zhoro, Lizzy, Simon, etc.)
- **Note:** Significant roster variation in November

---

## Record-by-Record Verification

### 2009-10-12 (Mon) — Units 70000-70043 ✓
- **Diary:** Five walkers, units 70000-70043
- **CSV:** Start: 70000, End: 70043
- **Status:** CONFIRMED

### 2009-10-13 (Tue) — Units 70044-70122 ✓
- **Diary:** Five walkers, units 70044-70122
- **CSV:** Start: 70044, End: 70122
- **Status:** CONFIRMED

### 2009-10-15 (Thu) — Units 70123-70163 ✓
- **Diary:** Six walkers (Stefan joined), units 70123-70163
- **CSV:** Start: 70123, End: 70163
- **Status:** CONFIRMED

### 2009-10-20 (Tue) — Units 70164-70240 ✓
- **Diary:** Six walkers, units 70164-70240
- **CSV:** Start: 70164, End: 70240
- **Status:** CONFIRMED

### 2009-10-21 (Wed) — Units 70241-70342 ✓
- **Diary:** Six walkers, units 70241-70342
- **CSV:** Start: 70241, End: 70342
- **Status:** CONFIRMED

### 2009-10-22 (Thu) — Units 70343-70477 ✓
- **Diary:** Six walkers, units 70343-70477
- **CSV:** Start: 70343, End: 70477
- **Status:** CONFIRMED

### 2009-10-23 (Fri) — Units 70478-70571 ✓
- **Diary:** Five walkers (Martin from Team A joined), units 70478-70571
- **CSV:** Start: 70478, End: 70571
- **Status:** CONFIRMED

### 2009-10-26 (Mon) — Units 70572-70655 ✓
- **Diary:** Units 70572-70655
- **CSV:** Start: 70572, End: 70655
- **Status:** CONFIRMED

### 2009-10-27 (Tue) — Units 70656-70747 ✓
- **Diary:** Units 70656-70747
- **CSV:** Start: 70656, End: 70747
- **Status:** CONFIRMED

### 2009-10-28 (Wed) — Units 70748-70839 ✓
- **Diary:** Five walkers, units 70748-70839
- **CSV:** Start: 70748, End: 70839
- **Status:** CONFIRMED

### 2009-10-29 (Thu) — Units 70840-70925 ✓
- **Diary:** Four walkers, units 70840-70925
- **CSV:** Start: 70840, End: 70925
- **Status:** CONFIRMED

### 2009-11-02 (Mon) — Units 70926-70962 ⚠️
- **Diary:** "First unit: 70926, Last unit: 70962, Total units: 36"
- **CSV:** Start: **(empty)**, End: **(empty)**
- **CSV QA_Notes:** Contains erroneous "No autumn 2009 survey season - diaries end in March/April"
- **Issue D001:** Missing unit range — diary clearly shows 70926-70962
- **Issue D002:** Erroneous QA_Notes — factually incorrect statement
- **Status:** DISCREPANCY (MAJOR)

### 2009-11-03 (Tue) — Units 70963-71062 ⚠️
- **Diary:** "First unit: 70963, Last unit: 71062, Total units: 100"
- **CSV:** Start: **(empty)**, End: **(empty)**
- **CSV QA_Notes:** Contains erroneous "No autumn 2009 survey season"
- **Issue D003:** Missing unit range — diary clearly shows 70963-71062
- **Issue D004:** Erroneous QA_Notes — factually incorrect statement
- **Status:** DISCREPANCY (MAJOR)

### 2009-11-05 (Thu) — Units 71063-71142 ⚠️
- **Diary:** "First unit: 71063, Last unit: 71142, Total units: 79"
- **CSV:** Start: **(empty)**, End: **(empty)**
- **CSV QA_Notes:** Contains erroneous "No autumn 2009 survey season"
- **Issue D005:** Missing unit range — diary clearly shows 71063-71142
- **Issue D006:** Erroneous QA_Notes — factually incorrect statement
- **Status:** DISCREPANCY (MAJOR)

### 2009-11-06 (Fri) — Units 71143-71201 ✓
- **Diary:** "First unit: 71143, Last unit: 71201"
- **CSV:** Start: 71143, End: 71201
- **Status:** CONFIRMED

### 2009-11-07 (Sat) — Units 71202-71257 ✓
- **Diary:** Units documented
- **CSV:** Start: 71202, End: 71257
- **Status:** CONFIRMED

### 2009-11-09 (Mon) — Units 71258-71313 ✓
- **Diary:** Four walkers
- **CSV:** Start: 71258, End: 71313, Walkers include "UNMAPPED: Lizzy"
- **Status:** CONFIRMED (name mapping issue is extraction-side, not QA error)

### 2009-11-10 (Tue) — Units 71314-71370 ✓
- **Diary:** Five walkers
- **CSV:** Start: 71314, End: 71370
- **Status:** CONFIRMED

### 2009-11-12 (Thu) — Units 71371-71405 ✓
- **Diary:** Five walkers
- **CSV:** Start: 71371, End: 71405
- **Status:** CONFIRMED

### 2009-11-13 (Fri) — Units 71406-71463 ✓
- **Diary:** Five walkers
- **CSV:** Start: 71406, End: 71463
- **Status:** CONFIRMED

---

## Issues Summary

| ID | Date | Field | Issue | Action |
|----|------|-------|-------|--------|
| D001 | 2009-11-02 | Start/End_Unit | Missing units 70926-70962 | Add unit range |
| D002 | 2009-11-02 | QA_Notes | Erroneous "no autumn diary" | Remove text |
| D003 | 2009-11-03 | Start/End_Unit | Missing units 70963-71062 | Add unit range |
| D004 | 2009-11-03 | QA_Notes | Erroneous "no autumn diary" | Remove text |
| D005 | 2009-11-05 | Start/End_Unit | Missing units 71063-71142 | Add unit range |
| D006 | 2009-11-05 | QA_Notes | Erroneous "no autumn diary" | Remove text |

---

## Corrections Required

### D001/D002: Add Nov 2 Units and Fix QA_Notes (MAJOR)

**Record:** 2009-11-02, Team B
**Fields:** Start_Unit, End_Unit, QA_Notes

**Current:**
- Start_Unit: (empty)
- End_Unit: (empty)
- QA_Notes: "MISSING: Survey units | No role data available | No autumn survey season: No autumn 2009 survey season - diaries end in March/April"

**Corrected:**
- Start_Unit: 70926
- End_Unit: 70962
- QA_Notes: "No role data available" (remove erroneous text)

**Source evidence:** DiaryTeamB.doc Nov 2 entry: "First unit: 70926, Last unit: 70962"

**Reasoning:** Diary clearly documents unit range. The erroneous QA_Note about "no autumn survey season" is factually wrong — the diary covers Oct 10 through Nov 21, 2009 with detailed daily entries.

**User Decision:**
- [ ] Approve
- [ ] Modify: _______________

**Status:** Pending

---

### D003/D004: Add Nov 3 Units and Fix QA_Notes (MAJOR)

**Record:** 2009-11-03, Team B
**Fields:** Start_Unit, End_Unit, QA_Notes

**Current:**
- Start_Unit: (empty)
- End_Unit: (empty)

**Corrected:**
- Start_Unit: 70963
- End_Unit: 71062

**Source evidence:** DiaryTeamB.doc Nov 3 entry: "First unit: 70963, Last unit: 71062"

**Reasoning:** Unit continuity confirms: 70963 follows Nov 2 end (70962) + 1.

**User Decision:**
- [ ] Approve
- [ ] Modify: _______________

**Status:** Pending

---

### D005/D006: Add Nov 5 Units and Fix QA_Notes (MAJOR)

**Record:** 2009-11-05, Team B
**Fields:** Start_Unit, End_Unit, QA_Notes

**Current:**
- Start_Unit: (empty)
- End_Unit: (empty)

**Corrected:**
- Start_Unit: 71063
- End_Unit: 71142

**Source evidence:** DiaryTeamB.doc Nov 5 entry: "First unit: 71063, Last unit: 71142"

**Reasoning:** Unit continuity confirms: 71063 follows Nov 3 end (71062) + 1. Nov 4 was rain day (no survey).

**User Decision:**
- [ ] Approve
- [ ] Modify: _______________

**Status:** Pending

---

## Unit Continuity Check

| Date | End Unit | Next Date | Start Unit | Gap | Status |
|------|----------|-----------|------------|-----|--------|
| Oct 12 | 70043 | Oct 13 | 70044 | +1 | ✓ |
| Oct 13 | 70122 | Oct 15 | 70123 | +1 | ✓ |
| Oct 15 | 70163 | Oct 20 | 70164 | +1 | ✓ |
| Oct 20 | 70240 | Oct 21 | 70241 | +1 | ✓ |
| Oct 21 | 70342 | Oct 22 | 70343 | +1 | ✓ |
| Oct 22 | 70477 | Oct 23 | 70478 | +1 | ✓ |
| Oct 23 | 70571 | Oct 26 | 70572 | +1 | ✓ |
| Oct 26 | 70655 | Oct 27 | 70656 | +1 | ✓ |
| Oct 27 | 70747 | Oct 28 | 70748 | +1 | ✓ |
| Oct 28 | 70839 | Oct 29 | 70840 | +1 | ✓ |
| Oct 29 | 70925 | Nov 2 | 70926 | +1 | ✓ (after correction) |
| Nov 2 | 70962 | Nov 3 | 70963 | +1 | ✓ (after correction) |
| Nov 3 | 71062 | Nov 5 | 71063 | +1 | ✓ (Nov 4 was rain) |
| Nov 5 | 71142 | Nov 6 | 71143 | +1 | ✓ |
| Nov 6 | 71201 | Nov 7 | 71202 | +1 | ✓ |
| Nov 7 | 71257 | Nov 9 | 71258 | +1 | ✓ (Nov 8 no survey) |
| Nov 9 | 71313 | Nov 10 | 71314 | +1 | ✓ |
| Nov 10 | 71370 | Nov 12 | 71371 | +1 | ✓ (Nov 11 no survey?) |
| Nov 12 | 71405 | Nov 13 | 71406 | +1 | ✓ |

**Note:** Perfect unit continuity after corrections applied.

---

## Summary Statistics

| Metric | Count |
|--------|-------|
| Records checked | 20 |
| Records confirmed | 14 |
| Issues found | 6 |
| Corrections required | 9 field updates (6 units + 3 QA_Notes) |
| MAJOR issues | 6 (missing units, erroneous notes) |

### Issues by Category
- Missing units: 3 records (D001, D003, D005)
- Erroneous QA_Notes: 3 records (D002, D004, D006)
- Walker errors: 0
- Role errors: 0

---

## Source Observations

### Source Divergences

No source divergences observed.

**Reason:** Single-source verification only. No DPF scans exist for ELH 2009 (season-wide gap S004). Diary is the sole primary source for all fields.

### Source Reliability Patterns

- **O1 not testable:** Cannot compare DPF vs diary for unit numbers (no DPF available)
- **Diary reliability:** Unit values from diary were consistent with Excel summary (ELH09 SurveySummary.xls)

### Implications for Future QA

- For 2009 seasons without DPF scans, diary is the only verification source
- Excel summary can provide secondary validation of unit ranges
- Unit continuity check (C1) becomes the primary error detection method

---

## Notes

### Observation: Erroneous Extraction Assumption
The original extraction incorrectly assumed no autumn 2009 diary existed ("diaries end in March/April"). This caused unit numbers for Nov 2, 3, 5 to be missed. The DiaryTeamB.doc clearly covers October 10 through November 21, 2009.

### Observation: Unit Continuity as Detection Method
The unit continuity check (Rule C1) would have flagged the missing Nov 2-5 units:
- Oct 29 ends at 70925
- Nov 6 starts at 71143
- Gap of ~218 units would indicate missing data

### Observation: Name Mapping
"UNMAPPED: Lizzy" appears in Nov 9-13 records. This is an extraction-side name standardisation issue (Lizzy → Elizabeth [surname]?) rather than a QA error. The walker was present and recorded correctly.

---

**Document created:** 2025-11-27
**Last updated:** 2025-11-27
