#!/usr/bin/env python3
"""
Extract Author data from Kazanlak 2010 scanned Daily Progress Forms (PDFs).

Data extracted via vision analysis of:
- Team A/FieldRecords/A_2010Summary.pdf
- Team B/FieldRecords/B_2010Summary.pdf

Author: Claude Code collaboration
Date: November 2025
"""

import csv

# Kaz 2010 Author data from PDF scans
# Format: (date, team): Author
KAZ2010_AUTHORS = {
    # Team A - from A_2010Summary.pdf
    ('2010-03-22', 'A'): 'Lindsay',
    ('2010-03-24', 'A'): 'Lindsay',
    ('2010-03-25', 'A'): 'Lindsay',
    ('2010-03-26', 'A'): 'Lindsay',
    ('2010-03-27', 'A'): 'Lindsay',
    ('2010-03-28', 'A'): 'Lindsay',
    ('2010-04-07', 'A'): 'Viki',
    ('2010-04-08', 'A'): 'Lindsay',

    # Team B - from B_2010Summary.pdf
    ('2010-03-17', 'B'): 'Vera',
    ('2010-03-19', 'B'): 'Petra J.',
    ('2010-03-20', 'B'): 'Petra',
    ('2010-03-21', 'B'): 'Petra',
    ('2010-03-25', 'B'): 'Dasa',
    ('2010-03-26', 'B'): 'Renee G',
    ('2010-03-30', 'B'): 'Vladka',
    ('2010-03-31', 'B'): 'Vladka',
    ('2010-04-01', 'B'): 'Vladka',
    ('2010-04-02', 'B'): 'Pt.',
    ('2010-04-07', 'B'): 'Dasa',
}


def main():
    """Update CSV with Author data from Kaz 2010 PDF scans."""
    input_file = 'outputs/final_attribution_v2_cleaned_edited.csv'

    # Read existing data
    with open(input_file, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        fieldnames = reader.fieldnames
        rows = list(reader)

    # Update rows with Author data (only if Author field is empty)
    updated_count = 0
    for row in rows:
        date = row['Date']
        team = row['Team']
        key = (date, team)

        if key in KAZ2010_AUTHORS:
            author = KAZ2010_AUTHORS[key]
            # Only update if currently empty
            if not row.get('Author') or row.get('Author') == '':
                row['Author'] = author
                updated_count += 1
                print(f"  Updated {date} Team {team}: Author = {author}")

    # Write updated data
    with open(input_file, 'w', encoding='utf-8', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)

    print(f"\nUpdated {updated_count} records with Author data from Kaz 2010 PDFs.")


if __name__ == '__main__':
    main()
