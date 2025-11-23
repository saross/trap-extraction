# TRAP Attribution Data Dictionary

**Dataset:** TRAP Archaeological Survey Attribution Data (2009-2011)
**File:** `outputs/attribution.csv`
**Records:** 268 survey day records
**Last Updated:** 23 November 2025
**Version:** 1.0.0

---

## Overview

This data dictionary documents all 17 columns in the TRAP attribution dataset. The dataset captures field walker (team member) attribution for pedestrian archaeological survey conducted in the Kazanluk Valley, Bulgaria across three field seasons (2009, 2010, 2011).

**Data Model:** Each row represents one survey day for one team, documenting who participated and what area was surveyed.

**Controlled Vocabularies:** See section below for complete taxonomy of controlled values.

---

## Column Definitions

### 1. Date

**Data Type:** String (date format)
**Format:** YYYY-MM-DD (ISO 8601)
**Required:** Yes
**Expected Coverage:** 100%
**Controlled Vocabulary:** No (constrained by survey season dates)

**Description:** Survey date when field walking was conducted.

**Valid Range:**
- 2009 Spring: 2009-03-03 to 2009-03-27
- 2009 Autumn: 2009-10-14 to 2009-11-14
- 2010 Spring: 2010-03-21 to 2010-04-15
- 2010 Autumn: 2010-10-22 to 2010-11-15
- 2011 Autumn: 2011-10-14 to 2011-11-29

**Examples:**
- `2009-03-16`
- `2010-04-08`
- `2011-10-21`

**Source:** Excel SurveySummary files (Tier 1 sources)

**Notes:**
- Two date errors were corrected during extraction:
  - 2010-03-08 → 2010-04-08 (Team C)
  - 2011-11-10 → 2011-10-21 (Team D)
- Three dates flagged as non-survey days in QA_Notes

---

### 2. Team

**Data Type:** String (single character)
**Format:** Single uppercase letter
**Required:** Yes
**Expected Coverage:** 100%
**Controlled Vocabulary:** Yes

**Description:** Team identifier indicating which survey team conducted field walking.

**Valid Values:**
- `A` - Team A (typically Julia Tzvetkova-led)
- `B` - Team B (typically Adela Sobotkova/Petra Janouchová-led)
- `C` - Team C (typically Elena Bozhinova/Bara Weissová-led)
- `D` - Team D (typically Georgi Nekhrizov-led)
- `E` - Team E (Shawn Ross-led, 2009 only)

**Examples:**
- `B`
- `D`

**Source:** Excel SurveySummary files (Tier 1 sources)

**Notes:**
- Team E only participated in 2009 Spring season
- Team composition and leadership varied by season
- See TRAP-Participants.csv for team membership details

---

### 3. Start Unit

**Data Type:** Float (survey unit number)
**Format:** Numeric, 4-5 digits
**Required:** No
**Expected Coverage:** ~93% (18 records missing)
**Controlled Vocabulary:** No (sequence constrained by survey area)

**Description:** First survey unit number in the sequence surveyed by this team on this date.

**Valid Range:**
- Kazanluk 2009: 20001-26999
- Kazanluk 2010: 30001-39999
- Kazanluk 2011: 40001-49999

**Examples:**
- `20127.0`
- `30742.0`
- `41088.0`

**Source:** Excel SurveySummary files (Tier 1 sources)

**Notes:**
- Stored as float due to CSV format (some values have .0 suffix)
- Missing values flagged in QA_Notes as "MISSING: Survey units"
- Unit sequences should be continuous (gaps may indicate non-survey days)

---

### 4. End Unit

**Data Type:** Float (survey unit number)
**Format:** Numeric, 4-5 digits
**Required:** No
**Expected Coverage:** ~93% (18 records missing)
**Controlled Vocabulary:** No (sequence constrained by survey area)

**Description:** Last survey unit number in the sequence surveyed by this team on this date.

**Valid Range:** Same as Start Unit

**Examples:**
- `20153.0`
- `30773.0`
- `41152.0`

**Source:** Excel SurveySummary files (Tier 1 sources)

**Notes:**
- End Unit should be ≥ Start Unit
- Missing values correspond to missing Start Unit values

---

### 5. Leader

**Data Type:** String (person identifier)
**Format:** Full name, initials, or abbreviated name
**Required:** Yes
**Expected Coverage:** 100%
**Controlled Vocabulary:** Semi-controlled (participant list)

**Description:** Team leader name or initials for this survey day.

**Format Variations:**
- Full name: `Julia Tzvetkova`, `Adela Sobotkova`
- Initials: `JT`, `AS`, `NK`
- Abbreviated: `Julia T.`, `Adela`

**Examples:**
- `Julia Tzvetkova`
- `AS`
- `NK`

**Source:** Excel SurveySummary files (Tier 1), Diaries (Tier 2)

**Notes:**
- Leaders are always included in walker lists (standardised policy)
- Name variations exist across sources (see name-mapping.csv)
- Cross-reference with TRAP-Participants.csv for full names

---

### 6. Walkers_Original

**Data Type:** String (pipe-delimited list)
**Format:** Names separated by ` | ` (space-pipe-space)
**Required:** Yes
**Expected Coverage:** 100%
**Controlled Vocabulary:** Semi-controlled (participant list)

**Description:** Original walker names as recorded in source documents, may include Cyrillic Bulgarian text.

**Format:**
- Each walker name separated by ` | `
- May contain Cyrillic characters
- May include initials, full names, or abbreviated names
- Order not significant

**Examples:**
- `Н. Кечева | В. Генчева | Е. Дакашев | Е. Тонкова | А. Антонов`
- `AS | Adela | Petra Janouchová | Petra Tušlová | Bethan Donnelly`
- `Julia Tzvetkova | Nelly | Dessy | Anna | Nadia`

**Source:** Team diaries (Tier 2), PDF forms (Tier 3), Excel summaries (Tier 1)

**Notes:**
- Bulgarian names preserved in original Cyrillic
- Leaders always included (standardised policy applied during extraction)
- See Walkers_Transliterated for Latin script version

---

### 7. Walkers_Transliterated

**Data Type:** String (pipe-delimited list)
**Format:** Names separated by ` | ` (space-pipe-space)
**Required:** Yes
**Expected Coverage:** 100%
**Controlled Vocabulary:** Semi-controlled (participant list)

**Description:** Walkers names transliterated to Latin script, suitable for international use.

**Format:** Same as Walkers_Original but with Cyrillic converted to Latin

**Examples:**
- `N. Kecheva | V. Gencheva | E. Dakashev | E. Tonkova | A. Antonov`
- `AS | Adela | Petra Janouchová | Petra Tušlová | Bethan Donnelly`
- `Julia Tzvetkova | Nelly | Dessy | Anna | Nadia`

**Source:** Derived from Walkers_Original via transliteration or directly from English diaries

**Notes:**
- When English diary used as primary source, may match Walkers_Original
- Transliteration follows standard Bulgarian-to-Latin conventions
- Used for international publication and cross-referencing

---

### 8. PDA_Operator

**Data Type:** String (person identifier)
**Format:** Name or initials
**Required:** No
**Expected Coverage:** <50% (sparse)
**Controlled Vocabulary:** Semi-controlled (participant list)

**Description:** Name of person operating the Personal Digital Assistant (PDA) device for field data entry.

**Examples:**
- `Nadja`
- `Petra`
- (empty - most common)

**Source:** Team diaries (Tier 2) - extracted from narrative descriptions

**Notes:**
- PDA role not systematically documented in most sources
- Extractable from diary narrative phrases like "Nadja operated PDA"
- Often empty due to limited source documentation
- Future enhancement: thorough NLP diary analysis could improve coverage

---

### 9. Paper_Recorder

**Data Type:** String (person identifier)
**Format:** Name or initials
**Required:** No
**Expected Coverage:** <50% (sparse)
**Controlled Vocabulary:** Semi-controlled (participant list)

**Description:** Name of person completing paper field recording forms.

**Examples:**
- `Vera`
- `Dessy`
- (empty - most common)

**Source:** Team diaries (Tier 2) - extracted from narrative descriptions

**Notes:**
- Paper recording role not systematically documented
- Often the same person as PDA_Operator or different for redundancy
- Future enhancement: diary NLP analysis could improve coverage

---

### 10. Data_Editor

**Data Type:** String (person identifier)
**Format:** Name or initials
**Required:** No
**Expected Coverage:** <10% (very sparse)
**Controlled Vocabulary:** Semi-controlled (participant list)

**Description:** Name of person performing data entry or GIS editing after field work.

**Examples:**
- (empty - most common)

**Source:** Team diaries (Tier 2) - rarely documented

**Notes:**
- Very rarely documented in field diaries
- Represents post-field data processing role
- May be recorded in project administrative records not used for this extraction

---

### 11. GPS_Operator

**Data Type:** String (person identifier)
**Format:** Name or initials
**Required:** No
**Expected Coverage:** <50% (sparse)
**Controlled Vocabulary:** Semi-controlled (participant list)

**Description:** Name of person operating GPS device for spatial data collection.

**Examples:**
- `Hamish`
- (empty - most common)

**Source:** Team diaries (Tier 2) - extracted from narrative descriptions

**Notes:**
- GPS operation sometimes mentioned in diary narratives
- Distinct from PDA operation (different devices)
- Future enhancement: diary NLP analysis could improve coverage

---

### 12. Photographer

**Data Type:** String (person identifier)
**Format:** Name or initials
**Required:** No
**Expected Coverage:** <50% (sparse)
**Controlled Vocabulary:** Semi-controlled (participant list)

**Description:** Name of person responsible for field photography.

**Examples:**
- `Hamish`
- (empty - most common)

**Source:** Team diaries (Tier 2) - extracted from narrative descriptions

**Notes:**
- Photography assignments occasionally mentioned in diaries
- Phrases like "Hamish was taking pictures" indicate photographer
- Future enhancement: diary NLP analysis could improve coverage

---

### 13. Author

**Data Type:** String (person identifier)
**Format:** Name or initials
**Required:** No
**Expected Coverage:** ~65% (moderate)
**Controlled Vocabulary:** Semi-controlled (participant list)

**Description:** Author of the diary or field form for this date.

**Examples:**
- `Petra`
- `Adela`
- (empty)

**Source:** Team diaries (Tier 2), PDF forms (Tier 3)

**Notes:**
- More consistently documented than other roles
- Diary authorship sometimes explicit, sometimes implicit
- Important for source provenance

---

### 14. XLS_Source

**Data Type:** String (filename)
**Format:** Excel filename with optional sheet reference
**Required:** Yes (at least one of XLS_Source or PDF_Source)
**Expected Coverage:** 100%
**Controlled Vocabulary:** Semi-controlled (known filenames)

**Description:** Excel SurveySummary filename providing date, team, leader, and unit data.

**Valid Filenames:**
- `KAZ09_SurveySummary.xls`
- `Kaz10_SurveySummary.xlsx`
- `Kaz11_SurveySummary.xlsx`

**Examples:**
- `Kaz10_SurveySummary.xlsx`
- `Kaz11_SurveySummary.xlsx | Sheet: Team A`

**Source:** Master Records directories

**Notes:**
- Primary structured data source (Tier 1)
- Sheet reference added when team-specific sheets used
- All records have XLS_Source (Excel is authoritative for dates/units)

---

### 15. PDF_Source

**Data Type:** String (filename or description)
**Format:** PDF filename or descriptive note
**Required:** No
**Expected Coverage:** ~75%
**Controlled Vocabulary:** Semi-controlled (known filenames)

**Description:** PDF summary form or scanned document providing walker or role data.

**Filename Pattern:** `{Team}_{YYYYMMDD}.pdf`

**Examples:**
- `B_20100408.pdf`
- `C_2011Summary.pdf`
- (empty)

**Source:** Daily progress forms, team summary PDFs

**Notes:**
- Secondary verification source (Tier 3)
- Not all dates have corresponding PDFs
- Used primarily when diary data incomplete
- OCR quality variable in scanned forms

---

### 16. Extraction_Notes

**Data Type:** String (free text)
**Format:** Descriptive notes with source citations
**Required:** No
**Expected Coverage:** ~90%
**Controlled Vocabulary:** No (free text with conventions)

**Description:** Detailed notes documenting extraction source, method, and any special circumstances.

**Common Patterns:**
- `Extracted from {diary name}: {quote from source}`
- `Manual extraction from {source}: {evidence}`
- `Walker names from {source}, roles from {source}`
- Bulgarian text quotes included where relevant

**Examples:**
- `Extracted from A_2010Diary_En.docx: "16.04 Team B: AS, Adela, Petr, Jana, Bethan"`
- `Manual extraction from D_2011Diary_BG.doc: "День 8 (21.10.2011) – 4 трансекти..."`
- `Leaders standardised: Added JT to walkers list (leader policy)`

**Source:** Generated during extraction process

**Notes:**
- Critical for provenance and verification
- Includes Bulgarian quotes for transparency
- Documents manual vs automated extraction
- Records any corrections or interpretations applied

---

### 17. QA_Notes

**Data Type:** String (pipe-delimited flags or descriptive text)
**Format:** Flag phrases separated by ` | ` or single descriptive phrase
**Required:** No
**Expected Coverage:** ~30% (only when issues exist)
**Controlled Vocabulary:** Yes (see taxonomy below)

**Description:** Quality assurance flags and notes documenting data quality issues, missing data, or special cases.

**QA_Notes Taxonomy (Controlled Vocabulary):**

1. **"Complete"** - All walker data present and verified, no issues
2. **"No role data available"** - Walker data complete, role columns empty (acceptable status)
3. **"MISSING: Survey units"** - Unit numbers not present in source data
4. **"NON-SURVEY DAY: {activity}"** - Date listed in Excel but no field walking occurred
   - Example: `NON-SURVEY DAY: Total collections activity`
5. **"Date error corrected: {details}"** - Source date error identified and corrected
6. **"Incomplete"** - Record has missing walker data (used during extraction, now obsolete)
7. **(empty)** - Walker data complete, no special issues to flag

**Examples:**
- `Complete`
- `No role data available`
- `MISSING: Survey units`
- `NON-SURVEY DAY: Rainy day documentation/site visits`
- `Date error corrected: Was 2011-11-10, should be 2011-10-21`
- (empty)

**Source:** Generated during extraction and QA process

**Notes:**
- "MISSING: Survey units" indicates source data limitation, not extraction failure
- "No role data available" is acceptable for 268 records (roles not primary objective)
- Non-survey days flagged to explain presence in Excel but absence in diaries
- All "MISSING: Walkers" flags removed after 100% coverage achieved

---

## Data Relationships

### Leader ⊆ Walkers (Leaders are always walkers)

During extraction, a standardisation policy was applied: team leaders are always included in the walker list. This policy was applied to 139 records (52%) where the leader was not originally listed as a walker.

**Rationale:** Team leaders participated in field walking while also managing the team.

---

### Walkers_Original ↔ Walkers_Transliterated (Paired fields)

These two fields represent the same information in different scripts:
- **Walkers_Original:** As recorded in source (may be Cyrillic)
- **Walkers_Transliterated:** Latin script version for international use

When English diary is primary source, these fields may be identical.

---

### Source Fields → Extraction_Notes (Provenance chain)

The source fields (XLS_Source, PDF_Source) identify **what** sources were used, while Extraction_Notes documents **how** data was extracted and provides direct quotes or evidence.

---

## Controlled Vocabularies Summary

### Team (Closed vocabulary, 5 values)
- A, B, C, D, E

### QA_Notes (Controlled phrases)
- Complete
- No role data available
- MISSING: Survey units
- NON-SURVEY DAY: {activity}
- Date error corrected: {details}
- (empty)

### Source Filenames (Known set)
**Excel:**
- KAZ09_SurveySummary.xls
- Kaz10_SurveySummary.xlsx
- Kaz11_SurveySummary.xlsx

**PDF Pattern:** `{Team}_{YYYYMMDD}.pdf` or `{Team}_{YYYY}Summary.pdf`

---

## Open Context Compatibility

**Archaeological Survey Attribution Model:**
This dataset follows a standard archaeological field survey attribution model common across intensive pedestrian surveys worldwide:

- **Core entities:** Survey day, Survey team, Survey area (units)
- **Personnel roles:** Leader, Walkers, Equipment operators, Recorders
- **Spatial data:** Survey unit sequences (not geometries in this extraction)
- **Temporal data:** Survey dates (ISO 8601)

**Pragmatic approach:** TRAP predates FAIR principles and Open Context standards. This extraction applies retrospective data curation while acknowledging limitations:
- Controlled vocabularies documented post-hoc
- Name standardisation applied pragmatically (see name-mapping.csv)
- Role data incomplete due to source limitations
- Survey unit geometries not included (reference GIS shapefiles separately)

**Future enhancements:**
- Link to published TRAP papers (bibtex available)
- Link to survey unit GIS shapefiles
- Align with Open Context field survey schema where applicable
- Add bounding box coordinates for spatial coverage

---

## Data Quality Metrics

**Coverage Achieved:**
- Date: 268/268 (100%)
- Team: 268/268 (100%)
- Start Unit: 250/268 (93.3%)
- End Unit: 250/268 (93.3%)
- Leader: 268/268 (100%)
- Walkers_Original: 268/268 (100%) ✅
- Walkers_Transliterated: 268/268 (100%) ✅
- PDA_Operator: <50%
- Paper_Recorder: <50%
- GPS_Operator: <50%
- Photographer: <50%
- Author: ~65%
- XLS_Source: 268/268 (100%)
- PDF_Source: ~75%

**Known Limitations:**
1. **Role data sparse:** PDA, GPS, Paper Recorder, Photographer, Data Editor fields have <50% coverage due to limited source documentation
2. **Survey units incomplete:** 18 records missing unit data (not present in Excel sources)
3. **Name variations:** Multiple name forms across sources (resolved via name-mapping.csv)

**Quality Improvements Applied:**
- 2 date errors corrected
- 139 records updated with leader-in-walkers standardisation
- 11 stale "MISSING: Walkers" flags removed
- 100% walker coverage achieved through diary extraction and narrative analysis

---

## Usage Notes

**For researchers:**
- Cross-reference walker names with TRAP-Participants.csv for full participant details
- Use Walkers_Transliterated for international publication
- Check QA_Notes for data quality caveats
- Consult Extraction_Notes for provenance details

**For data analysis:**
- Date field is string, convert to datetime for temporal analysis
- Start/End Unit are float, convert to int for numeric operations
- Walker lists are pipe-delimited strings, split on ` | ` for individual names
- Empty cells represent missing data (not zero or null in most cases)

**For data quality:**
- QA_Notes flags indicate known limitations
- "No role data available" is acceptable (not primary objective)
- "MISSING: Survey units" indicates source limitation
- Non-survey days explained in QA_Notes

---

## Change History

**Version 1.0.0 (23 November 2025):**
- Initial data dictionary created
- Documents final dataset: 268 records, 100% walker coverage
- All 17 columns documented with controlled vocabularies
- QA_Notes taxonomy formalized
- Data relationships documented
- Open Context compatibility assessed

---

**For questions or clarifications:** Please open an issue on GitHub (https://github.com/saross/trap-extraction)

**See also:**
- [README.md](README.md) - Project overview
- [STANDARDS-COMPLIANCE.md](STANDARDS-COMPLIANCE.md) - FAIR/FAIR4RS compliance documentation
- [Data Quality Summary](archive/reports/final/data-quality-summary.md) - Comprehensive quality assessment
