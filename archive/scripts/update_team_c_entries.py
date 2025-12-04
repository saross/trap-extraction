#!/usr/bin/env python3
"""
Update phase2b_pdf_walkers.csv with improved Team C diary entries.

Removes old Team C diary entries and adds the new improved ones.
"""

import csv
from pathlib import Path

OUTPUT_DIR = Path(__file__).parent.parent / "outputs"


def main():
    """Main execution function."""
    main_csv = OUTPUT_DIR / "phase2b_pdf_walkers.csv"
    team_c_csv = OUTPUT_DIR / "team_c_2009_diary_parsed.csv"

    # Read existing records, excluding old Team C diary entries
    existing_records = []
    removed_count = 0

    with open(main_csv, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            # Skip old Team C diary entries
            if row['Team'] == 'C' and row['PDF_Source'] == 'Diary Team C.doc':
                removed_count += 1
                continue
            existing_records.append(row)

    print(f"Removed {removed_count} old Team C diary entries")

    # Read new Team C records
    team_c_records = []
    with open(team_c_csv, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        team_c_records = list(reader)

    print(f"Adding {len(team_c_records)} new Team C diary entries")

    # Combine and write back
    all_records = existing_records + team_c_records

    with open(main_csv, 'w', encoding='utf-8', newline='') as f:
        fieldnames = ['Date', 'Team', 'Walkers', 'Team_Leader', 'Author',
                     'PDF_Source', 'Extraction_Notes']
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(all_records)

    print(f"\nUpdated {main_csv}")
    print(f"Total records: {len(all_records)}")


if __name__ == "__main__":
    main()
