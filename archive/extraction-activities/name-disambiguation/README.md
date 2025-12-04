# Name Disambiguation Archive

**Completion Date:** 22 November 2025
**Project Completion:** 23 November 2025 (100% walker coverage achieved)
**Last Updated:** 25 November 2025

This archive contains all work related to identifying, reviewing, and resolving ambiguous walker names in the attribution data.

**Part of:** TRAP Attribution Extraction Project v1.0.0 (see `../../PROJECT-COMPLETION.md`)

> **⚠️ Important:** The `name-mapping.csv` file in this directory is a **historical snapshot** from the initial disambiguation phase (282 entries). The **authoritative version** with all 698 mappings is located at `outputs/name-mapping.csv` in the repository root.

## Project Summary

- **Name variants identified:** Multiple forms of the same person's name across different sources
- **Ambiguous cases reviewed:** Names that could refer to different people
- **Status:** COMPLETED - All resolvable ambiguities addressed
- **Final coverage:** 698 name mappings in authoritative file (25 Nov 2025)

## Files

- `ambiguous-names-review.md` - Comprehensive review of ambiguous name cases
- `name-corrections-report.md` - Systematic name correction documentation
- `name-mapping.csv` - **HISTORICAL** canonical name mappings (282 entries) - see note above
- `name-mapping-qa-report.md` - Quality assurance review of mappings
- `petra-disambiguation-report.md` - Specific analysis of "Petra" variants

## Key Outcomes

- **283 name mappings created** - Comprehensive canonical name reference
- **111 canonical name replacements applied** across 73 attribution records
- **Standardised name representation** across all records
- **Documented disambiguation decisions** for future reference
- **Major disambiguations resolved:**
  - Helena vs Elena (standardised to "Elena")
  - Petra (Janouchová vs Tušlová - seasonal attendance patterns)
  - Adela (Sobotkova vs Dorňáková - 2010-autumn records)
  - Julia (older Kourilova vs younger Šašinková)
- **6 OCR false positives** marked as invalid (H., Hun, M, P, Olga, X)
- **2 uncertain entries** documented (Lizzy/Lisi - real person, full name being researched)

## Related Files

- **Authoritative name mappings:** `outputs/name-mapping.csv` (698 entries)
- **Attribution data:** `outputs/attribution.csv`
- **Extraction guide:** `archive/old-versions/documentation/manual-extraction-guide.md`
