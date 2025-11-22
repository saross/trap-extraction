# Manual Extraction Guide

**Created:** 22 November 2025
**Purpose:** Guide for manual resolution of diary extraction issues

---

## Issue 1: Date Discrepancy - IMMEDIATE ATTENTION REQUIRED

### The Problem

**Record:** 2010-03-08, Team C, Leader: Bara
**Issue:** The Excel SurveySummary lists this as 8 March 2010, but the diary entry is dated **18 March 2010** (18.03.2010)

### File Location

**File:** `C_2010Diary_BG.doc`
**Full path:** `/media/shawn/191c3b96-5fa5-4d0d-8805-0cf05d3d8468/synology/Adela/TRAP-WD-2020-04/Kazanluk/2010/Project Records/Team C/C_2010Diary_BG.doc`
**Version:** PRIMARY (214 KB) - Most complete Bulgarian diary

### Walker Data Found

The diary entry for **18 March 2010** contains walker data that was **NOT** extracted due to the date mismatch.

### Decision Required

You need to determine which date is correct:

**Option A: Excel is wrong, diary is correct (18 March)**
- Action: Change date in attribution.csv from 2010-03-08 to 2010-03-18
- Re-run extraction script to capture walker data
- Check if 2010-03-18 already exists as a separate record

**Option B: Diary is wrong, Excel is correct (8 March)**
- Action: Manually extract walker data from the 18 March diary entry
- Apply to the 2010-03-08 record
- Note discrepancy in Extraction_Notes

**Option C: Both are correct (two different survey days)**
- Possibility: Typo in diary header, content actually from 8 March
- Action: Review diary content context to determine actual date
- Check if 2010-03-18 exists as a separate record in Excel

### How to Investigate

1. **Check Excel SurveySummary:**
   ```
   File: Kazanluk/2010/Project Records/Master Records/Kaz10_SurveySummary.xls
   Look for: Does 2010-03-18 Team C exist as a separate entry?
   ```

2. **Read diary entry:**
   ```bash
   antiword "/media/shawn/191c3b96-5fa5-4d0d-8805-0cf05d3d8468/synology/Adela/TRAP-WD-2020-04/Kazanluk/2010/Project Records/Team C/C_2010Diary_BG.doc" | grep -A 30 "18.03.2010"
   ```

3. **Check survey unit numbers:**
   - Compare unit numbers in diary entry vs Excel record
   - Matching units = same survey day (date typo somewhere)
   - Different units = different survey days

### Recommended Workflow

```
1. Open Kaz10_SurveySummary.xls
2. Search for Team C entries between 2010-03-08 and 2010-03-18
3. Note the unit ranges for each entry
4. Read the 18 March diary entry
5. Match unit numbers to determine correct date
6. Make decision and document in attribution.csv Extraction_Notes
```

### After Decision

If you determine the correct date and walker data, update `attribution.csv` manually:
- Locate the row: Date=2010-03-08, Team=C
- Update Walkers_Original and Walkers_Transliterated columns
- Add note to Extraction_Notes: "Date verified as [correct date]; walker data from diary entry dated 18.03.2010"

---

## Issue 2: Failed Extractions (12 Records)

### Why They Failed

These diaries have **overall team walker lists** (listed once at the beginning of the season/period) rather than **daily walker lists** (repeated for each day). The extraction script was designed for daily lists.

### The 12 Failed Records

#### Group A: Elhovo 2009 Diaries with Overall Lists

##### 1. 2009-10-23, Team C

**File:** `The Diary of Team C.doc`
**Location:** `Elhovo 2010-12-12/2009/Project Records/Team C/`
**Format:** Overall walker list at top of diary

**What the diary shows:**
```
The Diary of Team C
Walkers: Bara, Petra, Sona, Tereza, Todor, Georgi
```

**Manual extraction process:**
1. Open the diary file
2. Find the overall walker list at the top
3. Verify this team composition is consistent for the entire period
4. If team composition changed during the season, check the specific date entry
5. Apply the walker list to attribution.csv

**Command to extract:**
```bash
antiword "/media/shawn/191c3b96-5fa5-4d0d-8805-0cf05d3d8468/synology/Adela/TRAP-WD-2020-04/Elhovo 2010-12-12/2009/Project Records/Team C/The Diary of Team C.doc" | head -10
```

**Expected walkers:** Bara | Petra | Sona | Tereza | Todor | Georgi

---

##### 2. 2009-11-14, Team A

**File:** `Diary Team A.doc`
**Location:** `Elhovo 2010-12-12/2009/Project Records/Team A/`
**Format:** Overall walker list or daily narrative

**Manual extraction process:**
1. The script successfully extracted 2009-11-09 from this diary
2. Try the same approach for 2009-11-14
3. Search for the date entry and look for team composition

**Command to check:**
```bash
antiword "/media/shawn/191c3b96-5fa5-4d0d-8805-0cf05d3d8468/synology/Adela/TRAP-WD-2020-04/Elhovo 2010-12-12/2009/Project Records/Team A/Diary Team A.doc" | grep -A 15 "14 November"
```

---

#### Group B: Kazanlak 2010 Spring Records

##### 3. 2010-04-06, Team B

**File:** `B_2010Diary_En.doc`
**Location:** `Kazanluk/2010/Project Records/Team B/`
**Format:** Structured EN (script extracted 2010-04-02, 04-07, 04-08 successfully)

**Manual extraction process:**
1. This is puzzling - the script worked for other dates in the same file
2. Likely the 6 April entry has a different format or is missing
3. Check if 6 April was a non-working day (Easter holiday period?)

**Command to check:**
```bash
antiword "/media/shawn/191c3b96-5fa5-4d0d-8805-0cf05d3d8468/synology/Adela/TRAP-WD-2020-04/Kazanluk/2010/Project Records/Team B/B_2010Diary_En.doc" | grep -A 30 "6 April\|April 6"
```

**Note:** Script showed "3 – 5 April 2010 Easter Holiday" in earlier extraction - 6 April may be immediately after holiday with no entry.

---

##### 4-5. 2010-04-07, Team A and 2010-04-08, Team A

**File:** `A_2010Diary_BG.doc`
**Location:** `Kazanluk/2010/Project Records/Team A/`
**Format:** Structured Bulgarian

**Manual extraction process:**
1. Extract text and search for dates: 07.04.2010 and 08.04.2010
2. Look for "Група:" pattern
3. Transliterate Bulgarian names using the pattern in diary-extraction-plan.md

**Command to extract:**
```bash
antiword "/media/shawn/191c3b96-5fa5-4d0d-8805-0cf05d3d8468/synology/Adela/TRAP-WD-2020-04/Kazanluk/2010/Project Records/Team A/A_2010Diary_BG.doc" | grep -A 15 "07.04.2010\|08.04.2010"
```

---

##### 6. 2010-04-07, Team C

**File:** `C_2010Diary_BG.doc`
**Location:** `Kazanluk/2010/Project Records/Team C/`
**Format:** Structured Bulgarian (script extracted 03-24, 03-25 successfully)

**Manual extraction process:**
1. Similar to Team A - structured Bulgarian format
2. Script worked for other dates, so format should be consistent
3. Check for the specific date entry

**Command to extract:**
```bash
antiword "/media/shawn/191c3b96-5fa5-4d0d-8805-0cf05d3d8468/synology/Adela/TRAP-WD-2020-04/Kazanluk/2010/Project Records/Team C/C_2010Diary_BG.doc" | grep -A 15 "07.04.2010"
```

---

#### Group C: Yambol 2010 Autumn

##### 7. 2010-11-14, Team B

**File:** `Team B Diary.docx`
**Location:** `Elhovo 2010-12-12/2010/Project Records/Team B/`
**Format:** Structured EN with roles (.docx file)

**Manual extraction process:**
1. This is a .docx file, may have extraction issues
2. Script used fallback XML extraction method (python-docx not installed)
3. May need to open in LibreOffice or export to .doc format

**Command to check:**
```bash
# Try unzip method
unzip -p "/media/shawn/191c3b96-5fa5-4d0d-8805-0cf05d3d8468/synology/Adela/TRAP-WD-2020-04/Elhovo 2010-12-12/2010/Project Records/Team B/Team B Diary.docx" word/document.xml | grep -A 30 "14"
```

**Alternative:** Open in LibreOffice and manually search for 14 November entry

---

#### Group D: Kazanlak 2011 Autumn Records

##### 8. 2011-10-24, Team A

**File:** `A_2011Diary_BG.doc`
**Location:** `Kazanluk/2011-11-30/Project Records/Team A/`
**Format:** Structured Bulgarian

**Manual extraction process:**
```bash
antiword "/media/shawn/191c3b96-5fa5-4d0d-8805-0cf05d3d8468/synology/Adela/TRAP-WD-2020-04/Kazanluk/2011-11-30/Project Records/Team A/A_2011Diary_BG.doc" | grep -A 15 "24.10.2011"
```

---

##### 9. 2011-11-08, Team B

**File:** `B_2011Diary_En.docx`
**Location:** `Kazanluk/2011-11-30/Project Records/Team B/`
**Format:** Structured EN (.docx)

**Manual extraction process:**
```bash
unzip -p "/media/shawn/191c3b96-5fa5-4d0d-8805-0cf05d3d8468/synology/Adela/TRAP-WD-2020-04/Kazanluk/2011-11-30/Project Records/Team B/B_2011Diary_En.docx" word/document.xml | grep -A 30 "8 November\|November 8"
```

**Alternative:** Open in LibreOffice

---

##### 10. 2011-11-10, Team D

**File:** `D_2011Diary_BG.doc`
**Location:** `Kazanluk/2011-11-30/Project Records/Team D/`
**Format:** Structured Bulgarian (script extracted 11-01, 11-02 successfully)

**Manual extraction process:**
```bash
antiword "/media/shawn/191c3b96-5fa5-4d0d-8805-0cf05d3d8468/synology/Adela/TRAP-WD-2020-04/Kazanluk/2011-11-30/Project Records/Team D/D_2011Diary_BG.doc" | grep -A 15 "10.11.2011"
```

---

##### 11. 2011-11-29, Team B

**File:** `B_2011Diary_En.docx`
**Location:** `Kazanluk/2011-11-30/Project Records/Team B/`
**Format:** Structured EN (.docx) - same file as record #9

**Manual extraction process:**
```bash
unzip -p "/media/shawn/191c3b96-5fa5-4d0d-8805-0cf05d3d8468/synology/Adela/TRAP-WD-2020-04/Kazanluk/2011-11-30/Project Records/Team B/B_2011Diary_En.docx" word/document.xml | grep -A 30 "29 November\|November 29"
```

---

## Recommended Workflow for Manual Extraction

### Step 1: Create a Working Document

Create a file: `outputs/manual-extraction-work.csv`

Headers:
```csv
Date,Team,Walker_Data,Source,Notes,Status
```

### Step 2: Process Each Record

For each of the 12 failed records:

1. **Run the suggested command** to view diary content
2. **Identify walker names** in the entry
3. **Transliterate if Bulgarian** (use the mapping in scripts/extract_diary_walkers.py)
4. **Record in working CSV:**
   ```csv
   2009-10-23,C,"Bara | Petra | Sona | Tereza | Todor | Georgi","Overall list at top of diary",extracted
   ```

### Step 3: Apply to attribution.csv

Once you have all 12 records extracted:

1. **Create backup:**
   ```bash
   cp outputs/attribution.csv outputs/attribution.csv.backup_manual
   ```

2. **Edit attribution.csv** (use LibreOffice Calc or similar):
   - Find each record by Date + Team
   - Update `Walkers_Original` column with pipe-delimited names
   - Update `Walkers_Transliterated` column (same for non-Bulgarian names)
   - Add note to `Extraction_Notes`: "Manually extracted from diary [date]"

3. **Verify changes:**
   ```bash
   # Count updated records
   grep "Manually extracted" outputs/attribution.csv | wc -l
   # Should show 12 (or 13 if you also fixed the date discrepancy)
   ```

---

## Bulgarian to Latin Transliteration Guide

For Bulgarian names, use this reference from successful extractions:

**Pattern Examples:**
- `Г. Нехризов` → `G. Nekhrizov`
- `Ю. Цветкова` → `Yu. Tsvetkova`
- `Б. Лилова` → `B. Lilova`
- `Н. Кечева` → `N. Kecheva`
- `Л. Марковски` → `L. Markovski`

**Common Cyrillic → Latin mappings:**
- Г → G
- Ю → Yu
- Ц → Ts
- Б → B
- Н → N
- Л → L
- к → k
- в → v
- х → kh

Full mapping table available in `scripts/extract_diary_walkers.py` (lines 45-52)

---

## Summary Checklist

- [ ] **PRIORITY**: Resolve 2010-03-08 date discrepancy
  - [ ] Check Excel SurveySummary for 2010-03-18
  - [ ] Read diary entry content
  - [ ] Compare unit numbers
  - [ ] Make decision and update attribution.csv
  - [ ] Document in Extraction_Notes

- [ ] Process 12 failed extractions
  - [ ] Extract walker data for each record
  - [ ] Transliterate Bulgarian names
  - [ ] Record in working CSV
  - [ ] Update attribution.csv
  - [ ] Verify all 12 are complete

- [ ] Create git commit when complete
  - [ ] Commit message: "feat(data): Manual extraction for 12 failed diary records"
  - [ ] Include note about date discrepancy resolution

---

## Questions or Issues?

If you encounter problems with any extraction:

1. **Can't find date entry:** The entry may be missing or use a different date format
2. **No walker list found:** Some days may genuinely have no walker data recorded
3. **Uncertain transliteration:** Compare with existing Bulgarian names in attribution.csv
4. **File access issues:** Check file permissions and paths

Document any unresolvable issues in `outputs/manual-extraction-work.csv` Notes column.

---

**Last updated:** 22 November 2025
