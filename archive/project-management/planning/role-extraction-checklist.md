# Role Extraction Checklist

**Task:** Extract role information from diary sources to populate attribution.csv
**Created:** 24 November 2025
**Status:** Complete

---

## Phase A: Automated Regex Pass

- [x] Create `scripts/extract-roles-regex.py` (completed 2025-11-24)
- [x] Run regex extraction across all diary files (completed 2025-11-24)
- [x] Review `outputs/role-extractions-regex.csv` results (completed 2025-11-24)
- [x] Document baseline findings (completed 2025-11-24)

**Phase A Results:**
- 31 files processed, 22 with matches
- 101 role mentions found (many false positives)
- Useful extractions: ~15-20 actual person assignments
- Key finds: Kaz 2010 Teams A, B, D have structured role headers
- Confirms need for manual NLP review for narrative diaries

---

## Phase B: Manual NLP Review (Season-Team Passes)

### Kazanlak 2009

- [x] **B.1 Team A** (~15 records) - completed 2025-11-24
  - Diaries: A_Diary_BG.doc (198 KB), A_Diary_En.doc (88 KB)
  - Output: `outputs/role-extractions-kaz2009-team-a.csv`
  - **Results:** Only 2 Author entries found (Stanislava Kučová 3/15, Petra 3/19)
  - **Notes:** Narrative style diaries - no PDA/GPS/recorder role assignments recorded

- [x] **B.2 Team B** (~15 records) - completed 2025-11-24
  - Diaries: B_Diary_BG.doc (152 KB), B_Diary_En.docx (62 KB)
  - **Results:** No role assignments found - narrative style only
  - **Notes:** Team compositions documented but no PDA/GPS/recorder roles

- [x] **B.3 Team C** (~15 records) - completed 2025-11-24
  - Diaries: C_Diary_BG.doc (215 KB)
  - **Results:** No role assignments - PDA mentioned as tool only
  - **Notes:** Same narrative pattern as other 2009 teams

- [x] **B.4 Team D** (~15 records) - completed 2025-11-24
  - Diaries: D Diary_BG.doc (222 KB)
  - **Results:** No role assignments found
  - **Notes:** Same narrative pattern

- [x] **B.5 Team E** (~16 records) - completed 2025-11-24
  - Diaries: E Diary_BG.doc (BG only)
  - **Results:** No role assignments found
  - **Notes:** Same narrative pattern

**Kaz 2009 Summary:** Only 2 Author entries found (Team A). Diaries use narrative style describing activities but don't document specific PDA/GPS/recorder role assignments. This was likely not standard practice in the 2009 season.

### Elhovo 2009

- [x] **B.6 Team A** (~12 records) - completed 2025-11-24
  - Diaries: Diary Team A.doc, Diary_Aneta.doc (29 KB)
  - Output: `outputs/role-extractions-elh2009-team-a.csv`
  - **Results:** 40 role extractions across 10 survey days
  - **Key pattern:** "usual setup" = Martin GPS, Aneta recording, Adela PDA
  - **Notes:** Oct 13 explicitly states roles; pattern inferred for other days

- [x] **B.7 Team B** (~12 records) - completed 2025-11-24
  - Diaries: DiaryTeamB.doc, TeamB_Dnevnik (Ross).doc (55 KB)
  - Output: `outputs/role-extractions-elh2009-team-b.csv`
  - **Results:** 40 role extractions across 20 survey days
  - **Key finds:** Scott PDA (Oct 22), Stanislav PDA (Oct 26), Vera Paper consistently
  - **Notes:** Detailed diary with explicit role mentions; Lizzy takes over forms Nov 9

- [x] **B.8 Team C** (~11 records) - completed 2025-11-24
  - Diaries: The Diary of Team C.doc, TeamC_Dnevnik.doc
  - Output: `outputs/role-extractions-elh2009-team-c.csv`
  - **Results:** 25 role extractions
  - **Key finds:** Oct 20 has full role breakdown (Petra PDA, Sona Paper, Tereza GPS)
  - **Notes:** Petra consistent photographer; Scott takes over as leader Nov 9

**Elh 2009 Summary:** Rich role data found - "usual setup" patterns documented for all teams. Oct 20 Team C entry provides explicit role assignments. Team B diary particularly detailed with explicit PDA and paper recorder mentions.

### Kazanlak 2011

- [x] **B.9 Team A** (~15 records) - completed 2025-11-24
  - Diaries: A_2011Diary_BG.doc + AUS_Diaries/*
  - **Results:** No role extractions - Bulgarian narrative diary only
  - **Notes:** Diary describes terrain and finds but no role assignments documented

- [x] **B.10 Team B** (~15 records) - completed 2025-11-24
  - Diaries: B_2011Diary_En.docx (63 KB), B_2011Diary_BG.docx + AUS_Diaries/*
  - Output: `outputs/role-extractions-kaz2011-team-b.csv`
  - **Results:** 22 role extractions across 14 survey days
  - **Key finds:** Nov 3 (Hamish photos, Joel PDA, Petra PDA), Nov 5 (Bethan Paper, Cecelia GPS)
  - **Notes:** Best role documentation for 2011 season - detailed diary with role assignments

- [x] **B.11 Team C** (~15 records) - completed 2025-11-24
  - Diaries: C_2011Diary_En.docx (70 KB), C_2011Diary_BG.docx + AUS_Diaries/*
  - Output: `outputs/role-extractions-kaz2011-team-c.csv`
  - **Results:** 16 Author extractions only (Shawn Ross as diary author)
  - **Notes:** Structured tables but no PDA/GPS/Paper role assignments documented

- [x] **B.12 Team D** (~15 records) - completed 2025-11-24
  - Diaries: D_2011Diary_BG.doc + AUS_Diaries/*
  - **Results:** No role extractions - Bulgarian narrative diary only
  - **Notes:** Same pattern as Team A

**Kaz 2011 Summary:** Team B diary provides excellent role data with explicit assignments. Teams A, C, and D diaries are narrative or structured without role assignments. Team B findings are valuable for improving coverage.

### Gap Filling (2010 seasons with existing partial coverage)

- [x] **B.13 Kazanlak 2010 gaps** - DEFERRED
  - **Notes:** 2010 seasons already have ~30% coverage from structured diary headers
  - **Recommendation:** Include in future QA pass if needed

- [x] **B.14 Elhovo 2010 gaps** - DEFERRED
  - **Notes:** 2010 seasons already have ~30% coverage from structured diary headers
  - **Recommendation:** Include in future QA pass if needed

---

## Phase C: Consolidate and Apply

- [x] Consolidate all extraction CSVs into `outputs/role-extractions-consolidated.csv` (completed 2025-11-24)
- [x] Create backup of attribution.csv (completed 2025-11-24)
- [x] Apply extractions to attribution.csv (empty fields only) (completed 2025-11-24)
- [x] Update Extraction_Notes with source citations (completed 2025-11-24)
- [x] Update QA_Notes (remove "No role data available" where applicable) (completed 2025-11-24)

**Phase C Results:**
- 145 extractions consolidated from 6 CSV files
- 80 records matched in attribution.csv
- 76 new role fields populated
- 69 fields skipped (already had data)
- Script: `scripts/apply-role-extractions.py`

---

## Phase D: Generate Report

- [x] Summary statistics documented below (completed 2025-11-24)

---

## Coverage Tracking

**Before extraction:**

| Role | Populated | Coverage |
|------|-----------|----------|
| Author | 210 | 78.4% |
| PDA_Operator | 30 | 11.2% |
| GPS_Operator | 25 | 9.3% |
| Paper_Recorder | 11 | 4.1% |
| Data_Editor | 8 | 3.0% |
| Photographer | 3 | 1.1% |

**After extraction:**

| Role | Populated | Coverage | Change |
|------|-----------|----------|--------|
| Author | 217 | 81.0% | +7 (+2.6%) |
| PDA_Operator | 44 | 16.4% | +14 (+5.2%) |
| GPS_Operator | 37 | 13.8% | +12 (+4.5%) |
| Paper_Recorder | 43 | 16.0% | +32 (+11.9%) |
| Data_Editor | 8 | 3.0% | +0 (no change) |
| Photographer | 14 | 5.2% | +11 (+4.1%) |

**Total fields updated:** 76

---

## Notes and Lessons Learned

1. **2009 Kazanlak diaries** use narrative style without role documentation - this wasn't standard practice in the 2009 spring season

2. **2009 Elhovo diaries** have the richest role documentation - "usual setup" patterns explicitly stated

3. **2011 Kazanlak Team B diary** (Petra Janouchová) provides excellent explicit role assignments

4. **Bulgarian-only diaries** consistently lack role assignments - future projects should ensure English translations include role data

5. **Paper_Recorder had largest improvement** (+11.9%) - this role was severely underdocumented before

6. **Data_Editor remains at 3%** - this role is rarely documented in field diaries (typically happens post-field)

---

## Source File Locations

**Kazanlak 2009:** `Kazanluk/2009/Project Records/Team[A-E]/`
**Kazanlak 2010:** `Kazanluk/2010/Project Records/Team [A-D]/`
**Kazanlak 2011:** `Kazanluk/2011-11-30/Project Records/Team [A-D]/`
**Kazanlak 2011 AUS:** `Kazanluk/2011-11-30/AUS_Diaries/`
**Elhovo 2009:** `Elhovo 2010-12-12/2009/Project Records/Team [A-C]/`
**Elhovo 2010:** `Elhovo 2010-12-12/2010/Project Records/Team [A-B]/`

---

**Last updated:** 25 November 2025 (extraction complete)
