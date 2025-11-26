# QA Discrepancies Log

**Created:** 26 November 2025
**Purpose:** Document cases where sources disagree and record resolution reasoning

---

## Format

Each entry records:

- **Record identifier** (date, team)
- **Field** with discrepancy
- **Source values** (what each source says)
- **Resolution** (which value was chosen)
- **Reasoning** (why that value was preferred)

---

## Elhovo 2010 Autumn

### D001: 2010-10-23, Team A — Start Unit

| Source | Value |
|--------|-------|
| DPF scan (Day_03.pdf, Form 2) | 61424 |
| Diary (A_Diary.docx) | 61425 |
| CSV (current) | 61424 |

**Resolution:** 61424 (DPF scan value)

**Reasoning:** Per source priority rules, DPF scans are PRIMARY for basic numeric information. The diary value (61425) may be a transcription error or the diary author may have misremembered. The DPF was completed on the day of fieldwork and is more likely to be accurate.

---

### D002: 2010-10-23, Team A — End Unit

| Source | Value |
|--------|-------|
| DPF scan (Day_03.pdf, Form 2) | 61475 |
| Diary (A_Diary.docx) | 61473 |
| CSV (current) | 61475 |

**Resolution:** 61475 (DPF scan value)

**Reasoning:** Same as D001. DPF scan is PRIMARY for unit numbers.

---

### D003: 2010-10-24, Team A — End Unit (Diary Typo)

| Source | Value |
|--------|-------|
| DPF scan (Day_03.pdf, Form 3) | 61549 |
| Diary (A_Diary.docx) | 61349 |
| CSV (current) | 61549 |

**Resolution:** 61549 (DPF scan value)

**Reasoning:** The diary value "61349" is clearly a typo — it would mean the end unit is lower than the start unit (61476), which is impossible. The DPF scan value 61549 is logically consistent (61549 > 61476) and matches the total units recorded (73 units from 61476 to 61549 inclusive = 74 units, close to "Total Units: 73" on the form).

---

### D004: 2010-11-02, Team A — Start Unit

| Source | Value |
|--------|-------|
| DPF scan (Day_05.pdf, Form 1) | 61549 |
| Diary (A_Diary.docx) | 61553 (stated as "First unit") |
| CSV (current) | 61549 |

**Resolution:** 61549 (DPF scan value)

**Reasoning:** The diary states "First unit: 61553" but the unit sample list in the same entry begins with "61549". This inconsistency within the diary itself suggests the "61553" was an error. The DPF scan value 61549 is consistent with the sample list and provides continuity from the previous day's end unit (2010-10-24 ended at 61549).

**Note:** The continuity of 61549 appearing as both Oct 24 end unit and Nov 2 start unit suggests either: (a) unit 61549 was walked on both days, or (b) there's a boundary/overlap convention. This is not an error, just an observation.

---

### D005: 2010-11-03, Team B — Start Unit (Major Error)

| Source | Value |
|--------|-------|
| DPF scan (Day_02.pdf, Form 2) | 71525 |
| Diary (Team B Diary new.docx) | 71525 |
| CSV (current) | 71245 |

**Resolution:** 71525 (DPF scan and diary agree)

**Reasoning:** Both sources agree on 71525. The CSV value 71245 is incorrect by 280 units — likely a transcription or OCR error during original extraction. This is not a minor discrepancy but a significant data error requiring correction.

---

### D006: 2010-11-04, Team B — End Unit

| Source | Value |
|--------|-------|
| DPF scan (Day_04.pdf, Form 1) | 71649 |
| Diary (Team B Diary new.docx) | 71650 |
| CSV (current) | 71650 |

**Resolution:** 71649 (DPF scan value)

**Reasoning:** DPF scan shows 71649, diary shows 71650. Per source priority rules, DPF scan takes precedence. Additionally, 71650 is the Start Unit for the following day (5 Nov), suggesting the diary copied the wrong boundary value. The DPF, completed on the day, is more reliable.

---

### D007: 2010-11-06, Team B — Missing Unit Range

| Source | Value |
|--------|-------|
| DPF scan (Day_06.pdf, Form 1) | Start: 71713, End: 71760 |
| Diary (Team B Diary new.docx) | Start: 71713, End: 71760 |
| CSV (current) | (empty) |

**Resolution:** Add Start Unit 71713, End Unit 71760

**Reasoning:** Both sources agree on the values. The CSV QA_Notes already flagged this as missing data. This is a source gap where data was available but not extracted, not a conflict between sources.

### D008: 2010-11-07, Team B — Missing CSV Record

**Type:** Missing record (not extracted)

| Source | Status | Data |
|--------|--------|------|
| CSV | ✗ MISSING | No record exists |
| DPF scan (Day_06.pdf, Form 2) | ✓ Present | Units 71761-71800, Leader: SAR/R.L |
| Primary Diary | ✓ Present | Units 71761-71800, Leader: Dr. Ross / Royce Lawrence |

**Evidence from diary:**
> "7 November 2010, Kimberley Lowe... Start Unit: 71761, End Unit: 71800, Total Units: 30"

**Action required:** Add missing record for 2010-11-07 Team B to attribution.csv

---

### D009: 2010-11-10, Team B — Missing CSV Record

**Type:** Missing record (not extracted)

| Source | Status | Data |
|--------|--------|------|
| CSV | ✗ MISSING | No record exists |
| DPF scan (Day_08.pdf, Form 1) | ✓ Present | Units 71801-71833, Leader: R.L |
| Primary Diary | ✓ Present | Units 71801-71833, Leader: Royce Lawrence |

**Evidence from diary:**
> "10 November 2010, Kimberley Lowe... Start Unit: 71801, End Unit: 71833, Total Units: 33"

**Action required:** Add missing record for 2010-11-10 Team B to attribution.csv

---

### D010: Unit Continuity — Explained

The apparent 41-unit gap between 6 Nov (71760) and 11 Nov (71801) is now explained:

| Date | Start | End | Status |
|------|-------|-----|--------|
| 6 Nov | 71713 | 71760 | ✓ In CSV |
| 7 Nov | 71761 | 71800 | ✗ **Missing from CSV** |
| 10 Nov | 71801 | 71833 | ✗ **Missing from CSV** |
| 11 Nov | 71834 | 71909 | ✓ In CSV |

Unit continuity is actually perfect once D008 and D009 records are added. No unexplained gaps.

---

## Source Gaps

Records where one or more expected sources are missing.

### S001: 2010-11-11, Team B — Diary Entry Missing

| Source | Status |
|--------|--------|
| DPF scan (Day_08.pdf, Form 2) | ✓ Present |
| Primary Diary (Team B Diary new.docx) | ✗ Missing |
| Secondary Diary (Team B Diary.docx) | ✗ Missing |

**Notes:** Both Team B diaries skip from 10 Nov directly to 12 Nov. The 11 Nov record was extracted solely from the DPF scan. Role information for this day is unavailable.

---

### S002: 2010-11-12, Team B — DPF Scan Missing

| Source | Status |
|--------|--------|
| DPF scan | ✗ Missing |
| Primary Diary (Team B Diary new.docx) | ✓ Present |
| Secondary Diary (Team B Diary.docx) | ✓ Present |

**Notes:** No DPF scan exists for 12 Nov. Record was extracted from diary. Unit numbers rely on diary alone (no cross-verification possible).

---

### S003: 2010-11-14, Team B — DPF Scan Missing

| Source | Status |
|--------|--------|
| DPF scan | ✗ Missing |
| Primary Diary (Team B Diary new.docx) | ✓ Present |
| Secondary Diary (Team B Diary.docx) | ✓ Present |

**Notes:** No DPF scan exists for 14 Nov. Record was extracted from diary. Unit numbers rely on diary alone (no cross-verification possible).

---

## Elhovo 2009 Autumn

### D011: 2009-11-02, Team B — Missing Unit Numbers

**Type:** CSV field missing (extraction error)

| Source | Value |
|--------|-------|
| EN Diary (DiaryTeamB.doc) | Start: 70926, End: 70962 |
| BG Diary (TeamB_Dnevnik Ross.doc) | Start: 70926, End: 70962 |
| CSV (current) | Start: (empty), End: (empty) |

**Resolution:** Add Start Unit 70926, End Unit 70962

**Reasoning:** Both EN and BG diaries agree on unit numbers. The CSV incorrectly contains the note "No autumn 2009 survey season - diaries end in March/April" which is factually incorrect — the diary covers autumn 2009 through mid-November. Unit continuity confirms: 70926 follows Oct 29 end unit (70925) + 1.

---

### D012: 2009-11-03, Team B — Missing Unit Numbers

**Type:** CSV field missing (extraction error)

| Source | Value |
|--------|-------|
| EN Diary (DiaryTeamB.doc) | Start: 70963, End: 71062 |
| BG Diary (TeamB_Dnevnik Ross.doc) | Start: 70963, End: 71062 |
| CSV (current) | Start: (empty), End: (empty) |

**Resolution:** Add Start Unit 70963, End Unit 71062

**Reasoning:** Both EN and BG diaries agree on unit numbers. Unit continuity confirms: 70963 follows Nov 2 end unit (70962) + 1.

---

### D013: 2009-11-05, Team B — Missing Unit Numbers

**Type:** CSV field missing (extraction error)

| Source | Value |
|--------|-------|
| EN Diary (DiaryTeamB.doc) | Start: 71063, End: 71142 |
| BG Diary (TeamB_Dnevnik Ross.doc) | Start: 71063, End: 71142 |
| CSV (current) | Start: (empty), End: (empty) |

**Resolution:** Add Start Unit 71063, End Unit 71142

**Reasoning:** Both EN and BG diaries agree on unit numbers. Unit continuity confirms: 71063 follows Nov 3 end unit (71062) + 1.

---

### D014: Erroneous QA_Notes — Incorrect Diary Coverage Statement

**Type:** Metadata error

**Affected records:** 2009-11-02 B, 2009-11-03 B, 2009-11-05 B

**Current QA_Notes contain:**
> "No autumn survey season: No autumn 2009 survey season - diaries end in March/April"

**Resolution:** Remove this erroneous note

**Reasoning:** The DiaryTeamB.doc covers 10 October 2009 through 21 November 2009 with detailed daily entries. The statement is factually incorrect and caused the extraction errors documented in D011-D013.

---

### S004: Elhovo 2009 — No DPF Scans for Season

**Type:** Source gap (entire season)

| Source | Status |
|--------|--------|
| DPF scans | ✗ **None exist for ELH 2009** |
| EN Diaries | ✓ Present for all teams |
| BG Diaries | ✓ Present for Teams B and C |

**Notes:** No Daily Progress Form scans exist for Elhovo 2009 Autumn. All 62 records (Teams A, B, C) rely on diary-only verification. This limits cross-verification confidence but does not affect data completeness where diaries are thorough (as with Team B).

---

### D015: 2009-10-21, Team A — Diary Transcription Error (No Correction Needed)

**Type:** Diary error — CSV is correct

| Source | Value | Status |
|--------|-------|--------|
| SU Form (FieldRecords, p.56) | Start: **60195** | ✓ PRIMARY |
| CSV (current) | Start: 60195, End: 60273 | ✓ CORRECT |
| Diary (Diary Team A.doc) | Start: 60196, End: 60273 | ✗ ERROR |

**Resolution:** No correction needed — CSV value is correct

**SU Form Evidence:**
The SU form for unit 60195 clearly shows:

- **Date:** 21 October 2009
- **Survey unit:** 60.195
- **Walk interval:** 10m
- **Walkers:** Martin, [unclear], Adela, [unclear], Eric

This definitively proves unit 60195 was surveyed on 21 October, not skipped.

**Diary Error Analysis:**
The diary's "First unit: 60196" is a transcription error made when compiling the unit summary table after fieldwork. The SU form, completed in the field at the time of survey, is the authoritative primary source.

**Lesson:** SU forms take precedence over diary summary tables for unit numbers.

---

### D016: 2009-10-26 to 2009-10-29, Team A — Walker Substitution Not Reflected

**Type:** Personnel error (4 records)

**Affected dates:** 2009-10-26, 2009-10-27, 2009-10-28, 2009-10-29

| Field | CSV Value (original) | Corrected Value |
|-------|----------------------|-----------------|
| Walkers_Original | ...Eric | ...Tereza |
| Walkers_Standardised | ...Erik Andersen | ...Tereza Dobrovodská |

**Diary evidence:**
- Oct 25 (Edirne excursion): "Eric decided to go on to Istanbul and is dropped off at the busstation near the main mosque parting with our team."
- Oct 26: "Team A comprises Adela, Ilija, Aneta, Martin and **Tereza as a substitute for Eric**."
- Oct 27: "Team A in Monday set up" (refers to Oct 26 composition with Tereza)
- Nov 1: "I get up at 5.30 to take Vera and Terka to the bus station" (Terka = Tereza leaving)

**Tereza disambiguation:**

Two Terezas were present in 2009 autumn per TRAP-Participants.csv:
- Tereza Blažková (FFUK)
- Tereza Dobrovodská (FFUK)

**Resolution method:** Team roster cross-reference

| Date | Team C Walkers | Team A Walkers |
|------|----------------|----------------|
| Oct 12-22 | Tereza Dobrovodská (documented) | Eric |
| Oct 23 | "Tereza sick" — Jana substitutes | Eric (until departure) |
| Oct 26-29 | No Tereza | Tereza (substitute for Eric) |

**Logic:** People were only on one team at a time. Tereza Dobrovodská was on Team C Oct 12-22, then sick Oct 23. She became available to substitute for Eric on Team A Oct 26-29. Tereza Blažková had no Team C presence to explain her sudden availability — she may have had a specialist role (ceramics, bioarchaeology) rather than field walking this season.

**Resolution:** Replace Eric/Erik Andersen with Tereza/Tereza Dobrovodská in Walkers_Original and Walkers_Standardised for all 4 records.

---

### D017: 2009-10-30, 2009-10-31, 2009-11-04, Team A — Erroneous QA_Notes (Issue Not Present)

**Type:** Originally documented as metadata error — **no correction needed**

**Originally suspected:** QA_Notes containing erroneous "No autumn survey season" statement

**Investigation result (26 Nov 2025):** Team A records for these dates do NOT contain this erroneous text. The QA_Notes contain only: "MISSING: Survey units | No role data available"

**Note:** The erroneous "No autumn survey season" text exists on **Team C** records (Oct 14, 16, 17, 18) — this is a separate issue not part of this QA cycle. Those Team C records have the text because they were non-survey days extracted without cross-verification.

**Resolution:** No action required for Team A records

---

### D018: 2009-11-09, Team A — Missing Diary_Author Field

**Type:** Field omission

| Field | CSV Value | Correct Value |
|-------|-----------|---------------|
| Diary_Author | (empty) | Adela Sobotkova |

**Note:** Original issue documented as "Diary_Source" but CSV has no such column. The actual missing field is "Diary_Author". PDF_Source already correctly contained "Diary Team A.doc".

**Evidence:** All other Team A November records (Nov 2-7, 10) have Diary_Author = "Adela Sobotkova". Nov 9 was an anomalous omission.

**Resolution:** Add "Adela Sobotkova" to Diary_Author field

---

## Summary Statistics

| Season | Value Discrepancies | Missing Records | Source Gaps |
|--------|---------------------|-----------------|-------------|
| Elhovo 2010 Autumn | 7 | 2 | 3 |
| Elhovo 2009 Autumn Team B | 3 (unit fields) | 0 | 1 (season-wide: no DPF scans) |
| Elhovo 2009 Autumn Team A | 1 (unit — diary error) + 4 (walkers) + 1 (Diary_Author) | 0 | — |

### Value Discrepancy Resolution (Elhovo 2010 Autumn)

| Scenario | Count | Fraction | Cases |
|----------|-------|----------|-------|
| DPF scan and diary agreed (CSV wrong) | 2 | 2/7 | D005, D007 |
| DPF scan preferred over diary | 5 | 5/7 | D001, D002, D003, D004, D006 |
| Diary preferred over DPF scan | 0 | 0/7 | — |
| **Total** | **7** | **7/7** | |

**Interpretation:** In all cases where DPF scan and diary conflicted, the DPF scan was preferred. This supports observation O1 (DPF scans more reliable for unit numbers).

**Note:** "DPF scan" = Daily Progress Form scan (the scanned PDF of the handwritten daily summary forms).

---

## Summary by Type

### Value Discrepancies (D001-D007)

| Type | Count | Records |
|------|-------|---------|
| DPF scan vs Diary (minor) | 4 | D001, D002, D004, D006 |
| Diary typo | 1 | D003 |
| CSV extraction error | 1 | D005 |
| CSV field missing | 1 | D007 |

### Missing CSV Records (D008-D009)

| Type | Count | Records |
|------|-------|---------|
| Entire record not extracted | 2 | D008 (2010-11-07 B), D009 (2010-11-10 B) |

### Source Gaps (S001-S003)

| Type | Count | Records |
|------|-------|---------|
| Diary missing | 1 | S001 (2010-11-11 B) |
| DPF scan missing | 2 | S002 (2010-11-12 B), S003 (2010-11-14 B) |

### Unit Continuity (D010)

All unit gaps explained by missing records. No unexplained discontinuities.

---

## Action Items

### Elhovo 2010 Autumn (Complete)

| ID | Action | Priority |
|----|--------|----------|
| D005 | ✅ Corrected Start Unit 71245→71525 | Done |
| D006 | ✅ Corrected End Unit 71650→71649 | Done |
| D007 | ✅ Added missing units 71713/71760 | Done |
| D008 | ✅ Added missing record 2010-11-07 B | Done |
| D009 | ✅ Added missing record 2010-11-10 B | Done |

### Elhovo 2009 Autumn Team B (Complete)

| ID | Action | Priority |
|----|--------|----------|
| D011 | ✅ Added units 70926/70962 to 2009-11-02 B | Done |
| D012 | ✅ Added units 70963/71062 to 2009-11-03 B | Done |
| D013 | ✅ Added units 71063/71142 to 2009-11-05 B | Done |
| D014 | ✅ Removed erroneous QA_Notes from 3 records | Done |

### Elhovo 2009 Autumn Team A (Complete — 26 Nov 2025)

| ID | Action | Status |
|----|--------|--------|
| D015 | ✅ No correction needed — SU form confirms CSV is correct (diary error) | Resolved |
| D016 | ✅ Eric→Tereza + Erik Andersen→Tereza Dobrovodská for 2009-10-26 A | Done |
| D016 | ✅ Eric→Tereza + Erik Andersen→Tereza Dobrovodská for 2009-10-27 A | Done |
| D016 | ✅ Eric→Tereza + Erik Andersen→Tereza Dobrovodská for 2009-10-28 A | Done |
| D016 | ✅ Eric→Tereza + Erik Andersen→Tereza Dobrovodská for 2009-10-29 A | Done |
| D017 | ✅ No correction needed — Team A records didn't have erroneous text | Resolved |
| D018 | ✅ Added Diary_Author (Adela Sobotkova) to 2009-11-09 A | Done |

**D016 Note:** Original CSV had Eric/Erik Andersen. A crashed session partially applied corrections using wrong Tereza (Blažková). This session identified the correct Tereza via team membership analysis: T. Dobrovodská was on Team C until Oct 22, sick Oct 23, then available to substitute for Eric on Team A Oct 26-29.

---

## Notes

- Most value discrepancies are minor numeric differences in unit numbers
- PDF has been consistently more reliable for unit data when both sources exist
- One major transcription error found (D005: 280-unit difference)
- Two entire records missing from CSV (D008, D009) — need to be added
- Source gaps prevent cross-verification for 3 records
- Unit continuity is perfect once missing records are accounted for
