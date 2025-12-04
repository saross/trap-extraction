# Diary Walker Extraction Plan

**Created:** 22 November 2025
**Status:** Approved - Ready for execution

---

## Goal

Extract walker data for 22 XLS-only records from diary sources and update source-inventory.md for accuracy and completeness.

---

## Background

Analysis revealed that all 22 XLS-only records (8.2% of total 269 records) have corresponding diary sources that contain walker data but were not extracted during initial processing. Research verified walker names are present in all 22 diary entries.

---

## PHASE 1: Update Source-Inventory.md

### 1.1 Add Tier 4 Section - Individual Survey Form PDFs

Create new "Tier 4: Individual Survey Form PDFs" section. Group by season/team with unit ranges (SURVEY UNITS ONLY):

- Elhovo 2009 Team A: Unit PDFs 60126-61344 (13 files)
- Elhovo 2009 Team B: Unit PDFs 70122-71463 (14 files)
- Elhovo 2009 Team C: Unit PDFs 80103-81008 (12 files)
- Elhovo 2010 Teams A/B: Individual dated survey form PDFs (20101022.pdf, etc.)

### 1.2 Correct Existing Errors

- Kazanlak 2009 Team D: Remove "MISSING" status from D Diary_BG.doc (file exists, 222 KB)
- Elhovo 2010 Team B: Replace "Team B Journal.docx" with actual files: "Team B Diary.docx" (25 KB) and "Team B Diary new.docx" (26 KB)

### 1.3 Mark Preferred Sources

**Terminology:**
- **PRIMARY/SECONDARY**: Different versions of the same document (curated vs uncurated, preferred vs alternative translations)
- **SUPPLEMENTAL**: Individual/personal diaries providing additional perspective

**Finalized vs Scans folders (Kazanlak 2009 Teams B & D):**
- Mark Finalized folders as PRIMARY (curated, date-named versions)
- Mark Scans folders as SECONDARY (uncurated, generic naming)

**Diary preferences based on file size:**
- Kazanlak 2009: BG versions larger → mark BG as PRIMARY, EN as SECONDARY
- Kazanlak 2010 Team B: EN larger (110 KB vs 42 KB) → mark EN as PRIMARY, BG as SECONDARY
- Kazanlak 2011 Teams B & C: EN larger → mark EN as PRIMARY, BG as SECONDARY
- All others: BG as PRIMARY, EN as SECONDARY

**Individual personal diaries:**
- Elhovo 2009 Team A: Mark "Diary_Aneta.doc" as SUPPLEMENTAL
- Kazanlak 2009 Team C: Compare "C_Journal_En.docx" vs "TeamC_Journal.docx" - if both are team diaries, mark by size; if one is personal, mark SUPPLEMENTAL

### 1.4 Update Last Modified Date

Change from "21 November 2025" to "22 November 2025"

---

## PHASE 2: Develop Walker Extraction Script

### 2.1 Create scripts/extract_diary_walkers.py

Script structure:
```python
# Read attribution.csv, identify 22 XLS-only records
# For each record:
#   - Identify primary diary source from updated source-inventory
#   - Extract text (.doc via antiword, .docx via python-docx)
#   - Parse for date entry
#   - Extract walkers using format-specific patterns:
#     * EN narrative: "Team X contains [names]"
#     * EN structured: "walkers: [names]" or numbered lists
#     * BG structured: "Група: [names]"
#     * Initials: match to name-mapping.csv
#   - Extract roles when available (PDA, GPS, Forms patterns)
#   - Transliterate Bulgarian names (match existing attribution.csv patterns)
#   - Format as pipe-delimited
# Create backup: attribution.csv.backup_diary_extraction
# Update attribution.csv
# Generate detailed extraction report
```

### 2.2 Transliteration Approach

- Analyse existing transliterations in attribution.csv for Bulgarian names
- Build transliteration mapping from existing patterns
- Apply consistently to new extractions

### 2.3 Handle Special Cases

- Yambol 2010-11-14: Expand initials (DG, EJ, RL, SH, AP, JP) using name-mapping.csv
- 2010-03-08 date discrepancy: Flag in Extraction_Notes, extract walker data from 18 March entry
- Narrative entries: Use NLP patterns to extract names from prose

### 2.4 Role Extraction

- Extract when available (Kazanlak 2010 Team B EN diary, Yambol 2010 Team B diary)
- Update PDA_Operator, GPS_Operator, Paper_Recorder, Data_Editor columns
- Estimate ~4-6 records will have role data

---

## PHASE 3: Test Extraction

### 3.1 Test on 3 Sample Records

- Sample 1: 2009-11-09 Team A (narrative EN format)
- Sample 2: 2010-04-02 Team B (structured EN with roles)
- Sample 3: 2010-03-21 Team D (structured BG requiring transliteration)

### 3.2 Verify Against Existing Patterns

- Check transliteration matches existing style
- Confirm pipe-delimiter formatting
- Validate name matching against name-mapping.csv
- Review role extraction format

### 3.3 Generate Test Report

- Show before/after for 3 test records
- Flag any issues or uncertainties
- List names requiring expansion or verification

---

## PHASE 4: Full Extraction

### 4.1 Execute Extraction for All 22 Records

Tier-by-tier execution:
- **Tier 1**: Kazanlak 2010 Spring (12 records) - largest impact
- **Tier 2**: Kazanlak 2011 Autumn (6 records)
- **Tier 3**: Elhovo 2009 Autumn (3 records)
- **Tier 4**: Yambol 2010 (1 record)

### 4.2 Quality Checks

- Verify all 22 records now have walker data
- Check names against name-mapping.csv canonical forms
- Flag any initials needing expansion
- Confirm transliteration consistency

### 4.3 Generate Extraction Report

Report format:
```markdown
# Diary Walker Extraction Report

## Summary
- Records processed: 22
- Successfully extracted: [count]
- Walkers added: [total names]
- Role data added: [count] records
- Flags for review: [count]

## By Record Detail
[Table with: Date, Team, Source, Walkers Extracted, Roles Added, Notes]

## Issues Flagged
- Date discrepancy: 2010-03-08 (diary shows 18 March)
- [Any other issues]

## Name Expansion Needed
[List of initials requiring mapping]
```

---

## PHASE 5: Update Documentation

### 5.1 Update follow-up-actions.md

- Mark "Investigate XLS-only Records" as COMPLETED
- Document extraction approach and results
- Note date discrepancy for 2010-03-08 requiring verification

### 5.2 Create outputs/diary-extraction-report.md

- Comprehensive documentation of extraction process
- Source mapping for each record
- Before/after examples
- Transliteration mapping used

### 5.3 Archive Backup

- Keep attribution.csv.backup_diary_extraction
- Note in follow-up-actions.md

---

## PHASE 6: Commit Changes

### 6.1 Commit source-inventory.md update

```
docs(sources): Update source-inventory with corrections and Tier 4

- Add Tier 4: Individual Survey Form PDFs (39 survey unit files)
- Correct D Diary_BG.doc status (file exists, not missing)
- Fix Elhovo 2010 Team B filenames
- Mark preferred sources using PRIMARY/SECONDARY/SUPPLEMENTAL terminology
- Finalized folders marked PRIMARY, Scans as SECONDARY
- Larger diary versions marked PRIMARY
- Personal diaries marked SUPPLEMENTAL
```

### 6.2 Commit extraction script

```
feat(extraction): Add diary walker extraction script

Script extracts walker and role data from diary sources for
22 XLS-only records. Handles EN narrative, EN structured, and
BG structured formats with transliteration.
```

### 6.3 Commit attribution.csv update

```
feat(data): Extract walker data from diaries for 22 XLS-only records

Filled walker gaps for all 22 records using primary diary sources:
- Elhovo 2009 autumn: 3 records from Team A/C diaries
- Kazanlak 2010 spring: 12 records from BG/EN diaries
- Yambol 2010 autumn: 1 record from Team B diary
- Kazanlak 2011 autumn: 6 records from BG/EN diaries

Role data added for 4-6 records where available.
```

### 6.4 Commit documentation

```
docs: Document diary walker extraction process and results

- Add diary-extraction-report.md with full extraction details
- Update follow-up-actions.md (mark XLS-only investigation complete)
- Flag 2010-03-08 date discrepancy for review
```

---

## DELIVERABLES

1. ✅ Updated source-inventory.md with Tier 4, corrections, and preferences (PRIMARY/SECONDARY/SUPPLEMENTAL terminology)
2. ✅ scripts/extract_diary_walkers.py (new extraction script)
3. ✅ Updated attribution.csv with walker data for all 22 records
4. ✅ outputs/diary-extraction-report.md (comprehensive documentation)
5. ✅ Updated follow-up-actions.md
6. ✅ 4 git commits with clear documentation

---

## SCOPE EXCLUSIONS

**Not included in this extraction:**
- Remote sensing records (GC-RS files)
- Object recording PDFs (A_Objects.pdf, C_Object.pdf, etc.)
- Total pickup records (A_TotalPic.pdf)
- Focus: Survey unit field walking only

---

## ESTIMATED IMPACT

- **Records enriched**: 22 (from 8.2% data gap to 0%)
- **Walker names added**: ~80-120 names
- **Role assignments added**: ~4-6 records
- **Survey unit source files catalogued**: 39 individual unit PDFs
- **Data quality improvement**: All survey day records now have team composition data

---

## 22 XLS-Only Records to Process

### Elhovo 2009 Autumn (3 records)

| Date | Team | Leader | Source | Format |
|------|------|--------|--------|--------|
| 2009-10-23 | C | Bara | The Diary of Team C.doc (EN) | Narrative |
| 2009-11-09 | A | Adela | Diary Team A.doc (EN) | Narrative |
| 2009-11-14 | A | Adela | Diary Team A.doc (EN) | Narrative |

### Kazanlak 2010 Spring (12 records)

| Date | Team | Leader | Source | Format |
|------|------|--------|--------|--------|
| 2010-03-08 | C | Bara | C_2010Diary_BG.doc (214 KB, PRIMARY) | Structured BG |
| 2010-03-21 | D | Zhoro | D_2010Diary_BG.doc (127 KB, PRIMARY) | Structured BG |
| 2010-03-24 | C | Bara | C_2010Diary_BG.doc (214 KB, PRIMARY) | Structured BG |
| 2010-03-25 | C | Bara | C_2010Diary_BG.doc (214 KB, PRIMARY) | Structured BG |
| 2010-03-25 | D | Zhoro | D_2010Diary_BG.doc (127 KB, PRIMARY) | Structured BG |
| 2010-04-02 | B | Adela | B_2010Diary_En.doc (110 KB, PRIMARY) | Structured EN + Roles |
| 2010-04-06 | B | Adela | B_2010Diary_En.doc (110 KB, PRIMARY) | Structured EN + Roles |
| 2010-04-07 | A | Petra | A_2010Diary_BG.doc (86 KB, PRIMARY) | Structured BG |
| 2010-04-07 | B | Adela | B_2010Diary_En.doc (110 KB, PRIMARY) | Structured EN + Roles |
| 2010-04-07 | C | Bara | C_2010Diary_BG.doc (214 KB, PRIMARY) | Structured BG |
| 2010-04-08 | A | Petra | A_2010Diary_BG.doc (86 KB, PRIMARY) | Structured BG |
| 2010-04-08 | B | Adela | B_2010Diary_En.doc (110 KB, PRIMARY) | Structured EN + Roles |

### Yambol 2010 Autumn (1 record)

| Date | Team | Leader | Source | Format |
|------|------|--------|--------|--------|
| 2010-11-14 | B | Royce | Team B Diary.docx (EN) | Structured EN + Roles |

### Kazanlak 2011 Autumn (6 records)

| Date | Team | Leader | Source | Format |
|------|------|--------|--------|--------|
| 2011-10-24 | A | GN | A_2011Diary_BG.doc (BG only) | Structured BG |
| 2011-11-01 | D | AA | D_2011Diary_BG.doc (BG only) | Structured BG |
| 2011-11-02 | D | AA | D_2011Diary_BG.doc (BG only) | Structured BG |
| 2011-11-08 | B | Petra | B_2011Diary_En.docx (63 KB, PRIMARY) | Structured EN |
| 2011-11-10 | D | NK | D_2011Diary_BG.doc (BG only) | Structured BG |
| 2011-11-29 | B | AS | B_2011Diary_En.docx (63 KB, PRIMARY) | Structured EN |

---

## Key Research Findings

### File Size Comparison (BG vs EN)

**Generally BG diaries are 2-10× larger**, indicating more extensive narrative content.

**Exceptions (prefer EN):**
- Kazanlak 2010 Team B: EN 110 KB vs BG 42 KB (2.6× larger)
- Kazanlak 2011 Team B: EN 63 KB vs BG 42 KB (1.5× larger)
- Kazanlak 2011 Team C: EN 70 KB vs BG 18 KB (3.9× larger)

### Transliteration Patterns in attribution.csv

Examples to match:
- `Г. Нехризов` → `G. Nekhrizov`
- `Ю. Цветкова` → `Yu. Tzvetkova`
- `ЮЦ | ЦЦ | ЮД` → `YuTs | TsTs | YuD`
- `Н. Кечева` → `N. Kecheva`

### Date Discrepancy Flag

- **Record**: 2010-03-08, Team C, Leader: Bara
- **Issue**: Diary entry dated "18.03.2010" (18 March), not 8 March
- **Action**: Extract walker data from 18 March entry, flag in Extraction_Notes for user review

---

**Last updated:** 22 November 2025
