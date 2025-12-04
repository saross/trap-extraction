#!/usr/bin/env python3
"""
Extract role information from diary files using regex patterns.

This script performs Phase A of the role extraction workflow: automated regex
scanning of all diary files to capture explicit/structured role mentions.

Expected yield is low (most diaries are narrative), but this establishes a
baseline before manual NLP review.

Role fields targeted:
- PDA_Operator
- GPS_Operator
- Paper_Recorder
- Photographer
- Author
- Data_Editor

Author: Claude Code
Date: 24 November 2025
"""

import csv
import re
import subprocess
from pathlib import Path
from datetime import datetime
from typing import Optional


# Base paths
BASE_PATH = Path('/media/shawn/191c3b96-5fa5-4d0d-8805-0cf05d3d8468/synology/Adela/TRAP-WD-2020-04')
TRAP_EXTRACTION = BASE_PATH / 'trap-extraction'
OUTPUT_FILE = TRAP_EXTRACTION / 'outputs' / 'role-extractions-regex.csv'

# Diary file locations (team diaries only - excluding templates, GC, RS)
DIARY_LOCATIONS = {
    # Kazanlak 2009
    'kaz2009': {
        'base': BASE_PATH / 'Kazanluk' / '2009' / 'Project Records',
        'files': {
            'A': ['TeamA/A_Diary_BG.doc', 'TeamA/A_Diary_En.doc'],
            'B': ['TeamB/B_Diary_BG.doc', 'TeamB/B_Diary_En.docx'],
            'C': ['TeamC/C_Diary_BG.doc'],
            'D': ['TeamD/D Diary_BG.doc', 'TeamD/D_Diary_En.docx'],
            'E': ['TeamE/E Diary_BG.doc'],
        },
        'supplemental': [BASE_PATH / 'Kazanluk' / '2009' / 'Diary March 09.doc'],
    },
    # Kazanlak 2010
    'kaz2010': {
        'base': BASE_PATH / 'Kazanluk' / '2010' / 'Project Records',
        'files': {
            'A': ['Team A/A_2010Diary_BG.doc', 'Team A/A_2010Diary_En.docx'],
            'B': ['Team B/B_2010Diary_En.doc', 'Team B/B_2010Diary_BG.docx'],
            'C': ['Team C/C_2010Diary_BG.doc', 'Team C/C_2010Diary_En.docx'],
            'D': ['Team D/D_2010Diary_BG.doc', 'Team D/D_2010Diary_En.docx'],
        },
    },
    # Kazanlak 2011
    'kaz2011': {
        'base': BASE_PATH / 'Kazanluk' / '2011-11-30' / 'Project Records',
        'files': {
            'A': ['Team A/A_2011Diary_BG.doc'],
            'B': ['Team B/B_2011Diary_En.docx', 'Team B/B_2011Diary_BG.docx'],
            'C': ['Team C/C_2011Diary_En.docx', 'Team C/C_2011Diary_BG.docx'],
            'D': ['Team D/D_2011Diary_BG.doc'],
        },
    },
    # Elhovo 2009
    'elh2009': {
        'base': BASE_PATH / 'Elhovo 2010-12-12' / '2009' / 'Project Records',
        'files': {
            'A': ['Team A/Diary Team A.doc', 'Team A/Diary_Aneta.doc'],
            'B': ['Team B/DiaryTeamB.doc'],
            'C': ['Team C/The Diary of Team C.doc'],
        },
    },
    # Elhovo 2010
    'elh2010': {
        'base': BASE_PATH / 'Elhovo 2010-12-12' / '2010' / 'Project Records',
        'files': {
            'A': ['Team A/A_Diary.docx'],
            'B': ['Team B/Team B Diary new.docx', 'Team B/Team B Diary.docx'],
        },
        'supplemental': [BASE_PATH / 'Elhovo 2010-12-12' / '2010' / 'Project Records' / 'Diary_Adela2010Fall.docx'],
    },
}

# Regex patterns for role extraction
# Format: (pattern, role_type, capture_group_index)
ROLE_PATTERNS = [
    # Explicit structured patterns (English)
    (r'PDA[:\s]+([A-Za-z\s,|&]+?)(?:\n|$|;)', 'PDA_Operator', 1),
    (r'PDA\s+operator[:\s]+([A-Za-z\s,|&]+?)(?:\n|$|;)', 'PDA_Operator', 1),
    (r'GPS[:\s]+([A-Za-z\s,|&]+?)(?:\n|$|;)', 'GPS_Operator', 1),
    (r'GPS\s+operator[:\s]+([A-Za-z\s,|&]+?)(?:\n|$|;)', 'GPS_Operator', 1),
    (r'Paper\s+recorder[:\s]+([A-Za-z\s,|&]+?)(?:\n|$|;)', 'Paper_Recorder', 1),
    (r'Recorder[:\s]+([A-Za-z\s,|&]+?)(?:\n|$|;)', 'Paper_Recorder', 1),
    (r'Forms[:\s]+([A-Za-z\s,|&]+?)(?:\n|$|;)', 'Paper_Recorder', 1),
    (r'Photographer[:\s]+([A-Za-z\s,|&]+?)(?:\n|$|;)', 'Photographer', 1),
    (r'Photo[:\s]+([A-Za-z\s,|&]+?)(?:\n|$|;)', 'Photographer', 1),
    (r'Author[:\s]+([A-Za-z\s,|&]+?)(?:\n|$|;)', 'Author', 1),
    (r'Written\s+by[:\s]+([A-Za-z\s,|&]+?)(?:\n|$|;)', 'Author', 1),
    (r'Data\s+entry[:\s]+([A-Za-z\s,|&]+?)(?:\n|$|;)', 'Data_Editor', 1),

    # Bulgarian patterns (transliterated)
    (r'ПДА[:\s]+([А-Яа-яA-Za-z\s,|&]+?)(?:\n|$|;)', 'PDA_Operator', 1),
    (r'GPS[:\s]+([А-Яа-яA-Za-z\s,|&]+?)(?:\n|$|;)', 'GPS_Operator', 1),
    (r'Автор[:\s]+([А-Яа-яA-Za-z\s,|&]+?)(?:\n|$|;)', 'Author', 1),
    (r'Снимки[:\s]+([А-Яа-яA-Za-z\s,|&]+?)(?:\n|$|;)', 'Photographer', 1),

    # Date-prefixed role assignments (from structured diary headers)
    (r'(?:Day\s+\d+|Date[:\s]+\d{1,2}[./]\d{1,2}[./]\d{2,4}).*?PDA[:\s]+([A-Za-z\s,|&]+?)(?:\n|;)', 'PDA_Operator', 1),
]


def extract_text_from_doc(file_path: Path) -> Optional[str]:
    """
    Extract text from a .doc file using antiword.

    Args:
        file_path: Path to the .doc file

    Returns:
        Extracted text or None if extraction failed
    """
    try:
        result = subprocess.run(
            ['antiword', str(file_path)],
            capture_output=True,
            text=True,
            timeout=30
        )
        if result.returncode == 0:
            return result.stdout
        else:
            print(f"  Warning: antiword failed for {file_path.name}: {result.stderr[:100]}")
            return None
    except subprocess.TimeoutExpired:
        print(f"  Warning: antiword timeout for {file_path.name}")
        return None
    except FileNotFoundError:
        print("  Error: antiword not installed. Install with: sudo apt install antiword")
        return None


def extract_text_from_docx(file_path: Path) -> Optional[str]:
    """
    Extract text from a .docx file using python-docx or pandoc.

    Args:
        file_path: Path to the .docx file

    Returns:
        Extracted text or None if extraction failed
    """
    # Try pandoc first (more reliable)
    try:
        result = subprocess.run(
            ['pandoc', '-t', 'plain', str(file_path)],
            capture_output=True,
            text=True,
            timeout=30
        )
        if result.returncode == 0:
            return result.stdout
    except (subprocess.TimeoutExpired, FileNotFoundError):
        pass

    # Fall back to python-docx
    try:
        from docx import Document
        doc = Document(str(file_path))
        return '\n'.join(para.text for para in doc.paragraphs)
    except ImportError:
        print("  Warning: python-docx not installed")
        return None
    except Exception as e:
        print(f"  Warning: Failed to read {file_path.name}: {e}")
        return None


def extract_text(file_path: Path) -> Optional[str]:
    """
    Extract text from a diary file (.doc or .docx).

    Args:
        file_path: Path to the diary file

    Returns:
        Extracted text or None if extraction failed
    """
    if not file_path.exists():
        return None

    suffix = file_path.suffix.lower()
    if suffix == '.doc':
        return extract_text_from_doc(file_path)
    elif suffix == '.docx':
        return extract_text_from_docx(file_path)
    else:
        print(f"  Warning: Unknown file type: {suffix}")
        return None


def extract_roles_from_text(text: str, source_file: str) -> list[dict]:
    """
    Extract role assignments from diary text using regex patterns.

    Args:
        text: Diary text content
        source_file: Source filename for citation

    Returns:
        List of extraction dictionaries
    """
    extractions = []

    for pattern, role_type, group_idx in ROLE_PATTERNS:
        matches = re.finditer(pattern, text, re.IGNORECASE | re.MULTILINE)
        for match in matches:
            person_name = match.group(group_idx).strip()
            # Clean up the extracted name
            person_name = re.sub(r'\s+', ' ', person_name)  # Normalise whitespace
            person_name = person_name.strip(' ,|&')  # Remove trailing punctuation

            if person_name and len(person_name) > 1:  # Skip single characters
                extractions.append({
                    'role_type': role_type,
                    'person_name': person_name,
                    'source_file': source_file,
                    'match_context': match.group(0)[:100].replace('\n', ' '),
                    'confidence': 'high',  # Regex matches are explicit
                })

    return extractions


def process_diary_files() -> list[dict]:
    """
    Process all diary files and extract role information.

    Returns:
        List of all extractions across all files
    """
    all_extractions = []
    files_processed = 0
    files_with_extractions = 0

    print("Processing diary files for role extraction...")
    print("=" * 60)

    for season_key, season_data in DIARY_LOCATIONS.items():
        print(f"\n{season_key.upper()}:")
        base_path = season_data['base']

        # Process team files
        for team, files in season_data.get('files', {}).items():
            for file_rel in files:
                file_path = base_path / file_rel
                print(f"  Processing: {file_path.name}...", end=' ')

                text = extract_text(file_path)
                if text:
                    extractions = extract_roles_from_text(text, file_path.name)
                    if extractions:
                        for ext in extractions:
                            ext['season'] = season_key
                            ext['team'] = team
                        all_extractions.extend(extractions)
                        files_with_extractions += 1
                        print(f"Found {len(extractions)} role mentions")
                    else:
                        print("No explicit role patterns found")
                    files_processed += 1
                else:
                    print("Could not read file")

        # Process supplemental files
        for supp_file in season_data.get('supplemental', []):
            if supp_file.exists():
                print(f"  Processing supplemental: {supp_file.name}...", end=' ')
                text = extract_text(supp_file)
                if text:
                    extractions = extract_roles_from_text(text, supp_file.name)
                    if extractions:
                        for ext in extractions:
                            ext['season'] = season_key
                            ext['team'] = 'SUPP'
                        all_extractions.extend(extractions)
                        files_with_extractions += 1
                        print(f"Found {len(extractions)} role mentions")
                    else:
                        print("No explicit role patterns found")
                    files_processed += 1
                else:
                    print("Could not read file")

    print("\n" + "=" * 60)
    print(f"Files processed: {files_processed}")
    print(f"Files with extractions: {files_with_extractions}")
    print(f"Total role mentions found: {len(all_extractions)}")

    return all_extractions


def write_extractions_csv(extractions: list[dict]) -> None:
    """
    Write extractions to CSV file.

    Args:
        extractions: List of extraction dictionaries
    """
    fieldnames = [
        'season', 'team', 'role_type', 'person_name',
        'source_file', 'match_context', 'confidence'
    ]

    OUTPUT_FILE.parent.mkdir(parents=True, exist_ok=True)

    with open(OUTPUT_FILE, 'w', encoding='utf-8', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(extractions)

    print(f"\nExtractions written to: {OUTPUT_FILE}")


def main():
    """Main entry point."""
    print("TRAP Role Extraction - Phase A: Automated Regex Pass")
    print(f"Started: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print()

    extractions = process_diary_files()

    if extractions:
        write_extractions_csv(extractions)

        # Summary by role type
        print("\nExtractions by role type:")
        role_counts = {}
        for ext in extractions:
            role = ext['role_type']
            role_counts[role] = role_counts.get(role, 0) + 1
        for role, count in sorted(role_counts.items()):
            print(f"  {role}: {count}")
    else:
        print("\nNo explicit role patterns found in any diary files.")
        print("This is expected - most diaries use narrative style.")
        print("Proceed to Phase B (manual NLP review) for comprehensive extraction.")


if __name__ == '__main__':
    main()
