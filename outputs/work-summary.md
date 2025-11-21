# TRAP Data Extraction - Work Summary

**Collaborative work between Dr. Adela Sobotkova and Claude Code**

**Last Updated:** November 2025

---

## Project Overview

This document summarises the collaborative extraction of walker (team member) attribution data from the Tundzha Regional Archaeological Project (TRAP) field survey records, covering the 2009-2011 seasons.

### Objective

Extract team composition data from heterogeneous archaeological field documentation to enable proper credit attribution for survey participants in the project archives and future publications.

### Current Status

| Metric | Value |
|--------|-------|
| Total survey day records | 269 |
| Leader coverage | 267/269 (99.3%) |
| Walker coverage | 210/269 (78.1%) |
| Author coverage | 177/269 (65.8%) |
| Name mappings | 282 entries |
| Mappings resolved | 223 (79%) |
| Mappings needing review | 59 (21%) |

---

## Coverage by Season

| Season | Records | Walker Coverage |
|--------|---------|-----------------|
| 2009 | 94 | 78.7% |
| 2010 | 39 | 94.9% |
| 2011 | 60 | 96.7% |
| XLS-only | 76 | 53.9% |
| **Total** | **269** | **78.1%** |

### Kazanlak 2009 Progress

Recent work focused on Kazanlak 2009 diary extraction:

- **5 team diaries processed** (Teams A-E, Bulgarian and English versions)
- **33 Kaz 2009 records** with 100% walker coverage
- **Key ambiguities resolved:**
  - Helena/Gena/Glena → Elena Bozhinova
  - Baron → Charlotte Devereux Byron
  - Chimela/Tomas → Tomáš Chmela
  - Baba → Bara Weissová
  - Julia 2/Julia (Small) → Yulia Dimitrova
  - Meggie/Megi → Meglena Parvin

---

## Working Files

| File | Description | Records |
|------|-------------|---------|
| `final_attribution_v2_cleaned_edited.csv` | Primary attribution dataset | 269 |
| `name-mapping-draft.csv` | Name normalisation mappings | 282 |

---

## Extraction Pipeline Summary

### Phase 1: Excel Survey Summaries

- **Sources:** 4 Excel files (ELH09, KAZ10, YAM10, KAZ11)
- **Script:** `extract_phase1.py`

### Phase 2: English Diaries (2009 Elhovo)

- **Sources:** 3 diary files (Team A, B, C)
- **Scripts:** `extract_phase2.py`, `parse_diaries.py`

### Phase 2b: PDF Summaries and Bulgarian Diaries

- **PDF Sources:** 20+ Daily Progress Forms
- **Bulgarian Diaries:** Team diaries across all seasons
- **Scripts:** `extract_phase2b_walkers.py`, `parse_bulgarian_diaries_2011.py`

### Phase 3: NLP Cleaning and Consolidation

- **Script:** `extract_phase3.py`, `consolidate_v2.py`

### QA and Name Normalisation

- Duplicate detection and merging
- Narrative text removal
- Cyrillic-to-Latin transliteration
- Name mapping and validation

---

## Outstanding Work

See `follow-up-actions.md` for items requiring attention:

1. **Silvia Ivanova** - appears in Team E 2009 diary but not in participant list
2. **59 name mappings** still marked as `review_needed`
3. **59 survey days** without walker data (XLS-only records)

---

## Source Reference

### Key Input Files

| File | Location |
|------|----------|
| Participant list | `inputs/TRAP-Participants.csv` |
| Kazanlak 2009 diaries | `Kazanluk/2009/Project Records/Team*/` |

### Archived Reports

Point-in-time reports from earlier phases are archived in:
`archive/reports/phase1-extraction/`

---

## Acknowledgements

This extraction pipeline was developed collaboratively by:

- **Dr. Adela Sobotkova** - Project Lead, TRAP
- **Claude Code (Anthropic)** - Extraction pipeline development and automation

---

**Report generated:** November 2025
