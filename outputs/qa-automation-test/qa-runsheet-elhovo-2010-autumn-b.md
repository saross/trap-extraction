# QA Runsheet: Elhovo 2010 Autumn Team B

**Study Area/Season:** Elhovo 2010 Autumn
**Team:** B
**QA Date:** 2025-11-27
**QA Performed By:** Claude Code (automated test)
**Records:** 9 (in original CSV)
**Date Range:** 2010-11-02 - 2010-11-15

---

## Sources Consulted

| Type | File | Location | Role |
|------|------|----------|------|
| Diary | Team B Diary new.docx | Elhovo 2010-12-12/2010/Project Records/Team B/ | PRIMARY (EN, 26 KB) |
| DPF scan | Day_02.pdf | .../Team B/Field Records/ | Nov 2-3 |
| DPF scan | Day_04.pdf | .../Team B/Field Records/ | Nov 4-5 |
| DPF scan | Day_06.pdf | .../Team B/Field Records/ | Nov 6-7 |
| DPF scan | Day_08.pdf | .../Team B/Field Records/ | Nov 10-11 |
| DPF scan | Day_12.pdf | .../Team B/Field Records/ | Nov 15-16 |

---

## Team Composition

### Phase 1: Nov 2-6 (Dr Ross leading)
- **Leader:** Shawn Ross (Dr. Ross)
- **Walkers:** Varies by day (5-6 walkers)
- **Note:** Nov 6 was "Royce first time leading team" - training day

### Phase 2: Nov 7-15 (Royce Lawrence leading)
- **Leader:** Royce Lawrence
- **Walkers:** Varies by day (5-6 walkers)

### Phase 3: Nov 15+ (Petra leading)
- **Leader:** Petra Tušlová
- **Walkers:** 5 walkers

---

## Record-by-Record Verification

### 2010-11-02 (Tue) — Units 71470-71524 ✓
- **Diary:** 5 walkers, Leader: Dr. Ross, Start: 71470, End: 61524 (typo for 71524)
- **DPF:** Start: 71470, End: 71524
- **CSV:** Start: 71470, End: 71524
- **Status:** CONFIRMED

### 2010-11-03 (Wed) — Units 71525-71583 ⚠️
- **Diary:** Start: 71525, End: 71567
- **DPF:** Start: **71525**, End: 71583
- **CSV:** Start: **71245**, End: 71583
- **Issue D001:** Start Unit error — CSV has 71245, DPF shows 71525
- **Status:** DISCREPANCY

### 2010-11-04 (Thu) — Units 71584-71649 ⚠️
- **Diary:** Start: 71584, End: 71650
- **DPF:** Start: 71584, End: **71649**
- **CSV:** Start: 71584, End: **71650**
- **Issue D002:** End Unit error — CSV has 71650, DPF shows 71649
- **Status:** DISCREPANCY

### 2010-11-05 (Fri) — Units 71650-71712 ✓
- **Diary:** Start: 71650, End: 71712
- **DPF:** Start: 71650, End: 71712
- **CSV:** Start: 71650, End: 71712
- **Status:** CONFIRMED

### 2010-11-06 (Sat) — Units 71713-71760 ⚠️
- **Diary:** Start: 71713, End: 71760
- **DPF:** Start: **71713**, End: **71760**
- **CSV:** Start: **(empty)**, End: **(empty)**
- **Issue D003:** Missing unit range — CSV has no Start/End Unit values
- **Status:** DISCREPANCY (SOURCE GAP in CSV)

### 2010-11-07 (Sun) — Units 71761-71800 ⚠️
- **Diary:** Start: 71761, End: 71800
- **DPF:** Start: **71761**, End: **71800**
- **CSV:** **RECORD MISSING**
- **Issue D004:** Missing record — Entire day missing from CSV
- **Status:** MISSING RECORD (MAJOR)

### 2010-11-10 (Wed) — Units 71801-71833 ⚠️
- **Diary:** Start: 71801, End: 71833
- **DPF:** Start: **71801**, End: **71833**
- **CSV:** **RECORD MISSING**
- **Issue D005:** Missing record — Entire day missing from CSV
- **Status:** MISSING RECORD (MAJOR)

### 2010-11-11 (Thu) — Units 71834-71909 ✓
- **Diary:** No diary entry for this date
- **DPF:** Start: 71834, End: 71909
- **CSV:** Start: 71834, End: 71909
- **Status:** CONFIRMED (PDF source only)

### 2010-11-12 (Fri) — Units 71910-71980 ✓
- **Diary:** Start: 71910, End: 71980
- **DPF:** Not checked (no Day_10.pdf)
- **CSV:** Start: 71910, End: 71980
- **Status:** CONFIRMED

### 2010-11-14 (Sun) — Units 71981-72024 ✓
- **Diary:** Start: 71981, End: 72024
- **DPF:** Not checked
- **CSV:** Start: 71981, End: 72024
- **Status:** CONFIRMED

### 2010-11-15 (Mon) — Units 72025-72087 ✓
- **Diary:** Start: 72025, End: 72087
- **DPF:** Available (Day_12.pdf)
- **CSV:** Start: 72025, End: 72087
- **Status:** CONFIRMED

---

## Issues Summary

| ID | Date | Field | Issue | Action |
|----|------|-------|-------|--------|
| D001 | 2010-11-03 | Start_Unit | CSV 71245, should be 71525 | Correct Start_Unit |
| D002 | 2010-11-04 | End_Unit | CSV 71650, should be 71649 | Correct End_Unit |
| D003 | 2010-11-06 | Start/End_Unit | CSV empty, should be 71713/71760 | Add unit range |
| D004 | 2010-11-07 | Entire record | Record missing from CSV | Add record |
| D005 | 2010-11-10 | Entire record | Record missing from CSV | Add record |

---

## Corrections Required

### D001: Correct Nov 3 Start_Unit

**Record:** 2010-11-03, Team B
**Field:** Start_Unit
**Current:** 71245
**Corrected:** 71525
**Source evidence:** DPF Day_02.pdf Form 2 clearly shows "Start Unit: 71525"
**Reasoning:** CSV value 71245 is impossible — it's less than Nov 2 end unit (71524). DPF is PRIMARY for unit numbers.

**User Decision:**
- [ ] Approve
- [ ] Modify: _______________

**Status:** Pending

---

### D002: Correct Nov 4 End_Unit

**Record:** 2010-11-04, Team B
**Field:** End_Unit
**Current:** 71650
**Corrected:** 71649
**Source evidence:** DPF Day_04.pdf Form 1 clearly shows "End Unit: 71649"
**Reasoning:** Diary shows 71650, but DPF (PRIMARY) shows 71649. Nov 5 starts at 71650, confirming 71649 is correct end for Nov 4.

**User Decision:**
- [ ] Approve
- [ ] Modify: _______________

**Status:** Pending

---

### D003: Add Nov 6 Unit Range

**Record:** 2010-11-06, Team B
**Field:** Start_Unit, End_Unit
**Current:** (empty), (empty)
**Corrected:** 71713, 71760
**Source evidence:** DPF Day_06.pdf Form 1 shows "Start Unit: 71713, End Unit: 71760"
**Reasoning:** Both diary and DPF agree on these values. CSV has the record but unit range was not extracted.

**User Decision:**
- [ ] Approve
- [ ] Modify: _______________

**Status:** Pending

---

### D004: Add Missing Nov 7 Record (MAJOR)

**Record:** 2010-11-07, Team B
**Field:** Entire record
**Current:** MISSING
**Source evidence:**
- DPF Day_06.pdf Form 2: Date 7/Nov/2010, Units 71761-71800, Leader SAR/R.L
- Diary: "7 November 2010, Kimberley Lowe" entry with Start: 71761, End: 71800

**Data to add:**
- Date: 2010-11-07
- Team: B
- Start_Unit: 71761
- End_Unit: 71800
- Leader: Shawn Ross | Royce Lawrence
- Walkers: (from diary/DPF)

**Reasoning:** Complete record exists in both sources but missing from CSV.

**User Decision:**
- [ ] Approve
- [ ] Modify: _______________

**Status:** Pending

---

### D005: Add Missing Nov 10 Record (MAJOR)

**Record:** 2010-11-10, Team B
**Field:** Entire record
**Current:** MISSING
**Source evidence:**
- DPF Day_08.pdf Form 1: Date 10/Nov/2010, Units 71801-71833, Leader R.L
- Diary: "10 November 2010, Kimberley Lowe" entry with Start: 71801, End: 71833

**Data to add:**
- Date: 2010-11-10
- Team: B
- Start_Unit: 71801
- End_Unit: 71833
- Leader: Royce Lawrence
- Walkers: KL, EJ, RL, JP, ACQ, DG (6 walkers)

**Reasoning:** Complete record exists in both sources but missing from CSV.

**User Decision:**
- [ ] Approve
- [ ] Modify: _______________

**Status:** Pending

---

## Unit Continuity Check

| Date | End Unit | Next Date | Start Unit | Gap | Status |
|------|----------|-----------|------------|-----|--------|
| Nov 2 | 71524 | Nov 3 | 71525 | +1 | ✓ |
| Nov 3 | 71583 | Nov 4 | 71584 | +1 | ✓ |
| Nov 4 | 71649 | Nov 5 | 71650 | +1 | ✓ |
| Nov 5 | 71712 | Nov 6 | 71713 | +1 | ✓ |
| Nov 6 | 71760 | Nov 7 | 71761 | +1 | ✓ |
| Nov 7 | 71800 | Nov 10 | 71801 | +1 | ✓ |
| Nov 10 | 71833 | Nov 11 | 71834 | +1 | ✓ |
| Nov 11 | 71909 | Nov 12 | 71910 | +1 | ✓ |
| Nov 12 | 71980 | Nov 14 | 71981 | +1 | ✓ |
| Nov 14 | 72024 | Nov 15 | 72025 | +1 | ✓ |

**Note:** Unit continuity is perfect after applying corrections. The missing records (Nov 7, Nov 10) were identified via continuity gaps in the original CSV.

---

## Summary Statistics

| Metric | Count |
|--------|-------|
| Records checked | 9 (original) + 2 missing = 11 total |
| Records confirmed | 6 |
| Issues found | 5 |
| Corrections required | 5 |
| MAJOR issues | 2 (missing records) |

### Issues by Category
- Unit errors: 3 (D001, D002, D003)
- Missing records: 2 (D004, D005)
- Walker errors: 0
- Role errors: 0

---

## Source Observations

### Source Divergences

| Date | Field | DPF Value | Diary Value | CSV Value | Resolution | Note |
|------|-------|-----------|-------------|-----------|------------|------|
| Nov 2 | End_Unit | 71524 | 61524 | 71524 | DPF correct | Diary digit transposition (6↔7) |
| Nov 4 | End_Unit | 71649 | 71650 | 71650 | DPF correct | Diary off-by-one; CSV inherited error |

### Source Reliability Patterns

- **O1 confirmed:** DPF more reliable than diary for unit numbers (2 cases)
  - Nov 2: DPF 71524 correct, diary had 61524 (digit transposition)
  - Nov 4: DPF 71649 correct, diary had 71650 (off-by-one)
- **Pattern:** Diary unit errors tend to be transcription/digit errors rather than systematic

### Implications for Future QA

- DPF scans should always be PRIMARY for unit numbers when available
- Digit transposition (6↔7, 1↔7) is a common diary error pattern
- Unit continuity check (C1) helps detect when diary values are erroneous

---

## Notes

### Observation: Nov 3 Start Unit Error Pattern
The CSV value 71245 for Nov 3 Start Unit appears to be a transcription/OCR error. The correct value 71525 maintains unit continuity with Nov 2 (ends 71524).

### Observation: Nov 4 End Unit Discrepancy
Diary shows 71650, DPF shows 71649. Per source priority rules (DPF PRIMARY for unit numbers), 71649 is correct. This also maintains proper continuity with Nov 5 (starts 71650).

### Missing Records Discovery
The missing Nov 7 and Nov 10 records were discoverable through:
1. Unit continuity analysis (gaps in sequence)
2. Diary entries for those dates
3. DPF forms (Day_06.pdf Form 2, Day_08.pdf Form 1)

---

**Document created:** 2025-11-27
**Last updated:** 2025-11-27
