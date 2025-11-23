#!/usr/bin/env python3
"""
Clean up stale 'MISSING: Walkers' flags from attribution.csv.

This script removes 'MISSING: Walkers' from QA_Notes when walker data is actually present
in either Walkers_Original or Walkers_Transliterated columns.

Author: Claude Code
Date: 2025-11-23
"""

import csv
import re
import shutil
from datetime import datetime
from pathlib import Path


def remove_missing_walkers_flag(qa_notes: str) -> str:
    """
    Remove 'MISSING: Walkers' flag from QA_Notes.

    Args:
        qa_notes: Original QA_Notes text

    Returns:
        Cleaned QA_Notes with 'MISSING: Walkers' removed
    """
    if not qa_notes:
        return qa_notes

    # Remove various forms of the missing walkers flag
    patterns = [
        r'MISSING:\s*Walkers\s*\|\s*',  # "MISSING: Walkers | "
        r'\|\s*MISSING:\s*Walkers\s*',  # " | MISSING: Walkers"
        r'MISSING:\s*Walkers',           # "MISSING: Walkers" (standalone)
    ]

    cleaned = qa_notes
    for pattern in patterns:
        cleaned = re.sub(pattern, '', cleaned, flags=re.IGNORECASE)

    # Clean up multiple pipes and trailing separators
    cleaned = re.sub(r'\|\s*\|', '|', cleaned)  # Remove double pipes
    cleaned = re.sub(r'^\s*\|\s*', '', cleaned)  # Remove leading pipe
    cleaned = re.sub(r'\s*\|\s*$', '', cleaned)  # Remove trailing pipe
    cleaned = cleaned.strip()

    return cleaned


def main():
    """Main function to clean stale MISSING: Walkers flags."""
    # File paths
    input_file = Path('outputs/attribution.csv')

    # Create backup with timestamp
    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    backup_file = Path(f'outputs/attribution.csv.backup_clean_stale_flags_{timestamp}')

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

        walkers_orig = row.get('Walkers_Original', '').strip()
        walkers_trans = row.get('Walkers_Transliterated', '').strip()
        qa_notes = row.get('QA_Notes', '').strip()

        # Skip if no QA notes or no walker data
        if not qa_notes:
            continue

        # Check if has "MISSING: Walkers" flag
        if 'MISSING: Walkers' in qa_notes or 'MISSING:Walkers' in qa_notes:
            # Check if walker data actually exists
            if walkers_orig or walkers_trans:
                # Remove the stale flag
                cleaned_qa = remove_missing_walkers_flag(qa_notes)
                row['QA_Notes'] = cleaned_qa
                updated_count += 1

                print(f"Cleaned {row['Date']} Team {row['Team']}: "
                      f"Removed stale 'MISSING: Walkers' flag")
                print(f"  Before: {qa_notes}")
                print(f"  After: {cleaned_qa}")
                print()

    # Write updated CSV
    with open(input_file, 'w', encoding='utf-8', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)

    print(f"\nStale flag cleaning complete:")
    print(f"  Records checked: {records_checked}")
    print(f"  Stale flags removed: {updated_count}")
    print(f"  Backup saved to: {backup_file}")


if __name__ == '__main__':
    main()
