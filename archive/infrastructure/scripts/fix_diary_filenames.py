#!/usr/bin/env python3
"""
Fix incorrect diary filename references in name-mapping.csv.

The actual filenames are:
- Team A: "Diary Team A.doc" (with spaces) - CORRECT
- Team B: "DiaryTeamB.doc" (no spaces) - but CSV has "Diary Team B.doc"
- Team C: "The Diary of Team C.doc" - but CSV has "Diary Team C.doc"

Author: Claude Code collaboration
Date: November 2025
"""

import csv


def main():
    """Fix diary filename references."""
    print("Fixing diary filename references in name-mapping.csv...")
    print()

    # Read CSV
    with open('outputs/name-mapping.csv', 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        fieldnames = reader.fieldnames
        rows = list(reader)

    # Track corrections
    corrections = []

    # Apply corrections
    for i, row in enumerate(rows):
        pdf_sources = row.get('pdf_sources', '')

        if pdf_sources:
            original = pdf_sources
            updated = pdf_sources

            # Fix: "Diary Team B.doc" → "DiaryTeamB.doc"
            updated = updated.replace('Diary Team B.doc', 'DiaryTeamB.doc')

            # Fix: "Diary Team C.doc" → "The Diary of Team C.doc"
            updated = updated.replace('Diary Team C.doc', 'The Diary of Team C.doc')

            if updated != original:
                row['pdf_sources'] = updated
                corrections.append({
                    'row': i + 2,
                    'extracted_name': row['extracted_name'],
                    'old': original,
                    'new': updated
                })

    # Write updated CSV
    if corrections:
        with open('outputs/name-mapping.csv', 'w', encoding='utf-8', newline='') as f:
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(rows)

        print(f"Applied {len(corrections)} corrections:\n")
        for correction in corrections:
            print(f"Row {correction['row']}: {correction['extracted_name']}")
            print(f"  Old: {correction['old']}")
            print(f"  New: {correction['new']}")
            print()

        print("Updated name-mapping.csv written.")
    else:
        print("No corrections needed.")


if __name__ == '__main__':
    main()
