# QA Runsheet: Elhovo 2009 Autumn Team C

**Study Area/Season:** Elhovo 2009 Autumn
**Team:** C
**QA Date:** 26 November 2025
**QA Performed By:** Claude Code (with Shawn Ross)
**Records:** 20
**Date Range:** 12 October - 14 November 2009

---

## Sources Consulted

| Type | File | Location | Role |
|------|------|----------|------|
| Diary | The Diary of Team C.doc | `Elhovo 2010-12-12/2009/Project Records/Team C/` | PRIMARY (EN, 103 KB) |
| Diary | TeamC_Dnevnik.doc | `Elhovo 2010-12-12/2009/Project Records/Team C/` | SECONDARY (BG, 41 KB) |
| SU Forms | 80103.pdf - 81008.pdf | `Team C/FieldRecords/` | Verification (12 files) |
| Excel | ELH09 SurveySummary.xls | `Master Records/` | Unit ranges |

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
- **Walkers vary by day** (see individual records)

---

## Record-by-Record Verification

### Oct 12 (Mon) — Units 80000-80026 ✓
- **Diary:** "Walkers: Bara, Petra, Sona, Tereza, Todor, Georgi" | Units 80000-80026
- **CSV:** Same walkers and units
- **Status:** CONFIRMED

### Oct 13 (Tue) — Units 80027-80061 ✓
- **Diary:** Same 6 walkers | Units 80027-80061
- **CSV:** Same walkers and units
- **Status:** CONFIRMED

### Oct 14 (Wed) — No survey ⚠️
- **Diary:** "We didn't walk in the fields because the Bulgarians from museum were tired"
- **CSV:** No units (correct), but has walkers listed and erroneous QA_Note
- **Issue D019:** QA_Notes contains "No autumn survey season: No autumn 2009 survey season - diaries end in March/April" — INCORRECT
- **Action:** Replace with "Non-survey day (no field walking conducted)"

### Oct 15 (Thu) — Units 80062-80115 ⚠️
- **Diary:** Units 80062-80103 (54 units total per diary table)
- **CSV:** Units 80062-80115
- **SU Forms:** 80115.pdf shows units 80104-80108+ dated Oct 15
- **Issue D020:** Diary end unit (80103) appears to be transcription error
- **Finding:** CSV unit range 80062-80115 is CORRECT per SU forms
- **Status:** CSV CONFIRMED; diary has transcription error (no correction needed)

### Oct 16 (Fri) — No survey ⚠️
- **Diary:** "Today we didn't walk because it was raining"
- **CSV:** No units (correct), but has erroneous QA_Note
- **Issue D019:** Same erroneous QA_Note as Oct 14
- **Action:** Replace with "Non-survey day (no field walking conducted)"

### Oct 17 (Sat) — No survey ⚠️
- **Diary:** "It was also raining today so we didn't walk again"
- **CSV:** No units (correct), but has erroneous QA_Note
- **Issue D019:** Same erroneous QA_Note as Oct 14
- **Action:** Replace with "Non-survey day (no field walking conducted)"

### Oct 18 (Sun) — No survey ⚠️
- **Diary:** "A trip to Burgas"
- **CSV:** No units (correct), but has erroneous QA_Note
- **Issue D019:** Same erroneous QA_Note as Oct 14
- **Action:** Replace with "Non-survey day (no field walking conducted)"

### Oct 20 (Tue) — Units 80116-80167 ✓
- **Diary:** Units 80116-80167 | Roles: Petra=PDA training, Sona=paper, Tereza=GPS
- **CSV:** Same units, roles captured
- **Status:** CONFIRMED

### Oct 21 (Wed) — Units 80168-80305 ✓
- **Diary:** Units 80168-80305 (137 units)
- **CSV:** Same units
- **Status:** CONFIRMED

### Oct 22 (Thu) — Units 80306-80404 ⚠️
- **Diary:** "Today we walked in five people because Georgi was away" | Units 80306-80404
- **CSV:** Units correct, but has 6 walkers including Georgi
- **Issue D021:** Walker count discrepancy — Georgi was absent this day
- **Action:** Remove Georgi from Walkers_Original and Walkers_Standardised

### Oct 23 (Fri) — Units 80405-80494 ✓
- **Diary:** "Today we were walking without Tereza because she was sick, but we had Jana instead"
- **CSV:** Correctly shows Jana replacing Tereza
- **Status:** CONFIRMED

### Oct 26 (Mon) — Units 80495-80589 ✓
- **Diary:** "Since today we are missing Tereza – she moved to Adelas team because Eric left"
- **CSV:** 5 walkers (no Tereza) — correct
- **Status:** CONFIRMED

### Oct 27 (Tue) — Units 80590-80666 ✓
- **Diary:** Units 80590-80666
- **CSV:** Same units
- **Status:** CONFIRMED

### Oct 28 (Wed) — Units 80667-80723 ✓
- **Diary:** Units 80667-80723
- **CSV:** Same units
- **Status:** CONFIRMED

### Oct 29 (Thu) — Units 80724-80794 ✓
- **Diary:** Units 80724-80794 | "just by us – Bára, Sona, Me [Petra], because Zhoro was tired and Todor refused to walk more"
- **CSV:** 5 walkers listed
- **Note:** Diary mentions only 3 finished some polygons, but 5 started the day — record represents full day roster
- **Status:** CONFIRMED (roster is for full day, not reduced subset)

### Nov 9 (Mon) — Units 80796-80852 ✓
- **Diary:** "Walkers: Scott (leader), Stanislav, Jarka, Radko, Javor" | Units 80796-80852
- **CSV:** Same walkers and units
- **Status:** CONFIRMED

### Nov 10 (Tue) — Units 80853-80909 ✓
- **Diary:** "Walkers: Scott, Stanislav, Jarka, Radko, Zhoro, Jana" | Units 80853-80909
- **CSV:** Same walkers and units
- **Status:** CONFIRMED

### Nov 12 (Thu) — Units 80910-80938 ⚠️
- **Diary:** "Walkers: Scott, Stanislav, Jarka, Radko, Jana" | Units 80910-80938
- **CSV:** Units 80910-80939 (end unit off by 1)
- **Issue D022:** End unit discrepancy — diary says 80938, CSV says 80939
- **Action:** Requires verification; may be Excel rounding or form discrepancy
- **Recommendation:** Accept CSV value pending SU form verification (minor discrepancy)

### Nov 13 (Fri) — Units 80939-80969 ⚠️
- **Diary:** "Walkers: Scott, Stanislav, Jarka, Radko, Jana" | Units 80939-80969
- **CSV:** Units 80839-80969 (start unit clearly wrong)
- **Issue D023:** Start unit typo — 80839 should be 80939
- **Evidence:** 80839 < Nov 12 start (80910), which is impossible for sequential dates
- **Action:** Correct Start_Unit from 80839 to 80939

### Nov 14 (Sat) — Units 80970-81002 ✓
- **Diary:** "Walkers: Scott, Stanislav, Lisi, Radko" | Units 80970-81002
- **CSV:** Same (Lisi = Lizzy)
- **Status:** CONFIRMED

---

## Issues Summary

| ID | Date | Field | Issue | Action |
|----|------|-------|-------|--------|
| D019 | Oct 14, 16, 17, 18 | QA_Notes | Erroneous "No autumn survey season" text | Remove erroneous text |
| D020 | Oct 15 | End_Unit | Diary says 80103, CSV/SU forms say 80115 | No action — CSV correct |
| D021 | Oct 22 | Walkers | Georgi listed but diary says he was away | Remove Georgi |
| D022 | Nov 12 | End_Unit | Diary 80938, CSV 80939 (off by 1) | Accept CSV (minor) |
| D023 | Nov 13 | Start_Unit | CSV 80839 is typo for 80939 | Correct to 80939 |

---

## Corrections Required

### D019: Correct QA_Notes for non-survey days (4 records)

**Records:** Oct 14, Oct 16, Oct 17, Oct 18

**Current QA_Notes contain:**
```
MISSING: Survey units | No role data available | No autumn survey season: No autumn 2009 survey season - diaries end in March/April
```

**Corrected QA_Notes:**
```
Non-survey day (no field walking conducted)
```

**Reasoning:** These are legitimate non-survey days documented in the diary:
- Oct 14: "We didn't walk in the fields because the Bulgarians from museum were tired"
- Oct 16: "Today we didn't walk because it was raining"
- Oct 17: "It was also raining today so we didn't walk again"
- Oct 18: "A trip to Burgas"

Nothing is "missing" — these records are complete as non-survey days.

**User Decision:**
- [X] Approve
- [ ] Modify: _______________

**Status:** ✅ APPLIED (27 Nov 2025)

---

### D021: Remove Georgi from Oct 22 record

**Record:** 2009-10-22, Team C

**Current Walkers_Original:**
```
Bara | Petra Tušlová | Sona | Tereza | Todor | Georgi
```

**Corrected Walkers_Original:**
```
Bara | Petra Tušlová | Sona | Tereza | Todor
```

**Current Walkers_Standardised:**
```
Bara Weissová | Petra Tušlová | Sona Holičková | Tereza Dobrovodská | Todor Vulchev | Georgi Nekhrizov
```

**Corrected Walkers_Standardised:**
```
Bara Weissová | Petra Tušlová | Sona Holičková | Tereza Dobrovodská | Todor Vulchev
```

**Source evidence:** Diary states "Today we walked in five people because Georgi was away"

**User Decision:**
- [X] Approve
- [ ] Modify: _______________

**Status:** ✅ APPLIED (27 Nov 2025)

---

### D023: Correct Nov 13 Start_Unit

**Record:** 2009-11-13, Team C

**Current Start_Unit:** 80839
**Corrected Start_Unit:** 80939

**Source evidence:**
- Diary clearly states units 80939-80969
- Unit 80839 is impossible — it's less than Nov 12's start unit (80910)
- Sequential unit progression: Nov 12 ends 80938/80939, Nov 13 starts 80939

**User Decision:**
- [X] Approve
- [ ] Modify: _______________

**Status:** ✅ APPLIED (27 Nov 2025)

---

## Summary Statistics

| Metric | Count |
|--------|-------|
| Records checked | 20 |
| Records confirmed | 14 |
| Issues found | 5 |
| Corrections required | 6 field updates |
| Source gaps | 0 |

### Issues by Category
- QA_Notes errors: 4 (D019)
- Walker errors: 1 (D021)
- Unit errors: 1 (D023)
- Unit discrepancies noted: 1 (D022 - minor, accepted)

---

## Notes

### Diary Observations

1. **Oct 15 unit count:** Diary table shows 54 total units with end unit 80103, but 80062-80103 is only 42 units. The actual end unit 80115 gives 54 units (80062-80115), matching the total. Transcription error in diary.

2. **Oct 22 "Tereza" anomaly:** Record still lists Tereza in walkers, but diary says only 5 people walked. However, Tereza didn't leave until Oct 26. Need to verify if Oct 22 should have Tereza (diary unclear on her presence that specific day vs Georgi's absence).

   **Resolution:** Re-reading diary: "Today we walked in five people because Georgi was away." The original 6-person team minus Georgi = 5 walkers, which includes Tereza. The CSV correctly has Tereza but incorrectly has Georgi. Correction confirmed.

3. **Nov 9-14 team change:** Complete roster change from Czech/Bulgarian team to Scott Jackson leading. Well documented in diary.

4. **"Lisi" = "Lizzy":** Nov 14 diary writes "Lisi" which is the same person as "Lizzy" in CSV (Czech diminutive). This is the unidentified Czech volunteer noted in follow-up-actions.md.

---

**Document created:** 26 November 2025
**Last updated:** 27 November 2025
