# Petra Disambiguation Report

**Generated:** 21 November 2025

**Task:** Disambiguate 'Petra' entries between Petra Janouchová and Petra Tušlová based on season/team patterns.

---

## Participant List Context

| Name | Role | Seasons Attended |
|------|------|------------------|
| **Petra Janouchová** | Epigrapher, Field walker | 2009-spring, 2010-spring, 2011-autumn |
| **Petra Tušlová** | Field walker | 2009-spring, 2009-autumn, 2010-spring, 2010-autumn |

**Key Observation:** Both Petras were present in 2009-spring and 2010-spring, requiring team-based disambiguation.

---

## Methodology

### Exclusion-based Assignment

When only one Petra attended a season, all 'Petra' entries are assigned to that person:

- **2009-autumn**: Only Tušlová attended
- **2010-autumn**: Only Tušlová attended
- **2011-autumn**: Only Janouchová attended

### Team Composition Analysis

For overlapping seasons (2009-spring, 2010-spring):

1. **Explicit identifications**: Use nearby records with surnames to anchor assignments
2. **Team stability**: Track consistent team member groupings
3. **Temporal continuity**: Assume same person continues on same team across consecutive days

---

## Assignments

### Clear Assignments (43 records)

#### Petra Janouchová (3 records)

**2011-autumn Team B**
- Dates: 2011-11-12, 2011-11-20, 2011-11-21
- Rationale: Only Janouchová attended 2011-autumn season

#### Petra Tušlová (40 records)

**2009-autumn Team C (14 records)**
- Dates: 2009-10-12 through 2009-10-29 (excluding 2009-10-19)
- Rationale: Only Tušlová attended 2009-autumn season

**2009-spring Team A (8 records)**
- Dates: 2009-03-16, 2009-03-19, 2009-03-20, 2009-03-23, 2009-03-24, 2009-03-25, 2009-03-26, 2009-03-27
- Rationale:
  - March 15 has explicit "Petra T." with "Stalna K." (Stana)
  - March 16-27 show "Petra" consistently with "Stana"
  - Temporal continuity suggests same person (Tušlová) continues on team after explicit identification

**2010-spring Team A (5 records)**
- Dates: 2010-03-24, 2010-03-25, 2010-03-26, 2010-03-27, 2010-03-28
- Rationale:
  - March 22 has explicit "Petra T." on Team A
  - March 24-28 show same team composition (Julia Tzvetkova, Lindsay, Yulia Dimitrova)
  - Temporal continuity suggests Tušlová continues on team

**2010-spring Team B (11 records)**
- Dates: 2010-03-17, 2010-03-18, 2010-03-19, 2010-03-20, 2010-03-21, 2010-03-27, 2010-03-29, 2010-03-30, 2010-03-31, 2010-04-01, 2010-04-09
- Rationale:
  - Petra appears 11 out of 12 Team B survey days
  - Stable core team: Adela (18d), Martin (12d), Pesho (10d), Petra (11d)
  - Pattern suggests Petra was a consistent core member (Tušlová)

**2010-autumn Teams A & B (2 records)**
- Dates: 2010-11-03 (Team A), 2010-11-15 (Team B)
- Rationale: Only Tušlová attended 2010-autumn season

---

## Ambiguous Records (5 records requiring manual review)

### 2009-spring Team A early records (3 records)

**Dates:** 2009-03-07, 2009-03-08, 2009-03-09

**Context:**
- These precede the March 15 explicit "Petra T." identification
- Team composition: Petra with Tereza, Stacey, Yulia
- Different team composition than later Petra+Stana pairing
- March 4, 6, 11 used initials (including "PJ" for Janouchová)
- March 7-9 switched to full first names

**Assignment:** **Ambiguous** - could be either Petra

**Recommendation:** Review source PDF (A_2009Summary.pdf) for handwriting clues or additional context

---

### 2009-spring Team E (1 record)

**Date:** 2009-04-03

**Context:**
- Walkers: Adela, Charlotte, Barbara, Petra, Brian
- Only Team E record with 'Petra'
- Team E had limited documentation

**Assignment:** **Ambiguous** - could be either Petra

**Recommendation:** Review source diary for Team E

---

### 2010-spring Team D (1 record)

**Date:** 2010-03-24

**Context:**
- Walkers: Zhoro, Reza, Marten, Petra, Juliet
- March 23 (previous day) shows "Petra mi" on Team D
- "Petra mi" is unclear - possibly "Petra" + middle initial
- Same date shows Tušlová explicitly on Team A

**Assignment:** **Ambiguous** - but likely Janouchová

**Rationale for Janouchová hypothesis:**
- Tušlová clearly established on Teams A & B in 2010-spring
- Janouchová may have been on Team D
- "Petra mi" on March 23 suggests potential middle initial variant

**Recommendation:** Review source PDF (D_2010Summary.pdf) to clarify "Petra mi" and March 24 handwriting

---

## Implementation

### Script: `scripts/disambiguate_petra.py`

**Function:** Updates `attribution.csv` by replacing generic 'Petra' with canonical names based on date/team criteria.

**Results:**
- 43 records updated with canonical names
- 5 records flagged as ambiguous (left unchanged)

### Name Mapping Update

Updated `name-mapping.csv` entry for 'Petra':
- Status: `disambiguated`
- Notes document the 43 assignments and 5 ambiguous records

---

## Next Steps

1. **Manual PDF Review** (5 records):
   - Review A_2009Summary.pdf for March 7-9 entries
   - Review Team E diary for April 3 entry
   - Review D_2010Summary.pdf for March 23-24 entries (especially "Petra mi")

2. **Update after review**:
   - Update `attribution.csv` with canonical names for resolved ambiguous records
   - Update `name-mapping.csv` status to 'confirmed' once all resolved

---

## Summary Statistics

| Metric | Count |
|--------|-------|
| Total 'Petra' records | 48 |
| Assigned to Petra Janouchová | 3 |
| Assigned to Petra Tušlová | 40 |
| Ambiguous (need review) | 5 |
| 'PJ' entries (already correct) | 3 |

**Coverage:** 43/48 (89.6%) records successfully disambiguated

---

**Generated by:** `scripts/disambiguate_petra.py`

**Date:** 21 November 2025
