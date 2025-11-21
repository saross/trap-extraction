# Narrative Text Cleanup Summary

**Date:** 2025-11-20
**Dataset:** final_attribution_v2_cleaned.csv
**Action:** Comprehensive narrative text removal from Walkers column

---

## Overview

A systematic review of the Walkers column identified 19 entries containing narrative text, survey notes, or location descriptions instead of (or mixed with) team member names. All narrative text has been removed to ensure data quality and consistency.

---

## Entries Cleaned

### English Narrative Text (4 entries)

| Row | Date | Team | Original Text | Action |
|-----|------|------|---------------|--------|
| 11 | 2009-10-13 | A | "A than walks" | Cleared - no names |
| 24 | 2009-10-21 | A | "A continues where they left off the previous day" | Cleared - narrative only |
| 33 | 2009-10-26 | A | "C was supposed to resurvey their site on Tuesday so we prepare" | Cleared - narrative only |
| 36 | 2009-10-27 | A | "delaying in the field \| decided to take a marsrutka home" | Cleared - narrative only |
| 47 | 2009-11-02 | A | "B stays to the north of the dirt road whileTeam A" | Cleared - narrative only |

### Survey Notes (1 entry)

| Row | Date | Team | Original Text | Action |
|-----|------|------|---------------|--------|
| 133 | 2010-04-15 | C | "[No field survey - GC work only]" | Cleared - note, not names |

### Bulgarian Entries with Location Descriptions (12 entries)

These entries had team member names at the beginning, followed by location/survey area descriptions. Names were extracted, location descriptions removed.

| Row | Date | Team | Names Extracted | Location Text Removed |
|-----|------|------|----------------|---------------------|
| 147 | 2011-10-14 | D | Н. Кечева \| Ю. Димитрова \| В. Генчева \| Г. Михайлов \| Е. Дакашев \| А. Рисков \| Христина Павкова | (kept all names) |
| 149 | 2011-10-15 | D | Н. Кечева \| Ю. Димитрова \| В. Генчева \| Г. Михайлов \| Е. Дакашев \| А. Рисков | "проведени през 2010 г. от Team B" |
| 151 | 2011-10-16 | D | Н. Кечева \| В. Генчева \| Е. Дакашев | "а от юг – от асфалтовия път Калофер-Казанлък" |
| 153 | 2011-10-19 | D | Н. Кечева \| В. Генчева \| Е. Дакашев \| Е. Тонкова | "а от юг – от асфалтовия път Калофер-Казанлък" |
| 155 | 2011-10-20 | D | Н. Кечева \| В. Генчева \| Е. Дакашев \| Е. Тонкова | "а от юг – от асфалтовия път Калофер-Казанлък" |
| 157 | 2011-10-21 | D | Н. Кечева \| В. Генчева \| Е. Дакашев \| Е. Тонкова | "а от юг – от асфалтовия път Калофер-Казанлък" |
| 159 | 2011-10-22 | D | Н. Кечева \| В. Генчева \| Е. Дакашев \| Е. Тонкова | "а от юг – от асфалтовия път Калофер-Казанлък" |
| 161 | 2011-10-23 | D | Г. Нехризов \| Н. Кечева \| В. Генчева \| Е. Дакашев \| Е. Тонкова | "от изток от Голямата река \| а от север – от черен път..." |
| 164 | 2011-10-25 | D | Г. Нехризов \| Н. Кечева \| В. Генчева \| Е. Дакашев \| Е. Тонкова | "от изток от канал \| вливащ се в Голямата река..." |
| 166 | 2011-10-26 | D | Н. Кечева \| Е. Дакашев \| Е. Тонкова | "от изток от канал \| вливащ се в Голямата река..." |
| 168 | 2011-10-27 | D | Н. Кечева \| Е. Дакашев \| Е. Тонкова | "заключени от запад от Селската река" |
| 170 | 2011-10-28 | D | Н. Кечева \| Е. Дакашев \| Е. Тонкова | "разположена между Селската река от запад..." |

### Bulgarian Survey Notes (2 entries)

| Row | Date | Team | Original Text | Action |
|-----|------|------|---------------|--------|
| 199 | 2011-11-16 | B | "суха трева на земеделски пасища \| като всички могили бяка записани" | Cleared - survey notes only |
| 208 | 2011-11-22 | B | 687 chars of survey notes about survey areas, GPS points, pottery fragments | Cleared - no names |

---

## Impact on Coverage

### Before Cleanup

- Records with walker data: 177/212 (83.5%)
- Initial assessment showed narrative contamination

### After Cleanup

- Records with walker data: 169/212 (79.7%)
- All entries contain only names or "[unclear]" notation
- 8 entries cleared (narrative text, no recoverable names)
- 11 entries cleaned (names extracted, narrative removed)

---

## Quality Improvements

1. **Data Integrity**: Walkers column now contains exclusively team member names
2. **Consistency**: No mix of names and descriptive text
3. **Clarity**: Entries with "[unclear]" notation properly indicate illegible handwriting (10 entries)
4. **Extraction Notes**: All cleaned entries documented with explanatory notes

---

## Acceptable "[unclear]" Notation

The following 10 entries contain "[unclear]" notation, which is **appropriate and retained**:

- Row 80: 2010-03-20, Team C - "Bara \| Elena \| BS \| [unclear]"
- Row 83: 2010-03-21, Team C - "Bara \| Elena \| Sonya \| [unclear] \| Bistra"
- Row 87: 2010-03-22, Team C - "Bara \| Elena \| Bistra \| [unclear] \| Todor"
- Row 100: 2010-03-26, Team C - "Bara \| Sonja \| Elena \| Bara \| [unclear]"
- Row 104: 2010-03-27, Team C - "Bara \| Sonja \| Elena \| [unclear] \| Todor"
- Row 113: 2010-03-30, Team C - "Bara \| Sonja \| Elena \| [unclear] \| Bara"
- Row 132: 2010-04-09, Team C - "Bara \| Sonja \| Elena \| Todor \| [unclear]"
- Row 184: 2011-11-06, Team B - "Oscar \| Hamish \| [unclear]"
- Row 190: 2011-11-09, Team B - "Joel \| Hamish \| Bethan \| [unclear]"
- Row 192: 2011-11-10, Team B - "Adela \| Bethan \| Hamish \| Bethan \| [unclear]"

These notations correctly document that one team member's name was illegible in the source document.

---

## Validation Results

Final validation confirms:

✓ **Zero entries** with narrative sentence structures
✓ **Zero entries** with location descriptions
✓ **Zero entries** with survey technical terms
✓ **All entries** contain only names or acceptable "[unclear]" notation
✓ **QA validation** passed with no narrative text detected

---

## Next Steps for Recipients

1. **Cross-reference** the 43 missing walker entries with project field records
2. **Consult PIs** for dates where narrative indicated "no survey" or administrative work
3. **Investigate** entries with "[unclear]" notation - team leaders may recall team composition
4. **Consider** that some cleared entries may have been non-survey days

---

**Cleanup completed:** 2025-11-20 23:22
**Final dataset:** final_attribution_v2_cleaned.csv
**Coverage:** 169/212 (79.7%)
**Quality status:** Clean, validated, ready for submission
