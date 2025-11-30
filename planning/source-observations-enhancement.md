# Enhancement: Source Observations Section

**Created:** 2025-11-27
**Status:** ✅ IMPLEMENTED (2025-11-27)
**Priority:** Medium

## Problem

Current QA runsheets document CSV errors but don't systematically capture **source-vs-source divergences** — cases where the primary sources themselves disagree or contain errors.

## Examples from Testing

| Date | Field | DPF Value | Diary Value | CSV Value | Issue Type |
|------|-------|-----------|-------------|-----------|------------|
| Nov 2 | End_Unit | 71524 | 61524 | 71524 | Diary typo (CSV correct) |
| Nov 4 | End_Unit | 71649 | 71650 | 71650 | Diary error, CSV inherited it |

## Proposed Solution

Add a **Source Observations** section to the runsheet template:

```markdown
## Source Observations

### Source Divergences

| Date | Field | DPF Value | Diary Value | Resolution | Note |
|------|-------|-----------|-------------|------------|------|
| Nov 2 | End_Unit | 71524 | 61524 (typo) | DPF correct | Digit transposition |
| Nov 4 | End_Unit | 71649 | 71650 | DPF correct | Off-by-one error |

### Source Reliability Patterns Observed

- **O1 confirmed:** DPF more reliable than diary for unit numbers (N cases)
- **New pattern:** [description]

### Implications for Future QA

- [Any refinements to source priority rules]
- [Patterns to watch for]
```

## Benefits

1. **Institutional knowledge**: Documents source reliability for future researchers
2. **Refines methodology**: Evidence base for source priority rules
3. **Distinguishes error types**: CSV error vs inherited source error vs source-only error
4. **Supports O-series observations**: Feeds into qa-guidance.md Observations section

## Implementation

1. Update `docs/qa-automation/qa-runsheet-template.md`
2. Update `docs/qa-automation/qa-prompt-template.md` to require this section
3. Update `docs/qa-guidance.md` Phase 4 documentation requirements

## Files to Modify

- `docs/qa-automation/qa-runsheet-template.md`
- `docs/qa-automation/qa-prompt-template.md`
- `docs/qa-guidance.md`

---

**Implemented:** 2025-11-27

### Files Modified

- ✅ `docs/qa-automation/qa-runsheet-template.md` — Added Source Observations section template
- ✅ `docs/qa-automation/qa-prompt-template.md` — Added Phase 5 step 4, Source Observations format, checklist item
- ✅ `docs/qa-guidance.md` — Added item 7 (Source Observations) to Phase 4.1 required sections
