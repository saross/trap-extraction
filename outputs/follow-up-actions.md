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

## Medium Priority

### 2. Review Remaining Name Mappings

**Status:** 59 entries marked `review_needed`

**Context:** The name mapping file contains 282 entries. Of these, 59 still require manual review to confirm the canonical name match.

**Action required:**
- [ ] Review `outputs/name-mapping.csv` entries with `status=review_needed`
- [ ] Update status to `confirmed` or `mapped` once verified
- [ ] Flag any names that cannot be resolved

**Sample entries needing review:**
- `Halyar` (Team B, 2009)
- `Knacfl` (Team B, 2009)
- `Serena` (Team B, 2009)
- `Tracy` (Team B, 2009)
- `Acna` (Team C, 2009)

---

### 3. Investigate XLS-only Records

**Status:** 76 records without diary/PDF walker data

**Context:** 76 survey day records exist only in the Excel summary files and lack corresponding diary or PDF sources for walker extraction.

**Action required:**
- [ ] Determine if additional source documents exist for these dates
- [ ] If no sources available, document as known limitation
- [ ] Consider whether leader-only records are sufficient for attribution

---

## Low Priority

### 4. Standardise Name Formats

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

### 5. Role Field Enhancement

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
- [x] Create comprehensive name mapping file
- [x] Archive point-in-time reports

---

## Notes

This file should be updated as actions are completed or new items are identified.

**Last updated:** November 2025
