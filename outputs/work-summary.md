# TRAP Data Extraction - Work Summary

**Collaborative work between Dr. Adela Sobotkova and Claude Code**

**Last Updated:** 21 November 2025

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
| Walker coverage | 223/269 (82.9%) |
| Author coverage | 209/269 (77.7%) |
| PDA Operator coverage | 23/269 (8.6%) |
| GPS Operator coverage | 18/269 (6.7%) |
| Paper Recorder coverage | 9/269 (3.3%) |
| Name mappings | 282 entries |
| Mappings resolved | 223 (79%) |
| Mappings needing review | 59 (21%) |

---

## Coverage by Season

| Season | Records | Walker Coverage |
|--------|---------|-----------------|
| 2009 | 125 | 80.8% |
| 2010 | 77 | 81.8% |
| 2011 | 67 | 88.1% |
| **Total** | **269** | **82.9%** |

### Recent Progress

**Tier 2 Diary Extraction:**

- Kazanlak 2009-2011 diaries (Teams A-E, BG and EN versions)
- Elhovo 2010 Team B diary with full role data
- Key ambiguities resolved (Helena→Elena, Baron→Charlotte, etc.)

**Tier 3 PDF Extraction (Vision):**

- Kazanlak 2009 PDFs: Teams A-E (16+ forms)
- Kazanlak 2010 PDFs: Teams A-D (4 summary files)
- Kazanlak 2011 PDFs: Teams B-C (2 summary files)
- Elhovo 2010 PDFs: Teams A-B (20+ daily forms)
- **136 Author entries** extracted via vision analysis
- **12 new records** updated (gaps not covered by diaries)

---

## Working Files

| File | Description | Records |
|------|-------------|---------|
| `final_attribution_v2_cleaned_edited.csv` | Primary attribution dataset | 269 |
| `name-mapping-draft.csv` | Name normalisation mappings | 282 |

---

## Extraction Pipeline Summary

### Phase 1: Excel Survey Summaries (Tier 1)

- **Sources:** 4 Excel files (ELH09, KAZ10, YAM10, KAZ11)
- **Script:** `extract_phase1.py`

### Phase 2: English Diaries (Tier 2)

- **Sources:** Team diaries from 2009-2011 seasons (BG and EN)
- **Scripts:** `extract_phase2.py`, `parse_diaries.py`

### Phase 2b: Role Extraction (Tier 2)

- **Sources:** Elhovo 2010 Team B diary, Kazanlak 2010 Teams A-B diaries
- **Scripts:** `extract_roles_elh2010.py`, `extract_roles_kaz2010.py`
- **Data:** PDA_Operator, GPS_Operator, Paper_Recorder, Photographer, Author

### Phase 3: PDF Daily Progress Forms (Tier 3)

- **Sources:** Scanned PDFs from Kaz 2009-2011, Elhovo 2010
- **Script:** `extract_authors_all_pdfs.py` (136 Author entries)
- **Data:** Author field from handwritten forms (vision extraction)

### Phase 4: NLP Cleaning and Consolidation

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
3. **46 survey days** without walker data (XLS-only records)
4. **Elhovo 2009 diaries** - not yet processed (Teams A, B, C)
5. **Kazanlak 2011 AUS_Diaries** - individual student journals not yet processed

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

**Report generated:** 21 November 2025
