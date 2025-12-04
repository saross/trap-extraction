# QA Pilot Plan: Elhovo 2010 Autumn

**Date:** 25 November 2025
**Status:** Ready for execution
**Objective:** Cross-source verification of 14 attribution records to validate accuracy and completeness

---

## Pilot Scope

### Records

**14 records** from Elhovo 2010 Autumn (October-November 2010):

| Team | Records | Dates |
|------|---------|-------|
| A | 5 | 22-24 Oct, 2-3 Nov |
| B | 9 | 2-6 Nov, 11-15 Nov |

### Purpose

1. **Validate QA methodology** before applying to full dataset (268 records)
2. **Develop runsheet template** through iterative refinement
3. **Establish source cross-referencing protocols**
4. **Create repeatable documentation** for future QA (e.g., by Gemini)

---

## Source Documents

### Team A

| Type | File | Location | Role |
|------|------|----------|------|
| Diary | A_Diary.docx | `Elhovo 2010-12-12/2010/Project Records/Team A/` | PRIMARY for roles |
| Daily Progress Forms | Day_03.pdf, Day_05.pdf | `Team A/Field Records/` | PRIMARY for basic info |

### Team B

| Type | File | Location | Role |
|------|------|----------|------|
| Diary | Team B Diary new.docx | `Elhovo 2010-12-12/2010/Project Records/Team B/` | PRIMARY (March 2011 corrected) |
| Diary | Team B Diary.docx | Same | SECONDARY (December 2010 field version) |
| Daily Progress Forms | Day_02.pdf, Day_04.pdf, Day_06.pdf, Day_08.pdf, Day_12.pdf | `Team B/Field Records/` | PRIMARY for basic info |

### Note on PDF Dates

The Day_XX.pdf files contain dates within their content (mostly legible), so date correlation can be read directly from the forms rather than requiring external mapping.

### Base Path

`/media/shawn/191c3b96-5fa5-4d0d-8805-0cf05d3d8468/synology/Adela/TRAP-WD-2020-04/`

---

## Source Priority Rules

### For Basic Information (Walkers, Units, Dates)

1. **PDF daily summary forms** - More accurate for basic data
2. **Diaries** - Cross-reference for name interpretation
3. **Both together** for confidence

### For Role Information (PDA, GPS, Paper, etc.)

1. **Diaries only** - PDFs don't contain role data

### Conflict Resolution

- PDF summary forms take precedence for basic info when conflicting with diaries
- Document conflicts in runsheet with evidence from both sources
- Flag for user decision if ambiguous

---

## Rules & Heuristics

Logical constraints that govern the data and help with validation/disambiguation. **This list will grow as we discover more during QA.**

### Rules (Must Be True)

| Rule | Description | Use |
|------|-------------|-----|
| **R1: Roles ⊆ Walkers** | All role holders (Leader, PDA_Operator, Paper_Recorder, GPS_Operator, Photographer, Author) must appear in the Walkers list | Validation check; if a role holder isn't a walker, one or the other is wrong |
| **R2: Leader ∈ Walkers** | The team leader must be included in the walker list | Validation check (special case of R1) |

### Heuristics (Usually True, Helpful for Disambiguation)

| Heuristic | Description | Use |
|-----------|-------------|-----|
| **H1: Team stability** | Teams are generally stable over a season (but not entirely) | If a name is illegible, check nearby days for the same team to complete the walker list |
| **H2: One team per day** | A walker is typically on only one team per day | If unsure which team someone was on, check that they don't appear on another team that day |

### Discovered During QA

*(Add new rules/heuristics here as they emerge)*

---

## Verification Workflow

### Per-Record Process

```text
1. EXTRACT record from attribution.csv
2. LOCATE corresponding PDF daily form
   - Read/transcribe walker names, units, date
3. LOCATE corresponding diary entry
   - Read walker list, roles, any notes
4. COMPARE CSV fields against sources:
   - Date: CONFIRMED / DISCREPANCY
   - Team: CONFIRMED / DISCREPANCY
   - Start Unit: CONFIRMED / DISCREPANCY / SOURCE GAP
   - End Unit: CONFIRMED / DISCREPANCY / SOURCE GAP
   - Leader: CONFIRMED / DISCREPANCY
   - Walkers: CONFIRMED / DISCREPANCY / PARTIAL
   - Roles (PDA, Paper, GPS, etc.): CONFIRMED / DISCREPANCY / SOURCE GAP
5. APPLY RULE CHECKS:
   - R1: Are all role holders in the Walkers list?
   - R2: Is the Leader in the Walkers list?
6. APPLY HEURISTICS if disambiguation needed:
   - H1: Check nearby days for team composition
   - H2: Verify walker isn't on multiple teams same day
7. DOCUMENT findings in runsheet
8. FLAG issues requiring user review
```

### Chunking Strategy

Process by team within season:

1. **Team A** (5 records) - Complete before moving to Team B
2. **Team B** (9 records) - Complete and produce final runsheet

---

## Runsheet Template

### Format for Each Issue Found

```markdown
## QA Issue: Elhovo 2010 Autumn - [DATE] Team [X] - [FIELD]

**Study Area/Season:** Elhovo 2010 Autumn
**Record:** [DATE], Team [TEAM]
**Field:** [FIELD_NAME]

**Current CSV value:** [value]
**Sources consulted:**
1. [PDF filename] - [page/section if applicable]
2. [Diary filename] - [date entry]

**Source evidence:**
- PDF: "[excerpt or description]"
- Diary: "[excerpt or description]"

**Finding:** [DISCREPANCY / CONFIRMED / SOURCE GAP]
**Recommended value:**
- English: [recommended value]
- Cyrillic: [if applicable]

**Reasoning:**
[Explanation of evidence and why change is recommended]

---
**User Decision:** [ ] Accept / [ ] Modify: _______________
```

### Summary Section (End of Runsheet)

```markdown
## Summary: Elhovo 2010 Autumn QA

| Metric | Count |
|--------|-------|
| Records checked | 14 |
| Fields verified | [count] |
| Issues found | [count] |
| Recommended corrections | [count] |
| Source gaps documented | [count] |

### Issues by Category
- Name errors: [count]
- Unit errors: [count]
- Role errors: [count]
- Other: [count]
```

---

## Execution Plan

### Phase 1: Team A (5 records)

| Step | Action |
|------|--------|
| 1.1 | Extract text from A_Diary.docx |
| 1.2 | Read PDF forms (Day_03.pdf, Day_05.pdf) |
| 1.3 | For each of 5 records: compare CSV vs sources |
| 1.4 | Document findings in runsheet draft |
| 1.5 | Present to user for template feedback |

### Phase 2: Refine Template

Based on user feedback from Phase 1:

- Adjust runsheet format as needed
- Clarify any ambiguous protocols
- Confirm conflict resolution approach

### Phase 3: Team B (9 records)

| Step | Action |
|------|--------|
| 3.1 | Extract text from Team B Diary new.docx |
| 3.2 | Read PDF forms (Day_02.pdf, Day_04.pdf, Day_06.pdf, Day_08.pdf, Day_12.pdf) |
| 3.3 | For each of 9 records: compare CSV vs sources |
| 3.4 | Document findings using refined template |

### Phase 4: Produce Final Runsheet

- Compile all findings into single QA runsheet document
- Include summary statistics
- Present to user for review and decisions

### Phase 5: Apply Corrections

After user review:

- Apply accepted corrections to attribution.csv
- Document changes in Extraction_Notes field
- Update QA_Notes as appropriate

---

## Output Deliverables

1. **QA Runsheet** - `outputs/qa-runsheet-elhovo-2010-autumn.md`
   - All issues found with evidence
   - User decision checkboxes
   - Summary statistics

2. **Methodology Document** (if pilot successful)
   - Formalised QA protocol
   - Repeatable by other LLMs
   - Source priority rules

3. **Updated attribution.csv**
   - Corrections applied after user approval
   - Extraction_Notes updated with QA provenance

---

## Success Criteria

### Pilot Success

- [ ] All 14 records verified against sources
- [ ] Runsheet template refined and approved
- [ ] Source cross-referencing protocol validated
- [ ] User comfortable with methodology

### Quality Metrics

- Every field checked against at least one source
- All discrepancies documented with evidence
- All recommendations include reasoning
- Format suitable for user review

---

## Notes

### Known Considerations

1. **PDF readability** - Handwritten forms may be difficult; will note legibility issues
2. **Name variations** - Cross-reference with name-mapping.csv for standardisation
3. **Role coverage** - Elhovo 2010 diaries have good role documentation per source-inventory.md
4. **Team B "new" vs original** - Use "Team B Diary new.docx" as PRIMARY (post-season corrections)

### Tools

- `antiword` for .doc files
- `unzip -p file.docx word/document.xml` for .docx files
- PDF reading via vision capabilities or pdftotext
- `outputs/name-mapping.csv` for name standardisation reference

---

## Future Tasks (Post-Pilot)

- [ ] **Update source-inventory.md** - Clarify varied file naming conventions across seasons:
  - Kazanlak: Consolidated `X_YYYYSummary.pdf` files
  - Elhovo 2010: Individual `Day_XX.pdf` files (day numbers, not dates)
  - Document mapping between naming conventions and actual daily progress forms
