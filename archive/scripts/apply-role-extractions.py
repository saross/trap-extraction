#!/usr/bin/env python3
"""
Apply role extractions from consolidated CSV to attribution.csv.

This script reads the consolidated role extractions and applies them to the
attribution.csv file, updating only empty role fields.

Author: Claude Code
Date: 24 November 2025
"""

import csv
from pathlib import Path
from datetime import datetime


# Paths
BASE_PATH = Path('/media/shawn/191c3b96-5fa5-4d0d-8805-0cf05d3d8468/synology/Adela/'
                 'TRAP-WD-2020-04/trap-extraction/outputs')
ATTRIBUTION_FILE = BASE_PATH / 'attribution.csv'
EXTRACTIONS_FILE = BASE_PATH / 'role-extractions-consolidated.csv'
OUTPUT_FILE = BASE_PATH / 'attribution.csv'

# Column mapping: role_type -> attribution.csv column name
ROLE_COLUMNS = {
    'PDA_Operator': 'PDA_Operator',
    'Paper_Recorder': 'Paper_Recorder',
    'Data_Editor': 'Data_Editor',
    'GPS_Operator': 'GPS_Operator',
    'Photographer': 'Photographer',
    'Author': 'Author',
}


def load_extractions(filepath: Path) -> dict:
    """
    Load extractions and group by (date, team).

    Args:
        filepath: Path to consolidated extractions CSV

    Returns:
        Dictionary keyed by (date, team) containing list of role extractions
    """
    extractions = {}

    with open(filepath, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            key = (row['date'], row['team'])
            if key not in extractions:
                extractions[key] = []
            extractions[key].append(row)

    return extractions


def apply_extractions(attribution_path: Path, extractions: dict) -> tuple:
    """
    Apply extractions to attribution.csv.

    Args:
        attribution_path: Path to attribution.csv
        extractions: Dictionary of extractions by (date, team)

    Returns:
        Tuple of (updated_rows, list of updated records, statistics)
    """
    updated_rows = []
    stats = {
        'records_matched': 0,
        'fields_updated': 0,
        'fields_skipped_existing': 0,
        'records_not_found': set(),
        'updates_by_role': {role: 0 for role in ROLE_COLUMNS.keys()},
    }

    # Read all attribution records
    with open(attribution_path, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        fieldnames = reader.fieldnames

        for row in reader:
            date = row['Date']
            team = row['Team']
            key = (date, team)

            if key in extractions:
                stats['records_matched'] += 1
                extraction_list = extractions[key]
                sources_added = []

                for extraction in extraction_list:
                    role_type = extraction['role_type']
                    person_name = extraction['person_name']
                    source_file = extraction['source_file']
                    confidence = extraction['confidence']
                    notes = extraction['notes']

                    if role_type in ROLE_COLUMNS:
                        col_name = ROLE_COLUMNS[role_type]
                        current_value = row.get(col_name, '').strip()

                        # Only update if field is empty
                        if not current_value:
                            row[col_name] = person_name
                            stats['fields_updated'] += 1
                            stats['updates_by_role'][role_type] += 1
                            sources_added.append(
                                f"{role_type}={person_name} ({source_file}, {confidence})"
                            )
                        else:
                            stats['fields_skipped_existing'] += 1

                # Update Extraction_Notes if we made updates
                if sources_added:
                    existing_notes = row.get('Extraction_Notes', '') or ''
                    new_note = f"Role extraction: {'; '.join(sources_added)}"
                    if existing_notes:
                        row['Extraction_Notes'] = f"{existing_notes} | {new_note}"
                    else:
                        row['Extraction_Notes'] = new_note

                    # Update QA_Notes - remove "No role data available" if present
                    qa_notes = row.get('QA_Notes', '') or ''
                    if 'No role data available' in qa_notes:
                        qa_notes = qa_notes.replace('No role data available', '').strip()
                        qa_notes = qa_notes.replace(' | ', ' | ').strip(' |')
                        row['QA_Notes'] = qa_notes if qa_notes else ''

            updated_rows.append(row)

    # Track extraction keys not found in attribution
    extraction_keys = set(extractions.keys())
    attribution_keys = {(row['Date'], row['Team']) for row in updated_rows}
    stats['records_not_found'] = extraction_keys - attribution_keys

    return updated_rows, fieldnames, stats


def write_attribution(filepath: Path, rows: list, fieldnames: list) -> None:
    """
    Write updated attribution data to CSV.

    Args:
        filepath: Output path
        rows: List of row dictionaries
        fieldnames: CSV field names
    """
    with open(filepath, 'w', encoding='utf-8', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)


def main():
    """Main entry point."""
    print("TRAP Role Extraction - Applying Extractions to attribution.csv")
    print(f"Started: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print()

    # Load extractions
    print(f"Loading extractions from: {EXTRACTIONS_FILE.name}")
    extractions = load_extractions(EXTRACTIONS_FILE)
    total_extractions = sum(len(v) for v in extractions.values())
    print(f"  Loaded {total_extractions} extractions for {len(extractions)} (date, team) keys")
    print()

    # Apply extractions
    print(f"Applying extractions to: {ATTRIBUTION_FILE.name}")
    rows, fieldnames, stats = apply_extractions(ATTRIBUTION_FILE, extractions)
    print()

    # Write output
    print(f"Writing updated attribution to: {OUTPUT_FILE.name}")
    write_attribution(OUTPUT_FILE, rows, fieldnames)
    print()

    # Print statistics
    print("=" * 60)
    print("STATISTICS")
    print("=" * 60)
    print(f"Records matched: {stats['records_matched']}")
    print(f"Fields updated: {stats['fields_updated']}")
    print(f"Fields skipped (already populated): {stats['fields_skipped_existing']}")
    print()
    print("Updates by role type:")
    for role, count in sorted(stats['updates_by_role'].items()):
        print(f"  {role}: {count}")
    print()

    if stats['records_not_found']:
        print(f"WARNING: {len(stats['records_not_found'])} extraction keys not found in attribution:")
        for key in sorted(stats['records_not_found'])[:10]:
            print(f"  {key}")
        if len(stats['records_not_found']) > 10:
            print(f"  ... and {len(stats['records_not_found']) - 10} more")

    print()
    print("Done!")


if __name__ == '__main__':
    main()
