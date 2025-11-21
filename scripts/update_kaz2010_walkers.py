#!/usr/bin/env python3
"""
Update Kazanlak 2010 walker data from diary extractions.

This script updates the final_attribution_v2_cleaned_edited.csv with accurate
walker data extracted from the Kaz 2010 team diaries (BG and EN versions).

Author: Claude Code collaboration
Date: November 2025
"""

import csv
from pathlib import Path

# Kaz 2010 walker data extracted from diaries
# Format: (date, team): (walkers_list, source_note)
KAZ2010_DIARY_DATA = {
    # Team A - from A_2010Diary_En.docx and A_2010Diary_BG.doc
    ('2010-03-22', 'A'): ('Julia Tzvetkova | Pesho | Tereza | Lindsay | Petra T.', 'A_2010Diary_En.docx'),
    ('2010-03-24', 'A'): ('Petra | Tereza | Lindsay | Yulia Dimitrova', 'A_2010Diary_BG.doc'),
    ('2010-03-25', 'A'): ('Julia Tzvetkova | Petra | Tereza | Lindsay | Yulia Dimitrova', 'A_2010Diary_BG.doc'),
    ('2010-03-26', 'A'): ('Julia Tzvetkova | Petra | Tereza | Lindsay | Yulia Dimitrova', 'A_2010Diary_BG.doc'),
    ('2010-03-27', 'A'): ('Julia Tzvetkova | Lindsay | Petra | Yulia Dimitrova', 'A_2010Diary_BG.doc'),
    ('2010-03-28', 'A'): ('Julia Tzvetkova | Lindsay | Petra | Yulia Dimitrova', 'A_2010Diary_BG.doc'),

    # Team B - from B_2010Diary_En.doc
    ('2010-03-17', 'B'): ('Adela | Lubomir | Vera | Petra | Pesho | Nadya | Tereza', 'B_2010Diary_En.doc'),
    ('2010-03-18', 'B'): ('Adela | Martin | Petra | Pesho | Lindsay', 'B_2010Diary_En.doc'),
    ('2010-03-19', 'B'): ('Adela | Petra | Pesho | Martin | Tereza | Lindsay', 'B_2010Diary_En.doc'),
    ('2010-03-20', 'B'): ('Adela | Petra | Pesho | Martin | Tereza | Lindsay', 'B_2010Diary_En.doc'),
    ('2010-03-21', 'B'): ('Adela | Petra | Tereza | Martin | Pesho | Lindsay', 'B_2010Diary_En.doc'),
    ('2010-03-22', 'B'): ('Adela | Martin | Renee | Stana | Dasa | Lubomir', 'B_2010Diary_En.doc'),
    ('2010-03-24', 'B'): ('Adela | Pesho | Dasa | Stana | Renee', 'B_2010Diary_En.doc'),
    ('2010-03-25', 'B'): ('Adela | Pesho | Dasa | Stana | Renee', 'B_2010Diary_En.doc'),
    ('2010-03-26', 'B'): ('Adela | Pesho | Dasa | Stana | Renee', 'B_2010Diary_En.doc'),
    ('2010-03-28', 'B'): ('Adela | Martin | Bogdana | Stana | Renee', 'B_2010Diary_En.doc'),
    ('2010-03-30', 'B'): ('Adela | Martin | Pesho | Stana | Petra', 'B_2010Diary_En.doc'),
    ('2010-03-31', 'B'): ('Adela | Martin | Pesho | Stana | Petra', 'B_2010Diary_En.doc'),
    ('2010-04-01', 'B'): ('Adela | Petra | Martin', 'B_2010Diary_En.doc'),

    # Team C - from C_2010Diary_BG.doc
    ('2010-03-17', 'C'): ('Elena | Bistra | Bara | Jana | Sonja | Lindsay', 'C_2010Diary_BG.doc'),
    ('2010-03-18', 'C'): ('Elena | Bistra | Bara | Jana | Sonja', 'C_2010Diary_BG.doc'),
    ('2010-03-19', 'C'): ('Elena | Bistra | Bara | Jana | Sonja', 'C_2010Diary_BG.doc'),
    ('2010-03-20', 'C'): ('Elena | Bistra | Bara | Jana | Sonja', 'C_2010Diary_BG.doc'),
    ('2010-03-21', 'C'): ('Elena | Bistra | Bara | Sonja | Jana', 'C_2010Diary_BG.doc'),
    ('2010-03-22', 'C'): ('Elena | Bistra | Bara | Sonja | Todor', 'C_2010Diary_BG.doc'),

    # Team D - from D_2010Diary_BG.doc
    ('2010-03-18', 'D'): ('Zhoro | Julia Tzvetkova | Nadja | Ljubo | Vera | Tereza', 'D_2010Diary_BG.doc'),
    ('2010-03-19', 'D'): ('Zhoro | Julia Tzvetkova | Nadja | Ljubo | Vera', 'D_2010Diary_BG.doc'),
    ('2010-03-20', 'D'): ('Zhoro | Bogdana | Nadja | Ljubo | Vera', 'D_2010Diary_BG.doc'),
}


def update_kaz2010_walkers():
    """Update Kaz 2010 records with diary-extracted walker data."""
    csv_path = Path(__file__).parent.parent / 'outputs' / 'final_attribution_v2_cleaned_edited.csv'

    # Read current CSV
    with open(csv_path, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        fieldnames = reader.fieldnames
        rows = list(reader)

    # Track updates
    updates = []

    for row in rows:
        date = row['Date']
        team = row['Team']
        key = (date, team)

        if key in KAZ2010_DIARY_DATA:
            walkers, source = KAZ2010_DIARY_DATA[key]
            old_walkers = row['Walkers_Original']

            # Update walker fields
            row['Walkers_Original'] = walkers
            row['Walkers_Transliterated'] = walkers  # Already in Latin

            # Update PDF source if not already set
            if not row['PDF_Source'] or row['PDF_Source'] == '':
                row['PDF_Source'] = source
            elif source not in row['PDF_Source']:
                row['PDF_Source'] = f"{row['PDF_Source']}, {source}"

            # Update extraction notes
            if 'diary' not in row.get('Extraction_Notes', '').lower():
                if row['Extraction_Notes']:
                    row['Extraction_Notes'] += '; Updated from diary'
                else:
                    row['Extraction_Notes'] = 'Extracted from diary'

            # Clear MISSING flag if walkers now present
            if 'MISSING: Walkers' in row.get('QA_Notes', ''):
                row['QA_Notes'] = row['QA_Notes'].replace('MISSING: Walkers | ', '')
                row['QA_Notes'] = row['QA_Notes'].replace('MISSING: Walkers', '')
                if row['QA_Notes'] == '':
                    row['QA_Notes'] = 'Complete'

            updates.append(f"{date} Team {team}: '{old_walkers}' -> '{walkers}'")

    # Write updated CSV
    with open(csv_path, 'w', encoding='utf-8', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)

    print(f"Updated {len(updates)} Kaz 2010 records:")
    for update in updates:
        print(f"  {update}")

    return len(updates)


if __name__ == '__main__':
    update_kaz2010_walkers()
