#!/usr/bin/env python3
"""
Correct Excel date error: Remove 2010-03-08 and update 2010-04-08 with survey units.

This script applies the corrections identified by user:
- Row 30: 2010-03-18 is CORRECT (already in data)
- Row 45: 2010-03-08 is WRONG → should be 2010-04-08
  - Delete the 2010-03-08 entry (units 30742-30773)
  - Add those units to the existing 2010-04-08 entry

Created: 23 November 2025
"""

import csv
from pathlib import Path

# File paths
BASE_DIR = Path("/media/shawn/191c3b96-5fa5-4d0d-8805-0cf05d3d8468/synology/Adela/TRAP-WD-2020-04/claude_extraction")
INPUT_FILE = BASE_DIR / "outputs/attribution.csv"
OUTPUT_FILE = INPUT_FILE  # Overwrite in place

def main():
    """Apply date corrections to attribution.csv."""

    rows = []
    header = None
    deleted_count = 0
    updated_count = 0

    # Read the file
    with open(INPUT_FILE, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        header = reader.fieldnames

        for row in reader:
            # Delete the incorrect 2010-03-08 Team C entry
            if row['Date'] == '2010-03-08' and row['Team'] == 'C':
                print(f"DELETING: {row['Date']} Team {row['Team']} (units {row['Start Unit']}-{row['End Unit']})")
                deleted_count += 1
                continue  # Skip this row

            # Update the 2010-04-08 Team C entry with survey units
            if row['Date'] == '2010-04-08' and row['Team'] == 'C':
                print(f"UPDATING: {row['Date']} Team {row['Team']}")
                print(f"  Before: Units={row['Start Unit']}-{row['End Unit']}")

                # Add the survey units from the deleted 03-08 entry
                row['Start Unit'] = '30742.0'
                row['End Unit'] = '30773.0'

                # Update source to include both XLS and PDF
                row['XLS_Source'] = 'Kaz10_SurveySummary.xls'

                # Update extraction notes
                existing_notes = row.get('Extraction_Notes', '')
                if existing_notes:
                    row['Extraction_Notes'] = f"{existing_notes}; Survey units corrected from Excel date error (was 2010-03-08, corrected to 2010-04-08)"
                else:
                    row['Extraction_Notes'] = "Survey units corrected from Excel date error (was 2010-03-08, corrected to 2010-04-08)"

                # Clear QA_Notes if it says "MISSING: Survey units"
                if 'MISSING: Survey units' in row.get('QA_Notes', ''):
                    row['QA_Notes'] = 'No role data available'

                print(f"  After: Units={row['Start Unit']}-{row['End Unit']}")
                updated_count += 1

            rows.append(row)

    # Write the corrected file
    with open(OUTPUT_FILE, 'w', encoding='utf-8', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=header)
        writer.writeheader()
        writer.writerows(rows)

    print(f"\n✓ Deleted {deleted_count} row(s)")
    print(f"✓ Updated {updated_count} row(s)")
    print(f"✓ Total rows in output: {len(rows)}")
    print(f"✓ Saved to: {OUTPUT_FILE}")

if __name__ == '__main__':
    main()
