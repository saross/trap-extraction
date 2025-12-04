#!/usr/bin/env python3
"""
Improved parser for Team C 2009 Elhovo diary.

Handles implicit team composition (uses header default unless changed).
"""

import re
import csv
from pathlib import Path
from datetime import datetime
from typing import List, Dict, Optional

OUTPUT_DIR = Path(__file__).parent.parent / "outputs"


def parse_date_from_header(line: str, year: int) -> Optional[str]:
    """Parse date from diary entry header."""
    pattern = r'(Monday|Tuesday|Wednesday|Thursday|Friday|Saturday|Sunday)\s+(\d{1,2})(?:st|nd|rd|th)?\s+(January|February|March|April|May|June|July|August|September|October|November|December)(?:\s+(\d{4}))?'

    match = re.search(pattern, line, re.IGNORECASE)
    if match:
        day_name, day, month_name, found_year = match.groups()
        year_to_use = int(found_year) if found_year else year

        try:
            date_obj = datetime.strptime(f"{day} {month_name} {year_to_use}", "%d %B %Y")
            return date_obj.strftime("%Y-%m-%d")
        except ValueError:
            return None

    # Also handle format like "Thursday 29.October"
    pattern2 = r'(Monday|Tuesday|Wednesday|Thursday|Friday|Saturday|Sunday)\s+(\d{1,2})\.(January|February|March|April|May|June|July|August|September|October|November|December)'
    match = re.search(pattern2, line, re.IGNORECASE)
    if match:
        day_name, day, month_name = match.groups()
        try:
            date_obj = datetime.strptime(f"{day} {month_name} {year}", "%d %B %Y")
            return date_obj.strftime("%Y-%m-%d")
        except ValueError:
            return None

    return None


def extract_names_from_list(text: str) -> List[str]:
    """Extract individual names from a comma/and-separated list."""
    # Replace 'and' with comma for consistent splitting
    text = re.sub(r'\s+and\s+', ', ', text)

    # Split by comma
    names = [name.strip() for name in text.split(',')]

    # Clean up
    cleaned = []
    for name in names:
        if not name or len(name) < 2:
            continue
        cleaned.append(name)

    return cleaned


def parse_team_c_2009_elhovo_improved(filepath: Path) -> List[Dict[str, str]]:
    """
    Parse Team C 2009 Elhovo diary with implicit team tracking.

    Returns:
        List of CSV record dictionaries
    """
    records = []

    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    lines = content.split('\n')

    # Default team from header
    current_team = ['Bara', 'Petra', 'Sona', 'Tereza', 'Todor', 'Georgi']
    current_leader = 'Bara'
    current_author = ''

    current_date = None
    date_has_survey = True  # Assume yes unless we see "didn't walk"

    for i, line in enumerate(lines):
        # Parse date
        parsed_date = parse_date_from_header(line, 2009)
        if parsed_date:
            # Save previous entry if valid
            if current_date and date_has_survey and current_team:
                records.append({
                    'Date': current_date,
                    'Team': 'C',
                    'Walkers': ' | '.join(current_team),
                    'Team_Leader': current_leader,
                    'Author': current_author,
                    'PDF_Source': 'Diary Team C.doc',
                    'Extraction_Notes': 'Extracted from Elhovo 2009 diary'
                })

            # Start new entry
            current_date = parsed_date
            date_has_survey = True  # Reset assumption
            continue

        # Check for no survey day
        if current_date and re.search(r"didn't walk|didn'?t walk|no walk|not walk", line, re.IGNORECASE):
            date_has_survey = False
            continue

        # Check for explicit walker list
        match = re.search(r'Walkers?:\s*\n?\s*([A-Za-z,\s()]+)', line + '\n' + (lines[i+1] if i+1 < len(lines) else ''))
        if match:
            names_str = match.group(1)

            # Extract leader if specified
            leader_match = re.search(r'(\w+)\s*\(leader\)', names_str)
            if leader_match:
                current_leader = leader_match.group(1)

            # Remove role annotations
            names_str = re.sub(r'\s*\([^)]+\)', '', names_str)

            names = extract_names_from_list(names_str)
            if names:
                current_team = names

        # Check for team changes mentioned in text
        # Example: "Since today we are missing Tereza"
        if re.search(r'missing Tereza', line):
            if 'Tereza' in current_team:
                current_team.remove('Tereza')

        # Check for author attribution
        # Example: "Petra is in charge of diary now"
        match = re.search(r'(\w+) is in charge of diary', line)
        if match:
            current_author = match.group(1)

    # Don't forget the last entry
    if current_date and date_has_survey and current_team:
        records.append({
            'Date': current_date,
            'Team': 'C',
            'Walkers': ' | '.join(current_team),
            'Team_Leader': current_leader,
            'Author': current_author,
            'PDF_Source': 'Diary Team C.doc',
            'Extraction_Notes': 'Extracted from Elhovo 2009 diary'
        })

    return records


def main():
    """Main execution function."""
    print("Parsing Team C 2009 Elhovo diary (improved)...")

    records = parse_team_c_2009_elhovo_improved(Path("/tmp/team_c_2009_elhovo.txt"))

    print(f"Extracted {len(records)} entries")
    print()

    # Display first few for verification
    for i, record in enumerate(records[:5]):
        print(f"{i+1}. {record['Date']} - Team: {record['Walkers'][:50]}...")

    if len(records) > 5:
        print(f"... and {len(records) - 5} more entries")

    # Write to separate file for review
    output_file = OUTPUT_DIR / "team_c_2009_diary_parsed.csv"
    with open(output_file, 'w', encoding='utf-8', newline='') as f:
        fieldnames = ['Date', 'Team', 'Walkers', 'Team_Leader', 'Author',
                     'PDF_Source', 'Extraction_Notes']
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(records)

    print(f"\nSaved to: {output_file}")


if __name__ == "__main__":
    main()
