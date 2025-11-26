# QA Runsheet: Elhovo 2010 Autumn

**Date:** 25-26 November 2025
**Scope:** 16 records verified (5 Team A, 11 Team B including 2 missing records discovered)
**Status:** PILOT COMPLETE

---

## Source Documents Consulted

### Team A

| Type | File | Notes |
|------|------|-------|
| Diary | A_Diary.docx | Primary for roles; 5 dated entries |
| PDF | Day_03.pdf | Contains 3 forms: 22, 23, 24 Oct 2010 |
| PDF | Day_05.pdf | Contains 2 forms: 2, 3 Nov 2010 |

---

## Team A Verification Results

### Record 1: 2010-10-22, Team A

| Field | CSV Value | PDF Value | Diary Value | Status |
|-------|-----------|-----------|-------------|--------|
| Date | 2010-10-22 | 22 Oct 2010 | 22 October 2010 | CONFIRMED |
| Team | A | A | Team A | CONFIRMED |
| Start Unit | 61400 | 61400 | 61400 | CONFIRMED |
| End Unit | 61423 | 61423 | 61423 | CONFIRMED |
| Leader | Adéla Dorňáková | Adela D | Adela D | CONFIRMED |
| Walker count | 7 names (6 unique) | 6 | 6 | **DISCREPANCY** |
| PDA_Operator | Emma Jakobsson \| Adéla Dorňáková | — | Emma (PDA), Adela D (PDA) | CONFIRMED |
| GPS_Operator | Adela Sobotkova | — | Adela S (GPS) | CONFIRMED |
| Author | Adéla Dorňáková | Royce L | Adela Dornakova | CONFIRMED (diary author) |

**Walkers comparison:**

- **CSV Walkers_Original:** `Adela D. | AS | RL | PT | BW | EJ | AD`
- **CSV Walkers_Standardised:** `Adéla Dorňáková | Adela Sobotkova | Royce Lawrence | Petra Tušlová | Bara Weissová | Emma Jakobsson | Adéla Dorňáková`
- **PDF:** AS, BW, AD, EJ, RL, PT (6 walkers)
- **Diary:** Adela S (GPS), Royce, Petra, Bara, Emma (PDA), Adela D (PDA) — 6 walkers

**Rule checks:**

- R1 (Roles ⊆ Walkers): PASS — all role holders are walkers
- R2 (Leader ∈ Walkers): PASS — leader is in walker list

---

## QA Issue #1: 2010-10-22 Team A - Walkers_Standardised

**Study Area/Season:** Elhovo 2010 Autumn
**Record:** 2010-10-22, Team A
**Field:** Walkers_Standardised

**Current CSV value:** `Adéla Dorňáková | Adela Sobotkova | Royce Lawrence | Petra Tušlová | Bara Weissová | Emma Jakobsson | Adéla Dorňáková`

**Sources consulted:**

1. Day_03.pdf — Form 1 (22 Oct 2010)
2. A_Diary.docx — 22 October 2010 entry

**Source evidence:**

- PDF: Walkers field shows "AS, BW, AD, EJ, RL, PT" (6 initials)
- Diary: "No. of walkers: 6 – Adela S (GPS), Royce, Petra, Bara, Emma (PDA), Adela D (PDA)"

**Finding:** DISCREPANCY
**Recommended value:**

- English: `Adéla Dorňáková | Adela Sobotkova | Royce Lawrence | Petra Tušlová | Bara Weissová | Emma Jakobsson`

**Reasoning:**
Both PDF and diary confirm 6 walkers. The CSV has 7 entries with "Adéla Dorňáková" appearing twice. This appears to be a systematic extraction error where the leader was appended to the walker list even though already present.

---

**User Decision:** [ ] Accept / [X] Modify: De-duplicate entire 'Walkers_Standardised' column in the CSV; each walker should appear only once in each record in this column.

---

### Record 2: 2010-10-23, Team A

| Field | CSV Value | PDF Value | Diary Value | Status |
|-------|-----------|-----------|-------------|--------|
| Date | 2010-10-23 | 23 Oct 2010 | 23 October 2010 | CONFIRMED |
| Team | A | A | Team A | CONFIRMED |
| Start Unit | 61424 | 61424 | 61425 | CONFIRMED (PDF primary) |
| End Unit | 61475 | 61475 | 61473 | CONFIRMED (PDF primary) |
| Leader | Adéla Dorňáková | Adela D | Adela D | CONFIRMED |
| Walker count | 6 names (5 unique) | 5 | 5 | **DISCREPANCY** |
| Author | Viktorie Chystyaková | Royce L | Viktoria Chystyakova | CONFIRMED (diary author) |

**Walkers comparison:**

- **CSV Walkers_Standardised:** `Adéla Dorňáková | Adela Sobotkova | Royce Lawrence | Viktorie Chystyaková | Emma Jakobsson | Adéla Dorňáková`
- **PDF:** AD, RL, AS, EJ, VC (5 walkers)
- **Diary:** Adela S (GPS), Royce, Viktoria, Emma (PDA), Adela D (PDA) — 5 walkers

**Rule checks:**

- R1: PASS
- R2: PASS

---

## QA Issue #2: 2010-10-23 Team A - Walkers_Standardised

**Study Area/Season:** Elhovo 2010 Autumn
**Record:** 2010-10-23, Team A
**Field:** Walkers_Standardised

**Current CSV value:** `Adéla Dorňáková | Adela Sobotkova | Royce Lawrence | Viktorie Chystyaková | Emma Jakobsson | Adéla Dorňáková`

**Sources consulted:**

1. Day_03.pdf — Form 2 (23 Oct 2010)
2. A_Diary.docx — 23 October 2010 entry

**Source evidence:**

- PDF: Walkers field shows "AD, RL, AS, EJ, VC" (5 initials)
- Diary: "No. of walkers: 5 – Adela S (GPS), Royce, Viktoria, Emma (PDA), Adela D (PDA)"

**Finding:** DISCREPANCY
**Recommended value:**

- English: `Adéla Dorňáková | Adela Sobotkova | Royce Lawrence | Viktorie Chystyaková | Emma Jakobsson`

**Reasoning:**
Both PDF and diary confirm 5 walkers. CSV has duplicate "Adéla Dorňáková" entry.

---

**User Decision:** [ ] Accept / [ ] Modify: _______________

---

### Record 3: 2010-10-24, Team A

| Field | CSV Value | PDF Value | Diary Value | Status |
|-------|-----------|-----------|-------------|--------|
| Date | 2010-10-24 | 24 Oct 2010 | 24 October 2010 | CONFIRMED |
| Team | A | A | Team A | CONFIRMED |
| Start Unit | 61476 | 61476 | 61476 | CONFIRMED |
| End Unit | 61549 | 61549 | 61349 (typo) | CONFIRMED |
| Leader | Adéla Dorňáková | Adela D | Adela D | CONFIRMED |
| Walker count | 6 names (5 unique) | 5 | 5 | **DISCREPANCY** |
| Author | Viktorie Chystyaková | Royce L | Viktoria Chystyakova | CONFIRMED (diary author) |

**Walkers comparison:**

- **CSV Walkers_Standardised:** `Adéla Dorňáková | Adela Sobotkova | Royce Lawrence | Viktorie Chystyaková | Emma Jakobsson | Adéla Dorňáková`
- **PDF:** AS, RL, AD, VC, EJ (5 walkers)
- **Diary:** Adela S (GPS), Royce, Viktoira, Emma (PDA), Adela D (PDA) — 5 walkers

**Note:** Diary shows "Last unit: 61349" which is clearly a typo (should be 61549). PDF confirms 61549.

**Rule checks:**

- R1: PASS
- R2: PASS

---

## QA Issue #3: 2010-10-24 Team A - Walkers_Standardised

**Study Area/Season:** Elhovo 2010 Autumn
**Record:** 2010-10-24, Team A
**Field:** Walkers_Standardised

**Current CSV value:** `Adéla Dorňáková | Adela Sobotkova | Royce Lawrence | Viktorie Chystyaková | Emma Jakobsson | Adéla Dorňáková`

**Sources consulted:**

1. Day_03.pdf — Form 3 (24 Oct 2010)
2. A_Diary.docx — 24 October 2010 entry

**Source evidence:**

- PDF: Walkers field shows "AS, RL, AD, VC, EJ" (5 initials)
- Diary: "No. of walkers: 5 – Adela S (GPS), Royce, Viktoira, Emma (PDA), Adela D (PDA)"

**Finding:** DISCREPANCY
**Recommended value:**

- English: `Adéla Dorňáková | Adela Sobotkova | Royce Lawrence | Viktorie Chystyaková | Emma Jakobsson`

**Reasoning:**
Both PDF and diary confirm 5 walkers. CSV has duplicate "Adéla Dorňáková" entry.

---

**User Decision:** [ ] Accept / [ ] Modify: _______________

---

### Record 4: 2010-11-02, Team A

| Field | CSV Value | PDF Value | Diary Value | Status |
|-------|-----------|-----------|-------------|--------|
| Date | 2010-11-02 | 02 Nov 2010 | 2nd of November 2010 | CONFIRMED |
| Team | A | A | Team A | CONFIRMED |
| Start Unit | 61549 | 61549 | 61553 | CONFIRMED (PDF primary) |
| End Unit | 61586 | 61586 | 61586 | CONFIRMED |
| Leader | Petra Tušlová | Petra T. | Petra | CONFIRMED |
| Walker count | 6 names (5 unique) | 5 | 5 | **DISCREPANCY** |
| PDA_Operator | Petra Tušlová | — | PDA: Petra | CONFIRMED |
| GPS_Operator | Adela Sobotkova | — | GPS: Adéla | CONFIRMED |
| Author | Bara Weissová | Drago G | Bara W. | CONFIRMED (diary author) |

**Walkers comparison:**

- **CSV Walkers_Standardised:** `Petra Tušlová | Adela Sobotkova | Petra Tušlová | Dragomir Garbov | Bara Weissová | Emma Jakobsson`
- **PDF:** Walkers: "Adela, Emma, Drago, Bara" + Leader Petra = 5
- **Diary:** "No. of Walkers: 5 - Adela S., Petra T., Drago, Bara, Emma"

**Note:** Diary says "First unit: 61553" but unit sample list includes 61549. PDF confirms Start Unit 61549.

**Rule checks:**

- R1: PASS
- R2: PASS

---

## QA Issue #4: 2010-11-02 Team A - Walkers_Standardised

**Study Area/Season:** Elhovo 2010 Autumn
**Record:** 2010-11-02, Team A
**Field:** Walkers_Standardised

**Current CSV value:** `Petra Tušlová | Adela Sobotkova | Petra Tušlová | Dragomir Garbov | Bara Weissová | Emma Jakobsson`

**Sources consulted:**

1. Day_05.pdf — Form 1 (02 Nov 2010)
2. A_Diary.docx — 2nd of November 2010 entry

**Source evidence:**

- PDF: Walkers field shows "Adela, Emma, Drago, Bara" with Leader "Petra T." (5 total)
- Diary: "No. of Walkers: 5 - Adela S., Petra T., Drago, Bara, Emma"

**Finding:** DISCREPANCY
**Recommended value:**

- English: `Petra Tušlová | Adela Sobotkova | Dragomir Garbov | Bara Weissová | Emma Jakobsson`

**Reasoning:**
Both PDF and diary confirm 5 walkers. CSV has "Petra Tušlová" appearing twice.

---

**User Decision:** [ ] Accept / [ ] Modify: _______________

---

### Record 5: 2010-11-03, Team A

| Field | CSV Value | PDF Value | Diary Value | Status |
|-------|-----------|-----------|-------------|--------|
| Date | 2010-11-03 | 3 Nov 2010 | 3 November 2010 | CONFIRMED |
| Team | A | A | Team A | CONFIRMED |
| Start Unit | 61587 | 61587 | 61587 | CONFIRMED |
| End Unit | 61643 | 61643 | 61643 | CONFIRMED |
| Leader | Petra Tušlová | Petra | Petra | CONFIRMED |
| Walker count | 6 names (5 unique) | 5 | 5 | **DISCREPANCY** |
| PDA_Operator | Petra Tušlová | — | PDA: Petra | CONFIRMED |
| GPS_Operator | Adela Sobotkova | — | GPS: Adéla | CONFIRMED |
| Author | Petra Tušlová | Emma J. | Petra T. | CONFIRMED (diary author) |

**Walkers comparison:**

- **CSV Walkers_Standardised:** `Petra Tušlová | Adela Sobotkova | Viktorie Chystyaková | Dragomir Garbov | Emma Jakobsson | Petra Tušlová`
- **PDF:** Walkers: "Petra, Vicky, Drago, Adela, Emma" (5 walkers)
- **Diary:** "No. of walkers: 5 – Adéla S., Viki, Drago, Emma, Petra T."

**Rule checks:**

- R1: PASS
- R2: PASS

---

## QA Issue #5: 2010-11-03 Team A - Walkers_Standardised

**Study Area/Season:** Elhovo 2010 Autumn
**Record:** 2010-11-03, Team A
**Field:** Walkers_Standardised

**Current CSV value:** `Petra Tušlová | Adela Sobotkova | Viktorie Chystyaková | Dragomir Garbov | Emma Jakobsson | Petra Tušlová`

**Sources consulted:**

1. Day_05.pdf — Form 2 (3 Nov 2010)
2. A_Diary.docx — 3 November 2010 entry

**Source evidence:**

- PDF: Walkers field shows "Petra, Vicky, Drago, Adela, Emma" (5 names)
- Diary: "No. of walkers: 5 – Adéla S., Viki, Drago, Emma, Petra T."

**Finding:** DISCREPANCY
**Recommended value:**

- English: `Petra Tušlová | Adela Sobotkova | Viktorie Chystyaková | Dragomir Garbov | Emma Jakobsson`

**Reasoning:**
Both PDF and diary confirm 5 walkers. CSV has "Petra Tušlová" appearing twice.

---

**User Decision:** [ ] Accept / [ ] Modify: _______________

---

## Team A Summary

| Metric | Count |
|--------|-------|
| Records checked | 5 |
| Fields verified per record | ~10 |
| Issues found | 5 |
| Recommended corrections | 5 |
| Source gaps documented | 0 |

### Issues by Category

- **Duplicate walker entries:** 5 (all records affected)
- Name errors: 0
- Unit errors: 0
- Role errors: 0
- Other: 0

### Systematic Issue Identified

**All 5 Team A records have the same issue:** The leader's name appears twice in `Walkers_Standardised`. This is likely a systematic extraction bug where the leader was appended to the walker list even when already present.

**Pattern:**

- Records 1-3 (Oct 22-24): Adéla Dorňáková appears twice
- Records 4-5 (Nov 2-3): Petra Tušlová appears twice

This suggests a fix could be applied programmatically across all affected records.

---

## Rules & Heuristics Applied

### Rules Checked

| Rule | Result |
|------|--------|
| R1: Roles ⊆ Walkers | PASS (all 5 records) |
| R2: Leader ∈ Walkers | PASS (all 5 records) |

### Heuristics Used

- H1 (Team stability): Confirmed — Team A composition was stable within each leadership period
- H2 (One team per day): Not needed for Team A verification

### New Observations

**O1: PDF vs Diary discrepancies in unit numbers**
- Diary occasionally has typos in unit numbers (e.g., 61349 vs 61549)
- PDF daily progress forms are more reliable for unit ranges
- This confirms PDF should be PRIMARY for basic numeric data

**O2: Author field interpretation**
- CSV "Author" field = diary entry author (who wrote the narrative)
- PDF "Author" field = form filler (who completed the daily progress form)
- These are often different people; CSV correctly captures diary author

---

## Team B Verification Results

### Source Documents Consulted

| Type | File | Dates Covered |
|------|------|---------------|
| Diary | Team B Diary new.docx | 2-7, 10, 12, 14-16 Nov 2010 |
| PDF | Day_02.pdf | 2-3 Nov 2010 |
| PDF | Day_04.pdf | 4-5 Nov 2010 |
| PDF | Day_06.pdf | 6-7 Nov 2010 |
| PDF | Day_08.pdf | 10-11 Nov 2010 |
| PDF | Day_12.pdf | 15-16 Nov 2010 |

---

### Record 6: 2010-11-02, Team B

| Field | CSV Value | PDF Value | Diary Value | Status |
|-------|-----------|-----------|-------------|--------|
| Date | 2010-11-02 | 2 Nov 2010 | 2 November 2010 | CONFIRMED |
| Team | B | B | Team B | CONFIRMED |
| Start Unit | 71470 | 71470 | 71470 | CONFIRMED |
| End Unit | 71524 | 71524 | 71524 | CONFIRMED |
| Leader | Shawn Ross | Dr Ross | Dr. Ross | CONFIRMED |
| Walkers | 5 unique | 5 (VC, RL, DR, KL, AP) | 5 | CONFIRMED |

**Rule checks:** R1 PASS, R2 PASS

---

### Record 7: 2010-11-03, Team B

| Field | CSV Value | PDF Value | Diary Value | Status |
|-------|-----------|-----------|-------------|--------|
| Date | 2010-11-03 | 3 Nov 2010 | 3 November 2010 | CONFIRMED |
| Start Unit | **71245** | **71525** | 71525 | **DISCREPANCY** |
| End Unit | 71583 | 71583 | 71567 | CONFIRMED (PDF primary) |
| Leader | Shawn Ross | Dr Ross | Dr. Ross | CONFIRMED |

---

## QA Issue #6: 2010-11-03 Team B - Start Unit

**Problem:** CSV Start Unit (71245) does not match PDF (71525) — difference of 280 units.

**Fix:** Change Start Unit from 71245 to 71525.

**Sources consulted:**

1. Day_02.pdf — Form 2 (3 Nov 2010): Start Unit clearly shows "71525"
2. Team B Diary new.docx: "Start Unit: 71525"

**Finding:** DISCREPANCY
**Recommended value:** 71525

**Reasoning:**
Both PDF and diary agree on 71525. The CSV value 71245 appears to be a transcription error (possibly digit transposition or OCR error from original extraction).

---

**User Decision:** [X] Accept / [ ] Modify: _______________

---

### Record 8: 2010-11-04, Team B

| Field | CSV Value | PDF Value | Diary Value | Status |
|-------|-----------|-----------|-------------|--------|
| Date | 2010-11-04 | 4 Nov 2010 | 4 November 2010 | CONFIRMED |
| Start Unit | 71584 | 71584 | 71584 | CONFIRMED |
| End Unit | **71650** | **71649** | 71650 | **DISCREPANCY** |
| Leader | Shawn Ross | Dr Ross | Dr. Ross | CONFIRMED |

---

## QA Issue #7: 2010-11-04 Team B - End Unit

**Problem:** CSV End Unit (71650) does not match PDF (71649) — off by 1 unit.

**Fix:** Change End Unit from 71650 to 71649.

**Sources consulted:**

1. Day_04.pdf — Form 1 (4 Nov 2010): End Unit clearly shows "71649"
2. Team B Diary new.docx: "End Unit: 71650"

**Finding:** DISCREPANCY (PDF vs Diary conflict)
**Recommended value:** 71649 (PDF is PRIMARY for unit numbers per O1)

**Reasoning:**
PDF shows 71649, diary shows 71650. Per source priority rules, PDF takes precedence for basic numeric data. Note: 71650 is the Start Unit for the next day (5 Nov), suggesting the diary may have copied forward incorrectly.

---

**User Decision:** [X] Accept / [ ] Modify: _______________

---

### Record 9: 2010-11-05, Team B

| Field | CSV Value | PDF Value | Diary Value | Status |
|-------|-----------|-----------|-------------|--------|
| Date | 2010-11-05 | 5 Nov 2010 | 5 November 2010 | CONFIRMED |
| Start Unit | 71650 | 71650 | 71650 | CONFIRMED |
| End Unit | 71712 | 71712 | 71712 | CONFIRMED |
| Leader | Shawn Ross | Dr Ross | Dr. Ross | CONFIRMED |

**Rule checks:** R1 PASS, R2 PASS — No issues found.

---

### Record 10: 2010-11-06, Team B

| Field | CSV Value | PDF Value | Diary Value | Status |
|-------|-----------|-----------|-------------|--------|
| Date | 2010-11-06 | 6 Nov 2010 | 6 November 2010 | CONFIRMED |
| Start Unit | **(empty)** | **71713** | 71713 | **MISSING** |
| End Unit | **(empty)** | **71760** | 71760 | **MISSING** |
| Leader | Shawn Ross \| Royce Lawrence | Dr Ross | Dr. Ross training Royce | CONFIRMED |

---

## QA Issue #8: 2010-11-06 Team B - Missing Unit Range

**Problem:** CSV has no Start/End Unit values, but PDF and diary both have data.

**Fix:** Add Start Unit = 71713, End Unit = 71760.

**Sources consulted:**

1. Day_06.pdf — Form 1 (6 Nov 2010): Start 71713, End 71760
2. Team B Diary new.docx: "Start Unit: 71713, End Unit: 71760"

**Finding:** SOURCE GAP (data exists but wasn't extracted)
**Recommended values:**

- Start Unit: 71713
- End Unit: 71760

**Reasoning:**
Both sources agree. The QA_Notes field already flags this: "MISSING: Survey units - check Excel SurveySummary". The data is available in both PDF and diary.

---

**User Decision:** [X] Accept / [ ] Modify: _______________

---

---

## QA Issue #9: 2010-11-07 Team B - Missing Record (MAJOR)

**Problem:** Entire record missing from CSV despite both PDF and diary having data.

**Fix:** Add new record with units 71761-71800.

**Sources consulted:**

1. Day_06.pdf — Form 2 (7 Nov 2010): Units 71761-71800, Leader SAR/R.L
2. Team B Diary new.docx — "7 November 2010, Kimberley Lowe"

**Finding:** MISSING RECORD
**Action:** Record added to attribution.csv

**Data added:**

- Date: 2010-11-07
- Team: B
- Start Unit: 71761
- End Unit: 71800
- Leader: Shawn Ross | Royce Lawrence
- Walkers: Shawn Ross, Kimberley Lowe, Royce Lawrence, Alina Petanec, Julia Paulová

---

**User Decision:** [X] Accept (applied)

---

## QA Issue #10: 2010-11-10 Team B - Missing Record (MAJOR)

**Problem:** Entire record missing from CSV despite both PDF and diary having data.

**Fix:** Add new record with units 71801-71833.

**Sources consulted:**

1. Day_08.pdf — Form 1 (10 Nov 2010): Units 71801-71833, Leader R.L
2. Team B Diary new.docx — "10 November 2010, Kimberley Lowe"

**Finding:** MISSING RECORD
**Action:** Record added to attribution.csv

**Data added:**

- Date: 2010-11-10
- Team: B
- Start Unit: 71801
- End Unit: 71833
- Leader: Royce Lawrence
- Walkers: Kimberley Lowe, Emma Jakobsson, Royce Lawrence, Julia Paulová, Ashley Chee-Quee, Dragomir Garbov

---

**User Decision:** [X] Accept (applied)

---

### Record 11: 2010-11-11, Team B

| Field | CSV Value | PDF Value | Diary Value | Status |
|-------|-----------|-----------|-------------|--------|
| Date | 2010-11-11 | 11 Nov 2010 | — | CONFIRMED |
| Start Unit | 71834 | 71834 | — | CONFIRMED |
| End Unit | 71909 | 71909 | — | CONFIRMED |
| Leader | Royce Lawrence | Royce | — | CONFIRMED |

**Note:** No diary entry found for 11 Nov. CSV was extracted from Day_08.pdf Form 2.

**Rule checks:** R1 PASS, R2 PASS — No issues found.

---

### Record 12: 2010-11-12, Team B

| Field | CSV Value | PDF Value | Diary Value | Status |
|-------|-----------|-----------|-------------|--------|
| Date | 2010-11-12 | — | 12 November 2010 | CONFIRMED |
| Start Unit | 71910 | — | 71910 | CONFIRMED |
| End Unit | 71980 | — | 71980 | CONFIRMED |
| Leader | Royce Lawrence | — | Royce Lawrence | CONFIRMED |

**Note:** No PDF form found for 12 Nov. CSV was extracted from diary.

**Rule checks:** R1 PASS, R2 PASS — No issues found.

---

### Record 13: 2010-11-14, Team B

| Field | CSV Value | PDF Value | Diary Value | Status |
|-------|-----------|-----------|-------------|--------|
| Date | 2010-11-14 | — | 14 November 2010 | CONFIRMED |
| Start Unit | 71981 | — | 71981 | CONFIRMED |
| End Unit | 72024 | — | 72024 | CONFIRMED |
| Leader | Royce Lawrence | — | Royce Lawrence | CONFIRMED |

**Note:** No PDF form found for 14 Nov. CSV was extracted from diary.

**Rule checks:** R1 PASS, R2 PASS — No issues found.

---

### Record 14: 2010-11-15, Team B

| Field | CSV Value | PDF Value | Diary Value | Status |
|-------|-----------|-----------|-------------|--------|
| Date | 2010-11-15 | 15 Nov 2010 | 15 November 2010 | CONFIRMED |
| Start Unit | 72025 | 72025 | 72025 | CONFIRMED |
| End Unit | 72087 | 72087 | 72087 | CONFIRMED |
| Leader | Petra Tušlová | Petra | Petra | CONFIRMED |

**Rule checks:** R1 PASS, R2 PASS — No issues found.

---

## Team B Summary

| Metric | Count |
|--------|-------|
| Records checked | 9 |
| Issues found | 3 |
| Recommended corrections | 3 |

### Issues by Category

- **Unit errors:** 3 (Issues #6, #7, #8)
- Name errors: 0
- Role errors: 0
- Walker duplicates: 0 (already fixed globally)

---

## Source Coverage Matrix

Comprehensive record of which sources were available for each record:

### Team A Source Coverage

| Date | PDF Form | Primary Diary | Secondary Diary | Notes |
|------|----------|---------------|-----------------|-------|
| 2010-10-22 | ✓ Day_03.pdf | ✓ A_Diary.docx | N/A | Both sources present |
| 2010-10-23 | ✓ Day_03.pdf | ✓ A_Diary.docx | N/A | Both sources present |
| 2010-10-24 | ✓ Day_03.pdf | ✓ A_Diary.docx | N/A | Both sources present |
| 2010-11-02 | ✓ Day_05.pdf | ✓ A_Diary.docx | N/A | Both sources present |
| 2010-11-03 | ✓ Day_05.pdf | ✓ A_Diary.docx | N/A | Both sources present |

### Team B Source Coverage

| Date | PDF Form | Primary Diary | Secondary Diary | CSV Status | Notes |
|------|----------|---------------|-----------------|------------|-------|
| 2010-11-02 | ✓ Day_02.pdf | ✓ Team B Diary new.docx | Not checked | ✓ Present | Both sources present |
| 2010-11-03 | ✓ Day_02.pdf | ✓ Team B Diary new.docx | Not checked | ✓ Present | Both sources present |
| 2010-11-04 | ✓ Day_04.pdf | ✓ Team B Diary new.docx | Not checked | ✓ Present | Both sources present |
| 2010-11-05 | ✓ Day_04.pdf | ✓ Team B Diary new.docx | Not checked | ✓ Present | Both sources present |
| 2010-11-06 | ✓ Day_06.pdf | ✓ Team B Diary new.docx | Not checked | ✓ Present | Both sources present |
| 2010-11-07 | ✓ Day_06.pdf | ✓ Team B Diary new.docx | ✓ Present | ✓ **Added** | **Was missing from CSV** |
| 2010-11-10 | ✓ Day_08.pdf | ✓ Team B Diary new.docx | ✓ Present | ✓ **Added** | **Was missing from CSV** |
| 2010-11-11 | ✓ Day_08.pdf | ✗ MISSING | ✗ MISSING | ✓ Present | **Diary gap** - both diaries skip 11 Nov |
| 2010-11-12 | ✗ MISSING | ✓ Team B Diary new.docx | ✓ Present | ✓ Present | **PDF gap** - no form for 12 Nov |
| 2010-11-14 | ✗ MISSING | ✓ Team B Diary new.docx | ✓ Present | ✓ Present | **PDF gap** - no form for 14 Nov |
| 2010-11-15 | ✓ Day_12.pdf | ✓ Team B Diary new.docx | ✓ Present | ✓ Present | Both sources present |

### Source Gap Summary

| Gap Type | Count | Records Affected |
|----------|-------|------------------|
| PDF Missing | 2 | 2010-11-12 B, 2010-11-14 B |
| Diary Missing | 1 | 2010-11-11 B |
| Both Missing | 0 | — |

---

## Unit Continuity Check

Cross-check of unit number continuity between consecutive days:

### Team A Continuity

| Day N-1 End | Day N Start | Gap/Overlap | Status |
|-------------|-------------|-------------|--------|
| — | 61400 | — | First day |
| 61423 | 61424 | +1 | ✓ Continuous |
| 61475 | 61476 | +1 | ✓ Continuous |
| 61549 | 61549 | 0 | ✓ Overlap (same unit) |
| 61586 | 61587 | +1 | ✓ Continuous |

### Team B Continuity (after corrections)

| Date | End Unit | Next Date | Start Unit | Gap | Status |
|------|----------|-----------|------------|-----|--------|
| 2 Nov | 71524 | 3 Nov | 71525 | +1 | ✓ Continuous |
| 3 Nov | 71583 | 4 Nov | 71584 | +1 | ✓ Continuous |
| 4 Nov | 71649 | 5 Nov | 71650 | +1 | ✓ Continuous |
| 5 Nov | 71712 | 6 Nov | 71713 | +1 | ✓ Continuous |
| 6 Nov | 71760 | 7 Nov | 71761 | +1 | ✓ Continuous |
| 7 Nov | 71800 | 10 Nov | 71801 | +1 | ✓ Continuous |
| 10 Nov | 71833 | 11 Nov | 71834 | +1 | ✓ Continuous |
| 11 Nov | 71909 | 12 Nov | 71910 | +1 | ✓ Continuous |
| 12 Nov | 71980 | 14 Nov | 71981 | +1 | ✓ Continuous |
| 14 Nov | 72024 | 15 Nov | 72025 | +1 | ✓ Continuous |

**Note:** All unit continuity gaps now resolved after adding missing records for 7 Nov and 10 Nov.

---

## Combined Summary: Elhovo 2010 Autumn QA

| Metric | Team A | Team B | Total |
|--------|--------|--------|-------|
| Records checked | 5 | 9 (+2 missing) | 16 |
| Issues found | 5 | 5 | 10 |
| MAJOR corrections | 0 | 5 | 5 |
| Minor corrections | 5 (walker dedup) | 0 | 5 |
| All corrections applied | ✓ | ✓ | ✓ |

### Issues by Severity

| Severity | Count | Issues |
|----------|-------|--------|
| **MAJOR** | 5 | #6 (unit), #7 (unit), #8 (unit), #9 (missing record), #10 (missing record) |
| Minor | 5 | #1-5 (walker duplicates) |

### All Corrections Applied

| Issue | Record | Field | Before | After |
|-------|--------|-------|--------|-------|
| #1-5 | Team A (all) | Walkers_Standardised | Duplicates | De-duplicated |
| #6 | 2010-11-03 B | Start Unit | 71245 | 71525 |
| #7 | 2010-11-04 B | End Unit | 71650 | 71649 |
| #8 | 2010-11-06 B | Start/End Unit | (empty) | 71713 / 71760 |
| #9 | 2010-11-07 B | Entire record | MISSING | Added |
| #10 | 2010-11-10 B | Entire record | MISSING | Added |

---

## Completion Status

1. [x] Team A verification complete
2. [x] Walker de-duplication applied (77 records fixed)
3. [x] Team B verification complete
4. [x] User review of QA Issues #6-10 — All accepted
5. [x] Apply accepted corrections to CSV — Done
6. [x] Update discrepancies log — Done
7. [x] Add missing records (D008, D009) — Done

**Pilot Status:** COMPLETE

**Final CSV record count:** 270 records (was 268, added 2 missing records)
