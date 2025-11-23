#!/usr/bin/env python3
"""
Extract walker and role data from Team B Diary new.docx (Yambol 2010).

This script extracts data from the PRIMARY diary source which contains
post-season corrections made in March 2011.
"""

import zipfile
import re
from pathlib import Path

def extract_docx_text(docx_path):
    """Extract text from .docx file."""
    with zipfile.ZipFile(docx_path, 'r') as zip_ref:
        xml_content = zip_ref.read('word/document.xml').decode('utf-8')

    # Extract text nodes
    text_pattern = re.compile(r'<w:t[^>]*>([^<]+)</w:t>')
    texts = text_pattern.findall(xml_content)
    return ''.join(texts)

def parse_entries(text):
    """Parse diary entries to extract walker and role data."""
    entries = []

    # Split into sections by date headings
    # Pattern: digit(s) + "November 2010" + optional author
    # Capture content until next date or end
    date_pattern = re.compile(
        r'(\d+)\s+November\s+2010,\s*([^N]+?)Number of [Ww]alkers?:\s*\d+\s*[-–]\s*([^L]+?)Leader:\s*([^WS]+?)(?=Weather:|Start Time:|Start:)',
        re.DOTALL | re.IGNORECASE
    )

    for match in date_pattern.finditer(text):
        day = match.group(1)
        author = match.group(2).strip()
        walkers_raw = match.group(3).strip()
        leader = match.group(4).strip()

        date = f'2010-11-{day.zfill(2)}'

        # Parse walker roles
        walkers = []
        roles = {
            'PDA': [],
            'GPS': [],
            'Forms': [],
            'Artifacts': [],
            'Documents': []
        }

        if walkers_raw:
            # Split by comma
            walker_parts = re.split(r',\s*', walkers_raw)
            for part in walker_parts:
                part = part.strip()
                if not part:
                    continue

                # Parse role annotations like "DR(PDA)" or "KL (GPS)" or "ACQ (GPS)"
                role_match = re.search(r'([A-Za-z\s\.]+?)\s*\(([^)]+)\)', part)
                if role_match:
                    name = role_match.group(1).strip()
                    role = role_match.group(2).strip()
                    walkers.append(name)

                    # Map role to standard categories
                    if 'PDA' in role:
                        roles['PDA'].append(name)
                    if 'GPS' in role:
                        roles['GPS'].append(name)
                    if 'Form' in role or 'Document' in role or 'Survey Document' in role:
                        roles['Forms'].append(name)
                    if 'Artifact' in role:
                        roles['Artifacts'].append(name)
                else:
                    # Name without role annotation (just initials like "JP")
                    walkers.append(part)

        entries.append({
            'date': date,
            'author': author,
            'leader': leader,
            'walkers_raw': walkers_raw,
            'walkers': walkers,
            'pda_operators': ' | '.join(roles['PDA']) if roles['PDA'] else '',
            'gps_operators': ' | '.join(roles['GPS']) if roles['GPS'] else '',
            'forms': ' | '.join(roles['Forms']) if roles['Forms'] else '',
        })

    return entries

def main():
    base_path = Path('/media/shawn/191c3b96-5fa5-4d0d-8805-0cf05d3d8468/synology/Adela/TRAP-WD-2020-04')
    docx_path = base_path / 'Elhovo 2010-12-12/2010/Project Records/Team B/Team B Diary new.docx'

    print('Extracting walker data from Team B Diary new.docx...')
    print('=' * 80)

    text = extract_docx_text(docx_path)
    entries = parse_entries(text)

    for entry in entries:
        print(f"\nDate: {entry['date']}")
        print(f"Author: {entry['author']}")
        print(f"Leader: {entry['leader']}")
        print(f"Walkers raw: {entry['walkers_raw']}")
        print(f"Walkers: {' | '.join(entry['walkers'])}")
        print(f"PDA: {entry['pda_operators']}")
        print(f"GPS: {entry['gps_operators']}")
        print(f"Forms: {entry['forms']}")
        print('-' * 80)

    print(f"\nTotal entries extracted: {len(entries)}")

if __name__ == '__main__':
    main()
