#!/usr/bin/env python3
"""
Interactive PDF extraction script for walker data.

This script helps Claude Code process PDF files systematically by organizing
them by team/year for efficient batch processing.
"""

import csv
from pathlib import Path
from datetime import datetime
from typing import Dict, List, Set, Tuple
from collections import defaultdict

# Base directory for TRAP data
BASE_DIR = Path("/media/shawn/191c3b96-5fa5-4d0d-8805-0cf05d3d8468/synology/Adela/TRAP-WD-2020-04")
OUTPUT_DIR = BASE_DIR / "claude_extraction" / "outputs"
INPUT_CSV = OUTPUT_DIR / "missing_walkers.csv"


def load_missing_walkers() -> Dict[Tuple[int, str], List[str]]:
    """
    Load missing walkers and group by (year, team).

    Returns:
        Dictionary mapping (year, team) to list of dates
    """
    grouped = defaultdict(list)

    with open(INPUT_CSV, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            if row['Date'] and row['Team']:
                date_obj = datetime.strptime(row['Date'], "%Y-%m-%d")
                year = date_obj.year
                team = row['Team']
                grouped[(year, team)].append(row['Date'])

    return dict(grouped)


def find_summary_pdfs() -> Dict[Tuple[int, str], List[Path]]:
    """
    Find all summary PDF files organised by (year, team).

    Returns:
        Dictionary mapping (year, team) to list of PDF paths
    """
    pdfs_by_team_year = defaultdict(list)

    # Define year directory mappings
    year_locations = [
        (2009, BASE_DIR / "Elhovo 2010-12-12" / "2009"),
        (2009, BASE_DIR / "Kazanluk" / "2009"),
        (2010, BASE_DIR / "Kazanluk" / "2010"),
        (2011, BASE_DIR / "Kazanluk" / "2011-11-30"),
    ]

    for year, year_dir in year_locations:
        if not year_dir.exists():
            continue

        project_records = year_dir / "Project Records"
        if not project_records.exists():
            continue

        # Find all team directories
        for team_dir in project_records.glob("Team *"):
            team = team_dir.name.replace("Team ", "")

            field_records = team_dir / "FieldRecords"
            if not field_records.exists():
                continue

            # Find summary PDFs
            summary_pdfs = (
                list(field_records.glob(f"{team}_*Summary.pdf")) +
                list(field_records.glob("*Summary.pdf")) +
                list(field_records.glob("Day_*.pdf"))
            )

            if summary_pdfs:
                pdfs_by_team_year[(year, team)].extend(summary_pdfs)

    return dict(pdfs_by_team_year)


def main():
    """Main workflow for organising PDF extraction."""
    print("=" * 80)
    print("TRAP Phase 2b: Interactive PDF Walker Extraction")
    print("=" * 80)

    # Load missing walkers
    missing_by_team_year = load_missing_walkers()
    print(f"\nMissing walker records: {sum(len(dates) for dates in missing_by_team_year.values())}")
    print(f"Unique team/year combinations: {len(missing_by_team_year)}")

    # Find summary PDFs
    summary_pdfs = find_summary_pdfs()
    print(f"\nFound summary PDFs for {len(summary_pdfs)} team/year combinations")

    print("\n" + "=" * 80)
    print("PDF Processing Plan")
    print("=" * 80)

    # Create processing plan
    for (year, team), dates in sorted(missing_by_team_year.items()):
        print(f"\n{year} Team {team}: {len(dates)} missing dates")

        if (year, team) in summary_pdfs:
            for pdf in summary_pdfs[(year, team)]:
                print(f"  PDF: {pdf.relative_to(BASE_DIR)}")
            print(f"  Dates needed: {min(dates)} to {max(dates)}")
        else:
            print("  ⚠️  No summary PDF found!")

    print("\n" + "=" * 80)
    print("Ready for interactive extraction using Claude Code vision")
    print("=" * 80)


if __name__ == "__main__":
    main()
