# Intermediate Data Files

**Last Updated:** 25 November 2025

Working data files generated during extraction pipeline phases. These represent intermediate states between source documents and the final `outputs/attribution.csv`.

## Subdirectories

### diary-extracts/

6 text files containing extracted text from team diaries (2009 season):

- `team-a-2009.txt`, `team-b-2009.txt`, etc.
- `C_Diary_BG_2009.txt` - Bulgarian diary extract

### role-extractions/

8 CSV files from role extraction work (24 Nov 2025):

- `role-extractions-consolidated.csv` - Consolidated role data
- Season/team-specific extraction files (Elhovo 2009, Kazanluk 2009/2011)
- `role-extractions-regex.csv` - Regex-based extractions

## Root Files

- `final_attribution_v2_cleaned.csv` - Cleaned v2 attribution
- `manual-extraction-work.csv` - Manual extraction working file
- `missing_walkers.csv` - Missing walker records
- `phase1_summary.csv`, `phase2_roles.csv`, `phase3_cleaned.csv` - Pipeline phase outputs
- `phase2b_pdf_walkers.csv` - PDF-extracted walker data
- `team_c_2009_diary_parsed.csv` - Team C 2009 diary parsing

## Notes

- These files are **historical artifacts** from the extraction pipeline
- The authoritative final data is `outputs/attribution.csv`
- Retained for provenance and potential debugging
