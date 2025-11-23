#!/usr/bin/env python3
"""
Check current state of failed extractions and incomplete records in attribution.csv.

This script identifies:
1. Records with no walker data
2. Records with QA flags (MISSING, DIARY COVERAGE GAP, Incomplete, etc.)
3. Records flagged as NON-SURVEY DAY
4. Overall walker data coverage statistics

Author: Claude Code
Date: 2025-11-23
"""

import csv
from collections import defaultdict
from pathlib import Path


def main():
    """Main function to analyse current extraction status."""
    input_file = Path('outputs/attribution.csv')

    # Read CSV
    with open(input_file, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        rows = list(reader)

    # Categorise records
    total_records = len(rows)
    missing_walkers = []
    qa_flagged = []
    non_survey_days = []
    incomplete_records = []
    complete_records = []

    for row in rows:
        date = row['Date']
        team = row['Team']
        walkers_orig = row.get('Walkers_Original', '').strip()
        walkers_trans = row.get('Walkers_Transliterated', '').strip()
        qa_notes = row.get('QA_Notes', '').strip()

        record_id = f"{date} Team {team}"

        # Check for missing walker data
        if not walkers_orig and not walkers_trans:
            missing_walkers.append({
                'id': record_id,
                'qa_notes': qa_notes,
                'leader': row.get('Leader', ''),
                'units': f"{row.get('Start Unit', '')}-{row.get('End Unit', '')}"
            })

        # Check for QA flags
        if qa_notes:
            if 'NON-SURVEY DAY' in qa_notes:
                non_survey_days.append({
                    'id': record_id,
                    'activity': qa_notes.replace('NON-SURVEY DAY:', '').strip(),
                    'walkers': walkers_trans or walkers_orig
                })
            elif any(flag in qa_notes for flag in
                    ['MISSING', 'Incomplete', 'DIARY COVERAGE GAP', 'ERROR']):
                qa_flagged.append({
                    'id': record_id,
                    'qa_notes': qa_notes,
                    'walkers': walkers_trans or walkers_orig
                })
            elif qa_notes == 'Complete':
                complete_records.append(record_id)
            elif 'No role data available' in qa_notes:
                # This is just about role columns, not walker data
                if walkers_orig or walkers_trans:
                    complete_records.append(record_id)
                else:
                    incomplete_records.append({
                        'id': record_id,
                        'qa_notes': qa_notes
                    })
        else:
            # No QA notes - check if walker data exists
            if walkers_orig or walkers_trans:
                complete_records.append(record_id)
            else:
                incomplete_records.append({
                    'id': record_id,
                    'qa_notes': 'No QA notes'
                })

    # Calculate statistics
    records_with_walkers = sum(1 for row in rows
                              if row.get('Walkers_Original', '').strip()
                              or row.get('Walkers_Transliterated', '').strip())

    # Print results
    print("=" * 80)
    print("CURRENT FAILED EXTRACTIONS AND INCOMPLETE RECORDS REPORT")
    print("=" * 80)
    print()

    print(f"Total records: {total_records}")
    print(f"Records with walker data: {records_with_walkers}/{total_records} "
          f"({records_with_walkers/total_records*100:.1f}%)")
    print(f"Records missing walker data: {len(missing_walkers)}/{total_records} "
          f"({len(missing_walkers)/total_records*100:.1f}%)")
    print()

    # Missing walkers
    if missing_walkers:
        print(f"RECORDS WITH NO WALKER DATA ({len(missing_walkers)}):")
        print("-" * 80)
        for record in missing_walkers:
            print(f"  {record['id']}")
            print(f"    Leader: {record['leader']}")
            print(f"    Units: {record['units']}")
            print(f"    QA Notes: {record['qa_notes']}")
            print()
    else:
        print("✅ NO RECORDS WITH MISSING WALKER DATA")
        print()

    # QA flagged records
    if qa_flagged:
        print(f"RECORDS WITH QA FLAGS ({len(qa_flagged)}):")
        print("-" * 80)
        for record in qa_flagged:
            print(f"  {record['id']}")
            print(f"    Walkers: {record['walkers']}")
            print(f"    QA Notes: {record['qa_notes']}")
            print()
    else:
        print("✅ NO RECORDS WITH QA FLAGS (MISSING/INCOMPLETE/ERROR)")
        print()

    # Non-survey days
    if non_survey_days:
        print(f"NON-SURVEY DAYS ({len(non_survey_days)}):")
        print("-" * 80)
        for record in non_survey_days:
            print(f"  {record['id']}")
            print(f"    Walkers: {record['walkers']}")
            print(f"    Activity: {record['activity']}")
            print()

    # Incomplete records (no walkers, no QA notes)
    if incomplete_records:
        print(f"INCOMPLETE RECORDS (NO WALKERS, UNCLEAR STATUS) ({len(incomplete_records)}):")
        print("-" * 80)
        for record in incomplete_records:
            print(f"  {record['id']}")
            print(f"    QA Notes: {record['qa_notes']}")
            print()

    print("=" * 80)
    print(f"SUMMARY: {len(missing_walkers)} missing walkers | "
          f"{len(qa_flagged)} QA flagged | "
          f"{len(non_survey_days)} non-survey days | "
          f"{len(incomplete_records)} unclear status")
    print("=" * 80)


if __name__ == '__main__':
    main()
