# GeoJSON to Attribution Join Report

**Generated:** 5 December 2025
**Author:** TRAP Data Extraction Project
**For:** Adela Sobotkova (error resolution)

---

## Executive Summary

This report documents the joining of GeoJSON survey unit polygon files with walker attribution data from `attribution.csv`. The join was performed to combine spatial data with walker information for Archaeological Knowledge Base (AKB) submission.

**Key outcomes:**

- **12,479 survey units** successfully joined (7,707 Kazanlak + 4,772 Yambol)
- **502 error records** flagged for review
- **7 error types** detected, ranging from data quality issues to cross-validation failures

---

## Input Files

| File | Description | Records |
|------|-------------|---------|
| `inputs/kaz-survey-units-reproj-w-uuids.geojson` | Kazanlak survey unit polygons | 7,707 features |
| `inputs/yam-survey-units-reproj-w-uuids.geojson` | Yambol/Elhovo survey unit polygons | 4,772 features |
| `outputs/attribution.csv` | Walker attribution data with unit ranges | 273 records (248 with unit ranges) |
| `outputs/name-mapping.csv` | Name mappings for leader cross-validation | 357 records |

---

## Output Files

| File | Description | Records |
|------|-------------|---------|
| `outputs/kaz-attribution-joined.csv` | Kazanlak joined data with Flag column | 7,707 |
| `outputs/yam-attribution-joined.csv` | Yambol joined data with Flag column | 4,772 |
| `outputs/join-error-report.csv` | Detailed error log with explanations | 500 |

---

## Processing Statistics

### Kazanlak Region

| Metric | Count |
|--------|-------|
| Total features | 7,707 |
| Matched to attribution | 7,544 |
| No match (NO_MATCH) | 163 |
| Duplicate units (DUPLICATE_UNITS) | 2 |
| Duplicate GeoJSON SUIDs (DUPLICATE_GIS_SU) | 4 |
| Date mismatches | 0 |
| Team mismatches | 0 |
| Leader mismatches | 203 |
| Orphan attribution ranges | 4 |

### Yambol/Elhovo Region

| Metric | Count |
|--------|-------|
| Total features | 4,772 |
| Matched to attribution | 4,651 |
| No match (NO_MATCH) | 119 |
| Duplicate units (DUPLICATE_UNITS) | 2 |
| Duplicate GeoJSON SUIDs (DUPLICATE_GIS_SU) | 5 |
| Date mismatches | 0 |
| Team mismatches | 0 |
| Leader mismatches | 0 |
| Orphan attribution ranges | 0 |

---

## Error Types Explained

### 1. NO_MATCH (282 records)

**Description:** GeoJSON survey unit not found in any attribution range.

**Cause:** These are units that exist as GeoJSON polygons but have no corresponding entry in `attribution.csv`. Many of these are documented field gaps (units that were never assigned during fieldwork).

**Resolution:** Review against `planning/follow-up-actions.md` which documents known gaps. Most are expected inter-season gaps or documented field numbering anomalies.

**Breakdown:**

- Kazanlak: 163 units
- Yambol: 119 units

---

### 2. LEADER_MISMATCH (203 records)

**Description:** The leader recorded in GeoJSON (as initials) does not match the leader in attribution.csv.

**Cause:** GeoJSON uses initials (e.g., "PJ", "BW", "SAR") which are mapped to canonical names via `name-mapping.csv`. Mismatches occur when:

1. The GeoJSON recorded a different leader than attribution.csv
2. The initials map to a different person than expected
3. Data entry errors in either source

**Leader Mismatch Patterns:**

| GeoJSON Leader | Mapped To | Attribution Leader | Count | Notes |
|----------------|-----------|-------------------|-------|-------|
| PJ | Petra Janouchová | Petra Tušlová | 87 | Different Petra |
| PJ | Petra Janouchová | Joel Sercombe | 52 | Completely different person |
| BW | Bara Weissová | Cecilia Choi | 34 | Different person |
| BW | Bara Weissová | Petra Tušlová | 25 | Different person |
| SAR | Shawn Ross | Bara Weissová | 5 | Different person |

**Resolution required:** Investigate whether:

- GeoJSON recorded the wrong leader
- Attribution.csv has incorrect leader
- The initials mapping is incorrect for these specific contexts
- There were leadership changes during the day not captured in one source

---

### 3. DUPLICATE_GIS_SU (9 records)

**Description:** The same Survey Unit ID (SUID) appears multiple times in the GeoJSON file. This is a GIS data quality issue where the same unit number was assigned to multiple polygons.

**Kazanlak duplicates (4 SUIDs):**

| SUID | Occurrences | Team |
|------|-------------|------|
| 10945 | 7 | A |
| 11334 | 2 | A |
| 30332 | 2 | C |
| 30962 | 2 | C |

**Yambol duplicates (5 SUIDs):**

| SUID | Occurrences | Team |
|------|-------------|------|
| 60479 | 2 | A |
| 61317 | 2 | A |
| 61549 | 2 | A |
| 70185 | 2 | B |
| 71029 | 2 | B |

**Resolution required:** GIS review needed to determine:

- Are these genuine duplicate polygons (same unit surveyed twice)?
- Data entry errors during GIS digitisation?
- Should duplicates be merged or one removed?

---

### 4. ORPHAN_ATTRIBUTION (4 records)

**Description:** Attribution ranges where no GeoJSON polygons exist for those unit numbers.

**Affected ranges:**

| Date | Team | Range | Leader | Notes |
|------|------|-------|--------|-------|
| 2009-03-31 | E | 50520-50542 | Shawn Ross | 23 units with no polygons |
| 2011-11-01 | D | 41454-41470 | Anani Antonov | 17 units with no polygons |
| 2011-11-02 | D | 41471-41477 | Anani Antonov | 7 units with no polygons |
| 2011-11-29 | B | 22600-22613 | Adela Sobotkova | 14 units with no polygons |

**Resolution required:** Investigate whether:

- Polygons were never digitised for these units
- Unit numbers in attribution.csv are incorrect
- These units were recorded but data was lost

---

### 5. DUPLICATE_UNITS (4 records)

**Description:** Survey units with duplicate field recording — either the same unit number used on multiple days (multi-day) or the same unit number assigned to two different SU forms on the same day (same-day).

#### Multi-Day Duplicate

**Affected unit:** 61549 (Yambol Team A)

| Date | Range | Leader |
|------|-------|--------|
| 2010-10-24 | 61476-61549 (end) | Adéla Dorňáková |
| 2010-11-02 | 61549-61586 (start) | Petra Tušlová |

**Explanation:** Unit 61549 was used as the end unit on 24 October and the start unit on 2 November. The same physical unit was recorded on both days.

**Status:** Documented in `attribution.csv` QA_Notes and `planning/follow-up-actions.md` (ELH10A-OV1). Pending project-level decision on resolution strategy.

#### Same-Day Duplicates

These are field recording errors where the same unit number was assigned to two different SU forms on the **same day**.

| ID | Unit | Team | Date | Range | Issue |
|----|------|------|------|-------|-------|
| F006 | 40100 | Kazanlak D | 2009-03-23 | 40096-40111 | Two distinct SU forms exist ("Near village" vs "Pine trees") |
| F009 | 11142 | Kazanlak A | 2010-04-08 | 11091-11157 | Two SU forms exist (Page 13 top and Page 14 bottom) |

**Status:** Documented in `attribution.csv` QA_Notes and `planning/follow-up-actions.md`. Flagged in joined CSV files and error report.

---

## Output File Structure

### Joined CSV Columns

```text
GIS_SU          - Survey Unit ID from GeoJSON
GIS_SU_Date     - Date from GeoJSON (if available, converted to ISO format)
GIS_SU_Team     - Team derived from SUID prefix
SU              - Survey Unit ID (same as GIS_SU)
Date            - Date from attribution.csv
Team            - Team from attribution.csv
Leader          - Team leader from attribution.csv
Walkers         - Standardised walker names from attribution.csv
PDA_Operator    - PDA operator from attribution.csv
Paper_Recorder  - Paper recorder from attribution.csv
Data_Editor     - Data editor from attribution.csv
GPS_Operator    - GPS operator from attribution.csv
Photographer    - Photographer from attribution.csv
Diary_Author    - Diary author from attribution.csv
DPF_Author      - Daily Progress Form author from attribution.csv
XLS_Source      - Excel source file from attribution.csv
PDF_Source      - PDF source file from attribution.csv
Extraction_Notes - Extraction notes from attribution.csv
QA_Notes        - Quality assurance notes from attribution.csv
Flag            - Error flag(s), pipe-separated if multiple
```

### Error Report Columns

```text
Flag              - Error type (NO_MATCH, LEADER_MISMATCH, etc.)
Region            - KAZ or YAM
GIS_SU            - Survey Unit ID from GeoJSON
GIS_SU_Date       - Date from GeoJSON
GIS_SU_Team       - Team derived from SUID
Attribution_Date  - Date from attribution.csv
Attribution_Team  - Team from attribution.csv
Attribution_Leader - Leader from attribution.csv
Attribution_Range - Start-End unit range from attribution.csv
Explanation       - Human-readable explanation of the error
```

---

## Team Derivation Logic

Teams are derived from the first digit of the 5-digit Survey Unit ID (SUID):

**Kazanlak:**

- 1xxxx = Team A
- 2xxxx = Team B
- 3xxxx = Team C
- 4xxxx = Team D
- 5xxxx = Team E

**Yambol/Elhovo:**

- 6xxxx = Team A
- 7xxxx = Team B
- 8xxxx = Team C

---

## Leader Initials Mapping

The following mappings were used to convert GeoJSON leader initials to canonical names for cross-validation:

| GeoJSON Initials | Canonical Name |
|------------------|----------------|
| AS | Adela Sobotkova |
| BW | Bara Weissová |
| Elena | Elena Bozhinova |
| GM | Georgi Mihailov |
| GN | Georgi Nekhrizov |
| JD | Yulia Dimitrova |
| JTs | Julia Tzvetkova |
| NK | Nadezhda Kecheva |
| PJ | Petra Janouchová |
| Petra | Petra Tušlová |
| SAR | Shawn Ross |

**Note:** The high number of LEADER_MISMATCH errors (203) suggests that either:

1. Some initials may have been used by multiple people in different contexts
2. Leadership assignments in GeoJSON may not always reflect the official team leader recorded in summaries
3. There may be systematic differences between how leaders were recorded in different data sources

---

## Recommended Actions

### High Priority

1. **Review LEADER_MISMATCH patterns** — The 203 mismatches follow clear patterns (PJ→Petra Tušlová, BW→Cecilia Choi). Determine if these represent:
   - GeoJSON recording errors
   - Attribution.csv errors
   - Context-dependent initials usage

2. **Review DUPLICATE_GIS_SU** — The 9 GeoJSON duplicate SUIDs need GIS investigation to determine correct polygon assignment.

### Medium Priority

3. **Review ORPHAN_ATTRIBUTION** — 4 attribution ranges (61 units total) have no GeoJSON polygons. Determine if polygons need to be created or attribution data corrected.

4. **Resolve DUPLICATE_UNITS** — Unit 61549 appears in two attribution ranges. Project-level decision needed.

### Lower Priority

5. **Review NO_MATCH units** — Most are documented field gaps, but 282 units should be cross-referenced against `planning/follow-up-actions.md` to confirm.

---

## QA Verification

The following checks were performed on 5 December 2025 to verify output integrity.

### Row Count Verification

| File | Expected | Actual | Status |
|------|----------|--------|--------|
| `kaz-attribution-joined.csv` | 7,707 (GeoJSON features) | 7,707 | ✓ Pass |
| `yam-attribution-joined.csv` | 4,772 (GeoJSON features) | 4,772 | ✓ Pass |
| `join-error-report.csv` | 502 (per header) | 502 | ✓ Pass |

### Flag Count Cross-Reference

| Flag Type | Error Report | Joined CSVs | Status |
|-----------|--------------|-------------|--------|
| LEADER_MISMATCH | 203 | 203 | ✓ Match |
| NO_MATCH | 282 (163 Kaz + 119 Yam) | 282 | ✓ Match |
| DUPLICATE_UNITS | 4 (2 Kaz + 2 Yam) | 4 | ✓ Match |
| DUPLICATE_GIS_SU | 9 unique SUIDs | 23 rows | ✓ Expected difference |
| ORPHAN_ATTRIBUTION | 4 | N/A | ✓ No GeoJSON row to flag |

**Note on DUPLICATE_GIS_SU:** The error report lists each duplicate SUID once (9 entries), while the joined CSVs flag every occurrence of those SUIDs (23 rows total). This is correct behaviour.

### Spot Check Verification

Six random units from different teams were verified against `attribution.csv`:

| Unit | Team | Date Match | Team Match | Leader Match | Status |
|------|------|------------|------------|--------------|--------|
| 10050 | Kaz A | ✓ | ✓ | ✓ | Pass |
| 21000 | Kaz B | ✓ | ✓ | ✓ | Pass |
| 30500 | Kaz C | ✓ | ✓ | ✓ | Pass |
| 40200 | Kaz D | ✓ | ✓ | ✓ | Pass |
| 61400 | Yam A | ✓ | ✓ | ✓ | Pass |
| 70500 | Yam B | ✓ | ✓ | ✓ | Pass |

### Same-Day Duplicate Verification

| Unit | Flag Present | Error Report Entry | Status |
|------|--------------|-------------------|--------|
| 40100 | ✓ DUPLICATE_UNITS | ✓ Present | Pass |
| 11142 | ✓ DUPLICATE_UNITS | ✓ Present | Pass |

**QA Result:** All checks passed. Output files are ready for handover.

---

## Script Information

**Script location:** `scripts/join-geojson-attribution.py`

**Features:**

- Reusable Python script with comprehensive documentation
- Detects 7 error types with detailed explanations
- Cross-validates dates, teams, and leaders
- Produces both joined CSVs and error report
- Handles edge cases (empty ranges, duplicates, missing data)

**To re-run:**

```bash
python scripts/join-geojson-attribution.py
```

---

## Related Documentation

- `planning/follow-up-actions.md` — Documents known data issues, gaps, and pending actions
- `outputs/attribution.csv` — Source attribution data with QA notes
- `outputs/name-mapping.csv` — Name disambiguation mappings
- `outputs/qa-corrections-manifest-comprehensive.json` — Record of all QA corrections applied

---

## Contact

For questions about this report or the join process, contact Shawn Ross.

For GIS-related issues (DUPLICATE_GIS_SU, polygon questions), GIS expertise may be required.
