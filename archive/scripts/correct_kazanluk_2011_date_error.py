#!/usr/bin/env python3
"""
Correct Kazanluk 2011 date error - Option A implementation.

Date Error: 2011-11-10 Team D is misdated - units 41088-41152 actually
belong to 2011-10-21 Team D.

Actions:
1. Delete erroneous 2011-11-10 Team D record
2. Update 2011-10-21 Team D with correct data:
   - Units: 41088-41152
   - Leader: NK
   - All 5 walkers including A. Antonov
   - Source: D_2011Diary_BG.doc
   - Extraction notes documenting the correction

Evidence: D_2011Diary_BG.doc Day 8 (21.10.2011) explicitly states
units 41088-41152. Team D diary ends 2 Nov - no November entries exist.
"""
import csv
from pathlib import Path
from datetime import datetime

# Correction data from D_2011Diary_BG.doc Day 8
CORRECTION_DATA = {
    'Date': '2011-10-21',
    'Team': 'D',
    'Start Unit': '41088',
    'End Unit': '41152',
    'Leader': 'NK',
    'Walkers_Original': 'Н. Кечева | В. Генчева | Е. Дакашев | Е. Тонкова | А. Антонов',
    'Walkers_Transliterated': 'N. Kecheva | V. Gencheva | E. Dakashev | E. Tonkova | A. Antonov',
    'PDF_Source': 'D_2011Diary_BG.doc',
    'Extraction_Notes': 'Corrected from erroneous 2011-11-10 record - units 41088-41152 belong to 2011-10-21 per Team D diary Day 8 (21.10.2011 г.) | Added missing walker А. Антонов (A. Antonov) | Evidence: "Направени са 4 трансекти (полигони с номера 41088 до 41152)" [4 transects were made (polygons numbered 41088 to 41152)]',
    'QA_Notes': 'DATE ERROR CORRECTED - Was incorrectly recorded as 2011-11-10 in source data (Kaz11_SurveySummary.xlsx) | Team D diary covers 14 Oct - 2 Nov only, no November 10 entry exists | Unit sequence confirms correction: 41008-41087 (Oct 20) → 41088-41152 (Oct 21) → 41153-41197 (Oct 22)'
}

# Record to delete
DELETE_RECORD = ('2011-11-10', 'D')

def apply_correction():
    """Apply Option A correction to attribution.csv."""

    input_path = Path('outputs/attribution.csv')
    backup_path = Path(f'outputs/attribution.csv.backup_kazanluk2011_dateerror_{datetime.now().strftime("%Y%m%d_%H%M%S")}')

    # Create backup
    print(f"Creating backup: {backup_path.name}")
    with open(input_path, 'r', encoding='utf-8') as f:
        backup_content = f.read()
    with open(backup_path, 'w', encoding='utf-8') as f:
        f.write(backup_content)

    # Read CSV
    rows = []
    with open(input_path, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        headers = reader.fieldnames
        rows = list(reader)

    # Track changes
    deleted = False
    updated = False
    original_2011_10_21 = None

    # Process rows
    filtered_rows = []
    for row in rows:
        key = (row['Date'], row['Team'])

        # Delete erroneous 2011-11-10 Team D record
        if key == DELETE_RECORD:
            print(f"\n🗑️  DELETING erroneous record:")
            print(f"   Date: {row['Date']}, Team: {row['Team']}")
            print(f"   Units: {row.get('Start Unit', 'N/A')}-{row.get('End Unit', 'N/A')}")
            print(f"   Leader: {row.get('Leader', 'N/A')}")
            print(f"   Reason: Date error - these units belong to 2011-10-21 Team D")
            deleted = True
            continue  # Skip this row (delete it)

        # Update 2011-10-21 Team D record
        if key == ('2011-10-21', 'D'):
            print(f"\n✏️  UPDATING record:")
            print(f"   Date: {row['Date']}, Team: {row['Team']}")

            # Store original values
            original_2011_10_21 = {
                'Units': f"{row.get('Start Unit', 'MISSING')}-{row.get('End Unit', 'MISSING')}",
                'Leader': row.get('Leader', 'MISSING'),
                'Walkers': row.get('Walkers_Transliterated', 'MISSING')
            }

            # Apply corrections
            for field, value in CORRECTION_DATA.items():
                if field in ['Date', 'Team']:
                    continue  # Don't change key fields
                row[field] = value

            updated = True

            # Show changes
            print(f"   BEFORE:")
            print(f"     Units: {original_2011_10_21['Units']}")
            print(f"     Leader: {original_2011_10_21['Leader']}")
            print(f"     Walkers: {original_2011_10_21['Walkers']}")
            print(f"   AFTER:")
            print(f"     Units: {row['Start Unit']}-{row['End Unit']}")
            print(f"     Leader: {row['Leader']}")
            print(f"     Walkers: {row['Walkers_Transliterated']}")

        filtered_rows.append(row)

    # Write corrected CSV
    with open(input_path, 'w', encoding='utf-8', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=headers)
        writer.writeheader()
        writer.writerows(filtered_rows)

    # Summary
    print(f"\n{'='*70}")
    print(f"OPTION A CORRECTION COMPLETE")
    print(f"{'='*70}")
    print(f"✅ Deleted: {DELETE_RECORD[0]} Team {DELETE_RECORD[1]} (erroneous record)")
    print(f"✅ Updated: 2011-10-21 Team D (complete data with 5 walkers)")
    print(f"📄 Backup saved: {backup_path.name}")
    print(f"\nTotal rows: {len(rows)} → {len(filtered_rows)} (-1 erroneous record)")

    if not deleted:
        print(f"\n⚠️  WARNING: Record {DELETE_RECORD} not found for deletion!")
    if not updated:
        print(f"\n⚠️  WARNING: Record 2011-10-21 Team D not found for update!")

    return deleted and updated

def create_correction_report():
    """Create report documenting the correction."""

    report_path = Path('outputs/kazanluk-2011-date-correction-applied.md')

    content = f"""# Kazanluk 2011 Date Error Correction Applied

**Date:** {datetime.now().strftime('%d %B %Y %H:%M')}
**Action:** Option A implementation
**Type:** Data quality correction

## Summary

Successfully corrected date error in Kazanluk 2011 attribution data per user request.

## Actions Taken

### 1. Deleted Erroneous Record

**Record:** 2011-11-10, Team D
- **Units:** 41088-41152
- **Leader:** NK
- **Status:** DELETED (date error)
- **Reason:** Team D diary ends 2 November - no November 10 entry exists

### 2. Updated Correct Record

**Record:** 2011-10-21, Team D

**Before correction:**
- Units: MISSING
- Leader: MISSING
- Walkers: Н. Кечева | В. Генчева | Е. Дакашев | Е. Тонкова (4 walkers)

**After correction:**
- Units: 41088-41152
- Leader: NK
- Walkers: Н. Кечева | В. Генчева | Е. Дакашев | Е. Тонкова | А. Антонов (5 walkers)
- Source: D_2011Diary_BG.doc
- Notes: Documented date error correction and evidence

## Evidence

From D_2011Diary_BG.doc, Ден 8: 21.10.2011 г. (петък):

```text
Екип:
Н. Кечева, В. Генчева, Е. Дакашев, Е. Тонкова, А. Антонов

Работа на терен:
Направени са 4 трансекти (полигони с номера 41088 до 41152) в посока С-Ю
между асфалтовия път Калофер-Казанлък от юг и жп линията София-Казанлък от
север.
```

**Translation:** 4 transects were made (polygons numbered 41088 to 41152)

## Impact

- **Before:** 1 erroneous record + 1 incomplete record
- **After:** 1 complete, correct record
- **Data quality:** Improved - date error corrected, missing data filled
- **CSV rows:** 269 → 268 (1 erroneous record deleted)

## Root Cause

Date entry error in source file **Kaz11_SurveySummary.xlsx** where 2011-10-21 was
incorrectly entered as 2011-11-10.

## Follow-Up Required

Source data custodian should correct Kaz11_SurveySummary.xlsx to prevent future
confusion. See follow-up-actions.md for details.

## Files Modified

- `outputs/attribution.csv` - Corrected data
- `scripts/correct_kazanluk_2011_date_error.py` - Correction script
- Backup: `attribution.csv.backup_kazanluk2011_dateerror_*`

## References

- Investigation report: `outputs/kazanluk-2011-date-error-report.md`
- Source diary: `../Kazanluk/2011-11-30/Project Records/Team D/D_2011Diary_BG.doc`

---

**Report generated:** {datetime.now().strftime('%d %B %Y %H:%M')}
**Method:** Automated correction via Python script
**Confidence:** Very High (100%) - diary evidence conclusive
"""

    with open(report_path, 'w', encoding='utf-8') as f:
        f.write(content)

    print(f"\n✅ Correction report created: {report_path}")
    return report_path

if __name__ == '__main__':
    print("=" * 70)
    print("KAZANLUK 2011 DATE ERROR CORRECTION (OPTION A)")
    print("=" * 70)
    print()
    print("This script will:")
    print("1. DELETE erroneous record: 2011-11-10 Team D")
    print("2. UPDATE correct record: 2011-10-21 Team D")
    print()

    success = apply_correction()

    if success:
        create_correction_report()
        print("\n✅ Correction complete!")
    else:
        print("\n❌ Correction failed - check warnings above")
