# TRAP Data Extraction - Source Inventory

**Created:** November 2025
**Last major update:** 23 November 2025
**Extraction status:** ✅ **100% COMPLETE** (268/268 records with walker data)
**Project completion:** 23 November 2025

This document catalogues all source documents for the TRAP walker attribution extraction project, organised by priority tier and annotated with version relationships and quality guidance.

**All Tier 2 diaries have been processed and walker data extracted.**

## Purpose

This inventory serves dual purposes:
1. **Extraction workflow guide** - Identifies which sources to use for data extraction
2. **Reference documentation** - Explains version relationships and source quality for future research

## Scope

**In scope:** Pedestrian surface survey field walking records (2009-2011)
**Out of scope:** Excavation diaries, Ground Control (GC) monumentalised site records, TRAP 2017-2018, other projects

## File Paths

All paths are relative to:
`/media/shawn/191c3b96-5fa5-4d0d-8805-0cf05d3d8468/synology/Adela/TRAP-WD-2020-04/`

## Tier Structure

Sources are organised into five tiers by data type and priority:

- **Tier 1:** Excel SurveySummary files - Authoritative for dates, teams, leaders, survey unit ranges
- **Tier 2:** Diaries and journals - Primary source for walker names and roles (PDA, GPS, Forms)
- **Tier 3:** Scanned daily progress form PDFs - Secondary verification source, OCR-prone
- **Tier 4:** Individual survey unit form PDFs - Supplemental field walking documentation
- **Tier 5:** Personnel and administrative records - Cross-reference and verification resources

## Version Terminology

**PRIMARY:** Preferred version for extraction
- Curated/corrected files (vs uncurated scans)
- More complete/detailed diaries (larger file size)
- Original working language (usually Bulgarian)
- Post-season corrected versions (vs field versions)

**SECONDARY:** Alternative version of same document
- Uncurated scans (when Finalized version exists)
- Less complete diaries (smaller file size)
- Translations (when BG original exists)
- Field versions (when corrected version exists)

**SUPPLEMENTAL:** Additional perspective, not alternative version
- Personal/individual diaries (vs official team diaries)
- Project leader expedition journals (overall perspective)
- Daily journals (when compiled journal exists)

## Language and File Size

**Bulgarian (BG) vs English (EN):**
- BG diaries are typically PRIMARY (more detailed, original field notes, Bulgarian terminology)
- EN diaries are usually SECONDARY (translations/summaries for international team)
- Exceptions exist where EN was the primary working document (see annotations below)
- File size is reliable indicator: larger file = more complete daily records

**File size ranges:**
- 150-220 KB: Very detailed, comprehensive daily diaries
- 60-110 KB: Moderate detail, full season coverage
- 20-50 KB: Summaries, translations, or incomplete drafts
- <20 KB: Brief summaries or partial coverage

## Using This Inventory

1. **For extraction:** Use PRIMARY version first; consult SECONDARY if PRIMARY missing or unclear
2. **For verification:** Cross-reference Tier 2 (diaries) against Tier 3 (PDFs) for walker accuracy
3. **For name resolution:** Check Tier 5 personnel lists to verify participant names and seasons
4. **For understanding roles:** See methodology documents (Tier 5) for PDA, GPS, Forms definitions

---

## Tier 1: Excel SurveySummary Files

Primary structured data source with dates, teams, leaders, and survey unit ranges.

| Season | File | Location |
|--------|------|----------|
| ELH 2009 | ELH09 SurveySummary.xls | `Elhovo 2010-12-12/2009/Project Records/Master Records/` |
| YAM 2010 | Yam10_SurveySummary.xls | `Elhovo 2010-12-12/2010/Project Records/MasterRecords/` |
| KAZ 2009 | KAZ09_SurveySummary.xls | `Kazanluk/2009/Project Records/Master Records/` |
| KAZ 2010 | Kaz10_SurveySummary.xls | `Kazanluk/2010/Project Records/Master Records/` |
| KAZ 2011 | Kaz11_SurveySummary.xlsx | `Kazanluk/2011-11-30/Project Records/MasterRecords/` |
| KAZ 2011 | Kaz11_SurveySummary_TeamA.xls | `Kazanluk/2011-11-30/Project Records/External Records/BG Team Records/` |
| KAZ 2011 | Kaz11_SurveySummary_TeamD.xls | `Kazanluk/2011-11-30/Project Records/External Records/BG Team Records/` |

---

## Tier 2: Diaries and Journals

Narrative records with walker names, roles (PDA, GPS, Forms), and daily activities.

### Elhovo 2009

| Team | File | Language | Walkers | Roles | Version | Location |
|------|------|----------|---------|-------|---------|----------|
| A | Diary Team A.doc | EN | [ ] | [ ] | PRIMARY | `Elhovo 2010-12-12/2009/Project Records/Team A/` |
| A | Diary_Aneta.doc | EN | [ ] | [ ] | SUPPLEMENTAL (29 KB) | `Elhovo 2010-12-12/2009/Project Records/Team A/` |
| B | DiaryTeamB.doc | EN | [x] | N/A | PRIMARY | `Elhovo 2010-12-12/2009/Project Records/Team B/` |
| B | TeamB_Dnevnik (Ross).doc | BG | [ ] | N/A | SECONDARY (55 KB) | `Elhovo 2010-12-12/2009/Project Records/Team B/` |
| C | The Diary of Team C.doc | EN | [ ] | [ ] | PRIMARY | `Elhovo 2010-12-12/2009/Project Records/Team C/` |
| C | TeamC_Dnevnik.doc | BG | [ ] | [ ] | SECONDARY | `Elhovo 2010-12-12/2009/Project Records/Team C/` |

### Elhovo 2010

| Team | File | Language | Walkers | Roles | Version | Location |
|------|------|----------|---------|-------|---------|----------|
| A | A_Diary.docx | EN | [ ] | [ ] | PRIMARY | `Elhovo 2010-12-12/2010/Project Records/Team A/` |
| B | Team B Diary new.docx | EN | [x] | [x] | PRIMARY (26 KB) | `Elhovo 2010-12-12/2010/Project Records/Team B/` |
| B | Team B Diary.docx | EN | [x] | [x] | SECONDARY (25 KB) | `Elhovo 2010-12-12/2010/Project Records/Team B/` |
| B | Team B Journal.docx | EN | [ ] | [ ] | SECONDARY (25 KB) | `Elhovo 2010-12-12/2010/Project Records/Team B/` |
| B | Team B Journal new.docx | EN | [ ] | [ ] | SECONDARY (25 KB) | `Elhovo 2010-12-12/2010/Project Records/Team B/` |
| - | Diary_Adela2010Fall.docx | EN | [ ] | [ ] | SUPPLEMENTAL | `Elhovo 2010-12-12/2010/Project Records/` |
| GC | Elh10_RSDiary_Bara_RS.docx | EN | [ ] | [ ] | - | `Elhovo 2010-12-12/2010/Project Records/GC-RS/` |
| GC | Elh10_RSDiary_Petra.docx | EN | [ ] | [ ] | - | `Elhovo 2010-12-12/2010/Project Records/GC-RS/` |
| GC | Elh10_RSdiary_Sona.docx | EN | [ ] | [ ] | - | `Elhovo 2010-12-12/2010/Project Records/GC-RS/` |

### Kazanlak 2009

| Team | File | Language | Walkers | Roles | Version | Location |
|------|------|----------|---------|-------|---------|----------|
| - | Diary March 09.doc | EN | [ ] | N/A | SUPPLEMENTAL (47 KB) | `Kazanluk/2009/` |
| - | Adela_JournalSurvey.doc | EN | [ ] | N/A | SUPPLEMENTAL | `Kazanluk/2009/Project Records/` |
| - | Adela_JournalExcav.docx | EN | [ ] | N/A | SUPPLEMENTAL | `Kazanluk/2009/Project Records/` |
| A | A_Diary_BG.doc | BG | [x] | N/A | PRIMARY (198 KB) | `Kazanluk/2009/Project Records/TeamA/` |
| A | A_Diary_En.doc | EN | [x] | N/A | SECONDARY (88 KB) | `Kazanluk/2009/Project Records/TeamA/` |
| B | B_Diary_BG.doc | BG | [x] | N/A | PRIMARY (152 KB) | `Kazanluk/2009/Project Records/TeamB/` |
| B | B_Diary_En.docx | EN | [x] | N/A | SECONDARY (62 KB) | `Kazanluk/2009/Project Records/TeamB/` |
| B | Adela_JournalApr09.docx | EN | [ ] | N/A | SUPPLEMENTAL | `Kazanluk/2009/Project Records/TeamB/` |
| C | C_Diary_BG.doc | BG | [x] | N/A | PRIMARY (215 KB) | `Kazanluk/2009/Project Records/TeamC/` |
| C | C_Journal_En.docx | EN | [ ] | N/A | SECONDARY (27 KB) | `Kazanluk/2009/Project Records/TeamC/` |
| C | TeamC_Journal.docx | EN | [ ] | N/A | SUPPLEMENTAL (20 KB) | `Kazanluk/2009/Project Records/TeamC/` |
| D | D Diary_BG.doc | BG | [x] | N/A | PRIMARY (222 KB) | `Kazanluk/2009/Project Records/TeamD/` |
| D | D_Diary_En.docx | EN | [ ] | N/A | SECONDARY | `Kazanluk/2009/Project Records/TeamD/` |
| E | E Diary_BG.doc | BG | [x] | N/A | PRIMARY (only BG) | `Kazanluk/2009/Project Records/TeamE/` |

### Kazanlak 2010

| Team | File | Language | Walkers | Roles | Version | Location |
|------|------|----------|---------|-------|---------|----------|
| A | A_2010Diary_BG.doc | BG | [x] | N/A | PRIMARY (86 KB) - Coverage: 17 March to 28 March | `Kazanluk/2010/Project Records/Team A/` |
| A | A_2010Diary_En.docx | EN | [x] | [x] | co-PRIMARY - Coverage: April entries (7-9 April) | `Kazanluk/2010/Project Records/Team A/` |
| B | B_2010Diary_En.doc | EN | [x] | [x] | PRIMARY (108 KB) | `Kazanluk/2010/Project Records/Team B/` |
| B | B_2010Diary_BG.docx | BG | [x] | N/A | SECONDARY (42 KB) | `Kazanluk/2010/Project Records/Team B/` |
| C | C_2010Diary_BG.doc | BG | [x] | N/A | PRIMARY (214 KB) | `Kazanluk/2010/Project Records/Team C/` |
| C | C_2010Diary_En.docx | EN | [ ] | N/A | SECONDARY | `Kazanluk/2010/Project Records/Team C/` |
| D | D_2010Diary_BG.doc | BG | [x] | N/A | PRIMARY (127 KB) | `Kazanluk/2010/Project Records/Team D/` |
| D | D_2010Diary_En.docx | EN | [ ] | N/A | SECONDARY | `Kazanluk/2010/Project Records/Team D/` |

### Kazanlak 2011

| Team | File | Language | Walkers | Roles | Version | Location |
|------|------|----------|---------|-------|---------|----------|
| A | A_2011Diary_BG.doc | BG | [x] | N/A | PRIMARY (only BG) | `Kazanluk/2011-11-30/Project Records/Team A/` |
| B | B_2011Diary_En.docx | EN | [x] | N/A | PRIMARY (63 KB) | `Kazanluk/2011-11-30/Project Records/Team B/` |
| B | B_2011Diary_BG.docx | BG | [x] | N/A | SECONDARY (42 KB) | `Kazanluk/2011-11-30/Project Records/Team B/` |
| C | C_2011Diary_En.docx | EN | [x] | N/A | PRIMARY (70 KB) | `Kazanluk/2011-11-30/Project Records/Team C/` |
| C | C_2011Diary_BG.docx | BG | [x] | N/A | SECONDARY (18 KB) | `Kazanluk/2011-11-30/Project Records/Team C/` |
| D | D_2011Diary_BG.doc | BG | [x] | N/A | PRIMARY (only BG) | `Kazanluk/2011-11-30/Project Records/Team D/` |

### Kazanlak 2011 - Individual Journals (AUS_Diaries)

Student journals from the 2011 season, organised by author initials:

| Author | Count | Location |
|--------|-------|----------|
| cchoi | 15 files | `Kazanluk/2011-11-30/AUS_Diaries/cchoi/` |
| gburn | 24 files | `Kazanluk/2011-11-30/AUS_Diaries/gburn/` |
| hmorr | 20+ files | `Kazanluk/2011-11-30/AUS_Diaries/hmorr/` |
| hsinc | 18 files | `Kazanluk/2011-11-30/AUS_Diaries/hsinc/` |
| jmccl | 25 files | `Kazanluk/2011-11-30/AUS_Diaries/jmccl/` |
| jserc | 17 files | `Kazanluk/2011-11-30/AUS_Diaries/jserc/` |
| owarr | 1 file | `Kazanluk/2011-11-30/AUS_Diaries/owarr/` |

---

## Tier 3: Scanned Daily Progress Forms (PDFs)

Handwritten forms scanned to PDF. Quality varies; OCR prone to errors.

### Kazanlak 2009 (PDFs)

| Team | Files | Version | Location |
|------|-------|---------|----------|
| A | A_2009Summary.pdf, A_Summary04Mar-08Mar.pdf, etc. | - | `Kazanluk/2009/Project Records/TeamA/` |
| B | B_2009Summary.pdf, B_Summary04Mar-08Mar.pdf, etc. | PRIMARY (Finalized) | `Kazanluk/2009/Project Records/TeamB/Finalized/` |
| B | B_2009Summary.pdf (scans) | SECONDARY (Scans) | `Kazanluk/2009/Project Records/TeamB/Scans/` |
| C | C_2009Summary.pdf, C_Summary04Mar-06Mar.pdf, etc. | - | `Kazanluk/2009/Project Records/TeamC/` |
| D | D_Summary.pdf | PRIMARY (Finalized) | `Kazanluk/2009/Project Records/TeamD/FInalized/` |
| D | D_Summary.pdf (scans) | SECONDARY (Scans) | `Kazanluk/2009/Project Records/TeamD/Scans/` |
| E | E_Summary.pdf, E_Summary20Mar-25Mar.pdf, etc. | - | `Kazanluk/2009/Project Records/TeamE/` |

### Kazanlak 2010 (PDFs)

| Team | File | Location |
|------|------|----------|
| A | A_2010Summary.pdf | `Kazanluk/2010/Project Records/Team A/FieldRecords/` |
| B | B_2010Summary.pdf | `Kazanluk/2010/Project Records/Team B/FieldRecords/` |
| C | C_2010Summary.pdf | `Kazanluk/2010/Project Records/Team C/FieldRecords/` |
| D | D_2010Summary.pdf | `Kazanluk/2010/Project Records/Team D/FieldRecords/` |

### Kazanlak 2011 (PDFs)

| Team | File | Location |
|------|------|----------|
| B | B_2011Summary.pdf | `Kazanluk/2011-11-30/Project Records/Team B/FieldRecords/` |
| C | C_2011Summary.pdf | `Kazanluk/2011-11-30/Project Records/Team C/FieldRecords/` |

### Elhovo 2010 (PDFs)

Daily field records by date (YYYYMMDD format):

| Team | Files | Location |
|------|-------|----------|
| A | Day_03.pdf, Day_05.pdf, 20101022.pdf, etc. | `Elhovo 2010-12-12/2010/Project Records/Team A/Field Records/` |
| B | Day_02.pdf, Day_04.pdf, ..., Day_12.pdf, 20101102.pdf, etc. | `Elhovo 2010-12-12/2010/Project Records/Team B/Field Records/` |

---

## Tier 4: Individual Survey Form PDFs

Individual survey unit forms scanned to PDF. These complement the consolidated Summary PDFs in Tier 3.

### Elhovo 2009 Survey Unit PDFs

| Team | Unit Range | Count | Location |
|------|------------|-------|----------|
| A | 60126-61344 | 13 files | `Elhovo 2010-12-12/2009/Project Records/Team A/Field Records/` |
| B | 70122-71463 | 14 files | `Elhovo 2010-12-12/2009/Project Records/Team B/Field Records/` |
| C | 80103-81008 | 12 files | `Elhovo 2010-12-12/2009/Project Records/Team C/Field Records/` |

### Elhovo 2010 Dated Survey Form PDFs

| Team | Format | Count | Location |
|------|--------|-------|----------|
| A | 20101022.pdf, 20101023.pdf, etc. | Multiple | `Elhovo 2010-12-12/2010/Project Records/Team A/Field Records/` |
| B | 20101102.pdf, 20101103.pdf, etc. | Multiple | `Elhovo 2010-12-12/2010/Project Records/Team B/Field Records/` |

**Note:** Tier 4 focuses on survey unit field walking forms only. Remote sensing records (GC-RS), object recording PDFs, and total pickup records are excluded from this inventory.

---

## Tier 5: Personnel and Administrative Records

Supporting documents that provide context and verification for walker attribution data.

### Personnel Lists

| Season | File | Location | Purpose |
|--------|------|----------|---------|
| ELH 2009 Fall | ParticipantsF09.xls | `Elhovo 2010-12-12/2009/Admin/Personnel/` | Complete participant roster |
| YAM 2009 Fall | ParticipantsYAMF09.xls | `Elhovo 2010-12-12/2009/Admin/Personnel/` | Complete participant roster |
| KAZ 2010 Spring | ParticipantsS10.xls | `Kazanluk/2010/Admin/Personnel/` | Complete participant roster |
| ELH 2010 Fall | ParticipantsF10.xls | `Elhovo 2010-12-12/2010/Admin/Personnel/` | Complete participant roster |
| KAZ 2011 | Participants.xlsx | `Kazanluk/2011-11-30/Admin/Personnel/` | Complete participant roster |
| KAZ 2011 | Team_preferences_division.docx | `Kazanluk/2011-11-30/Admin/Personnel/` | Team assignment planning |

**Note:** These files provide verification and cross-referencing for walker names found in diaries and PDFs. May help resolve name ambiguities and identify missing personnel.

### Methodology Documents (Reference Only)

| Document | Locations | Purpose |
|----------|-----------|---------|
| Survey Manual.doc | `*/Admin/Work Protocols/Survey/` | Field methodology, role definitions, walker intervals |
| Roles & Duties.docx | `*/Admin/Work Protocols/Survey/` | Base camp role assignments |

**Note:** These documents explain survey methodology and terminology but do not contain walker attribution data. Useful for understanding role terminology (PDA, GPS, Forms) and team organisation. Survey Manual documents 10-15m walker intervals for intensive survey.

---

## Priority Rules

When extracting data, apply these priority rules:

1. **Source Version Terminology**:
   - **PRIMARY**: Preferred version (curated files, larger/more complete diaries, preferred translations)
   - **SECONDARY**: Alternative version of same document (uncurated scans, smaller diaries, alternative translations)
   - **SUPPLEMENTAL**: Personal/individual diaries providing additional perspective (not different versions)

2. **Names**: Prefer PRIMARY diaries for extraction; use larger diaries (BG or EN) as they typically contain more detail
3. **Data conflicts**: Tier 2 (diaries) > Tier 3 (scanned PDFs) > Tier 4 (individual forms) for walker accuracy
4. **Roles (PDA, GPS, Forms)**: Only available in Tier 2 diaries
5. **Dates/Units**: Tier 1 (Excel) is authoritative for survey unit numbers

---

## Expected but Missing Files

Based on the pattern that each season should have a SurveySummary and each team should have diaries and PDF scans:

### Tier 1 (Excel SurveySummary)

All seasons have SurveySummary files. ✓

### Tier 2 (Diaries) - Missing EN Versions

| Season | Team | Missing |
|--------|------|---------|
| KAZ 2009 | E | English diary (only BG exists) |
| KAZ 2011 | A | English diary (only BG exists) |
| KAZ 2011 | D | English diary (only BG exists) |

### Tier 3 (PDF Scans) - Missing

| Season | Team | Status |
|--------|------|--------|
| ELH 2009 | A | No PDF scans found |
| ELH 2009 | B | No PDF scans found |
| ELH 2009 | C | No PDF scans found |
| KAZ 2011 | A | No PDF scans found |
| KAZ 2011 | D | No PDF scans found |

---

## Extraction Status

### Completed

- [x] **Tier 1:** All Excel SurveySummary files processed
- [x] **Tier 2:** Kazanlak 2009-2011 diaries (Teams A-E, BG and EN)
- [x] **Tier 2:** Elhovo 2010 Team B diary (roles extracted)
- [x] **Tier 3:** Kazanlak 2009 PDFs (Teams A-E) - Author data
- [x] **Tier 3:** Kazanlak 2010 PDFs (Teams A-D) - Author data
- [x] **Tier 3:** Kazanlak 2011 PDFs (Teams B-C) - Author data
- [x] **Tier 3:** Elhovo 2010 PDFs (Teams A-B) - Author data

### Not Yet Processed

- [ ] Elhovo 2009 diaries (Teams A, B, C)
- [ ] Kazanlak 2011 individual student journals (AUS_Diaries)
- [ ] Role data from remaining diary sources

---

## Notes

- `.doc` files require `antiword` for extraction
- `.docx` files can be extracted via `unzip -p file.docx word/document.xml`
- Bulgarian text requires transliteration for the Walkers_Transliterated column
- PDF quality varies significantly; diary sources are more reliable
- `Diary March 09.doc` (Kazanlak 2009) is a general expedition diary covering 28 Feb - 19 March 2009, written in narrative style. Contains project-wide activities, training, and daily life but not structured team walker lists. Located in `Kazanluk/2009/` (unusual location - not in Project Records subfolder).

### Version Notes and Annotations

**Elhovo 2009:**
- **Team A:** "Diary Team A.doc" is PRIMARY. "Diary_Aneta.doc" (29 KB, SUPPLEMENTAL) is a personal diary by team member Aneta, providing individual perspective rather than official team record. Duplicate copy exists in `Reports/Otchet/BG Diaries/`.
- **Team B:** "DiaryTeamB.doc" (EN) is PRIMARY. "TeamB_Dnevnik (Ross).doc" (55 KB BG, SECONDARY) is Bulgarian version by Ross. Duplicate copy exists in `Reports/Otchet/BG Diaries/`.

**Elhovo 2010:**
- **Team B versions:** Four diary files exist for Team B 2010. File comparison analysis (23 November 2025) determined that "Team B Diary new.docx" (26 KB, March 2011) is PRIMARY as it contains critical post-season data quality corrections including: corrected object numbers, annotations flagging data errors (e.g., "no such artefact brought to base"), and added missing object records. The December 2010 versions represent the original field recordings. "Diary" vs "Journal" naming is meaningless - these are duplicate files with different names. Initial data extraction was performed from "Team B Diary.docx" (SECONDARY); attribution CSV updated on 23 November 2025 to use PRIMARY version data for all affected records.

**Kazanlak 2009:**
- **Team A:** BG version (198 KB) is PRIMARY - more than twice the size of EN version (88 KB), indicating significantly more detailed daily entries and complete field notes. BG diaries typically contain fuller narratives and Bulgarian-specific terminology.
- **Team B:** BG version (152 KB) is PRIMARY - 2.5x larger than EN version (62 KB), suggesting more complete daily records and detail.
- **Team C - Three versions:** C_Diary_BG.doc (215 KB) is PRIMARY - complete Bulgarian daily diary with detailed field notes. C_Journal_En.docx (27 KB, SECONDARY) is complete English translation/summary of the season. TeamC_Journal.docx (20 KB, SUPPLEMENTAL) is earlier draft of English journal with incomplete entries (missing content for March 12, 20, 23) and uncorrected typos; appears to be working version superseded by C_Journal_En.docx.
- **Team D:** BG version (222 KB) is PRIMARY - largest diary file for 2009, indicating most detailed field records. EN version provided for accessibility.
- **Team E:** BG version only (no English translation created). Use transliteration for walker names.
- **PDF Scans - Teams B & D:** "Finalized" subdirectories contain curated, corrected versions of daily progress forms (PRIMARY). "Scans" subdirectories contain original raw scans (SECONDARY). Use Finalized versions for data extraction.

**Kazanlak 2010:**
- **Team A:** BG version (86 KB) is PRIMARY - file size indicates more complete daily records than EN version.
- **Team B - Unusual pattern:** EN version (108 KB, created 9 Aug 2010) is PRIMARY - significantly more complete than BG version (42 KB, created 13 Aug 2010, 4 days later). File comparison shows EN contains full detailed daily entries with author attributions, while BG is structured differently and missing substantial content. This reverses the normal BG=PRIMARY pattern.
- **Team C:** BG version (214 KB) is PRIMARY - 5x larger than EN version, indicating substantially more detailed field records.
- **Team D:** BG version (127 KB) is PRIMARY - file size indicates more complete daily narratives than EN version.

**Kazanlak 2011:**
- **Team A:** BG version only (no English translation created). Use transliteration for walker names.
- **Team B:** EN version (63 KB) is PRIMARY - 1.5x larger than BG version (42 KB), indicating more complete daily records.
- **Team C:** EN version (70 KB) is PRIMARY - nearly 4x larger than BG version (18 KB), suggesting substantially more detailed entries.
- **Team D:** BG version only (no English translation created). Use transliteration for walker names.

**General pattern:** Bulgarian (BG) diaries are typically PRIMARY as they contain more detailed daily entries, complete field observations, and Bulgarian-specific terminology. English (EN) versions are usually translations/summaries created for international team members and publications. Exceptions occur when EN version was the primary working document (e.g., Kazanlak 2010 Team B, Kazanlak 2011 Teams B & C). File size is a reliable indicator of completeness - larger files contain more daily entries and detail.

---

## Document History

**Created:** November 2025
**Last major update:** 23 November 2025 (comprehensive version annotations and structural improvements)
**Project completion:** 23 November 2025
**Contributors:** Adela Sobotkova, Claude Code

This inventory is a living document. Updates include new source discoveries, version comparisons, and quality notes to support ongoing and future research.

---

**GitHub Repository:** https://github.com/saross/trap-extraction
