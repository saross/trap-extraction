# QA Runsheet: Kazanlak 2009 Spring Team E

**Study Area/Season:** Kazanlak (Seuthopolis) 2009 Spring
**Team:** E
**QA Date:** 2025-12-01
**QA Performed By:** Claude Code (with Shawn Ross)
**Records in CSV:** 7
**Date Range:** 2009-03-20 to 2009-04-03

---

## Sources Consulted

| Type | File | Location | Role |
|------|------|----------|------|
| DPF scan | E_Summary.pdf | `Kazanluk/2009/Project Records/TeamE/` | PRIMARY (226 KB, 8 pages) |
| DPF scan | E_Summary26Mar-3Apr.pdf | `Kazanluk/2009/Project Records/TeamE/` | Verification (114 KB) |
| Diary | E Diary_BG.doc | `Kazanluk/2009/Project Records/TeamE/` | Reference (BG only, 83 KB) |

---

## Team Composition

### Survey Period: 20 March - 3 April 2009
- **Leader:** Shawn Ross (throughout)
- **Regular walkers:** Bryan Zlatos (Brian), Katarina Čuláková, Silvia Ivanova, Evtimka Dimitrova
- **Later additions:** Charlotte Devereux Byron, Tomáš Chmela (from Mar 25)
- **Apr 03 crew:** Adela Sobotkova, Charlotte, Barbara Olujic, Petra Janouchová, Bryan Zlatos

### DPF Authors
- **Primary:** Katarina Čuláková (most forms)
- **Others:** Petra Tušlová (Apr 03), Matyáš Kracík + Tereza Blažková (Mar 27)

---

## Record-by-Record Verification

### 2009-03-20 (Friday) — Units 50011-50059 ⚠️ MAJOR ERROR
- **DPF (p.1):** Team E, Leader: Shawn, Walkers: Brian Zlatos, Katarina Culakova, Silvia, Eftimka, Units: 50000-50070, Total: ~68, Skipped: 50011, 50015, Author: Katarina
- **CSV:** Leader: Shawn Ross, Units: 50011-50059, Walkers: 5 (Shawn, Bryan, Katarina, Silvia, Evtimka)
- **Source divergence:** CSV Start Unit 50011 is actually a SKIPPED unit in DPF. DPF shows 50000-50070; CSV shows 50011-50059.
- **Analysis:** CSV range is incorrect. Start should be 50000, End should be 50070.
- **Status:** UNIT ERROR (E001) - Both Start and End units incorrect

### 2009-03-23 (Monday) — Units 50071-50142 ⚠️
- **DPF (p.2):** Team E, Leader: Shawn, Walkers: Shawn, Brian, Zlatos, Tomas Chimela, Katarina Culakova, Silvia Ivanova, Units: 50070-50142, Total: 72, Author: Katarina Culakova
- **CSV:** Leader: Shawn Ross, Units: 50071-50142, Walkers: 5 (Shawn, Bryan, Tomáš, Katarina, Silvia)
- **Source divergence:** CSV Start Unit 50071 vs DPF 50070 (off by 1)
- **Samples noted:** 50072, 50073, 50074, 50075, 50077, 50087, 50091, 50093, 50111, 50113, 50116, 50137, 50140
- **Objects:** O-5001, Q-5002
- **Status:** UNIT DISCREPANCY (E002) - Start Unit off by 1

### 2009-03-24 (Tuesday) — MISSING FROM CSV ❌
- **DPF (p.3 of E_Summary.pdf):** Team E, Leader: Sean (Shawn), Walkers: Sean Ross, Charlotte Baron, Silvia Ivanova, Tomas Chimela, Katarina Culakova, Units: 50143-50202, Total: 60, Author: Katarina Culakova
- **CSV:** NO RECORD EXISTS for March 24
- **Objects:** O-5003 (point), Q-5005 (polygon)
- **Status:** MISSING RECORD (E003) - Entire day missing from CSV

### 2009-03-25 (Wednesday) — Units 50203-50249 ⚠️
- **DPF (p.4):** Team E, Leader: Shawn, Walkers: Shawn Ross, Charlotte Baron, Silvia Ivanova, Tomas Chimela, Katarina Culakova, Units: 50203-50246, Total: 44, Author: Katarina Culakova
- **CSV:** Leader: Shawn Ross, Units: 50203-50249, Walkers: 5 (Shawn, Charlotte, Katarina, Silvia, Tomáš)
- **Source divergence:** CSV End Unit 50249 vs DPF 50246 (off by 3)
- **Samples noted:** 50217, 50218, 50220, 50221, 50222, 50226, 50229, 50233, 50234, 50239, 50241
- **Objects:** O-5004 (point), O-5006 (flat scatter)
- **Status:** UNIT DISCREPANCY (E004) - End Unit off by 3

### 2009-03-26 (Thursday) — Units 50247-50289 ✓
- **DPF (p.5, also E_Summary26Mar-3Apr.pdf p.1):** Team E, Leader: Shawn Ross, Walkers: Charlotte Baron, Katarina Culakova, Silvia Ivanova, Tomas Chimela, Shawn Ross, Units: 50247-50289, Total: 43, Skipped: 8, Author: Katarina Culakova
- **CSV:** Leader: Shawn Ross, Units: 50247-50289, Walkers: 5 (Shawn, Charlotte, Katarina, Silvia, Tomáš)
- **GPS Points:** 5008 (mound), 5007 (mound), 5009 (worked stone)
- **Status:** CONFIRMED

### 2009-03-27 (Friday) — Units 50290-50319 ✓
- **DPF (E_Summary26Mar-3Apr.pdf):** Team E, Leader: Shawn Ross, Walkers: Tomas Chimela, Matyáš Kracík, Tereza Blažková, Charlotte Baron, Martin..., Units: 50290-50319, Total: 29, Skipped: 50316, Author: M Kracík + Tereza Bl.
- **CSV:** Leader: Shawn Ross, Units: 50290-50319, Walkers: 5 (Shawn, Charlotte, Silvia, Tomáš, Katarina)
- **Note:** DPF comments "12 in forms, others not checked off" - suggests larger team than CSV shows
- **Status:** CONFIRMED

### 2009-03-31 (Tuesday) — Units 50520-50542 ⚠️ QUESTIONABLE
- **DPF (handwritten note):** Team E, Date: 31 March 2009, Shawn Ross, "total pick-ups only at site KAZ005", samples 502-504
- **CSV:** Leader: Shawn Ross, Units: 50520-50542, Walkers: 1 (Shawn Ross only)
- **Source divergence:** DPF says "pick-ups only" (no intensive survey units), but CSV shows unit range 50520-50542
- **Gap analysis:** If Mar 27 ends at 50319 and Apr 03 DPF starts at 50320, then 50520-50542 doesn't fit the sequence
- **Status:** NEEDS VERIFICATION (E005) - CSV units don't match DPF or unit sequence

### 2009-04-03 (Friday) — No Units (Mound Reconnaissance) ⚠️ ERROR
- **DPF (E_Summary26Mar-3Apr.pdf):** Team E, Leader: Shawn, Walkers: Adela, Charlotte, Barbara, Petra, Brian, Units: 50320-50342, Total: 23, Author: P.T.
- **CSV:** Leader: Shawn Ross, Units: none, Walkers: 6 (Shawn, Adela, Charlotte, Barbara, Petra, Bryan), Note: "Non-standard survey: Combined team mound reconnaissance west of Kran"
- **Source divergence:** DPF clearly shows intensive survey units 50320-50342, but CSV marks as non-standard with no units
- **GPS Points:** 5024-5040
- **Status:** INCORRECT CATEGORISATION (E006) - Should have units 50320-50342

---

## Issues Summary

| ID | Date | Field | Issue | Action |
|----|------|-------|-------|--------|
| E001 | Mar 20 | Unit Range | CSV: 50011-50059, DPF: 50000-50070 | [ ] Update to 50000-50070 |
| E002 | Mar 23 | Start Unit | CSV: 50071, DPF: 50070 | [ ] Update to 50070 |
| E003 | Mar 24 | Record | MISSING - DPF shows units 50143-50202 | [ ] Add record |
| E004 | Mar 25 | End Unit | CSV: 50249, DPF: 50246 | [ ] Update to 50246 |
| E005 | Mar 31 | Unit Range | CSV: 50520-50542, DPF: "pickup only" | [ ] Verify source |
| E006 | Apr 03 | Unit Range | CSV: none, DPF: 50320-50342 | [ ] Add units |

---

## Corrections Required

### E001: Mar 20 Unit Range (MAJOR)
- **Current:** Start Unit = 50011, End Unit = 50059
- **DPF shows:** Start Unit = 50000, End Unit = 50070, Skipped: 50011, 50015
- **Analysis:** CSV Start Unit 50011 is actually listed as a skipped unit in DPF. The true range is 50000-50070.
- **Recommendation:** Update to 50000-50070
- [ ] User Decision Required

### E002: Mar 23 Start Unit
- **Current:** Start Unit = 50071
- **DPF shows:** Start Unit = 50070
- **Gap analysis:** Mar 20 DPF ends at 50070; Mar 23 DPF starts at 50070 (continuous)
- **Recommendation:** Update to 50070
- [ ] User Decision Required

### E003: Mar 24 Missing Record (MAJOR)
- **Current:** No record exists
- **DPF shows:** Team E, Leader: Shawn, Units: 50143-50202, Total: 60 units, Author: Katarina Čuláková
- **Walkers:** Shawn Ross, Charlotte Baron, Silvia Ivanova, Tomáš Chmela, Katarina Čuláková
- **Recommendation:** Add new record for 2009-03-24
- [ ] User Decision Required

### E004: Mar 25 End Unit
- **Current:** End Unit = 50249
- **DPF shows:** End Unit = 50246
- **Gap analysis:** Mar 24 DPF ends at 50202; Mar 25 DPF starts at 50203 (continuous). Mar 25 ends at 50246; Mar 26 starts at 50247 (continuous).
- **Recommendation:** Update to 50246
- [ ] User Decision Required

### E005: Mar 31 Unit Range (NEEDS VERIFICATION)
- **Current:** Start Unit = 50520, End Unit = 50542
- **DPF shows:** "total pick-ups only at site KAZ005" - no intensive survey units
- **Analysis:** The unit range 50520-50542 doesn't fit the sequence. DPF suggests this was pickup work, not unit survey.
- **Recommendation:** Verify against original source; may need to remove units or flag as non-standard
- [ ] User Decision Required

### E006: Apr 03 Missing Units
- **Current:** No units (marked as "Non-standard survey: Combined team mound reconnaissance")
- **DPF shows:** Start Unit = 50320, End Unit = 50342, Total = 23 units
- **Analysis:** DPF clearly shows this was intensive survey with units. The "mound reconnaissance" note may refer to a portion of the day.
- **Recommendation:** Add units 50320-50342, update QA_Notes
- [ ] User Decision Required

---

## Source Observations

### Unit Sequence Analysis (DPF-based)

| Date | DPF Start | DPF End | DPF Total | Continuity |
|------|-----------|---------|-----------|------------|
| Mar 20 | 50000 | 50070 | ~68 | Start |
| Mar 23 | 50070 | 50142 | 72 | Continuous |
| Mar 24 | 50143 | 50202 | 60 | Continuous |
| Mar 25 | 50203 | 50246 | 44 | Continuous |
| Mar 26 | 50247 | 50289 | 43 | Continuous |
| Mar 27 | 50290 | 50319 | 29 | Continuous |
| Mar 31 | — | — | — | Pickup only |
| Apr 03 | 50320 | 50342 | 23 | Continuous |

**Key observation:** The DPF unit sequence is perfectly continuous from 50000 to 50342 (excluding Mar 31 which was pickup work). The CSV has multiple breaks in this continuity.

### CSV vs DPF Comparison

| Date | CSV Range | DPF Range | Match |
|------|-----------|-----------|-------|
| Mar 20 | 50011-50059 | 50000-50070 | ❌ Major error |
| Mar 23 | 50071-50142 | 50070-50142 | ⚠️ Start off by 1 |
| Mar 24 | MISSING | 50143-50202 | ❌ Record missing |
| Mar 25 | 50203-50249 | 50203-50246 | ⚠️ End off by 3 |
| Mar 26 | 50247-50289 | 50247-50289 | ✓ |
| Mar 27 | 50290-50319 | 50290-50319 | ✓ |
| Mar 31 | 50520-50542 | (pickup only) | ❓ Questionable |
| Apr 03 | none | 50320-50342 | ❌ Units missing |

### Source Reliability Patterns

- **O1 confirmed:** DPF scans are authoritative for unit numbers.
- **Missing record:** Mar 24 data exists in DPF but was not extracted to CSV (60 survey units).
- **Categorisation error:** Apr 03 was incorrectly marked as non-standard survey despite having intensive survey units.
- **Mar 31 anomaly:** CSV shows units 50520-50542 but DPF says "pickup only". This range doesn't fit the unit sequence and may be incorrectly attributed.

### Implications for Future QA

- Check for missing records by verifying unit range continuity
- Skipped units in DPF should not be used as Start/End values in CSV
- "Non-standard survey" categorisation should be verified against DPF unit fields

---

## Notes

- **BG diary only:** No English diary exists for Team E. Verification limited to DPF comparison.
- **Unit numbering:** Team E used 50xxx prefix (compared to A=10xxx, B=20xxx, C=30xxx, D=40xxx)
- **Mar 31 anomaly:** The CSV shows units 50520-50542, which is a gap of ~200 units from Mar 27 (50319). This suggests either: (a) different source material, (b) incorrect date attribution, or (c) a different team's data.
- **Large team on Mar 27:** DPF notes "12 in forms, others not checked off" suggesting more walkers than recorded.

---

## Summary Statistics

| Metric | Count |
|--------|-------|
| Records in CSV | 7 |
| Records in DPF | 8 |
| Records confirmed | 2 |
| Unit discrepancies | 3 (E001, E002, E004) |
| Missing records | 1 (E003 - Mar 24) |
| Categorisation errors | 1 (E006 - Apr 03) |
| Questionable data | 1 (E005 - Mar 31) |
| Corrections required | 6 |

### Issues by Category
- Missing records: 1 (E003 - Mar 24)
- Unit range errors: 3 (E001, E002, E004)
- Incorrect categorisation: 1 (E006 - Apr 03)
- Questionable data: 1 (E005 - Mar 31)
- Walker errors: 0
- Role errors: 0

---

**Document created:** 2025-12-01
**Last updated:** 2025-12-01
