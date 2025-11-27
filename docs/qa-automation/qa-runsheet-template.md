# QA Runsheet Template

**Created:** 2025-11-27
**Based on:** qa-runsheet-elhovo-2009-autumn-c.md (exemplar)
**Purpose:** Template for QA runsheet output from automated QA prompt

---

## Template

Replace all `{PARAMETER}` placeholders with actual values.

```markdown
# QA Runsheet: {STUDY_AREA} {YEAR} {SEASON} Team {TEAM}

**Study Area/Season:** {STUDY_AREA} {YEAR} {SEASON}
**Team:** {TEAM}
**QA Date:** {QA_DATE}
**QA Performed By:** {MODEL_NAME} (with {USER_NAME})
**Records:** {RECORD_COUNT}
**Date Range:** {DATE_START} - {DATE_END}

---

## Sources Consulted

| Type | File | Location | Role |
|------|------|----------|------|
| Diary | {DIARY_PRIMARY_FILE} | {DIARY_PRIMARY_PATH} | PRIMARY ({LANGUAGE}, {SIZE}) |
| Diary | {DIARY_SECONDARY_FILE} | {DIARY_SECONDARY_PATH} | SECONDARY ({LANGUAGE}, {SIZE}) |
| DPF scan | {DPF_FILE_PATTERN} | {DPF_PATH} | (if available) |
| SU Forms | {SU_FILE_PATTERN} | {SU_PATH} | Verification |
| Excel | {EXCEL_FILE} | {EXCEL_PATH} | Unit ranges |

---

## Team Composition

### Phase 1: {DATE_RANGE_PHASE1}
- **Leader:** {LEADER_NAME}
- **Walkers:** {WALKER_LIST}

### Phase 2: {DATE_RANGE_PHASE2} (if applicable)
- **Leader:** {LEADER_NAME}
- **Walkers:** {WALKER_LIST}
- **Note:** {ROSTER_CHANGE_NOTES}

{Continue phases as needed to document roster changes}

---

## Record-by-Record Verification

### {DATE} ({DAY_OF_WEEK}) — Units {START_UNIT}-{END_UNIT} {STATUS_ICON}
- **Diary:** {DIARY_QUOTE_OR_SUMMARY}
- **CSV:** {CURRENT_CSV_VALUES}
- **Issue {ISSUE_ID}:** {ISSUE_DESCRIPTION} (if applicable)
- **Status:** CONFIRMED / DISCREPANCY

{Status icons: ✓ = confirmed, ⚠️ = discrepancy found}

{Repeat for each record in the set}

---

## Issues Summary

| ID | Date | Field | Issue | Action |
|----|------|-------|-------|--------|
| {D###} | {DATE} | {FIELD_NAME} | {ISSUE_DESCRIPTION} | {ACTION_REQUIRED} |

---

## Corrections Required

### {ISSUE_ID}: {CORRECTION_TITLE}

**Record:** {DATE}, Team {TEAM}
**Field:** {FIELD_NAME}
**Current:** {CURRENT_VALUE}
**Corrected:** {NEW_VALUE}
**Source evidence:** {DIARY_QUOTE_OR_REFERENCE}
**Reasoning:** {EXPLANATION}

**User Decision:**
- [ ] Approve
- [ ] Modify: _______________

**Status:** Pending

---

{Repeat correction block for each required correction}

---

## Summary Statistics

| Metric | Count |
|--------|-------|
| Records checked | {N} |
| Records confirmed | {N} |
| Issues found | {N} |
| Corrections required | {N} |
| Source gaps | {N} |

### Issues by Category
- QA_Notes errors: {N}
- Walker errors: {N}
- Unit errors: {N}
- Role errors: {N}
- Other: {N}

---

## Notes

{Optional section for observations, diary anomalies, methodology notes}

---

**Document created:** {QA_DATE}
**Last updated:** {QA_DATE}
```

---

## Parameters Reference

| Parameter | Description | Example |
|-----------|-------------|---------|
| `{STUDY_AREA}` | Study area name | Elhovo, Kazanlak |
| `{YEAR}` | Survey year | 2009, 2010, 2011 |
| `{SEASON}` | Survey season | autumn, spring |
| `{TEAM}` | Team letter | A, B, C, D, E |
| `{QA_DATE}` | Date of QA (YYYY-MM-DD) | 2025-11-27 |
| `{MODEL_NAME}` | AI model performing QA | Claude Code, Gemini |
| `{USER_NAME}` | Human reviewer | Shawn Ross |
| `{RECORD_COUNT}` | Number of records verified | 20 |
| `{DATE_START}` | First record date | 2009-10-12 |
| `{DATE_END}` | Last record date | 2009-11-14 |
| `{STATUS_ICON}` | ✓ (confirmed) or ⚠️ (discrepancy) | ✓ |
| `{D###}` | Discrepancy ID | D019 |

---

## Status Values

### Record Status
- **CONFIRMED** — CSV matches source(s)
- **DISCREPANCY** — CSV differs from source(s)
- **SOURCE GAP** — Source unavailable for verification

### Correction Status
- **Pending** — Awaiting user decision
- **✅ APPLIED (YYYY-MM-DD)** — Correction applied to CSV

---

## Non-Survey Days

For days without fieldwork, use this format:

```markdown
### {DATE} ({DAY_OF_WEEK}) — No survey ⚠️
- **Diary:** "{REASON_FROM_DIARY}"
- **CSV:** No units (correct), but has erroneous QA_Note
- **Issue {D###}:** Erroneous QA_Notes text
- **Action:** Replace with "Non-survey day (no field walking conducted)"
```

---

## See Also

- `docs/qa-guidance.md` — Full QA protocol
- `outputs/qa-runsheet-elhovo-2009-autumn-c.md` — Exemplar completed runsheet
