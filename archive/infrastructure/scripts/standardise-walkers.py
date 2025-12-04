#!/usr/bin/env python3
"""
Walker Data Standardisation Script for TRAP Attribution Data

This script performs a multi-phase transformation of walker data in attribution.csv:
    Phase 1.1: Merge transliterated content from Walkers_Transliterated into Walkers_Original
               for records with Cyrillic names (28 records from 2011 autumn Teams A & D)
    Phase 1.2: Normalise all separators to pipe format (space-pipe-space)
    Phase 1.3: Deduplicate exact names within each record
    Phase 2:   Delete the Walkers_Transliterated column
    Phase 3:   Create new Walkers_Standardised column with canonical "First Last" names

Author: Claude Code
Date: 25 November 2025
Project: TRAP Data Extraction for AKB Submission
"""

import csv
import re
import shutil
from datetime import datetime
from pathlib import Path
from typing import Optional


# Configuration
PROJECT_ROOT = Path(__file__).parent.parent
ATTRIBUTION_FILE = PROJECT_ROOT / "outputs" / "attribution.csv"
NAME_MAPPING_FILE = PROJECT_ROOT / "outputs" / "name-mapping.csv"
PARTICIPANTS_FILE = PROJECT_ROOT / "inputs" / "TRAP-Participants.csv"
REPORT_FILE = PROJECT_ROOT / "outputs" / "walker-standardisation-report.md"
BACKUP_SUFFIX = f".backup_standardisation_{datetime.now().strftime('%Y%m%d_%H%M%S')}"


def contains_cyrillic(text: str) -> bool:
    """
    Check if a string contains Cyrillic characters.

    Args:
        text: String to check

    Returns:
        True if the string contains any Cyrillic characters
    """
    if not text:
        return False
    return bool(re.search(r'[\u0400-\u04FF]', text))


def load_name_mapping() -> dict[str, str]:
    """
    Load the name mapping from name-mapping.csv and TRAP-Participants.csv.

    Builds a comprehensive lookup dictionary mapping name variants to canonical names.

    Returns:
        Dictionary mapping lowercase name variants to canonical "First Last" names
    """
    mapping = {}

    # Load from name-mapping.csv
    with open(NAME_MAPPING_FILE, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            extracted = row.get('extracted_name', '').strip()
            canonical = row.get('canonical_name', '').strip()
            status = row.get('status', '').strip()

            # Skip invalid entries (they should be removed from walkers)
            if status == 'invalid':
                # Map to empty string to signal removal
                if extracted:
                    mapping[extracted.lower()] = ''
                continue

            # Map extracted name to canonical
            if extracted and canonical:
                mapping[extracted.lower()] = canonical

    # Load from TRAP-Participants.csv for canonical names
    with open(PARTICIPANTS_FILE, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            first = row.get('First name', '').strip()
            last = row.get('Last name', '').strip()

            if first and last:
                canonical = f"{first} {last}"
                # Map various forms
                mapping[first.lower()] = canonical
                mapping[f"{first} {last}".lower()] = canonical
                mapping[f"{last}, {first}".lower()] = canonical
                mapping[f"{last}".lower()] = canonical  # Surname only

    return mapping


def normalise_separators(walker_string: str) -> str:
    """
    Normalise separators in a walker string to pipe format.

    Handles mixed pipe/comma separators by:
    1. Splitting on pipes first
    2. Then splitting on commas within each part
    3. Rejoining with space-pipe-space

    Args:
        walker_string: Original walker string with mixed separators

    Returns:
        Normalised string with consistent pipe separators
    """
    if not walker_string:
        return ''

    # First split on pipes
    parts = walker_string.split('|')

    # Then split each part on commas
    names = []
    for part in parts:
        # Split on comma and strip whitespace
        subparts = [name.strip() for name in part.split(',')]
        names.extend([n for n in subparts if n])

    return ' | '.join(names)


def deduplicate_names(walker_string: str) -> str:
    """
    Remove exact duplicate names from a walker string.

    Preserves the first occurrence of each name and maintains order.
    Case-sensitive comparison.

    Args:
        walker_string: Pipe-separated walker string

    Returns:
        Deduplicated pipe-separated string
    """
    if not walker_string:
        return ''

    names = [name.strip() for name in walker_string.split('|')]
    seen = set()
    unique_names = []

    for name in names:
        if name and name not in seen:
            seen.add(name)
            unique_names.append(name)

    return ' | '.join(unique_names)


def standardise_names(walker_string: str, name_mapping: dict[str, str]) -> str:
    """
    Convert walker names to canonical "First Last" format.

    Uses the name mapping to convert variants, initials, and diminutives
    to their canonical full names. Names not in the mapping are flagged.

    Args:
        walker_string: Pipe-separated walker string
        name_mapping: Dictionary mapping name variants to canonical names

    Returns:
        Pipe-separated string of canonical names
    """
    if not walker_string:
        return ''

    names = [name.strip() for name in walker_string.split('|')]
    standardised = []

    for name in names:
        if not name:
            continue

        # Clean up the name for lookup
        lookup_key = name.lower().strip()

        # Special handling for combined entries like "Dr. Ross training Royce Lawrence"
        if lookup_key in name_mapping:
            canonical = name_mapping[lookup_key]
            if canonical:  # Non-empty means valid mapping
                # Handle pipe-separated canonical names (combined entries)
                if '|' in canonical:
                    standardised.extend([n.strip() for n in canonical.split('|')])
                else:
                    standardised.append(canonical)
            # Empty canonical means invalid - skip
        else:
            # Not in mapping - flag as unmapped
            standardised.append(f"UNMAPPED: {name}")

    return ' | '.join(standardised)


def process_attribution_data():
    """
    Main processing function for walker standardisation.

    Executes all phases:
    - Phase 1.1: Merge transliterations (Cyrillic -> Latin)
    - Phase 1.2: Normalise separators
    - Phase 1.3: Deduplicate names
    - Phase 2: Remove Walkers_Transliterated column
    - Phase 3: Create Walkers_Standardised column

    Returns:
        Dictionary containing statistics and details for the report
    """
    # Create backup
    backup_file = ATTRIBUTION_FILE.with_suffix(ATTRIBUTION_FILE.suffix + BACKUP_SUFFIX)
    shutil.copy2(ATTRIBUTION_FILE, backup_file)
    print(f"Created backup: {backup_file}")

    # Load name mapping
    name_mapping = load_name_mapping()
    print(f"Loaded {len(name_mapping)} name mappings")

    # Read current data
    with open(ATTRIBUTION_FILE, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        fieldnames = reader.fieldnames
        rows = list(reader)

    # Statistics tracking
    stats = {
        'total_records': len(rows),
        'transliterations_merged': 0,
        'separators_normalised': 0,
        'duplicates_removed': 0,
        'unmapped_names': [],
        'merged_records': [],
        'skipped_vera_petra': False,
    }

    # Process each row
    processed_rows = []
    for row in rows:
        date = row.get('Date', '')
        team = row.get('Team', '')
        original = row.get('Walkers_Original', '')
        transliterated = row.get('Walkers_Transliterated', '')

        # Phase 1.1: Merge transliterations for Cyrillic records
        # Exception: Skip 2010-03-24 Team D (Vera/Petra discrepancy - keep Vera)
        if contains_cyrillic(original) and transliterated:
            if date == '2010-03-24' and team == 'D':
                # Skip this record - keep Original with Vera
                stats['skipped_vera_petra'] = True
            else:
                # Replace Cyrillic Original with Latin Transliterated
                row['Walkers_Original'] = transliterated
                stats['transliterations_merged'] += 1
                stats['merged_records'].append({
                    'date': date,
                    'team': team,
                    'before': original,
                    'after': transliterated
                })

        # Get the working walker string (after potential merge)
        walkers = row.get('Walkers_Original', '')

        # Phase 1.2: Normalise separators
        if walkers and (',' in walkers or '  ' in walkers):
            normalised = normalise_separators(walkers)
            if normalised != walkers:
                row['Walkers_Original'] = normalised
                stats['separators_normalised'] += 1
            walkers = normalised

        # Phase 1.3: Deduplicate names
        if walkers and '|' in walkers:
            deduplicated = deduplicate_names(walkers)
            if deduplicated != walkers:
                row['Walkers_Original'] = deduplicated
                stats['duplicates_removed'] += 1
            walkers = deduplicated

        # Phase 3: Create Walkers_Standardised
        standardised = standardise_names(walkers, name_mapping)
        row['Walkers_Standardised'] = standardised

        # Track unmapped names
        for name in standardised.split('|'):
            name = name.strip()
            if name.startswith('UNMAPPED:'):
                unmapped = name.replace('UNMAPPED:', '').strip()
                if unmapped not in [u['name'] for u in stats['unmapped_names']]:
                    stats['unmapped_names'].append({
                        'name': unmapped,
                        'date': date,
                        'team': team
                    })

        processed_rows.append(row)

    # Phase 2: Remove Walkers_Transliterated column
    new_fieldnames = [f for f in fieldnames if f != 'Walkers_Transliterated']

    # Add Walkers_Standardised column after Walkers_Original
    if 'Walkers_Standardised' not in new_fieldnames:
        original_idx = new_fieldnames.index('Walkers_Original')
        new_fieldnames.insert(original_idx + 1, 'Walkers_Standardised')

    # Write updated data
    with open(ATTRIBUTION_FILE, 'w', encoding='utf-8', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=new_fieldnames, extrasaction='ignore')
        writer.writeheader()
        writer.writerows(processed_rows)

    print(f"Processed {stats['total_records']} records")
    print(f"  - Transliterations merged: {stats['transliterations_merged']}")
    print(f"  - Separators normalised: {stats['separators_normalised']}")
    print(f"  - Records with duplicates removed: {stats['duplicates_removed']}")
    print(f"  - Unmapped names: {len(stats['unmapped_names'])}")

    return stats


def generate_report(stats: dict):
    """
    Generate a markdown report documenting all changes made.

    Args:
        stats: Dictionary containing processing statistics and details
    """
    report_lines = [
        "# Walker Standardisation Report",
        "",
        f"**Generated:** {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}",
        f"**Total records processed:** {stats['total_records']}",
        "",
        "---",
        "",
        "## Summary",
        "",
        f"- **Transliterations merged:** {stats['transliterations_merged']} records",
        f"- **Separators normalised:** {stats['separators_normalised']} records",
        f"- **Duplicates removed:** {stats['duplicates_removed']} records",
        f"- **Unmapped names:** {len(stats['unmapped_names'])}",
        "",
    ]

    # Vera/Petra exception
    if stats['skipped_vera_petra']:
        report_lines.extend([
            "### Special Case: 2010-03-24 Team D",
            "",
            "Transliteration merge **skipped** for this record as per plan.",
            "- Original had \"Vera\" (correct)",
            "- Transliterated had \"Petra\" (error)",
            "- Resolution: Kept \"Vera\" from Original",
            "",
        ])

    # Merged records section
    if stats['merged_records']:
        report_lines.extend([
            "---",
            "",
            "## Transliteration Merges",
            "",
            "Records where Cyrillic names in Walkers_Original were replaced with Latin transliterations:",
            "",
            "| Date | Team | Before (Cyrillic) | After (Latin) |",
            "|------|------|-------------------|---------------|",
        ])
        for record in stats['merged_records'][:30]:  # Show first 30
            before = record['before'][:50] + "..." if len(record['before']) > 50 else record['before']
            after = record['after'][:50] + "..." if len(record['after']) > 50 else record['after']
            report_lines.append(f"| {record['date']} | {record['team']} | {before} | {after} |")

        if len(stats['merged_records']) > 30:
            report_lines.append(f"\n*... and {len(stats['merged_records']) - 30} more records*")
        report_lines.append("")

    # Unmapped names section
    if stats['unmapped_names']:
        report_lines.extend([
            "---",
            "",
            "## Unmapped Names",
            "",
            "Names that could not be mapped to canonical \"First Last\" format.",
            "These require manual review or additional entries in name-mapping.csv.",
            "",
            "| Name | First Occurrence (Date) | Team |",
            "|------|-------------------------|------|",
        ])
        for unmapped in stats['unmapped_names']:
            report_lines.append(f"| {unmapped['name']} | {unmapped['date']} | {unmapped['team']} |")
        report_lines.append("")
    else:
        report_lines.extend([
            "---",
            "",
            "## Unmapped Names",
            "",
            "**All names successfully mapped!** No unmapped names found.",
            "",
        ])

    # Footer
    report_lines.extend([
        "---",
        "",
        "## Files Modified",
        "",
        "- `outputs/attribution.csv`",
        "  - Walkers_Original: Cleaned (merged transliterations, normalised separators, deduplicated)",
        "  - Walkers_Transliterated: Column removed",
        "  - Walkers_Standardised: New column with canonical names",
        "",
        "## Verification Steps",
        "",
        "1. Check that no Cyrillic characters remain in Walkers_Original",
        "2. Verify all pipe separators are consistent (space-pipe-space)",
        "3. Confirm no exact duplicate names within any record",
        "4. Review any UNMAPPED entries in Walkers_Standardised",
        "",
        "---",
        "",
        "*Report generated by `scripts/standardise-walkers.py`*",
    ])

    # Write report
    with open(REPORT_FILE, 'w', encoding='utf-8') as f:
        f.write('\n'.join(report_lines))

    print(f"Report generated: {REPORT_FILE}")


def main():
    """
    Main entry point for the walker standardisation script.
    """
    print("=" * 60)
    print("TRAP Walker Data Standardisation")
    print("=" * 60)
    print()

    # Verify files exist
    if not ATTRIBUTION_FILE.exists():
        print(f"ERROR: Attribution file not found: {ATTRIBUTION_FILE}")
        return

    if not NAME_MAPPING_FILE.exists():
        print(f"ERROR: Name mapping file not found: {NAME_MAPPING_FILE}")
        return

    if not PARTICIPANTS_FILE.exists():
        print(f"ERROR: Participants file not found: {PARTICIPANTS_FILE}")
        return

    # Process data
    stats = process_attribution_data()

    # Generate report
    generate_report(stats)

    print()
    print("=" * 60)
    print("Standardisation complete!")
    print("=" * 60)


if __name__ == "__main__":
    main()
