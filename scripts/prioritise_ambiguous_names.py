#!/usr/bin/env python3
"""
Prioritise candidates for ambiguous names using team composition analysis.

For each 'review_needed' name in name-mapping.csv:
1. Find dates and PDF sources from attribution.csv
2. Build team composition profiles from confirmed data
3. Prioritise candidates who are frequent team members
4. Update name-mapping.csv with improved candidate lists

Author: Claude Code collaboration
Date: November 2025
"""

import csv
import re
from collections import defaultdict
from pathlib import Path


def parse_season(date_str):
    """Parse date to determine season."""
    if not date_str or len(date_str) < 10:
        return None

    year, month, _ = date_str.split('-')
    if month in ['03', '04']:
        return f"{year}-spring"
    elif month in ['10', '11']:
        return f"{year}-autumn"
    return None


def build_team_profiles():
    """Build team composition profiles from attribution.csv."""
    team_members = defaultdict(lambda: defaultdict(int))

    with open('outputs/attribution.csv', 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            date = row['Date']
            team = row['Team']
            walkers = row['Walkers_Original']

            if date and team and walkers:
                season = parse_season(date)
                if season:
                    # Parse walkers
                    walker_list = [w.strip() for w in re.split(r'[|,]', walkers) if w.strip()]
                    for walker in walker_list:
                        team_members[(season, team)][walker] += 1

    return team_members


def find_dates_and_sources(extracted_name):
    """Find all dates and PDF sources for an extracted name in attribution.csv."""
    dates = set()
    pdf_sources = set()
    teams = set()
    seasons = set()

    # Search in Walkers_Original, Author, Leader fields
    with open('outputs/attribution.csv', 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            # Check if name appears in any field
            text_to_search = ' | '.join([
                row.get('Walkers_Original', ''),
                row.get('Author', ''),
                row.get('Leader', '')
            ])

            if extracted_name in text_to_search:
                date = row['Date']
                team = row['Team']
                pdf_source = row.get('PDF_Source', '')

                if date:
                    dates.add(date)
                    season = parse_season(date)
                    if season:
                        seasons.add(season)
                if team:
                    teams.add(team)
                if pdf_source:
                    for source in pdf_source.split(','):
                        pdf_sources.add(source.strip())

    return {
        'dates': ' | '.join(sorted(dates)),
        'pdf_sources': ' | '.join(sorted(pdf_sources)),
        'teams': list(teams),
        'seasons': list(seasons)
    }


def prioritise_candidates(extracted_name, team, season, candidates_str, team_profiles):
    """
    Prioritise candidates based on team membership frequency.

    Returns a new candidates string with team members prioritized.
    """
    if not candidates_str or not team or not season:
        return candidates_str

    # Parse existing candidates
    # Format: "Name (score) | Name (score) | ..."
    candidate_list = []
    for cand in candidates_str.split('|'):
        cand = cand.strip()
        if cand:
            # Extract name and score
            match = re.match(r'^(.+?)\s*\((\d+)\)\s*$', cand)
            if match:
                name = match.group(1)
                score = int(match.group(2))
                candidate_list.append((name, score))

    if not candidate_list:
        return candidates_str

    # Get team member frequencies
    team_key = (season, team)
    team_freq = team_profiles.get(team_key, {})

    # Re-score candidates: boost score for team members
    rescored = []
    for name, orig_score in candidate_list:
        freq = team_freq.get(name, 0)

        # Calculate boost: add frequency * 10 to original score
        boost = freq * 10
        new_score = orig_score + boost

        rescored.append((name, new_score, freq, orig_score))

    # Sort by new score (descending)
    rescored.sort(key=lambda x: x[1], reverse=True)

    # Format output: show team members first with frequency indicator
    output_parts = []
    for name, new_score, freq, orig_score in rescored:
        if freq > 0:
            output_parts.append(f"{name} ({orig_score}+{freq*10}={new_score} | {freq}d)")
        else:
            output_parts.append(f"{name} ({orig_score})")

    return ' | '.join(output_parts)


def main():
    """Update name-mapping.csv with improved candidate prioritisation."""
    # Build team profiles
    print("Building team composition profiles...")
    team_profiles = build_team_profiles()

    print(f"Loaded {len(team_profiles)} team profiles")
    print()

    # Read name-mapping.csv
    mapping_file = 'outputs/name-mapping.csv'
    with open(mapping_file, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        fieldnames = reader.fieldnames
        rows = list(reader)

    # Process review_needed entries
    updated_count = 0
    added_dates_count = 0
    added_sources_count = 0
    reprioritised_count = 0

    for row in rows:
        if row['status'] == 'review_needed':
            extracted_name = row['extracted_name']

            # Find dates and sources if missing
            if not row['dates'] or not row['pdf_sources']:
                info = find_dates_and_sources(extracted_name)

                if not row['dates'] and info['dates']:
                    row['dates'] = info['dates']
                    added_dates_count += 1

                if not row['pdf_sources'] and info['pdf_sources']:
                    row['pdf_sources'] = info['pdf_sources']
                    added_sources_count += 1

                # Update team and season if found
                if info['teams'] and not row['team']:
                    row['team'] = info['teams'][0]  # Use first team found

                if info['seasons'] and not row['season']:
                    row['season'] = ', '.join(info['seasons'])

                updated_count += 1

            # Prioritise candidates based on team membership
            if row['candidates'] and row['team'] and row['season']:
                # Get first season if multiple
                season = row['season'].split(',')[0].strip()

                new_candidates = prioritise_candidates(
                    extracted_name,
                    row['team'],
                    season,
                    row['candidates'],
                    team_profiles
                )

                if new_candidates != row['candidates']:
                    row['candidates'] = new_candidates
                    reprioritised_count += 1
                    updated_count += 1

    # Write updated CSV
    with open(mapping_file, 'w', encoding='utf-8', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)

    print(f"Updated {updated_count} review_needed entries:")
    print(f"  Added dates: {added_dates_count}")
    print(f"  Added PDF sources: {added_sources_count}")
    print(f"  Re-prioritised candidates: {reprioritised_count}")
    print()
    print(f"Updated name-mapping.csv written.")


if __name__ == '__main__':
    main()
