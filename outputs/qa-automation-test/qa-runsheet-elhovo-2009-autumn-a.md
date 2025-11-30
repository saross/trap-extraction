# QA Runsheet: Elhovo 2009 Autumn Team A

**Study Area/Season:** Elhovo 2009 Autumn
**Team:** A
**QA Date:** 2025-11-27
**QA Performed By:** Claude Code (automated test)
**Records:** 22 (in original CSV)
**Date Range:** 2009-10-12 - 2009-11-14

---

## Sources Consulted

| Type | File | Location | Role |
|------|------|----------|------|
| Diary | Diary Team A.doc | Elhovo 2010-12-12/2009/Project Records/Team A/ | PRIMARY (EN, 132 KB) |
| SU Forms | *.pdf | .../Team A/FieldRecords/ | PRIMARY for unit numbers |
| Excel | ELH09 SurveySummary.xls | .../Master Records/ | Unit ranges |

**Note:** No DPF scans exist for ELH 2009 (season-wide gap). SU form PDFs available for unit verification.

---

## Team Composition

### Phase 1: Oct 12-25 (Standard composition)
- **Leader:** Adela Sobotkova
- **Walkers:** Adela, Ilija Iliev, Aneta Kohoutová, Martin Mladenov, Eric (Erik Andersen)
- **Roles:** Adela (PDA), Aneta (Paper), Martin (GPS)

### Phase 2: Oct 26-29 (Eric departed, Tereza substituted)
- **Leader:** Adela Sobotkova
- **Walkers:** Adela, Ilija, Aneta, Martin, **Tereza Dobrovodská** (substitute for Eric)
- **Evidence:** Diary Oct 25 "Eric decided to go on to Istanbul"; Oct 26 "Tereza as a substitute for Eric"

### Phase 3: Nov 2-14 (New team composition)
- **Leader:** Adela Sobotkova
- **Walkers:** Adela, Ilija, Todor Vulchev, Martin Mladenov, Katarina Čuláková
- **Diary:** "Team A ( new incarnation of me, Ilija, Todor, Martin and Katarina)"

---

## Record-by-Record Verification

### 2009-10-12 (Mon) — Units 60000-60038 ✓
- **Diary:** Team A (Ilija, myself, Aneta, Martin and Eric), units 60000-60038
- **CSV:** Start: 60000, End: 60038, Walkers: Ilija | Adela | Aneta | Martin | Eric
- **Status:** CONFIRMED

### 2009-10-13 (Tue) — Units 60039-60086 ✓
- **Diary:** Units 60039-60086, "Martin – GPS, Aneta- recording, me – PDA"
- **CSV:** Start: 60039, End: 60086, Walkers match
- **Status:** CONFIRMED

### 2009-10-15 (Thu) — Units 60087-60126 ✓
- **Diary:** Units 60087-60126, same composition
- **CSV:** Start: 60087, End: 60126
- **Status:** CONFIRMED

### 2009-10-20 (Tue) — Units 60127-60194 ✓
- **Diary:** "Team A ( Adela, Ilija, Martin, Aneta, Eric) heads on", units 60127-60194
- **CSV:** Start: 60127, End: 60194
- **Status:** CONFIRMED

### 2009-10-21 (Wed) — Units 60195-60273 ✓
- **Diary:** Units **60196**-60273 (diary error)
- **SU Form:** Unit 60195 form exists, dated 21 October 2009
- **CSV:** Start: **60195**, End: 60273
- **Status:** CONFIRMED (CSV correct, diary has transcription error)
- **Note:** SU form is PRIMARY for unit numbers; diary summary table error

### 2009-10-22 (Thu) — Units 60274-60376 ✓
- **Diary:** Units 60274-60376
- **CSV:** Start: 60274, End: 60376
- **Status:** CONFIRMED

### 2009-10-23 (Fri) — Units 60377-60456 ✓
- **Diary:** "Team A – Adela, Ilija, Aneta a Eric, Martin is off with Team B", units 60377-60456
- **CSV:** Walkers: Adela | Ilija | Aneta | Eric (4 walkers, Martin absent) ✓
- **Status:** CONFIRMED

### 2009-10-26 (Mon) — Units 60457-60546 ⚠️
- **Diary:** "Team A comprises Adela, Ilija, Aneta, Martin and **Tereza as a substitute for Eric**"
- **Diary context:** Oct 25: "Eric decided to go on to Istanbul and is dropped off at the busstation"
- **CSV:** Walkers: **Ilija | Adela | Aneta | Martin | Eric** (WRONG)
- **Issue D001:** Walker error — CSV has Eric, should be Tereza
- **Status:** DISCREPANCY

### 2009-10-27 (Tue) — Units 60547-60616 ⚠️
- **Diary:** References "Monday setup" (same composition as Oct 26)
- **CSV:** Walkers: **Ilija | Adela | Aneta | Martin | Eric** (WRONG)
- **Issue D002:** Walker error — CSV has Eric, should be Tereza
- **Status:** DISCREPANCY

### 2009-10-28 (Wed) — Units 60617-60696 ⚠️
- **Diary:** Narrative continuity with standard composition (Tereza still substituting)
- **CSV:** Walkers: **Ilija | Adela | Aneta | Martin | Eric** (WRONG)
- **Issue D003:** Walker error — CSV has Eric, should be Tereza
- **Status:** DISCREPANCY

### 2009-10-29 (Thu) — Units 60697-60776 ⚠️
- **Diary:** References "usual setup" (Tereza still substituting)
- **CSV:** Walkers: **Ilija | Adela | Aneta | Martin | Eric** (WRONG)
- **Issue D004:** Walker error — CSV has Eric, should be Tereza
- **Status:** DISCREPANCY

### 2009-10-30 (Fri) — Non-survey day ✓
- **Diary:** "Resting day due to muddy fields" — rain, indoor pottery processing
- **CSV:** No units (correct)
- **Status:** CONFIRMED (non-survey day)

### 2009-10-31 (Sat) — Non-survey day ✓
- **Diary:** "Halloween party preparations" — pottery analysis, photography
- **CSV:** No units (correct)
- **Status:** CONFIRMED (non-survey day)

### 2009-11-02 (Mon) — Units 60777-60861 ✓
- **Diary:** "Team A ( new incarnation of me, Ilija, Todor, Martin and Katarina)"
- **CSV:** Walkers: Adela | Ilija | Todor | Martin | Katerina ✓
- **Status:** CONFIRMED

### 2009-11-03 (Tue) — Units 60862-60964 ✓
- **Diary:** Same composition as 11-02
- **CSV:** Walkers match
- **Status:** CONFIRMED

### 2009-11-04 (Wed) — Non-survey day ✓
- **Diary:** "We wake up to a rain... Resting day"
- **CSV:** No units (correct)
- **Status:** CONFIRMED (non-survey day)

### 2009-11-05 (Thu) — Units 60965-61021 ✓
- **Diary:** "Team A ( Adela, Todor, Martin and Katarina)" — Ilija absent
- **CSV:** Walkers: Adela | Todor | Martin | Katerina (4 walkers) ✓
- **Status:** CONFIRMED

### 2009-11-06 (Fri) — Units 61022-61079 ✓
- **Diary:** "Team A ( Adela, Ilija, Marto, Todor and Katka )"
- **CSV:** Walkers: Adela | Ilija | Martin | Todor | Katerina ✓
- **Status:** CONFIRMED

### 2009-11-07 (Sat) — Units 61080-61185 ✓
- **Diary:** "Team A assembles... usual setup except for missing Ilja"
- **CSV:** Walkers: Adela | Martin | Todor | Katerina (4 walkers) ✓
- **Status:** CONFIRMED

### 2009-11-09 (Mon) — Units 61186-61249 ⚠️
- **Diary:** Entry exists (Nov 9 documented)
- **CSV:** Author field is **empty** (other records have "Adela Sobotkova")
- **Issue D005:** Missing Author — CSV has no Diary_Author value
- **Status:** DISCREPANCY (minor)

### 2009-11-10 (Tue) — Units 61250-61339 ✓
- **Diary:** "Team A in usual setup ( Marto, Todor, Ilija, Katya and me)"
- **CSV:** Walkers match
- **Status:** CONFIRMED

### 2009-11-14 (Sat) — Units 61340-61344 ✓
- **Diary:** "Team A heads out (Adela, Katya and Marto) to do total pick ups"
- **CSV:** Walkers: Adela | Katya | Marto (3 walkers for total collections) ✓
- **Status:** CONFIRMED

---

## Issues Summary

| ID | Date | Field | Issue | Action |
|----|------|-------|-------|--------|
| D001 | 2009-10-26 | Walkers | Eric→Tereza substitution not reflected | Correct walker ×2 fields |
| D002 | 2009-10-27 | Walkers | Eric→Tereza substitution not reflected | Correct walker ×2 fields |
| D003 | 2009-10-28 | Walkers | Eric→Tereza substitution not reflected | Correct walker ×2 fields |
| D004 | 2009-10-29 | Walkers | Eric→Tereza substitution not reflected | Correct walker ×2 fields |
| D005 | 2009-11-09 | Author | Missing Diary_Author | Add "Adela Sobotkova" |

---

## Corrections Required

### D001-D004: Correct Oct 26-29 Walker Lists (MAJOR)

**Records:** 2009-10-26, 2009-10-27, 2009-10-28, 2009-10-29
**Fields:** Walkers_Original, Walkers_Standardised

**Source evidence:**
- Oct 25 diary: "Eric decided to go on to Istanbul and is dropped off at the busstation"
- Oct 26 diary: "Team A comprises Adela, Ilija, Aneta, Martin and **Tereza as a substitute for Eric**"

**Disambiguation:**
- H2 (one team per day) applied: Tereza Dobrovodská was on Team C until Oct 22
- Team C diary Oct 23: "Today we were walking without Tereza because she was sick"
- Tereza Dobrovodská then substituted for Eric on Team A starting Oct 26

**Corrections:**

| Date | Walkers_Original | Walkers_Standardised |
|------|------------------|----------------------|
| 2009-10-26 | Eric → Tereza | Erik Andersen → Tereza Dobrovodská |
| 2009-10-27 | Eric → Tereza | Erik Andersen → Tereza Dobrovodská |
| 2009-10-28 | Eric → Tereza | Erik Andersen → Tereza Dobrovodská |
| 2009-10-29 | Eric → Tereza | Erik Andersen → Tereza Dobrovodská |

**Reasoning:** Diary explicitly states Eric departed Oct 25 and Tereza substituted from Oct 26. CSV incorrectly shows Eric for these 4 days.

**User Decision:**
- [ ] Approve
- [ ] Modify: _______________

**Status:** Pending

---

### D005: Add Nov 9 Diary_Author (Minor)

**Record:** 2009-11-09, Team A
**Field:** Author (Diary_Author)
**Current:** (empty)
**Corrected:** Adela Sobotkova
**Source evidence:** Diary Team A.doc authored by Adela; all other Team A November records have this value
**Reasoning:** Extraction gap — field was not populated during original extraction

**User Decision:**
- [ ] Approve
- [ ] Modify: _______________

**Status:** Pending

---

## Unit Continuity Check

| Date | End Unit | Next Date | Start Unit | Gap | Status |
|------|----------|-----------|------------|-----|--------|
| Oct 12 | 60038 | Oct 13 | 60039 | +1 | ✓ |
| Oct 13 | 60086 | Oct 15 | 60087 | +1 | ✓ |
| Oct 15 | 60126 | Oct 20 | 60127 | +1 | ✓ |
| Oct 20 | 60194 | Oct 21 | 60195 | +1 | ✓ |
| Oct 21 | 60273 | Oct 22 | 60274 | +1 | ✓ |
| Oct 22 | 60376 | Oct 23 | 60377 | +1 | ✓ |
| Oct 23 | 60456 | Oct 26 | 60457 | +1 | ✓ |
| Oct 26 | 60546 | Oct 27 | 60547 | +1 | ✓ |
| Oct 27 | 60616 | Oct 28 | 60617 | +1 | ✓ |
| Oct 28 | 60696 | Oct 29 | 60697 | +1 | ✓ |
| Oct 29 | 60776 | Nov 2 | 60777 | +1 | ✓ |
| Nov 2 | 60861 | Nov 3 | 60862 | +1 | ✓ |
| Nov 3 | 60964 | Nov 5 | 60965 | +1 | ✓ |
| Nov 5 | 61021 | Nov 6 | 61022 | +1 | ✓ |
| Nov 6 | 61079 | Nov 7 | 61080 | +1 | ✓ |
| Nov 7 | 61185 | Nov 9 | 61186 | +1 | ✓ |
| Nov 9 | 61249 | Nov 10 | 61250 | +1 | ✓ |
| Nov 10 | 61339 | Nov 14 | 61340 | +1 | ✓ |

**Note:** Perfect unit continuity. Diary error on Oct 21 (60196 vs 60195) was a transcription error — CSV and SU forms correct.

---

## Summary Statistics

| Metric | Count |
|--------|-------|
| Records checked | 22 |
| Records confirmed | 17 |
| Issues found | 5 |
| Corrections required | 9 field updates (8 walker + 1 author) |
| MAJOR issues | 4 (walker substitution) |
| Minor issues | 1 (missing author) |

### Issues by Category
- Walker errors: 4 (D001-D004)
- Missing fields: 1 (D005)
- Unit errors: 0
- Role errors: 0

---

## Source Observations

### Source Divergences

| Date | Field | SU Form Value | Diary Value | CSV Value | Resolution | Note |
|------|-------|---------------|-------------|-----------|------------|------|
| Oct 21 | Start_Unit | 60195 | 60196 | 60195 | SU form correct | Diary summary table transcription error |

### Source Reliability Patterns

- **O1 confirmed:** SU forms more reliable than diary for unit numbers (1 case)
  - Oct 21: SU form 60195 correct, diary summary showed 60196
- **Pattern:** Diary summary tables may contain transcription errors; individual SU forms are more reliable

### Implications for Future QA

- SU forms should be PRIMARY for unit numbers when DPF scans unavailable (2009 season)
- Diary summary tables are secondary to individual day SU forms
- Unit continuity check (C1) validates: Oct 20 ends 60194 → Oct 21 starts 60195

---

## Notes

### Observation: Walker Substitution Detection
The Oct 26-29 Eric→Tereza substitution was detectable through:
1. Oct 25 diary entry stating Eric departed for Istanbul
2. Oct 26 diary explicitly naming "Tereza as a substitute for Eric"
3. Cross-reference with Team C diary (Tereza sick Oct 23, available for transfer)

### Observation: Diary Transcription Error
Oct 21 diary summary table shows Start Unit 60196, but SU form confirms 60195 is correct. This confirms source priority rules: SU forms > diary for unit numbers.

### Observation: Non-Survey Days
Oct 30, 31, Nov 4 correctly recorded as non-survey days with documented reasons (rain, Halloween, rain).

---

**Document created:** 2025-11-27
**Last updated:** 2025-11-27
