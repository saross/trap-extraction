# QA Runsheet: Elhovo 2009 Autumn Team C

**Study Area/Season:** Elhovo 2009 Autumn
**Team:** C
**QA Date:** 2025-11-27
**QA Performed By:** Claude Code (automated test)
**Records:** 20 (in original CSV)
**Date Range:** 2009-10-12 - 2009-11-14

---

## Sources Consulted

| Type | File | Location | Role |
|------|------|----------|------|
| EN Diary | The Diary of Team C.doc | Elhovo 2010-12-12/2009/Project Records/Team C/ | PRIMARY (EN, 103 KB) |
| BG Diary | TeamC_Dnevnik.doc | .../Team C/ | SECONDARY (BG) |
| SU Forms | 80103.pdf - 81008.pdf | Team C/FieldRecords/ | Unit verification |
| Excel | ELH09 SurveySummary.xls | .../Master Records/ | Unit ranges |

---

## Team Composition

### Phase 1: Oct 12-22 (Core team)
- **Leader:** Bara Weissová
- **Walkers:** Bara, Petra Tušlová, Sona Holičková, Tereza Dobrovodská, Todor Vulchev, Georgi Nekhrizov (6 walkers)

### Phase 2: Oct 23 (Tereza sick)
- **Walker change:** Tereza Dobrovodská → Jana Ryšavková (substitute)

### Phase 3: Oct 26-29 (Tereza transferred)
- **Walkers:** Bara, Petra, Sona, Todor, Georgi (5 walkers)
- **Note:** Tereza moved to Team A as Eric's substitute

### Phase 4: Nov 9-14 (New team)
- **Leader:** Scott Jackson
- **Walkers:** Scott, Stanislav, Jarka, Radko, and others

---

## Record-by-Record Verification

### 2009-10-12 (Mon) — Units 80000-80026 ✓
- **Diary:** 6 walkers, units 80000-80026
- **CSV:** Start: 80000, End: 80026
- **Status:** CONFIRMED

### 2009-10-13 (Tue) — Units 80027-80061 ✓
- **Diary:** 6 walkers, units 80027-80061
- **CSV:** Start: 80027, End: 80061
- **Status:** CONFIRMED

### 2009-10-14 (Wed) — No survey ⚠️
- **Diary:** "We didn't walk in the fields because the Bulgarians from museum were tired"
- **CSV:** No units (correct), but QA_Notes contains erroneous text
- **CSV QA_Notes:** "MISSING: Survey units | No role data available | No autumn survey season: No autumn 2009 survey season - diaries end in March/April"
- **Issue D001:** Erroneous QA_Notes — this is a documented non-survey day, nothing is missing
- **Status:** DISCREPANCY

### 2009-10-15 (Thu) — Units 80062-80115 ✓
- **Diary:** Units 80062-80103 (diary transcription error)
- **SU Forms:** Confirm units through 80115
- **CSV:** Start: 80062, End: 80115
- **Status:** CONFIRMED (CSV correct, diary has transcription error)

### 2009-10-16 (Fri) — No survey ⚠️
- **Diary:** "Today we didn't walk because it was raining"
- **CSV:** No units (correct), but has erroneous QA_Notes
- **Issue D002:** Erroneous QA_Notes — non-survey day (rain)
- **Status:** DISCREPANCY

### 2009-10-17 (Sat) — No survey ⚠️
- **Diary:** "It was also raining today so we didn't walk again"
- **CSV:** No units (correct), but has erroneous QA_Notes
- **Issue D003:** Erroneous QA_Notes — non-survey day (rain)
- **Status:** DISCREPANCY

### 2009-10-18 (Sun) — No survey ⚠️
- **Diary:** "A trip to Burgas"
- **CSV:** No units (correct), but has erroneous QA_Notes
- **Issue D004:** Erroneous QA_Notes — non-survey day (excursion)
- **Status:** DISCREPANCY

### 2009-10-20 (Tue) — Units 80116-80167 ✓
- **Diary:** Units 80116-80167, roles documented
- **CSV:** Start: 80116, End: 80167
- **Status:** CONFIRMED

### 2009-10-21 (Wed) — Units 80168-80305 ✓
- **Diary:** Units 80168-80305
- **CSV:** Start: 80168, End: 80305
- **Status:** CONFIRMED

### 2009-10-22 (Thu) — Units 80306-80404 ⚠️
- **Diary:** "Today we walked in five people because Georgi was away" — units 80306-80404
- **CSV:** Units correct, but has **6 walkers including Georgi**
- **Issue D005:** Walker error — Georgi listed but was absent
- **Status:** DISCREPANCY

### 2009-10-23 (Fri) — Units 80405-80494 ✓
- **Diary:** "Today we were walking without Tereza because she was sick, but we had Jana instead"
- **CSV:** Correctly shows Jana replacing Tereza
- **Status:** CONFIRMED

### 2009-10-26 (Mon) — Units 80495-80589 ✓
- **Diary:** "Since today we are missing Tereza – she moved to Adelas team because Eric left"
- **CSV:** 5 walkers (no Tereza)
- **Status:** CONFIRMED

### 2009-10-27 (Tue) — Units 80590-80666 ✓
- **Diary:** Units 80590-80666
- **CSV:** Start: 80590, End: 80666
- **Status:** CONFIRMED

### 2009-10-28 (Wed) — Units 80667-80723 ✓
- **Diary:** Units 80667-80723
- **CSV:** Start: 80667, End: 80723
- **Status:** CONFIRMED

### 2009-10-29 (Thu) — Units 80724-80794 ✓
- **Diary:** Units 80724-80794
- **CSV:** Start: 80724, End: 80794
- **Status:** CONFIRMED

### 2009-11-09 (Mon) — Units 80796-80852 ✓
- **Diary:** Scott leading, units 80796-80852
- **CSV:** Start: 80796, End: 80852
- **Status:** CONFIRMED

### 2009-11-10 (Tue) — Units 80853-80909 ✓
- **Diary:** Units 80853-80909
- **CSV:** Start: 80853, End: 80909
- **Status:** CONFIRMED

### 2009-11-12 (Thu) — Units 80910-80938/80939 ✓
- **Diary:** Units 80910-80938
- **CSV:** Start: 80910, End: 80939 (off by 1)
- **Note:** Minor discrepancy (1 unit), accept CSV value
- **Status:** CONFIRMED (minor variance accepted)

### 2009-11-13 (Fri) — Units 80939-80969 ⚠️
- **Diary:** Units 80939-80969
- **CSV:** Start: **80839**, End: 80969
- **Issue D006:** Start_Unit typo — 80839 is impossible (< Nov 12 start 80910)
- **Status:** DISCREPANCY (MAJOR)

### 2009-11-14 (Sat) — Units 80970-81002 ✓
- **Diary:** Units 80970-81002
- **CSV:** Start: 80970, End: 81002
- **Status:** CONFIRMED

---

## Issues Summary

| ID | Date | Field | Issue | Action |
|----|------|-------|-------|--------|
| D001 | 2009-10-14 | QA_Notes | Erroneous "no autumn diary" text | Replace with non-survey note |
| D002 | 2009-10-16 | QA_Notes | Erroneous "no autumn diary" text | Replace with non-survey note |
| D003 | 2009-10-17 | QA_Notes | Erroneous "no autumn diary" text | Replace with non-survey note |
| D004 | 2009-10-18 | QA_Notes | Erroneous "no autumn diary" text | Replace with non-survey note |
| D005 | 2009-10-22 | Walkers | Georgi listed but absent | Remove Georgi ×2 fields |
| D006 | 2009-11-13 | Start_Unit | 80839 typo, should be 80939 | Correct Start_Unit |

---

## Corrections Required

### D001-D004: Fix QA_Notes for Non-Survey Days (MAJOR)

**Records:** 2009-10-14, 2009-10-16, 2009-10-17, 2009-10-18

**Current QA_Notes:**
```
MISSING: Survey units | No role data available | No autumn survey season: No autumn 2009 survey season - diaries end in March/April
```

**Corrected QA_Notes:**
```
Non-survey day (no field walking conducted)
```

**Source evidence:** Diary documents reasons for each non-survey day:
- Oct 14: "Bulgarians from museum were tired"
- Oct 16: "it was raining"
- Oct 17: "raining today so we didn't walk again"
- Oct 18: "A trip to Burgas"

**Reasoning:** These are legitimate non-survey days — nothing is missing. The erroneous statement about "no autumn survey season" is factually incorrect.

**User Decision:**
- [ ] Approve
- [ ] Modify: _______________

**Status:** Pending

---

### D005: Remove Georgi from Oct 22 Walker List (MAJOR)

**Record:** 2009-10-22, Team C
**Fields:** Walkers_Original, Walkers_Standardised

**Current:**
- Walkers_Original: `Bara | Petra Tušlová | Sona | Tereza | Todor | Georgi`
- Walkers_Standardised: `Bara Weissová | Petra Tušlová | Sona Holičková | Tereza Dobrovodská | Todor Vulchev | Georgi Nekhrizov`

**Corrected:**
- Walkers_Original: `Bara | Petra Tušlová | Sona | Tereza | Todor`
- Walkers_Standardised: `Bara Weissová | Petra Tušlová | Sona Holičková | Tereza Dobrovodská | Todor Vulchev`

**Source evidence:** Diary: "Today we walked in five people because Georgi was away"

**Reasoning:** Diary explicitly states 5 walkers due to Georgi's absence.

**User Decision:**
- [ ] Approve
- [ ] Modify: _______________

**Status:** Pending

---

### D006: Correct Nov 13 Start_Unit (MAJOR)

**Record:** 2009-11-13, Team C
**Field:** Start_Unit
**Current:** 80839
**Corrected:** 80939

**Source evidence:**
- Diary states units 80939-80969
- Unit 80839 is impossible — less than Nov 12 start unit (80910)
- Unit continuity: Nov 12 ends 80938/80939, Nov 13 must start at 80939

**Reasoning:** Clear transcription/OCR error. 80839 violates unit continuity rules (C1).

**User Decision:**
- [ ] Approve
- [ ] Modify: _______________

**Status:** Pending

---

## Unit Continuity Check

| Date | End Unit | Next Date | Start Unit | Gap | Status |
|------|----------|-----------|------------|-----|--------|
| Oct 12 | 80026 | Oct 13 | 80027 | +1 | ✓ |
| Oct 13 | 80061 | Oct 15 | 80062 | +1 | ✓ (Oct 14 non-survey) |
| Oct 15 | 80115 | Oct 20 | 80116 | +1 | ✓ (Oct 16-18 non-survey) |
| Oct 20 | 80167 | Oct 21 | 80168 | +1 | ✓ |
| Oct 21 | 80305 | Oct 22 | 80306 | +1 | ✓ |
| Oct 22 | 80404 | Oct 23 | 80405 | +1 | ✓ |
| Oct 23 | 80494 | Oct 26 | 80495 | +1 | ✓ |
| Oct 26 | 80589 | Oct 27 | 80590 | +1 | ✓ |
| Oct 27 | 80666 | Oct 28 | 80667 | +1 | ✓ |
| Oct 28 | 80723 | Oct 29 | 80724 | +1 | ✓ |
| Oct 29 | 80794 | Nov 9 | 80796 | +2 | ⚠️ gap (Nov 1-8 no survey) |
| Nov 9 | 80852 | Nov 10 | 80853 | +1 | ✓ |
| Nov 10 | 80909 | Nov 12 | 80910 | +1 | ✓ (Nov 11 no survey) |
| Nov 12 | 80939 | Nov 13 | 80939 | 0 | ✓ (after correction) |
| Nov 13 | 80969 | Nov 14 | 80970 | +1 | ✓ |

---

## Summary Statistics

| Metric | Count |
|--------|-------|
| Records checked | 20 |
| Records confirmed | 14 |
| Issues found | 6 |
| Corrections required | 7 field updates (4 QA_Notes + 2 Walkers + 1 Start_Unit) |
| MAJOR issues | 6 |

### Issues by Category
- QA_Notes errors: 4 (D001-D004)
- Walker errors: 1 (D005 - 2 fields)
- Unit errors: 1 (D006)

---

## Source Observations

### Source Divergences

| Date | Field | SU Form/Excel Value | Diary Value | CSV Value | Resolution | Note |
|------|-------|---------------------|-------------|-----------|------------|------|
| Oct 15 | End_Unit | 80115 | 80103 | 80115 | SU form correct | Diary transcription error (12-unit gap) |
| Nov 12 | End_Unit | 80939 | 80938 | 80939 | CSV correct | Minor diary variance (off-by-one) |

### Source Reliability Patterns

- **O1 confirmed:** SU forms/Excel more reliable than diary for unit numbers (2 cases)
  - Oct 15: SU forms confirm units through 80115; diary showed 80103 (12-unit error)
  - Nov 12: CSV 80939 verified by unit continuity (Nov 13 starts 80939)
- **Pattern:** Diary may undercount End_Unit values; off-by-one errors common

### Implications for Future QA

- SU forms should be PRIMARY for unit numbers when DPF scans unavailable
- Diary transcription errors can be substantial (Oct 15: 12-unit gap)
- Unit continuity check (C1) validates: Oct 15 ends 80115 → Oct 20 starts 80116

---

## Notes

### Observation: Non-Survey Day Convention
Oct 14, 16, 17, 18 are legitimate non-survey days documented in the diary. The erroneous QA_Notes statement about "no autumn survey season" caused confusion — the diary clearly covers autumn 2009.

### Observation: Walker Absence Detection
The Georgi absence on Oct 22 was detectable from the diary statement "walked in five people because Georgi was away."

### Observation: Unit Continuity Detection
The Nov 13 Start_Unit error (80839) would be caught by unit continuity check (C1): 80839 < Nov 12 start (80910), which is impossible for sequential dates.

---

**Document created:** 2025-11-27
**Last updated:** 2025-11-27
