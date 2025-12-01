# QA Runsheet: Kazanlak 2010 Spring Team D

**Study Area/Season:** Kazanlak (Seuthopolis) 2010 Spring
**Team:** D
**QA Date:** 2025-12-01
**QA Performed By:** Claude Code (with Shawn Ross)
**Records in CSV:** 14 (13 survey days + 1 non-survey day)
**Date Range:** 2010-03-18 to 2010-04-01

---

## Sources Consulted

| Type | File | Location | Role |
|------|------|----------|------|
| DPF scan | D_2010Summary.pdf | `Kazanluk/2010/Project Records/Team D/FieldRecords/` | PRIMARY (219 KB, 5 pages) |
| Diary | D_2010Diary_BG.doc | `Kazanluk/2010/Project Records/Team D/` | Reference (BG, 127 KB) |
| Diary | D_2010Diary_En.docx | `Kazanluk/2010/Project Records/Team D/` | Reference (EN, 26 KB) |

---

## Team Composition

### Full Season: 18 March - 1 April 2010
- **Leader:** Georgi Nekhrizov (Zhoro) - throughout except Apr 1
- **Apr 1 Leader:** Nadezhda Kecheva (Nadja)
- **Core walkers:** Vera Doležálková, Lyubomir Markovski (Ljubo), Nadezhda Kecheva (Nadja)
- **Rotating walkers:** Julia Tzvetkova, Bogdana Lilova, Martin Mladenov, Viktorie Chystyaková (Viki), Yulia Dimitrova, Dagmar Winklerová (Dasa), Lindsay Prazak, Renee Gardiner, Todor Vulchev (Teodor)
- **Primary DPF Author:** Vera Doležálková

---

## Record-by-Record Verification

### March 2010

| Date | CSV Range | DPF Range | Total | Status |
|------|-----------|-----------|-------|--------|
| Mar 18 | 40251-40301 | 40251-40301 | 50 | ✓ CONFIRMED |
| Mar 19 | 40302-40353 | 40302-40353 | 51 | ✓ CONFIRMED |
| Mar 20 | 40354-40432 | 40354-40432 | 78 | ✓ CONFIRMED |
| Mar 21 | 40424-40482 | 40424-40482 | 56 | ✓ CONFIRMED (note: overlaps Mar 20) |
| Mar 22 | 40483-40544 | 40483-40544 | 61 | ✓ CONFIRMED |
| Mar 23 | — | (no form) | — | ✓ Non-survey: Rain day |
| Mar 24 | 40545-40640 | 40545-40640 | 95 | ✓ CONFIRMED |
| Mar 25 | 40641-40676 | 40641-40676 | 35 | ✓ CONFIRMED |
| Mar 26 | 40667-40737 | 40677-40737 | 60 | ⚠️ START UNIT ERROR |
| Mar 27 | 40738-40773 | 40738-40773 | 35 | ✓ CONFIRMED |
| Mar 28 | 40774-40800 | 40774-40800 | 27 | ✓ CONFIRMED |
| Mar 30 | 40801-40841 | 40801-40841 | 40 | ✓ CONFIRMED |
| Mar 31 | 40842-40877 | 40842-40877 | 36 | ✓ CONFIRMED |

### April 2010

| Date | CSV Range | DPF Range | Total | Status |
|------|-----------|-----------|-------|--------|
| Apr 01 | 40878-40914 | 40878-40914 | 36 | ✓ CONFIRMED |

---

## Issues Summary

| ID | Date | Field | Issue | Action |
|----|------|-------|-------|--------|
| D001 | Mar 26 | Start Unit | CSV: 40667, DPF: 40677 (10 unit difference) | [ ] Update to 40677 |

---

## Corrections Required

### D001: Mar 26 Start Unit
- **Current:** Start Unit = 40667
- **DPF shows:** Start Unit = 40677
- **Gap analysis:** Mar 25 DPF ends at 40676; Mar 26 DPF starts at 40677 (continuous). CSV value 40667 overlaps with Mar 25 range.
- **Recommendation:** Update to 40677
- [ ] User Decision Required

---

## Source Observations

### Unit Sequence Analysis

| Date | DPF Start | DPF End | Continuity |
|------|-----------|---------|------------|
| Mar 18 | 40251 | 40301 | Start |
| Mar 19 | 40302 | 40353 | Continuous |
| Mar 20 | 40354 | 40432 | Continuous |
| Mar 21 | 40424 | 40482 | **Overlaps Mar 20 by 9 units** |
| Mar 22 | 40483 | 40544 | Continuous from Mar 21 |
| Mar 24 | 40545 | 40640 | Continuous |
| Mar 25 | 40641 | 40676 | Continuous |
| Mar 26 | 40677 | 40737 | Continuous |
| Mar 27 | 40738 | 40773 | Continuous |
| Mar 28 | 40774 | 40800 | Continuous |
| Mar 30 | 40801 | 40841 | Continuous |
| Mar 31 | 40842 | 40877 | Continuous |
| Apr 01 | 40878 | 40914 | Continuous |

### Notable Pattern: Mar 20-21 Overlap

Both CSV and DPF show that Mar 21 (40424-40482) overlaps with Mar 20 (40354-40432) by 9 units. This is consistent across sources and may represent:
- Resurvey of specific units
- Units walked by different sub-teams on different days
- Intentional overlap for quality control

This is **not an error** - both sources agree on this unusual pattern.

### Source Reliability Patterns

- **High accuracy:** 12 of 13 survey days (92%) have exact unit matches
- **Single error:** Mar 26 Start Unit is incorrect in CSV (40667 instead of 40677)
- **Non-survey day:** Mar 23 correctly flagged as rain cancellation in both sources
- **Consistent leadership:** Georgi Nekhrizov led all days except Apr 1

---

## Notes

- **BG diary primary:** The Bulgarian diary (127 KB) was the primary source for many records.
- **Unit overlap:** The Mar 20-21 overlap is unusual but verified - not a data error.
- **Weather interruption:** Mar 23 was cancelled due to rain (confirmed in Team B diary).
- **Leadership change:** Nadezhda Kecheva led on Apr 1 while Georgi was absent.

---

## Summary Statistics

| Metric | Count |
|--------|-------|
| Records in CSV | 14 |
| Survey days | 13 |
| Non-survey days | 1 |
| Records confirmed | 12 |
| Unit discrepancies | 1 (D001) |
| Missing records | 0 |
| Corrections required | 1 |

### Issues by Category
- Unit range errors: 1 (D001 - Mar 26)
- Missing records: 0
- Walker errors: 0
- Role errors: 0
- Other: 0

---

**Document created:** 2025-12-01
**Last updated:** 2025-12-01
