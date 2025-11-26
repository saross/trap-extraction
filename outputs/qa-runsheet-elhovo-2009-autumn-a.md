# QA Runsheet: Elhovo 2009 Autumn — Team A

**Date:** 26 November 2025
**Status:** COMPLETE — Corrections applied
**Records verified:** 22
**Scope:** Team A, October-November 2009

---

## Source Documents Consulted

| Source | Type | Location | Notes |
|--------|------|----------|-------|
| Diary Team A.doc | EN Diary | `Elhovo 2010-12-12/2009/Project Records/Team A/` | 132 KB, comprehensive daily entries with unit summary tables |
| SU Form PDFs | Field Records (PRIMARY) | `Elhovo 2010-12-12/2009/Project Records/Team A/FieldRecords/` | Survey Unit forms — authoritative for unit numbers |
| ELH09 SurveySummary.xls | Excel (Tier 1) | `Elhovo 2010-12-12/2009/Project Records/Master Records/` | Authoritative unit numbers |

**Note:** No DPF scans exist for ELH 2009 (season-wide gap documented in S004). However, SU form PDFs exist and provide primary field evidence for unit numbers.

---

## Verification Summary

| Category | Count | Details |
|----------|-------|---------|
| Records verified | 22 | 11 survey days + 3 non-survey days + 1 total collections day |
| Diary errors (CSV correct) | 1 | Oct 21 start unit — diary says 60196, SU form confirms CSV's 60195 is correct |
| Walker discrepancies | 4 | Oct 26-29: Eric→Tereza substitution not reflected (D016) |
| Erroneous QA_Notes | 3 | Oct 30, 31, Nov 4: incorrect "no autumn diary" note (D017) |
| Missing Diary_Source | 1 | Nov 9 record (D018) |
| Confirmed correct | 14 | Including Oct 21 after SU form verification |

---

## Record-by-Record Verification

### Survey Days with Unit Data

| Date | CSV Units | Diary Units | Walkers Match | Status |
|------|-----------|-------------|---------------|--------|
| 2009-10-12 | 60000-60038 | 60000-60038 | ✓ | ✅ Verified |
| 2009-10-13 | 60039-60086 | 60039-60086 | ✓ | ✅ Verified |
| 2009-10-15 | 60087-60126 | 60087-60126 | ✓ | ✅ Verified |
| 2009-10-20 | 60127-60194 | 60127-60194 | ✓ | ✅ Verified |
| 2009-10-21 | 60195-60273 | ~~60196~~-60273 | ✓ | ✅ CSV correct (diary error, SU form confirms) |
| 2009-10-22 | 60274-60376 | 60274-60376 | ✓ | ✅ Verified |
| 2009-10-23 | 60377-60456 | 60377-60456 | ✓ | ✅ Verified |
| 2009-10-26 | 60457-60546 | 60457-60546 | ⚠️ Eric→Tereza | ⚠️ Walker error |
| 2009-10-27 | 60547-60616 | 60547-60616 | ⚠️ Eric→Tereza | ⚠️ Walker error |
| 2009-10-28 | 60617-60696 | 60617-60696 | ⚠️ Eric→Tereza | ⚠️ Walker error |
| 2009-10-29 | 60697-60776 | 60697-60776 | ⚠️ Eric→Tereza | ⚠️ Walker error |
| 2009-11-02 | 60777-60861 | 60777-60861 | ✓ | ✅ Verified |
| 2009-11-03 | 60862-60964 | 60862-60964 | ✓ | ✅ Verified |
| 2009-11-05 | 60965-61021 | 60965-61021 | ✓ | ✅ Verified |
| 2009-11-06 | 61022-61079 | 61022-61079 | ✓ | ✅ Verified |
| 2009-11-07 | 61080-61185 | 61080-61185 | ✓ | ✅ Verified |
| 2009-11-09 | 61186-61249 | 61186-61249 | ✓ | ⚠️ Missing Diary_Source |
| 2009-11-10 | 61250-61339 | 61250-61339 | ✓ | ✅ Verified |
| 2009-11-14 | 61340-61344 | 61340-61344 | ✓ | ✅ Verified |

### Non-Survey Days

| Date | CSV Status | Diary Evidence | QA_Notes Issue |
|------|------------|----------------|----------------|
| 2009-10-30 | No units (correct) | Rain, muddy fields — "Resting day due to muddy fields" | ⚠️ Erroneous "no autumn diary" note |
| 2009-10-31 | No units (correct) | Halloween, pottery analysis — "Halloween party preparations" | ⚠️ Erroneous "no autumn diary" note |
| 2009-11-04 | No units (correct) | Rain — "We wake up to a rain... Resting day" | ⚠️ Erroneous "no autumn diary" note |

---

## Issues Found

### D015: 2009-10-21 — Diary Transcription Error (No CSV Correction Needed)

**Type:** Diary error — CSV is correct

| Source | Start Unit | End Unit | Status |
|--------|------------|----------|--------|
| SU Form (60192.pdf, p.56) | **60195** | — | ✓ PRIMARY |
| CSV (current) | 60195 | 60273 | ✓ CORRECT |
| Diary (Diary Team A.doc) | 60196 | 60273 | ✗ ERROR |

**Resolution:** No correction required — CSV value 60195 is correct

**SU Form Evidence:**

The SU form for unit 60195 (page 56 of field records) clearly shows:

- **Date:** 21 October 2009
- **Survey unit:** 60.195
- **Walk interval:** 10m
- **Walkers:** Martin, [unclear], Adela, [unclear], Eric

This definitively proves unit 60195 was surveyed on 21 October, not skipped.

**Diary Error Analysis:**
The diary's "First unit: 60196" is a transcription error made when Adela compiled the unit summary table after fieldwork. The SU form, completed in the field at the time of survey, is the authoritative primary source.

**Lesson:** SU forms take precedence over diary summary tables for unit numbers. Diaries are secondary sources for numeric data, subject to transcription errors.

---

### D016: 2009-10-26 to 2009-10-29, Team A — Walker Substitution

**Problem:** Eric departed for Istanbul on Oct 25; Tereza Dobrovodská substituted for him Oct 26-29. CSV incorrectly showed Eric/Erik Andersen.

**Original CSV values (git commit 528a5f0^):**
- Walkers_Original: `...Eric`
- Walkers_Standardised: `...Erik Andersen`

**Fix:** Replace Eric → Tereza and Erik Andersen → Tereza Dobrovodská for 4 records.

**Sources consulted:**

1. Diary Team A.doc — Oct 25, 26, 27 entries
2. Diary Team C.doc — Oct 23 entry (Tereza sick)
3. TRAP-Participants.csv — both Terezas present in 2009-autumn
4. attribution.csv — Team C walker list shows T. Dobrovodská on Team C Oct 12-22

**Evidence:**

> Oct 25: "Eric decided to go on to Istanbul and is dropped off at the busstation"

> Oct 23 Team C: "Today we were walking without Tereza because she was sick, but we had Jana instead" — Tereza Dobrovodská left Team C

> Oct 26 Team A: "Team A comprises Adela, Ilija, Aneta, Martin and **Tereza as a substitute for Eric**." — T. Dobrovodská moved to Team A

**Resolution logic:** People were only on one team at a time. Tereza Dobrovodská was on Team C until Oct 22, sick Oct 23, then moved to Team A Oct 26-29. Tereza Blažková had no Team C presence to explain her availability.

**Note:** A previous session (crashed) partially applied this correction using Tereza Blažková. This session corrected the Tereza identity based on team membership analysis.

**Correction applied (26 Nov 2025):**

| Date | Walkers_Original | Walkers_Standardised |
|------|------------------|----------------------|
| 2009-10-26 | Eric → Tereza ✅ | Erik Andersen → Tereza Dobrovodská ✅ |
| 2009-10-27 | Eric → Tereza ✅ | Erik Andersen → Tereza Dobrovodská ✅ |
| 2009-10-28 | Eric → Tereza ✅ | Erik Andersen → Tereza Dobrovodská ✅ |
| 2009-10-29 | Eric → Tereza ✅ | Erik Andersen → Tereza Dobrovodská ✅ |

**Severity:** MAJOR (personnel error)

---

**User Decision:** [X] Approved

---

### D017: 2009-10-30, 2009-10-31, 2009-11-04, Team A — Erroneous QA_Notes

**Problem:** QA_Notes incorrectly state "No autumn 2009 survey season - diaries end in March/April" — this is factually wrong.

**Fix:** Remove the erroneous statement from QA_Notes for these 3 non-survey day records.

**Resolution (26 Nov 2025):** ✅ **No correction needed** — Upon inspection, Team A records for Oct 30, 31, Nov 4 do NOT contain this erroneous text. The text exists on Team C records (Oct 14, 16, 17, 18) which is a separate issue.

Team A QA_Notes currently contain only: "MISSING: Survey units | No role data available"

**Severity:** N/A (issue did not apply to Team A)

---

**User Decision:** [X] Resolved — no action required

---

### D018: 2009-11-09, Team A — Missing Diary_Author Field

**Problem:** Diary_Author field was empty while all other Team A November records had "Adela Sobotkova".

**Note:** Original issue documented as "Diary_Source" but CSV has no such column. The actual field is "Diary_Author". PDF_Source already had "Diary Team A.doc".

**Fix:** Add "Adela Sobotkova" to the Diary_Author field.

**Sources consulted:**

1. Diary Team A.doc — Nov 9 entry (confirms Adela authored)
2. Other Team A records (Nov 2-7, 10) — all have Diary_Author = "Adela Sobotkova"

**Correction applied (26 Nov 2025):**

| Date | Field | Before | After |
|------|-------|--------|-------|
| 2009-11-09 | Diary_Author | (empty) | Adela Sobotkova ✅ |

**Severity:** Minor (metadata omission)

---

**User Decision:** [X] Approved

---

## Unit Continuity Check

| Date | End Unit | Next Date | Start Unit | Gap | Status |
|------|----------|-----------|------------|-----|--------|
| 10-12 | 60038 | 10-13 | 60039 | 0 | ✓ |
| 10-13 | 60086 | 10-15 | 60087 | 0 | ✓ |
| 10-15 | 60126 | 10-20 | 60127 | 0 | ✓ |
| 10-20 | 60194 | 10-21 | 60195 | 0 | ✓ |
| 10-21 | 60273 | 10-22 | 60274 | 0 | ✓ |
| 10-22 | 60376 | 10-23 | 60377 | 0 | ✓ |
| 10-23 | 60456 | 10-26 | 60457 | 0 | ✓ |
| 10-26 | 60546 | 10-27 | 60547 | 0 | ✓ |
| 10-27 | 60616 | 10-28 | 60617 | 0 | ✓ |
| 10-28 | 60696 | 10-29 | 60697 | 0 | ✓ |
| 10-29 | 60776 | 11-02 | 60777 | 0 | ✓ |
| 11-02 | 60861 | 11-03 | 60862 | 0 | ✓ |
| 11-03 | 60964 | 11-05 | 60965 | 0 | ✓ |
| 11-05 | 61021 | 11-06 | 61022 | 0 | ✓ |
| 11-06 | 61079 | 11-07 | 61080 | 0 | ✓ |
| 11-07 | 61185 | 11-09 | 61186 | 0 | ✓ |
| 11-09 | 61249 | 11-10 | 61250 | 0 | ✓ |
| 11-10 | 61339 | 11-14 | 61340 | 0 | ✓ |

**Note:** Perfect unit continuity confirmed. The apparent gap (diary stating Oct 21 starts at 60196) was a diary transcription error — SU form confirms unit 60195 was surveyed on Oct 21.

---

## Walker Composition Changes (Verified)

The diary documents these team composition changes:

| Period | Team A Composition | Notes |
|--------|-------------------|-------|
| Oct 12-23 | Adela, Ilija, Aneta, Martin, Eric | Standard 5-person team |
| Oct 23 | Adela, Ilija, Aneta, Eric (4) | Martin with Team B |
| Oct 25 | — | Eric departs for Istanbul during Edirne excursion |
| Oct 26-29 | Adela, Ilija, Aneta, Martin, **Tereza** | Tereza substitutes for Eric |
| Nov 1 | — | Tereza departs; Katarina arrives |
| Nov 2-14 | Adela, Ilija, Todor, Martin, Katarina | "New incarnation" of Team A |
| Nov 5 | Adela, Todor, Martin, Katarina (4) | Ilija absent |
| Nov 7 | Adela, Martin, Todor, Katarina (4) | Ilija absent |
| Nov 14 | Adela, Katarina, Martin (3) | Total collections day |

---

## Role Data Assessment

The diary contains explicit role assignments for early October:

| Date | PDA_Operator | Paper_Recorder | GPS_Operator | Source |
|------|--------------|----------------|--------------|--------|
| Oct 12 | Adela | Aneta | Martin | Implicit from Oct 13 entry |
| Oct 13 | Adela | Aneta | Martin | "Martin – GPS, Aneta- recording, me – PDA" |
| Oct 15-29 | Adela | Aneta | Martin | Diary refers to "usual setup" |

**Note:** Role data is sparse for November records. The diary does not consistently document role assignments after the team composition change on Nov 2.

---

## Summary Statistics

| Metric | Value |
|--------|-------|
| Total records | 22 |
| Survey days | 19 |
| Non-survey days | 3 |
| Issues investigated | 4 (D015-D018) |
| Corrections applied | 9 field updates across 5 records |
| Issues resolved (no change) | 2 (D015 diary error, D017 not applicable) |

---

## Applied Corrections (26 Nov 2025)

| ID | Date(s) | Field | Before | After | Status |
|----|---------|-------|--------|-------|--------|
| D015 | 2009-10-21 | Start_Unit | 60195 | 60195 | ✅ No change (diary error) |
| D016 | 2009-10-26 | Walkers_Original | ...Eric | ...Tereza | ✅ Done |
| D016 | 2009-10-26 | Walkers_Standardised | ...Erik Andersen | ...Tereza Dobrovodská | ✅ Done |
| D016 | 2009-10-27 | Walkers_Original | ...Eric | ...Tereza | ✅ Done |
| D016 | 2009-10-27 | Walkers_Standardised | ...Erik Andersen | ...Tereza Dobrovodská | ✅ Done |
| D016 | 2009-10-28 | Walkers_Original | ...Eric | ...Tereza | ✅ Done |
| D016 | 2009-10-28 | Walkers_Standardised | ...Erik Andersen | ...Tereza Dobrovodská | ✅ Done |
| D016 | 2009-10-29 | Walkers_Original | ...Eric | ...Tereza | ✅ Done |
| D016 | 2009-10-29 | Walkers_Standardised | ...Erik Andersen | ...Tereza Dobrovodská | ✅ Done |
| D017 | 2009-10-30, 31, 11-04 | QA_Notes | — | — | ✅ No change needed |
| D018 | 2009-11-09 | Diary_Author | (empty) | Adela Sobotkova | ✅ Done |

**Summary:** 9 field updates applied (D016: 8, D018: 1); 2 issues required no changes after investigation.

---

## Document History

- **Created:** 26 November 2025
- **Updated:** 26 November 2025 — D015 resolved via SU form verification (CSV correct, diary error)
- **Updated:** 26 November 2025 — D016 correction: Tereza Blažková→Dobrovodská (T.D. was Team C walker who moved to Team A as Eric substitute)
- **Updated:** 26 November 2025 — D017: No correction needed (Team A records didn't have erroneous text)
- **Updated:** 26 November 2025 — D018: Added Diary_Author (Adela Sobotkova) to Nov 9
- **QA performed by:** Claude Code
- **Primary sources:** SU Form PDFs (FieldRecords/), Diary Team A.doc (EN, 132 KB), TRAP-Participants.csv
