# Attribution CSV Snapshots

**Purpose:** Preserve point-in-time versions of `attribution.csv` for comparison, testing, and audit purposes.

---

## Naming Convention

```text
attribution-YYYY-MM-DD-[description].csv
```

- **YYYY-MM-DD** — Date of snapshot
- **description** — Brief label indicating the state (e.g., `pre-qa-pilot`, `post-extraction`, `gemini-baseline`)

---

## Snapshots

### attribution-2025-11-26-pre-qa-pilot.csv

| Property | Value |
|----------|-------|
| **Date created** | 26 November 2025 |
| **Git commit** | 4955501 |
| **Records** | 267 |
| **Schema** | Original (single `Author` column) |

**Description:** State of attribution.csv before QA pilot corrections were applied. This version:

- Has the original `Author` column (not yet split into `Diary_Author` / `Summary_Author`)
- Contains walker duplicates in `Walkers_Standardised` (77 records affected)
- Missing 2 records that should exist (2010-11-07 B, 2010-11-10 B)
- Contains unit number errors (D005, D006, D007)

**Use cases:**

- Baseline for comparing QA performance between Claude and Gemini
- Audit trail showing what corrections were made
- Testing QA methodology on uncorrected data

---

## Adding New Snapshots

When creating a new snapshot:

1. Use `git show [commit]:outputs/attribution.csv > archive/snapshots/attribution-YYYY-MM-DD-[description].csv`
2. Add an entry to this README with:
   - Date created
   - Git commit (if applicable)
   - Record count
   - Schema version
   - Description of state
   - Use cases
