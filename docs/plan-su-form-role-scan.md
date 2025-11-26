# Plan: Dedicated SU Form Scan for Role Data

**Created:** 26 November 2025
**Status:** Draft — awaiting prioritisation
**Priority:** Low (enhancement task)
**Estimated effort:** High (multi-session task)

---

## Objective

Systematically review Survey Unit (SU) form PDFs to extract role assignment information (PDA Operator, GPS Operator, Paper Recorder) from marginal notes. This data is not consistently recorded but occasionally appears, and could supplement the attribution.csv for records currently missing role information.

---

## Background

### Why This Task Exists

Role assignments (who operated PDA, GPS, or did paper recording) are inconsistently documented:

- **Diaries:** Primary source for roles, but not all diaries record them
- **DPF scans:** Do NOT reliably indicate roles (see O3 in qa-guidance.md)
- **SU forms:** No dedicated role fields, but **marginal notes occasionally contain role information**

### What We Learned (26 November 2025 Experiment)

Examined `70970.pdf` (Elhovo 2009 Team B) to assess SU form utility:

1. **Form structure:** 4 forms per page, bottom form = first unit
2. **Walker data:** Names/initials in position boxes (bottom-left) — reliable
3. **Role data:** No dedicated field; must scan marginal notes
4. **Marginal notes:** Often archaeological observations, but occasionally contain role assignments
5. **Legibility:** Variable; handwritten annotations require careful interpretation

### Current Role Data Gaps

From QA of Elhovo 2009 Team B (20 records):

| Field | Records with Data | Gap |
|-------|-------------------|-----|
| PDA_Operator | 2/20 | 90% missing |
| Paper_Recorder | 15/20 | 25% missing |
| GPS_Operator | 1/20 | 95% missing |
| Photographer | 1/20 | 95% missing |

Similar gaps exist across other seasons.

---

## Scope

### In Scope

| Season | Team | PDF Count | Location |
|--------|------|-----------|----------|
| ELH 2009 | A | 13 | `Elhovo 2010-12-12/2009/Project Records/Team A/FieldRecords/` |
| ELH 2009 | B | 14 | `Elhovo 2010-12-12/2009/Project Records/Team B/FieldRecords/` |
| ELH 2009 | C | 12 | `Elhovo 2010-12-12/2009/Project Records/Team C/FieldRecords/` |
| ELH 2010 | A | Multiple | `Elhovo 2010-12-12/2010/Project Records/Team A/Field Records/` |
| ELH 2010 | B | Multiple | `Elhovo 2010-12-12/2010/Project Records/Team B/Field Records/` |

**Note:** Kazanlak seasons have DPF scans available, so SU forms are lower priority for those seasons.

### Out of Scope

- Kazanlak seasons (DPF scans provide better source)
- Archaeological content extraction (materials, site observations)
- Walker name verification (already confirmed via diary QA)

---

## Methodology

### Phase 1: Preparation

1. **Inventory SU form PDFs** for target seasons
   - List all PDF files with page counts
   - Calculate total pages to review
   - Prioritise by role data gap severity

2. **Create extraction template**
   - Date
   - Unit number (or range)
   - Role type (PDA, GPS, Paper, Photographer, Other)
   - Person assigned
   - Source (filename, page number)
   - Confidence (Clear / Probable / Uncertain)
   - Notes (context, legibility issues)

### Phase 2: Systematic Review

For each PDF file:

1. **Open PDF and navigate page by page**

2. **For each page, examine:**
   - Marginal notes (left margin, right margin, between forms)
   - Notes field on each form
   - Any annotations near walker position boxes
   - Top/bottom of page annotations

3. **Look for role indicators:**
   - Explicit: "PDA: [name]", "GPS: [name]", "Forms: [name]"
   - Implicit: "[name] - PDA", "[name] recording", etc.
   - Abbreviations: "P" for paper, "G" for GPS, etc.

4. **Record findings** in extraction template

5. **Flag ambiguous cases** for review

### Phase 3: Validation and Integration

1. **Cross-reference extracted roles** against:
   - Existing diary-based role data
   - Known walker assignments for that date
   - Team composition patterns

2. **Resolve conflicts** (if SU form contradicts diary)
   - Document in discrepancies log
   - Apply source priority rules

3. **Update attribution.csv** with validated role data
   - Add Extraction_Notes indicating SU form source

---

## Execution Approach

### Option A: Manual Review (Recommended for Initial Pass)

**Process:**
1. Read each PDF using Claude Code's vision capability
2. Examine each page systematically
3. Record findings immediately

**Advantages:**
- Can interpret handwriting context
- Can assess confidence levels
- Can spot unexpected patterns

**Disadvantages:**
- Time-intensive
- Requires focused attention

### Option B: Targeted Sampling

**Process:**
1. Focus on records with known role gaps
2. Only review SU forms for specific dates/units
3. Skip dates where roles are already documented

**Advantages:**
- Reduced scope
- Faster completion

**Disadvantages:**
- May miss role data for dates we thought were complete
- Less systematic

### Recommended Approach

**Start with Option B (targeted sampling) for one team/season:**
- Select ELH 2009 Team B (already QA'd, gaps known)
- Review only SU forms for dates with role gaps (Nov 2-6, Nov 9-13)
- Assess yield before committing to full scan

If yield is promising (>20% of reviewed pages contain role data), expand to Option A for remaining seasons.

---

## Expected Outputs

### Primary Output

**File:** `outputs/su-form-role-extractions.csv`

| Date | Team | Unit_Range | Role | Person | Source_File | Source_Page | Confidence | Notes |
|------|------|------------|------|--------|-------------|-------------|------------|-------|
| 2009-11-03 | B | 70963-70980 | PDA | Scott | 70970.pdf | 5 | Probable | Marginal note "S - PDA" |

### Secondary Outputs

1. **Updated attribution.csv** with new role data
2. **Extraction log** documenting pages reviewed, time spent, yield rate
3. **Observations** on patterns (e.g., certain recorders more likely to note roles)

---

## Effort Estimate

### Per-PDF Estimates

| Activity | Time per PDF |
|----------|--------------|
| Open and orient | 2 min |
| Review pages (30 pages avg) | 15-20 min |
| Record findings | 5 min |
| **Total per PDF** | **~25 min** |

### Total Effort by Scope

| Scope | PDF Count | Est. Hours |
|-------|-----------|------------|
| ELH 2009 Team B only (targeted) | 5-6 PDFs | 2-3 hours |
| ELH 2009 all teams | ~39 PDFs | 15-20 hours |
| ELH 2009 + ELH 2010 | ~50+ PDFs | 20-25 hours |

### Recommended Phasing

| Phase | Scope | Effort | Decision Point |
|-------|-------|--------|----------------|
| Pilot | ELH 2009 Team B, Nov dates only | 2-3 hours | Assess yield |
| Expansion | ELH 2009 remaining teams | 12-15 hours | If pilot yield >20% |
| Full scan | Add ELH 2010 | +5-10 hours | If expansion successful |

---

## Success Criteria

### Minimum Success

- Complete pilot phase
- Document yield rate (role findings per page reviewed)
- Make informed decision on expansion

### Full Success

- Extract role data for >50% of currently-missing role records
- Validate extracted data against existing sources
- Update attribution.csv with new role assignments
- Document methodology for future reference

---

## Risks and Mitigations

| Risk | Likelihood | Impact | Mitigation |
|------|------------|--------|------------|
| Low yield (few role notes found) | Medium | Medium | Start with pilot; abandon if <10% yield |
| Handwriting illegibility | Medium | Low | Flag uncertain entries; don't guess |
| Time overrun | Medium | Low | Set session time limits; track progress |
| Conflicting data with diary | Low | Medium | Apply source priority rules; document conflicts |

---

## Prerequisites

Before starting:

1. ✓ QA guidance updated with SU form interpretation notes
2. ✓ Experiment completed demonstrating feasibility
3. [ ] Inventory of SU form PDFs for target seasons
4. [ ] Extraction template created (CSV or spreadsheet)
5. [ ] Time allocated for pilot phase

---

## Next Steps

1. **Prioritise** this task relative to other QA work
2. **Schedule** pilot phase (2-3 hours)
3. **Create** extraction template
4. **Execute** pilot on ELH 2009 Team B November dates
5. **Evaluate** yield and decide on expansion

---

## References

- `docs/qa-guidance.md` — SU form interpretation guidance (Tier 4 Sources section)
- `outputs/qa-runsheet-elhovo-2009-autumn-b.md` — Role gaps identified
- `outputs/source-inventory.md` — PDF locations

---

## Document History

- **Created:** 26 November 2025
- **Author:** Claude Code
- **Status:** Draft
