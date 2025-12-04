#!/usr/bin/env python3
"""
Extract Author data from Kazanlak 2009 scanned Daily Progress Forms (PDFs).

Data extracted via vision analysis of:
- TeamA/A_2009Summary.pdf
- TeamB/Finalized/B_2009Summary.pdf
- TeamC/C_2009Summary.pdf

Author: Claude Code collaboration
Date: November 2025
"""

import csv

# Kaz 2009 Author data from PDF scans
# Format: (date, team): Author
KAZ2009_AUTHORS = {
    # Team A - from A_2009Summary.pdf
    ('2009-03-04', 'A'): 'SB',  # Stacey Barker
    ('2009-03-06', 'A'): 'SB',
    ('2009-03-07', 'A'): 'Tereza D.',
    ('2009-03-08', 'A'): 'Tereza',
    ('2009-03-09', 'A'): 'Tereza',
    ('2009-03-11', 'A'): 'Tereza D.',
    ('2009-03-12', 'A'): 'SB',
    ('2009-03-15', 'A'): 'Bara W.',
    ('2009-03-16', 'A'): 'Stalka K.',
    ('2009-03-19', 'A'): 'Stalka',
    ('2009-03-20', 'A'): 'Stalka',
    ('2009-03-21', 'A'): 'ST.',
    ('2009-03-24', 'A'): 'Stalka',
    ('2009-03-25', 'A'): 'ST.',
    ('2009-03-26', 'A'): 'PT.',  # Petra Tuslova
    ('2009-03-27', 'A'): 'Pt.',

    # Team B - from B_2009Summary.pdf
    ('2009-03-06', 'B'): 'Vera',
    ('2009-03-07', 'B'): 'Vera',
    ('2009-03-08', 'B'): 'Vera',
    ('2009-03-09', 'B'): 'Vera',
    ('2009-03-11', 'B'): 'V.',
    ('2009-03-12', 'B'): 'V.',
    ('2009-03-16', 'B'): 'Tereza',
    ('2009-03-19', 'B'): 'Ivana Klimova',
    ('2009-03-20', 'B'): 'Ivana Klimova',
    ('2009-03-23', 'B'): 'TB',  # Tereza Blazkova
    ('2009-03-24', 'B'): 'Ivana Klimova',
    ('2009-03-25', 'B'): 'Ivana Klimova',
    ('2009-03-26', 'B'): 'Ivana Klimova',
    ('2009-03-27', 'B'): 'Petra T.',
    ('2009-04-05', 'B'): 'Sobotkova',  # Signature

    # Team C - from C_2009Summary.pdf
    ('2009-03-04', 'C'): 'Adela',
    ('2009-03-06', 'C'): 'CB',  # Charlotte B.
    ('2009-03-07', 'C'): 'CB',
    ('2009-03-09', 'C'): 'CB',
    ('2009-03-11', 'C'): 'CS',
    ('2009-03-12', 'C'): 'CR',
    ('2009-03-16', 'C'): 'CB',
    ('2009-03-19', 'C'): 'Katarina',
    ('2009-03-23', 'C'): 'CB',
    ('2009-03-25', 'C'): 'Bryan Zlatos',
    ('2009-03-24', 'C'): 'Bryan Zlatos',
    ('2009-03-26', 'C'): 'Bryan Zlatos',
    ('2009-03-27', 'C'): 'Bryan Zlatos',
}


def main():
    """Update CSV with Author data from Kaz 2009 PDF scans."""
    input_file = 'outputs/attribution.csv'

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

        if key in KAZ2009_AUTHORS:
            author = KAZ2009_AUTHORS[key]
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

    print(f"\nUpdated {updated_count} records with Author data from Kaz 2009 PDFs.")


if __name__ == '__main__':
    main()
