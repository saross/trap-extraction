#!/usr/bin/env python3
"""
Standardise attribution.csv so that the team leader is always listed as a walker.

This script ensures consistency by:
1. Reading attribution.csv
2. For each record with a leader, checking if the leader appears in the walker lists
3. Adding the leader to walker lists if missing
4. Creating a backup before modifying the file

Author: Claude Code
Date: 2025-11-23
"""

import csv
import shutil
from datetime import datetime
from pathlib import Path


def is_leader_in_walkers(leader_name: str, leader_alias: str,
                        walkers_name: str, walkers_alias: str) -> bool:
    """
    Check if leader appears in either walker name or alias fields.

    Args:
        leader_name: Leader's full name
        leader_alias: Leader's alias/short name
        walkers_name: Pipe-separated walker full names
        walkers_alias: Pipe-separated walker aliases

    Returns:
        True if leader found in either walker field, False otherwise
    """
    # Handle empty/missing values
    if not leader_name and not leader_alias:
        return True  # No leader to check

    if not walkers_name and not walkers_alias:
        return False  # No walkers listed, leader missing

    # Split walker lists and strip whitespace
    walker_names = [w.strip() for w in walkers_name.split('|')] if walkers_name else []
    walker_aliases = [w.strip() for w in walkers_alias.split('|')] if walkers_alias else []

    # Check if leader appears in either list
    leader_name_stripped = leader_name.strip() if leader_name else ''
    leader_alias_stripped = leader_alias.strip() if leader_alias else ''

    found_in_names = leader_name_stripped in walker_names if leader_name_stripped else False
    found_in_aliases = leader_alias_stripped in walker_aliases if leader_alias_stripped else False

    return found_in_names or found_in_aliases


def add_leader_to_walkers(leader_name: str, leader_alias: str,
                          walkers_name: str, walkers_alias: str) -> tuple[str, str]:
    """
    Add leader to walker lists if not already present.

    Args:
        leader_name: Leader's full name
        leader_alias: Leader's alias/short name
        walkers_name: Pipe-separated walker full names
        walkers_alias: Pipe-separated walker aliases

    Returns:
        Tuple of (updated_walkers_name, updated_walkers_alias)
    """
    # Handle empty walker lists
    if not walkers_name:
        walkers_name = ''
    if not walkers_alias:
        walkers_alias = ''

    # Split walker lists
    walker_names = [w.strip() for w in walkers_name.split('|')] if walkers_name else []
    walker_aliases = [w.strip() for w in walkers_alias.split('|')] if walkers_alias else []

    # Add leader to names if not present
    if leader_name and leader_name.strip() not in walker_names:
        walker_names.insert(0, leader_name.strip())

    # Add leader alias to aliases if not present
    if leader_alias and leader_alias.strip() not in walker_aliases:
        walker_aliases.insert(0, leader_alias.strip())

    # Rejoin with pipe separator
    updated_names = ' | '.join(walker_names) if walker_names else ''
    updated_aliases = ' | '.join(walker_aliases) if walker_aliases else ''

    return updated_names, updated_aliases


def main():
    """Main function to standardise leader inclusion in walker lists."""
    # File paths
    input_file = Path('outputs/attribution.csv')

    # Create backup with timestamp
    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    backup_file = Path(f'outputs/attribution.csv.backup_leader_standardisation_{timestamp}')

    print(f"Creating backup: {backup_file}")
    shutil.copy2(input_file, backup_file)

    # Read CSV
    with open(input_file, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        rows = list(reader)
        fieldnames = reader.fieldnames

    # Track changes
    updated_count = 0
    records_checked = 0

    # Process each row
    for row in rows:
        records_checked += 1

        leader = row.get('Leader', '')
        walkers_original = row.get('Walkers_Original', '')
        walkers_transliterated = row.get('Walkers_Transliterated', '')

        # Skip rows with no leader
        if not leader:
            continue

        # Check if leader is in walker lists
        if not is_leader_in_walkers(leader, leader, walkers_original, walkers_transliterated):
            # Add leader to walker lists
            updated_original, updated_transliterated = add_leader_to_walkers(
                leader, leader, walkers_original, walkers_transliterated
            )

            row['Walkers_Original'] = updated_original
            row['Walkers_Transliterated'] = updated_transliterated
            updated_count += 1

            print(f"Updated {row['Date']} Team {row['Team']}: "
                  f"Added leader '{leader}' to walker list")

    # Write updated CSV
    with open(input_file, 'w', encoding='utf-8', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)

    print(f"\nStandardisation complete:")
    print(f"  Records checked: {records_checked}")
    print(f"  Records updated: {updated_count}")
    print(f"  Backup saved to: {backup_file}")


if __name__ == '__main__':
    main()
