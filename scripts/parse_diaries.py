#!/usr/bin/env python3
"""
Parse TRAP field diary text files to extract walker information.

Extracts date, team members, and roles (Team Leader, Author, PDA Operator)
from diary entries and formats as CSV records for phase2b_pdf_walkers.csv.
"""

import re
import csv
from pathlib import Path
from datetime import datetime
from typing import List, Dict, Optional, Tuple

# Output directory
OUTPUT_DIR = Path(__file__).parent.parent / "outputs"

def parse_date_from_header(line: str, year: int) -> Optional[str]:
    """
    Parse date from diary entry header.

    Handles formats like:
    - "Monday 12 October"
    - "Thursday 22 October"
    - "Monday 2 November 2009"
    - "Monday 12th October"

    Args:
        line: Line potentially containing a date
        year: Year to use if not specified in line

    Returns:
        Date in YYYY-MM-DD format, or None if no date found
    """
    # Pattern for day names followed by date and month
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

    return None


def extract_names_from_list(text: str) -> List[str]:
    """
    Extract individual names from a comma/and-separated list.

    Handles formats like:
    - "Ilija, myself, Aneta, Martin and Eric"
    - "Scott, Vera, Shawn, Yabor, Stanislav"
    - "me, Ilija, Todor, Martin and Katarina"

    Args:
        text: Text containing name list

    Returns:
        List of cleaned names
    """
    # Replace 'and' with comma for consistent splitting
    text = re.sub(r'\s+and\s+', ', ', text)

    # Split by comma
    names = [name.strip() for name in text.split(',')]

    # Clean up common patterns
    cleaned = []
    for name in names:
        # Skip empty strings
        if not name:
            continue

        # Handle common variations
        name = name.strip()

        # Skip if too short (likely noise)
        if len(name) < 2:
            continue

        cleaned.append(name)

    return cleaned


def parse_team_a_2009_elhovo(filepath: Path) -> List[Dict[str, str]]:
    """
    Parse Team A 2009 Elhovo diary.

    Author: Adela Sobotkova (Team Leader)
    Format: Daily entries with team composition in various formats

    Returns:
        List of CSV record dictionaries
    """
    records = []

    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Split into lines for processing
    lines = content.split('\n')

    current_date = None
    current_team = []

    for i, line in enumerate(lines):
        # Try to parse date from line
        parsed_date = parse_date_from_header(line, 2009)
        if parsed_date:
            # Save previous entry if we have one
            if current_date and current_team:
                records.append({
                    'Date': current_date,
                    'Team': 'A',
                    'Walkers': ' | '.join(current_team),
                    'Team_Leader': 'Adela',
                    'Author': 'Adela',
                    'PDF_Source': 'Diary Team A.doc',
                    'Extraction_Notes': 'Extracted from Elhovo 2009 diary'
                })

            # Start new entry
            current_date = parsed_date
            current_team = []
            continue

        # Look for team composition patterns
        if current_date:
            # Pattern 1: "Team A holds the outer edge and comprises Ilija, myself, Aneta, Martin and Eric"
            match = re.search(r'comprises\s+([A-Za-z,\s]+(?:and\s+[A-Za-z]+)?)', line)
            if match:
                names = extract_names_from_list(match.group(1))
                # Replace "myself" with "Adela"
                names = ['Adela' if n.lower() in ['myself', 'me'] else n for n in names]
                if names:
                    current_team = names
                    continue

            # Pattern 2: "Team A continues in usual setup (Martin – GPS, Aneta- recording, me – PDA, ...)"
            match = re.search(r'\(([^)]+)\)', line)
            if match and ('GPS' in match.group(1) or 'recording' in match.group(1) or 'PDA' in match.group(1)):
                # Extract names with roles
                role_pattern = r'([A-Za-z]+)\s*[–-]\s*[A-Za-z]+'
                names = [m.group(1) for m in re.finditer(role_pattern, match.group(1))]
                names = ['Adela' if n.lower() in ['myself', 'me'] else n for n in names]
                if names:
                    current_team = names
                    continue

            # Pattern 3: "Team: Adela, Ilija, Eric, Aneta and Martin"
            match = re.search(r'Team[:\s]+([A-Za-z,\s]+(?:and\s+[A-Za-z]+)?)', line, re.IGNORECASE)
            if match:
                names = extract_names_from_list(match.group(1))
                names = ['Adela' if n.lower() in ['myself', 'me'] else n for n in names]
                if names:
                    current_team = names
                    continue

            # Pattern 4: "Team A (new incarnation of me, Ilija, Todor, Martin and Katarina)"
            match = re.search(r'Team A \([^)]*of\s+([A-Za-z,\s]+(?:and\s+[A-Za-z]+)?)\)', line)
            if match:
                names = extract_names_from_list(match.group(1))
                names = ['Adela' if n.lower() in ['myself', 'me'] else n for n in names]
                if names:
                    current_team = names
                    continue

    # Don't forget the last entry
    if current_date and current_team:
        records.append({
            'Date': current_date,
            'Team': 'A',
            'Walkers': ' | '.join(current_team),
            'Team_Leader': 'Adela',
            'Author': 'Adela',
            'PDF_Source': 'Diary Team A.doc',
            'Extraction_Notes': 'Extracted from Elhovo 2009 diary'
        })

    return records


def parse_team_b_2009_elhovo(filepath: Path) -> List[Dict[str, str]]:
    """
    Parse Team B 2009 Elhovo diary.

    Author: Shawn Ross (Team Leader)
    Format: Very consistent "X walkers: Name1, Name2, ..." format

    Returns:
        List of CSV record dictionaries
    """
    records = []

    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    lines = content.split('\n')

    current_date = None

    for line in lines:
        # Try to parse date from line
        parsed_date = parse_date_from_header(line, 2009)
        if parsed_date:
            current_date = parsed_date
            continue

        # Look for walker list pattern: "Five walkers: Scott, Vera, Shawn, Yabor, Stanislav"
        if current_date:
            match = re.search(r'(\w+)\s+walkers?:\s+([A-Za-z,\s]+)', line)
            if match:
                count, names_str = match.groups()
                names = extract_names_from_list(names_str)

                if names:
                    records.append({
                        'Date': current_date,
                        'Team': 'B',
                        'Walkers': ' | '.join(names),
                        'Team_Leader': 'Shawn',
                        'Author': 'Shawn',
                        'PDF_Source': 'Diary Team B.doc',
                        'Extraction_Notes': f'Extracted from Elhovo 2009 diary ({count} walkers)'
                    })
                    # Reset current_date after successful extraction
                    current_date = None

    return records


def parse_team_c_2009_elhovo(filepath: Path) -> List[Dict[str, str]]:
    """
    Parse Team C 2009 Elhovo diary.

    Authors: Multiple (Bara, Petra, Sona, Scott)
    Format: Header roster + evolving team composition in entries

    Returns:
        List of CSV record dictionaries
    """
    records = []

    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    lines = content.split('\n')

    # Default team from header
    default_team = ['Bara', 'Petra', 'Sona', 'Tereza', 'Todor', 'Georgi']
    default_leader = 'Bara'

    current_date = None

    for line in lines:
        # Try to parse date from line
        parsed_date = parse_date_from_header(line, 2009)
        if parsed_date:
            current_date = parsed_date
            continue

        # Look for explicit walker list: "Walkers: Scott (leader), Stanislav, Jarka, Radko, Javor"
        if current_date:
            match = re.search(r'Walkers?:\s+([A-Za-z,\s()]+)', line)
            if match:
                names_str = match.group(1)

                # Extract leader if specified
                leader_match = re.search(r'(\w+)\s*\(leader\)', names_str)
                leader = leader_match.group(1) if leader_match else default_leader

                # Remove role annotations
                names_str = re.sub(r'\s*\([^)]+\)', '', names_str)

                names = extract_names_from_list(names_str)

                if names:
                    records.append({
                        'Date': current_date,
                        'Team': 'C',
                        'Walkers': ' | '.join(names),
                        'Team_Leader': leader,
                        'Author': '',  # Multiple authors
                        'PDF_Source': 'Diary Team C.doc',
                        'Extraction_Notes': 'Extracted from Elhovo 2009 diary'
                    })
                    # Reset current_date after successful extraction
                    current_date = None

    return records


def append_to_csv(records: List[Dict[str, str]], output_file: Path):
    """
    Append records to phase2b_pdf_walkers.csv.

    Args:
        records: List of record dictionaries
        output_file: Path to output CSV file
    """
    if not records:
        return

    # Check if file exists to determine if we need to write header
    file_exists = output_file.exists()

    with open(output_file, 'a', encoding='utf-8', newline='') as f:
        fieldnames = ['Date', 'Team', 'Walkers', 'Team_Leader', 'Author',
                     'PDF_Source', 'Extraction_Notes']
        writer = csv.DictWriter(f, fieldnames=fieldnames)

        # Write header only if file is new
        if not file_exists:
            writer.writeheader()

        writer.writerows(records)


def main():
    """Main execution function."""
    print("Parsing TRAP field diaries for walker information...")
    print()

    output_file = OUTPUT_DIR / "phase2b_pdf_walkers.csv"

    # Parse Team A 2009 Elhovo
    print("Parsing Team A 2009 Elhovo diary...")
    team_a_records = parse_team_a_2009_elhovo(Path("/tmp/team_a_2009_elhovo.txt"))
    print(f"  Extracted {len(team_a_records)} entries")
    append_to_csv(team_a_records, output_file)

    # Parse Team B 2009 Elhovo
    print("Parsing Team B 2009 Elhovo diary...")
    team_b_records = parse_team_b_2009_elhovo(Path("/tmp/team_b_2009_elhovo.txt"))
    print(f"  Extracted {len(team_b_records)} entries")
    append_to_csv(team_b_records, output_file)

    # Parse Team C 2009 Elhovo
    print("Parsing Team C 2009 Elhovo diary...")
    team_c_records = parse_team_c_2009_elhovo(Path("/tmp/team_c_2009_elhovo.txt"))
    print(f"  Extracted {len(team_c_records)} entries")
    append_to_csv(team_c_records, output_file)

    print()
    print(f"Total diary entries extracted: {len(team_a_records) + len(team_b_records) + len(team_c_records)}")
    print(f"Appended to: {output_file}")


if __name__ == "__main__":
    main()
