# QA Runsheet: Kazanlak 2009 Spring Team D

**Study Area/Season:** Kazanlak (Seuthopolis) 2009 Spring
**Team:** D
**QA Date:** 2025-11-30
**QA Performed By:** Claude Code (with Shawn Ross)
**Records in CSV:** 10
**Date Range:** 2009-03-04 to 2009-03-27

---

## Sources Consulted

| Type | File | Location | Role |
|------|------|----------|------|
| DPF scan | D_Summary.pdf | `Kazanluk/2009/Project Records/TeamD/FInalized/` | PRIMARY (280 KB, 11 pages) |
| Diary | D_Diary_En.docx | `Kazanluk/2009/Project Records/TeamD/` | Verification (EN, 61 KB) |
| Diary | D Diary_BG.doc | `Kazanluk/2009/Project Records/TeamD/` | Reference (BG, 227 KB) |

---

## Team Composition

### Survey Period: 4-27 March 2009
- **Leader:** Georgi Nekhrizov (throughout)
- **Core members:** Lyubomir Markovski (L.M.), Nadezhda Kecheva (N.K.), Barbara Klara Olujic (B.O.)
- **Rotating members:** Magda Bolečková (early), Tomáš Chmela, Vera Doležálková, Yulia Dimitrova (late)

---

## Record-by-Record Verification

### 2009-03-04 (Wednesday) — Units 40001-40066 ⚠️ MAJOR ERROR
- **DPF (p.1):** Team D, Leader: Georgi Nehrizov, Walkers: Georgi N., Nadezhda, Lubomir M., Magda B., Units: 40001-40023, Total: 23, Author: Magda B.
- **CSV:** Leader: Georgi Nekhrizov, Units: 40001-40066, Walkers: 4 (Georgi, Nadezhda, Lyubomir, Magda)
- **Source divergence:** CSV End Unit 40066 vs DPF 40023 (difference of 43 units!)
- **Status:** UNIT ERROR (D001) - CSV End Unit is incorrect

### 2009-03-07 (Saturday) — Units 40031-40032 ✓
- **DPF (p.2-3):** Team D, Leader: Georgi Nehrizov, Walkers: Georgi N., Lubomir M., Nadezda K., Barbara O., Units: 40031-40032, Total: 2, Author: Barbara Klara Olujic
- **CSV:** Leader: Georgi Nekhrizov, Units: 40031-40032, Walkers: 4 (Georgi, Lyubomir, Nadezhda, Barbara)
- **Comments:** "Walking was very difficult because of the trees, and barbed/wires with thorns"
- **Status:** CONFIRMED

### 2009-03-15 (Sunday) — Units 40039-40065 ⚠️
- **DPF (p.4):** Team D, Leader: Georgi Nekhrizov, Walkers: G.N., L.M., B.O., N.K., Units: 40039-40065 (approximately), Author: Barbara Klara Olujic
- **CSV:** Leader: Georgi Nekhrizov, Units: 40039-40065, Walkers: 4 (Georgi, Lyubomir, Barbara, Nadezhda)
- **Note:** DPF form header appears to show "J-15-03" which may indicate combined or date range
- **Status:** CONFIRMED (pending verification of DPF date interpretation)

### 2009-03-19 (Thursday) — Units 40048-40073 ⚠️ MAJOR ERROR
- **DPF (p.5):** Team D, Leader: Georgi Nekhrizov, Walkers: G.N., Ntag(?), Kata(?), B.O., Tomas, Units: 40069-40074, Total: 5, Author: Barbara/Iveta Olujic
- **CSV:** Leader: Georgi Nekhrizov, Units: 40048-40073, Walkers: 3 (Georgi, Tomáš, Barbara)
- **Source divergence:** CSV 40048-40073 vs DPF 40069-40074 - completely different ranges!
- **Analysis:** CSV Start Unit 40048 overlaps with Mar 15 range; DPF shows 40069-40074 which follows Mar 15 end (40065)
- **Status:** UNIT ERROR (D002) - CSV range is incorrect

### 2009-03-20 (Friday) — Units 40075-40082 ⚠️
- **DPF (p.6):** Team D, Leader: Georgi Nekhrizov, Walkers: G.N., B.O., Tomas, Units: 40075-40095, Total: 20, Author: Barbara Klara Olujic
- **CSV:** Leader: Georgi Nekhrizov, Units: 40075-40082, Walkers: 3 (Georgi, Barbara, Tomáš)
- **Source divergence:** CSV End Unit 40082 vs DPF 40095 (difference of 13 units)
- **Status:** UNIT ERROR (D003) - CSV End Unit is incorrect

### 2009-03-23 (Monday) — Units 40069-40094 ⚠️ MAJOR ERROR
- **DPF (p.7):** Team D, Leader: Georgi Nehrizov, Walkers: B.d(?), G.N., L.M., Units: 40096-40104 (approximately), Total: 14, Author: Barbara Klara Olujic
- **CSV:** Leader: Georgi Nekhrizov, Units: 40069-40094, Walkers: 2 (Georgi, Lyubomir)
- **Source divergence:** CSV 40069-40094 vs DPF 40096-40104 - completely different ranges!
- **Analysis:** CSV range 40069-40094 overlaps with Mar 19 and Mar 20 CSV ranges. DPF shows 40096-40104 which follows Mar 20 DPF end (40095).
- **Status:** UNIT ERROR (D004) - CSV range is incorrect

### 2009-03-24 (Tuesday) — Units 40112-40124 ✓
- **DPF (p.8):** Team D, Leader: Georgi Nehrizov, Walkers: G.N., B.O., N.K., L.M., Units: 40112-40124, Total: 12, Author: Barbara Klara Olujic
- **CSV:** Leader: Georgi Nekhrizov, Units: 40112-40124, Walkers: 4 (Georgi, Barbara, Nadezhda, Lyubomir)
- **Status:** CONFIRMED

### 2009-03-25 (Wednesday) — Units 40125-40211 ⚠️
- **DPF (p.9):** Team D, Leader: Georgi Nekhrizov, Walkers: V (Vera), B.O., N.K., L.M., G.N., Units: 40125-40214, Total: 46(?), Author: (blank)
- **CSV:** Leader: Georgi Nekhrizov, Units: 40125-40211, Walkers: 5 (Georgi, Vera, Barbara, Nadezhda, Lyubomir)
- **Source divergence:** CSV End Unit 40211 vs DPF 40214 (difference of 3 units)
- **Comments:** DPF notes "40194-40198 = SHRT SITE" (short site?)
- **Status:** UNIT DISCREPANCY (D005) - minor

### 2009-03-26 (Thursday) — Units 40212-40214 ✓
- **DPF (p.10):** Team D, Leader: Georgi Nekhrizov, Walkers: G.N., L.M., N.K., B.O., Units: 40212-40214 (approximately), Total: 5(?), Author: Barbara Klara Olujic
- **CSV:** Leader: Georgi Nekhrizov, Units: 40212-40214, Walkers: 4 (Georgi, Lyubomir, Nadezhda, Barbara)
- **Comments:** "ONE SITE"
- **Note:** DPF Start Unit field may show 40292 (transcription issue) but context suggests 40212
- **Status:** CONFIRMED (approximately)

### 2009-03-27 (Friday) — Units 40218-40250 ✓
- **DPF (p.11):** Team D, Leader: X (crossed out - no leader listed), Walkers: Jutea/Yulia (Small), L.M., B.O., Units: 40218-40250, Total: 32, Author: Barbara Klara Olujic
- **CSV:** Leader: (blank), Units: 40218-40250, Walkers: 3 (Yulia, Lyubomir, Barbara)
- **Note:** CSV correctly shows no leader, matching DPF where leader field is crossed out
- **Status:** CONFIRMED

---

## Issues Summary

| ID | Date | Field | Issue | Action |
|----|------|-------|-------|--------|
| D001 | Mar 04 | End Unit | CSV: 40066, DPF: 40023 (43 unit difference) | [ ] Update to 40023 |
| D002 | Mar 19 | Unit Range | CSV: 40048-40073, DPF: 40069-40074 | [ ] Update to 40069-40074 |
| D003 | Mar 20 | End Unit | CSV: 40082, DPF: 40095 (13 unit difference) | [ ] Update to 40095 |
| D004 | Mar 23 | Unit Range | CSV: 40069-40094, DPF: 40096-40104 | [ ] Update to 40096-40104 |
| D005 | Mar 25 | End Unit | CSV: 40211, DPF: 40214 (3 unit difference) | [ ] Update to 40214 |

---

## Corrections Required

### D001: Mar 04 End Unit (MAJOR)
- **Current:** End Unit = 40066
- **DPF shows:** End Unit = 40023
- **Recommendation:** Update to 40023
- [ ] User Decision Required

### D002: Mar 19 Unit Range (MAJOR)
- **Current:** Start Unit = 40048, End Unit = 40073
- **DPF shows:** Start Unit = 40069, End Unit = 40074
- **Analysis:** CSV range overlaps with Mar 15 (40039-40065). DPF range follows Mar 15 properly.
- **Recommendation:** Update to 40069-40074
- [ ] User Decision Required

### D003: Mar 20 End Unit
- **Current:** End Unit = 40082
- **DPF shows:** End Unit = 40095
- **Recommendation:** Update to 40095
- [ ] User Decision Required

### D004: Mar 23 Unit Range (MAJOR)
- **Current:** Start Unit = 40069, End Unit = 40094
- **DPF shows:** Start Unit = 40096, End Unit = 40104 (approximately)
- **Analysis:** CSV range 40069-40094 overlaps with CSV Mar 19 and Mar 20. DPF range follows Mar 20 DPF end (40095).
- **Recommendation:** Update to 40096-40104
- [ ] User Decision Required

### D005: Mar 25 End Unit (MINOR)
- **Current:** End Unit = 40211
- **DPF shows:** End Unit = 40214
- **Recommendation:** Update to 40214
- [ ] User Decision Required

---

## Source Observations

### Unit Sequence Analysis (DPF-based)

| Date | DPF Start | DPF End | DPF Total | Continuity |
|------|-----------|---------|-----------|------------|
| Mar 04 | 40001 | 40023 | 23 | Start |
| Mar 07 | 40031 | 40032 | 2 | Gap (40024-40030) |
| Mar 15 | 40039 | 40065 | ~27 | Gap (40033-40038) |
| Mar 19 | 40069 | 40074 | 5 | Gap (40066-40068) |
| Mar 20 | 40075 | 40095 | 20 | Continuous |
| Mar 23 | 40096 | 40104 | ~14 | Continuous |
| Mar 24 | 40112 | 40124 | 12 | Gap (40105-40111) |
| Mar 25 | 40125 | 40214 | ~46 | Continuous |
| Mar 26 | 40212 | 40214 | ~5 | Overlaps Mar 25 |
| Mar 27 | 40218 | 40250 | 32 | Gap (40215-40217) |

### CSV vs DPF Comparison

| Date | CSV Range | DPF Range | Match |
|------|-----------|-----------|-------|
| Mar 04 | 40001-40066 | 40001-40023 | ❌ End differs by 43 |
| Mar 07 | 40031-40032 | 40031-40032 | ✓ |
| Mar 15 | 40039-40065 | 40039-40065 | ✓ |
| Mar 19 | 40048-40073 | 40069-40074 | ❌ Completely different |
| Mar 20 | 40075-40082 | 40075-40095 | ❌ End differs by 13 |
| Mar 23 | 40069-40094 | 40096-40104 | ❌ Completely different |
| Mar 24 | 40112-40124 | 40112-40124 | ✓ |
| Mar 25 | 40125-40211 | 40125-40214 | ⚠️ End differs by 3 |
| Mar 26 | 40212-40214 | 40212-40214 | ✓ |
| Mar 27 | 40218-40250 | 40218-40250 | ✓ |

### Source Reliability Patterns

- **O1 confirmed:** DPF scans are authoritative for unit numbers. CSV has multiple major errors.
- **Overlapping CSV ranges:** CSV Mar 19, 20, 23 ranges overlap with each other, indicating extraction errors.
- **DPF continuity:** When DPF values are used, unit sequences are mostly continuous with expected gaps for non-survey days.
- **Unit gaps:** Multiple gaps in DPF sequence (e.g., 40024-40030, 40033-40038) may indicate survey areas that were skipped or non-contiguous terrain.

### Implications for Future QA

- Team D CSV data has severe errors requiring full review
- Overlapping unit ranges in CSV are a red flag for extraction errors
- DPF should be considered definitive for unit ranges

---

## Notes

- **Leader consistency:** Georgi Nekhrizov was leader throughout except Mar 27 (no leader recorded)
- **Author consistency:** Barbara Klara Olujic was DPF author for most forms
- **Unit gaps:** The DPF sequence has several gaps which may reflect non-contiguous survey areas or skipped units for terrain/access reasons
- **Mar 26 overlap:** Both CSV and DPF show Mar 26 starting at 40212, which is within the Mar 25 range. This may indicate resurvey or site-focused work.

---

## Summary Statistics

| Metric | Count |
|--------|-------|
| Records in CSV | 10 |
| Records confirmed | 5 |
| Unit errors | 5 (D001-D005) |
| Major errors | 4 (D001-D004) |
| Minor errors | 1 (D005) |
| Corrections required | 5 |

### Issues by Category
- Unit range errors: 5 (all issues are unit-related)
- Missing records: 0
- Walker errors: 0
- Role errors: 0

---

**Document created:** 2025-11-30
**Last updated:** 2025-11-30
