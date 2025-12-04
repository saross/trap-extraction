#!/usr/bin/env python3
"""
Update attribution.csv with manual extractions from diary records.

This script updates 7 records that failed automated extraction due to:
- Overall team lists instead of daily lists
- Non-standard date formats
- Narrative-embedded walker information
- .docx file format issues

All extractions follow user-provided resolutions documented in
manual-extraction-guide.md.
"""
import csv
from pathlib import Path
from datetime import datetime

# Extracted data from diary sources
MANUAL_EXTRACTIONS = {
    ('2009-10-23', 'C'): {
        'walkers': 'Bara | Petra | Sona | Tereza | Todor | Georgi',
        'source': 'The Diary of Team C.doc',
        'note': 'Default walker list from diary header (team stable throughout season)',
        'roles': {}
    },
    ('2009-11-14', 'A'): {
        'walkers': 'Adela | Katya | Marto',
        'source': 'Diary Team A.doc',
        'note': 'Extracted from narrative (Team A heads out with Adela, Katya and Marto)',
        'roles': {}
    },
    ('2010-04-07', 'A'): {
        'walkers': 'Stanislav | Martin | Viki | Petra',
        'source': 'A_2010Diary_En.docx',
        'note': 'Extracted from EN diary (BG diary ends 28 March)',
        'roles': {
            'GPS': 'Stanislav',
            'PDA': 'Petra',
            'Leader': 'Petra'
        },
        'author': 'Petra Tuslova'
    },
    ('2010-04-08', 'A'): {
        'walkers': 'Petra | Viki | Lindsay | Stanislav | Marto',
        'source': 'A_2010Diary_En.docx',
        'note': 'Extracted from EN diary (BG diary ends 28 March)',
        'roles': {
            'GPS': 'Stanislav',
            'PDA': 'Petra',
            'Leader': 'Petra'
        },
        'author': 'Lindsay'
    },
    ('2010-04-07', 'C'): {
        'walkers': 'Elena | Bara | Sonya | Todor | Lindsay',
        'source': 'C_2010Diary_BG.doc',
        'note': 'Re-extracted with Roman numeral date format awareness (7. IV. 2010)',
        'roles': {}
    },
    ('2011-10-24', 'A'): {
        'walkers': 'GN | YuTs | ET | Anani Antonov | Al.R',
        'source': 'A_2011Diary_BG.doc',
        'note': 'Rainy day, no survey walking; 5-person group visited burial mounds for GPS coordinates',
        'roles': {}
    },
    ('2011-11-08', 'B'): {
        'walkers': 'Petra | Adela | Bethan | Elaine | Hamish',
        'source': 'B_2011Diary_En.docx',
        'note': 'Re-extracted using pandoc for .docx format',
        'roles': {
            'Leader': 'Petra'
        }
    }
}

def update_attribution_csv():
    """Update attribution.csv with manual extractions."""

    input_path = Path('outputs/attribution.csv')
    output_path = Path('outputs/attribution.csv')
    backup_path = Path(f'outputs/attribution.csv.backup_manual_{datetime.now().strftime("%Y%m%d_%H%M%S")}')

    # Create backup
    print(f"Creating backup: {backup_path.name}")
    with open(input_path, 'r', encoding='utf-8') as f:
        backup_content = f.read()
    with open(backup_path, 'w', encoding='utf-8') as f:
        f.write(backup_content)

    # Read CSV
    rows = []
    with open(input_path, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        headers = reader.fieldnames
        rows = list(reader)

    # Update records
    updated_count = 0
    for row in rows:
        key = (row['Date'], row['Team'])
        if key in MANUAL_EXTRACTIONS:
            data = MANUAL_EXTRACTIONS[key]

            # Update walker columns
            row['Walkers_Original'] = data['walkers']
            row['Walkers_Transliterated'] = data['walkers']  # Already transliterated

            # Update roles if provided
            if 'GPS' in data['roles']:
                row['GPS_Operator'] = data['roles']['GPS']
            if 'PDA' in data['roles']:
                row['PDA_Operator'] = data['roles']['PDA']
            if 'Leader' in data['roles'] and not row['Leader']:
                row['Leader'] = data['roles']['Leader']
            if 'author' in data:
                row['Author'] = data['author']

            # Update source reference
            if 'PDF_Source' in row:
                row['PDF_Source'] = data['source']

            # Update extraction notes
            old_note = row.get('Extraction_Notes', '')
            if 'MISSING' in old_note or not old_note:
                row['Extraction_Notes'] = f"Manual extraction: {data['note']}"
            else:
                row['Extraction_Notes'] = f"{old_note} | Manual extraction: {data['note']}"

            updated_count += 1
            print(f"Updated {row['Date']}, Team {row['Team']}: {data['walkers']}")

    # Write updated CSV
    with open(output_path, 'w', encoding='utf-8', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=headers)
        writer.writeheader()
        writer.writerows(rows)

    print(f"\n✅ Updated {updated_count} records in {output_path}")
    print(f"Backup saved: {backup_path}")

if __name__ == '__main__':
    update_attribution_csv()
