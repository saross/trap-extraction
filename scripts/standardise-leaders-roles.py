#!/usr/bin/env python3
"""
Leader and Role Column Standardisation Script for TRAP Attribution Data

This script standardises the Leader and Role columns in attribution.csv:
    - Leader: Standardise to canonical "First Last" names, handle multiple leaders
    - PDA_Operator: Standardise to canonical names
    - Paper_Recorder: Standardise to canonical names, remove metadata entries
    - Data_Editor: Standardise to canonical names, clear placeholders
    - GPS_Operator: Standardise to canonical names
    - Photographer: Standardise to canonical names
    - Author: Standardise to canonical names

Unlike walker standardisation, this script replaces values directly (no "_Original"
preservation needed).

Author: Claude Code
Date: 25 November 2025
Project: TRAP Data Extraction for AKB Submission
"""

import csv
import shutil
from datetime import datetime
from pathlib import Path
from typing import Optional


# Configuration
PROJECT_ROOT = Path(__file__).parent.parent
ATTRIBUTION_FILE = PROJECT_ROOT / "outputs" / "attribution.csv"
NAME_MAPPING_FILE = PROJECT_ROOT / "outputs" / "name-mapping.csv"
PARTICIPANTS_FILE = PROJECT_ROOT / "inputs" / "TRAP-Participants.csv"
REPORT_FILE = PROJECT_ROOT / "outputs" / "leader-role-standardisation-report.md"
BACKUP_SUFFIX = f".backup_leader_role_standardisation_{datetime.now().strftime('%Y%m%d_%H%M%S')}"

# Columns to standardise
ROLE_COLUMNS = [
    'Leader',
    'PDA_Operator',
    'Paper_Recorder',
    'Data_Editor',
    'GPS_Operator',
    'Photographer',
    'Author'
]


def load_name_mapping() -> dict[str, str]:
    """
    Load the name mapping from name-mapping.csv and TRAP-Participants.csv.

    Builds a comprehensive lookup dictionary mapping name variants to canonical names.

    Returns:
        Dictionary mapping lowercase name variants to canonical "First Last" names.
        Empty string value means the entry should be cleared (invalid/metadata).
    """
    mapping = {}

    # Load from name-mapping.csv
    with open(NAME_MAPPING_FILE, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            extracted = row.get('extracted_name', '').strip()
            canonical = row.get('canonical_name', '').strip()
            status = row.get('status', '').strip()

            # Skip entries without extracted_name
            if not extracted:
                continue

            # Invalid entries should be cleared (map to empty string)
            if status == 'invalid':
                mapping[extracted.lower()] = ''
                continue

            # Map extracted name to canonical
            if canonical:
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
                mapping[last.lower()] = canonical  # Surname only

    return mapping


def map_single_name(name: str, name_mapping: dict[str, str]) -> Optional[str]:
    """
    Map a single name to its canonical form.

    Args:
        name: The name to map
        name_mapping: Dictionary of name mappings

    Returns:
        Canonical name, empty string if should be cleared, or None if unmapped
    """
    if not name:
        return ''

    lookup_key = name.lower().strip()

    if lookup_key in name_mapping:
        canonical = name_mapping[lookup_key]
        return canonical  # Could be empty string (invalid) or canonical name

    return None  # Not found - will be flagged as unmapped


def standardise_leader(leader_value: str, name_mapping: dict[str, str]) -> tuple[str, list[str]]:
    """
    Standardise Leader column value.

    Handles single leaders and multiple leaders (comma-separated).

    Args:
        leader_value: Original leader value
        name_mapping: Dictionary of name mappings

    Returns:
        Tuple of (standardised value, list of unmapped names)
    """
    if not leader_value:
        return '', []

    unmapped = []

    # Handle multiple leaders (comma-separated within quotes)
    if ',' in leader_value:
        leaders = [l.strip() for l in leader_value.split(',')]
        standardised = []

        for leader in leaders:
            if not leader:
                continue

            result = map_single_name(leader, name_mapping)
            if result is None:
                # Not found - flag as unmapped
                standardised.append(f"UNMAPPED: {leader}")
                unmapped.append(leader)
            elif result:  # Non-empty means valid mapping
                # Handle pipe-separated canonical names (combined entries)
                if '|' in result:
                    standardised.extend([n.strip() for n in result.split('|')])
                else:
                    standardised.append(result)
            # Empty result means invalid - skip

        return ' | '.join(standardised), unmapped

    # Single leader
    result = map_single_name(leader_value, name_mapping)
    if result is None:
        return f"UNMAPPED: {leader_value}", [leader_value]
    return result, []


def standardise_role(role_value: str, name_mapping: dict[str, str]) -> tuple[str, list[str]]:
    """
    Standardise a role column value.

    Handles single names and pipe-separated values.

    Args:
        role_value: Original role value
        name_mapping: Dictionary of name mappings

    Returns:
        Tuple of (standardised value, list of unmapped names)
    """
    if not role_value:
        return '', []

    unmapped = []

    # Handle pipe-separated values (e.g., "Nadja | Ljubo")
    if '|' in role_value:
        names = [n.strip() for n in role_value.split('|')]
        standardised = []

        for name in names:
            if not name:
                continue

            result = map_single_name(name, name_mapping)
            if result is None:
                standardised.append(f"UNMAPPED: {name}")
                unmapped.append(name)
            elif result:  # Non-empty means valid mapping
                # Handle pipe-separated canonical names
                if '|' in result:
                    standardised.extend([n.strip() for n in result.split('|')])
                else:
                    standardised.append(result)
            # Empty result means invalid - skip

        return ' | '.join(standardised), unmapped

    # Single name
    result = map_single_name(role_value, name_mapping)
    if result is None:
        return f"UNMAPPED: {role_value}", [role_value]
    return result, []


def process_attribution_data():
    """
    Main processing function for leader and role standardisation.

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
        'columns_processed': ROLE_COLUMNS,
        'changes_per_column': {col: 0 for col in ROLE_COLUMNS},
        'cleared_per_column': {col: 0 for col in ROLE_COLUMNS},
        'unmapped_names': {},  # {name: {'column': col, 'date': date, 'team': team}}
    }

    # Process each row
    processed_rows = []
    for row in rows:
        date = row.get('Date', '')
        team = row.get('Team', '')

        # Process Leader column
        original_leader = row.get('Leader', '')
        if original_leader:
            standardised, unmapped = standardise_leader(original_leader, name_mapping)
            if standardised != original_leader:
                row['Leader'] = standardised
                stats['changes_per_column']['Leader'] += 1
                if not standardised:
                    stats['cleared_per_column']['Leader'] += 1
            for name in unmapped:
                if name not in stats['unmapped_names']:
                    stats['unmapped_names'][name] = {
                        'column': 'Leader',
                        'date': date,
                        'team': team
                    }

        # Process role columns
        for column in ROLE_COLUMNS[1:]:  # Skip Leader, already processed
            original = row.get(column, '')
            if original:
                standardised, unmapped = standardise_role(original, name_mapping)
                if standardised != original:
                    row[column] = standardised
                    stats['changes_per_column'][column] += 1
                    if not standardised:
                        stats['cleared_per_column'][column] += 1
                for name in unmapped:
                    if name not in stats['unmapped_names']:
                        stats['unmapped_names'][name] = {
                            'column': column,
                            'date': date,
                            'team': team
                        }

        processed_rows.append(row)

    # Write updated data
    with open(ATTRIBUTION_FILE, 'w', encoding='utf-8', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(processed_rows)

    print(f"\nProcessed {stats['total_records']} records")
    print("\nChanges per column:")
    for col in ROLE_COLUMNS:
        changes = stats['changes_per_column'][col]
        cleared = stats['cleared_per_column'][col]
        print(f"  - {col}: {changes} changes ({cleared} cleared)")
    print(f"\nUnmapped names: {len(stats['unmapped_names'])}")

    return stats


def generate_report(stats: dict):
    """
    Generate a markdown report documenting all changes made.

    Args:
        stats: Dictionary containing processing statistics and details
    """
    report_lines = [
        "# Leader and Role Standardisation Report",
        "",
        f"**Generated:** {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}",
        f"**Total records processed:** {stats['total_records']}",
        "",
        "---",
        "",
        "## Summary",
        "",
        "| Column | Changes | Cleared |",
        "|--------|---------|---------|",
    ]

    total_changes = 0
    total_cleared = 0
    for col in ROLE_COLUMNS:
        changes = stats['changes_per_column'][col]
        cleared = stats['cleared_per_column'][col]
        total_changes += changes
        total_cleared += cleared
        report_lines.append(f"| {col} | {changes} | {cleared} |")

    report_lines.extend([
        f"| **Total** | **{total_changes}** | **{total_cleared}** |",
        "",
    ])

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
            "| Name | Column | First Occurrence (Date) | Team |",
            "|------|--------|-------------------------|------|",
        ])
        for name, info in stats['unmapped_names'].items():
            report_lines.append(f"| {name} | {info['column']} | {info['date']} | {info['team']} |")
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
        "## Columns Modified",
        "",
        "- **Leader**: Standardised to canonical \"First Last\" names",
        "- **PDA_Operator**: Standardised to canonical names",
        "- **Paper_Recorder**: Standardised, metadata entries cleared",
        "- **Data_Editor**: Standardised, placeholders cleared",
        "- **GPS_Operator**: Standardised to canonical names",
        "- **Photographer**: Standardised to canonical names",
        "- **Author**: Standardised to canonical names",
        "",
        "## Verification Steps",
        "",
        "1. Check that all Leader values are canonical names or empty",
        "2. Verify no metadata entries remain in role columns",
        "3. Verify no placeholder entries remain in role columns",
        "4. Review any UNMAPPED entries for manual resolution",
        "",
        "---",
        "",
        "*Report generated by `scripts/standardise-leaders-roles.py`*",
    ])

    # Write report
    with open(REPORT_FILE, 'w', encoding='utf-8') as f:
        f.write('\n'.join(report_lines))

    print(f"\nReport generated: {REPORT_FILE}")


def main():
    """
    Main entry point for the leader and role standardisation script.
    """
    print("=" * 60)
    print("TRAP Leader and Role Standardisation")
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
