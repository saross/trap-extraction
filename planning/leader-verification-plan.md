# Leader Verification Plan

**Status:** Deferred - to be incorporated into broader QA/verification pass
**Created:** 24 November 2025
**Deferred reason:** Only 1 record with empty leader; 267/268 (99.6%) already populated

---

## Objective

Systematically verify the Leader field in `attribution.csv` against primary source documents (Daily Progress Form PDFs and team diaries), similar to the survey unit extraction workflow. This phase focuses on:
- Verifying existing leader values are correct
- Extracting leaders for any genuinely empty records
- Fixing obvious transcription errors where source clearly shows different value
- Documenting findings comprehensively

**NOT in scope:** Name standardisation (initials→full names, format consistency) - that's a separate phase.

---

## Current State

| Metric | Count | Notes |
|--------|-------|-------|
| Total records | 268 | |
| Leader populated | 267 | 99.6% |
| Leader empty | 1 | 2010-04-06 Team B (non-survey day) |
| Initials only | 28 | NK, JD, GM, GN, AA, JTs - leave as-is for now |

---

## Source Hierarchy

Per `source-inventory.md`, sources are processed in priority order:

### Tier 3: Daily Progress Form PDFs (Primary for leader field)
The scanned forms have an explicit "Leader" field - most authoritative.

**Locations:**
- Kazanlak 2009: `Kazanluk/2009/Project Records/Team[A-E]/`
- Kazanlak 2010: `Kazanluk/2010/Project Records/Team [A-D]/FieldRecords/`
- Kazanlak 2011: `Kazanluk/2011-11-30/Project Records/Team [B-C]/FieldRecords/`
- Elhovo 2010: `Elhovo 2010-12-12/2010/Project Records/Team [A-B]/Field Records/`

### Tier 2: Primary Diaries (Secondary verification)
Diary entries often mention the day's leader.

**Primary diaries per source-inventory.md:**
- Bulgarian diaries are generally PRIMARY (larger, more detailed)
- English diaries PRIMARY for: KAZ 2010 Team B, KAZ 2011 Teams B & C, all Elhovo

### Tier 1: Excel SurveySummary (Tertiary reference)
Contains leader column but may have transcription errors (as found with date corrections).

---

## Workflow (When Resumed)

### Phase 1: Generate Investigation Runsheet

Create `outputs/leader-investigation-runsheet.md` listing all 268 records with:
- Current leader value
- Issue type: `verified`, `needs_check`, `empty`, `initials_only`
- Source files to check (PDF path, diary path)
- Space for findings

**Script:** `scripts/generate-leader-investigation-runsheet.py`

### Phase 2: PDF Extraction (Tier 3)

For each team/season combination:
1. Read Daily Progress Form PDFs using vision
2. Extract leader name from "Leader" field on each form
3. Record in extraction CSV with source citation

**Output:** `outputs/leader-extraction-pdf.csv`

### Phase 3: Diary Verification (Tier 2)

For records where PDF is unavailable or unclear:
1. Read primary diary for that team/season
2. Search for leader mentions in daily entries
3. Record findings with source citation

**Output:** `outputs/leader-extraction-diary.csv`

### Phase 4: Consolidate and Compare

Compare extracted leaders against attribution.csv:
1. Match by (Date, Team) tuple
2. Categorise each record:
   - `match`: Extracted matches existing
   - `mismatch`: Extracted differs from existing (flag for review)
   - `empty_filled`: Existing was empty, now have value
   - `no_source`: No source found (document limitation)

**Output:** `outputs/leader-comparison.csv`

### Phase 5: Apply Verified Updates

For records with clear corrections:
1. Create backup of attribution.csv
2. Update Leader field where source clearly shows different value
3. Add extraction notes citing source

**NOT applied:** Initials→full name conversions (that's standardisation phase)

### Phase 6: Generate Verification Report

**Output:** `outputs/leader-verification-report.md`

---

## Processing Order

Process by season/team to efficiently batch PDF and diary reading:

1. **Kazanlak 2009** (Teams A-E) - 76 records
2. **Kazanlak 2010** (Teams A-D) - 70 records
3. **Kazanlak 2011** (Teams A-D) - 60 records
4. **Elhovo 2009** (Teams A-C) - 35 records
5. **Elhovo 2010** (Teams A-B) - 27 records

---

## Handling Special Cases

### Empty Leaders (1 record)
- 2010-04-06 Team B: Non-survey rainy day
- Attempt to find leader from diary
- If none found, flag as "UNVERIFIED: Leader (non-survey day)"

### Initials-Only (28 records)
- **Leave as-is** during extraction phase
- Verify the initials match what's in the source
- Document in report for standardisation phase

### Conflicts
- If PDF and diary disagree, prefer PDF (explicit field)
- Document both values in extraction notes
- Flag for user review if significant

---

## Success Criteria

- [ ] All 268 records investigated against sources
- [ ] PDF extraction attempted for all available forms
- [ ] Diary verification for records without PDFs
- [ ] Any genuine errors corrected with source citation
- [ ] 1 empty record either filled or flagged
- [ ] Comprehensive report documenting all findings
- [ ] Initials-only records documented for future standardisation

---

## Integration with QA Pass

This plan should be executed as part of the broader QA exercise (Task 5 in akb-submission-todo.md), which includes:
- Cross-reference checks against source Excel summaries
- Verification of walker counts against diary entries
- Validation of date sequences
- Source citation verification

The leader verification workflow can be combined with other QA checks for efficiency.
