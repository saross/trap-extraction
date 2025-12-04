# Supersession Project Archive

**Completion Date:** 23 November 2025

This archive contains all work related to the systematic review and correction of attribution records where SECONDARY or Tier 3 sources were used when PRIMARY sources existed.

## Project Summary

- **Identified:** 2 supersession cases (Yambol 2010 Teams A and B)
- **Records Corrected:** 14 total (9 Team B + 5 Team A)
- **Status:** COMPLETED - All identified issues resolved

## Files

### Main Documentation
- `superseded-sources-comprehensive-review.md` - Complete project documentation with outcomes
- `elhovo-2010-team-b-diary-comparison.md` - Initial Team B analysis

### Team B (Phase 1)
- `team-b-supersession-report.md` - Detailed comparison report
- `team-b-diary-new-extraction.csv` - PRIMARY source data extraction

### Team A (Phase 2)
- `team-a-supersession-report.md` - Detailed comparison report
- `team-a-diary-extraction.csv` - PRIMARY source data extraction

### Obsolete Documentation (Archived 23 November 2025)
- `CLAUDE_CODE_INSTRUCTIONS.md` - Early PDF extraction instructions (superseded by diary-based approach)
- `CLAUDE_CODE_PROMPT.md` - Early PDF extraction prompt (superseded by diary-based approach)

**Note:** These files documented an earlier PDF-based extraction approach that was superseded by the diary-based extraction method actually used. The successful approach is documented in the extraction scripts and final reports.

## Key Improvements

1. Role completeness: Added missing PDA/GPS operator data
2. Name accuracy: Corrected walker names, removed OCR errors
3. Source reliability: Upgraded Tier 3 PDFs to Tier 2 diaries
4. Source currency: Applied post-season corrections (March 2011)
5. Author attribution: Diary authors correctly recorded

## Related Files

- Extraction scripts: `scripts/extract_team_a_diary.py`, `scripts/extract_team_b_diary_new.py`
- Updated data: `outputs/attribution.csv`
- Backups: `outputs/attribution.csv.backup_phase1_*`, `outputs/attribution.csv.backup_phase2_*`

---

**Project completed:** 23 November 2025
**GitHub repository:** https://github.com/saross/trap-extraction
