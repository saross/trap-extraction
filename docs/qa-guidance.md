# QA Guidance: Attribution Data Verification

**Created:** 26 November 2025
**Updated:** 26 November 2025
**Purpose:** Complete protocol for cross-source verification of attribution.csv, including rules, heuristics, workflow, and documentation requirements

## Document Contents

1. [Source Priority Rules](#source-priority-rules) — Which sources to trust for which data
2. [Error Severity Classification](#error-severity-classification) — MAJOR vs minor errors
3. [Rules (Must Be True)](#rules-must-be-true) — Logical constraints for validation
4. [Heuristics (Usually True)](#heuristics-usually-true) — Patterns for disambiguation
5. [Observations](#observations-discovered-during-qa) — Discovered patterns
6. [QA Protocol: Complete Workflow](#qa-protocol-complete-workflow) — Step-by-step verification process
7. [Checklist: What to Record](#checklist-what-to-record) — Ensuring completeness

---

## Source Priority Rules

**Note:** "DPF scan" = Daily Progress Form scan (the scanned PDF of the handwritten daily summary forms completed in the field).

### For Basic Information (Walkers, Units, Dates)

1. **DPF scans** — PRIMARY source; more accurate for numeric/factual data
2. **Diaries** — Cross-reference for name interpretation and context
3. **Both together** — Required for high confidence

### For Role Information (PDA, GPS, Paper Recorder, etc.)

1. **Diaries** — PRIMARY and often ONLY source for role assignments
2. **DPF scans** — Do NOT reliably indicate Paper Recorder (see O3 below)

### Conflict Resolution

- DPF scans take precedence for basic info when conflicting with diaries
- Document all conflicts in discrepancies log with reasoning
- Flag genuinely ambiguous cases for user decision

### Source Gap Tracking

For every record, document which sources were available:

- **DPF scan:** Present / Missing
- **Primary Diary Entry:** Present / Missing
- **Secondary Diary Entry:** Present / Missing / N/A

When a primary diary entry is missing, check secondary diaries (e.g., "Team B Diary.docx" if "Team B Diary new.docx" lacks an entry).

### Cross-Check: Unit Number Continuity

**Rule C1:** The Start Unit of day N should equal or follow the End Unit of day N-1.

Use this to validate source priority:

- If DPF scan creates a gap/overlap with adjacent days but diary doesn't → evidence to prefer diary
- If diary creates a gap/overlap but DPF scan doesn't → confirms DPF scan as PRIMARY
- Document all continuity anomalies in discrepancies log

---

## Error Severity Classification

### MAJOR Errors (Affect Data Integrity)

These errors affect the core data that will be submitted to the AKB:

| Type | Description | Example |
|------|-------------|---------|
| **Missing record** | CSV lacks a record when DPF scan/diary sources exist | D008, D009 |
| **Unit number error** | Start/End Unit incorrect or missing | D005, D007 |
| **Personnel error** | Wrong/missing walkers, roles, or leader | — |

### Minor Errors (Metadata/Bonus Fields)

These errors affect supporting information but not core data submission:

| Type | Description | Example |
|------|-------------|---------|
| **Author error** | Diary_Author or DPF_Author incorrect | — |
| **Source reference** | Wrong PDF_Source or XLS_Source filename | — |

### Runsheet Documentation

- **MAJOR errors:** Document in main runsheet with full issue format; flag for immediate correction
- **Minor errors:** Document in discrepancies log; correct when convenient
- **Missing records:** Always add to main runsheet as QA issues (not just discrepancies log)

---

## Rules (Must Be True)

These are logical constraints that must hold for valid data. Violations indicate errors.

| ID | Rule | Description | Validation Use |
|----|------|-------------|----------------|
| **R1** | Roles ⊆ Walkers | All role holders (Leader, PDA_Operator, Paper_Recorder, GPS_Operator, Photographer, Author) must appear in the Walkers list | If a role holder isn't a walker, one or the other is wrong |
| **R2** | Leader ∈ Walkers | The team leader must be included in the walker list | Special case of R1; always check |

---

## Heuristics (Usually True)

These are patterns that usually hold but have exceptions. Useful for disambiguation.

| ID | Heuristic | Description | Disambiguation Use |
|----|-----------|-------------|-------------------|
| **H1** | Team stability | Teams are generally stable over a season (but not entirely) | If a name is illegible, check nearby days for the same team to infer likely walkers |
| **H2** | One team per day | A walker is typically on only one team per day | If unsure which team someone was on, verify they don't appear on another team that day |

---

## Observations (Discovered During QA)

These are patterns discovered during verification that inform methodology.

| ID | Observation | Evidence | Implication |
|----|-------------|----------|-------------|
| **O1** | DPF scan more reliable for unit numbers | Diary entry for 2010-10-24 shows "Last unit: 61349" (typo); DPF scan shows correct value 61549. Similar discrepancies in other records. | Always prefer DPF scan for Start Unit / End Unit values |
| **O2** | Diary Author ≠ DPF Author | The person who wrote the diary entry (narrative) is often different from the person who filled out the DPF. These are distinct roles. | Split into separate fields: `Diary_Author` and `DPF_Author` |
| **O3** | DPF Author ≠ Paper Recorder | Tested hypothesis that DPF "Author" = Paper Recorder. Team B data showed only 2/6 matches between diary-assigned "Paper Records" role and DPF Author. | Cannot reliably infer Paper_Recorder from DPF Author; these appear to be different tasks |

---

## Applying Observations

### O2: Separate Author Fields

The CSV now uses two distinct author fields:

- **Diary_Author** — Person who wrote the diary/narrative entry for that day
- **DPF_Author** — Person who filled out the DPF (Daily Progress Form)

These are often different people. The diary author writes the detailed narrative; the DPF author completes the standardised form at end of day.

### O3: Paper Recorder (Disproven Hypothesis)

**Initial hypothesis:** DPF "Author" = Paper Recorder role

**Testing:** Compared Team B diary (which explicitly names "Paper Records" / "Documents" roles) against DPF Author field.

**Result:** Only 2 of 6 records matched. The hypothesis is **not supported**.

**Conclusion:** The DPF Author and the diary-assigned "Paper Records" role appear to be different tasks:

- **Paper Records role** (diary) — May refer to recording finds/samples on unit forms during survey
- **DPF Author** — Whoever fills out the end-of-day summary form

Do NOT use DPF Author to populate Paper_Recorder column.

---

## QA Protocol: Complete Workflow

This section documents the full QA process for verifying a group of attribution records. Follow this protocol to ensure consistent, repeatable verification.

### Phase 1: Pre-QA Setup

Before beginning verification:

1. **Identify records to verify**
   - Filter attribution.csv by study area, season, and/or team
   - Note total record count and date range

2. **Locate source documents**
   - DPF scans (check `Field Records/` directories)
   - Primary diary (check `Project Records/Team X/` directories)
   - Secondary diary (if applicable — older versions or alternate team diaries)

3. **Create source inventory table**

   ```markdown
   | Type | File | Location | Dates Covered |
   |------|------|----------|---------------|
   | Diary | [filename] | [path] | [dates] |
   | DPF scan | [filename] | [path] | [dates] |
   ```

4. **Note DPF-to-date mapping**
   - Day_XX.pdf files may contain multiple forms for different dates
   - Record which forms appear in which DPF files

### Phase 2: Per-Record Verification

For each record in the target set:

#### Step 2.1: Extract CSV Record

Pull the current CSV values for all fields:

- Date, Team, Start Unit, End Unit
- Leader, Walkers_Original, Walkers_Standardised
- PDA_Operator, Paper_Recorder, GPS_Operator, Photographer
- Diary_Author, DPF_Author
- XLS_Source, PDF_Source
- Extraction_Notes, QA_Notes

#### Step 2.2: Locate DPF Scan

1. Find the corresponding DPF scan for the date
2. Extract from DPF:
   - Date (verify match)
   - Team designation
   - Start Unit, End Unit
   - Leader name
   - Walker names/initials
   - Form Author (→ DPF_Author)
3. **Record DPF availability:** Present / Missing

#### Step 2.3: Locate Diary Entry

1. Find the corresponding diary entry for the date
2. Extract from diary:
   - Date (verify match)
   - Walker count and names
   - Role assignments (PDA, GPS, Paper Records, etc.)
   - Leader
   - Diary Author
3. **If primary diary entry missing:** Check secondary diary
4. **Record diary availability:** Present / Missing / Secondary Used

#### Step 2.4: Compare Fields

Create a comparison table for each record:

```markdown
| Field | CSV Value | DPF Value | Diary Value | Status |
|-------|-----------|-----------|-------------|--------|
| Date | | | | CONFIRMED / DISCREPANCY |
| Team | | | | CONFIRMED / DISCREPANCY |
| Start Unit | | | | CONFIRMED / DISCREPANCY / SOURCE GAP |
| End Unit | | | | CONFIRMED / DISCREPANCY / SOURCE GAP |
| Leader | | | | CONFIRMED / DISCREPANCY |
| Walker count | | | | CONFIRMED / DISCREPANCY |
| Walkers | | | | CONFIRMED / PARTIAL / DISCREPANCY |
| Roles | | | | CONFIRMED / SOURCE GAP |
```

Status values:

- **CONFIRMED** — CSV matches source(s)
- **DISCREPANCY** — CSV differs from source(s)
- **SOURCE GAP** — Source unavailable for this field
- **PARTIAL** — Some values match, others differ

#### Step 2.5: Apply Rule Checks

For each record, verify:

- [ ] **R1:** All role holders appear in Walkers list
- [ ] **R2:** Leader appears in Walkers list
- [ ] **C1:** Start Unit follows previous day's End Unit (±1)

Document any rule violations.

#### Step 2.6: Apply Heuristics (If Needed)

Use heuristics for disambiguation:

- **H1 (Team stability):** Check nearby days if name illegible
- **H2 (One team per day):** Verify walker doesn't appear on multiple teams

#### Step 2.7: Document Findings

**For CONFIRMED records:** Add to verification summary (no issue needed)

**For DISCREPANCIES:** Create QA Issue in runsheet using template:

```markdown
## QA Issue #[N]: [DATE] Team [X] - [FIELD]

**Problem:** [One sentence describing what's wrong]

**Fix:** [One sentence describing the correction]

**Sources consulted:**
1. [DPF scan filename] — [form/page]
2. [Diary filename] — [date entry]

**Source evidence:**
- DPF: "[relevant excerpt]"
- Diary: "[relevant excerpt]"

**Finding:** DISCREPANCY / MISSING / SOURCE GAP
**Recommended value:** [value]

**Reasoning:**
[Why this value is correct, referencing source priority rules]

---
**User Decision:** [ ] Accept / [ ] Modify: _______________
```

**For MISSING RECORDS:** Always document as MAJOR QA Issue

### Phase 3: Cross-Record Checks

After verifying all individual records:

#### 3.1: Unit Continuity Check

Create a unit continuity table for the entire record set:

```markdown
| Date | End Unit | Next Date | Start Unit | Gap | Status |
|------|----------|-----------|------------|-----|--------|
| [date] | [end] | [date] | [start] | [+/-N] | ✓ / ⚠ |
```

- Gap of +1: Normal (continuous)
- Gap of 0: Overlap (same unit, may be valid)
- Gap > +1: Investigate — may indicate missing records
- Negative gap: Error — units shouldn't go backwards

**IMPORTANT:** Unit gaps often indicate missing CSV records, not missing field days. Always check DPF scan and diary for the gap dates.

#### 3.2: Source Coverage Matrix

Document source availability for all records:

```markdown
| Date | DPF Scan | Primary Diary | Secondary Diary | CSV Status | Notes |
|------|----------|---------------|-----------------|------------|-------|
| [date] | ✓/✗ | ✓/✗ | ✓/✗/N/A | Present/Missing/Added | [notes] |
```

#### 3.3: Walker Consistency Check

- [ ] No duplicate walkers within any record
- [ ] Walker names consistently standardised across records
- [ ] Leaders always included in walker lists

### Phase 4: Documentation Outputs

A complete QA run must produce:

#### 4.1: QA Runsheet (`outputs/qa-runsheet-[area]-[season].md`)

Required sections:

1. **Header:** Date, scope (record count), status
2. **Source Documents Consulted:** Table of files used
3. **Per-Record Verification Results:** Comparison tables
4. **QA Issues:** All discrepancies with full issue format
5. **Source Coverage Matrix:** Complete source availability
6. **Unit Continuity Check:** Full continuity table
7. **Summary:** Counts by category, corrections applied

#### 4.2: Discrepancies Log (`docs/qa-discrepancies-log.md`)

Add entries for:

- **Value discrepancies (Dxxx):** DPF scan vs Diary conflicts, CSV errors
- **Missing records (Dxxx):** Records that should exist but don't
- **Source gaps (Sxxx):** Missing DPF scan or diary entries
- Each entry must include: source values, resolution, reasoning

#### 4.3: Updated attribution.csv

After user approval:

- Apply accepted corrections
- Add missing records (if any)
- Update Extraction_Notes with QA provenance

### Phase 5: Summary Statistics

Record final counts:

```markdown
| Metric | Count |
|--------|-------|
| Records verified | [N] |
| MAJOR issues | [N] |
| Minor issues | [N] |
| Corrections applied | [N] |
| Missing records added | [N] |
| Source gaps documented | [N] |
```

---

## Checklist: What to Record

Use this checklist to ensure nothing is missed during QA:

### Per Record

- [ ] Source availability (DPF scan, primary diary, secondary diary)
- [ ] Field-by-field comparison (Date, Team, Units, Leader, Walkers, Roles)
- [ ] Rule check results (R1, R2)
- [ ] Any discrepancies with source values and resolution
- [ ] Any source gaps (fields that couldn't be verified)

### Per Record Set

- [ ] Source coverage matrix (all records)
- [ ] Unit continuity table (all consecutive days)
- [ ] Summary of issues by severity (MAJOR vs minor)
- [ ] List of all corrections applied
- [ ] List of any missing records discovered and added

### Documentation

- [ ] QA runsheet created/updated
- [ ] Discrepancies log updated with new entries
- [ ] CSV corrections applied after approval
- [ ] New rules/heuristics/observations added to this guidance document

---

## Quality Checks (Quick Reference)

### Systematic Checks

- [ ] All walkers unique within each record (no duplicates)
- [ ] All role holders appear in walker list
- [ ] Leader appears in walker list
- [ ] Unit ranges are plausible (end ≥ start, within season range)
- [ ] Unit continuity between consecutive days
- [ ] No unexplained gaps (investigate before assuming "days off")

### Red Flags

- Unit gap > 1 between consecutive records → Check for missing records
- Walker count mismatch between CSV and sources → Verify walker list
- Role holder not in walker list → R1 violation
- Leader not in walker list → R2 violation
- Both DPF scan and diary missing → Document as source gap; flag low confidence

---

## Future Additions

*Add new rules, heuristics, or observations here as QA progresses*

---

## References

- `outputs/source-inventory.md` — Source document locations and reliability notes
- `outputs/name-mapping.csv` — Name standardisation reference
- `outputs/qa-runsheet-elhovo-2010-autumn.md` — Detailed verification findings
- `docs/qa-discrepancies-log.md` — Record of source conflicts and resolutions
