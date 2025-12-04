#!/usr/bin/env python3
"""
Extract Team A diary data from A_Diary.docx for Yambol 2010.

This script extracts walker, role, and author information from the PRIMARY
source (A_Diary.docx - March 2011 corrected version) to supersede data
currently extracted from SECONDARY/Tier 3 PDF sources (Day_XX.pdf).
"""

import csv
from pathlib import Path


def main():
    """Extract Team A diary data and write to CSV."""
    # Team A diary entries from A_Diary.docx
    # Extracted from PRIMARY source (26 KB, March 2011)

    diary_data = [
        {
            'Date': '2010-10-22',
            'Author': 'Adela Dornakova',
            'Leader': 'Adela D.',
            'Walkers_Original': 'AS | RL | PT | BW | EJ | AD',
            'PDA_Operator': 'EJ | AD',
            'GPS_Operator': 'AS',
            'Paper_Recorder': '',  # Not explicitly mentioned in diary
            'Source': 'A_Diary.docx',
            'Notes': 'PRIMARY source (March 2011); 6 walkers; 2 PDAs used',
        },
        {
            'Date': '2010-10-23',
            'Author': 'Viktoria Chystyakova',
            'Leader': 'Adela D.',
            'Walkers_Original': 'AS | RL | VC | EJ | AD',
            'PDA_Operator': 'EJ | AD',
            'GPS_Operator': 'AS',
            'Paper_Recorder': '',  # Not explicitly mentioned in diary
            'Source': 'A_Diary.docx',
            'Notes': 'PRIMARY source (March 2011); 5 walkers',
        },
        {
            'Date': '2010-10-24',
            'Author': 'Viktoria Chystyakova',
            'Leader': 'Adela D.',
            'Walkers_Original': 'AS | RL | VC | EJ | AD',
            'PDA_Operator': 'EJ | AD',
            'GPS_Operator': 'AS',
            'Paper_Recorder': '',  # Not explicitly mentioned in diary
            'Source': 'A_Diary.docx',
            'Notes': 'PRIMARY source (March 2011); 5 walkers',
        },
        {
            'Date': '2010-11-02',
            'Author': 'Bara W.',
            'Leader': 'Petra',
            'Walkers_Original': 'AS | PT | DG | BW | EJ',
            'PDA_Operator': 'PT',
            'GPS_Operator': 'AS',
            'Paper_Recorder': '',  # Not explicitly mentioned in diary
            'Source': 'A_Diary.docx',
            'Notes': 'PRIMARY source (March 2011); 5 walkers; '
                     'Leader identified as "Petra T." in text',
        },
        {
            'Date': '2010-11-03',
            'Author': 'Petra T.',
            'Leader': 'Petra',
            'Walkers_Original': 'AS | VC | DG | EJ | PT',
            'PDA_Operator': 'PT',
            'GPS_Operator': 'AS',
            'Paper_Recorder': '',  # Not explicitly mentioned in diary
            'Source': 'A_Diary.docx',
            'Notes': 'PRIMARY source (March 2011); 5 walkers',
        },
    ]

    # Name/Initial expansion guide (from diary)
    # AS = Adela Sobotkova (Adela S.)
    # RL = Royce Lawrence (Royce)
    # PT = Petra Tušlová (Petra, Petra T.)
    # BW = Bara Weissova (Bara, Bara W.)
    # EJ = Emma Jakobsson (Emma)
    # AD = Adela Dornakova (Adela D., Adela Dorňáková)
    # VC = Viktoria Chystyakova (Viktoria, Viki)
    # DG = Daniel Giannangelo (Drago)

    # Write to CSV
    output_file = Path('outputs/team-a-diary-extraction.csv')

    fieldnames = [
        'Date', 'Author', 'Leader', 'Walkers_Original',
        'PDA_Operator', 'GPS_Operator', 'Paper_Recorder',
        'Source', 'Notes'
    ]

    with open(output_file, 'w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(diary_data)

    print(f"Extracted {len(diary_data)} Team A diary entries to {output_file}")
    print("\nSummary:")
    for entry in diary_data:
        print(f"  {entry['Date']}: {entry['Leader']} leading "
              f"{len(entry['Walkers_Original'].split(' | '))} walkers")


if __name__ == '__main__':
    main()
