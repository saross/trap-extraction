#!/usr/bin/env python3
"""
Apply manual name corrections from name-mapping.csv to attribution.csv.

This script processes 66 review_needed entries from the manual review:
- Valid corrections (58): Apply canonical_name to attribution.csv
- Invalid entries (6): Clear from attribution.csv, mark as 'invalid'
- Uncertain entries (2): Apply corrected_name with note

Author: Claude Code collaboration
Date: 2025-11-22
"""

import csv
import re
from collections import defaultdict
from pathlib import Path

# Paths
NAME_MAPPING_PATH = Path("outputs/name-mapping.csv")
ATTRIBUTION_PATH = Path("outputs/attribution.csv")
ATTRIBUTION_BACKUP = Path("outputs/attribution.csv.backup")

# Columns in attribution.csv that may contain names to correct
NAME_COLUMNS = [
    "Leader",
    "Walkers_Original",
    "Walkers_Transliterated",
    "Author",
    "PDA_Operator",
    "Paper_Recorder",
    "GPS_Operator",
    "Data_Editor",
    "Photographer",
]

# Invalid markers that indicate OCR false positives or illegible entries
INVALID_MARKERS = [
    "none",
    "ocr false positive",
    "illegible",
    "unknown",
    "false positive",
]


def is_invalid_marker(corrected_name):
    """Check if corrected_name indicates an invalid/irrecoverable entry."""
    if not corrected_name:
        return False
    return any(marker in corrected_name.lower() for marker in INVALID_MARKERS)


def exact_name_replace(text, old_name, new_name, case_sensitive=False):
    """
    Replace exact occurrences of old_name with new_name in text.
    Preserves delimiters (pipes, commas) and handles name lists.

    Uses word boundaries to avoid partial matches.
    """
    if not text or not old_name:
        return text

    # Escape special regex characters in the name
    escaped_old = re.escape(old_name)

    # Use word boundaries to ensure exact match
    # \b doesn't work well with some Unicode, so use more explicit pattern
    pattern = r'(?:^|(?<=[,|\s]))' + escaped_old + r'(?=\s*[,|\s]|$)'

    flags = 0 if case_sensitive else re.IGNORECASE

    # Replace with new_name
    result = re.sub(pattern, new_name, text, flags=flags)

    return result


def load_name_mapping():
    """Load name-mapping.csv and categorize review_needed entries."""
    corrections = {
        'valid': [],
        'invalid': [],
        'uncertain': []
    }

    with open(NAME_MAPPING_PATH, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            if row['status'] != 'review_needed':
                continue

            extracted_name = row['extracted_name']
            corrected_name = row['corrected_name']
            canonical_name = row['canonical_name']

            # Categorise
            if is_invalid_marker(corrected_name):
                corrections['invalid'].append(row)
            elif canonical_name:
                corrections['valid'].append(row)
            else:
                # Has corrected_name but no canonical_name
                corrections['uncertain'].append(row)

    return corrections


def load_attribution():
    """Load attribution.csv."""
    records = []
    with open(ATTRIBUTION_PATH, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        fieldnames = reader.fieldnames
        for row in reader:
            records.append(row)
    return records, fieldnames


def apply_corrections(attribution_records, corrections):
    """
    Apply corrections to attribution records.
    Returns statistics about changes made.
    """
    stats = {
        'valid': {'entries': 0, 'records_modified': 0, 'replacements': 0},
        'invalid': {'entries': 0, 'records_modified': 0, 'replacements': 0},
        'uncertain': {'entries': 0, 'records_modified': 0, 'replacements': 0},
    }

    change_log = []

    # Process each category
    for category in ['valid', 'invalid', 'uncertain']:
        for correction in corrections[category]:
            extracted_name = correction['extracted_name']
            corrected_name = correction['corrected_name']
            canonical_name = correction['canonical_name']
            dates_str = correction['dates']
            team = correction['team']

            # Determine replacement value
            if category == 'invalid':
                replacement = ''  # Clear invalid entries
            elif category == 'valid':
                replacement = canonical_name
            else:  # uncertain
                replacement = corrected_name

            # Parse dates (pipe-separated)
            dates = [d.strip() for d in dates_str.split('|')] if dates_str else []

            # Find matching records
            records_modified = 0
            replacements_made = 0

            for record in attribution_records:
                # Check if this record matches the dates/team
                if dates and record['Date'] not in dates:
                    continue
                if team and record['Team'] != team:
                    continue

                # Try to replace in each name column
                record_changed = False
                for col in NAME_COLUMNS:
                    if col not in record:
                        continue

                    original_value = record[col]
                    if not original_value:
                        continue

                    # Attempt replacement
                    new_value = exact_name_replace(
                        original_value,
                        extracted_name,
                        replacement,
                        case_sensitive=False
                    )

                    if new_value != original_value:
                        record[col] = new_value
                        record_changed = True
                        replacements_made += 1

                        change_log.append({
                            'date': record['Date'],
                            'team': record['Team'],
                            'column': col,
                            'extracted': extracted_name,
                            'replacement': replacement,
                            'category': category,
                            'before': original_value,
                            'after': new_value
                        })

                if record_changed:
                    records_modified += 1

            # Update stats
            stats[category]['entries'] += 1
            stats[category]['records_modified'] += records_modified
            stats[category]['replacements'] += replacements_made

            if records_modified == 0:
                print(f"⚠️  No matches found for '{extracted_name}' "
                      f"(dates: {dates_str}, team: {team})")

    return stats, change_log


def update_name_mapping_status(corrections):
    """Update status in name-mapping.csv for processed entries."""
    # Read all rows
    all_rows = []
    with open(NAME_MAPPING_PATH, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        fieldnames = reader.fieldnames
        for row in reader:
            all_rows.append(row)

    # Create lookup of extracted_name to category
    extracted_to_category = {}
    for category in ['valid', 'invalid', 'uncertain']:
        for correction in corrections[category]:
            extracted_to_category[correction['extracted_name']] = category

    # Update status for review_needed entries
    for row in all_rows:
        if row['status'] != 'review_needed':
            continue

        extracted_name = row['extracted_name']
        category = extracted_to_category.get(extracted_name)

        if category == 'valid':
            row['status'] = 'corrected'
        elif category == 'invalid':
            row['status'] = 'invalid'
            # Move invalid marker from corrected_name to notes
            if is_invalid_marker(row['corrected_name']):
                if row['notes']:
                    row['notes'] = f"{row['corrected_name']}. {row['notes']}"
                else:
                    row['notes'] = row['corrected_name']
                row['corrected_name'] = ''
        elif category == 'uncertain':
            row['status'] = 'uncertain'
            if row['notes']:
                row['notes'] = f"Identity not confirmed. {row['notes']}"
            else:
                row['notes'] = "Identity not confirmed"

    # Write back
    with open(NAME_MAPPING_PATH, 'w', encoding='utf-8', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(all_rows)


def main():
    print("=" * 80)
    print("APPLYING NAME CORRECTIONS FROM name-mapping.csv TO attribution.csv")
    print("=" * 80)
    print()

    # Load data
    print("📖 Loading name-mapping.csv...")
    corrections = load_name_mapping()
    print(f"   - Valid corrections: {len(corrections['valid'])}")
    print(f"   - Invalid entries: {len(corrections['invalid'])}")
    print(f"   - Uncertain entries: {len(corrections['uncertain'])}")
    print()

    print("📖 Loading attribution.csv...")
    attribution_records, fieldnames = load_attribution()
    print(f"   - Total records: {len(attribution_records)}")
    print()

    # Backup attribution.csv
    print("💾 Creating backup: attribution.csv.backup...")
    with open(ATTRIBUTION_BACKUP, 'w', encoding='utf-8', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(attribution_records)
    print()

    # Apply corrections
    print("🔧 Applying corrections...")
    stats, change_log = apply_corrections(attribution_records, corrections)
    print()

    # Write updated attribution.csv
    print("💾 Writing updated attribution.csv...")
    with open(ATTRIBUTION_PATH, 'w', encoding='utf-8', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(attribution_records)
    print()

    # Update name-mapping.csv status
    print("📝 Updating name-mapping.csv status...")
    update_name_mapping_status(corrections)
    print()

    # Print statistics
    print("=" * 80)
    print("CORRECTION STATISTICS")
    print("=" * 80)
    print()

    total_entries = 0
    total_records = 0
    total_replacements = 0

    for category in ['valid', 'invalid', 'uncertain']:
        s = stats[category]
        total_entries += s['entries']
        total_records += s['records_modified']
        total_replacements += s['replacements']

        print(f"{category.upper()} corrections:")
        print(f"  - Entries processed: {s['entries']}")
        print(f"  - Attribution records modified: {s['records_modified']}")
        print(f"  - Total replacements: {s['replacements']}")
        print()

    print(f"TOTAL:")
    print(f"  - Entries processed: {total_entries}")
    print(f"  - Attribution records modified: {total_records}")
    print(f"  - Total replacements: {total_replacements}")
    print()

    # Show sample changes
    print("=" * 80)
    print("SAMPLE CHANGES (first 10)")
    print("=" * 80)
    print()

    for i, change in enumerate(change_log[:10], 1):
        print(f"{i}. {change['date']} Team {change['team']} | "
              f"{change['column']}")
        print(f"   '{change['extracted']}' → '{change['replacement']}'")
        print(f"   Before: {change['before']}")
        print(f"   After:  {change['after']}")
        print()

    if len(change_log) > 10:
        print(f"... and {len(change_log) - 10} more changes")
        print()

    print("=" * 80)
    print("✅ CORRECTIONS COMPLETE")
    print("=" * 80)
    print()
    print("Files updated:")
    print(f"  - {ATTRIBUTION_PATH}")
    print(f"  - {NAME_MAPPING_PATH}")
    print(f"  - Backup: {ATTRIBUTION_BACKUP}")
    print()

    return change_log


if __name__ == "__main__":
    change_log = main()
