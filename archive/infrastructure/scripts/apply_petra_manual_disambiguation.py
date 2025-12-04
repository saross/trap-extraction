#!/usr/bin/env python3
"""
Apply manual disambiguation decisions for remaining Petra entries.

Based on manual PDF review by Dr. Sobotkova:
- 2009-03-07 Team A: Petra Janouchová
- 2009-03-08 Team A: Petra Janouchová
- 2009-03-09 Team A: Petra Janouchová
- 2009-04-03 Team E: Petra Janouchová
- 2010-03-24 Team D: Extraction error - should be 'Vera', not 'Petra'

Author: Claude Code collaboration
Date: November 2025
"""

import csv
from pathlib import Path


def main():
    """Apply manual disambiguation corrections to attribution.csv."""
    input_file = Path('outputs/attribution.csv')

    # Manual disambiguation decisions
    corrections = {
        ('2009-03-07', 'A'): ('Petra', 'Petra Janouchová'),
        ('2009-03-08', 'A'): ('Petra', 'Petra Janouchová'),
        ('2009-03-09', 'A'): ('Petra', 'Petra Janouchová'),
        ('2009-04-03', 'E'): ('Petra', 'Petra Janouchová'),
        ('2010-03-24', 'D'): ('Petra', 'Vera'),  # Extraction error
    }

    # Read CSV
    with open(input_file, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        fieldnames = reader.fieldnames
        rows = list(reader)

    # Apply corrections
    updates = []
    for row in rows:
        date = row['Date']
        team = row['Team']
        key = (date, team)

        if key in corrections:
            old_name, new_name = corrections[key]
            walkers = row['Walkers_Original']

            if old_name in walkers:
                # Replace the name
                new_walkers = walkers.replace(old_name, new_name)
                row['Walkers_Original'] = new_walkers

                updates.append({
                    'date': date,
                    'team': team,
                    'old': old_name,
                    'new': new_name,
                    'walkers': new_walkers
                })

    # Write updated CSV
    with open(input_file, 'w', encoding='utf-8', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)

    # Report results
    print(f"Applied {len(updates)} manual corrections:\n")
    for update in updates:
        print(f"{update['date']} Team {update['team']}: {update['old']} → {update['new']}")
        print(f"  Walkers: {update['walkers']}")
        print()

    print("Updated attribution.csv written.")
    print()
    print("Summary:")
    print("  Petra Janouchová: 4 records")
    print("  Extraction error corrected: 1 record (Petra → Vera)")


if __name__ == '__main__':
    main()
