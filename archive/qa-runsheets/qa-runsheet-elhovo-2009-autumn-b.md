# QA Runsheet: Elhovo 2009 Autumn — Team B

**Date:** 26 November 2025
**Status:** COMPLETE — Corrections applied (26 Nov 2025)
**Records verified:** 20
**Scope:** Team B, October-November 2009

---

## Source Documents Consulted

| Type | File | Location | Notes |
|------|------|----------|-------|
| Primary Diary | DiaryTeamB.doc | `Elhovo 2010-12-12/2009/Project Records/Team B/` | EN, detailed daily entries with walkers and unit numbers |
| Secondary Diary | TeamB_Dnevnik (Ross).doc | `Elhovo 2010-12-12/2009/Project Records/Team B/` | BG translation, confirms EN diary data |
| DPF Scans | **NONE** | — | No daily progress form scans exist for ELH 2009 |
| Individual Unit Forms | 70122.pdf, 70239.pdf, etc. | `Team B/FieldRecords/` | Unit-level forms only, not daily summaries |

**Note:** This season has **diary-only verification** — no DPF scans available for cross-reference. Confidence is based on EN/BG diary agreement.

---

## Source Coverage Matrix

| Date | CSV Record | EN Diary | BG Diary | DPF Scan | Status |
|------|------------|----------|----------|----------|--------|
| 2009-10-12 | ✓ | ✓ | ✓ | ✗ | CONFIRMED |
| 2009-10-13 | ✓ | ✓ | ✓ | ✗ | CONFIRMED |
| 2009-10-15 | ✓ | ✓ | ✓ | ✗ | CONFIRMED |
| 2009-10-20 | ✓ | ✓ | ✓ | ✗ | CONFIRMED |
| 2009-10-21 | ✓ | ✓ | ✓ | ✗ | CONFIRMED |
| 2009-10-22 | ✓ | ✓ | ✓ | ✗ | CONFIRMED |
| 2009-10-23 | ✓ | ✓ | ✓ | ✗ | CONFIRMED |
| 2009-10-26 | ✓ | ✓ | ✓ | ✗ | CONFIRMED |
| 2009-10-27 | ✓ | ✓ | ✓ | ✗ | CONFIRMED |
| 2009-10-28 | ✓ | ✓ | ✓ | ✗ | CONFIRMED |
| 2009-10-29 | ✓ | ✓ | ✓ | ✗ | CONFIRMED |
| 2009-11-02 | ✓ (units missing) | ✓ | ✓ | ✗ | **DISCREPANCY** |
| 2009-11-03 | ✓ (units missing) | ✓ | ✓ | ✗ | **DISCREPANCY** |
| 2009-11-05 | ✓ (units missing) | ✓ | ✓ | ✗ | **DISCREPANCY** |
| 2009-11-06 | ✓ | ✓ | ✓ | ✗ | CONFIRMED |
| 2009-11-07 | ✓ | ✓ | ✓ | ✗ | CONFIRMED |
| 2009-11-09 | ✓ | ✓ | ✓ | ✗ | CONFIRMED (minor: UNMAPPED Lizzy) |
| 2009-11-10 | ✓ | ✓ | ✓ | ✗ | CONFIRMED (minor: UNMAPPED Lizzy) |
| 2009-11-12 | ✓ | ✓ | ✓ | ✗ | CONFIRMED (minor: UNMAPPED Lizzy) |
| 2009-11-13 | ✓ | ✓ | ✓ | ✗ | CONFIRMED (minor: UNMAPPED Lizzy) |

---

## QA Issues

### QA Issue #1: 2009-11-02 Team B — Missing Unit Numbers (MAJOR)

**Problem:** CSV has empty Start Unit and End Unit values, but diary has complete data.

**Current CSV values:**

- Start Unit: (empty)
- End Unit: (empty)
- QA_Notes: "MISSING: Survey units | No role data available | No autumn survey season: No autumn 2009 survey season - diaries end in March/April"

**Source evidence:**

- EN Diary (DiaryTeamB.doc, Monday 2 November):
  > "First unit: 70926 / Last unit: 70962 / Total units: 36"
- BG Diary (TeamB_Dnevnik Ross.doc, 2 ноември):
  > "Първи полигон: 70926 / Последен полигон: 70962 / Общ брой полигони: 36"

**Finding:** DISCREPANCY — Both diaries agree; CSV incorrectly missing data

**Recommended values:**

- Start Unit: 70926
- End Unit: 70962

**Reasoning:** Both EN and BG diaries contain the same unit numbers. The QA_Notes statement "No autumn 2009 survey season - diaries end in March/April" is **factually incorrect** — the diaries clearly contain autumn 2009 entries through 13 November.

**Unit continuity check:** 70926 follows Oct 29 end unit (70925) + 1 = ✓ Perfect continuity

---

**User Decision:** [X] Accept / [ ] Modify: _______________

---

### QA Issue #2: 2009-11-03 Team B — Missing Unit Numbers (MAJOR)

**Problem:** CSV has empty Start Unit and End Unit values, but diary has complete data.

**Current CSV values:**

- Start Unit: (empty)
- End Unit: (empty)
- QA_Notes: "MISSING: Survey units | No role data available | No autumn survey season: No autumn 2009 survey season - diaries end in March/April"

**Source evidence:**

- EN Diary (DiaryTeamB.doc, Tuesday 3 November):
  > "First unit: 70963 / Last unit: 71062 / Total units: 100"
- BG Diary (TeamB_Dnevnik Ross.doc, 3 ноември):
  > "Първи полигон: 70963 / Последен полигон: 71062 / Общ брой полигони: 100"

**Finding:** DISCREPANCY — Both diaries agree; CSV incorrectly missing data

**Recommended values:**

- Start Unit: 70963
- End Unit: 71062

**Reasoning:** Both EN and BG diaries contain the same unit numbers. Perfect continuity with previous day.

**Unit continuity check:** 70963 follows Nov 2 end unit (70962) + 1 = ✓ Perfect continuity

---

**User Decision:** [X] Accept / [ ] Modify: _______________

---

### QA Issue #3: 2009-11-05 Team B — Missing Unit Numbers (MAJOR)

**Problem:** CSV has empty Start Unit and End Unit values, but diary has complete data.

**Current CSV values:**

- Start Unit: (empty)
- End Unit: (empty)
- QA_Notes: "MISSING: Survey units | No role data available | No autumn survey season: No autumn 2009 survey season - diaries end in March/April"

**Source evidence:**

- EN Diary (DiaryTeamB.doc, Thursday 5 November):
  > "First unit: 71063 / Last unit: 71142 / Total units: 79"
- BG Diary (TeamB_Dnevnik Ross.doc, 5 ноември):
  > "Първи полигон: 71063 / Последен полигон: 71142 / Общ брой полигони: 79"

**Finding:** DISCREPANCY — Both diaries agree; CSV incorrectly missing data

**Recommended values:**

- Start Unit: 71063
- End Unit: 71142

**Reasoning:** Both EN and BG diaries contain the same unit numbers. Perfect continuity with previous day.

**Unit continuity check:** 71063 follows Nov 3 end unit (71062) + 1 = ✓ Perfect continuity

---

**User Decision:** [X] Accept / [ ] Modify: _______________

---

### QA Issue #4: Erroneous QA_Notes — Incorrect Statement About Diary Coverage

**Problem:** Multiple records contain the erroneous note "No autumn 2009 survey season - diaries end in March/April" — this is factually incorrect.

**Affected records:** 2009-11-02, 2009-11-03, 2009-11-05 (and possibly others)

**Evidence:** The DiaryTeamB.doc covers the period 10 October 2009 through 21 November 2009, with detailed daily entries for all survey days. The BG diary (TeamB_Dnevnik Ross.doc) confirms the same coverage.

**Recommended action:** Remove or correct this erroneous note from QA_Notes field.

---

**User Decision:** [X] Accept / [ ] Modify: _______________

---

### QA Issue #5: UNMAPPED: Lizzy — Unresolved Walker Name (Minor)

**Problem:** "Lizzy" appears in 4 records but remains unmapped to a canonical name.

**Affected records:** 2009-11-09, 2009-11-10, 2009-11-12, 2009-11-13

**Current status in name-mapping.csv:**

```text
Lizzy,Lizzy,,uncertain,B,2009-autumn,2009-11-12 | 2009-11-13,...,"Czech volunteer, full name being researched."
```

**Source evidence:**

- EN Diary: "Lizzy" appears as a walker
- BG Diary: "Лиси" (transliteration of Lizzy)
- No full name given in either diary

**Finding:** SOURCE GAP — Full name not recorded in available sources

**Recommended action:** Flag for future research; retain "UNMAPPED: Lizzy" until resolved. Check personnel lists or other administrative records.

---

**User Decision:** [ ] Accept / [X] Flag for future research: Already in follow-up-actions, nothing else needed, this is a known issue

---

## Per-Record Verification Results

### October 2009 Records (11 records) — All CONFIRMED

| Date | Start Unit | End Unit | Walkers (Count) | CSV Match | Diary Match |
|------|------------|----------|-----------------|-----------|-------------|
| 10-12 | 70000 | 70043 | Scott, Vera, Shawn, Yabor, Stanislav (5) | ✓ | ✓ |
| 10-13 | 70044 | 70122 | Scott, Vera, Shawn, Yabor, Stanislav (5) | ✓ | ✓ |
| 10-15 | 70123 | 70163 | Scott, Vera, Shawn, Yabor, Stanislav, Stefan (6) | ✓ | ✓ |
| 10-20 | 70164 | 70240 | Scott, Vera, Shawn, Yabor, Stanislav, Stefan (6) | ✓ | ✓ |
| 10-21 | 70241 | 70342 | Scott, Vera, Shawn, Yabor, Stanislav, Stefan (6) | ✓ | ✓ |
| 10-22 | 70343 | 70477 | Scott, Vera, Shawn, Yabor, Stanislav, Stefan (6) | ✓ | ✓ |
| 10-23 | 70478 | 70571 | Scott, Vera, Shawn, Martin, Stanislav (5) | ✓ | ✓ |
| 10-26 | 70572 | 70655 | Scott, Vera, Shawn, Yavor, Stanislav, Stefan (6) | ✓ | ✓ |
| 10-27 | 70656 | 70747 | Scott, Vera, Shawn, Yabor, Stanislav, Stefan (6) | ✓ | ✓ |
| 10-28 | 70748 | 70839 | Scott, Vera, Shawn, Yabor, Stanislav (5) | ✓ | ✓ |
| 10-29 | 70840 | 70925 | Scott, Vera, Shawn, Stanislav (4) | ✓ | ✓ |

### November 2009 Records (9 records) — 3 DISCREPANCIES, 6 CONFIRMED

| Date | Start Unit | End Unit | Walkers (Count) | CSV Match | Diary Match | Issue |
|------|------------|----------|-----------------|-----------|-------------|-------|
| 11-02 | (empty) | (empty) | Scott, Dasha, Shawn, Stanislav (4) | ✗ Units | ✓ | **#1** |
| 11-03 | (empty) | (empty) | Scott, Dasha, Shawn, Stanislav, Zhoro, Yabor (6) | ✗ Units | ✓ | **#2** |
| 11-05 | (empty) | (empty) | Scott, Dasha, Shawn, Stanislav (4) | ✗ Units | ✓ | **#3** |
| 11-06 | 71143 | 71201 | Scott, Dasha, Shawn, Stanislav (4) | ✓ | ✓ | — |
| 11-07 | 71202 | 71257 | Scott, Dasha, Shawn, Stanislav (4) | ✓ | ✓ | — |
| 11-09 | 71258 | 71313 | Shawn, Zhoro, Lizzy, Simon (4) | ✓ | ✓ | #5 (Lizzy) |
| 11-10 | 71314 | 71370 | Shawn, Yavor, Dasha, Lizzy, Simon (5) | ✓ | ✓ | #5 (Lizzy) |
| 11-12 | 71371 | 71405 | Shawn, Martin, Todor, Katerina, Lizzy (5) | ✓ | ✓ | #5 (Lizzy) |
| 11-13 | 71406 | 71463 | Shawn, Martin, Todor, Dasha, Lizzy (5) | ✓ | ✓ | #5 (Lizzy) |

---

## Unit Continuity Check

| Date | End Unit | Next Date | Start Unit | Gap | Status |
|------|----------|-----------|------------|-----|--------|
| 10-12 | 70043 | 10-13 | 70044 | +1 | ✓ |
| 10-13 | 70122 | 10-15 | 70123 | +1 | ✓ |
| 10-15 | 70163 | 10-20 | 70164 | +1 | ✓ |
| 10-20 | 70240 | 10-21 | 70241 | +1 | ✓ |
| 10-21 | 70342 | 10-22 | 70343 | +1 | ✓ |
| 10-22 | 70477 | 10-23 | 70478 | +1 | ✓ |
| 10-23 | 70571 | 10-26 | 70572 | +1 | ✓ |
| 10-26 | 70655 | 10-27 | 70656 | +1 | ✓ |
| 10-27 | 70747 | 10-28 | 70748 | +1 | ✓ |
| 10-28 | 70839 | 10-29 | 70840 | +1 | ✓ |
| 10-29 | 70925 | 11-02 | 70926* | +1 | ✓ |
| 11-02 | 70962* | 11-03 | 70963* | +1 | ✓ |
| 11-03 | 71062* | 11-05 | 71063* | +1 | ✓ |
| 11-05 | 71142* | 11-06 | 71143 | +1 | ✓ |
| 11-06 | 71201 | 11-07 | 71202 | +1 | ✓ |
| 11-07 | 71257 | 11-09 | 71258 | +1 | ✓ |
| 11-09 | 71313 | 11-10 | 71314 | +1 | ✓ |
| 11-10 | 71370 | 11-12 | 71371 | +1 | ✓ |
| 11-12 | 71405 | 11-13 | 71406 | +1 | ✓ |

*Values from diary (currently missing in CSV)

**Result:** Perfect unit continuity across all 20 records. The diary-provided unit numbers for Nov 2, 3, 5 fit perfectly into the sequence.

---

## Rule Check Results

### R1: Roles ⊆ Walkers

All role holders (Paper_Recorder, GPS_Operator, PDA_Operator) appear in the walker lists where assigned. ✓

### R2: Leader ∈ Walkers

Leader (Shawn Ross) appears in walker list for all 20 records. ✓

---

## Summary

| Metric | Count |
|--------|-------|
| Records verified | 20 |
| MAJOR issues (unit numbers) | 3 |
| Minor issues (unmapped names) | 1 (affects 4 records) |
| Metadata issues (erroneous notes) | 1 |
| Corrections required | 3 (unit number additions) |
| Source gaps (no DPF scan) | 20 (all records) |

### Issues by Category

| Category | Count | Records |
|----------|-------|---------|
| Missing unit numbers | 3 | 2009-11-02, 2009-11-03, 2009-11-05 |
| Erroneous QA_Notes | 3 | Same as above |
| Unmapped walker name | 4 | 2009-11-09, 2009-11-10, 2009-11-12, 2009-11-13 |

### Key Finding

The original extraction appears to have incorrectly assumed the Team B diary did not cover autumn 2009, resulting in unit numbers being omitted for 3 records. The diary actually contains complete coverage through mid-November, and all data can be recovered.

---

## Recommended Corrections

1. **Add unit numbers** to records 2009-11-02, 2009-11-03, 2009-11-05
2. **Remove erroneous QA_Notes** statement about diary coverage
3. **Flag Lizzy** for future name research (already in name-mapping.csv)

---

## Observations for Methodology

### New Observation: O4 — Extraction Errors from Incorrect Assumptions

**Observation:** The original extraction contained systematic errors where the extractor incorrectly assumed source documents did not exist, resulting in missing data that was actually available.

**Evidence:** Records for Nov 2, 3, 5 were flagged as "No autumn survey season - diaries end in March/April" despite the diary clearly containing autumn 2009 entries.

**Implication:** QA should always verify source availability claims by checking the actual documents, not just the extraction notes.

---

## Document History

- **Created:** 26 November 2025
- **Verified by:** Claude Code (QA pilot extension)
- **Source verification:** Diary-only (no DPF scans available)
