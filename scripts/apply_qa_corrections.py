#!/usr/bin/env python3
"""
Apply QA Corrections to Attribution CSV

This script reads pending corrections from the QA corrections manifest
and applies them to the attribution.csv file.

Author: Claude Code (with Shawn Ross)
Created: 2025-12-02
"""

import csv
import json
import sys
from pathlib import Path
from datetime import datetime


def load_manifest(manifest_path: Path) -> dict:
    """Load the corrections manifest."""
    with open(manifest_path, 'r', encoding='utf-8') as f:
        return json.load(f)


def load_csv(csv_path: Path) -> tuple[list[str], list[dict]]:
    """Load CSV file and return headers and rows as list of dicts."""
    with open(csv_path, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        headers = reader.fieldnames
        rows = list(reader)
    return headers, rows


def save_csv(csv_path: Path, headers: list[str], rows: list[dict]):
    """Save rows to CSV file."""
    with open(csv_path, 'w', encoding='utf-8', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=headers)
        writer.writeheader()
        writer.writerows(rows)


def find_record(rows: list[dict], date: str, team: str) -> int:
    """Find index of record matching date and team. Returns -1 if not found."""
    for i, row in enumerate(rows):
        if row['Date'] == date and row['Team'] == team:
            return i
    return -1


def apply_correction(rows: list[dict], correction: dict) -> tuple[bool, str]:
    """
    Apply a single correction to the rows.
    Returns (success, message).
    """
    corr_type = correction['type']
    corr_id = correction['id']
    date = correction.get('date')
    team = correction.get('team')

    if corr_type == 'CORRECTION':
        # Find the record
        idx = find_record(rows, date, team)
        if idx == -1:
            return False, f"{corr_id}: Record not found for {date} Team {team}"

        # Apply field corrections
        fields = correction.get('fields', {})
        for field_name, field_spec in fields.items():
            action = field_spec.get('action')

            # Map field names from manifest to CSV column names
            csv_field = field_name
            if field_name == 'Start_Unit':
                csv_field = 'Start Unit'
            elif field_name == 'End_Unit':
                csv_field = 'End Unit'
            elif field_name == 'Walkers_Transliterated':
                csv_field = 'Walkers_Standardised'

            if action == 'REPLACE' or action == 'SET':
                old_val = rows[idx].get(csv_field, '')
                new_val = field_spec.get('corrected', '')
                rows[idx][csv_field] = new_val
                print(f"  {csv_field}: '{old_val}' -> '{new_val}'")
            elif action == 'REPLACE_IN_STRING':
                find_str = field_spec.get('find', '')
                replace_str = field_spec.get('replace', '')
                old_val = rows[idx].get(csv_field, '')
                new_val = old_val.replace(find_str, replace_str)
                rows[idx][csv_field] = new_val
                print(f"  {csv_field}: replaced '{find_str}' with '{replace_str}'")

        return True, f"{corr_id}: Applied corrections to {date} Team {team}"

    elif corr_type == 'ADD_RECORD':
        # Check if record already exists
        idx = find_record(rows, date, team)
        if idx != -1:
            return False, f"{corr_id}: Record already exists for {date} Team {team}"

        # Create new record with defaults
        new_record = correction.get('new_record', {})
        row = {
            'Date': new_record.get('Date', date),
            'Team': new_record.get('Team', team),
            'Start Unit': new_record.get('Start_Unit', ''),
            'End Unit': new_record.get('End_Unit', ''),
            'Leader': new_record.get('Leader', ''),
            'Walkers_Original': new_record.get('Walkers_Original', ''),
            'Walkers_Standardised': new_record.get('Walkers_Standardised', ''),
            'PDA_Operator': new_record.get('PDA_Operator', ''),
            'Paper_Recorder': new_record.get('Paper_Recorder', ''),
            'Data_Editor': new_record.get('Data_Editor', ''),
            'GPS_Operator': new_record.get('GPS_Operator', ''),
            'Photographer': new_record.get('Photographer', ''),
            'Diary_Author': new_record.get('Diary_Author', ''),
            'DPF_Author': new_record.get('DPF_Author', ''),
            'XLS_Source': new_record.get('XLS_Source', ''),
            'PDF_Source': new_record.get('PDF_Source', ''),
            'Extraction_Notes': new_record.get('Extraction_Notes', f'Added from QA correction {corr_id}'),
            'QA_Notes': new_record.get('QA_Notes', f'QA correction {corr_id}: Record added during QA review')
        }

        # Insert in date order
        insert_idx = len(rows)
        for i, r in enumerate(rows):
            if r['Date'] > date or (r['Date'] == date and r['Team'] > team):
                insert_idx = i
                break
        rows.insert(insert_idx, row)

        return True, f"{corr_id}: Added new record for {date} Team {team}"

    elif corr_type == 'VERIFY_NO_CHANGE':
        return True, f"{corr_id}: Verified - no change needed"

    elif corr_type == 'FLAG_ONLY':
        return True, f"{corr_id}: Flagged for follow-up"

    else:
        return False, f"{corr_id}: Unknown correction type '{corr_type}'"


def main():
    """Main function to apply corrections."""
    base_path = Path('/home/shawn/Code/trap-extraction')
    manifest_path = base_path / 'outputs' / 'qa-corrections-manifest-comprehensive.json'
    csv_path = base_path / 'outputs' / 'attribution.csv'

    print("=" * 60)
    print("QA Corrections Application Script")
    print("=" * 60)
    print(f"Manifest: {manifest_path}")
    print(f"CSV: {csv_path}")
    print()

    # Load data
    manifest = load_manifest(manifest_path)
    headers, rows = load_csv(csv_path)

    print(f"Loaded {len(rows)} records from CSV")
    print(f"Loaded {len(manifest['corrections'])} corrections from manifest")
    print()

    # Filter for pending corrections
    pending = [c for c in manifest['corrections'] if c.get('status') == 'PENDING']
    print(f"Found {len(pending)} pending corrections to apply")
    print()

    # Apply corrections
    applied = 0
    failed = 0
    applied_ids = []

    for correction in pending:
        corr_id = correction['id']
        print(f"Applying {corr_id}...")

        success, message = apply_correction(rows, correction)

        if success:
            print(f"  ✓ {message}")
            applied += 1
            applied_ids.append(corr_id)
        else:
            print(f"  ✗ {message}")
            failed += 1
        print()

    # Save updated CSV
    print("=" * 60)
    print(f"Applied: {applied}")
    print(f"Failed: {failed}")
    print(f"Total records: {len(rows)}")

    if applied > 0:
        save_csv(csv_path, headers, rows)
        print(f"\nSaved updated CSV to {csv_path}")

        # Output the IDs that were applied for manifest update
        print("\nApplied correction IDs:")
        for cid in applied_ids:
            print(f"  - {cid}")

    return 0 if failed == 0 else 1


if __name__ == '__main__':
    sys.exit(main())
