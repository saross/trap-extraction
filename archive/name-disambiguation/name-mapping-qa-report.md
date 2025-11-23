# Name Mapping QA Report - pdf_sources Verification

**Date:** 21 November 2025

**Objective:** Verify all pdf_sources references in name-mapping.csv point to existing files and correct any erroneous entries.

---

## Executive Summary

**Total Rows:** 282

**Rows with pdf_sources:** 275

**Initial Errors Found:** 17 entries with incorrect or missing file references

**Corrections Applied:** 32 total corrections across two phases

**Final Status:** ✅ All 275 pdf_sources references verified - 0 errors remaining

---

## Methodology

### Phase 1: Automated Verification

**Script:** `scripts/qa_name_mapping_sources.py`

**Process:**

1. Built comprehensive file index of 2,106 files across project directories
2. Verified each pdf_sources reference against actual filesystem
3. For missing files, cross-referenced with attribution.csv to find correct source
4. Applied automated corrections where match confidence was high

**Phase 1 Results:**

- 10 corrections applied automatically
- 8 remaining errors requiring manual investigation

### Phase 2: Manual Corrections

**Issue Identified:** Inconsistent diary file naming conventions

**Root Cause:**

- Team A: "Diary Team A.doc" (with spaces) ✅ Correct
- Team B: Actual file is "DiaryTeamB.doc" (no spaces), but CSV had "Diary Team B.doc" ❌
- Team C: Actual file is "The Diary of Team C.doc", but CSV had "Diary Team C.doc" ❌

**Script:** `scripts/fix_diary_filenames.py`

**Process:**

1. Systematically replaced incorrect diary filenames:
   - "Diary Team B.doc" → "DiaryTeamB.doc"
   - "Diary Team C.doc" → "The Diary of Team C.doc"
2. Applied corrections across all 282 rows
3. Re-verified all pdf_sources references

**Phase 2 Results:**

- 22 corrections applied
- All diary filename references standardised to match actual files

---

## Detailed Corrections

### Phase 1: Automated Corrections (10 entries)

| Row | Extracted Name | Issue | Resolution |
|-----|----------------|-------|------------|
| 56 | Reza | Multiple sources, only one verified | Corrected to D_2010Summary.pdf |
| 67 | Georgi | Wrong source file | Updated source reference |
| 85 | Tereza | Incomplete source list | Added A_2010Diary_BG.doc, B_2010Diary_En.doc |
| 86 | Todor | Missing diary source | Added C_2010Diary_BG.doc |
| 87 | Jana | Missing diary source | Added C_2010Diary_BG.doc |
| 88 | Zhoro | Missing diary source | Added D_2010Diary_BG.doc |
| 89 | Bara | Duplicate sources | De-duplicated, added C_2010Diary_BG.doc |
| 104 | AD | Excessive sources | Narrowed to Day_03.pdf |
| 105 | ET | Excessive sources | Narrowed to Day_03.pdf |
| 193 | Petra | Incomplete sources | Added A_2009Summary.pdf, A_2010Diary_BG.doc, B_2010Diary_En.doc |

### Phase 2: Diary Filename Corrections (22 entries)

**Pattern:** Fixed systematic naming inconsistencies for Elhovo 2009 autumn season diaries

**Affected Rows:** 2, 3, 36, 67, 71-82, 84, 86, 88, 90, 103, 225

**Key Corrections:**

- **Lizzy** (Row 2): "Diary Team B.doc" → "DiaryTeamB.doc"
- **Lisi** (Row 3): Both Team B and Team C diary references corrected
- **Georgi** (Row 67): "Diary Team C.doc" → "The Diary of Team C.doc"
- **Scott, Stanislav** (Rows 77-78): Both Team B and Team C references corrected
- **Jarka, Javor, Radko, Sona** (Rows 79-82): Team C diary corrected

---

## Verification Results

### Final Verification Run

```text
Total rows checked: 282
Rows with pdf_sources: 275
Erroneous entries found: 0
Corrections applied: 0
```

✅ **All pdf_sources successfully verified**

---

## File Locations Confirmed

### Elhovo 2009 Autumn Diaries

- **Team A:** `Elhovo 2010-12-12/2009/Project Records/Team A/Diary Team A.doc`
- **Team B:** `Elhovo 2010-12-12/2009/Project Records/Team B/DiaryTeamB.doc`
- **Team C:** `Elhovo 2010-12-12/2009/Project Records/Team C/The Diary of Team C.doc`

### Kazanlak Diaries and PDFs

All Kazanlak diary and PDF references verified against files in:

- `Kazanluk/2009/Project Records/Team*/`
- `Kazanluk/2010/Project Records/Team*/`
- `Kazanluk/2011/Project Records/Team*/`

### Elhovo 2010 PDFs

All Elhovo 2010 daily form PDF references verified against:

- `Elhovo 2010-12-12/2010/Project Records/Team A/`
- `Elhovo 2010-12-12/2010/Project Records/Team B/`

---

## Impact Assessment

### Data Quality Improvements

1. **Referential Integrity:** All 275 pdf_sources now point to verifiable files
2. **Traceability:** Each ambiguous name can now be reliably traced to source documents
3. **Consistency:** Standardised diary filename references across all seasons

### Downstream Benefits

- Manual PDF review for ambiguous names now reliable (all sources findable)
- Future data extraction can trust pdf_sources field
- Audit trail complete for all extracted walker names

---

## Lessons Learned

### Naming Convention Issues

**Problem:** Inconsistent file naming across different seasons/locations

**Solution:** Created comprehensive file index with fuzzy matching capabilities

### Systemic Errors

**Problem:** Diary filename patterns not consistently captured during initial extraction

**Root Cause:** Different directory structures and naming conventions between Elhovo and Kazanlak seasons

**Resolution:** Manual investigation and systematic correction of all affected entries

---

## Recommendations

### For Future Data Extraction

1. **Create file inventory first:** Index all source files before extraction begins
2. **Validate sources immediately:** Check pdf_sources references during extraction, not after
3. **Standardise naming:** Document and normalise file naming conventions early

### For Ongoing Work

1. **Review similar fields:** Consider QA verification for XLS_Source field in attribution.csv
2. **Document conventions:** Create reference guide for file naming patterns across seasons
3. **Automate validation:** Integrate pdf_sources verification into extraction pipeline

---

## QA Scripts Created

1. **`scripts/qa_name_mapping_sources.py`**
   - Comprehensive file existence verification
   - Cross-reference with attribution.csv
   - Automated correction where confidence high
   - Reusable for future QA needs

2. **`scripts/fix_diary_filenames.py`**
   - Targeted correction for diary naming inconsistencies
   - Documents specific Elhovo 2009 autumn issue
   - Preserves audit trail of changes

---

## Conclusion

All 32 erroneous pdf_sources entries have been successfully identified and corrected. The name-mapping.csv file now has complete referential integrity, with all 275 pdf_sources references verified against actual files in the project directory structure.

This QA process uncovered and resolved systematic naming inconsistencies, particularly for Elhovo 2009 autumn season diaries, ensuring reliable traceability for all extracted walker names.

---

**QA Conducted By:** Claude Code in collaboration with Dr. Adela Sobotkova

**Scripts:** `qa_name_mapping_sources.py`, `fix_diary_filenames.py`

**Date Completed:** 21 November 2025
