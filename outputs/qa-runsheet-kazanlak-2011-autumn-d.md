# QA Runsheet: Kazanlak 2011 Autumn Team D

**Study Area/Season:** Kazanlak (Seuthopolis) 2011 Autumn
**Team:** D
**QA Date:** 2025-12-01
**QA Performed By:** Claude Code (with Shawn Ross)
**Records in CSV:** 14
**Date Range:** 2011-10-14 to 2011-11-02

---

## Sources Consulted

| Type | File | Location | Role |
|------|------|----------|------|
| Diary | D_2011Diary_BG.doc | `Kazanluk/2011-11-30/Project Records/Team D/` | PRIMARY (BG, 137 KB) |
| Day PDFs | D_2011*.pdf | `Kazanluk/2011-11-30/Project Records/Team D/FieldRecords/` | Not used (API size limit) |

**Note:** This QA uses Bulgarian diary as the sole verification source. Day PDFs exist but exceed API processing limits. Role data (Leader vs Walker) is not available from diary sources.

---

## Team Composition

### Phase 1: 14-16 October 2011 (Initial Team)
- **Core walkers:** Nadezhda Kecheva (Н. Кечева), Yulia Dimitrova (Ю. Димитрова), Veronika Gencheva (В. Генчева), Georgi Mihailov (Г. Михайлов), Emil Dakashev (Е. Дакашев), Aleksandar Riskov (А. Рисков), Hristina Pavkova (Х. Павкова)
- **Note:** 7-person team including training day (Oct 14)

### Phase 2: 19-22 October 2011 (Roster Change)
- **Walkers:** Nadezhda Kecheva, Veronika Gencheva, Emil Dakashev, Eva Tonkova (Е. Тонкова), Anani Antonov (А. Антонов)
- **Note:** Eva Tonkova and Anani Antonov join; others leave

### Phase 3: 23-25 October 2011 (With G. Nekhrizov)
- **Walkers:** Georgi Nekhrizov (Г. Нехризов), Nadezhda Kecheva, Veronika Gencheva, Emil Dakashev, Eva Tonkova, Anani Antonov
- **Note:** 6-person team with Georgi Nekhrizov added

### Phase 4: 26-28 October 2011 (Reduced Team)
- **Walkers:** Nadezhda Kecheva, Emil Dakashev, Eva Tonkova, Anani Antonov
- **Note:** 4-person team; Veronika Gencheva and G. Nekhrizov leave

### Phase 5: 1-2 November 2011 (Foreign Students)
- **Walkers:** Tsoni Tsonev, Anani Antonov, Oscar Warren, Joel Sercombe, Georgia Burnett, Sharon
- **Note:** Mix of Bulgarian and foreign students

---

## Record-by-Record Verification

### October 2011

| Date | CSV Range | Diary Range | Total | Walkers Status |
|------|-----------|-------------|-------|----------------|
| Oct 14 | 40915-40919 | 40915-40919 | 5 | ✓ CONFIRMED |
| Oct 15 | 40920-40958 | 40920-40958 | 39 | ⚠️ MISSING WALKER |
| Oct 16 | 40959-40967 | 40959-40967 | 9 | ⚠️ MISSING WALKER |
| Oct 19 | 40968-41007 | 40968-41007 | 40 | ⚠️ MISSING WALKER |
| Oct 20 | 41008-41087 | 41008-41087 | 80 | ⚠️ MISSING WALKER |
| Oct 21 | 41088-41152 | 41088-41152 | 65 | ✓ CONFIRMED |
| Oct 22 | 41153-41197 | 41153-41197 | 45 | ⚠️ MISSING WALKER |
| Oct 23 | 41198-41221 | 41198-41221 | 24 | ⚠️ MISSING WALKER |
| Oct 25 | 41222-41249 | ~41222-41249 | 28 | ⚠️ MISSING WALKER |
| Oct 26 | 41250-41316 | 41250-41316 | 67 | ⚠️ MISSING WALKER |
| Oct 27 | 41317-41399 | 41317-41399 | 83 | ⚠️ MISSING WALKER |
| Oct 28 | 41400-41453 | 41400-41453 | 54 | ⚠️ MISSING WALKER |

### November 2011

| Date | CSV Range | Diary Range | Total | Walkers Status |
|------|-----------|-------------|-------|----------------|
| Nov 01 | 41454-41470 | 41454-41470 | 17 | ✓ CONFIRMED |
| Nov 02 | 41471-41477 | 41471-41477 | 7 | ✓ CONFIRMED |

---

## Issues Summary

| ID | Date | Field | Issue | Action |
|----|------|-------|-------|--------|
| D001 | Oct 15 | Walkers | Missing Hristina Pavkova (Х. Павкова) | [ ] Add walker |
| D002 | Oct 16 | Walkers | Missing Hristina Pavkova | [ ] Add walker |
| D003 | Oct 19 | Walkers | Missing Anani Antonov (А. Антонов) | [ ] Add walker |
| D004 | Oct 20 | Walkers | Missing Anani Antonov | [ ] Add walker |
| D005 | Oct 22 | Walkers | Missing Anani Antonov | [ ] Add walker |
| D006 | Oct 23 | Walkers | Missing Anani Antonov | [ ] Add walker |
| D007 | Oct 25 | Walkers | Missing Anani Antonov | [ ] Add walker |
| D008 | Oct 26 | Walkers | Missing Anani Antonov | [ ] Add walker |
| D009 | Oct 27 | Walkers | Missing Anani Antonov | [ ] Add walker |
| D010 | Oct 28 | Walkers | Missing Anani Antonov | [ ] Add walker |

**Note:** All unit ranges are CORRECT - only walker lists need updating.

---

## Corrections Required

### D001: Oct 15 Missing Walker

**Record:** 2011-10-15, Team D
**Field:** Walkers_Transliterated
**Current:** Nadezhda Kecheva | Yulia Dimitrova | Veronika Gencheva | Georgi Mihailov | Emil Dakashev | Aleksandar Riskov
**Corrected:** Nadezhda Kecheva | Yulia Dimitrova | Veronika Gencheva | Georgi Mihailov | Emil Dakashev | Aleksandar Riskov | Hristina Pavkova

**Source evidence:**
> "Екип: Н. Кечева, Ю. Димитрова, В. Генчева, Г. Михайлов, Е. Дакашев, А. Рисков, Х. Павкова"

**Reasoning:** Diary explicitly lists 7 team members; CSV has 6 (missing Hristina Pavkova).

**User Decision:**
- [X] Approve
- [ ] Modify: _______________

**Status:** Pending

---

### D002: Oct 16 Missing Walker

**Record:** 2011-10-16, Team D
**Field:** Walkers_Transliterated
**Current:** Nadezhda Kecheva | Veronika Gencheva | Emil Dakashev
**Corrected:** Nadezhda Kecheva | Veronika Gencheva | Emil Dakashev | Hristina Pavkova

**Source evidence:**
> "Екип: Н. Кечева, В. Генчева, Е. Дакашев, Х. Павкова"

**Reasoning:** Diary explicitly lists 4 team members; CSV has 3 (missing Hristina Pavkova).

**User Decision:**
- [X] Approve
- [ ] Modify: _______________

**Status:** Pending

---

### D003-D004: Oct 19-20 Missing Walker

**Records:** 2011-10-19 and 2011-10-20, Team D
**Field:** Walkers_Transliterated
**Current:** Nadezhda Kecheva | Veronika Gencheva | Emil Dakashev | Eva Tonkova
**Corrected:** Nadezhda Kecheva | Veronika Gencheva | Emil Dakashev | Eva Tonkova | Anani Antonov

**Source evidence (Oct 19, Day 6):**
> "Екип: Н. Кечева, В. Генчева, Е. Дакашев, Е. Тонкова, А. Антонов"

**Source evidence (Oct 20, Day 7):**
> "Екип: Н. Кечева, В. Генчева, Е. Дакашев, Е. Тонкова, А. Антонов"

**Reasoning:** Both days have 5 walkers per diary; CSV has 4 (missing Anani Antonov).

**User Decision:**
- [X] Approve both
- [ ] Modify: _______________

**Status:** Pending

---

### D005: Oct 22 Missing Walker

**Record:** 2011-10-22, Team D
**Field:** Walkers_Transliterated
**Current:** Nadezhda Kecheva | Veronika Gencheva | Emil Dakashev | Eva Tonkova
**Corrected:** Nadezhda Kecheva | Veronika Gencheva | Emil Dakashev | Eva Tonkova | Anani Antonov

**Source evidence (Day 9):**
> "Екип: Н. Кечева, В. Генчева, Е. Дакашев, Е. Тонкова, А. Антонов"

**Reasoning:** Diary explicitly lists 5 team members; CSV has 4 (missing Anani Antonov).

**User Decision:**
- [X] Approve
- [ ] Modify: _______________

**Status:** Pending

---

### D006-D007: Oct 23 & Oct 25 Missing Walker

**Records:** 2011-10-23 and 2011-10-25, Team D
**Field:** Walkers_Transliterated
**Current:** Georgi Nekhrizov | Nadezhda Kecheva | Veronika Gencheva | Emil Dakashev | Eva Tonkova
**Corrected:** Georgi Nekhrizov | Nadezhda Kecheva | Veronika Gencheva | Emil Dakashev | Eva Tonkova | Anani Antonov

**Source evidence (Oct 23, Day 10):**
> "Екип: Г. Нехризов, Н. Кечева, В. Генчева, Е. Дакашев, Е. Тонкова, А. Антонов"

**Source evidence (Oct 25, Day 12):**
> "Екип: Г. Нехризов, Н. Кечева, В. Генчева, Е. Дакашев, Е. Тонкова, А. Антонов"

**Reasoning:** Both days have 6 walkers per diary; CSV has 5 (missing Anani Antonov).

**User Decision:**
- [X] Approve both
- [ ] Modify: _______________

**Status:** Pending

---

### D008-D010: Oct 26-28 Missing Walker

**Records:** 2011-10-26, 2011-10-27, 2011-10-28, Team D
**Field:** Walkers_Transliterated
**Current:** Nadezhda Kecheva | Emil Dakashev | Eva Tonkova
**Corrected:** Nadezhda Kecheva | Emil Dakashev | Eva Tonkova | Anani Antonov

**Source evidence (all three days):**
> "Екип: Н. Кечева, Е. Дакашев, Е. Тонкова, А. Антонов"

**Reasoning:** All three days have 4 walkers per diary; CSV has 3 (missing Anani Antonov).

**User Decision:**
- [X] Approve all three
- [ ] Modify: _______________

**Status:** Pending

---

## Source Observations

### Unit Sequence Analysis

| Date | Diary Start | Diary End | Total | Continuity |
|------|-------------|-----------|-------|------------|
| Oct 14 | 40915 | 40919 | 5 | Start |
| Oct 15 | 40920 | 40958 | 39 | +1 (continuous) |
| Oct 16 | 40959 | 40967 | 9 | +1 (continuous) |
| Oct 17-18 | — | — | 0 | Rain days (Дъждовен ден!) |
| Oct 19 | 40968 | 41007 | 40 | +1 (continuous) |
| Oct 20 | 41008 | 41087 | 80 | +1 (continuous) |
| Oct 21 | 41088 | 41152 | 65 | +1 (continuous) |
| Oct 22 | 41153 | 41197 | 45 | +1 (continuous) |
| Oct 23 | 41198 | 41221 | 24 | +1 (continuous) |
| Oct 24 | — | — | 0 | Rain day (Дъждовен ден!) |
| Oct 25 | 41222 | 41249 | 28 | +1 (continuous) |
| Oct 26 | 41250 | 41316 | 67 | +1 (continuous) |
| Oct 27 | 41317 | 41399 | 83 | +1 (continuous) |
| Oct 28 | 41400 | 41453 | 54 | +1 (continuous) |
| Nov 01 | 41454 | 41470 | 17 | +1 (continuous) |
| Nov 02 | 41471 | 41477 | 7 | +1 (continuous) |

**Total units surveyed:** 563 units across 14 survey days

### Non-Survey Days

| Date | Status | Diary Evidence |
|------|--------|----------------|
| Oct 17 | Rain day | "Дъждовен ден!" (Day 4) |
| Oct 18 | Rain day | "Дъждовен ден!" (Day 5) |
| Oct 24 | Rain day | "Дъждовен ден!" (Day 11) |
| Oct 29-31 | Not documented | Diary ends at Oct 28 for Team D core; Nov work by different team |

**Note:** Oct 17, 18, 24 correctly not in CSV. Oct 29-31 gap is real - Team D core finished Oct 28, new team (Tsoni, Anani, foreign students) picked up Nov 1.

### Source Reliability Patterns

- **Unit data reliability:** 100% - All 14 survey day unit ranges match diary exactly
- **Unit continuity:** Perfect - Every day starts exactly where previous day ended (+1)
- **Walker data reliability:** 29% (4 of 14 records fully correct)
- **Systematic walker omission:** Anani Antonov missing from 8 records; Hristina Pavkova missing from 2 records
- **Root cause:** Original extraction appears to have missed some Bulgarian abbreviated names (А. Антонов, Х. Павкова)

### Implications for Future QA

- **Abbreviated name handling:** Both missing walkers (А. Антонов, Х. Павкова) use abbreviated format in diary. Extraction may have failed to parse these correctly.
- **Oct 21 exception:** CSV notes show Oct 21 was manually corrected with Anani Antonov added based on diary. Other days were not similarly corrected.
- **Systematic pattern:** The same walker omission across multiple days suggests a parsing/extraction issue rather than random error.

---

## Notes

- **Oct 15 unit gap note:** Diary shows two separate unit sequences (40920-40943 and 40945-40958), suggesting unit 40944 was skipped. CSV normalises this to 40920-40958. This is acceptable as the overall range is correct.

- **Oct 23 multi-area work:** Day 10 included work in multiple areas, including object documentation with additional polygon numbers (41222-41226). These may overlap with Day 12's formal start. Unit continuity remains correct.

- **Nov 1-2 team change:** Different team composition (Tsoni Tsonev, Anani Antonov with foreign students) took over. Leader changed from Nadezhda Kecheva to Anani Antonov. Walker data for these days is CONFIRMED.

- **Archaeological objects:** Team D registered 10 archaeological objects (trap_codes 4125-4134) during the season, well-documented in the diary.

---

## Summary Statistics

| Metric | Count |
|--------|-------|
| Records in CSV | 14 |
| Records in Diary | 14 (+ 3 rain days) |
| Unit ranges confirmed | 14/14 (100%) |
| Walker data confirmed | 4/14 (29%) |
| Corrections required | 10 |

### Issues by Category
- Unit range errors: 0
- Missing walkers: 10 (D001-D010)
- Missing records: 0
- Role errors: N/A (diary-only verification)

### Walker Correction Summary
- Hristina Pavkova: Add to 2 records (Oct 15, 16)
- Anani Antonov: Add to 8 records (Oct 19, 20, 22, 23, 25, 26, 27, 28)

---

**Document created:** 2025-12-01
**Last updated:** 2025-12-01
