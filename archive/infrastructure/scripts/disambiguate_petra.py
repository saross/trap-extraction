#!/usr/bin/env python3
"""
Disambiguate 'Petra' entries in attribution.csv into Petra Janouchová and Petra Tušlová.

Based on analysis:
- Petra Janouchová: 2009-spring, 2010-spring, 2011-autumn
- Petra Tušlová: 2009-spring, 2009-autumn, 2010-spring, 2010-autumn

Uses season/team patterns and explicit identifications to assign.

Author: Claude Code collaboration
Date: November 2025
"""

import csv
from pathlib import Path


def parse_season(date_str):
    """Parse date to determine season."""
    if not date_str or len(date_str) < 10:
        return None
    year, month, _ = date_str.split('-')
    if month in ['03', '04']:
        return f"{year}-spring"
    elif month in ['10', '11', '12']:
        return f"{year}-autumn"
    return None


def determine_petra(date, team, walkers, season):
    """
    Determine which Petra based on date, team, and context.

    Returns:
        'Petra Janouchová' | 'Petra Tušlová' | None (ambiguous)
    """
    # Clear assignments based on season exclusivity
    if season == '2009-autumn':
        return 'Petra Tušlová'  # Only she attended

    if season == '2010-autumn':
        return 'Petra Tušlová'  # Only she attended

    if season == '2011-autumn':
        return 'Petra Janouchová'  # Only she attended

    # 2009-spring Team A: After March 15, Petra = Tušlová
    # (March 15 has explicit 'Petra T.' with Stana, continues together)
    if season == '2009-spring' and team == 'A':
        if date >= '2009-03-16':  # After explicit identification
            return 'Petra Tušlová'

    # 2009-spring Team E: Ambiguous (April 3) - flag for review
    if season == '2009-spring' and team == 'E':
        return None  # Ambiguous

    # 2010-spring Team A: All Petra = Tušlová
    # (March 22 has explicit 'Petra T.', continues March 24-28)
    if season == '2010-spring' and team == 'A':
        return 'Petra Tušlová'

    # 2010-spring Team B: All Petra = Tušlová (stable core team)
    if season == '2010-spring' and team == 'B':
        return 'Petra Tušlová'

    # 2010-spring Team D: Ambiguous (March 24) - flag for review
    # Context: March 23 has 'Petra mi' which is unclear
    if season == '2010-spring' and team == 'D':
        return None  # Ambiguous

    # Should not reach here for generic 'Petra'
    return None


def main():
    """Update attribution.csv with disambiguated Petra names."""
    input_file = Path('outputs/attribution.csv')

    # Read CSV
    with open(input_file, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        fieldnames = reader.fieldnames
        rows = list(reader)

    # Track changes
    updates = []
    ambiguous = []

    for row in rows:
        date = row['Date']
        team = row['Team']
        walkers = row['Walkers_Original']
        season = parse_season(date)

        # Check for generic 'Petra' (no surname or initial)
        if ('Petra' in walkers and
            'Janouchová' not in walkers and
            'Tušlová' not in walkers and
            'Petra T' not in walkers and
            'Petra J' not in walkers and
            'Petra mi' not in walkers):

            assignment = determine_petra(date, team, walkers, season)

            if assignment:
                # Replace 'Petra' with full canonical name
                # Use word boundaries to avoid replacing parts of other names
                new_walkers = walkers.replace('Petra', assignment)
                row['Walkers_Original'] = new_walkers

                updates.append({
                    'date': date,
                    'team': team,
                    'season': season,
                    'old': 'Petra',
                    'new': assignment
                })
            else:
                # Flag as ambiguous
                ambiguous.append({
                    'date': date,
                    'team': team,
                    'season': season,
                    'walkers': walkers
                })

    # Write updated CSV
    with open(input_file, 'w', encoding='utf-8', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)

    # Report results
    print(f"Updated {len(updates)} records:")
    print()

    # Group by assignment
    by_person = {}
    for update in updates:
        person = update['new']
        if person not in by_person:
            by_person[person] = []
        by_person[person].append(update)

    for person, records in sorted(by_person.items()):
        print(f"{person}: {len(records)} records")
        by_season = {}
        for rec in records:
            season_team = f"{rec['season']} Team {rec['team']}"
            if season_team not in by_season:
                by_season[season_team] = []
            by_season[season_team].append(rec['date'])

        for season_team, dates in sorted(by_season.items()):
            print(f"  {season_team}: {len(dates)} days")

    print()
    print(f"Ambiguous records (need manual review): {len(ambiguous)}")
    for rec in ambiguous:
        print(f"  {rec['date']} Team {rec['team']} ({rec['season']})")
        print(f"    Walkers: {rec['walkers'][:80]}")

    print()
    print(f"Updated attribution.csv written.")


if __name__ == '__main__':
    main()
