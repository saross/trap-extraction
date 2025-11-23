# Kazanluk 2011 Date Error Report (Phase 4)

**Date:** 23 November 2025
**Phase:** Phase 4
**Issue:** Date error in source data (Kaz11_SurveySummary.xlsx)
**Type:** Data quality investigation

## Executive Summary

During Phase 4 extraction planning, a critical **date error** was discovered in the source data. The record dated **2011-11-10 Team D** (units 41088-41152) is misdated - these units actually belong to **2011-10-21 Team D**. Team D's diary contains no November 10 entry, as their field season ended 2 November 2011.

## Error Details

### Erroneous Record

**Current attribution.csv entry:**
- Date: 2011-11-10
- Team: D
- Units: 41088-41152
- Leader: NK
- Walkers: (MISSING)
- Source: Kaz11_SurveySummary.xlsx

### Correct Information

**From D_2011Diary_BG.doc (Day 8: 21.10.2011):**
- Date: **2011-10-21** (not 2011-11-10)
- Team: D
- Units: 41088-41152
- Leader: Н. Кечева (N. Kecheva) = NK
- Walkers: Н. Кечева | В. Генчева | Е. Дакашев | Е. Тонкова | **А. Антонов**
- Transliterated: N. Kecheva | V. Gencheva | E. Dakashev | E. Tonkova | **A. Antonov**

## Evidence

### 1. Unit Sequence Analysis

Team D unit progression in October 2011:

| Date       | Team | Units        | Status in CSV |
|------------|------|--------------|---------------|
| 2011-10-20 | D    | 41008-41087  | ✓ Correct     |
| 2011-10-21 | D    | **MISSING**  | ⚠️ Units missing |
| 2011-10-22 | D    | 41153-41197  | ✓ Correct     |
| 2011-11-10 | D    | 41088-41152  | ❌ **Date error** |

The units **41088-41152** fit **sequentially** between October 20 and October 22, not in November.

### 2. Team D Diary Coverage

**D_2011Diary_BG.doc date range:**
- **First day:** Ден 1: 14.10.2011 (14 October 2011)
- **Last day:** 02.11.2011 (2 November 2011)
- **Total days:** 15 working days covering 14 October - 2 November
- **NO November 10 entry** - diary ends 8 days earlier

### 3. Diary Text Evidence

**Ден 8: 21.10.2011 г. (петък)** [Day 8: 21 October 2011 (Friday)]

```
Екип:
Н. Кечева, В. Генчева, Е. Дакашев, Е. Тонкова, А. Антонов

Работа на терен:
Направени са 4 трансекти (полигони с номера 41088 до 41152) в посока С-Ю
между асфалтовия път Калофер-Казанлък от юг и жп линията София-Казанлък от
север.
```

**Translation:**
Team: N. Kecheva, V. Gencheva, E. Dakashev, E. Tonkova, A. Antonov

Field work: 4 transects were made (polygons numbered 41088 to 41152) in N-S direction between the Kalofer-Kazanlak asphalt road to the south and the Sofia-Kazanlak railway line to the north.

### 4. Existing 2011-10-21 Record

**Current attribution.csv record for 2011-10-21:**
- Date: 2011-10-21
- Team: D
- Units: **(MISSING)**
- Leader: **(MISSING)**
- Walkers: Н. Кечева | В. Генчева | Е. Дакашев | Е. Тонкова
- Status: MISSING: Leader | MISSING: Survey units

**Issues identified:**
1. Missing survey units 41088-41152 (incorrectly assigned to 2011-11-10)
2. Missing leader NK (Nadya Kecheva)
3. Missing walker А. Антонов (A. Antonov) - 5th team member

### 5. Activity on 10 November 2011

**Actual survey activity on 10 November 2011:**
- **Team B** (not Team D) was working
- Leader: Petra
- Walkers: Adela | Hamish | Bethan | Cecilia
- Units: 22124-22198
- **Already correctly recorded in attribution.csv**

**Team D had NO activity on 10 November 2011** - diary ended 2 November.

## Root Cause

**Source:** Kaz11_SurveySummary.xlsx

The source Excel file contains an incorrect date entry. This appears to be a data entry error where:
- Date was entered as 2011-11-10 instead of 2011-10-21
- Possible causes: date formatting error, manual transcription error, or Excel date conversion issue

## Impact on Attribution Data

### Current State (with error)
- 2011-10-21 Team D: **MISSING** units and leader
- 2011-11-10 Team D: **INCORRECT** date with correct units
- Result: 1 record with incomplete data, 1 record with wrong date

### After Correction
- 2011-10-21 Team D: Complete record (date, units, leader, all walkers)
- 2011-11-10 Team D: **DELETED** (erroneous record)
- Result: Data quality improved, error corrected

## Recommended Actions

### 1. Immediate Actions
- **Do NOT extract walker data for "2011-11-10 Team D"** - record is erroneous
- Flag this record in attribution.csv as containing a date error
- Update 2011-10-21 Team D record with correct data

### 2. Data Correction

**Update 2011-10-21, Team D record:**
```csv
Date: 2011-10-21
Team: D
Start_Unit: 41088
End_Unit: 41152
Leader: NK
Walkers_Original: Н. Кечева | В. Генчева | Е. Дакашев | Е. Тонкова | А. Антонов
Walkers_Transliterated: N. Kecheva | V. Gencheva | E. Dakashev | E. Tonkova | A. Antonov
PDF_Source: D_2011Diary_BG.doc
Extraction_Notes: Corrected from erroneous 2011-11-10 record - units 41088-41152 belong to 2011-10-21 per Team D diary Day 8 | Added missing walker A. Antonov
Issues: DATE ERROR CORRECTED - Was incorrectly recorded as 2011-11-10 in source data
```

**Flag 2011-11-10, Team D record:**
```csv
Issues: DATE ERROR - These units (41088-41152) actually belong to 2011-10-21 Team D per D_2011Diary_BG.doc Day 8 | Team D diary ends 2 November - no 10 November entry exists | RECOMMEND DELETION
```

### 3. Source Data Correction
- **Contact data custodian** to correct Kaz11_SurveySummary.xlsx
- Change 2011-11-10 Team D → 2011-10-21 Team D
- Verify no other date errors exist in source file

## Phase 4 Status

**Original Plan:** Extract walker data for 3 Kazanluk 2011 records
- 2011-11-10, Team D ❌ **ERRONEOUS - Date error discovered**
- 2011-11-16, Team B ✓ Already has walker data in CSV
- 2011-11-22, Team B ✓ Already has walker data in CSV

**Actual Result:**
Phase 4 identified a **data quality issue** rather than extracting walker data. The discovery of this date error:
1. Prevents incorrect data from being propagated
2. Identifies root cause in source data (Kaz11_SurveySummary.xlsx)
3. Provides path to correct attribution.csv
4. Adds 1 complete walker record when corrected (2011-10-21)

## Files Analyzed

- `../Kazanluk/2011-11-30/Project Records/Team D/D_2011Diary_BG.doc`
- `../Kazanluk/2011-11-30/Project Records/Team B/B_2011Diary_En.docx`
- `outputs/attribution.csv`

## Next Steps

1. **User decision required:** How to handle the erroneous 2011-11-10 Team D record
   - Option A: Delete and update 2011-10-21 with complete data
   - Option B: Flag both records with error notes, retain for audit trail
2. **Create correction script** if user approves data fix
3. **Report to data custodian** for source file correction

---

**Report generated:** 23 November 2025 15:05
**Method:** Diary cross-reference + unit sequence analysis
**Confidence:** Very High (100%) - conclusive diary evidence
**Type:** Data quality investigation (Phase 4)
