# QA Verification Prompt Template

**Created:** 2025-11-27
**Purpose:** Parameterised prompt for autonomous QA verification of TRAP attribution records
**Model-agnostic:** Designed for Claude or Gemini

---

## How to Use This Template

1. Copy the prompt below (everything in the "Prompt" section)
2. Replace all `{PARAMETER}` placeholders with values from qa-queue.yaml
3. Include the CSV data for the target team/season
4. Execute with Claude or Gemini
5. Review the generated runsheet and approve/modify corrections

---

## Prompt

```text
# QA Verification: {STUDY_AREA} {YEAR} {SEASON} Team {TEAM}

## Mission

You are performing Quality Assurance verification on TRAP walker attribution records. Your task is to verify CSV records against source documents and produce a QA runsheet with any required corrections.

**Scope:**
- Study Area: {STUDY_AREA}
- Year: {YEAR}
- Season: {SEASON}
- Team: {TEAM}
- Records: {RECORD_COUNT}
- Date Range: {DATE_START} to {DATE_END}

**Outputs:**
1. QA runsheet: `outputs/qa-runsheet-{area}-{year}-{season}-{team}.md`
2. Corrections added to: `docs/qa-automation/qa-corrections.md` (JSON format)
3. Discrepancy entries added to: `docs/qa-discrepancies-log.md`

---

## Critical Rules (Must Follow)

### Source Priority Table

| Data Type | PRIMARY Source | SECONDARY Source |
|-----------|----------------|------------------|
| Unit numbers (Start_Unit, End_Unit) | DPF scan / SU forms | Diary |
| Walker names | Diary | DPF scan |
| Walker count | Diary | DPF scan |
| Role assignments (PDA, GPS, Paper) | Diary ONLY | — |
| Leader | Diary | DPF scan |
| Dates | DPF scan | Diary |

### Validation Rules (Must Be True)

- **R1:** All role holders must appear in Walkers list
  - If PDA_Operator = "Petra", then "Petra" must be in Walkers_Standardised
- **R2:** Leader must appear in Walkers list
  - If Leader = "Scott Jackson", then "Scott Jackson" must be in Walkers_Standardised
- **C1:** Start Unit should follow previous day's End Unit (±1)
  - If Oct 20 ends at 60194, Oct 21 should start at 60194 or 60195
  - Gaps > 1 indicate potential missing records or errors

### Disambiguation Heuristics

- **H1 (Team stability):** Teams are generally stable within a season. If a name is illegible, check adjacent days for the same team.
- **H2 (One team per day):** A person is on only one team per day. If ambiguous which "Tereza" is meant, verify they don't appear on another team that day.

### Non-Survey Day Convention

When diary indicates no survey occurred (weather, rest day, excursion):
- **QA_Notes:** `Non-survey day (no field walking conducted)`
- **NOT:** `MISSING: Survey units` — nothing is missing; the record is complete
- Document the reason from diary (rain, rest, trip, etc.)

### QA Citation Format

For Source_Notes/Extraction_Notes corrections:
```
QA D###: [description] (YYYY-MM-DD)
```
Example: `QA D021: Removed Georgi - diary states 'walked in five' (2025-11-27)`

### Error Severity

- **MAJOR:** Affects core data (unit numbers, walker names, missing records)
- **Minor:** Affects metadata (author fields, source references)

---

## Source Documents for This Run

| Type | File | Path | Role |
|------|------|------|------|
| Primary Diary | {DIARY_PRIMARY_FILE} | {DIARY_PRIMARY_PATH} | PRIMARY |
| Secondary Diary | {DIARY_SECONDARY_FILE} | {DIARY_SECONDARY_PATH} | SECONDARY |
| DPF Scans | {DPF_FILE_PATTERN} | {DPF_PATH} | Unit verification |
| SU Forms | {SU_FILE_PATTERN} | {SU_PATH} | Tier 4 backup |
| Excel Summary | {EXCEL_FILE} | {EXCEL_PATH} | Unit ranges |

**Source availability notes:**
{SOURCE_NOTES}

---

## Records to Verify

{CSV_DATA}

---

## Workflow

Execute these phases in order:

### Phase 1: Source Discovery

1. Read the primary diary for this team
2. Identify diary coverage dates and any gaps
3. If DPF scans exist, note which files cover which dates
4. Document all sources consulted in the runsheet header

### Phase 2: Team Composition

1. Extract team roster from diary:
   - Who was the leader?
   - Who were the walkers?
   - Were there roster changes during the season?
2. Document roster in "Team Composition" section with phase dates

### Phase 3: Per-Record Verification

For EACH record in the CSV:

1. **Locate diary entry** for this date
2. **Extract from diary:**
   - Walker names and count
   - Unit range (if mentioned)
   - Role assignments (PDA, GPS, Paper)
   - Any notes about absences or changes
3. **Compare CSV values:**
   - Do walkers match?
   - Do units match?
   - Are roles correctly assigned?
4. **Apply rule checks:**
   - R1: Do all role holders appear in walkers?
   - R2: Does leader appear in walkers?
5. **Document finding:**
   - CONFIRMED: CSV matches sources
   - DISCREPANCY: CSV differs (document specifics)

### Phase 4: Cross-Record Checks

After verifying individual records:

1. **Unit continuity:** Verify Start_Unit follows previous End_Unit
2. **Walker consistency:** No duplicate walkers, consistent standardisation
3. **Flag anomalies:** Gaps, overlaps, unexpected patterns

### Phase 5: Documentation

1. **Create runsheet** using template format:
   - Header with scope and sources
   - Team composition with phases
   - Record-by-record verification (REQUIRED)
   - Issues summary table
   - Corrections with inline User Decision checkboxes
   - Summary statistics

2. **For each discrepancy:**
   - Assign ID: D### (continue from existing numbering in qa-discrepancies-log.md)
   - Add correction block to qa-corrections.md (JSON format)
   - Include User Decision checkbox: `[ ] Approve` / `[ ] Modify`

3. **Calculate summary statistics:**
   - Records checked
   - Records confirmed
   - Issues found
   - Corrections required

---

## Output Requirements

### Runsheet Format

Follow the template in `docs/qa-automation/qa-runsheet-template.md`:

- **Daily breakdown is REQUIRED** — each record must have verification entry
- **User Decision checkboxes** appear with each correction (inline)
- **Status field** for each correction (Pending initially)
- **Non-survey days:** Use standard notation

### Corrections JSON Format

Add to `docs/qa-automation/qa-corrections.md`:

```json
{
  "corrections": [
    {
      "id": "C###",
      "discrepancy_ref": "D###",
      "type": "field_update",
      "record": {
        "date": "YYYY-MM-DD",
        "team": "X",
        "study_area": "{STUDY_AREA}"
      },
      "changes": [
        {
          "field": "Field_Name",
          "old_value": "current value",
          "new_value": "corrected value"
        }
      ],
      "extraction_notes_append": "QA D###: description (YYYY-MM-DD)",
      "sources": ["source file, entry location"],
      "reasoning": "explanation",
      "severity": "MAJOR",
      "status": "pending"
    }
  ]
}
```

### Discrepancy Log Format

Add to `docs/qa-discrepancies-log.md`:

```markdown
### D###: {Date} Team {Team} - {Field} {Issue_Type}

**Scope:** {STUDY_AREA} {YEAR} {SEASON}
**Severity:** MAJOR / minor

**Source Values:**
| Source | Value |
|--------|-------|
| CSV | {value} |
| Diary | {value} |
| DPF/SU | {value or N/A} |

**Resolution:** {what was done}

**Reasoning:** {why this decision was made}

**Status:** Pending / ✅ Applied (YYYY-MM-DD)
```

---

## Special Cases

### Seasons Without DPF Scans

- Elhovo 2009: NO DPF scans exist
- Use SU forms (Tier 4) for unit verification if diary data suspicious
- Diary is primary source for all other fields

### Non-Survey Days

If diary indicates no survey occurred:
- Record exists in CSV but has no units
- This is correct — record documents non-survey
- QA_Notes should be: `Non-survey day (no field walking conducted)`
- Document reason from diary

### Name Disambiguation

When names are ambiguous:
1. Check team roster on adjacent days (H1: team stability)
2. Verify person not on another team same day (H2: one team per day)
3. Cross-reference TRAP-Participants.csv if needed
4. Document disambiguation reasoning

### Bulgarian-Only Diaries

For teams with BG diary only (no EN translation):
- Use transliteration for names
- Cross-reference name-mapping.csv for standardisation
- Note any unclear transliterations

---

## Reference Documents

Read these as needed for edge cases:

1. `docs/qa-guidance.md` — Full QA protocol, rules, heuristics, observations
2. `outputs/source-inventory.md` — Source file locations and version notes
3. `docs/qa-automation/qa-runsheet-template.md` — Output structure template
4. `outputs/qa-runsheet-elhovo-2009-autumn-c.md` — Exemplar completed runsheet
5. `outputs/name-mapping.csv` — Name standardisation reference

---

## Completion Checklist

Before finishing, verify:

- [ ] All {RECORD_COUNT} records verified (daily breakdown complete)
- [ ] Runsheet created with all required sections
- [ ] Each correction has User Decision checkbox
- [ ] Corrections added to qa-corrections.md (JSON format)
- [ ] Discrepancies added to qa-discrepancies-log.md
- [ ] Summary statistics calculated
- [ ] Sources consulted documented

---

## Final Output

After completing verification:

1. Write the runsheet to: `outputs/qa-runsheet-{area}-{year}-{season}-{team}.md`
2. Append corrections to: `docs/qa-automation/qa-corrections.md`
3. Append discrepancies to: `docs/qa-discrepancies-log.md`
4. Report completion summary with counts

The runsheet will be reviewed by the user, who will mark User Decisions.
After approval, corrections will be applied to attribution.csv.
```

---

## Parameter Reference

| Parameter | Source | Example |
|-----------|--------|---------|
| `{STUDY_AREA}` | qa-queue.yaml | Elhovo |
| `{YEAR}` | qa-queue.yaml | 2010 |
| `{SEASON}` | qa-queue.yaml | autumn |
| `{TEAM}` | qa-queue.yaml | A |
| `{RECORD_COUNT}` | qa-queue.yaml or count from CSV | 20 |
| `{DATE_START}` | qa-queue.yaml or first CSV date | 2010-10-21 |
| `{DATE_END}` | qa-queue.yaml or last CSV date | 2010-11-14 |
| `{DIARY_PRIMARY_FILE}` | qa-queue.yaml sources.diary_primary | A_Diary.docx |
| `{DIARY_PRIMARY_PATH}` | qa-queue.yaml sources.diary_primary | Elhovo 2010-12-12/2010/... |
| `{DIARY_SECONDARY_FILE}` | qa-queue.yaml sources.diary_secondary | (or "N/A") |
| `{DPF_FILE_PATTERN}` | qa-queue.yaml sources.dpf_scans | Day_*.pdf |
| `{DPF_PATH}` | qa-queue.yaml sources.dpf_scans | .../Field Records/ |
| `{SU_FILE_PATTERN}` | qa-queue.yaml sources.su_forms | (or "N/A") |
| `{SOURCE_NOTES}` | qa-queue.yaml notes | Team B already QA'd... |
| `{CSV_DATA}` | Filter attribution.csv by team/season | (paste filtered rows) |

---

## Preparing CSV Data

Filter attribution.csv for the target team and season:

```bash
# Example: Extract Elhovo 2010 Team A records
head -1 outputs/attribution.csv > temp.csv
grep ",Elhovo,2010,autumn,A," outputs/attribution.csv >> temp.csv
```

Include the header row and all matching records in `{CSV_DATA}`.
