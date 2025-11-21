#!/usr/bin/env python3
"""
Parse Bulgarian TRAP field diary text files from 2011.

Extracts date, team members, and roles from Bulgarian diaries.
"""

import re
import csv
from pathlib import Path
from datetime import datetime
from typing import List, Dict, Optional

OUTPUT_DIR = Path(__file__).parent.parent / "outputs"


def parse_team_d_2011_bulgarian(filepath: Path) -> List[Dict[str, str]]:
    """
    Parse Team D 2011 Bulgarian diary.

    Format:
        Ден 1: 14.10.2011 г. (петък)

        Екип:
        Н. Кечева, Ю. Димитрова, В. Генчева, Г. Михайлов, Е. Дакашев, А. Рисков,
        Христина Павкова

    Returns:
        List of CSV record dictionaries
    """
    records = []

    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    lines = content.split('\n')

    current_date = None
    looking_for_team = False
    team_lines = []

    for i, line in enumerate(lines):
        # Look for day header: "Ден 1: 14.10.2011 г. (петък)"
        match = re.search(r'Ден\s+\d+:\s+(\d{2})\.(\d{2})\.(\d{4})', line)
        if match:
            # Save previous entry if we have one
            if current_date and team_lines:
                team_text = ' '.join(team_lines)
                walkers = extract_bulgarian_names(team_text)
                if walkers:
                    records.append({
                        'Date': current_date,
                        'Team': 'D',
                        'Walkers': ' | '.join(walkers),
                        'Team_Leader': '',  # Not specified in Bulgarian diaries
                        'Author': '',
                        'PDF_Source': 'D_2011Diary_BG.doc',
                        'Extraction_Notes': 'Extracted from Bulgarian diary'
                    })

            # Start new entry
            day, month, year = match.groups()
            current_date = f"{year}-{month}-{day}"
            looking_for_team = True
            team_lines = []
            continue

        # Look for team section
        if looking_for_team and 'Екип:' in line:
            looking_for_team = False
            # Team members usually on next lines
            continue

        # Collect team member lines (after "Екип:" until we hit another section)
        if current_date and not looking_for_team and team_lines is not None:
            # Stop collecting if we hit a new section
            if re.search(r'^(Задача|Работа на терен|Регистрирани|Ден \d+):', line):
                # Process the team
                team_text = ' '.join(team_lines)
                walkers = extract_bulgarian_names(team_text)
                if walkers:
                    records.append({
                        'Date': current_date,
                        'Team': 'D',
                        'Walkers': ' | '.join(walkers),
                        'Team_Leader': '',
                        'Author': '',
                        'PDF_Source': 'D_2011Diary_BG.doc',
                        'Extraction_Notes': 'Extracted from Bulgarian diary'
                    })
                    current_date = None
                    team_lines = []

                # Re-process this line in case it's a new day
                if re.search(r'Ден\s+\d+:\s+(\d{2})\.(\d{2})\.(\d{4})', line):
                    match = re.search(r'Ден\s+\d+:\s+(\d{2})\.(\d{2})\.(\d{4})', line)
                    day, month, year = match.groups()
                    current_date = f"{year}-{month}-{day}"
                    looking_for_team = True
                continue

            # Collect non-empty lines
            if line.strip() and not line.strip().startswith('Ден '):
                team_lines.append(line.strip())

    # Don't forget the last entry
    if current_date and team_lines:
        team_text = ' '.join(team_lines)
        walkers = extract_bulgarian_names(team_text)
        if walkers:
            records.append({
                'Date': current_date,
                'Team': 'D',
                'Walkers': ' | '.join(walkers),
                'Team_Leader': '',
                'Author': '',
                'PDF_Source': 'D_2011Diary_BG.doc',
                'Extraction_Notes': 'Extracted from Bulgarian diary'
            })

    return records


def extract_bulgarian_names(text: str) -> List[str]:
    """
    Extract Bulgarian names from comma-separated text.

    Handles formats like:
    - "Н. Кечева, Ю. Димитрова, В. Генчева"
    - "Н. Кечева, Ю. Димитрова, В. Генчева, Г. Михайлов, Е. Дакашев"

    Returns:
        List of cleaned names
    """
    # Split by comma
    names = [name.strip() for name in text.split(',')]

    cleaned = []
    for name in names:
        if not name:
            continue

        # Clean up common patterns
        name = name.strip()

        # Remove punctuation at end
        name = name.rstrip('.')

        # Skip if too short or looks like a section header
        if len(name) < 3:
            continue

        # Skip section headers
        if any(keyword in name for keyword in ['Екип', 'Задача', 'Работа',
                                                 'Регистрирани', 'Ден']):
            continue

        cleaned.append(name)

    return cleaned


def parse_team_a_2011_bulgarian(filepath: Path) -> List[Dict[str, str]]:
    """
    Parse Team A 2011 Bulgarian diary.

    Returns:
        List of CSV record dictionaries
    """
    records = []

    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    lines = content.split('\n')

    current_date = None
    looking_for_team = False
    team_lines = []

    for i, line in enumerate(lines):
        # Look for date patterns - try multiple formats
        # Format 1: "Ден 1: 14.10.2011 г."
        match = re.search(r'(?:Ден\s+\d+:\s+)?(\d{2})\.(\d{2})\.(\d{4})', line)
        if match and len(line.strip()) < 50:  # Likely a date header, not body text
            # Save previous entry
            if current_date and team_lines:
                team_text = ' '.join(team_lines)
                walkers = extract_bulgarian_names(team_text)
                if walkers:
                    records.append({
                        'Date': current_date,
                        'Team': 'A',
                        'Walkers': ' | '.join(walkers),
                        'Team_Leader': '',
                        'Author': '',
                        'PDF_Source': 'A_2011Diary_BG.doc',
                        'Extraction_Notes': 'Extracted from Bulgarian diary'
                    })

            # Start new entry
            day, month, year = match.groups()
            current_date = f"{year}-{month}-{day}"
            looking_for_team = True
            team_lines = []
            continue

        # Look for team section
        if looking_for_team and 'Екип:' in line:
            looking_for_team = False
            continue

        # Collect team member lines
        if current_date and not looking_for_team and team_lines is not None:
            # Stop collecting if we hit a new section
            if re.search(r'^(Задача|Работа|Регистрирани|Ден \d+|\d{2}\.\d{2}\.\d{4}):', line):
                team_text = ' '.join(team_lines)
                walkers = extract_bulgarian_names(team_text)
                if walkers:
                    records.append({
                        'Date': current_date,
                        'Team': 'A',
                        'Walkers': ' | '.join(walkers),
                        'Team_Leader': '',
                        'Author': '',
                        'PDF_Source': 'A_2011Diary_BG.doc',
                        'Extraction_Notes': 'Extracted from Bulgarian diary'
                    })
                    current_date = None
                    team_lines = []
                continue

            # Collect non-empty lines
            if line.strip():
                team_lines.append(line.strip())

    # Last entry
    if current_date and team_lines:
        team_text = ' '.join(team_lines)
        walkers = extract_bulgarian_names(team_text)
        if walkers:
            records.append({
                'Date': current_date,
                'Team': 'A',
                'Walkers': ' | '.join(walkers),
                'Team_Leader': '',
                'Author': '',
                'PDF_Source': 'A_2011Diary_BG.doc',
                'Extraction_Notes': 'Extracted from Bulgarian diary'
            })

    return records


def parse_team_b_c_2011_bulgarian(filepath: Path, team: str, source: str) -> List[Dict[str, str]]:
    """
    Parse Team B or C 2011 Bulgarian diary.

    Args:
        filepath: Path to diary file
        team: 'B' or 'C'
        source: Source filename for attribution

    Returns:
        List of CSV record dictionaries
    """
    records = []

    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    lines = content.split('\n')

    current_date = None
    looking_for_team = False
    team_lines = []

    for i, line in enumerate(lines):
        # Look for date patterns
        match = re.search(r'(?:Ден\s+\d+:\s+)?(\d{2})\.(\d{2})\.(\d{4})', line)
        if match and len(line.strip()) < 50:
            # Save previous entry
            if current_date and team_lines:
                team_text = ' '.join(team_lines)
                walkers = extract_bulgarian_names(team_text)
                if walkers:
                    records.append({
                        'Date': current_date,
                        'Team': team,
                        'Walkers': ' | '.join(walkers),
                        'Team_Leader': '',
                        'Author': '',
                        'PDF_Source': source,
                        'Extraction_Notes': 'Extracted from Bulgarian diary'
                    })

            # Start new entry
            day, month, year = match.groups()
            current_date = f"{year}-{month}-{day}"
            looking_for_team = True
            team_lines = []
            continue

        # Look for team section
        if looking_for_team and ('Екип:' in line or 'Walkers:' in line):
            looking_for_team = False
            continue

        # Collect team member lines
        if current_date and not looking_for_team and team_lines is not None:
            if re.search(r'^(Задача|Работа|Регистрирани|Ден \d+|\d{2}\.\d{2}\.\d{4}):', line):
                team_text = ' '.join(team_lines)
                walkers = extract_bulgarian_names(team_text)
                if walkers:
                    records.append({
                        'Date': current_date,
                        'Team': team,
                        'Walkers': ' | '.join(walkers),
                        'Team_Leader': '',
                        'Author': '',
                        'PDF_Source': source,
                        'Extraction_Notes': 'Extracted from Bulgarian diary'
                    })
                    current_date = None
                    team_lines = []
                continue

            if line.strip():
                team_lines.append(line.strip())

    # Last entry
    if current_date and team_lines:
        team_text = ' '.join(team_lines)
        walkers = extract_bulgarian_names(team_text)
        if walkers:
            records.append({
                'Date': current_date,
                'Team': team,
                'Walkers': ' | '.join(walkers),
                'Team_Leader': '',
                'Author': '',
                'PDF_Source': source,
                'Extraction_Notes': 'Extracted from Bulgarian diary'
            })

    return records


def main():
    """Main execution function."""
    print("Parsing Bulgarian TRAP 2011 field diaries...")
    print()

    output_file = OUTPUT_DIR / "phase2b_pdf_walkers.csv"

    # Parse Team D 2011
    print("Parsing Team D 2011 Bulgarian diary...")
    team_d_records = parse_team_d_2011_bulgarian(Path("/tmp/team_d_2011_diary.txt"))
    print(f"  Extracted {len(team_d_records)} entries")

    # Parse Team A 2011
    print("Parsing Team A 2011 Bulgarian diary...")
    team_a_records = parse_team_a_2011_bulgarian(Path("/tmp/team_a_2011_bg.txt"))
    print(f"  Extracted {len(team_a_records)} entries")

    # Parse Team B 2011
    print("Parsing Team B 2011 Bulgarian diary...")
    team_b_records = parse_team_b_c_2011_bulgarian(
        Path("/tmp/team_b_2011_bg.txt"), 'B', 'B_2011Diary_BG.docx')
    print(f"  Extracted {len(team_b_records)} entries")

    # Parse Team C 2011
    print("Parsing Team C 2011 Bulgarian diary...")
    team_c_records = parse_team_b_c_2011_bulgarian(
        Path("/tmp/team_c_2011_bg.txt"), 'C', 'C_2011Diary_BG.docx')
    print(f"  Extracted {len(team_c_records)} entries")

    # Append all to CSV
    all_records = team_d_records + team_a_records + team_b_records + team_c_records

    if all_records:
        with open(output_file, 'a', encoding='utf-8', newline='') as f:
            fieldnames = ['Date', 'Team', 'Walkers', 'Team_Leader', 'Author',
                         'PDF_Source', 'Extraction_Notes']
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            writer.writerows(all_records)

    print()
    print(f"Total 2011 Bulgarian diary entries extracted: {len(all_records)}")
    print(f"Appended to: {output_file}")


if __name__ == "__main__":
    main()
