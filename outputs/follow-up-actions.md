# TRAP Data Extraction - Follow-up Actions

**Created:** November 2025

This file tracks outstanding actions that fall outside the core data extraction work.

---

## High Priority

### 1. Add Silvia Ivanova to Participant List

**Status:** Pending verification

**Context:** Silvia Ivanova (Силвия Иванова) appears in the Team E 2009 Bulgarian diary but is NOT in `inputs/TRAP-Participants.csv`.

**Evidence:**
- Team E diary entry mentions "Силвия Иванова" as a team member
- No matching entry in the 104-person participant list

**Action required:**
- [ ] Verify Silvia Ivanova's participation in TRAP 2009
- [ ] If confirmed, add to `inputs/TRAP-Participants.csv` with appropriate details:
  - Role: Field walker
  - Affiliation: Unknown
  - Season: 2009 spring (x in column)

**Location:** `name-mapping.csv` lines 234 and 269

---

### 2. Disambiguate Adela (Sobotkova vs Dorňáková)

**Status:** Pending investigation

**Context:** Two different people named Adela participated in TRAP:
- **Adela Sobotkova** - Project leader, attended multiple seasons (2009-2011)
- **Adela Dorňáková** - Field walker, attended 2010-autumn only

**Issue:** Generic "Adela" entries in attribution.csv need to be verified to ensure Adela Dorňáková is correctly identified where she participated (2010-autumn), and not confused with Adela Sobotkova.

**Action required:**
- [ ] Search attribution.csv for all "Adela" entries in 2010-autumn
- [ ] Cross-reference with team compositions and dates
- [ ] Verify Dorňáková is correctly identified in her season
- [ ] Update any ambiguous "Adela" entries with full names

**Expected impact:** 2010-autumn records (October-November 2010)

---

## Medium Priority

### 3. Review Remaining Name Mappings

**Status:** ✅ COMPLETED (22 November 2025)

**Context:** The name mapping file contains 283 entries. All entries have been reviewed and processed.

**Completed actions:**
- [x] Reviewed all 66 `review_needed` entries in `outputs/name-mapping.csv`
- [x] Applied 58 valid corrections to `attribution.csv` (canonical names)
- [x] Marked 6 entries as `invalid` (OCR false positives: H., Hun, M, P, Olga, X [leader])
- [x] Marked 2 entries as `uncertain` (Lizzy/Lisi - Czech volunteer, identity being researched)
- [x] Updated status for all entries to `corrected`, `invalid`, or `uncertain`

**Results:**
- 111 name replacements made across 73 attribution records
- 126 invalid OCR entries cleared from data
- Detailed report: `outputs/name-corrections-report.md`
- Scripts: `scripts/apply_name_corrections.py`

**Current status distribution:**
- `confident`: 84 entries
- `mapped`: 126 entries
- `corrected`: 58 entries
- `confirmed`: 6 entries
- `uncertain`: 2 entries (Lizzy/Lisi - real person, full name being researched)
- `invalid`: 6 entries (OCR false positives)
- `disambiguated`: 1 entry (Petra)

---

### 4. Investigate XLS-only Records

**Status:** 76 records without diary/PDF walker data

**Context:** 76 survey day records exist only in the Excel summary files and lack corresponding diary or PDF sources for walker extraction.

**Action required:**
- [ ] Determine if additional source documents exist for these dates
- [ ] If no sources available, document as known limitation
- [ ] Consider whether leader-only records are sufficient for attribution

---

## Low Priority

### 5. Standardise Name Formats

**Status:** Deferred

**Context:** The attribution data contains a mix of:
- Full names (e.g., "Adela Sobotkova")
- First names only (e.g., "Adela")
- Initials (e.g., "A.S.")
- Diminutives (e.g., "Bara" for "Barbora")

**Action required:**
- [ ] Decide on preferred standardisation approach
- [ ] Apply name mapping to create standardised walker column
- [ ] Consider separate columns for original vs. standardised names

---

### 6. Role Field Enhancement

**Status:** Deferred

**Context:** PDA_Operator, Paper_Recorder, and Data_Editor fields have <5% coverage due to limited source documentation.

**Action required:**
- [ ] Determine if this data exists in other sources
- [ ] If not recoverable, document as known limitation

---

## Completed Actions

- [x] Extract Kazanlak 2009 team compositions from diaries
- [x] Resolve Helena/Elena ambiguity
- [x] Resolve Julia older/younger distinction
- [x] Create comprehensive name mapping file (283 entries)
- [x] Archive point-in-time reports
- [x] Review and process all 66 `review_needed` entries (22 November 2025)
- [x] Apply 58 valid name corrections to attribution.csv
- [x] Mark 6 invalid OCR entries
- [x] Disambiguate Petra (Janouchová vs Tušlová)
- [x] Verify and correct all pdf_sources in name-mapping.csv
- [x] Fix Lizzy/Lisi typo and clarify identity

---

## Notes

This file should be updated as actions are completed or new items are identified.

**Outstanding research:**
- Lizzy (Czech volunteer, 2009-autumn) - Full name being researched
- Silvia Ivanova - Verify participation and add to participant list if confirmed
- Jiří Musil - Check if needs to be added to participant list (Spring 2010 Kazanlak)

**Last updated:** 22 November 2025
