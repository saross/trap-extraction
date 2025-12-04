# Plan: QA Automation System

**Created:** 2025-11-27
**Status:** Approved, ready for implementation

**Goal:** Create a reusable QA prompt that can run autonomously to verify attribution.csv records against source documents, produce runsheets, and accumulate corrections for batch application.

**Model-agnostic:** Designed to work with Claude or Gemini.

**Key Design Decisions:**

- **Date format:** ISO 8601 (YYYY-MM-DD) throughout
- **Corrections format:** JSON-in-Markdown (safer parsing, universal support)
- **Prompt strategy:** Hybrid — embed critical rules (~300 words), reference full docs for detail
- **Queue file:** Yes — qa-queue.yaml with source paths and status tracking

---

## Stage 0: Capture Recent Learnings

Before creating automation, update existing documentation with learnings from recent QA sessions.

### 0.1 Update `docs/qa-guidance.md`

Add these missing items discovered during ELH 2009 Teams A, B, C QA:

1. **Non-survey day convention** (new section after "Error Severity"):
   - QA_Notes should read: "Non-survey day (no field walking conducted)"
   - NOT "MISSING: Survey units" — nothing is missing, record is complete
   - Document the reason from diary (rain, rest day, excursion, etc.)

2. **QA citation format in Source_Notes**:
   - Format: `QA D###: [description] (YYYY-MM-DD)`
   - Example: `QA D021: Removed Georgi - diary states 'walked in five' (2025-11-27)`

3. **Runsheet format requirements** (update Phase 4):
   - Daily breakdown is **required** (record-by-record verification section)
   - Inline Approve/Modify checkboxes with each correction (not at end)
   - Include "Status: ✅ APPLIED" after corrections are made

4. **New observation O4** (add to Observations section):
   - **O4:** Name disambiguation via team roster cross-reference
   - Evidence: Tereza disambiguation (D016) - checked who was on which team on which days
   - Implication: When multiple people share a name, use team membership constraints

5. **Add reference to Team C runsheet** in References section

### 0.2 Update `outputs/source-inventory.md`

1. Update extraction status:
   - Change `[ ] Elhovo 2009 diary (Team C)` to `[x] Elhovo 2009 diaries (Teams A, B, C) — QA completed 2025-11-27`

2. Add Team C SU form index entries discovered during QA (if any)

---

## Stage 1: Create QA Automation Infrastructure

### 1.1 File Structure

```text
docs/qa-automation/
    qa-prompt-template.md       # Main parameterised prompt
    qa-runsheet-template.md     # Output structure template
    qa-corrections.md           # Accumulating corrections document (JSON blocks)
    qa-queue.yaml               # Queue of teams to QA with source paths
```

Note: Critical rules (~300 words) embedded directly in prompt; no separate qa-reference-rules.md needed.

### 1.2 Create `qa-queue.yaml`

Queue file with all teams to QA, source paths, and status:

```yaml
# QA Queue - Teams pending verification
# Status: pending | in_progress | complete | skipped

queue:
  # Elhovo 2010 Autumn (partially complete)
  - id: "ELH-2010-A"
    study_area: "Elhovo"
    year: 2010
    season: "autumn"
    team: "A"
    status: "pending"
    record_count: 5
    date_range: ["2010-10-21", "2010-11-14"]
    sources:
      diary_primary: "Elhovo 2010-12-12/2010/Project Records/Team A/A_Diary.docx"
      dpf_scans: "Elhovo 2010-12-12/2010/Project Records/Team A/Field Records/"
      su_forms: null
    notes: "Team B already QA'd as part of pilot"

  # Kazanlak 2009 Spring (Teams A-E)
  - id: "KAZ-2009-A"
    study_area: "Kazanlak"
    year: 2009
    season: "spring"
    team: "A"
    status: "pending"
    sources:
      diary_primary: "Kazanluk/2009/Project Records/TeamA/A_Diary_BG.doc"
      diary_secondary: "Kazanluk/2009/Project Records/TeamA/A_Diary_En.doc"
      dpf_scans: "Kazanluk/2009/Project Records/TeamA/"
      su_forms: null

  # ... (continue for all remaining teams)

completed:
  - id: "ELH-2010-B"
    completed_date: "2025-11-26"
    runsheet: "outputs/qa-runsheet-elhovo-2010-autumn.md"
  - id: "ELH-2009-A"
    completed_date: "2025-11-26"
    runsheet: "outputs/qa-runsheet-elhovo-2009-autumn-a.md"
  - id: "ELH-2009-B"
    completed_date: "2025-11-26"
    runsheet: "outputs/qa-runsheet-elhovo-2009-autumn-b.md"
  - id: "ELH-2009-C"
    completed_date: "2025-11-27"
    runsheet: "outputs/qa-runsheet-elhovo-2009-autumn-c.md"
```

### 1.3 Create `qa-runsheet-template.md`

Based on qa-runsheet-elhovo-2009-autumn-c.md (best example):

```markdown
# QA Runsheet: {Study_Area} {Year} {Season} Team {Team}

**Study Area/Season:** {Study_Area} {Year} {Season}
**Team:** {Team}
**QA Date:** {Date}
**QA Performed By:** {Model} (with {User})
**Records:** {Count}
**Date Range:** {Start_Date} - {End_Date}

---

## Sources Consulted

| Type | File | Location | Role |
|------|------|----------|------|
| Diary | {name} | {path} | PRIMARY/SECONDARY |
| DPF scan | {name} | {path} | (if available) |
| SU Forms | {pattern} | {path} | Verification |

---

## Team Composition

### Phase 1: {Date range}
- **Leader:** {name}
- **Walkers:** {list}

{Document roster changes across phases}

---

## Record-by-Record Verification

### {Date} ({Day}) — Units {Start}-{End} {Status_Icon}
- **Diary:** {quote or summary}
- **CSV:** {current values}
- **Issue {ID}:** {if applicable}
- **Status:** CONFIRMED / DISCREPANCY

{Repeat for each record}

---

## Issues Summary

| ID | Date | Field | Issue | Action |
|----|------|-------|-------|--------|

---

## Corrections Required

### {ID}: {Description}

**Record:** {date}, Team {team}
**Field:** {field_name}
**Current:** {value}
**Corrected:** {value}
**Source evidence:** {quote}
**Reasoning:** {explanation}

**User Decision:**
- [ ] Approve
- [ ] Modify: _______________

**Status:** {Pending / ✅ APPLIED (date)}

---

## Summary Statistics

| Metric | Count |
|--------|-------|
| Records checked | |
| Records confirmed | |
| Issues found | |
| Corrections required | |

---

**Document created:** {date}
**Last updated:** {date}
```

### 1.4 Create `qa-corrections.md`

JSON-in-Markdown format for accumulating corrections:

```markdown
# QA Corrections Document

**Created:** 2025-11-27
**Purpose:** Accumulate approved corrections from QA runsheets for batch application
**Format Version:** 1.0

---

## Pending Corrections

### {QA_RUN_ID} — {Scope}

**QA Run:** qa-runsheet-{area}-{year}-{season}-{team}.md
**Date:** {date}

```json
{
  "corrections": [
    {
      "id": "C001",
      "discrepancy_ref": "D024",
      "type": "field_update",
      "record": {
        "date": "2010-10-22",
        "team": "A"
      },
      "changes": [
        {
          "field": "Start_Unit",
          "old_value": "61424",
          "new_value": "61425"
        }
      ],
      "extraction_notes_append": "QA D024: Corrected start unit (2025-11-28)",
      "sources": ["A_Diary.docx, Oct 22 entry"],
      "reasoning": "Diary shows 61425; DPF unclear",
      "severity": "MAJOR",
      "status": "pending"
    }
  ]
}
```

**User Decision:**

| ID | Status | Decision | Reviewer |
|----|--------|----------|----------|
| C001 | pending | [ ] Approve / [ ] Reject | |

---

## Applied Corrections

{Move approved+applied corrections here with applied_date field added}

---

## Document History

| Date | Action | QA Run | Corrections |
|------|--------|--------|-------------|
```

### 1.5 Create `qa-prompt-template.md`

Main prompt (~3000 words) with embedded critical rules. Key sections:

1. **Mission** — Scope (team, records, date range), outputs expected
2. **Critical Rules (Embedded)** — Source priority table, R1/R2/C1 rules, heuristics H1/H2, non-survey day convention, QA citation format
3. **Reference Documents** — Pointers to qa-guidance.md, source-inventory.md, templates
4. **Source Documents for This Run** — Parameterised table of diary, DPF, SU form paths
5. **Records to Verify** — CSV data for target team/season
6. **Workflow** — 5 phases: Source Discovery, Per-Record Verification, Cross-Record Checks, Documentation, Output
7. **Output Requirements** — Runsheet format, JSON corrections format, discrepancy log format
8. **Special Cases** — Non-survey days, seasons without DPF scans, name disambiguation
9. **Completion Checklist**

---

## Stage 2: Usage Workflow

### Running QA

1. **Prepare prompt:** Fill parameters from qa-queue.yaml
2. **Execute:** Run prompt with Claude or Gemini
3. **Review:** Check runsheet, mark User Decisions
4. **Apply:** After all teams reviewed, apply corrections from qa-corrections.md

### Remaining Teams to QA

| Study Area | Year | Season | Team | Status |
|------------|------|--------|------|--------|
| Elhovo | 2010 | Autumn | A | Pending |
| Kazanlak | 2009 | Spring | A-E | Pending |
| Kazanlak | 2010 | Spring | A-D | Pending |
| Kazanlak | 2011 | Spring | A-D | Pending |

---

## Files to Create/Modify

| File | Action |
|------|--------|
| `docs/qa-guidance.md` | Update with Stage 0 learnings |
| `outputs/source-inventory.md` | Update Team C QA status |
| `docs/qa-automation/qa-queue.yaml` | Create (populate all remaining teams) |
| `docs/qa-automation/qa-runsheet-template.md` | Create |
| `docs/qa-automation/qa-corrections.md` | Create (empty, ready for first run) |
| `docs/qa-automation/qa-prompt-template.md` | Create (with embedded critical rules) |

---

## Implementation Order

1. Stage 0.1: Update qa-guidance.md with learnings
2. Stage 0.2: Update source-inventory.md status
3. Stage 1.2: Create qa-queue.yaml with all remaining teams
4. Stage 1.3: Create qa-runsheet-template.md
5. Stage 1.4: Create qa-corrections.md (empty template)
6. Stage 1.5: Create qa-prompt-template.md
7. Commit all changes
8. Test: Run prompt on ELH-2010-A (next in queue)
