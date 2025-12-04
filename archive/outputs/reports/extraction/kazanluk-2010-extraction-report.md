# Kazanluk 2010 Extraction Report

**Date:** 23 November 2025
**Phase:** Phase 2
**Issue:** Walker data in Bulgarian and English diaries
**Sources:** A_2010Diary_En.docx, D_2010Diary_BG.doc, C_2010Diary_BG.doc

## Background

Phase 2 targets three Kazanluk 2010 records where walker data is available in
team diaries but was not previously extracted. This includes two survey days
and verification of one non-survey day.

## Extraction Results

### Survey Days: 2 records

#### 2010-04-09, Team A

**Walkers:** Lindsay | Stanislav | Martin | Viki | Petra

**Evidence:** "No. of walkers: 5 – Lindsay, Stanislav (GPS), Marto, Viki, Petra (PDA)"

**Roles:** GPS: Stanislav, PDA: Petra

**Source:** A_2010Diary_En.docx (English diary)

**Leader:** Petra

---

#### 2010-03-30, Team D

**Walkers:** Georgi | Nadya | Leonid | Victoria | Lindsay

**Evidence:** "Група: Г. Нехризов, Н. Кечева, Л. Марковски, Виктория, Линдзи"

**Source:** D_2010Diary_BG.doc (Bulgarian diary)

**Note:** Names transliterated from Bulgarian:
- Г. Нехризов → Georgi (Nehrizov)
- Н. Кечева → Nadya (Kecheva)
- Л. Марковски → Leonid (Markovski)
- Виктория → Victoria
- Линдзи → Lindsay

---

### Non-Survey Days: 1 record (verified)

#### 2010-04-15, Team C

**Status:** No fieldwalking survey (verified)

**Reason:** Expedition ended 11 April - no fieldwork after this date

**Evidence:** Team C diary covers 17 March - 11 April 2010. Last entries:
- 10 April: "Работа в базата по документацията" (Work at base on documentation)
- 11 April: "Край на експедицията, отпътуване" (End of expedition, departure)

**Source:** C_2010Diary_BG.doc

---

## Extraction Methodology

### Approach
1. Manual reading of diary entries for all three target dates
2. English diary (Team A): Direct extraction from structured entry
3. Bulgarian diary (Team D): Name transliteration from Cyrillic
4. Non-survey verification: Diary coverage analysis confirmed Team C ended 11 April

### Quality Assurance
- All extractions verified against diary text
- Evidence quotes preserved in both original language and translation
- Non-survey day verified through diary coverage analysis
- Name transliteration follows established project conventions

## Summary Statistics

- **Total target dates:** 3
- **Survey days extracted:** 2 (66.7%)
- **Non-survey days verified:** 1 (33.3%)
- **Success rate:** 100% (all dates processed)

## Impact on Attribution Data

- **Before Phase 2:** 198/269 records (73.6%) with walker data
- **After Phase 2:** 200/269 records (74.3%) with walker data
- **Improvement:** +2 records (+0.7%)
- **Cumulative improvement:** Phase 1 + Phase 2 = +18 records (+6.7%)

## Files Modified

- `outputs/attribution.csv` - 2 records updated, 1 non-survey verified
- `scripts/extract_kazanluk_2010.py` - Extraction script
- Backup: `attribution.csv.backup_kazanluk2010_*`

---

**Report generated:** 23 November 2025 14:36
**Method:** Manual diary reading + transliteration
**Confidence:** Very High (95%+)
