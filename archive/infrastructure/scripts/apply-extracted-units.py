#!/usr/bin/env python3
"""
Apply Extracted Survey Units to Attribution CSV

This script updates the main attribution.csv file with survey unit numbers
that were successfully extracted from PDFs, Bulgarian diaries, and Excel files.

It reads the extraction results from missing-survey-units-extracted.csv and
populates the Start Unit and End Unit columns in attribution.csv for all
records with status "Found".

Input files:
    - outputs/missing-survey-units-extracted.csv (extraction results)
    - outputs/attribution.csv (main attribution data)

Output files:
    - outputs/attribution.csv (updated with extracted units)
    - outputs/attribution-pre-update-backup.csv (backup of original)

Author: Claude Code
Date: 2025-11-24
"""

import csv
from pathlib import Path
from datetime import datetime
from shutil import copy2


def load_extracted_units(csv_path: Path) -> dict:
    """
    Load successfully extracted survey units from CSV.

    Args:
        csv_path: Path to missing-survey-units-extracted.csv

    Returns:
        Dictionary mapping (Date, Team) tuples to (Start Unit, End Unit) tuples
    """
    extracted = {}

    with open(csv_path, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            if row['Status'] == 'Found':
                key = (row['Date'], row['Team'])
                value = (row['Start Unit'], row['End Unit'])
                extracted[key] = value

    return extracted


def update_attribution_csv(attribution_path: Path, extracted_units: dict) -> tuple:
    """
    Update attribution.csv with extracted survey units.

    Args:
        attribution_path: Path to attribution.csv
        extracted_units: Dictionary of extracted units from load_extracted_units()

    Returns:
        Tuple of (updated_count, rows_updated)
    """
    # Read all rows from attribution.csv
    rows = []
    with open(attribution_path, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        fieldnames = reader.fieldnames

        for row in reader:
            rows.append(row)

    # Update rows with extracted units
    updated_count = 0
    rows_updated = []

    for row in rows:
        key = (row['Date'], row['Team'])

        if key in extracted_units:
            start_unit, end_unit = extracted_units[key]

            # Only update if currently empty or different
            if (not row['Start Unit'] or not row['End Unit'] or
                row['Start Unit'] != start_unit or row['End Unit'] != end_unit):

                row['Start Unit'] = start_unit
                row['End Unit'] = end_unit
                updated_count += 1
                rows_updated.append(f"{key[0]} Team {key[1]}: {start_unit}-{end_unit}")

    # Write updated rows back to CSV
    with open(attribution_path, 'w', encoding='utf-8', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)

    return updated_count, rows_updated


def main():
    """Main execution function."""
    # Set up paths
    base_dir = Path(__file__).parent.parent
    extracted_csv = base_dir / 'outputs' / 'missing-survey-units-extracted.csv'
    attribution_csv = base_dir / 'outputs' / 'attribution.csv'
    backup_csv = base_dir / 'outputs' / 'attribution-pre-update-backup.csv'

    print("Apply Extracted Survey Units to Attribution CSV")
    print("=" * 60)
    print()

    # Create backup
    print(f"Creating backup: {backup_csv.name}")
    copy2(attribution_csv, backup_csv)
    print("✓ Backup created")
    print()

    # Load extracted units
    print(f"Loading extracted units from: {extracted_csv.name}")
    extracted_units = load_extracted_units(extracted_csv)
    print(f"✓ Loaded {len(extracted_units)} successfully extracted records")
    print()

    # Update attribution.csv
    print(f"Updating attribution file: {attribution_csv.name}")
    updated_count, rows_updated = update_attribution_csv(attribution_csv, extracted_units)
    print(f"✓ Updated {updated_count} records")
    print()

    # Display updated records
    if rows_updated:
        print("Updated records:")
        print("-" * 60)
        for record in rows_updated:
            print(f"  • {record}")
        print()

    # Summary
    print("=" * 60)
    print("Summary:")
    print(f"  Total extracted units available: {len(extracted_units)}")
    print(f"  Records updated in attribution.csv: {updated_count}")
    print(f"  Backup saved to: {backup_csv.name}")
    print()
    print("✓ Attribution CSV successfully updated")


if __name__ == '__main__':
    main()
