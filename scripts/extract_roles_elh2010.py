#!/usr/bin/env python3
"""
Extract role data from Elhovo/Yambol 2010 Team B diary.

Initials mapping:
- DR = Dr. Ross (Shawn Ross)
- KL = Kimberly Lowe
- AP = Alina Petanec
- RL = Royce Lawrence
- JP = Julia Prazniak
- ACQ = Ashley Chee Quee
- PT = Petra Tuslova
- BW = Bara Weissova
- DG = Daniel Giannangelo
- EJ = Ellen Janssen
- SH = Sophie Hay

Author: Claude Code collaboration
Date: November 2025
"""

import csv

# Name mapping for initials
INITIALS = {
    'DR': 'Shawn Ross',
    'KL': 'Kimberly Lowe',
    'AP': 'Alina Petanec',
    'RL': 'Royce Lawrence',
    'JP': 'Julia Prazniak',
    'ACQ': 'Ashley Chee Quee',
    'PT': 'Petra Tuslova',
    'BW': 'Bara Weissova',
    'DG': 'Daniel Giannangelo',
    'EJ': 'Ellen Janssen',
    'SH': 'Sophie Hay',
    'VC': 'VC',  # Unknown
    'YL': 'YL',  # Unknown
    'AS': 'AS',  # Unknown
    'EL': 'EL',  # Unknown
}

# Elhovo 2010 role data extracted from Team B Diary
# Format: (date, team): {roles dict}
ELH2010_ROLES = {
    ('2010-11-02', 'B'): {
        'PDA_Operator': 'Shawn Ross | VC',
        'GPS_Operator': 'Kimberly Lowe',
        'Paper_Recorder': 'Royce Lawrence',
        'Author': 'Royce Lawrence'
    },
    ('2010-11-03', 'B'): {
        'PDA_Operator': 'Shawn Ross',
        'GPS_Operator': 'Kimberly Lowe',
        'Paper_Recorder': 'Royce Lawrence',
        'Author': 'Royce Lawrence'
    },
    ('2010-11-04', 'B'): {
        'PDA_Operator': 'Shawn Ross',
        'GPS_Operator': 'Kimberly Lowe',
        'Paper_Recorder': 'Royce Lawrence',
        'Author': 'Alina Petanec'
    },
    ('2010-11-05', 'B'): {
        'PDA_Operator': 'Shawn Ross | Royce Lawrence',
        'GPS_Operator': 'Ashley Chee Quee',
        'Paper_Recorder': 'Julia Prazniak',
        'Author': 'Ashley Chee Quee'
    },
    ('2010-11-06', 'B'): {
        'PDA_Operator': 'Shawn Ross | Royce Lawrence',
        'GPS_Operator': 'Royce Lawrence',
        'Paper_Recorder': 'Julia Prazniak',
        'Author': 'Alina Petanec'
    },
    ('2010-11-07', 'B'): {
        'PDA_Operator': 'Shawn Ross | Royce Lawrence',
        'GPS_Operator': 'Kimberly Lowe',
        'Photographer': 'Kimberly Lowe',
        'Paper_Recorder': 'Julia Prazniak',
        'Author': 'Kimberly Lowe'
    },
    ('2010-11-10', 'B'): {
        'PDA_Operator': 'Royce Lawrence',
        'GPS_Operator': 'Kimberly Lowe',
        'Photographer': 'Ashley Chee Quee | Daniel Giannangelo',
        'Paper_Recorder': 'Julia Prazniak',
        'Author': 'Kimberly Lowe'
    },
    ('2010-11-12', 'B'): {
        'PDA_Operator': 'Royce Lawrence',
        'GPS_Operator': 'Daniel Giannangelo',
        'Paper_Recorder': 'Ellen Janssen',
        'Author': 'Alina Petanec'
    },
    ('2010-11-14', 'B'): {
        'PDA_Operator': 'Daniel Giannangelo | Royce Lawrence',
        'Paper_Recorder': 'Daniel Giannangelo | Julia Prazniak',
        'Author': 'Alina Petanec'
    },
    ('2010-11-15', 'B'): {
        'PDA_Operator': 'Petra Tuslova',
        'GPS_Operator': 'Ashley Chee Quee',
        'Paper_Recorder': 'Sophie Hay',
        'Author': 'Alina Petanec'
    },
    ('2010-11-16', 'B'): {
        'PDA_Operator': 'Bara Weissova',
        'GPS_Operator': 'AS',
        'Paper_Recorder': 'Sophie Hay',
        'Author': 'Petra Tuslova'
    },
}


def main():
    """Update CSV with role data from Elhovo 2010 diaries."""
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

        if key in ELH2010_ROLES:
            roles = ELH2010_ROLES[key]
            for field, value in roles.items():
                if field in fieldnames and value:
                    if not row.get(field) or row.get(field) == '':
                        row[field] = value
            updated_count += 1
            print(f"  Updated {date} Team {team}")

    # Write updated data
    with open(input_file, 'w', encoding='utf-8', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)

    print(f"\nUpdated {updated_count} records with role data from Elhovo 2010 diaries.")


if __name__ == '__main__':
    main()
