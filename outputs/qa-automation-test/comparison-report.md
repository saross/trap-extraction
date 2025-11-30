# QA Automation Test: Comparison Report

**Created:** 2025-11-27
**Purpose:** Compare automated QA results against manual QA to validate the automation pipeline

---

## Test 1: ELH-2010-B (Elhovo 2010 Autumn Team B)

### Ground Truth (Manual QA)

From `outputs/qa-runsheet-elhovo-2010-autumn.md`, Team B issues found:

| Issue | Date | Field | Problem | Resolution |
|-------|------|-------|---------|------------|
| #6 | 2010-11-03 | Start_Unit | 71245 (wrong) | → 71525 |
| #7 | 2010-11-04 | End_Unit | 71650 (wrong) | → 71649 |
| #8 | 2010-11-06 | Start/End_Unit | Empty (missing) | → 71713/71760 |
| #9 | 2010-11-07 | Entire record | MISSING | Add record |
| #10 | 2010-11-10 | Entire record | MISSING | Add record |

### Automated QA Results

From `outputs/qa-automation-test/qa-runsheet-elhovo-2010-autumn-b.md`:

| Issue | Date | Field | Problem | Resolution |
|-------|------|-------|---------|------------|
| D001 | 2010-11-03 | Start_Unit | 71245 (wrong) | → 71525 |
| D002 | 2010-11-04 | End_Unit | 71650 (wrong) | → 71649 |
| D003 | 2010-11-06 | Start/End_Unit | Empty (missing) | → 71713/71760 |
| D004 | 2010-11-07 | Entire record | MISSING | Add record |
| D005 | 2010-11-10 | Entire record | MISSING | Add record |

### Comparison Results

| Metric | Count |
|--------|-------|
| **True Positives** | 5 |
| **False Negatives** | 0 |
| **False Positives** | 0 |
| **Precision** | 100% |
| **Recall** | 100% |

### Issue-by-Issue Match

| Manual | Automated | Match |
|--------|-----------|-------|
| #6 (Start_Unit) | D001 | ✅ Exact match |
| #7 (End_Unit) | D002 | ✅ Exact match |
| #8 (Missing units) | D003 | ✅ Exact match |
| #9 (Missing record) | D004 | ✅ Exact match |
| #10 (Missing record) | D005 | ✅ Exact match |

### Notes

1. **All 5 Team B issues found** — The automation correctly identified every discrepancy that the manual QA found.

2. **Same evidence cited** — Both manual and automated QA used the same sources (DPF scans as PRIMARY for unit numbers, diary for context).

3. **Same corrections proposed** — The recommended values match exactly.

4. **Unit continuity analysis worked** — The automation used unit continuity (Rule C1) to flag potential issues, which helped identify the missing records.

---

## Test 2: ELH-2009-A (Elhovo 2009 Autumn Team A)

### Ground Truth (Manual QA)

From `outputs/qa-runsheet-elhovo-2009-autumn-a.md`, Team A issues found:

| Issue | Date(s) | Field | Problem | Resolution |
|-------|---------|-------|---------|------------|
| D015 | 2009-10-21 | Start_Unit | Diary error (60196) | No change (CSV 60195 correct) |
| D016 | 2009-10-26 to 29 | Walkers | Eric→Tereza substitution | 8 field updates |
| D017 | Oct 30, 31, Nov 4 | QA_Notes | Erroneous text | N/A (not on Team A records) |
| D018 | 2009-11-09 | Author | Missing field | Add "Adela Sobotkova" |

**Actionable corrections:** 9 field updates (D016: 8 walker fields + D018: 1 author field)

### Automated QA Results

From `outputs/qa-automation-test/qa-runsheet-elhovo-2009-autumn-a.md`:

| Issue | Date(s) | Field | Problem | Resolution |
|-------|---------|-------|---------|------------|
| D001-D004 | 2009-10-26 to 29 | Walkers | Eric→Tereza substitution | 8 field updates |
| D005 | 2009-11-09 | Author | Missing field | Add "Adela Sobotkova" |

### Comparison Results

| Metric | Count |
|--------|-------|
| **True Positives** | 9 (all field updates) |
| **False Negatives** | 0 |
| **False Positives** | 0 |
| **Precision** | 100% |
| **Recall** | 100% |

### Issue-by-Issue Match

| Manual | Automated | Match |
|--------|-----------|-------|
| D015 (diary error, no change) | Not flagged | ✅ Correct (no false positive) |
| D016 (walker ×8 fields) | D001-D004 | ✅ Exact match |
| D017 (not on Team A) | Not flagged | ✅ Correct (not applicable) |
| D018 (author field) | D005 | ✅ Exact match |

### Notes

1. **Walker substitution detected** — The automation correctly identified the Eric→Tereza substitution from diary narrative:
   - Oct 25: "Eric decided to go on to Istanbul"
   - Oct 26: "Tereza as a substitute for Eric"

2. **Name disambiguation worked** — Correctly identified Tereza Dobrovodská (from Team C) rather than Tereza Blažková using H2 heuristic (one team per day).

3. **Diary error not flagged** — D015 (Oct 21 start unit 60196 vs 60195) correctly NOT flagged since CSV is already correct.

4. **Missing author detected** — Found empty Author field on Nov 9.

---

## Test Summary

| Test | Records | Manual Issues | Auto Issues | TP | FN | FP |
|------|---------|---------------|-------------|----|----|-----|
| ELH-2010-B | 9 | 5 | 5 | 5 | 0 | 0 |
| ELH-2009-A | 22 | 9* | 9 | 9 | 0 | 0 |

*Manual issues = actionable corrections only (D016: 8 + D018: 1 = 9)

**Overall Result:** ✅ **PASS** — Automation matched manual QA for both tests.

---

## Test 3: ELH-2009-B (Elhovo 2009 Autumn Team B)

### Ground Truth (Manual QA)

From `docs/qa-discrepancies-log.md`, Team B issues found:

| Issue | Date(s) | Field | Problem | Resolution |
|-------|---------|-------|---------|------------|
| D011 | 2009-11-02 | Start/End_Unit | Missing 70926-70962 | Add units |
| D012 | 2009-11-03 | Start/End_Unit | Missing 70963-71062 | Add units |
| D013 | 2009-11-05 | Start/End_Unit | Missing 71063-71142 | Add units |
| D014 | Nov 2, 3, 5 | QA_Notes | Erroneous "no autumn diary" | Remove text |

**Actionable corrections:** 9 field updates (6 unit fields + 3 QA_Notes)

### Automated QA Results

From `outputs/qa-automation-test/qa-runsheet-elhovo-2009-autumn-b.md`:

| Issue | Date(s) | Field | Problem | Resolution |
|-------|---------|-------|---------|------------|
| D001/D002 | 2009-11-02 | Units + QA_Notes | Missing 70926-70962 + erroneous notes | Add units, fix notes |
| D003/D004 | 2009-11-03 | Units + QA_Notes | Missing 70963-71062 + erroneous notes | Add units, fix notes |
| D005/D006 | 2009-11-05 | Units + QA_Notes | Missing 71063-71142 + erroneous notes | Add units, fix notes |

### Comparison Results

| Metric | Count |
|--------|-------|
| **True Positives** | 9 (all field updates) |
| **False Negatives** | 0 |
| **False Positives** | 0 |
| **Precision** | 100% |
| **Recall** | 100% |

### Notes

1. **Missing units detected** — Diary clearly shows unit ranges for Nov 2, 3, 5.

2. **Erroneous QA_Notes flagged** — "No autumn 2009 survey season" statement is factually wrong; diary covers Oct 10 - Nov 21, 2009.

3. **Unit continuity validation** — Nov 2 start (70926) follows Oct 29 end (70925) + 1.

---

## Test 4: ELH-2009-C (Elhovo 2009 Autumn Team C)

### Ground Truth (Manual QA)

From `outputs/qa-runsheet-elhovo-2009-autumn-c.md`, Team C issues found:

| Issue | Date(s) | Field | Problem | Resolution |
|-------|---------|-------|---------|------------|
| D019 | Oct 14, 16, 17, 18 | QA_Notes | Erroneous "no autumn diary" | Replace with non-survey note |
| D020 | 2009-10-15 | End_Unit | Diary error (80103) | No change (CSV 80115 correct) |
| D021 | 2009-10-22 | Walkers | Georgi listed but absent | Remove Georgi ×2 fields |
| D022 | 2009-11-12 | End_Unit | Diary 80938, CSV 80939 | Accept CSV (minor) |
| D023 | 2009-11-13 | Start_Unit | 80839 typo | Correct to 80939 |

**Actionable corrections:** 7 field updates (D019: 4, D021: 2, D023: 1)

### Automated QA Results

From `outputs/qa-automation-test/qa-runsheet-elhovo-2009-autumn-c.md`:

| Issue | Date(s) | Field | Problem | Resolution |
|-------|---------|-------|---------|------------|
| D001-D004 | Oct 14, 16, 17, 18 | QA_Notes | Erroneous text | Replace with non-survey note |
| D005 | 2009-10-22 | Walkers | Georgi listed but absent | Remove Georgi ×2 fields |
| D006 | 2009-11-13 | Start_Unit | 80839 typo | Correct to 80939 |

### Comparison Results

| Metric | Count |
|--------|-------|
| **True Positives** | 7 (all field updates) |
| **False Negatives** | 0 |
| **False Positives** | 0 |
| **Precision** | 100% |
| **Recall** | 100% |

### Issue-by-Issue Match

| Manual | Automated | Match |
|--------|-----------|-------|
| D019 (QA_Notes ×4) | D001-D004 | ✅ Exact match |
| D020 (diary error, no change) | Not flagged | ✅ Correct (CSV correct) |
| D021 (Georgi absent ×2) | D005 | ✅ Exact match |
| D022 (minor, accepted) | Not flagged | ✅ Correct (minor variance) |
| D023 (Start_Unit typo) | D006 | ✅ Exact match |

### Notes

1. **Non-survey days handled correctly** — Oct 14, 16, 17, 18 correctly identified as non-survey days.

2. **Walker absence detected** — Diary statement "walked in five people because Georgi was away" flagged the error.

3. **Unit continuity caught typo** — 80839 < Nov 12 start (80910), impossible for sequential dates.

4. **Diary errors not flagged** — D020 and D022 correctly NOT flagged since CSV values are correct.

---

## Test Summary

| Test | Records | Manual Issues | Auto Issues | TP | FN | FP |
|------|---------|---------------|-------------|----|----|-----|
| ELH-2010-B | 9 | 5 | 5 | 5 | 0 | 0 |
| ELH-2009-A | 22 | 9* | 9 | 9 | 0 | 0 |
| ELH-2009-B | 20 | 9 | 9 | 9 | 0 | 0 |
| ELH-2009-C | 20 | 7 | 7 | 7 | 0 | 0 |
| **TOTAL** | **71** | **30** | **30** | **30** | **0** | **0** |

*Manual issues = actionable corrections only

**Overall Precision:** 100% (30/30)
**Overall Recall:** 100% (30/30)

---

## Final Assessment

### ✅ AUTOMATION VALIDATED

The QA automation pipeline achieved **100% precision and recall** across all four test cases:

1. **Unit errors detected** — All missing/incorrect unit numbers found
2. **Walker errors detected** — Substitutions and absences correctly identified
3. **QA_Notes errors detected** — Erroneous metadata flagged
4. **Missing records detected** — Nov 7, Nov 10 (2010-B) correctly identified
5. **Diary errors NOT flagged** — No false positives when CSV was correct

### Capabilities Demonstrated

| Capability | Test Evidence |
|------------|---------------|
| Unit continuity analysis (C1) | Nov 3 Start_Unit error, Nov 13 Start_Unit typo |
| Narrative interpretation | Eric→Tereza substitution (Oct 26-29) |
| Name disambiguation (H2) | Tereza Dobrovodská vs Blažková |
| Non-survey day handling | Oct 14/16/17/18, Oct 30/31, Nov 4 |
| Source priority rules | DPF PRIMARY for units, diary for walkers |
| Missing record detection | Nov 7 and Nov 10 (2010-B) |

### Recommendation

**Proceed with remaining QA queue** using the automated pipeline. The automation successfully reproduced all manual QA findings with no false positives or negatives.

---

## Observations

### What Worked Well

1. **Source priority rules** — DPF PRIMARY for unit numbers correctly identified Nov 4 End_Unit discrepancy (diary had 71650, DPF had 71649).

2. **Unit continuity check** — Caught the impossible Nov 3 Start_Unit (71245 < Nov 2 End_Unit 71524).

3. **Missing record detection** — Both diary and DPF cross-reference successfully identified Nov 7 and Nov 10 missing records.

4. **Runsheet format** — Output follows the template with daily breakdown, sources consulted, corrections with checkboxes.

### Not Tested Yet

1. **Walker duplicate detection** — Team A had systematic walker duplicates (Issues #1-5). Need to test on data with walker errors.

2. **Non-survey day handling** — ELH-2009-C had non-survey days. Need to test that convention.

3. **Name disambiguation** — ELH-2009 Teams had name disambiguation cases.

4. **Bulgarian-only diaries** — Kazanlak teams have BG-only diaries.

---

## Completed Tests

1. ✅ ELH-2010-B — All 5 issues found (unit errors, missing records)
2. ✅ ELH-2009-A — Walker substitution detected via narrative interpretation
3. ✅ ELH-2009-B — Missing units and erroneous QA_Notes found
4. ✅ ELH-2009-C — Non-survey days, walker absence, unit typo all detected

---

## Next Steps

1. ~~**Implement Source Observations enhancement**~~ ✅ DONE — See `planning/source-observations-enhancement.md`
2. **Process remaining QA queue** — 14 team-seasons pending (see `docs/qa-automation/qa-queue.yaml`)
3. **Consider cross-model comparison** — Test with Gemini to compare results

---

## Source Observations Validation

**Test Date:** 2025-11-27
**Purpose:** Validate that the Source Observations enhancement correctly captures source-vs-source divergences

### Expected vs Actual Divergences

| Team-Season | Expected Divergences | Actual Divergences | Match |
|-------------|---------------------|-------------------|-------|
| ELH-2010-B | Nov 2 (diary 61524 vs DPF 71524), Nov 4 (diary 71650 vs DPF 71649) | Nov 2 (diary 61524 vs DPF 71524), Nov 4 (diary 71650 vs DPF 71649) | ✅ |
| ELH-2009-A | Oct 21 (diary 60196 vs SU form 60195) | Oct 21 (diary 60196 vs SU form 60195) | ✅ |
| ELH-2009-B | None (single-source) | None (single-source) | ✅ |
| ELH-2009-C | Oct 15 (diary 80103 vs SU form 80115), Nov 12 (diary 80938 vs CSV 80939) | Oct 15 (diary 80103 vs SU form 80115), Nov 12 (diary 80938 vs CSV 80939) | ✅ |

### Detailed Validation

#### ELH-2010-B
- **Expected:** 2 DPF-vs-diary divergences
- **Found:** ✅ Both divergences documented
  - Nov 2 End_Unit: DPF 71524, Diary 61524 (digit transposition)
  - Nov 4 End_Unit: DPF 71649, Diary 71650 (off-by-one)
- **O1 Confirmed:** Yes — DPF more reliable than diary for unit numbers

#### ELH-2009-A
- **Expected:** 1 SU form-vs-diary divergence
- **Found:** ✅ Divergence documented
  - Oct 21 Start_Unit: SU form 60195, Diary 60196 (transcription error)
- **O1 Confirmed:** Yes — SU forms more reliable than diary for unit numbers

#### ELH-2009-B
- **Expected:** No divergences (single-source, no DPF for 2009)
- **Found:** ✅ Correctly noted as single-source verification
- **O1 Status:** Not testable (no DPF available)

#### ELH-2009-C
- **Expected:** 2 diary transcription errors
- **Found:** ✅ Both divergences documented
  - Oct 15 End_Unit: SU form 80115, Diary 80103 (12-unit gap)
  - Nov 12 End_Unit: CSV 80939, Diary 80938 (off-by-one)
- **O1 Confirmed:** Yes — SU forms/Excel more reliable than diary for unit numbers

### Summary

| Metric | Count |
|--------|-------|
| Expected divergences | 5 |
| Actual divergences found | 5 |
| False positives | 0 |
| False negatives | 0 |
| O1 confirmations | 3 teams (1 not testable) |

### ✅ SOURCE OBSERVATIONS VALIDATION: PASSED

All expected source-vs-source divergences were correctly captured in the Source Observations sections. The enhancement successfully:

1. **Documents divergences even when CSV correct** — Oct 15 (2009-C), Oct 21 (2009-A) where CSV was correct but diary had errors
2. **Handles single-source cases** — ELH-2009-B correctly noted as single-source (no divergences possible)
3. **Confirms O1 observation** — DPF/SU forms more reliable than diary for unit numbers (5 cases across 3 teams)
4. **Captures error patterns** — Digit transposition, off-by-one, transcription errors documented

---

**Document created:** 2025-11-27
**Last updated:** 2025-11-27
**Test status:** COMPLETE — All validation tests passed (including Source Observations)
