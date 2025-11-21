#!/usr/bin/env python3
"""
Consolidated Author extraction from all Tier 3 PDF Daily Progress Forms.

This script combines Author data extracted via vision analysis from:
- Kazanlak 2009: Teams A, B, C, D, E
- Kazanlak 2010: Teams A, B, C, D
- Kazanlak 2011: Teams B, C
- Elhovo/Yambol 2010: Teams A, B

Data only updates records where Author field is currently empty,
preserving higher-priority Tier 2 diary data.

Author: Claude Code collaboration
Date: November 2025
"""

import csv

# All PDF-extracted Author data by (date, team) key
PDF_AUTHORS = {
    # =========================================================================
    # KAZANLAK 2009
    # =========================================================================

    # Team A - from A_2009Summary.pdf
    ('2009-03-04', 'A'): 'SB',  # Stacey Barker
    ('2009-03-06', 'A'): 'SB',
    ('2009-03-07', 'A'): 'Tereza D.',
    ('2009-03-08', 'A'): 'Tereza',
    ('2009-03-09', 'A'): 'Tereza',
    ('2009-03-11', 'A'): 'Tereza D.',
    ('2009-03-12', 'A'): 'SB',
    ('2009-03-15', 'A'): 'Bara W.',
    ('2009-03-16', 'A'): 'Stalka K.',
    ('2009-03-19', 'A'): 'Stalka',
    ('2009-03-20', 'A'): 'Stalka',
    ('2009-03-21', 'A'): 'ST.',
    ('2009-03-24', 'A'): 'Stalka',
    ('2009-03-25', 'A'): 'ST.',
    ('2009-03-26', 'A'): 'PT.',  # Petra Tuslova
    ('2009-03-27', 'A'): 'Pt.',

    # Team B - from B_2009Summary.pdf
    ('2009-03-06', 'B'): 'Vera',
    ('2009-03-07', 'B'): 'Vera',
    ('2009-03-08', 'B'): 'Vera',
    ('2009-03-09', 'B'): 'Vera',
    ('2009-03-11', 'B'): 'V.',
    ('2009-03-12', 'B'): 'V.',
    ('2009-03-16', 'B'): 'Tereza',
    ('2009-03-19', 'B'): 'Ivana Klimova',
    ('2009-03-20', 'B'): 'Ivana Klimova',
    ('2009-03-23', 'B'): 'TB',  # Tereza Blazkova
    ('2009-03-24', 'B'): 'Ivana Klimova',
    ('2009-03-25', 'B'): 'Ivana Klimova',
    ('2009-03-26', 'B'): 'Ivana Klimova',
    ('2009-03-27', 'B'): 'Petra T.',
    ('2009-04-05', 'B'): 'Sobotkova',

    # Team C - from C_2009Summary.pdf
    ('2009-03-04', 'C'): 'Adela',
    ('2009-03-06', 'C'): 'CB',  # Charlotte B.
    ('2009-03-07', 'C'): 'CB',
    ('2009-03-09', 'C'): 'CB',
    ('2009-03-11', 'C'): 'CS',
    ('2009-03-12', 'C'): 'CR',
    ('2009-03-16', 'C'): 'CB',
    ('2009-03-19', 'C'): 'Katarina',
    ('2009-03-23', 'C'): 'CB',
    ('2009-03-24', 'C'): 'Bryan Zlatos',
    ('2009-03-25', 'C'): 'Bryan Zlatos',
    ('2009-03-26', 'C'): 'Bryan Zlatos',
    ('2009-03-27', 'C'): 'Bryan Zlatos',

    # Team D - from D_Summary.pdf
    ('2009-03-04', 'D'): 'Magda B.',
    ('2009-03-07', 'D'): 'Barbora Klánová',
    ('2009-03-08', 'D'): 'Barbora Klánová',
    ('2009-03-09', 'D'): 'Barbora Klánová',
    ('2009-03-11', 'D'): 'Barbora Klánová',
    ('2009-03-12', 'D'): 'Barbora Klánová',
    ('2009-03-16', 'D'): 'Barbora Klánová',
    ('2009-03-19', 'D'): 'Barbora Klánová',
    ('2009-03-20', 'D'): 'Barbora Klánová',
    ('2009-03-23', 'D'): 'Barbora Klánová',
    ('2009-03-24', 'D'): 'Barbora Klánová',
    ('2009-03-25', 'D'): 'Barbora Klánová',
    ('2009-03-26', 'D'): 'Barbora Klánová',
    ('2009-03-27', 'D'): 'Barbora Klánová',

    # Team E - from E_Summary.pdf
    ('2009-03-20', 'E'): 'Katarina',
    ('2009-03-23', 'E'): 'Katarina Culakova',
    ('2009-03-24', 'E'): 'Katarina Culakova',
    ('2009-03-25', 'E'): 'Katarina Culakova',
    ('2009-03-26', 'E'): 'Katarina Culakova',
    ('2009-04-03', 'E'): 'P.T.',  # Petra Tuslova

    # =========================================================================
    # KAZANLAK 2010
    # =========================================================================

    # Team A - from A_2010Summary.pdf
    ('2010-03-22', 'A'): 'Lindsay',
    ('2010-03-24', 'A'): 'Lindsay',
    ('2010-03-25', 'A'): 'Lindsay',
    ('2010-03-26', 'A'): 'Lindsay',
    ('2010-03-27', 'A'): 'Lindsay',
    ('2010-03-28', 'A'): 'Lindsay',
    ('2010-04-07', 'A'): 'Viki',
    ('2010-04-08', 'A'): 'Lindsay',

    # Team B - from B_2010Summary.pdf
    ('2010-03-17', 'B'): 'Vera',
    ('2010-03-19', 'B'): 'Petra J.',
    ('2010-03-20', 'B'): 'Petra',
    ('2010-03-21', 'B'): 'Petra',
    ('2010-03-25', 'B'): 'Dasa',
    ('2010-03-26', 'B'): 'Renee G',
    ('2010-03-30', 'B'): 'Vladka',
    ('2010-03-31', 'B'): 'Vladka',
    ('2010-04-01', 'B'): 'Vladka',
    ('2010-04-02', 'B'): 'Pt.',
    ('2010-04-07', 'B'): 'Dasa',

    # Team C - from C_2010Summary.pdf
    ('2010-03-17', 'C'): 'Jana',
    ('2010-03-18', 'C'): 'Sonja',
    ('2010-03-19', 'C'): 'Jana',
    ('2010-03-20', 'C'): 'P.H.',
    ('2010-03-21', 'C'): 'P.H.',
    ('2010-03-22', 'C'): 'Sona',
    ('2010-03-24', 'C'): 'Sona',
    ('2010-03-25', 'C'): 'Sona',
    ('2010-03-26', 'C'): 'Sonja',
    ('2010-03-27', 'C'): 'Sonja',
    ('2010-03-28', 'C'): 'Sonja',
    ('2010-03-30', 'C'): 'Sonja',
    ('2010-03-31', 'C'): 'Sonja',
    ('2010-04-01', 'C'): 'Sonja',
    ('2010-04-02', 'C'): 'Sonja',
    ('2010-04-07', 'C'): 'Sonja',
    ('2010-04-08', 'C'): 'Sonja',
    ('2010-04-09', 'C'): 'Sonja',
    ('2010-04-10', 'C'): 'Sonja',
    ('2010-04-14', 'C'): 'Sonja',

    # Team D - from D_2010Summary.pdf
    ('2010-03-18', 'D'): 'Vera',
    ('2010-03-19', 'D'): 'Vera',
    ('2010-03-20', 'D'): 'Vera',
    ('2010-03-21', 'D'): 'Vera',
    ('2010-03-22', 'D'): 'Vera',
    ('2010-03-24', 'D'): 'Olga',
    ('2010-03-25', 'D'): 'Vera',
    ('2010-03-26', 'D'): 'Vera',
    ('2010-03-27', 'D'): 'V.K.',
    ('2010-03-28', 'D'): 'V.K.',
    ('2010-03-31', 'D'): 'Liubovy',

    # =========================================================================
    # KAZANLAK 2011
    # =========================================================================

    # Team B - from B_2011Summary.pdf
    ('2011-03-14', 'B'): 'Bethan',
    ('2011-03-15', 'B'): 'Bethan',
    ('2011-03-16', 'B'): 'Cecilia',
    ('2011-03-17', 'B'): 'Petra',
    ('2011-03-18', 'B'): 'Adela',
    ('2011-03-19', 'B'): 'Corinne',
    ('2011-03-21', 'B'): 'Petra',
    ('2011-03-22', 'B'): 'Petra',

    # Team C - from C_2011Summary.pdf
    ('2011-03-14', 'C'): 'Corinne S.',
    ('2011-03-15', 'C'): 'Jodie',
    ('2011-03-16', 'C'): 'Elaine',
    ('2011-03-17', 'C'): 'Martin',
    ('2011-03-18', 'C'): 'Sophie',
    ('2011-03-19', 'C'): 'Georgia',
    ('2011-03-21', 'C'): 'Sophie',
    ('2011-03-22', 'C'): 'Sophie',
    ('2011-03-23', 'C'): 'Sophie',

    # =========================================================================
    # ELHOVO/YAMBOL 2010
    # =========================================================================

    # Team A - from Day_03.pdf and other Team A PDFs
    ('2010-10-22', 'A'): 'Royce L.',
    ('2010-10-23', 'A'): 'Royce L.',
    ('2010-10-24', 'A'): 'Royce L.',

    # Team B - from Day_02.pdf and other Team B PDFs
    # Note: Most Team B dates covered by diary (higher priority)
    ('2010-11-02', 'B'): 'Royce L.',
    ('2010-11-03', 'B'): 'Ashley',
}


def main():
    """Update CSV with Author data from all PDF scans."""
    input_file = 'outputs/final_attribution_v2_cleaned_edited.csv'

    # Read existing data
    with open(input_file, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        fieldnames = reader.fieldnames
        rows = list(reader)

    # Update rows with Author data (only if Author field is empty)
    updated_count = 0
    for row in rows:
        date = row['Date']
        team = row['Team']
        key = (date, team)

        if key in PDF_AUTHORS:
            author = PDF_AUTHORS[key]
            # Only update if currently empty
            if not row.get('Author') or row.get('Author') == '':
                row['Author'] = author
                updated_count += 1
                print(f"  Updated {date} Team {team}: Author = {author}")

    # Write updated data
    with open(input_file, 'w', encoding='utf-8', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)

    print(f"\nUpdated {updated_count} records with Author data from PDF scans.")
    print(f"Total PDF Author entries available: {len(PDF_AUTHORS)}")


if __name__ == '__main__':
    main()
