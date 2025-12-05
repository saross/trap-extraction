#!/usr/bin/env python3
"""
Join GeoJSON Survey Units with Walker Attribution Data.

This script joins GeoJSON survey unit polygon files with walker attribution data
from attribution.csv, producing combined CSV files with error flagging and a
detailed error report.

Purpose:
    Match each GeoJSON survey unit (by SUID) to the corresponding attribution
    record (by Start_Unit - End_Unit range), combining spatial data with walker
    information for Archaeological Knowledge Base (AKB) submission.

Inputs:
    - inputs/kaz-survey-units-reproj-w-uuids.geojson: Kazanlak survey unit polygons
    - inputs/yam-survey-units-reproj-w-uuids.geojson: Yambol/Elhovo survey unit polygons
    - outputs/attribution.csv: Walker attribution data with unit ranges
    - outputs/name-mapping.csv: Name mappings for leader cross-validation

Outputs:
    - outputs/kaz-attribution-joined.csv: Kazanlak joined data with Flag column
    - outputs/yam-attribution-joined.csv: Yambol joined data with Flag column
    - outputs/join-error-report.csv: Detailed error log with explanations

Error Flags:
    - NO_MATCH: GeoJSON unit not in any attribution range
    - DATE_MISMATCH: GeoJSON SU_Date does not match attribution Date
    - TEAM_MISMATCH: Derived team does not match attribution Team
    - LEADER_MISMATCH: GeoJSON Leader does not match attribution Leader
    - DUPLICATE_UNITS: Unit falls in multiple attribution ranges
    - DUPLICATE_GIS_SU: Same SUID appears multiple times in GeoJSON (GIS data issue)
    - ORPHAN_ATTRIBUTION: Attribution range with no GeoJSON polygons

Usage:
    python scripts/join-geojson-attribution.py

Author: TRAP Data Extraction Project
Date: December 2025
"""

import csv
import json
from pathlib import Path
from typing import Optional


# =============================================================================
# CONFIGURATION
# =============================================================================

# Base directory (project root)
BASE_DIR = Path(__file__).parent.parent

# Input file paths
KAZ_GEOJSON_PATH = BASE_DIR / "inputs" / "kaz-survey-units-reproj-w-uuids.geojson"
YAM_GEOJSON_PATH = BASE_DIR / "inputs" / "yam-survey-units-reproj-w-uuids.geojson"
ATTRIBUTION_CSV_PATH = BASE_DIR / "outputs" / "attribution.csv"
NAME_MAPPING_PATH = BASE_DIR / "outputs" / "name-mapping.csv"

# Output file paths
KAZ_OUTPUT_PATH = BASE_DIR / "outputs" / "kaz-attribution-joined.csv"
YAM_OUTPUT_PATH = BASE_DIR / "outputs" / "yam-attribution-joined.csv"
ERROR_REPORT_PATH = BASE_DIR / "outputs" / "join-error-report.csv"

# Output CSV columns (in order)
OUTPUT_COLUMNS = [
    "GIS_SU",
    "GIS_SU_Date",
    "GIS_SU_Team",
    "SU",
    "Date",
    "Team",
    "Leader",
    "Walkers",
    "PDA_Operator",
    "Paper_Recorder",
    "Data_Editor",
    "GPS_Operator",
    "Photographer",
    "Diary_Author",
    "DPF_Author",
    "XLS_Source",
    "PDF_Source",
    "Extraction_Notes",
    "QA_Notes",
    "Flag",
]

# Error report columns
ERROR_COLUMNS = [
    "Flag",
    "Region",
    "GIS_SU",
    "GIS_SU_Date",
    "GIS_SU_Team",
    "Attribution_Date",
    "Attribution_Team",
    "Attribution_Leader",
    "Attribution_Range",
    "Explanation",
]


# =============================================================================
# DATA LOADING FUNCTIONS
# =============================================================================


def load_geojson(filepath: Path) -> list[dict]:
    """
    Load GeoJSON file and return list of feature properties.

    Args:
        filepath: Path to GeoJSON file.

    Returns:
        List of dictionaries, each containing the properties of a feature.
        Includes SUID, SU_Date, Leader, and other attributes.
    """
    print(f"Loading GeoJSON: {filepath.name}")

    with open(filepath, "r", encoding="utf-8") as f:
        data = json.load(f)

    # Extract properties from each feature
    features = []
    for feature in data["features"]:
        props = feature["properties"].copy()
        features.append(props)

    print(f"  Loaded {len(features)} features")
    return features


def load_attribution_csv(filepath: Path) -> list[dict]:
    """
    Load attribution CSV and return list of records with valid unit ranges.

    Filters out records with empty Start Unit or End Unit fields (non-survey days).

    Args:
        filepath: Path to attribution CSV file.

    Returns:
        List of dictionaries, each representing an attribution record.
        Only includes records with valid (non-empty) unit ranges.
    """
    print(f"Loading attribution CSV: {filepath.name}")

    with open(filepath, "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        all_rows = list(reader)

    # Filter to records with valid unit ranges
    valid_rows = [
        row for row in all_rows if row["Start Unit"].strip() and row["End Unit"].strip()
    ]

    print(f"  Loaded {len(valid_rows)} records with unit ranges")
    print(f"  (Filtered out {len(all_rows) - len(valid_rows)} records without unit ranges)")

    return valid_rows


def load_name_mapping(filepath: Path) -> dict[str, str]:
    """
    Load name mapping CSV and build lookup from extracted names to canonical names.

    The mapping file contains columns: extracted_name, corrected_name, canonical_name, status
    We use canonical_name as the target for mapping.

    Args:
        filepath: Path to name-mapping CSV file.

    Returns:
        Dictionary mapping extracted names (and initials) to canonical names.
        Only includes mappings where canonical_name is populated.
    """
    print(f"Loading name mapping: {filepath.name}")

    mapping = {}

    with open(filepath, "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            extracted = row["extracted_name"].strip()
            canonical = row["canonical_name"].strip()

            # Only add mapping if canonical name exists
            if extracted and canonical:
                mapping[extracted] = canonical

    print(f"  Loaded {len(mapping)} name mappings")
    return mapping


def find_duplicate_gis_suids(features: list[dict], region: str) -> tuple[list[dict], set[int]]:
    """
    Find SUIDs that appear multiple times in the GeoJSON features.

    This is a GIS data quality issue where the same survey unit number
    has been assigned to multiple polygons.

    Args:
        features: List of GeoJSON feature properties.
        region: Region identifier ('kaz' or 'yam').

    Returns:
        Tuple of (error_records, duplicate_suids):
        - error_records: List of error report records for each duplicate
        - duplicate_suids: Set of SUIDs that have duplicates (for flagging)
    """
    from collections import Counter

    # Count occurrences of each SUID
    suid_counts = Counter(f.get("SUID") for f in features)

    # Find duplicates (count > 1)
    duplicates = {suid: count for suid, count in suid_counts.items() if count > 1}

    if duplicates:
        print(f"  Found {len(duplicates)} duplicate SUIDs in GeoJSON:")
        for suid, count in sorted(duplicates.items()):
            print(f"    SUID {suid}: {count} occurrences")

    # Create error records for each duplicate
    error_records = []
    for suid, count in duplicates.items():
        # Derive team from SUID for reporting
        first_digit = str(suid)[0] if suid else "?"
        if region == "kaz":
            team_map = {"1": "A", "2": "B", "3": "C", "4": "D", "5": "E"}
        else:
            team_map = {"6": "A", "7": "B", "8": "C"}
        gis_team = team_map.get(first_digit, "?")

        error_record = {
            "Flag": "DUPLICATE_GIS_SU",
            "Region": region.upper(),
            "GIS_SU": suid,
            "GIS_SU_Date": "",
            "GIS_SU_Team": gis_team,
            "Attribution_Date": "",
            "Attribution_Team": "",
            "Attribution_Leader": "",
            "Attribution_Range": "",
            "Explanation": (
                f"GIS data issue: SUID {suid} appears {count} times in GeoJSON. "
                f"Same unit number assigned to multiple polygons."
            ),
        }
        error_records.append(error_record)

    return error_records, set(duplicates.keys())


# =============================================================================
# TEAM DERIVATION AND UNIT RANGE INDEX
# =============================================================================


def derive_team_from_suid(suid: int, region: str) -> str:
    """
    Derive team letter from Survey Unit ID (SUID) prefix.

    Team assignments are based on the first digit of the 5-digit SUID:
    - Kazanlak: 1xxxx=A, 2xxxx=B, 3xxxx=C, 4xxxx=D, 5xxxx=E
    - Yambol:   6xxxx=A, 7xxxx=B, 8xxxx=C

    Args:
        suid: Survey Unit ID (integer).
        region: Region identifier ("kaz" or "yam").

    Returns:
        Team letter (A, B, C, D, or E), or "?" if unknown.
    """
    # Get the first digit of the SUID
    first_digit = str(suid)[0]

    if region == "kaz":
        # Kazanlak team mapping
        team_map = {"1": "A", "2": "B", "3": "C", "4": "D", "5": "E"}
    else:
        # Yambol/Elhovo team mapping
        team_map = {"6": "A", "7": "B", "8": "C"}

    return team_map.get(first_digit, "?")


def build_unit_range_index(
    attribution_rows: list[dict], region: str
) -> dict[int, list[dict]]:
    """
    Build an index mapping each unit number to its attribution row(s).

    This pre-computes which attribution row(s) each possible unit number
    belongs to, enabling O(1) lookup during matching. Some units (like 61549)
    may appear in multiple ranges due to field recording errors.

    Args:
        attribution_rows: List of attribution records with Start Unit and End Unit.
        region: Region identifier ("kaz" or "yam") to filter relevant rows.

    Returns:
        Dictionary mapping unit numbers (int) to lists of attribution rows.
        Most units map to a single row, but duplicates map to multiple.
    """
    print(f"Building unit range index for {region}...")

    # Define region boundaries based on SUID prefix
    if region == "kaz":
        min_unit, max_unit = 10000, 59999
    else:
        min_unit, max_unit = 60000, 89999

    # Build the index
    index: dict[int, list[dict]] = {}

    for row in attribution_rows:
        start = int(row["Start Unit"])
        end = int(row["End Unit"])

        # Skip rows outside this region's range
        if start < min_unit or start > max_unit:
            continue

        # Add each unit in the range to the index
        for unit in range(start, end + 1):
            if unit not in index:
                index[unit] = []
            index[unit].append(row)

    # Count duplicates for reporting
    duplicates = {k: v for k, v in index.items() if len(v) > 1}
    if duplicates:
        print(f"  Found {len(duplicates)} unit(s) in multiple ranges:")
        for unit, rows in duplicates.items():
            dates = [r["Date"] for r in rows]
            print(f"    Unit {unit}: appears on {', '.join(dates)}")

    print(f"  Indexed {len(index)} unique unit numbers")
    return index


# =============================================================================
# MATCHING AND CROSS-VALIDATION
# =============================================================================


def convert_gis_date(gis_date: Optional[int | str]) -> Optional[str]:
    """
    Convert GeoJSON date format (YYYYMMDD integer) to ISO format (YYYY-MM-DD).

    Args:
        gis_date: Date in YYYYMMDD format (integer or string), or None.

    Returns:
        Date in YYYY-MM-DD format, or None if input is None/empty.
    """
    if gis_date is None or gis_date == "":
        return None

    # Convert to string if integer
    date_str = str(gis_date)

    # Parse YYYYMMDD format
    if len(date_str) == 8 and date_str.isdigit():
        year = date_str[:4]
        month = date_str[4:6]
        day = date_str[6:8]
        return f"{year}-{month}-{day}"

    return None


def validate_match(
    gis_feature: dict,
    attr_row: dict,
    name_mapping: dict[str, str],
    gis_team: str,
) -> list[str]:
    """
    Cross-validate GeoJSON fields against attribution row.

    Performs three checks:
    1. Date match: If GeoJSON has SU_Date, compare to attribution Date
    2. Team match: Compare derived team (from SUID) to attribution Team
    3. Leader match: Map GeoJSON Leader initials to canonical name, compare

    Args:
        gis_feature: GeoJSON feature properties dictionary.
        attr_row: Attribution record dictionary.
        name_mapping: Dictionary mapping initials/names to canonical names.
        gis_team: Team letter derived from SUID.

    Returns:
        List of validation flags (e.g., ['DATE_MISMATCH', 'LEADER_MISMATCH']).
        Empty list if all validations pass.
    """
    flags = []

    # ---------------------------------------------------------------------
    # 1. Date validation (only if GeoJSON has a date)
    # ---------------------------------------------------------------------
    gis_date_raw = gis_feature.get("SU_Date")
    gis_date_iso = convert_gis_date(gis_date_raw)
    attr_date = attr_row.get("Date", "").strip()

    if gis_date_iso and attr_date:
        if gis_date_iso != attr_date:
            flags.append("DATE_MISMATCH")

    # ---------------------------------------------------------------------
    # 2. Team validation
    # ---------------------------------------------------------------------
    attr_team = attr_row.get("Team", "").strip()

    if gis_team and attr_team:
        if gis_team != attr_team:
            flags.append("TEAM_MISMATCH")

    # ---------------------------------------------------------------------
    # 3. Leader validation (only if GeoJSON has a leader)
    # ---------------------------------------------------------------------
    gis_leader_raw = gis_feature.get("Leader")
    attr_leader = attr_row.get("Leader", "").strip()

    if gis_leader_raw and attr_leader:
        # Map GeoJSON leader initials to canonical name
        gis_leader_canonical = name_mapping.get(gis_leader_raw, gis_leader_raw)

        # Check if the mapped name appears in the attribution leader field
        # (Attribution may have multiple leaders separated by ' | ')
        attr_leaders = [l.strip() for l in attr_leader.split("|")]

        if gis_leader_canonical not in attr_leaders:
            flags.append("LEADER_MISMATCH")

    return flags


def match_unit_to_attribution(
    suid: int, unit_index: dict[int, list[dict]]
) -> tuple[list[dict], list[str]]:
    """
    Find attribution row(s) for a given Survey Unit ID.

    Args:
        suid: Survey Unit ID to look up.
        unit_index: Pre-built index mapping unit numbers to attribution rows.

    Returns:
        Tuple of (matching_rows, flags):
        - matching_rows: List of attribution rows that contain this unit
        - flags: List containing 'NO_MATCH' if no match, 'DUPLICATE_UNITS' if
                 multiple matches, or empty list if exactly one match
    """
    matching_rows = unit_index.get(suid, [])
    flags = []

    if len(matching_rows) == 0:
        flags.append("NO_MATCH")
    elif len(matching_rows) > 1:
        flags.append("DUPLICATE_UNITS")

    return matching_rows, flags


# =============================================================================
# REGION PROCESSING
# =============================================================================


def create_joined_record(
    gis_feature: dict,
    attr_row: Optional[dict],
    gis_team: str,
    flags: list[str],
) -> dict:
    """
    Create a joined output record combining GeoJSON and attribution data.

    Args:
        gis_feature: GeoJSON feature properties.
        attr_row: Attribution record (may be None if NO_MATCH).
        gis_team: Team letter derived from SUID.
        flags: List of error flags.

    Returns:
        Dictionary with all output columns populated.
    """
    suid = gis_feature.get("SUID")
    gis_date_iso = convert_gis_date(gis_feature.get("SU_Date"))

    record = {
        "GIS_SU": suid,
        "GIS_SU_Date": gis_date_iso or "",
        "GIS_SU_Team": gis_team,
        "SU": suid,  # Same as GIS_SU for clarity
        "Flag": " | ".join(flags) if flags else "",
    }

    # Add attribution fields if we have a match
    if attr_row:
        record["Date"] = attr_row.get("Date", "")
        record["Team"] = attr_row.get("Team", "")
        record["Leader"] = attr_row.get("Leader", "")
        record["Walkers"] = attr_row.get("Walkers_Standardised", "")
        record["PDA_Operator"] = attr_row.get("PDA_Operator", "")
        record["Paper_Recorder"] = attr_row.get("Paper_Recorder", "")
        record["Data_Editor"] = attr_row.get("Data_Editor", "")
        record["GPS_Operator"] = attr_row.get("GPS_Operator", "")
        record["Photographer"] = attr_row.get("Photographer", "")
        record["Diary_Author"] = attr_row.get("Diary_Author", "")
        record["DPF_Author"] = attr_row.get("DPF_Author", "")
        record["XLS_Source"] = attr_row.get("XLS_Source", "")
        record["PDF_Source"] = attr_row.get("PDF_Source", "")
        record["Extraction_Notes"] = attr_row.get("Extraction_Notes", "")
        record["QA_Notes"] = attr_row.get("QA_Notes", "")
    else:
        # No match - leave attribution fields empty
        for col in OUTPUT_COLUMNS[4:-1]:  # Skip GIS_*, SU, and Flag
            if col not in record:
                record[col] = ""

    return record


def create_error_record(
    flag: str,
    region: str,
    gis_feature: Optional[dict],
    attr_row: Optional[dict],
    gis_team: str,
    explanation: str,
) -> dict:
    """
    Create an error report record.

    Args:
        flag: Error flag type (e.g., 'NO_MATCH', 'DATE_MISMATCH').
        region: Region identifier ('kaz' or 'yam').
        gis_feature: GeoJSON feature properties (may be None for ORPHAN).
        attr_row: Attribution record (may be None for NO_MATCH).
        gis_team: Team letter derived from SUID.
        explanation: Human-readable explanation of the error.

    Returns:
        Dictionary with error report columns populated.
    """
    record = {
        "Flag": flag,
        "Region": region.upper(),
        "GIS_SU": gis_feature.get("SUID", "") if gis_feature else "",
        "GIS_SU_Date": convert_gis_date(gis_feature.get("SU_Date")) if gis_feature else "",
        "GIS_SU_Team": gis_team if gis_feature else "",
        "Attribution_Date": attr_row.get("Date", "") if attr_row else "",
        "Attribution_Team": attr_row.get("Team", "") if attr_row else "",
        "Attribution_Leader": attr_row.get("Leader", "") if attr_row else "",
        "Attribution_Range": "",
        "Explanation": explanation,
    }

    # Add attribution range if available
    if attr_row:
        start = attr_row.get("Start Unit", "")
        end = attr_row.get("End Unit", "")
        record["Attribution_Range"] = f"{start}-{end}"

    return record


def process_region(
    geojson_path: Path,
    attribution_rows: list[dict],
    name_mapping: dict[str, str],
    region: str,
) -> tuple[list[dict], list[dict], set[tuple]]:
    """
    Process all survey units for a region (Kazanlak or Yambol).

    For each GeoJSON feature:
    1. Derive team from SUID prefix
    2. Look up attribution row(s) by unit range
    3. Cross-validate dates, teams, and leaders
    4. Create joined record and any error records

    Args:
        geojson_path: Path to GeoJSON file.
        attribution_rows: List of all attribution records.
        name_mapping: Dictionary for leader name lookups.
        region: Region identifier ('kaz' or 'yam').

    Returns:
        Tuple of (joined_records, error_records, matched_ranges):
        - joined_records: List of joined output records
        - error_records: List of error report records
        - matched_ranges: Set of (start, end) tuples for matched attribution rows
    """
    print(f"\nProcessing {region.upper()} region...")

    # Load GeoJSON features
    features = load_geojson(geojson_path)

    # Check for duplicate SUIDs in GeoJSON (GIS data quality issue)
    gis_dup_errors, duplicate_gis_suids = find_duplicate_gis_suids(features, region)

    # Build unit range index for this region
    unit_index = build_unit_range_index(attribution_rows, region)

    joined_records = []
    error_records = []
    matched_ranges: set[tuple] = set()

    # Add GIS duplicate errors to error records
    error_records.extend(gis_dup_errors)

    # Track statistics
    stats = {
        "total": 0,
        "matched": 0,
        "no_match": 0,
        "duplicate": 0,
        "duplicate_gis_su": len(duplicate_gis_suids),
        "date_mismatch": 0,
        "team_mismatch": 0,
        "leader_mismatch": 0,
    }

    # Process each GeoJSON feature
    for feature in features:
        stats["total"] += 1
        suid = feature.get("SUID")

        if suid is None:
            print(f"  WARNING: Feature without SUID, skipping")
            continue

        # Derive team from SUID
        gis_team = derive_team_from_suid(suid, region)

        # Look up attribution row(s)
        matching_rows, match_flags = match_unit_to_attribution(suid, unit_index)

        # Initialise flags with match flags (NO_MATCH or DUPLICATE_UNITS)
        all_flags = match_flags.copy()

        # Add DUPLICATE_GIS_SU flag if this SUID appears multiple times in GeoJSON
        if suid in duplicate_gis_suids:
            all_flags.append("DUPLICATE_GIS_SU")

        # Handle different match scenarios
        if len(matching_rows) == 0:
            # NO_MATCH case
            stats["no_match"] += 1

            # Create joined record with empty attribution fields
            joined_record = create_joined_record(feature, None, gis_team, all_flags)
            joined_records.append(joined_record)

            # Create error record
            explanation = f"Unit {suid} not found in any attribution range"
            error_record = create_error_record(
                "NO_MATCH", region, feature, None, gis_team, explanation
            )
            error_records.append(error_record)

        elif len(matching_rows) == 1:
            # Single match - perform cross-validation
            attr_row = matching_rows[0]
            stats["matched"] += 1

            # Track that this attribution range was matched
            matched_ranges.add((attr_row["Start Unit"], attr_row["End Unit"]))

            # Cross-validate
            validation_flags = validate_match(feature, attr_row, name_mapping, gis_team)
            all_flags.extend(validation_flags)

            # Track validation flag statistics
            if "DATE_MISMATCH" in validation_flags:
                stats["date_mismatch"] += 1
            if "TEAM_MISMATCH" in validation_flags:
                stats["team_mismatch"] += 1
            if "LEADER_MISMATCH" in validation_flags:
                stats["leader_mismatch"] += 1

            # Create joined record
            joined_record = create_joined_record(feature, attr_row, gis_team, all_flags)
            joined_records.append(joined_record)

            # Create error records for any validation failures
            for flag in validation_flags:
                if flag == "DATE_MISMATCH":
                    gis_date = convert_gis_date(feature.get("SU_Date"))
                    attr_date = attr_row.get("Date", "")
                    explanation = f"GeoJSON date {gis_date} != attribution date {attr_date}"
                elif flag == "TEAM_MISMATCH":
                    attr_team = attr_row.get("Team", "")
                    explanation = f"Derived team {gis_team} != attribution team {attr_team}"
                elif flag == "LEADER_MISMATCH":
                    gis_leader = feature.get("Leader", "")
                    attr_leader = attr_row.get("Leader", "")
                    explanation = f"GeoJSON leader '{gis_leader}' != attribution leader '{attr_leader}'"
                else:
                    explanation = f"Validation error: {flag}"

                error_record = create_error_record(
                    flag, region, feature, attr_row, gis_team, explanation
                )
                error_records.append(error_record)

        else:
            # Multiple matches (DUPLICATE_UNITS)
            stats["duplicate"] += 1

            # Use first match for the joined record (arbitrary choice)
            attr_row = matching_rows[0]

            # Track all matched ranges
            for row in matching_rows:
                matched_ranges.add((row["Start Unit"], row["End Unit"]))

            # Still perform validation against first match
            validation_flags = validate_match(feature, attr_row, name_mapping, gis_team)
            all_flags.extend(validation_flags)

            # Create joined record
            joined_record = create_joined_record(feature, attr_row, gis_team, all_flags)
            joined_records.append(joined_record)

            # Create error record for duplicate
            date_list = ", ".join(r["Date"] for r in matching_rows)
            range_list = ", ".join(
                f"{r['Start Unit']}-{r['End Unit']}" for r in matching_rows
            )
            explanation = (
                f"Unit {suid} appears in {len(matching_rows)} attribution ranges: "
                f"dates [{date_list}], ranges [{range_list}]"
            )
            error_record = create_error_record(
                "DUPLICATE_UNITS", region, feature, attr_row, gis_team, explanation
            )
            error_records.append(error_record)

    # Print statistics
    print(f"\n  {region.upper()} Statistics:")
    print(f"    Total features:     {stats['total']}")
    print(f"    Matched:            {stats['matched']}")
    print(f"    No match:           {stats['no_match']}")
    print(f"    Duplicate units:    {stats['duplicate']}")
    print(f"    Duplicate GIS SU:   {stats['duplicate_gis_su']}")
    print(f"    Date mismatches:    {stats['date_mismatch']}")
    print(f"    Team mismatches:    {stats['team_mismatch']}")
    print(f"    Leader mismatches:  {stats['leader_mismatch']}")

    return joined_records, error_records, matched_ranges


def find_orphan_attributions(
    attribution_rows: list[dict],
    matched_ranges: set[tuple],
    region: str,
) -> list[dict]:
    """
    Find attribution rows where no GeoJSON units matched.

    These are "orphan" attribution records - they have unit ranges defined
    but no corresponding GeoJSON polygons exist for those units.

    Args:
        attribution_rows: List of all attribution records.
        matched_ranges: Set of (start, end) tuples that were matched.
        region: Region identifier ('kaz' or 'yam').

    Returns:
        List of error records for orphan attribution rows.
    """
    print(f"\n  Checking for orphan attribution ranges in {region.upper()}...")

    # Define region boundaries
    if region == "kaz":
        min_unit, max_unit = 10000, 59999
    else:
        min_unit, max_unit = 60000, 89999

    orphan_errors = []

    for row in attribution_rows:
        start = row.get("Start Unit", "").strip()
        end = row.get("End Unit", "").strip()

        # Skip empty ranges
        if not start or not end:
            continue

        start_int = int(start)
        end_int = int(end)

        # Skip rows outside this region
        if start_int < min_unit or start_int > max_unit:
            continue

        # Check if this range was matched
        if (start, end) not in matched_ranges:
            explanation = (
                f"Attribution range {start}-{end} ({row['Date']} Team {row['Team']}) "
                f"has no matching GeoJSON polygons"
            )
            error_record = create_error_record(
                "ORPHAN_ATTRIBUTION",
                region,
                None,  # No GeoJSON feature
                row,
                "",  # No GIS team
                explanation,
            )
            orphan_errors.append(error_record)

    print(f"    Found {len(orphan_errors)} orphan attribution ranges")
    return orphan_errors


# =============================================================================
# OUTPUT WRITING
# =============================================================================


def write_joined_csv(records: list[dict], output_path: Path) -> None:
    """
    Write joined records to CSV file.

    Args:
        records: List of joined record dictionaries.
        output_path: Path to output CSV file.
    """
    print(f"\nWriting joined CSV: {output_path.name}")

    with open(output_path, "w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=OUTPUT_COLUMNS)
        writer.writeheader()
        writer.writerows(records)

    print(f"  Wrote {len(records)} records")


def write_error_report(errors: list[dict], output_path: Path) -> None:
    """
    Write error report to CSV file.

    Args:
        errors: List of error record dictionaries.
        output_path: Path to output CSV file.
    """
    print(f"\nWriting error report: {output_path.name}")

    # Sort errors by flag type, then region, then GIS_SU
    sorted_errors = sorted(
        errors,
        key=lambda e: (e["Flag"], e["Region"], str(e.get("GIS_SU", ""))),
    )

    with open(output_path, "w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=ERROR_COLUMNS)
        writer.writeheader()
        writer.writerows(sorted_errors)

    print(f"  Wrote {len(errors)} error records")

    # Print summary by flag type
    flag_counts: dict[str, int] = {}
    for error in errors:
        flag = error["Flag"]
        flag_counts[flag] = flag_counts.get(flag, 0) + 1

    print("\n  Error summary by type:")
    for flag in sorted(flag_counts.keys()):
        print(f"    {flag}: {flag_counts[flag]}")


# =============================================================================
# MAIN ENTRY POINT
# =============================================================================


def main() -> None:
    """
    Main entry point for the join script.

    Orchestrates the full processing pipeline:
    1. Load all input files
    2. Process Kazanlak region
    3. Process Yambol region
    4. Find orphan attribution ranges
    5. Write output files
    6. Print summary statistics
    """
    print("=" * 70)
    print("GeoJSON to Attribution CSV Join Script")
    print("=" * 70)

    # -------------------------------------------------------------------------
    # Load input data
    # -------------------------------------------------------------------------
    print("\n" + "-" * 70)
    print("LOADING INPUT DATA")
    print("-" * 70)

    attribution_rows = load_attribution_csv(ATTRIBUTION_CSV_PATH)
    name_mapping = load_name_mapping(NAME_MAPPING_PATH)

    # -------------------------------------------------------------------------
    # Process Kazanlak region
    # -------------------------------------------------------------------------
    print("\n" + "-" * 70)
    print("PROCESSING KAZANLAK")
    print("-" * 70)

    kaz_joined, kaz_errors, kaz_matched = process_region(
        KAZ_GEOJSON_PATH, attribution_rows, name_mapping, "kaz"
    )

    # Find orphan attributions for Kazanlak
    kaz_orphans = find_orphan_attributions(attribution_rows, kaz_matched, "kaz")
    kaz_errors.extend(kaz_orphans)

    # -------------------------------------------------------------------------
    # Process Yambol region
    # -------------------------------------------------------------------------
    print("\n" + "-" * 70)
    print("PROCESSING YAMBOL")
    print("-" * 70)

    yam_joined, yam_errors, yam_matched = process_region(
        YAM_GEOJSON_PATH, attribution_rows, name_mapping, "yam"
    )

    # Find orphan attributions for Yambol
    yam_orphans = find_orphan_attributions(attribution_rows, yam_matched, "yam")
    yam_errors.extend(yam_orphans)

    # -------------------------------------------------------------------------
    # Write output files
    # -------------------------------------------------------------------------
    print("\n" + "-" * 70)
    print("WRITING OUTPUT FILES")
    print("-" * 70)

    write_joined_csv(kaz_joined, KAZ_OUTPUT_PATH)
    write_joined_csv(yam_joined, YAM_OUTPUT_PATH)

    # Combine all errors for single report
    all_errors = kaz_errors + yam_errors
    write_error_report(all_errors, ERROR_REPORT_PATH)

    # -------------------------------------------------------------------------
    # Final summary
    # -------------------------------------------------------------------------
    print("\n" + "=" * 70)
    print("PROCESSING COMPLETE")
    print("=" * 70)
    print(f"\nOutput files created:")
    print(f"  - {KAZ_OUTPUT_PATH}")
    print(f"  - {YAM_OUTPUT_PATH}")
    print(f"  - {ERROR_REPORT_PATH}")
    print(f"\nTotal joined records: {len(kaz_joined) + len(yam_joined)}")
    print(f"Total error records:  {len(all_errors)}")
    print("\n" + "=" * 70)


if __name__ == "__main__":
    main()
