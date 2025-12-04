#!/usr/bin/env python3
"""
Extract role data from Kazanlak 2010 diaries.

This script updates the final_attribution_v2_cleaned_edited.csv with:
- PDA_Operator
- GPS_Operator
- Photographer
- Paper_Recorder (Forms)
- Author

Data extracted from Team A and Team B English diaries.

Author: Claude Code collaboration
Date: November 2025
"""

import csv

# Kaz 2010 role data extracted from diaries
# Format: (date, team): {roles dict}
KAZ2010_ROLES = {
    # Team B - from B_2010Diary_En.doc
    ('2010-03-17', 'B'): {
        'PDA_Operator': 'Petra | Nadya | Pesho',
        'GPS_Operator': 'Tereza',
        'Paper_Recorder': 'Vera',
        'Photographer': '',
        'Author': 'Petra J.'
    },
    ('2010-03-18', 'B'): {
        'Author': 'Petra J.'
    },
    ('2010-03-19', 'B'): {
        'Author': ''
    },
    ('2010-03-20', 'B'): {
        'Author': 'Petra J.'
    },
    ('2010-03-21', 'B'): {
        'PDA_Operator': 'Tereza | Petra | Pesho',
        'GPS_Operator': 'Adela',
        'Photographer': 'Adela',
        'Author': 'Petra J.'
    },
    ('2010-03-22', 'B'): {
        'PDA_Operator': 'Adela | Lubomir',
        'GPS_Operator': 'Adela | Dasa',
        'Photographer': 'Renee',
        'Author': 'Renee Gardiner'
    },
    ('2010-03-23', 'B'): {
        'Author': 'Renee Gardiner'
    },
    ('2010-03-24', 'B'): {
        'PDA_Operator': 'Adela',
        'GPS_Operator': 'Adela | Dasa',
        'Photographer': 'Renee',
        'Author': 'Renee Gardiner'
    },
    ('2010-03-25', 'B'): {
        'Author': 'Renee Gardiner'
    },
    ('2010-03-26', 'B'): {
        'Author': 'Renee Gardiner'
    },
    ('2010-03-27', 'B'): {
        'Author': 'Renee Gardiner'
    },
    ('2010-03-28', 'B'): {
        'Author': 'Renee Gardiner'
    },
    ('2010-03-29', 'B'): {
        'Author': ''
    },
    ('2010-03-30', 'B'): {
        'Author': 'Petra Tuslova'
    },
    ('2010-03-31', 'B'): {
        'Author': 'Petra Tuslova'
    },
    ('2010-04-01', 'B'): {
        'Author': 'Adela Sobotkova'
    },
    ('2010-04-02', 'B'): {
        'Author': 'Adela Sobotkova'
    },
    ('2010-04-07', 'B'): {
        'Author': 'Adela Sobotkova'
    },
    ('2010-04-08', 'B'): {
        'Author': 'Adela Sobotkova'
    },
    ('2010-04-09', 'B'): {
        'Author': 'Adela Sobotkova'
    },
    ('2010-04-10', 'B'): {
        'Author': 'Adela Sobotkova'
    },

    # Team A - from A_2010Diary_En.docx
    ('2010-03-22', 'A'): {
        'PDA_Operator': 'Tereza | Pesho',
        'GPS_Operator': 'Petra T.',
        'Author': 'Petra T.'
    },
    ('2010-03-24', 'A'): {
        'PDA_Operator': 'Tereza',
        'GPS_Operator': 'Petra T.',
        'Author': 'Petra Tuslova'
    },
    ('2010-03-25', 'A'): {
        'PDA_Operator': 'Tereza',
        'GPS_Operator': 'Julia',
        'Author': 'Petra Tuslova'
    },
    ('2010-03-26', 'A'): {
        'PDA_Operator': 'Tereza',
        'GPS_Operator': 'Julia',
        'Author': 'Petra Tuslova'
    },
    ('2010-03-27', 'A'): {
        'Author': 'Petra Tuslova'
    },
    ('2010-03-28', 'A'): {
        'PDA_Operator': 'Petra',
        'GPS_Operator': 'Petra',
        'Author': 'Petra Tuslova'
    },
    ('2010-04-07', 'A'): {
        'PDA_Operator': 'Petra',
        'GPS_Operator': 'Stanislav',
        'Author': 'Petra Tuslova'
    },
    ('2010-04-08', 'A'): {
        'PDA_Operator': 'Petra',
        'GPS_Operator': 'Stanislav',
        'Author': 'Lindsay'
    },
    ('2010-04-09', 'A'): {
        'PDA_Operator': 'Petra',
        'GPS_Operator': 'Stanislav',
        'Author': 'Petra T.'
    },
}


def main():
    """Update CSV with role data from Kaz 2010 diaries."""
    input_file = 'outputs/attribution.csv'

    # Read existing data
    with open(input_file, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        fieldnames = reader.fieldnames
        rows = list(reader)

    # Update rows with role data
    updated_count = 0
    for row in rows:
        date = row['Date']
        team = row['Team']
        key = (date, team)

        if key in KAZ2010_ROLES:
            roles = KAZ2010_ROLES[key]
            for field, value in roles.items():
                if field in fieldnames and value:
                    # Only update if currently empty or if we have better data
                    if not row.get(field) or row.get(field) == '':
                        row[field] = value
            updated_count += 1
            print(f"  Updated {date} Team {team}")

    # Write updated data
    with open(input_file, 'w', encoding='utf-8', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)

    print(f"\nUpdated {updated_count} records with role data from Kaz 2010 diaries.")


if __name__ == '__main__':
    main()
