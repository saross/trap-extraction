# Plan: Test Source Observations Enhancement

**Created:** 2025-11-27
**Status:** ✅ COMPLETE (2025-11-27)
**Goal:** Validate that the new Source Observations section correctly captures source-vs-source divergences by re-running automation tests on the 4 previously tested team-seasons.

---

## Background

We just implemented the Source Observations enhancement (see `planning/source-observations-enhancement.md`), which adds a new section to QA runsheets to capture source-vs-source divergences — cases where primary sources disagree, regardless of CSV correctness.

Files modified:
- `docs/qa-automation/qa-runsheet-template.md`
- `docs/qa-automation/qa-prompt-template.md`
- `docs/qa-guidance.md`

Now we need to test that the automation correctly populates this section.

---

## Known Source Divergences to Detect

From our manual QA, these source divergences were observed:

### ELH-2010-B (Team B)

| Date | Field | DPF Value | Diary Value | CSV Value | Issue Type |
|------|-------|-----------|-------------|-----------|------------|
| Nov 2 | End_Unit | 71524 | 61524 | 71524 | Diary typo (CSV correct) |
| Nov 4 | End_Unit | 71649 | 71650 | 71650 | Diary error, CSV inherited it |

### ELH-2009-A (Team A)

| Date | Field | SU Form Value | Diary Value | CSV Value | Issue Type |
|------|-------|---------------|-------------|-----------|------------|
| Oct 21 | Start_Unit | 60195 | 60196 | 60195 | Diary transcription error (CSV correct) |

### ELH-2009-B (Team B)

- No DPF scans exist for 2009 — diary-only verification
- No source divergences to document (single-source)

### ELH-2009-C (Team C)

| Date | Field | SU Form/Excel Value | Diary Value | CSV Value | Issue Type |
|------|-------|---------------------|-------------|-----------|------------|
| Oct 15 | End_Unit | 80115 | 80103 | 80115 | Diary transcription error (CSV correct) |
| Nov 12 | End_Unit | 80939 | 80938 | 80939 | Minor diary variance (CSV correct) |

---

## Test Approach

### Phase 1: Re-run Automated QA Tests

For each of the 4 team-seasons, re-generate runsheets with the updated template that includes Source Observations:

1. **ELH-2010-B** — Should capture Nov 2 and Nov 4 DPF-vs-diary divergences
2. **ELH-2009-A** — Should capture Oct 21 SU form-vs-diary divergence
3. **ELH-2009-B** — Should note "No source divergences (single-source verification)"
4. **ELH-2009-C** — Should capture Oct 15 and Nov 12 diary transcription errors

### Phase 2: Verify Source Observations Sections

Check each generated runsheet for:

1. **Source Divergences table** populated correctly
2. **Source Reliability Patterns** — confirms O1 (DPF > diary for units)
3. **Implications for Future QA** — any methodology notes

### Phase 3: Update Comparison Report

Add a new section to `outputs/qa-automation-test/comparison-report.md`:
- "Source Observations Validation"
- Table showing expected vs actual divergences detected
- Overall pass/fail assessment

---

## Files to Modify

| File | Action |
|------|--------|
| `outputs/qa-automation-test/qa-runsheet-elhovo-2010-autumn-b.md` | Add Source Observations section |
| `outputs/qa-automation-test/qa-runsheet-elhovo-2009-autumn-a.md` | Add Source Observations section |
| `outputs/qa-automation-test/qa-runsheet-elhovo-2009-autumn-b.md` | Add Source Observations section |
| `outputs/qa-automation-test/qa-runsheet-elhovo-2009-autumn-c.md` | Add Source Observations section |
| `outputs/qa-automation-test/comparison-report.md` | Add Source Observations validation section |

---

## Implementation Steps

1. [x] Add Source Observations section to ELH-2010-B runsheet (2025-11-27)
2. [x] Add Source Observations section to ELH-2009-A runsheet (2025-11-27)
3. [x] Add Source Observations section to ELH-2009-B runsheet (2025-11-27)
4. [x] Add Source Observations section to ELH-2009-C runsheet (2025-11-27)
5. [x] Update comparison report with validation results (2025-11-27)
6. [x] Report overall pass/fail status (2025-11-27)

---

## Success Criteria

- All known source divergences captured in Source Observations tables
- O1 observation (DPF > diary for units) referenced appropriately
- No false divergences reported
- Comparison report updated with validation summary

---

## Key Files Reference

- Original CSV: `outputs/qa-automation-test/original-attribution.csv`
- Comparison report: `outputs/qa-automation-test/comparison-report.md`
- Template: `docs/qa-automation/qa-runsheet-template.md`
- Test runsheets: `outputs/qa-automation-test/qa-runsheet-elhovo-*.md`

---

## Test Results

**Completed:** 2025-11-27
**Overall Status:** ✅ PASSED

### Summary

| Team-Season | Divergences Expected | Divergences Found | O1 Confirmed |
|-------------|---------------------|-------------------|--------------|
| ELH-2010-B | 2 | 2 | Yes |
| ELH-2009-A | 1 | 1 | Yes |
| ELH-2009-B | 0 (single-source) | 0 | N/A |
| ELH-2009-C | 2 | 2 | Yes |
| **Total** | **5** | **5** | **3/3** |

### Results

- **Precision:** 100% (no false positives)
- **Recall:** 100% (no false negatives)
- **O1 Observation:** Confirmed in all testable cases (DPF/SU forms > diary for units)

### Files Modified

- ✅ `outputs/qa-automation-test/qa-runsheet-elhovo-2010-autumn-b.md`
- ✅ `outputs/qa-automation-test/qa-runsheet-elhovo-2009-autumn-a.md`
- ✅ `outputs/qa-automation-test/qa-runsheet-elhovo-2009-autumn-b.md`
- ✅ `outputs/qa-automation-test/qa-runsheet-elhovo-2009-autumn-c.md`
- ✅ `outputs/qa-automation-test/comparison-report.md`
