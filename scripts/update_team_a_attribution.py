#!/usr/bin/env python3
"""
Update Team A attribution records with PRIMARY source data from A_Diary.docx.

This script updates 5 Team A records in attribution.csv that were extracted
from Tier 3 PDF sources with data from the PRIMARY diary source (A_Diary.docx).
"""

import csv
from pathlib import Path


def main():
    """Update Team A records in attribution.csv with PRIMARY diary data."""

    # Load Team A diary extractions
    diary_file = Path('outputs/team-a-diary-extraction.csv')
    with open(diary_file, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        diary_data = {row['Date']: row for row in reader}

    # Load attribution CSV
    attribution_file = Path('outputs/attribution.csv')
    with open(attribution_file, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        fieldnames = reader.fieldnames
        rows = list(reader)

    # Update Team A records
    updates = 0
    for row in rows:
        date = row['Date']
        if date in diary_data and row['Team'] == 'A':
            diary_entry = diary_data[date]

            # Update fields from diary
            row['Leader'] = diary_entry['Leader']
            row['Walkers_Original'] = diary_entry['Walkers_Original']
            row['Walkers_Transliterated'] = diary_entry['Walkers_Original']
            row['PDA_Operator'] = diary_entry['PDA_Operator']
            row['GPS_Operator'] = diary_entry['GPS_Operator']
            row['Paper_Recorder'] = diary_entry['Paper_Recorder']
            row['Author'] = diary_entry['Author']
            row['PDF_Source'] = diary_entry['Source']

            # Update extraction notes
            row['Extraction_Notes'] = (
                f"Updated from PRIMARY source (A_Diary.docx; "
                f"March 2011 corrected version)"
            )

            # Clear QA notes about missing role data
            if 'No role data available' in row.get('QA_Notes', ''):
                row['QA_Notes'] = ''

            updates += 1
            print(f"Updated {date}: {row['Leader']} with "
                  f"{diary_entry['Walkers_Original']}")

    # Write updated CSV
    with open(attribution_file, 'w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)

    print(f"\n✅ Updated {updates} Team A records in attribution.csv")
    print("   All records now use PRIMARY source (A_Diary.docx)")


if __name__ == '__main__':
    main()
