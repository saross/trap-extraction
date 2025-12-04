# QA Runsheet: Kazanlak 2011 Autumn Team C

**Study Area/Season:** Kazanlak (Seuthopolis) 2011 Autumn
**Team:** C
**QA Date:** 2025-12-01
**QA Performed By:** Claude Code (with Shawn Ross)
**Records in CSV:** 18 (17 survey days + 1 non-survey day)
**Date Range:** 2011-11-02 to 2011-11-24

---

## Sources Consulted

| Type | File | Location | Role |
|------|------|----------|------|
| DPF scan | C_2011Summary.pdf | `Kazanluk/2011-11-30/Project Records/Team C/FieldRecords/` | PRIMARY (3.4 MB, 9 pages) |
| Diary | C_2011Diary_En.docx | `Kazanluk/2011-11-30/Project Records/Team C/` | Reference (EN, 70 KB) |
| Diary | C_2011Diary_BG.docx | `Kazanluk/2011-11-30/Project Records/Team C/` | Reference (BG, 18 KB) |

---

## Team Composition

### Full Season: 2-24 November 2011
- **Primary Leader:** Shawn Ross (throughout, except Nov 13 & 15)
- **Alternate Leaders:** Bara Weissová (Nov 13), Cecilia Choi (Nov 15)
- **Core walkers:** Jodie McClintock, Georgia Burnett, Corinne Softley
- **Additional walkers:** Cecilia Choi, Martin Mladenov, Oscar Warren, Eva Tonkova, Siobhan Lawler, Elaine Lin, Hannah Morris, Tanya Mateeva

### DPF Authors
- **Primary:** Corinne Softley, Jodie McClintock
- **Others:** Martin Mladenov, Cecilia Choi, Elaine Lin, Georgia Burnett

---

## Record-by-Record Verification

### November 2011

| Date | CSV Range | DPF Range | Total | Status |
|------|-----------|-----------|-------|--------|
| Nov 02 | 30821-30880 | 30821-30880 | 59 | ✓ CONFIRMED |
| Nov 03 | 30881-30949 | 30881-30949 | 68 | ✓ CONFIRMED |
| Nov 05 | 30950-30971 | 30950-30971 | 21 | ✓ CONFIRMED |
| Nov 06 | 30972-31020 | 30972-31020 | 48 | ✓ CONFIRMED |
| Nov 07 | 31021-31105 | 31021-31105 | 85 | ✓ CONFIRMED |
| Nov 08 | 31106-31180 | 31106-31180 | 75 | ✓ CONFIRMED |
| Nov 09 | 31181-31245 | 31181-31245 | 65 | ✓ CONFIRMED |
| Nov 12 | — | (no units) | — | ✓ Non-survey: Mound recording |
| Nov 13 | 31246-31250 | 31246-31250 | 5 | ✓ CONFIRMED |
| Nov 15 | 31251-31284 | 31251-31284 | 33 | ✓ CONFIRMED |
| Nov 16 | 31285-31302 | 31285-31302 | 18 | ✓ CONFIRMED |
| Nov 17 | 31303-31335 | 31303-31335 | 33 | ✓ CONFIRMED |
| Nov 18 | 31335-31342 | 31336-31343 | 8 | ⚠️ OVERLAP ERROR |
| Nov 20 | 31344-31355 | 31344-31355 | 12 | ✓ CONFIRMED |
| Nov 21 | 31356-31376 | 31356-31376 | 21 | ✓ CONFIRMED |
| Nov 22 | 31377-31395 | 31377-31395 | 19 | ✓ CONFIRMED |
| Nov 23 | 31396-31439 | 31396-31439 | 44 | ✓ CONFIRMED |
| Nov 24 | 31440-31450 | 31440-31450 | 11 | ✓ CONFIRMED |

---

## Issues Summary

| ID | Date | Field | Issue | Action |
|----|------|-------|-------|--------|
| C001 | Nov 18 | Unit Range | CSV: 31335-31342, DPF: 31336-31343 (start overlaps Nov 17 end) | [ ] Update to 31336-31343 |

---

## Corrections Required

### C001: Nov 18 Unit Range (OVERLAP ERROR)
- **Current:** Start Unit = 31335, End Unit = 31342
- **DPF shows:** Start Unit = 31336, End Unit = 31343, Total = 8 units
- **Problem:** CSV Start Unit 31335 is identical to Nov 17's End Unit 31335, creating an overlap
- **Continuity analysis:**
  - Nov 17 DPF: 31303-31335 (ends at 31335)
  - Nov 18 DPF: 31336-31343 (starts at 31336, continuous)
  - Nov 20 DPF: 31344-31355 (starts at 31344, continuous)
- **Unit count:** Both CSV and DPF show 8 units for Nov 18 (count is correct, range shifted by 1)
- **Recommendation:** Update to 31336-31343
- [ ] User Decision Required

---

## Source Observations

### Unit Sequence Analysis

| Date | DPF Start | DPF End | Total | Continuity |
|------|-----------|---------|-------|------------|
| Nov 02 | 30821 | 30880 | 59 | Start |
| Nov 03 | 30881 | 30949 | 68 | Continuous |
| Nov 05 | 30950 | 30971 | 21 | Continuous |
| Nov 06 | 30972 | 31020 | 48 | Continuous |
| Nov 07 | 31021 | 31105 | 85 | Continuous |
| Nov 08 | 31106 | 31180 | 75 | Continuous |
| Nov 09 | 31181 | 31245 | 65 | Continuous |
| Nov 12 | — | — | — | Non-survey |
| Nov 13 | 31246 | 31250 | 5 | Continuous |
| Nov 15 | 31251 | 31284 | 33 | Continuous |
| Nov 16 | 31285 | 31302 | 18 | Continuous |
| Nov 17 | 31303 | 31335 | 33 | Continuous |
| Nov 18 | 31336 | 31343 | 8 | Continuous |
| Nov 20 | 31344 | 31355 | 12 | Continuous |
| Nov 21 | 31356 | 31376 | 21 | Continuous |
| Nov 22 | 31377 | 31395 | 19 | Continuous |
| Nov 23 | 31396 | 31439 | 44 | Continuous |
| Nov 24 | 31440 | 31450 | 11 | Continuous |

**Total units surveyed:** ~630 units across 17 survey days

### Non-Survey Days

| Date | Reason | DPF Form | CSV Flag |
|------|--------|----------|----------|
| Nov 04 | No survey | No form | Not in CSV |
| Nov 10-11 | No survey | No form | Not in CSV |
| Nov 12 | Mound recording (non-unit work) | Form present (extensive objects) | Correctly flagged |
| Nov 14 | No survey | No form | Not in CSV |
| Nov 19 | No survey | No form | Not in CSV |

### Source Reliability Patterns

- **Excellent accuracy:** 17 of 18 records (94%) have exact unit matches with DPF
- **Single error:** Nov 18 has overlap with Nov 17 due to off-by-one start unit
- **Nov 12 handling:** Correctly flagged as non-survey (mound recording day) with no unit range
- **Consistent leadership:** Shawn Ross led most days; two days had alternate leaders (Bara, Cecilia)

---

## Notes

- **High productivity team:** Team C completed ~630 units across 17 survey days, averaging 37 units/day.
- **Skipped units:** Nov 05 DPF notes unit 30958 was skipped - this is within the recorded range and doesn't affect counts.
- **Mixed survey types:** Most days had intensive survey; later days (Nov 16 onwards) shifted to extensive survey for mound reconnaissance.
- **Nov 12 context:** The team spent the day recording mounds (objects 3244, 3268, 3500-3508) without conducting unit-based survey.
- **Unit overlap on Nov 18:** The CSV start unit 31335 duplicates Nov 17's end unit, likely a transcription error.

---

## Summary Statistics

| Metric | Count |
|--------|-------|
| Records in CSV | 18 |
| Records in DPF | 18 |
| Survey days | 17 |
| Non-survey days | 1 |
| Records confirmed | 17 |
| Unit discrepancies | 1 (C001) |
| Missing records | 0 |
| Corrections required | 1 |

### Issues by Category
- Unit overlap errors: 1 (C001 - Nov 18)
- Missing records: 0
- Walker errors: 0
- Role errors: 0
- Other: 0

---

**Document created:** 2025-12-01
**Last updated:** 2025-12-01
