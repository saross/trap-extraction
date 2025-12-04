# QA Issue Template

Use this format for all QA issues requiring user review.

---

## Template

```markdown
### [ID]: [DATE(s)], Team [X] — [Brief Description]

**Problem:** [One sentence describing what's wrong]

**Fix:** [One sentence describing the correction]

**Sources consulted:**

1. [Source 1] — [specific location/page]
2. [Source 2] — [specific location/page]

**Evidence:**

> "[Relevant quote or description from source]"

**Severity:** MAJOR / Minor
**Status:** Pending approval

---

**User Decision:** [ ] Approve / [ ] Modify: _______________
```

---

## Example (Completed)

```markdown
### D016: 2009-10-26 to 2009-10-29, Team A — Walker Substitution

**Problem:** CSV shows Eric as walker, but Eric departed for Istanbul on Oct 25; Tereza substituted.

**Fix:** Replace Eric/Erik Andersen with Tereza/Tereza Dobrovodská in Walkers_Raw and Walkers_Full for 4 records.

**Sources consulted:**

1. Diary Team A.doc — Oct 25-26 entries

**Evidence:**

> Oct 25: "Eric decided to go on to Istanbul and is dropped off at the busstation"
> Oct 26: "Team A comprises Adela, Ilija, Aneta, Martin and Tereza as a substitute for Eric"

**Severity:** MAJOR (personnel error)
**Status:** Pending approval

---

**User Decision:** [x] Approve / [ ] Modify: _______________
```

---

## Notes

- Always include the **User Decision** line — this is the approval mechanism
- **Problem** and **Fix** should each be one sentence maximum
- Include specific source locations (page numbers, date entries)
- Quote evidence directly when possible
- Mark severity to help prioritise review
