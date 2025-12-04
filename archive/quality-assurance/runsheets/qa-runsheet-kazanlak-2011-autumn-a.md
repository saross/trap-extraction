# QA Runsheet: Kazanlak 2011 Autumn Team A

**Study Area/Season:** Kazanlak (Seuthopolis) 2011 Autumn
**Team:** A
**QA Date:** 2025-12-01
**QA Performed By:** Claude Code (with Shawn Ross)
**Records in CSV:** 17
**Date Range:** 2011-10-16 to 2011-11-03

---

## Sources Consulted

| Type | File | Location | Role |
|------|------|----------|------|
| Diary | A_2011Diary_BG.doc | `Kazanluk/2011-11-30/Project Records/Team A/` | PRIMARY (BG, 108 KB) |
| Day PDFs | A_2011*.pdf | `Kazanluk/2011-11-30/Project Records/Team A/FieldRecords/` | Not used (API size limit) |

**Note:** This QA uses Bulgarian diary as the sole verification source. Day PDFs exist but exceed API processing limits. Role data (Leader vs Walker) is not available from diary sources.

---

## Team Composition

### Phase 1: 16-23 October 2011 (Initial Team)
- **Core walkers:** Julia Tzvetkova (ЮЦ), Tsoni Tsonev (ЦЦ), Yulia Dimitrova (ЮД), Georgi Mihailov (Г. Михайлов)
- **Note:** 4-person team initially (Oct 16), expanded to 5 with Aleksandar Riskov joining (Oct 19)

### Phase 2: 25-28 October 2011 (Roster Change)
- **Walkers:** Yulia Dimitrova, Veronika Gencheva (ВГ), Georgi Mihailov, Aleksandar Riskov
- **Note:** Julia Tzvetkova and Tsoni Tsonev out; Veronika Gencheva joins

### Phase 3: 29-31 October 2011 (Further Changes)
- **Walkers:** Julia Tzvetkova (returns), Eva Tonkova (ЕТ), Anani Antonov (АА), Georgi Mihailov, Aleksandar Riskov
- **Note:** Major roster change - Yulia Dimitrova, Veronika Gencheva out; Eva Tonkova, Anani Antonov join

### Phase 4: 1-3 November 2011 (Foreign Students)
- **Core:** Georgi Mihailov (ГМ), Eva Tonkova (ЕТ)
- **Foreign students:** Bethan Donnelly, Corinne Softley, Hamish Sinclair, Elaine Lin, Cecilia Choi, Zac Spielvogel
- **Note:** Nov 1-2 predominantly foreign student teams; Nov 3 mixed team with Tsoni Tsonev, Anani Antonov

---

## Record-by-Record Verification

### October 2011

| Date | CSV Range | Diary Range | Total | Walkers Status |
|------|-----------|-------------|-------|----------------|
| Oct 16 | 11206-11224 | 11206-11224 | 19 | ✓ CONFIRMED (4 walkers) |
| Oct 19 | 11225-11325 | 11225-11325 | 101 | ✓ CONFIRMED (5 walkers) |
| Oct 20 | 11326-11391 | 11326-11391 | 66 | ✓ CONFIRMED |
| Oct 21 | 11392-11448 | 11392-11448 | 57 | ✓ CONFIRMED |
| Oct 22 | 11449-11492 | 11449-11492 | 44 | ✓ CONFIRMED |
| Oct 23 | 11493-11559 | 11493-11559 | 67 | ✓ CONFIRMED |
| Oct 24 | — | — | 0 | ✓ NON-SURVEY DAY (rain) |
| Oct 25 | 11560-11596 | 11560-11596 | 37 | ✓ CONFIRMED |
| Oct 26 | 11597-11634 | 11597-11634 | 38 | ✓ CONFIRMED |
| Oct 27 | 11635-11672 | 11635-11672 | 38 | ✓ CONFIRMED |
| Oct 28 | 11673-11750 | 11673-11750 | 78 | ✓ CONFIRMED |
| Oct 29 | 11751-11781 | 11751-11781 | 31 | ⚠️ WALKER DISCREPANCY |
| Oct 30 | 11782-11822 | 11782-11822 | 41 | ⚠️ WALKER DISCREPANCY |
| Oct 31 | 11823-11850 | 11823-11850 | 28 | ⚠️ WALKER DISCREPANCY |

### November 2011

| Date | CSV Range | Diary Range | Total | Walkers Status |
|------|-----------|-------------|-------|----------------|
| Nov 01 | 11851-11876 | 11851-11876 | 26 | ⚠️ WALKER DISCREPANCY |
| Nov 02 | 11877-11925 | 11877-11925 | 49 | ⚠️ WALKER DISCREPANCY |
| Nov 03 | 11926-11987 | 11926-11987 | 62 | ✓ CONFIRMED |

---

## Issues Summary

| ID | Date | Field | Issue | Action |
|----|------|-------|-------|--------|
| A001 | Oct 29 | Walkers | CSV: 6 walkers (wrong team), Diary: 5 walkers (different people) | [ ] Update walkers |
| A002 | Oct 30 | Walkers | CSV uses Phase 2 team, Diary shows Phase 3 team | [ ] Update walkers |
| A003 | Oct 31 | Walkers | CSV uses Phase 2 team, Diary shows Phase 3 team | [ ] Update walkers |
| A004 | Nov 01 | Walkers | CSV uses Phase 2 team, Diary shows foreign students | [ ] Update walkers |
| A005 | Nov 02 | Walkers | CSV uses Phase 2 team, Diary shows foreign students | [ ] Update walkers |

**Note:** All unit ranges are CORRECT - only walker assignments need correction.

---

## Corrections Required

### A001: Oct 29 Walker Data

**Record:** 2011-10-29, Team A
**Field:** Walkers_Transliterated
**Current:** Julia Tzvetkova | Yulia Dimitrova | Veronika Gencheva | Georgi Mihailov | Aleksandar Riskov | Tsoni Tsonev
**Corrected:** Julia Tzvetkova | Aleksandar Riskov | Eva Tonkova | Anani Antonov | Georgi Mihailov

**Source evidence:**
> "Група от пет човека в състав: ЮЦ, Ал. Р, ЕТ, АА и ГМ"
> (Group of five people: Julia, Aleksandar, Eva, Anani and Georgi)

**Reasoning:** Diary explicitly lists 5 walkers. CSV incorrectly shows 6 walkers with Phase 2 team composition.

**User Decision:**
- [X] Approve
- [ ] Modify: _______________

**Status:** Pending

---

### A002: Oct 30 Walker Data

**Record:** 2011-10-30, Team A
**Field:** Walkers_Transliterated
**Current:** Yulia Dimitrova | Veronika Gencheva | Georgi Mihailov | Aleksandar Riskov | Tsoni Tsonev
**Corrected:** Aleksandar Riskov | Anani Antonov | Eva Tonkova | Tsoni Tsonev | Georgi Mihailov

**Source evidence:**
> "Група от пет човека в състав: АлР, АА, ЕТ, ЦЦ и ГМ"
> (Group of five people: Aleksandar, Anani, Eva, Tsoni and Georgi)

**Reasoning:** Diary explicitly lists 5 walkers. CSV has Yulia Dimitrova and Veronika Gencheva who were not present according to diary.

**User Decision:**
- [X] Approve
- [ ] Modify: _______________

**Status:** Pending

---

### A003: Oct 31 Walker Data

**Record:** 2011-10-31, Team A
**Field:** Walkers_Transliterated
**Current:** Yulia Dimitrova | Veronika Gencheva | Georgi Mihailov | Aleksandar Riskov | Tsoni Tsonev
**Corrected:** Anani Antonov | Eva Tonkova | Tsoni Tsonev | Georgi Mihailov

**Source evidence:**
> "Група от 4 човека в състав: АА, ЕТ, ЦЦ и ГМ обхожда територия западно от с. Хаджидимитрово. [...] За обучение в методиката на работа с групата обхождаха трима чуждестранни студенти: Zack Spielvogel, Georgia Burnett и Corinne Softley."
> (Group of 4 people: Anani, Eva, Tsoni and Georgi [...] Three foreign students joined for training: Zack, Georgia and Corinne)

**Reasoning:** Diary states 4 core walkers plus 3 foreign trainees. CSV incorrectly shows Phase 2 team (Yulia, Veronika, Aleksandar) who were not present.

**User Decision:**
- [X] Approve
- [ ] Modify: _______________

**Status:** Pending

---

### A004: Nov 01 Walker Data

**Record:** 2011-11-01, Team A
**Field:** Walkers_Transliterated
**Current:** Yulia Dimitrova | Veronika Gencheva | Georgi Mihailov | Aleksandar Riskov | Tsoni Tsonev
**Corrected:** Georgi Mihailov | Eva Tonkova | Bethan Donnelly | Corinne Softley | Hamish Sinclair | Elaine Lin

**Source evidence:**
> "Екип от шест човека в състав: ГМ, ЕТ, Bethan Donnelly, Corinne Softley, Hamish Sinclair, Elaine Lin"
> (Team of six people: Georgi, Eva, Bethan, Corinne, Hamish, Elaine)

**Reasoning:** Diary explicitly names 6 walkers - 2 Bulgarian (Georgi, Eva) and 4 foreign students. CSV has completely wrong team composition.

**User Decision:**
- [X] Approve
- [ ] Modify: _______________

**Status:** Pending

---

### A005: Nov 02 Walker Data

**Record:** 2011-11-02, Team A
**Field:** Walkers_Transliterated
**Current:** Yulia Dimitrova | Veronika Gencheva | Georgi Mihailov | Aleksandar Riskov | Tsoni Tsonev
**Corrected:** Georgi Mihailov | Elaine Lin | Zac Spielvogel | Hamish Sinclair | Cecilia Choi

**Source evidence:**
> "Екип от 5 човека в състав: ГМ, EL, ZS, HS и Cecilia Choi"
> (Team of 5 people: Georgi, Elaine, Zac, Hamish and Cecilia)

**Reasoning:** Diary explicitly names 5 walkers - 1 Bulgarian (Georgi) and 4 foreign students. CSV has completely wrong team composition.

**User Decision:**
- [X] Approve
- [ ] Modify: _______________

**Status:** Pending

---

## Source Observations

### Unit Sequence Analysis

| Date | Diary Start | Diary End | Total | Continuity |
|------|-------------|-----------|-------|------------|
| Oct 16 | 11206 | 11224 | 19 | Start |
| Oct 19 | 11225 | 11325 | 101 | +1 (continuous) |
| Oct 20 | 11326 | 11391 | 66 | +1 (continuous) |
| Oct 21 | 11392 | 11448 | 57 | +1 (continuous) |
| Oct 22 | 11449 | 11492 | 44 | +1 (continuous) |
| Oct 23 | 11493 | 11559 | 67 | +1 (continuous) |
| Oct 24 | — | — | 0 | Non-survey (rain) |
| Oct 25 | 11560 | 11596 | 37 | +1 (continuous) |
| Oct 26 | 11597 | 11634 | 38 | +1 (continuous) |
| Oct 27 | 11635 | 11672 | 38 | +1 (continuous) |
| Oct 28 | 11673 | 11750 | 78 | +1 (continuous) |
| Oct 29 | 11751 | 11781 | 31 | +1 (continuous) |
| Oct 30 | 11782 | 11822 | 41 | +1 (continuous) |
| Oct 31 | 11823 | 11850 | 28 | +1 (continuous) |
| Nov 01 | 11851 | 11876 | 26 | +1 (continuous) |
| Nov 02 | 11877 | 11925 | 49 | +1 (continuous) |
| Nov 03 | 11926 | 11987 | 62 | +1 (continuous) |

**Total units surveyed:** 782 units across 16 survey days

### Non-Survey Days

| Date | Status | Diary Evidence |
|------|--------|----------------|
| Oct 17 | Rain day | "Дъждовен ден, работа в базата" (Rainy day, base work) |
| Oct 18 | Rain day | "Дъждовен ден, работа в базата" (Rainy day, base work) |
| Oct 24 | Rain day | "Дъждовен ден. Не се обхожда." (Rainy day. No survey.) |

**Note:** Oct 17-18 correctly not in CSV (no survey records). Oct 24 correctly in CSV as non-survey day with documented reason.

### Source Reliability Patterns

- **Unit data reliability:** 100% - All 16 survey day unit ranges match diary exactly
- **Unit continuity:** Perfect - Every day starts exactly where previous day ended (+1)
- **Walker data reliability:** 71% (12 of 17 records correct)
- **Walker discrepancies:** 5 records (Oct 29, 30, 31, Nov 1, 2) have incorrect team composition
- **Root cause:** CSV extraction appears to have used "default" team composition from Phase 2 instead of actual daily compositions

### Implications for Future QA

- **Team roster instability:** Team A had significant roster changes in late October
- **Foreign student participation:** Nov 1-2 were predominantly foreign student survey days - needs special attention
- **Day-by-day verification essential:** Default/inherited walker lists are unreliable when teams change frequently

---

## Notes

- **Oct 16 walker count:** Diary says "Група от 4 човека" (group of 4), but the Walkers_Original field shows 5 abbreviations. This appears to be a duplicate encoding of ЮЦ (as both "JTs" and "YuTs"). The Walkers_Transliterated correctly shows 4 people.

- **Oct 24 activities:** Although marked as non-survey day, a group of 5 (ГН, ЮЦ, ЕТ, АА, Ал.Р) visited burial mounds for GPS coordinates. This is correctly documented in CSV QA_Notes.

- **Training days:** Oct 31, Nov 1 included foreign students training alongside regular team members. These should be recorded accurately for provenance.

- **Oct 22 note:** Diary mentions "7/5 човека" (7/5 people) - team size varied during the day. The 7 included ГН who joined temporarily.

---

## Summary Statistics

| Metric | Count |
|--------|-------|
| Records in CSV | 17 |
| Records in Diary | 17 (16 survey + 1 non-survey) |
| Unit ranges confirmed | 17/17 (100%) |
| Walker data confirmed | 12/17 (71%) |
| Corrections required | 5 |

### Issues by Category
- Unit range errors: 0
- Walker errors: 5 (A001-A005)
- Missing records: 0
- Role errors: N/A (diary-only verification)

---

**Document created:** 2025-12-01
**Last updated:** 2025-12-01
