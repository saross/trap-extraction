# Team A Diary Supersession Report

**Date:** 23 November 2025
**Issue:** Elhovo 2010 Team A records extracted from Tier 3 PDF sources need updating to PRIMARY diary source

## Background

The source inventory indicates that "A_Diary.docx" (26 KB, March 2011) is the PRIMARY source for Elhovo/Yambol 2010 Team A, containing post-season data quality corrections. However, the current attribution CSV contains data extracted from PDF files (Day_XX.pdf) which are Tier 3 sources (scanned forms) and less reliable than the Tier 2 diary source.

## Sources

- **PRIMARY (should use):** `A_Diary.docx` - Post-season corrected version from March 2011
- **Tier 3 (currently used):** Various Day_XX.pdf files - Scanned daily progress forms with OCR errors and incomplete role data

## Comparison: Existing CSV vs PRIMARY Diary

### 2010-10-22

**Current (from Day_03.pdf, form 1):**
- Leader: Adela D
- Walkers: Adela Sobotkova | Royce Lawrence | AD | ET | RL | Adela Dorňáková
- PDA: (blank)
- GPS: (blank)
- Forms: (blank)
- Author: Royce L
- Source: Day_03.pdf

**PRIMARY Diary shows:**
- Leader: Adela D.
- Walkers: AS | RL | PT | BW | EJ | AD (6 walkers)
- PDA: EJ | AD (Emma + Adela D; 2 PDAs)
- GPS: AS (Adela S.)
- Forms: (not mentioned)
- Author: Adela Dornakova
- Source: A_Diary.docx

**Changes needed:** Fix walker list (remove duplicates, use consistent initials); add PDA and GPS roles; correct author

---

### 2010-10-23

**Current (from Day_03.pdf, form 2):**
- Leader: Adela D
- Walkers: AD | RL | AS | Emma Jakobsson | VC
- PDA: (blank)
- GPS: (blank)
- Forms: (blank)
- Author: Royce L
- Source: Day_03.pdf

**PRIMARY Diary shows:**
- Leader: Adela D.
- Walkers: AS | RL | VC | EJ | AD (5 walkers)
- PDA: EJ | AD (Emma + Adela D)
- GPS: AS (Adela S.)
- Forms: (not mentioned)
- Author: Viktoria Chystyakova
- Source: A_Diary.docx

**Changes needed:** Reorder walker list for consistency; add PDA and GPS roles; correct author

---

### 2010-10-24

**Current (from Day_03.pdf, form 3):**
- Leader: Adela D
- Walkers: AS | RL | AD | VC | Emma Jakobsson
- PDA: (blank)
- GPS: (blank)
- Forms: (blank)
- Author: Royce L
- Source: Day_03.pdf

**PRIMARY Diary shows:**
- Leader: Adela D.
- Walkers: AS | RL | VC | EJ | AD (5 walkers)
- PDA: EJ | AD (Emma + Adela D)
- GPS: AS (Adela S.)
- Forms: (not mentioned)
- Author: Viktoria Chystyakova
- Source: A_Diary.docx

**Changes needed:** Reorder walker list for consistency; add PDA and GPS roles; correct author

---

### 2010-11-02

**Current (from Day_05.pdf, form 1):**
- Leader: Petra T
- Walkers: Adela Sobotkova | Elena | Drago | Bistra
- PDA: (blank)
- GPS: (blank)
- Forms: (blank)
- Author: Drago G
- Source: Day_05.pdf

**PRIMARY Diary shows:**
- Leader: Petra
- Walkers: AS | PT | DG | BW | EJ (5 walkers)
- PDA: PT (Petra)
- GPS: AS (Adéla)
- Forms: (not mentioned)
- Author: Bara W.
- Source: A_Diary.docx

**Changes needed:** Fix walker list (Elena/Bistra are incorrect - should be BW/Bara and EJ/Emma); add PDA and GPS roles; correct author; add PT to walker list

---

### 2010-11-03

**Current (from Day_05.pdf, form 2):**
- Leader: Petra
- Walkers: Petra Tušlová | Viktorie Chystyaková | Drago | Adela Sobotkova | Emma
- PDA: (blank)
- GPS: (blank)
- Forms: (blank)
- Author: Emma
- Source: Day_05.pdf

**PRIMARY Diary shows:**
- Leader: Petra
- Walkers: AS | VC | DG | EJ | PT (5 walkers)
- PDA: PT (Petra)
- GPS: AS (Adéla S.)
- Forms: (not mentioned)
- Author: Petra T.
- Source: A_Diary.docx

**Changes needed:** Use consistent initials for walker list; add PDA and GPS roles; correct author

---

## Summary

- **5 records need updating** to use PRIMARY diary source instead of Tier 3 PDFs
- **All 5 records** are missing PDA and GPS role data that is present in the diary

## Key Improvements from PRIMARY Source

1. **Complete role data:** PDA and GPS operators are specified in diary but missing from PDFs
2. **Correct walker lists:** Diary provides accurate walker names/initials, PDFs have OCR errors and incorrect names
3. **Consistent formatting:** Diary uses standard initials throughout
4. **Post-season corrections:** March 2011 version includes data quality fixes
5. **Correct author attribution:** Diary explicitly states who wrote each entry (PDFs show photographer as author)

## Recommended Action

1. Update all 5 affected records in attribution.csv with data from PRIMARY diary
2. Update PDF_Source column to reference "A_Diary.docx" instead of Day_XX.pdf
3. Add note in Extraction_Notes indicating data updated from PRIMARY source

## Name/Initial Expansion Guide

Based on diary cross-referencing:

- AS = Adela Sobotkova (Adela S., Adéla S.)
- RL = Royce Lawrence (Royce)
- PT = Petra Tušlová (Petra, Petra T.)
- BW = Bara Weissova (Bara, Bara W.)
- EJ = Emma Jakobsson (Emma)
- AD = Adela Dornakova (Adela D., Adela Dorňáková)
- VC = Viktoria Chystyakova (Viktoria, Viki)
- DG = Daniel Giannangelo (Drago)

## Issues with Current PDF Data

1. **2010-10-22:** Duplicate entries (AD, Adela Dorňáková appear twice in walker list); ET not identified
2. **2010-11-02:** Incorrect walker names (Elena, Bistra not in diary - should be Bara, Emma)
3. **All dates:** Author shown as photographer, not diary author
4. **All dates:** No PDA or GPS role data despite both being used every day
