# Name Standardisation Plan for attribution.csv

**Date:** 25 November 2025
**Status:** ✅ COMPLETE
**Objective:** Clean up walker columns and create standardised walker names

---

## Summary

Transform the walker data in `attribution.csv` through four phases:
1. **Update name-mapping.csv** - add 24 missing name variants (pre-requisite)
2. **Clean Walkers_Original** - normalise separators, deduplicate, merge transliterations
3. **Delete Walkers_Transliterated** - after merging unique content
4. **Create Walkers_Standardised** - map all names to canonical "First Last" format

---

## Phase 0: Update name-mapping.csv (Pre-requisite)

Add the following 24 unmapped names to `outputs/name-mapping.csv`:

### Placeholders/Invalid
| extracted_name | canonical_name | status | notes |
|----------------|----------------|--------|-------|
| [unclear] | | invalid | Placeholder for illegible text - remove from walkers |

### Title/Informal Variants
| extracted_name | canonical_name | status | notes |
|----------------|----------------|--------|-------|
| Dr. Ross | Shawn Ross | mapped | Title variant |
| Dr. Ross training Royce Lawrence | Shawn Ross \| Royce Lawrence | mapped | Combined entry - split into two names |

### Typos/OCR Errors
| extracted_name | canonical_name | status | notes |
|----------------|----------------|--------|-------|
| Silvia Ivanova Ivanova | Silvia Ivanova | corrected | Double surname OCR error |
| Leonid | Prazak Lindsay | corrected | OCR error for Линдзи |
| Peg Meglena Parvin | Meglena Parvin | corrected | OCR error - Peg prefix |

### Uncertain Identity (Add to follow-up-actions.md)
| extracted_name | canonical_name | status | notes |
|----------------|----------------|--------|-------|
| Sharon | Sharon | uncertain | Appears once (2011-11-02 Team D). Clearly written as Шарон in BG diary. Shawn Ross confirms not him. Requires investigation - possible missing participant. |

### Initials
| extracted_name | canonical_name | status | notes |
|----------------|----------------|--------|-------|
| ACQ | Ashley Chee Quee | mapped | Initials |
| Al.R | Aleksandar Riskov | mapped | Abbreviated initials |
| YuTs | Julia Tzvetkova | mapped | Cyrillic initials ЮЦ transliterated |

### Abbreviated (Initial.Surname)
| extracted_name | canonical_name | status | notes |
|----------------|----------------|--------|-------|
| B. Lilova | Bogdana Lilova | mapped | Initial + surname |
| G. Nekhrizov | Georgi Nekhrizov | mapped | Initial + surname |
| L. Markovski | Lyubomir Markovski | mapped | Initial + surname |
| N. Kecheva | Nadezhda Kecheva | mapped | Initial + surname |
| Yu. Tsvetkova | Julia Tzvetkova | mapped | Initial + surname |

### Diminutives/Variants
| extracted_name | canonical_name | status | notes |
|----------------|----------------|--------|-------|
| Lubomir | Lyubomir Markovski | mapped | Spelling variant of Lyubomir |
| Nadya | Nadezhda Kecheva | mapped | Diminutive of Nadezhda |
| Viera | Vera Doležálková | mapped | Czech spelling variant |
| Katya | Katarina Čuláková | mapped | Diminutive of Katarina |

### Bulgarian Transliterations
| extracted_name | canonical_name | status | notes |
|----------------|----------------|--------|-------|
| Dzhoel | Joel Sercombe | mapped | Bulgarian transliteration Джоел |
| Dzhordzhiya | Georgia Burnett | mapped | Bulgarian transliteration Джорджия |

### Name Variants
| extracted_name | canonical_name | status | notes |
|----------------|----------------|--------|-------|
| Magdalena | Magda Bolečková | mapped | Full form of Magda |
| Victoria | Viktorie Chystyaková | mapped | English spelling variant |
| Oskar | Oscar Warren | mapped | German/Scandi spelling variant |

**Total:** 24 new entries to add to name-mapping.csv

### Also: Add Silvia Ivanova to TRAP-Participants.csv

She's a legitimate participant missing from the canonical document. Add to `inputs/TRAP-Participants.csv`:

| Field | Value |
|-------|-------|
| Last name | Ivanova |
| First name | Silvia |
| Role | Field walker |
| Affiliation | (unknown) |
| Position | (unknown) |
| Country | Bulgaria |
| 2009 spring | x |

This resolves the follow-up action item from `planning/follow-up-actions.md`.

### Also: Add Sharon investigation to follow-up-actions.md

Add new item under "Participant List Updates":
- **Sharon** (2011-11-02 Team D) - Unidentified participant. Clearly written as Шарон in Bulgarian diary. Not Shawn Ross (confirmed). Appears only once across all diaries. Research needed.

---

## Phase 1: Clean Walkers_Original Column

### 1.1 Merge Transliterated Content First

**Issue:** 28 records have Cyrillic names in Walkers_Original with Latin transliterations in Walkers_Transliterated that must be preserved.

**Action:** For these 28 records (mostly 2011 autumn Teams A & D), replace the Cyrillic names in Walkers_Original with their Latin transliterations from Walkers_Transliterated.

**Records affected:**
- 2011-10-14 to 2011-11-03, Teams A and D

**Exception:** Skip 2010-03-24 Team D - keep "Vera" (confirmed correct), discard erroneous "Petra" from Transliterated.

**Example transformation:**

```text
Before: NK | Н. Кечева | Ю. Димитрова | В. Генчева | Г. Михайлов
After:  NK | N. Kecheva | Yu. Dimitrova | V. Gencheva | G. Mikhaylov
```

### 1.2 Normalise Separators

**Issue:** 59 records have mixed pipe/comma separators.

**Action:** Convert all entries to pipe-separated format:
- Split on pipes first, then on commas within each part
- Rejoin with ` | ` (space-pipe-space)

**Example:**

```text
Before: Adela | Bryan, Simon, Magda, Adela, Vera, Martin
After:  Adela | Bryan | Simon | Magda | Adela | Vera | Martin
```

### 1.3 Deduplicate Exact Names

**Issue:** 30 records have exact duplicate names (typically Leader appearing twice).

**Action:** Remove exact duplicates while preserving one instance (Leader should appear once in walker list).

**Example:**

```text
Before: Adela | Bryan | Simon | Magda | Adela | Vera | Martin
After:  Adela | Bryan | Simon | Magda | Vera | Martin
```

---

## Phase 2: Delete Walkers_Transliterated Column

**Prerequisite:** Phase 1.1 must be complete (all unique transliterated content merged).

**Action:** Remove the Walkers_Transliterated column entirely.

**Verification:** Generate a report listing all 28 merged records for user review.

---

## Phase 3: Create Walkers_Standardised Column

### 3.1 Build Canonical Name Lookup

**Sources:**
1. `inputs/TRAP-Participants.csv` - authoritative list of 104+ participants
2. `outputs/name-mapping.csv` - 283+ entries mapping variants to canonical names

**Lookup structure:**

```python
{
    "adela": "Adela Sobotkova",
    "adela sobotkova": "Adela Sobotkova",
    "a.s.": "Adela Sobotkova",
    "bara": "Bara Weissová",
    ...
}
```

### 3.2 Standardisation Logic

For each name in Walkers_Original:
1. Clean whitespace and normalise
2. Look up in canonical name map
3. If found, use canonical name
4. If not found:
   - Check if it's initials that map to a full name
   - Flag as "UNMAPPED: [original]" if no match

**Output format:** Pipe-separated list of "First Last" canonical names

**Example:**

```text
Original:     Adela | Bryan | Simon | Magda | Vera | Martin
Standardised: Adela Sobotkova | Bryan Zlatos | Simon Connor | Magda Bolečková | Vera Doležálková | Martin Mladenov
```

### 3.3 Handle Edge Cases

| Case | Handling |
|------|----------|
| Initials only (e.g., "TB", "MK") | Map via name-mapping.csv where available |
| OCR errors (e.g., "Adela Sobstkova") | Correct via name-mapping.csv |
| Uncertain identity (e.g., "Lizzy", "Sharon") | Retain as-is with note |
| Invalid entries (e.g., "M", "P", "[unclear]") | Remove (marked as invalid OCR) |
| Not in participant list | Flag as "UNMAPPED: [name]" |

---

## Implementation Script

**File:** `scripts/standardise-walkers.py`

**Functions:**
1. `merge_transliterations()` - Phase 1.1
2. `normalise_separators()` - Phase 1.2
3. `deduplicate_names()` - Phase 1.3
4. `build_canonical_lookup()` - Phase 3.1
5. `standardise_names()` - Phase 3.2
6. `main()` - orchestrate all phases

**Outputs:**
- Updated `outputs/attribution.csv` with:
  - Cleaned Walkers_Original
  - Walkers_Transliterated column removed
  - New Walkers_Standardised column
- Report: `outputs/walker-standardisation-report.md`
  - Records with merged transliterations
  - Unmapped names for review
  - Statistics

---

## Critical Files

| File | Purpose |
|------|---------|
| `outputs/attribution.csv` | Main data file to modify |
| `outputs/name-mapping.csv` | Name variant mappings (add 24 new entries) |
| `inputs/TRAP-Participants.csv` | Canonical participant names (add Silvia Ivanova) |
| `planning/follow-up-actions.md` | Add Sharon investigation item |

---

## Verification Steps

1. **Pre-flight:**
   - Create backup: `attribution.csv.backup_standardisation`
   - Verify all 268 records present

2. **Phase 1 verification:**
   - Count records with Cyrillic names (should be 0 after merge)
   - Count mixed separators (should be 0)
   - Count duplicate names (should be 0)

3. **Phase 3 verification:**
   - Count unmapped names (flag for review)
   - Sample check 10 random records
   - Verify all names in Walkers_Standardised exist in TRAP-Participants.csv (except flagged)

---

## Resolved Issues

### 2010-03-24 Team D Discrepancy
**Issue:** Original has "Vera", Transliterated has "Petra"
**Resolution:** Keep "Vera" - confirmed from source diary (Bulgarian "Виера") and scanned daily summary sheet. The "Petra" in Walkers_Transliterated was an error.

---

## Success Criteria

- [x] All 268 records have clean Walkers_Original (pipe-separated, no duplicates) ✓
- [x] Walkers_Transliterated column removed ✓
- [x] New Walkers_Standardised column with "First Last" format ✓
- [x] < 5% unmapped names (flagged for review) ✓ (2 names = 0.2%: Lizzy, YL - both uncertain identity)
- [x] Report generated documenting all changes ✓ (`outputs/walker-standardisation-report.md`)
- [x] Silvia Ivanova added to TRAP-Participants.csv ✓
- [x] Sharon investigation added to follow-up-actions.md ✓

**Status: COMPLETE** - 25 November 2025

---

**Last updated:** 25 November 2025
