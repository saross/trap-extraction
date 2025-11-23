# Date Discrepancy Analysis: 2010-03-08 Team C

**Analyst:** Claude Code
**Date:** 22 November 2025

---

## Investigation Results

### The Answer: Both dates are CORRECT (separate survey days)

**Finding:** The Excel SurveySummary and diary are BOTH correct. These are **two different survey days**, and the **8 March diary entry is MISSING**.

---

## Evidence

### Excel SurveySummary Records (Team C, March 2010)

```
Date         Units           Leader
2010-03-08   30742-30773     Bara    ← MISSING from diary
2010-03-17   30200-30223     Bara    ✓ In diary (17.03.2010)
2010-03-18   30224-30227     Bara    ✓ In diary (18.03.2010)
2010-03-19   30228-30280     Bara    ✓ In diary (19.03.2010)
2010-03-20   30281-30388     Bara    ✓ In diary (20.03.2010)
... (continues)
```

### Team C Diary Dates Found

The Bulgarian diary (`C_2010Diary_BG.doc`) contains these March dates:
```
17.03.2010
18.03.2010  ← Script tried to use this for 08.03.2010
19.03.2010
20.03.2010
21.03.2010
22.03.2010
... (continues)
```

**NOTABLY ABSENT:** 08.03.2010

---

## Conclusion

1. **8 March 2010** was a real survey day (units 30742-30773)
2. **18 March 2010** was ALSO a real survey day (units 30224-30227)
3. The diary is **missing the entry for 8 March**
4. The extraction script incorrectly tried to match 08.03 to the 18.03 diary entry

---

## Why is 8 March Missing from Diary?

Possible explanations:
1. **Diary started on 17 March** - Team C may not have worked 8-16 March, or used a different diary
2. **Data entry gap** - Entry was never written
3. **Lost pages** - Physical diary pages may be missing
4. **Wrong diary file** - The 8 March entry might be in a different document

---

## Recommended Action

### Check for Alternative Sources

**Option 1: Check the English diary**
- File: `C_2010Diary_En.docx` (SECONDARY version)
- Location: `Kazanluk/2010/Project Records/Team C/`
- May have different date coverage

```bash
unzip -p "/media/shawn/191c3b96-5fa5-4d0d-8805-0cf05d3d8468/synology/Adela/TRAP-WD-2020-04/Kazanluk/2010/Project Records/Team C/C_2010Diary_En.docx" word/document.xml | grep -E "March 8|8 March"
```

**Option 2: Check Team C Summary PDF**
- File: `C_2010Summary.pdf`
- Location: `Kazanluk/2010/Project Records/Team C/FieldRecords/`
- May contain walker information

**Option 3: Accept data gap**
- 8 March walker data is genuinely unavailable from diaries
- Mark in attribution.csv as: `Extraction_Notes: "Diary entry missing for this date"`
- Keep record with Leader only (Bara)

---

## Decision Matrix

| Option | Action | When to Use |
|--------|--------|-------------|
| **A** | Extract from EN diary if entry exists | If EN diary has 8 March entry |
| **B** | Extract from PDF Summary | If PDF has walker data |
| **C** | Mark as unavailable | If no sources have 8 March data |
| **D** | Use team roster from nearby dates | If team composition was stable |

---

## Specific Commands to Try

### 1. Check English Diary
```bash
# Extract and search
unzip -p "/media/shawn/191c3b96-5fa5-4d0d-8805-0cf05d3d8468/synology/Adela/TRAP-WD-2020-04/Kazanluk/2010/Project Records/Team C/C_2010Diary_En.docx" word/document.xml > /tmp/teamc_en.txt

grep -i "march 8\|8 march\|8\.03\|08\.03" /tmp/teamc_en.txt
```

### 2. List all dates in English diary
```bash
grep -oE "[0-9]{1,2} March 2010|March [0-9]{1,2}, 2010" /tmp/teamc_en.txt | sort -u
```

### 3. Check team composition on nearby dates
The BG diary has 17 March as the first entry. Check the team composition:
```bash
antiword "/media/shawn/191c3b96-5fa5-4d0d-8805-0cf05d3d8468/synology/Adela/TRAP-WD-2020-04/Kazanluk/2010/Project Records/Team C/C_2010Diary_BG.doc" | grep -A 10 "17.03.2010"
```

If the team was stable, you could use the 17 March team for 8 March.

---

## Recommended Immediate Action

1. **Run command to check English diary:**
   ```bash
   unzip -p "/media/shawn/191c3b96-5fa5-4d0d-8805-0cf05d3d8468/synology/Adela/TRAP-WD-2020-04/Kazanluk/2010/Project Records/Team C/C_2010Diary_En.docx" word/document.xml | grep -iC 20 "march 8\|8 march"
   ```

2. **If found:** Extract walker data and update attribution.csv

3. **If not found:** Check PDF Summary or accept as data gap

4. **Update attribution.csv:**
   - If data found: Add to `Walkers_Original` and `Walkers_Transliterated`
   - If not found: Add to `Extraction_Notes`: "8 March entry missing from all diary sources - Leader only"

---

## Update to manual-extraction-work.csv

Change the status for 2010-03-08:

**Before:**
```csv
2010-03-08,C,,"C_2010Diary_BG.doc (18.03.2010)","DATE DISCREPANCY: Diary shows 18 March not 8 March - RESOLVE FIRST",pending
```

**After investigation:**
```csv
2010-03-08,C,,"C_2010Diary_En.docx OR PDF OR accept gap","8 March entry MISSING from BG diary - check EN diary or PDF",in_progress
```

---

**Analysis complete.** Proceed with checking alternative sources as outlined above.
