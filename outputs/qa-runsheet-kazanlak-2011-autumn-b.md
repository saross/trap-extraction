# QA Runsheet: Kazanlak 2011 Autumn Team B

**Study Area/Season:** Kazanlak (Seuthopolis) 2011 Autumn
**Team:** B
**QA Date:** 2025-12-01
**QA Performed By:** Claude Code (with Shawn Ross)
**Records in CSV:** 17
**Date Range:** 2011-11-03 to 2011-11-29

---

## Sources Consulted

| Type | File | Location | Role |
|------|------|----------|------|
| DPF scan | B_2011Summary.pdf | `Kazanluk/2011-11-30/Project Records/Team B/FieldRecords/` | PRIMARY (694 KB, 8 pages) |
| DPF scan | B_20111129.pdf | `Kazanluk/2011-11-30/Project Records/Team B/FieldRecords/` | Verification (635 KB) |
| Diary | B_2011Diary_En.docx | `Kazanluk/2011-11-30/Project Records/Team B/` | Reference (EN, 63 KB) |
| Diary | B_2011Diary_BG.docx | `Kazanluk/2011-11-30/Project Records/Team B/` | Reference (BG, 42 KB) |

---

## Team Composition

### Full Season: 3-29 November 2011
- **Primary Leader:** Petra Tušlová (Nov 3-12, 17-18)
- **Alternate Leaders:** Joel Sercombe (Nov 15-16), Adela Sobotkova (Nov 20-22, 29), Bara Weissová (Nov 13)
- **Core walkers:** Hamish Sinclair, Cecilia Choi, Joel Sercombe, Bethan Donnelly
- **Additional walkers:** Oscar Warren, Elaine Lin, Siobhan Lawler, Petra Janouchová, Adela Sobotkova

---

## Record-by-Record Verification

### November 2011

| Date | CSV Range | DPF Range | Total | Status |
|------|-----------|-----------|-------|--------|
| Nov 03 | 21840-21855 | 21840-21855 | 15 | ✓ CONFIRMED |
| Nov 05 | 21856-21900 | 21856-21900 | 34 | ✓ CONFIRMED |
| Nov 06 | 21901-21965 | 21901-21965 | 65 | ✓ CONFIRMED |
| Nov 07 | 21966-22016 | 21966-22016 | 50 | ✓ CONFIRMED |
| Nov 08 | 22017-22086 | 22017-22086 | 69 | ✓ CONFIRMED |
| Nov 09 | 22087-22123 | 22087-22123 | 36 | ✓ CONFIRMED |
| Nov 10 | 22124-22198 | 22124-22198 | 74 | ✓ CONFIRMED |
| Nov 12 | 22206-22243 | 22206-22243 | 37 | ✓ CONFIRMED |
| Nov 13 | 22244-22268 | 22244-22268 | 24 | ✓ CONFIRMED |
| Nov 15 | 22269-22282 | 22269-22282 | 14 | ✓ CONFIRMED |
| Nov 16 | 72088-72206 | 22283-22320 | 47 | ❌ MAJOR ERROR |
| Nov 17 | 22321-22367 | 22321-22367 | 46 | ✓ CONFIRMED |
| Nov 18 | 22368-22407 | 22368-22407 | 39 | ✓ CONFIRMED |
| Nov 20 | 22408-22462 | 22408-22462 | 54 | ✓ CONFIRMED |
| Nov 21 | 22463-22508 | 22463-22508 | 45 | ✓ CONFIRMED |
| Nov 22 | 22509-22542 | 22509-22542 | 33 | ✓ CONFIRMED |
| Nov 29 | 22600-22613 | 22600-22613 | 14 | ✓ CONFIRMED |

---

## Issues Summary

| ID | Date | Field | Issue | Action |
|----|------|-------|-------|--------|
| B001 | Nov 16 | Unit Range | CSV: 72088-72206 (WRONG SOURCE), DPF: 22283-22320 | [ ] Update to 22283-22320 |

---

## Corrections Required

### B001: Nov 16 Unit Range (CRITICAL)
- **Current:** Start Unit = 72088, End Unit = 72206
- **DPF shows:** Start Unit = 22283, End Unit = 22320, Total = 47 units
- **Root cause:** CSV extraction used wrong source file ("Yam10_SurveySummary.xls" - Yambol 2010 data instead of Kazanlak 2011)
- **Evidence:** The 72xxx prefix belongs to Yambol region; Kazanlak 2011 Team B uses 21xxx-22xxx prefix
- **Unit continuity:** Nov 15 ends at 22282; Nov 17 starts at 22321. DPF value 22283-22320 fits perfectly.
- **Recommendation:** Update to 22283-22320 (URGENT - wrong region data)
- [ ] User Decision Required

---

## Source Observations

### Unit Sequence Analysis

| Date | DPF Start | DPF End | Total | Continuity |
|------|-----------|---------|-------|------------|
| Nov 03 | 21840 | 21855 | 15 | Start |
| Nov 05 | 21856 | 21900 | 34 | Continuous |
| Nov 06 | 21901 | 21965 | 65 | Continuous |
| Nov 07 | 21966 | 22016 | 50 | Continuous |
| Nov 08 | 22017 | 22086 | 69 | Continuous |
| Nov 09 | 22087 | 22123 | 36 | Continuous |
| Nov 10 | 22124 | 22198 | 74 | Continuous |
| Nov 12 | 22206 | 22243 | 37 | Gap of 7 (22199-22205) |
| Nov 13 | 22244 | 22268 | 24 | Continuous |
| Nov 15 | 22269 | 22282 | 14 | Continuous |
| Nov 16 | 22283 | 22320 | 47 | Continuous |
| Nov 17 | 22321 | 22367 | 46 | Continuous |
| Nov 18 | 22368 | 22407 | 39 | Continuous |
| Nov 20 | 22408 | 22462 | 54 | Continuous |
| Nov 21 | 22463 | 22508 | 45 | Continuous |
| Nov 22 | 22509 | 22542 | 33 | Continuous |
| Nov 29 | 22600 | 22613 | 14 | Gap of 57 (22543-22599) |

**Total units surveyed:** ~770 units across 17 days

### Non-Survey Days

| Date | Status |
|------|--------|
| Nov 04 | No survey (likely rest day after season start) |
| Nov 11 | No survey |
| Nov 14 | No survey |
| Nov 19 | No survey |
| Nov 23-28 | No survey (gap before final day) |

### Source Reliability Patterns

- **High accuracy:** 16 of 17 records (94%) have exact unit matches with DPF
- **Critical error:** Nov 16 extracted from wrong source file (Yambol instead of Kazanlak)
- **Nov 29 verified:** Separate daily file B_20111129.pdf confirms units 22600-22613
- **Consistent leadership:** Petra Tušlová led majority of days; leadership changes clearly documented

---

## Notes

- **Wrong source extraction:** The Nov 16 error is serious - data from Yambol 2010 was incorrectly attributed to Kazanlak 2011 Team B. The source field shows "Yam10_SurveySummary.xls" which is clearly the wrong file.
- **Unit gap Nov 10-12:** Small gap of 7 units (22199-22205) may represent allocation to another team.
- **Unit gap Nov 22-29:** Larger gap of 57 units (22543-22599) suggests survey pause or other team allocation.
- **Final survey day:** Nov 29 documented in separate daily file, not in summary PDF (diary ends Nov 25).

---

## Summary Statistics

| Metric | Count |
|--------|-------|
| Records in CSV | 17 |
| Records in DPF | 17 |
| Records confirmed | 16 |
| Unit discrepancies | 1 (B001 - CRITICAL) |
| Missing records | 0 |
| Corrections required | 1 |

### Issues by Category
- Wrong source extraction: 1 (B001 - Nov 16)
- Unit range errors: 0
- Missing records: 0
- Walker errors: 0
- Role errors: 0

---

**Document created:** 2025-12-01
**Last updated:** 2025-12-01
