# QA Guidance: Attribution Data Verification

**Created:** 26 November 2025
**Updated:** 2 December 2025
**Purpose:** Complete protocol for cross-source verification of attribution.csv, including rules, heuristics, workflow, and documentation requirements

## Document Contents

1. [Source Priority Rules](#source-priority-rules) — Which sources to trust for which data
2. [Error Severity Classification](#error-severity-classification) — MAJOR vs minor errors
3. [Rules (Must Be True)](#rules-must-be-true) — Logical constraints for validation
4. [Heuristics (Usually True)](#heuristics-usually-true) — Patterns for disambiguation
5. [Non-Survey Day Convention](#non-survey-day-convention) — Handling days without fieldwork
6. [QA Citation Format](#qa-citation-format) — Documenting corrections
7. [Observations](#observations-discovered-during-qa) — Discovered patterns
8. [QA Protocol: Complete Workflow](#qa-protocol-complete-workflow) — Step-by-step verification process
9. [Checklist: What to Record](#checklist-what-to-record) — Ensuring completeness

---

## Source Priority Rules

**Note:** "DPF scan" = Daily Progress Form scan (the scanned PDF of the handwritten daily summary forms completed in the field).

### Default Source Priority

**For unit numbers and walker names:** DPF scans supersede diaries by default.

**For role information (PDA, GPS, Paper Recorder, etc.):** Diaries are PRIMARY and often the ONLY source. DPF scans do NOT reliably indicate roles (see O3 below).

### When DPF Priority Does NOT Apply

DPF values should NOT be automatically preferred when they produce **unexpected results** with no explanation in the diary:

1. **Unit discontinuity:** DPF value creates a gap or overlap with adjacent days
2. **Unexpected walker:** DPF walker list differs from previous/succeeding days or "usual" team composition without explanation
3. **Disallowed placement:** DPF would place the same person on two teams on the same day

### Conflict Resolution Decision Tree

When DPF and diary conflict for unit numbers or walker names:

```text
1. Does the DPF value produce continuity AND expected walkers?
   YES → Use DPF value (default priority applies)
   NO  → Continue to step 2

2. Does the diary value produce continuity AND expected walkers?
   YES → Use diary value (DPF likely has recording error)
   NO  → Continue to step 3

3. Can EITHER source's value be reconciled with context?
   - Check if diary explains an unusual situation
   - Check adjacent days for patterns
   - Check if one value is a plausible transcription error
   YES → Use the reconcilable value with documented reasoning
   NO  → Continue to step 4

4. ESCALATE: Present evidence to user for SU form verification
   - Document both source values
   - Note why neither produces a satisfactory result
   - Request user review of individual survey unit forms
```

### Documentation Requirements

- **All conflicts** must be documented in the discrepancies log with reasoning
- **Source attribution** required: note which source the final value came from
- **Escalated cases** must include specific evidence (file, page, values from each source)

### Source Gap Tracking

For every record, document which sources were available:

- **DPF scan:** Present / Missing
- **Primary Diary Entry:** Present / Missing
- **Secondary Diary Entry:** Present / Missing / N/A

When a primary diary entry is missing, check secondary diaries (e.g., "Team B Diary.docx" if "Team B Diary new.docx" lacks an entry).

### Cross-Check: Unit Number Continuity

**Rule C1:** The Start Unit of day N should equal or follow the End Unit of day N-1.

Use continuity as a validation check:

- **Both sources agree:** Confirm the value
- **Sources conflict, one maintains continuity:** Prefer the source that maintains continuity
- **Sources conflict, both break continuity:** Escalate for SU form verification
- **Document all continuity anomalies** in discrepancies log

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

## Non-Survey Day Convention

When a record represents a day where no field survey was conducted (due to weather, rest days, excursions, etc.), use the following convention:

### QA_Notes Field

**Correct:** `Non-survey day (no field walking conducted)`

**Incorrect:**
- `MISSING: Survey units` — Nothing is actually missing; the record is complete
- `No autumn survey season: ...` — Erroneous text from automated processing

### What Constitutes a Non-Survey Day

- **Weather:** Rain, adverse conditions preventing fieldwork
- **Rest days:** Scheduled or unscheduled breaks
- **Excursions:** Site visits, museum trips, cultural activities
- **Logistics:** Equipment issues, travel days, team reorganisation

### Documentation

In the runsheet, document the reason from the diary:
- "Oct 14: 'We didn't walk in the fields because the Bulgarians from museum were tired'"
- "Oct 16: 'Today we didn't walk because it was raining'"
- "Oct 18: 'A trip to Burgas'"

These records are **complete** — they document that no survey occurred and why.

---

## QA Citation Format

When documenting corrections in the Source_Notes or Extraction_Notes fields, use this format:

```text
QA D###: [description] (YYYY-MM-DD)
```

### Examples

- `QA D021: Removed Georgi - diary states 'walked in five' (2025-11-27)`
- `QA D023: Corrected Start_Unit 80839→80939 (2025-11-27)`
- `QA D019: Non-survey day (2025-11-27)`

### Guidelines

- **D###** references the discrepancy ID from qa-discrepancies-log.md
- **Description** should be brief but informative
- **Date** is the QA correction date in ISO 8601 format (YYYY-MM-DD)
- Multiple QA citations can be appended, separated by ` | `

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
| **O1** | DPF scan more reliable for unit numbers (with exceptions) | Diary entry for 2010-10-24 shows "Last unit: 61349" (typo); DPF scan shows correct value 61549. However, KAZ09A Mar 19 shows diary had 10387 (creating overlap) while DPF had 10385 (maintaining continuity). | DPF supersedes diary for unit numbers BY DEFAULT, but use the decision tree when DPF creates discontinuity or unexpected results |
| **O2** | Diary Author ≠ DPF Author | The person who wrote the diary entry (narrative) is often different from the person who filled out the DPF. These are distinct roles. | Split into separate fields: `Diary_Author` and `DPF_Author` |
| **O3** | DPF Author ≠ Paper Recorder | Tested hypothesis that DPF "Author" = Paper Recorder. Team B data showed only 2/6 matches between diary-assigned "Paper Records" role and DPF Author. | Cannot reliably infer Paper_Recorder from DPF Author; these appear to be different tasks |
| **O4** | Name disambiguation via team roster cross-reference | Team C D016 case: disambiguated "Tereza" by checking team rosters on adjacent days. Person cannot be on two teams on the same day (H2). | When a name is ambiguous (multiple people with same first name), use team membership constraints across dates to disambiguate |

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

#### 4.1: QA Runsheet (`outputs/qa-runsheet-[area]-[season]-[team].md`)

Required sections:

1. **Header:** Date, scope (record count, team, date range), QA performer
2. **Sources Consulted:** Table of files with type, location, and role (PRIMARY/SECONDARY)
3. **Team Composition:** Roster with phases documenting personnel changes
4. **Record-by-Record Verification:** Daily breakdown with diary quote/summary, CSV values, status (CONFIRMED/DISCREPANCY)
5. **Issues Summary:** Table with ID, date, field, issue, action
6. **Corrections Required:** Each correction with:
   - Record identification (date, team)
   - Current vs corrected values
   - Source evidence (diary quote)
   - Reasoning
   - **Inline User Decision checkbox** (`[ ] Approve` / `[ ] Modify`)
   - **Status field** (`Pending` / `✅ APPLIED (YYYY-MM-DD)`)
7. **Source Observations:** Document source-vs-source divergences:
   - **Source Divergences table:** Date, field, DPF value, diary value, CSV value, resolution, note
   - **Source Reliability Patterns:** Confirm/refine O-series observations (e.g., O1: DPF > diary for units)
   - **Implications for Future QA:** Patterns to watch for, methodology refinements
8. **Summary Statistics:** Records checked, confirmed, issues found, corrections required

**Format notes:**
- Daily breakdown is **required** — each record must have explicit verification entry
- User Decision checkboxes appear **with each correction**, not batched at end
- Mark status as `✅ APPLIED (YYYY-MM-DD)` immediately after applying corrections
- Non-survey days: Use `Non-survey day (no field walking conducted)` notation

See `outputs/qa-runsheet-elhovo-2009-autumn-c.md` for exemplar format.

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

## Tier 4 Sources: Survey Unit (SU) Forms

Individual survey unit forms (scanned PDFs) provide field-level data recorded at the time of survey. These are a fallback verification source when primary sources (DPF scans, diaries) are unavailable or suspicious.

### When to Use SU Forms

**Use SU forms when diary data looks suspicious:**

- Unexpected walker changes (single day differs from surrounding days)
- Unit number gaps or discontinuities
- Date mismatches between CSV and diary
- Walker count inconsistencies

**Do NOT routinely check SU forms if diary data is coherent:**

- Continuous unit numbers across days
- Consistent walker composition (expected team stability)
- Dates match between sources
- No unexplained anomalies

SU forms are **high-effort to interpret** (handwritten, 4 forms per page, variable legibility). Only use when needed.

### What SU Forms Provide

| Data | Reliability | Location on Form |
|------|-------------|------------------|
| Unit numbers | ✓ Direct | "Survey unit:" field |
| Walker names | ✓ Good | Bottom-left position boxes (1-5) |
| Walker count | ✓ Good | Count non-Xed columns |
| Dates | ✓ Good | "Date:" field (often abbreviated) |
| Role assignments | ✗ Poor | Occasional marginal notes only |

### Reading SU Forms

**Form layout:**
- 4 forms per page, arranged vertically
- **Bottom form = first unit** (fieldwalkers work upward on the page)
- Walker names in numbered position boxes (bottom-left corner)

**Visual cues:**
- **X through column(s):** Area not surveyed → fewer walkers
- **Hand-drawn extra columns:** More than 5 walkers
- **Count non-Xed columns:** Actual walker count

**Marginal notes:**
- Often archaeological observations (materials found, site conditions)
- Occasionally contain role assignments — examine but don't rely on
- Look for keywords: "PDA", "GPS", "forms", "recorder"

### SU Forms for Seasons Without DPF Scans

For seasons like **Elhovo 2009** where no DPF scans exist, SU forms become the **only primary field source** to cross-verify unit numbers against diary entries. The unit number on each SU form is recorded in the field at the time of survey, making it definitive.

### Protocol: Investigating Unit Gaps/Overlaps with SU Forms

This protocol applies when unit continuity analysis reveals a gap, overlap, or other discrepancy that cannot be resolved from diaries and DPF scans alone. It is **labour-intensive** — only invoke when necessary.

**Trigger conditions:**

- Unit gap > 1 between consecutive survey days
- Unit overlap (same unit on different days)
- Diary and CSV disagree on Start/End Unit

#### Step 1: Assess the Situation

Before diving into SU forms, consider:

1. **Does the CSV maintain continuity?** If CSV is continuous but diary claims a gap, the diary may have a transcription error. Approach with an open mind — either could be correct.

2. **Is there a DPF scan?** Check first; DPF scans are easier to read than SU forms.

3. **What is the exact discrepancy?** Document precisely: "Diary says Oct 21 starts at 60196; CSV says 60195; Oct 20 ends at 60194."

#### Step 2: Locate Relevant SU Form Files

1. **List all SU form PDFs** for the team/season:

   ```bash
   ls -la "[Team]/FieldRecords/*.pdf"
   ```

2. **Check filename convention:**
   - Some seasons use date-based naming (e.g., `Oct21.pdf`) — use these directly
   - Some seasons use unit-based or batch naming (e.g., `60192.pdf`) — requires manual investigation

3. **If filenames do not contain dates:** You must sample each file to identify date coverage.

#### Step 3: Sample Files to Identify Date Coverage

For each PDF file with unclear naming:

1. **Read the first form** (page 1, bottom form) — note the date and unit number
2. **Read a middle form** (mid-document) — note the date
3. **Read the last form** (final page, top form) — note the date and unit number

Create an SU Form Index:

```markdown
| File | First Date | Last Date | Unit Range | Pages |
|------|------------|-----------|------------|-------|
| 60192.pdf | Oct 20 | Oct 20 | 60127-60194 | 18 |
| [next file] | ... | ... | ... | ... |
```

**Record this index** in source-inventory.md for future reference — this effort should not be repeated.

#### Step 4: Narrow Down to Relevant Files

Using your index, identify which file(s) should contain the disputed units:

- For a gap between Oct 20 (ends 60194) and Oct 21 (starts 60195 or 60196?), find the file covering Oct 21

#### Step 5: Careful Reading with Open Mind

**Critical:** Do not assume you know the answer. Either the diary or the CSV could be correct.

1. **Read the relevant file thoroughly** — pages may not be in order
2. **Find the specific unit(s) in question** — e.g., look for unit 60195
3. **Note the date on that form** — this is the definitive answer
4. **Record walker names** if relevant to other discrepancies

#### Step 6: Document Findings

Whether the SU form confirms or refutes your initial assumption:

1. **Update the discrepancy log** with SU form evidence
2. **Note the file, page, and specific data** found
3. **If diary was wrong:** Document as "Diary transcription error — SU form confirms [value]"
4. **If CSV was wrong:** Document correction needed

#### Step 7: Update Source Inventory

Add any newly discovered file-to-date mappings to `source-inventory.md`:

```markdown
**ELH 2009 SU Forms:** File naming does not follow date convention.
Manual date identification required. Page numbers are season-continuous.

| File | Date(s) | Unit Range |
|------|---------|------------|
| 60192.pdf | Oct 20 | 60127-60194 |
```

### Lessons Learned: SU Form Investigation

**From D015 (Elhovo 2009 Team A, Oct 21):**

The diary stated "First unit: 60196" but the CSV had 60195. Initial QA assumed the diary was correct based on:

- Blank forms observed after unit 60194 in one PDF file
- Confirmation bias — evidence was interpreted as supporting the diary

**Resolution:** User-directed SU form review found unit 60195 on a form dated 21 October, proving:

- CSV value (60195) was **correct**
- Diary value (60196) was a **transcription error**

**Key lessons:**

1. **Trust continuity as a prior** — CSV value 60195 maintained unit continuity; diary value created a gap
2. **Search exhaustively** — the relevant form was in a different file than initially examined
3. **Record negative findings** — "File X does not contain unit Y" is useful information
4. **Keep an open mind** — do not assume diary is correct; SU forms are the primary field record

---

## Future Additions

### Potential Future Tasks

1. **Dedicated SU form scan for role data:** Systematically review SU form marginal notes across all available PDFs to extract occasional role assignments. High effort but could yield some role data for records currently missing this information.

*Add new rules, heuristics, or observations here as QA progresses*

---

## References

- `docs/qa-issue-template.md` — Standard format for QA issues requiring user approval
- `docs/qa-discrepancies-log.md` — Record of source conflicts and resolutions
- `outputs/source-inventory.md` — Source document locations and reliability notes
- `outputs/name-mapping.csv` — Name standardisation reference
- `outputs/qa-runsheet-elhovo-2010-autumn.md` — Detailed verification findings (ELH 2010 Team B pilot)
- `outputs/qa-runsheet-elhovo-2009-autumn-a.md` — Detailed verification findings (ELH 2009 Team A)
- `outputs/qa-runsheet-elhovo-2009-autumn-b.md` — Detailed verification findings (ELH 2009 Team B)
- `outputs/qa-runsheet-elhovo-2009-autumn-c.md` — **Exemplar runsheet format** (ELH 2009 Team C)
