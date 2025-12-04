#!/usr/bin/env python3
"""
Extract walker data from diary sources for 22 XLS-only records.

This script extracts walker and role data from primary diary sources for records
that currently lack walker information. It handles multiple diary formats:
- EN narrative (Elhovo 2009)
- EN structured with roles (Kazanlak/Yambol 2010)
- BG structured (Kazanlak 2010-2011)

The script includes Bulgarian to Latin transliteration matching existing patterns
in attribution.csv.

Author: Claude Code collaboration
Date: 2025-11-22
"""

import csv
import re
import subprocess
import zipfile
from pathlib import Path
from typing import Dict, List, Optional, Tuple
from datetime import datetime
import shutil

# Paths
BASE_PATH = Path("/media/shawn/191c3b96-5fa5-4d0d-8805-0cf05d3d8468/synology/Adela/TRAP-WD-2020-04")
ATTRIBUTION_PATH = Path("outputs/attribution.csv")
ATTRIBUTION_BACKUP = Path("outputs/attribution.csv.backup_diary_extraction")
NAME_MAPPING_PATH = Path("outputs/name-mapping.csv")
REPORT_PATH = Path("outputs/diary-extraction-report.md")

# Bulgarian to Latin transliteration mapping (matching existing patterns in attribution.csv)
TRANSLITERATION_MAP = {
    # Cyrillic uppercase
    'А': 'A', 'Б': 'B', 'В': 'V', 'Г': 'G', 'Д': 'D', 'Е': 'E', 'Ж': 'Zh',
    'З': 'Z', 'И': 'I', 'Й': 'Y', 'К': 'K', 'Л': 'L', 'М': 'M', 'Н': 'N',
    'О': 'O', 'П': 'P', 'Р': 'R', 'С': 'S', 'Т': 'T', 'У': 'U', 'Ф': 'F',
    'Х': 'Kh', 'Ц': 'Ts', 'Ч': 'Ch', 'Ш': 'Sh', 'Щ': 'Sht', 'Ъ': 'A', 'Ь': 'Y',
    'Ю': 'Yu', 'Я': 'Ya',
    # Cyrillic lowercase
    'а': 'a', 'б': 'b', 'в': 'v', 'г': 'g', 'д': 'd', 'е': 'e', 'ж': 'zh',
    'з': 'z', 'и': 'i', 'й': 'y', 'к': 'k', 'л': 'l', 'м': 'm', 'н': 'n',
    'о': 'o', 'п': 'p', 'р': 'r', 'с': 's', 'т': 't', 'у': 'u', 'ф': 'f',
    'х': 'kh', 'ц': 'ts', 'ч': 'ch', 'ш': 'sh', 'щ': 'sht', 'ъ': 'a', 'ь': 'y',
    'ю': 'yu', 'я': 'ya',
}

# 22 XLS-only records to process (from diary-extraction-plan.md)
RECORDS_TO_PROCESS = [
    # Elhovo 2009 Autumn (3 records)
    {"date": "2009-10-23", "team": "C", "source": "The Diary of Team C.doc", "format": "narrative_en"},
    {"date": "2009-11-09", "team": "A", "source": "Diary Team A.doc", "format": "narrative_en"},
    {"date": "2009-11-14", "team": "A", "source": "Diary Team A.doc", "format": "narrative_en"},

    # Kazanlak 2010 Spring (12 records)
    {"date": "2010-03-08", "team": "C", "source": "C_2010Diary_BG.doc", "format": "structured_bg"},
    {"date": "2010-03-21", "team": "D", "source": "D_2010Diary_BG.doc", "format": "structured_bg"},
    {"date": "2010-03-24", "team": "C", "source": "C_2010Diary_BG.doc", "format": "structured_bg"},
    {"date": "2010-03-25", "team": "C", "source": "C_2010Diary_BG.doc", "format": "structured_bg"},
    {"date": "2010-03-25", "team": "D", "source": "D_2010Diary_BG.doc", "format": "structured_bg"},
    {"date": "2010-04-02", "team": "B", "source": "B_2010Diary_En.doc", "format": "structured_en_roles"},
    {"date": "2010-04-06", "team": "B", "source": "B_2010Diary_En.doc", "format": "structured_en_roles"},
    {"date": "2010-04-07", "team": "A", "source": "A_2010Diary_BG.doc", "format": "structured_bg"},
    {"date": "2010-04-07", "team": "B", "source": "B_2010Diary_En.doc", "format": "structured_en_roles"},
    {"date": "2010-04-07", "team": "C", "source": "C_2010Diary_BG.doc", "format": "structured_bg"},
    {"date": "2010-04-08", "team": "A", "source": "A_2010Diary_BG.doc", "format": "structured_bg"},
    {"date": "2010-04-08", "team": "B", "source": "B_2010Diary_En.doc", "format": "structured_en_roles"},

    # Yambol 2010 Autumn (1 record)
    {"date": "2010-11-14", "team": "B", "source": "Team B Diary.docx", "format": "structured_en_roles"},

    # Kazanlak 2011 Autumn (6 records)
    {"date": "2011-10-24", "team": "A", "source": "A_2011Diary_BG.doc", "format": "structured_bg"},
    {"date": "2011-11-01", "team": "D", "source": "D_2011Diary_BG.doc", "format": "structured_bg"},
    {"date": "2011-11-02", "team": "D", "source": "D_2011Diary_BG.doc", "format": "structured_bg"},
    {"date": "2011-11-08", "team": "B", "source": "B_2011Diary_En.docx", "format": "structured_en"},
    {"date": "2011-11-10", "team": "D", "source": "D_2011Diary_BG.doc", "format": "structured_bg"},
    {"date": "2011-11-29", "team": "B", "source": "B_2011Diary_En.docx", "format": "structured_en"},
]


def transliterate_bulgarian(text: str) -> str:
    """
    Transliterate Bulgarian Cyrillic text to Latin alphabet.

    Matches existing patterns in attribution.csv:
    - Г. Нехризов → G. Nekhrizov
    - Ю. Цветкова → Yu. Tzvetkova

    Args:
        text: Bulgarian text in Cyrillic

    Returns:
        Transliterated text in Latin alphabet
    """
    result = []
    for char in text:
        result.append(TRANSLITERATION_MAP.get(char, char))
    return ''.join(result)


def extract_text_from_doc(filepath: Path) -> str:
    """
    Extract text from .doc file using antiword.

    Args:
        filepath: Path to .doc file

    Returns:
        Extracted text content
    """
    try:
        result = subprocess.run(
            ['antiword', str(filepath)],
            capture_output=True,
            text=True,
            check=True
        )
        return result.stdout
    except subprocess.CalledProcessError as e:
        print(f"Error extracting {filepath}: {e}")
        return ""


def extract_text_from_docx(filepath: Path) -> str:
    """
    Extract text from .docx file using python-docx or unzip method.

    Args:
        filepath: Path to .docx file

    Returns:
        Extracted text content
    """
    try:
        # Try using python-docx first
        try:
            from docx import Document
            doc = Document(filepath)
            return '\n'.join([para.text for para in doc.paragraphs])
        except ImportError:
            # Fallback to unzip method
            with zipfile.ZipFile(filepath, 'r') as docx:
                xml_content = docx.read('word/document.xml')
                # Simple XML text extraction (not perfect but workable)
                text = re.sub(r'<[^>]+>', ' ', xml_content.decode('utf-8'))
                return text
    except Exception as e:
        print(f"Error extracting {filepath}: {e}")
        return ""


def get_diary_path(record: Dict[str, str]) -> Path:
    """
    Get the full path to the diary file for a record.

    Args:
        record: Record dictionary with date, team, source fields

    Returns:
        Full path to diary file
    """
    date = record['date']
    team = record['team']
    source = record['source']

    year = int(date.split('-')[0])

    # Determine season folder
    if '2009' in date:
        if '10-' in date or '11-' in date:
            season_folder = "Elhovo 2010-12-12/2009"
        else:
            season_folder = "Kazanluk/2009"
    elif '2010' in date:
        if date < "2010-10-01":
            # Spring 2010
            season_folder = "Kazanluk/2010"
        else:
            # Autumn 2010
            season_folder = "Elhovo 2010-12-12/2010"
    elif '2011' in date:
        season_folder = "Kazanluk/2011-11-30"
    else:
        raise ValueError(f"Unknown date: {date}")

    # Build path to diary
    if "Elhovo" in season_folder:
        if "Team A" in source or "Team C" in source or "Team B Diary" in source:
            team_folder = f"Project Records/Team {team}"
        else:
            team_folder = f"Project Records/Team {team}"
    else:
        # Kazanlak
        if '2009' in date:
            team_folder = f"Project Records/Team{team}"
        else:
            team_folder = f"Project Records/Team {team}"

    full_path = BASE_PATH / season_folder / team_folder / source

    return full_path


def parse_date_variations(date_str: str, year: int) -> Optional[str]:
    """
    Parse various date formats found in diaries.

    Handles:
    - dd.mm.yyyy (Bulgarian format)
    - d Month yyyy
    - Month d, yyyy

    Args:
        date_str: Date string to parse
        year: Default year if not in string

    Returns:
        Date in YYYY-MM-DD format or None
    """
    # Try Bulgarian format: dd.mm.yyyy or dd.mm.yy
    match = re.search(r'(\d{1,2})\.(\d{1,2})\.(\d{2,4})', date_str)
    if match:
        day, month, year_str = match.groups()
        if len(year_str) == 2:
            year_str = f"20{year_str}"
        try:
            return f"{year_str}-{int(month):02d}-{int(day):02d}"
        except ValueError:
            pass

    # Try English formats
    months = {
        'january': 1, 'february': 2, 'march': 3, 'april': 4,
        'may': 5, 'june': 6, 'july': 7, 'august': 8,
        'september': 9, 'october': 10, 'november': 11, 'december': 12
    }

    for month_name, month_num in months.items():
        pattern = rf'(\d{{1,2}})\s+{month_name}(?:\s+(\d{{4}}))?'
        match = re.search(pattern, date_str, re.IGNORECASE)
        if match:
            day, found_year = match.groups()
            year_to_use = int(found_year) if found_year else year
            return f"{year_to_use}-{month_num:02d}-{int(day):02d}"

    return None


def extract_walkers_narrative_en(text: str, target_date: str) -> Tuple[Optional[str], Dict[str, str]]:
    """
    Extract walkers from English narrative format (Elhovo 2009).

    Looks for patterns like:
    - "Team X contains [names]"
    - "The team: [names]"
    - "Team members: [names]"

    Args:
        text: Diary text content
        target_date: Date to find entry for (YYYY-MM-DD)

    Returns:
        Tuple of (walkers_pipe_delimited, roles_dict)
    """
    year = int(target_date.split('-')[0])
    lines = text.split('\n')

    # Find date entry
    in_target_entry = False
    entry_lines = []

    for i, line in enumerate(lines):
        date_found = parse_date_variations(line, year)
        if date_found == target_date:
            in_target_entry = True
            entry_lines = []
        elif in_target_entry and date_found:
            # Hit next date entry, stop
            break
        elif in_target_entry:
            entry_lines.append(line)

    if not entry_lines:
        return None, {}

    entry_text = '\n'.join(entry_lines)

    # Extract team members
    patterns = [
        r'[Tt]eam\s+[A-Z]\s+contains?\s+(?:the\s+)?(?:usual\s+)?(?:troops?\s+[-–]\s+)?([^.]+)',
        r'[Tt]he\s+team:\s*([^.]+)',
        r'[Tt]eam\s+members?:\s*([^.]+)',
        r'[Ww]alkers?:\s*([^.]+)',
        r'[Tt]oday[\'s]*\s+team:\s*([^.]+)',
    ]

    for pattern in patterns:
        match = re.search(pattern, entry_text, re.IGNORECASE)
        if match:
            names_str = match.group(1).strip()
            # Split by comma and 'and'
            names_str = re.sub(r'\s+and\s+', ', ', names_str)
            names = [n.strip() for n in names_str.split(',') if n.strip()]

            # Filter out noise words and pronouns
            noise = ['myself', 'me', 'the', 'a', 'an', 'i']
            names = [n for n in names if n.lower() not in noise and len(n) > 1]

            if names:
                return ' | '.join(names), {}

    return None, {}


def extract_walkers_structured_bg(text: str, target_date: str) -> Tuple[Optional[str], Dict[str, str]]:
    """
    Extract walkers from Bulgarian structured format (Kazanlak 2010-2011).

    Looks for patterns like:
    - "Група: [names]"
    - "Екип: [names]"
    - Numbered lists: "1. Name, 2. Name"

    Args:
        text: Diary text content
        target_date: Date to find entry for (YYYY-MM-DD)

    Returns:
        Tuple of (walkers_pipe_delimited, roles_dict)
    """
    year = int(target_date.split('-')[0])
    lines = text.split('\n')

    # Find date entry
    in_target_entry = False
    entry_lines = []

    for i, line in enumerate(lines):
        date_found = parse_date_variations(line, year)
        if date_found == target_date:
            in_target_entry = True
            entry_lines = []
        elif in_target_entry and date_found:
            break
        elif in_target_entry:
            entry_lines.append(line)

    if not entry_lines:
        return None, {}

    entry_text = '\n'.join(entry_lines)

    # Extract team members (Bulgarian patterns)
    patterns = [
        r'Група:\s*([^\n]+)',
        r'Екип:\s*([^\n]+)',
        r'Участници:\s*([^\n]+)',
    ]

    for pattern in patterns:
        match = re.search(pattern, entry_text, re.IGNORECASE)
        if match:
            names_str = match.group(1).strip()
            # Split by comma
            names = [n.strip() for n in names_str.split(',') if n.strip()]

            if names:
                # Transliterate Bulgarian names
                names_latin = [transliterate_bulgarian(n) for n in names]
                return ' | '.join(names_latin), {}

    return None, {}


def extract_walkers_structured_en(text: str, target_date: str, with_roles: bool = False) -> Tuple[Optional[str], Dict[str, str]]:
    """
    Extract walkers from English structured format (Kazanlak/Yambol 2010-2011).

    Looks for patterns like:
    - "Walkers: [names]"
    - "Team: [names]"
    - "PDA: name, GPS: name, Forms: name"

    Args:
        text: Diary text content
        target_date: Date to find entry for (YYYY-MM-DD)
        with_roles: If True, also extract role assignments

    Returns:
        Tuple of (walkers_pipe_delimited, roles_dict)
    """
    year = int(target_date.split('-')[0])
    lines = text.split('\n')

    # Find date entry
    in_target_entry = False
    entry_lines = []

    for i, line in enumerate(lines):
        date_found = parse_date_variations(line, year)
        if date_found == target_date:
            in_target_entry = True
            entry_lines = []
        elif in_target_entry and date_found:
            break
        elif in_target_entry:
            entry_lines.append(line)

    if not entry_lines:
        return None, {}

    entry_text = '\n'.join(entry_lines)

    # Extract team members
    patterns = [
        r'[Nn]o\.\s+of\s+walkers?:\s*\d+\s*[-–]\s*([^\n]+)',
        r'[Ww]alkers?:\s*([^\n]+)',
        r'[Tt]eam:\s*([^\n]+)',
        r'[Mm]embers?:\s*([^\n]+)',
    ]

    walkers = None
    for pattern in patterns:
        match = re.search(pattern, entry_text, re.IGNORECASE)
        if match:
            names_str = match.group(1).strip()
            # Remove any leading count patterns like "6 –"
            names_str = re.sub(r'^\d+\s*[-–]\s*', '', names_str)
            # Split by comma and 'and'
            names_str = re.sub(r'\s+and\s+', ', ', names_str)
            names = [n.strip() for n in names_str.split(',') if n.strip()]

            if names:
                walkers = ' | '.join(names)
                break

    # Extract roles if requested
    roles = {}
    if with_roles:
        role_patterns = {
            'PDA_Operator': r'PDA:\s*([^,\n]+)',
            'GPS_Operator': r'GPS:\s*([^,\n]+)',
            'Paper_Recorder': r'(?:Forms?|Paper):\s*([^,\n]+)',
        }

        for role_key, pattern in role_patterns.items():
            match = re.search(pattern, entry_text, re.IGNORECASE)
            if match:
                roles[role_key] = match.group(1).strip()

    return walkers, roles


def load_name_mapping() -> Dict[str, str]:
    """
    Load name-mapping.csv to expand initials.

    Returns:
        Dictionary mapping initials to full names
    """
    mapping = {}
    try:
        with open(NAME_MAPPING_PATH, 'r', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            for row in reader:
                extracted = row['extracted_name']
                canonical = row['canonical_name']
                if canonical and len(extracted) <= 4:  # Likely initials
                    mapping[extracted] = canonical
    except FileNotFoundError:
        pass

    return mapping


def extract_walkers_for_record(record: Dict[str, str]) -> Tuple[Optional[str], Dict[str, str], str]:
    """
    Extract walker data for a single record.

    Args:
        record: Record dictionary from RECORDS_TO_PROCESS

    Returns:
        Tuple of (walkers_pipe_delimited, roles_dict, notes)
    """
    diary_path = get_diary_path(record)

    if not diary_path.exists():
        return None, {}, f"Diary not found: {diary_path}"

    # Extract text
    if diary_path.suffix == '.doc':
        text = extract_text_from_doc(diary_path)
    elif diary_path.suffix == '.docx':
        text = extract_text_from_docx(diary_path)
    else:
        return None, {}, f"Unknown file type: {diary_path.suffix}"

    if not text:
        return None, {}, "Failed to extract text from diary"

    # Extract walkers based on format
    format_type = record['format']
    target_date = record['date']

    if format_type == 'narrative_en':
        walkers, roles = extract_walkers_narrative_en(text, target_date)
    elif format_type == 'structured_bg':
        walkers, roles = extract_walkers_structured_bg(text, target_date)
    elif format_type == 'structured_en_roles':
        walkers, roles = extract_walkers_structured_en(text, target_date, with_roles=True)
    elif format_type == 'structured_en':
        walkers, roles = extract_walkers_structured_en(text, target_date, with_roles=False)
    else:
        return None, {}, f"Unknown format: {format_type}"

    notes = ""
    if not walkers:
        notes = f"No walkers found in {record['source']} for {target_date}"

    # Special case: 2010-03-08 date discrepancy
    if target_date == "2010-03-08":
        notes = "Date discrepancy: diary entry dated 18.03.2010, not 08.03.2010 - FLAG FOR REVIEW"

    return walkers, roles, notes


def update_attribution_csv(extraction_results: List[Dict]) -> int:
    """
    Update attribution.csv with extracted walker data.

    Args:
        extraction_results: List of extraction result dictionaries

    Returns:
        Number of records updated
    """
    # Load attribution.csv
    records = []
    with open(ATTRIBUTION_PATH, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        fieldnames = reader.fieldnames
        for row in reader:
            records.append(row)

    # Create backup
    shutil.copy(ATTRIBUTION_PATH, ATTRIBUTION_BACKUP)

    # Update records
    updated_count = 0
    for result in extraction_results:
        if not result['walkers']:
            continue

        # Find matching record
        date = result['date']
        team = result['team']

        for record in records:
            if record['Date'] == date and record['Team'] == team:
                # Update walker fields
                record['Walkers_Original'] = result['walkers']
                record['Walkers_Transliterated'] = result['walkers']  # Already transliterated

                # Update role fields if present
                for role_key, role_value in result.get('roles', {}).items():
                    if role_key in record:
                        record[role_key] = role_value

                # Add extraction note
                if result.get('notes'):
                    if record.get('Extraction_Notes'):
                        record['Extraction_Notes'] += f"; {result['notes']}"
                    else:
                        record['Extraction_Notes'] = result['notes']

                updated_count += 1
                break

    # Write updated attribution.csv
    with open(ATTRIBUTION_PATH, 'w', encoding='utf-8', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(records)

    return updated_count


def generate_report(extraction_results: List[Dict]) -> None:
    """
    Generate detailed extraction report.

    Args:
        extraction_results: List of extraction result dictionaries
    """
    successful = [r for r in extraction_results if r['walkers']]
    failed = [r for r in extraction_results if not r['walkers']]

    with open(REPORT_PATH, 'w', encoding='utf-8') as f:
        f.write("# Diary Walker Extraction Report\n\n")
        f.write(f"**Date:** {datetime.now().strftime('%Y-%m-%d')}\n\n")
        f.write("---\n\n")

        f.write("## Summary\n\n")
        f.write(f"- Records processed: {len(extraction_results)}\n")
        f.write(f"- Successfully extracted: {len(successful)}\n")
        f.write(f"- Failed extractions: {len(failed)}\n")

        # Count walkers and roles
        total_walkers = sum(len(r['walkers'].split('|')) for r in successful if r['walkers'])
        total_roles = sum(len(r.get('roles', {})) for r in successful)

        f.write(f"- Total walker names added: {total_walkers}\n")
        f.write(f"- Records with role data: {total_roles}\n\n")

        f.write("---\n\n")

        f.write("## By Record Detail\n\n")
        f.write("| Date | Team | Source | Walkers Extracted | Roles Added | Notes |\n")
        f.write("|------|------|--------|-------------------|-------------|-------|\n")

        for result in extraction_results:
            walkers_count = len(result['walkers'].split('|')) if result['walkers'] else 0
            roles_count = len(result.get('roles', {}))
            notes = result.get('notes', '-')

            f.write(f"| {result['date']} | {result['team']} | {result['source']} | "
                   f"{walkers_count} | {roles_count} | {notes} |\n")

        f.write("\n---\n\n")

        if failed:
            f.write("## Failed Extractions\n\n")
            for result in failed:
                f.write(f"- **{result['date']} Team {result['team']}**: {result.get('notes', 'Unknown error')}\n")
            f.write("\n---\n\n")

        f.write("## Extraction Details\n\n")
        for result in successful:
            f.write(f"### {result['date']} - Team {result['team']}\n\n")
            f.write(f"**Source:** {result['source']}\n\n")
            f.write(f"**Walkers extracted:** {result['walkers']}\n\n")

            if result.get('roles'):
                f.write("**Roles extracted:**\n")
                for role_key, role_value in result['roles'].items():
                    f.write(f"- {role_key}: {role_value}\n")
                f.write("\n")

            if result.get('notes'):
                f.write(f"**Notes:** {result['notes']}\n\n")

            f.write("---\n\n")


def main():
    """Main execution function."""
    print("TRAP Diary Walker Extraction")
    print("=" * 50)
    print(f"Processing {len(RECORDS_TO_PROCESS)} records...\n")

    extraction_results = []

    for i, record in enumerate(RECORDS_TO_PROCESS, 1):
        print(f"[{i}/{len(RECORDS_TO_PROCESS)}] Processing {record['date']} Team {record['team']}...")

        walkers, roles, notes = extract_walkers_for_record(record)

        result = {
            'date': record['date'],
            'team': record['team'],
            'source': record['source'],
            'walkers': walkers,
            'roles': roles,
            'notes': notes
        }

        extraction_results.append(result)

        if walkers:
            print(f"  ✓ Extracted: {walkers}")
            if roles:
                print(f"    Roles: {', '.join(f'{k}={v}' for k, v in roles.items())}")
        else:
            print(f"  ✗ Failed: {notes}")

    print("\n" + "=" * 50)
    print("Updating attribution.csv...")

    updated_count = update_attribution_csv(extraction_results)

    print(f"Updated {updated_count} records")
    print(f"Backup created: {ATTRIBUTION_BACKUP}")

    print("\nGenerating report...")
    generate_report(extraction_results)
    print(f"Report saved: {REPORT_PATH}")

    print("\n" + "=" * 50)
    print("Extraction complete!")

    successful = len([r for r in extraction_results if r['walkers']])
    print(f"Success rate: {successful}/{len(extraction_results)} ({100*successful//len(extraction_results)}%)")


if __name__ == "__main__":
    main()
