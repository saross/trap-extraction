#!/usr/bin/env python3
"""
Parse Team A 2011 Bulgarian diary with narrative team composition.

Team A format embeds team members in narrative text rather than a separate section.
"""

import re
import csv
from pathlib import Path
from datetime import datetime
from typing import List, Dict, Optional

OUTPUT_DIR = Path(__file__).parent.parent / "outputs"


def extract_bulgarian_names(text: str) -> List[str]:
    """Extract Bulgarian names from comma-separated text."""
    # Split by comma
    names = [name.strip() for name in text.split(',')]

    cleaned = []
    for name in names:
        if not name:
            continue

        name = name.strip()

        # Skip if too short
        if len(name) < 2:
            continue

        # Skip section headers
        if any(keyword in name for keyword in ['Екип', 'Задача', 'Работа',
                                                 'Регистрирани', 'Ден', 'Група']):
            continue

        cleaned.append(name)

    return cleaned


def parse_team_a_2011_bulgarian(filepath: Path) -> List[Dict[str, str]]:
    """
    Parse Team A 2011 Bulgarian diary.

    Format:
        16.10.2011 г., неделя

        Група от 4 човека в състав ЮЦ, ЦЦ, ЮД, Г. Михайлов обхожда...

    Team composition persists across days until a new team is mentioned.

    Returns:
        List of CSV record dictionaries
    """
    records = []

    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    lines = content.split('\n')

    current_date = None
    current_team = []
    persistent_team = []  # Team carries over to next days
    is_survey_day = True

    for i, line in enumerate(lines):
        # Look for date header: "16.10.2011 г., неделя"
        match = re.search(r'^(\d{2})\.(\d{2})\.(\d{4})\s+г\.', line)
        if match:
            # Save previous entry
            if current_date and is_survey_day and current_team:
                records.append({
                    'Date': current_date,
                    'Team': 'A',
                    'Walkers': ' | '.join(current_team),
                    'Team_Leader': '',
                    'Author': '',
                    'PDF_Source': 'A_2011Diary_BG.doc',
                    'Extraction_Notes': 'Extracted from Bulgarian diary'
                })

            # Start new entry
            day, month, year = match.groups()
            current_date = f"{year}-{month}-{day}"

            # Inherit previous team unless we find a new one
            current_team = persistent_team.copy()
            is_survey_day = True  # Assume survey day unless proven otherwise
            continue

        # Check for "no survey" days FIRST
        if current_date and re.search(r'Дъждовен ден|работа в базата', line, re.IGNORECASE):
            is_survey_day = False
            current_date = None  # Skip this date entirely
            continue

        # Look for team composition in narrative:
        # "Група от 4 човека в състав ЮЦ, ЦЦ, ЮД, Г. Михайлов"
        if current_date:
            match = re.search(r'Група\s+от\s+\d+\s+човека\s+в\s+състав\s+(.+?)\s+(?:обхожда|продължава|започва)', line)
            if match:
                team_text = match.group(1).strip()
                walkers = extract_bulgarian_names(team_text)
                if walkers:
                    current_team = walkers
                    persistent_team = walkers  # Update persistent team
                continue

            # Alternative pattern: "в състав [names] обхожда"
            match = re.search(r'в\s+състав\s+(.+?)\s+(?:обхожда|продължава)', line)
            if match:
                team_text = match.group(1).strip()
                walkers = extract_bulgarian_names(team_text)
                if walkers:
                    current_team = walkers
                    persistent_team = walkers  # Update persistent team
                continue

    # Don't forget the last entry
    if current_date and is_survey_day and current_team:
        records.append({
            'Date': current_date,
            'Team': 'A',
            'Walkers': ' | '.join(current_team),
            'Team_Leader': '',
            'Author': '',
            'PDF_Source': 'A_2011Diary_BG.doc',
            'Extraction_Notes': 'Extracted from Bulgarian diary'
        })

    return records


def main():
    """Main execution function."""
    print("Parsing Team A 2011 Bulgarian diary...")

    records = parse_team_a_2011_bulgarian(Path("/tmp/team_a_2011_bg.txt"))

    print(f"Extracted {len(records)} entries")
    print()

    # Display entries for verification
    for i, record in enumerate(records[:10]):
        print(f"{i+1}. {record['Date']} - {record['Walkers'][:60]}...")

    if len(records) > 10:
        print(f"... and {len(records) - 10} more entries")

    # Append to main CSV
    output_file = OUTPUT_DIR / "phase2b_pdf_walkers.csv"

    if records:
        with open(output_file, 'a', encoding='utf-8', newline='') as f:
            fieldnames = ['Date', 'Team', 'Walkers', 'Team_Leader', 'Author',
                         'PDF_Source', 'Extraction_Notes']
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            writer.writerows(records)

        print(f"\nAppended to: {output_file}")


if __name__ == "__main__":
    main()
