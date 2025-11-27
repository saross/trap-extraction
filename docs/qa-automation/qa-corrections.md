# QA Corrections Document

**Created:** 2025-11-27
**Purpose:** Accumulate approved corrections from QA runsheets for batch application to attribution.csv
**Format Version:** 1.0

---

## How to Use This Document

1. **After QA run:** Automated QA adds correction entries to "Pending Corrections" section
2. **User review:** Mark decisions in the User Decision table (Approve/Reject)
3. **Batch application:** Apply all approved corrections to attribution.csv
4. **Archive:** Move applied corrections to "Applied Corrections" section

---

## Correction JSON Schema

Each correction block follows this schema:

```json
{
  "corrections": [
    {
      "id": "C001",                          // Unique correction ID
      "discrepancy_ref": "D024",             // Reference to qa-discrepancies-log.md
      "type": "field_update",                // Type: field_update | record_add | record_delete
      "record": {
        "date": "2010-10-22",                // ISO date (YYYY-MM-DD)
        "team": "A",                         // Team letter
        "study_area": "Elhovo"               // Study area name
      },
      "changes": [
        {
          "field": "Start_Unit",             // CSV column name
          "old_value": "61424",              // Current value in CSV
          "new_value": "61425"               // Corrected value
        }
      ],
      "extraction_notes_append": "QA D024: Corrected start unit (2025-11-28)",
      "sources": ["A_Diary.docx, Oct 22 entry"],
      "reasoning": "Diary shows 61425; DPF unclear",
      "severity": "MAJOR",                   // MAJOR or minor
      "status": "pending"                    // pending | approved | rejected | applied
    }
  ]
}
```

---

## Pending Corrections

{New QA runs add correction blocks here}

---

## Applied Corrections

{Move approved and applied corrections here with `applied_date` field added}

### ELH-2009-C — Elhovo 2009 Autumn Team C

**QA Run:** qa-runsheet-elhovo-2009-autumn-c.md
**QA Date:** 2025-11-27
**Applied Date:** 2025-11-27

```json
{
  "corrections": [
    {
      "id": "C001",
      "discrepancy_ref": "D019",
      "type": "field_update",
      "record": {
        "dates": ["2009-10-14", "2009-10-16", "2009-10-17", "2009-10-18"],
        "team": "C",
        "study_area": "Elhovo"
      },
      "changes": [
        {
          "field": "QA_Notes",
          "old_value": "MISSING: Survey units | No role data available | No autumn survey season: ...",
          "new_value": "Non-survey day (no field walking conducted)"
        }
      ],
      "extraction_notes_append": "QA D019: Non-survey day (2025-11-27)",
      "sources": ["The Diary of Team C.doc"],
      "reasoning": "Diary documents reasons for each non-survey day (tired, rain, trip to Burgas)",
      "severity": "MAJOR",
      "status": "applied",
      "applied_date": "2025-11-27"
    },
    {
      "id": "C002",
      "discrepancy_ref": "D021",
      "type": "field_update",
      "record": {
        "date": "2009-10-22",
        "team": "C",
        "study_area": "Elhovo"
      },
      "changes": [
        {
          "field": "Walkers_Original",
          "old_value": "Bara | Petra Tušlová | Sona | Tereza | Todor | Georgi",
          "new_value": "Bara | Petra Tušlová | Sona | Tereza | Todor"
        },
        {
          "field": "Walkers_Standardised",
          "old_value": "Bara Weissová | Petra Tušlová | Sona Holičková | Tereza Dobrovodská | Todor Vulchev | Georgi Nekhrizov",
          "new_value": "Bara Weissová | Petra Tušlová | Sona Holičková | Tereza Dobrovodská | Todor Vulchev"
        }
      ],
      "extraction_notes_append": "QA D021: Removed Georgi - diary states 'walked in five' (2025-11-27)",
      "sources": ["The Diary of Team C.doc, Oct 22 entry"],
      "reasoning": "Diary states 'Today we walked in five people because Georgi was away'",
      "severity": "MAJOR",
      "status": "applied",
      "applied_date": "2025-11-27"
    },
    {
      "id": "C003",
      "discrepancy_ref": "D023",
      "type": "field_update",
      "record": {
        "date": "2009-11-13",
        "team": "C",
        "study_area": "Elhovo"
      },
      "changes": [
        {
          "field": "Start_Unit",
          "old_value": "80839",
          "new_value": "80939"
        }
      ],
      "extraction_notes_append": "QA D023: Corrected Start_Unit 80839→80939 (2025-11-27)",
      "sources": ["The Diary of Team C.doc, Nov 13 entry"],
      "reasoning": "Diary says units 80939-80969; 80839 is impossible (less than Nov 12 start unit 80910)",
      "severity": "MAJOR",
      "status": "applied",
      "applied_date": "2025-11-27"
    }
  ]
}
```

---

## Document History

| Date | Action | QA Run | Corrections |
|------|--------|--------|-------------|
| 2025-11-27 | Created | — | — |
| 2025-11-27 | Added applied | ELH-2009-C | C001-C003 (D019, D021, D023) |
