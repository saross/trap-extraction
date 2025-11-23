# Manual Extraction Guide

**Created:** 22 November 2025
**Purpose:** Guide for manual resolution of diary extraction issues

---

## Issue 1: Date Discrepancy - ✅ RESOLVED

### The Problem

**Record:** 2010-03-08, Team C, Leader: Bara
**Issue:** The Excel SurveySummary listed this as 8 March 2010, but the diary entry was dated **18 March 2010** (18.03.2010)

### Resolution (Completed 23 November 2025)

**Determination:** The Excel file contained an error. The correct date was **2010-04-08** (8 April), not 2010-03-08 (8 March).

**Investigation findings:**
- The diary entry dated "18.03.2010" was for **18 March** - a separate, correct entry
- **08 March** could not exist because the survey season started 17 March
- Row 45 in Excel SurveySummary incorrectly showed 2010-03-08 but should have been 2010-04-08
- Row 30 with 2010-03-18 was already correct and matched diary/PDF sources
- 08 April diary entry was missing, but PDF exists (`C_20100408.pdf`)

**Actions completed:**
- ✅ Created corrected Excel file: `Kaz10_SurveySummary-NEW-2025-correction.xlsx`
- ✅ Deleted incorrect 2010-03-08 Team C entry from attribution.csv
- ✅ Transferred survey units (30742-30773) to correct 2010-04-08 entry
- ✅ Verified 2010-03-18 entry already correct with walker data from diary
- ✅ Created backup: `attribution.csv.backup_date_correction`

**Result:**
- Total records: 269 → 268 (1 duplicate removed)
- 2010-04-08 Team C now has complete data (units + walkers from PDF)
- 2010-03-18 Team C confirmed correct with walker data from diary

**Note:** The corrected Excel file should be cascaded to all copies of TRAP 2010 data outside the regular backup pipeline.

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

**Suggested resolution:** You are correct, this diary has only a single list of walkers at the beginning of the diary. Teams were often, but not always, stable. Course of action: *default* to this list of walkers for every day of the season for this team *unless* individual diary entries *or* another source (such as the scans of the daily progress sheets) indicate different walkers, in which case prioritise the specific list from the daily diary entry or the other source.

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

**Suggested resolution:** In this diary, Adela seems to have incorporated walker lists into the narrative on many days. These lists sometimes contain valuable information about who is doing what, e.g., from Tuesday 13 October: 'Team A continues in usual setup ( Martin – GPS, Aneta- recording, me – PDA, Ilija – consultation, Eric- pottery)'. Course of action: read each diary entry and look for the walkers plus additional role information where available using NLP rather than a script. Note language like 'usual setup' to determine default walkers, and use those on days where no contradictory, specific walker information is given. Specific information on any given day supercedes default walkers, as does specific information in other sources like scanned daily progress forms. In short, you should be able to determine defaults, and use those *unless* specific information contradicting the defaults is provided by a daily diary entry or another source.
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

**Suggested resolution:** The diary entry shows '6 April 2010 – Rainy day, no fieldwalking, documentation day and  visiting of Roman sites with Jiri Musil followed by the Tour of the mounds'. So, no fieldwalking that day (I'm not sure why the script picked up the holiday but not the 'rainy day, no fieldwalking' here). Course of action: nothing missing, no survey on 2010-04-06.

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

**Suggested resolution:** 28.03.2010 is the last entry in A_2010Diary_BG.doc. There are no later entries, including for 07.04 or 08.04. HOWEVER, if you look at the *English* diary (A_2010Diary_En.docx), there are entries for '7th April 2010' and '8 April 2010'. These entries seem very complete, including lists of all walkers, name of the leader, etc. Course of action: Use the English diary (A_2010Diary_En.docx) for these days. Also, promote the English library to 'primary' in our source-inventory, explaining that the BG and EN diaries have different data coverage.
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

**Suggested resolution:** 2010-04-07 exists in C_2010Diary_BG.doc. The entry is titled '7. IV. 2010 – Сряда'. It contains a list of walkers and other expected information. Course of action: re-extract now that you know the heading for the entry, or explain further what the problem is. Furthermore, expect this format of date (Arabic numeral = day [dot] Roman numeral = month [dot] arabic numeral = year) and extract any other dates you missed, there are many more than just the 24th and 25th. I see that dates are presented in several formats, you may need to use NLP rather than a script, or update your script to cover all date formats used in this document. Furthermore, you should check other diaries for non-standard or unexpected date formats, particularly in the Bulgarian diaries. 

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

**Suggested resolution:** I installed pandoc for your, but if you need something else installed, ask, since we have many .docx files that need to be examined. Also, be sure to use the 'Team B Diary new.docx' file, which has superseded file you examined. I can confirm that 14 November 2010 exists, with detailed information about who was operating the PDA and who was keeping paper records. Course of action: interact with .docx files using pandoc, *or* request me to install necessary libraries / utilities; re-extract as needed to cover all dates in this diary. Note that you *may* have already extracted this data when you updated extraction to the 'new' diary (a task you have been working on while I undertake this manual review). 

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

**Suggested resolution:** A brief entry exists for 2011-10-24; I have pasted it in full below. Course of action: update based on the text I provide here:

24.10.2011 г., понеделник
Дъждовен ден. Не се обхожда. Работа в базата
Група от 5 човека в състав ГН., ЮЦ, ЕТ, Анани Антонов, Ал.Р посещават въведени в АКБ обекти с цел вземане на координати и актуализиране на теренната инф. Посетени са 2 надгробни могили в землище на с. Шейново. Те получават полеви номера 1059 и 1060.

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

**Suggested resolution:** 2011-11-08 exists in the diary, under the heading 'Date: 08 November, Tuesday, overcast, fog lifting in midafternoon'. Course of action: please attempt extraction again. I see nothing that should interfer with re-extraction. 

---

##### 10. 2011-11-10, Team D

**File:** `D_2011Diary_BG.doc`
**Location:** `Kazanluk/2011-11-30/Project Records/Team D/`
**Format:** Structured Bulgarian (script extracted 11-01, 11-02 successfully)

**Manual extraction process:**
```bash
antiword "/media/shawn/191c3b96-5fa5-4d0d-8805-0cf05d3d8468/synology/Adela/TRAP-WD-2020-04/Kazanluk/2011-11-30/Project Records/Team D/D_2011Diary_BG.doc" | grep -A 15 "10.11.2011"
```

**Suggested resolution:** The final day of Team D fieldwork in the diary is 2011-11-02 ('02.11.2011(четвъртък)'). Course of action: no diary information available for 10 November 2011 in D_2011Diary_BG.doc; rely on other sources.

---

##### 11. 2011-11-29, Team B

**File:** `B_2011Diary_En.docx`
**Location:** `Kazanluk/2011-11-30/Project Records/Team B/`
**Format:** Structured EN (.docx) - same file as record #9

**Manual extraction process:**
```bash
unzip -p "/media/shawn/191c3b96-5fa5-4d0d-8805-0cf05d3d8468/synology/Adela/TRAP-WD-2020-04/Kazanluk/2011-11-30/Project Records/Team B/B_2011Diary_En.docx" word/document.xml | grep -A 30 "29 November\|November 29"
```

**Suggested resolution:** The final day of Team B fieldwork in the diary is 2011-11-28 ('28 November, Monday'). Course of action: no diary information available for 29 November 2011 in B_2011Diary_EN.docx; rely on other sources.


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

- [x] **PRIORITY**: Resolve 2010-03-08 date discrepancy ✅ **COMPLETED** (23 Nov 2025)
  - [x] Check Excel SurveySummary for 2010-03-18
  - [x] Read diary entry content
  - [x] Compare unit numbers
  - [x] Make decision and update attribution.csv
  - [x] Document in Extraction_Notes

- [x] Process failed extractions ✅ **COMPLETED** (23 Nov 2025)
  - [x] #1: 2009-10-23, Team C - Use default walker list ✅
  - [x] #2: 2009-11-14, Team A - Extract with NLP from narrative ✅
  - [x] #3: 2010-04-06, Team B - N/A (no fieldwalking, rainy day) ✅
  - [x] #4-5: 2010-04-07/08, Team A - Extract from EN diary, promote to co-PRIMARY ✅
  - [x] #6: 2010-04-07, Team C - Re-extract with multiple date format awareness ✅
  - [x] #7: 2010-11-14, Team B - Already extracted in supersession project ✅
  - [x] #8: 2011-10-24, Team A - Extract from provided Bulgarian text ✅
  - [x] #9: 2011-11-08, Team B - Re-attempt extraction ✅
  - [x] #10: 2011-11-10, Team D - N/A (no diary entry available) ✅
  - [x] #11: 2011-11-29, Team B - N/A (no diary entry available) ✅

- [ ] Create git commit when complete
  - [ ] Commit message: "feat(data): Manual extraction for remaining diary records"
  - [ ] Include note about all resolutions applied

---

## Questions or Issues?

If you encounter problems with any extraction:

1. **Can't find date entry:** The entry may be missing or use a different date format
2. **No walker list found:** Some days may genuinely have no walker data recorded
3. **Uncertain transliteration:** Compare with existing Bulgarian names in attribution.csv
4. **File access issues:** Check file permissions and paths

Document any unresolvable issues in `outputs/manual-extraction-work.csv` Notes column.

---

## Completion Summary

**Completion date:** 23 November 2025

All manual extractions have been completed successfully. The following records were updated in `attribution.csv`:

### Records Updated

1. **2009-10-23, Team C**: Bara | Petra | Sona | Tereza | Todor | Georgi
   - Source: The Diary of Team C.doc (default walker list)
   - Resolution: Used team-wide walker list from diary header

2. **2009-11-14, Team A**: Adela | Katya | Marto
   - Source: Diary Team A.doc
   - Resolution: Extracted from narrative text using NLP approach

3. **2010-04-07, Team A**: Stanislav | Martin | Viki | Petra
   - Source: A_2010Diary_En.docx
   - Resolution: Extracted from EN diary (BG diary ends 28 March)
   - Roles: GPS: Stanislav, PDA: Petra, Leader: Petra, Author: Petra Tuslova

4. **2010-04-08, Team A**: Petra | Viki | Lindsay | Stanislav | Marto
   - Source: A_2010Diary_En.docx
   - Resolution: Extracted from EN diary (BG diary ends 28 March)
   - Roles: GPS: Stanislav, PDA: Petra, Leader: Petra, Author: Lindsay

5. **2010-04-07, Team C**: Elena | Bara | Sonya | Todor | Lindsay
   - Source: C_2010Diary_BG.doc
   - Resolution: Re-extracted with Roman numeral date format awareness (7. IV. 2010)

6. **2011-10-24, Team A**: GN | YuTs | ET | Anani Antonov | Al.R
   - Source: A_2011Diary_BG.doc
   - Resolution: Rainy day with site visits (no survey walking)

7. **2011-11-08, Team B**: Petra | Adela | Bethan | Elaine | Hamish
   - Source: B_2011Diary_En.docx
   - Resolution: Re-extracted using pandoc for .docx format

### Additional Actions

- **Source inventory updated**: A_2010Diary_En.docx promoted to co-PRIMARY status for Kazanlak 2010 Team A
  - Coverage note added: BG diary covers 17 March to 28 March; EN diary covers April entries (7-9 April)

### Files Created

- `scripts/update_manual_extractions.py` - Python script for updating attribution CSV
- `outputs/attribution.csv.backup_manual_20251123_134623` - Backup before manual updates

### Verification

All 7 manual extractions verified successfully:
- ✅ Walker data present in all records
- ✅ Source references updated
- ✅ Extraction notes added
- ✅ Role data added where available

---

**Last updated:** 23 November 2025
