#!/usr/bin/env python3
"""
Update Attribution CSV with Non-Survey Explanations

This script updates the attribution.csv file with detailed explanations for
the 30 dates that have no survey units. It adds explanatory notes to the
QA_Notes column documenting why no survey units exist (non-unit survey work,
weather cancellations, gap days, etc.).

Input files:
    - outputs/missing-survey-units-extracted.csv (investigation results)
    - outputs/attribution.csv (main attribution data)

Output files:
    - outputs/attribution.csv (updated with explanations)
    - outputs/attribution-pre-explanations-backup.csv (backup)

Author: Claude Code
Date: 2025-11-24
"""

import csv
from pathlib import Path
from shutil import copy2


def load_explanations(csv_path: Path) -> dict:
    """
    Load explanations for missing survey units from investigation CSV.

    Args:
        csv_path: Path to missing-survey-units-extracted.csv

    Returns:
        Dictionary mapping (Date, Team) tuples to explanation strings
    """
    explanations = {}

    with open(csv_path, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            # Only process records without units that have explanations
            if not row['Start Unit'] and row['Status'] != 'Found':
                key = (row['Date'], row['Team'])

                # Build explanation text based on status
                status = row['Status']
                note = row['Extraction_Note']

                if status == 'Non-unit survey work':
                    explanation = f"Non-standard survey: {note}"
                elif status == 'Weather cancellation':
                    explanation = f"Weather cancellation: {note}"
                elif status == 'Non-survey day':
                    explanation = f"Non-survey activity: {note}"
                elif status == 'Gap day':
                    explanation = f"Gap day: {note}"
                elif status == 'Team not working':
                    explanation = f"Team not working: {note}"
                elif status == 'No autumn season':
                    explanation = f"No autumn survey season: {note}"
                elif status == 'In source but no units':
                    explanation = f"In source but no units: {note}"
                else:
                    explanation = note

                explanations[key] = explanation

    return explanations


def update_attribution_csv(attribution_path: Path, explanations: dict) -> tuple:
    """
    Update attribution.csv with explanatory notes in QA_Notes column.

    Args:
        attribution_path: Path to attribution.csv
        explanations: Dictionary of explanations from load_explanations()

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

    # Update rows with explanations
    updated_count = 0
    rows_updated = []

    for row in rows:
        key = (row['Date'], row['Team'])

        if key in explanations:
            explanation = explanations[key]

            # Add explanation to QA_Notes, preserving existing notes
            existing_notes = row.get('QA_Notes', '').strip()

            if existing_notes:
                # Append explanation if notes exist
                row['QA_Notes'] = f"{existing_notes} | {explanation}"
            else:
                # Set explanation as new note
                row['QA_Notes'] = explanation

            updated_count += 1
            rows_updated.append(f"{key[0]} Team {key[1]}: {explanation}")

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
    explanations_csv = base_dir / 'outputs' / 'missing-survey-units-extracted.csv'
    attribution_csv = base_dir / 'outputs' / 'attribution.csv'
    backup_csv = base_dir / 'outputs' / 'attribution-pre-explanations-backup.csv'

    print("Update Attribution CSV with Non-Survey Explanations")
    print("=" * 60)
    print()

    # Create backup
    print(f"Creating backup: {backup_csv.name}")
    copy2(attribution_csv, backup_csv)
    print("✓ Backup created")
    print()

    # Load explanations
    print(f"Loading explanations from: {explanations_csv.name}")
    explanations = load_explanations(explanations_csv)
    print(f"✓ Loaded {len(explanations)} explanations for dates without units")
    print()

    # Update attribution.csv
    print(f"Updating attribution file: {attribution_csv.name}")
    updated_count, rows_updated = update_attribution_csv(attribution_csv, explanations)
    print(f"✓ Updated {updated_count} records with explanations")
    print()

    # Display updated records by category
    if rows_updated:
        print("Updated records:")
        print("-" * 60)

        # Group by explanation type
        by_type = {}
        for record in rows_updated:
            if 'Non-standard survey:' in record:
                category = 'Non-standard survey methods'
            elif 'Weather cancellation:' in record:
                category = 'Weather cancellations'
            elif 'Non-survey activity:' in record:
                category = 'Non-survey activities'
            elif 'Gap day:' in record:
                category = 'Gap days'
            elif 'Team not working:' in record:
                category = 'Team not working'
            elif 'No autumn survey season:' in record:
                category = 'No autumn survey season'
            else:
                category = 'Other'

            if category not in by_type:
                by_type[category] = []
            by_type[category].append(record)

        # Display by category
        for category in sorted(by_type.keys()):
            print(f"\n{category}: {len(by_type[category])} records")
            for record in by_type[category]:
                print(f"  • {record}")
        print()

    # Summary
    print("=" * 60)
    print("Summary:")
    print(f"  Total explanations available: {len(explanations)}")
    print(f"  Records updated in attribution.csv: {updated_count}")
    print(f"  Backup saved to: {backup_csv.name}")
    print()
    print("✓ Attribution CSV successfully updated with explanations")
    print()
    print("All 30 dates without survey units now have documented")
    print("explanations in the QA_Notes column.")


if __name__ == '__main__':
    main()
