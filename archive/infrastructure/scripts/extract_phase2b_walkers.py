#!/usr/bin/env python3
"""
Phase 2b: Extract walker information from TRAP survey PDFs using vision.

This script processes missing walker data by reading scanned PDF forms and
extracting team member names/initials using Claude Code's vision capabilities.
"""

import csv
import json
from pathlib import Path
from datetime import datetime
from typing import Dict, List, Optional, Tuple

# Base directory for TRAP data
BASE_DIR = Path("/media/shawn/191c3b96-5fa5-4d0d-8805-0cf05d3d8468/synology/Adela/TRAP-WD-2020-04")
OUTPUT_DIR = BASE_DIR / "claude_extraction" / "outputs"
INPUT_CSV = OUTPUT_DIR / "missing_walkers.csv"
OUTPUT_CSV = OUTPUT_DIR / "phase2b_pdf_walkers.csv"


def find_pdf_files(date_str: str, team: str) -> Dict[str, List[Path]]:
    """
    Find relevant PDF files for a given date and team.

    Args:
        date_str: Date in YYYY-MM-DD format
        team: Team letter (A, B, C, D, E)

    Returns:
        Dictionary with 'daily_progress' and 'survey_unit' PDF paths
    """
    date_obj = datetime.strptime(date_str, "%Y-%m-%d")
    year = date_obj.year

    # Convert date to various formats for matching
    date_yyyymmdd = date_obj.strftime("%Y%m%d")

    results = {
        'daily_progress': [],
        'survey_unit': []
    }

    # Define year directory mappings
    # Kazanluk: 2009, 2010, 2011-11-30
    # Elhovo 2010-12-12: 2009
    year_dir_patterns = []

    if year == 2009:
        year_dir_patterns = [
            BASE_DIR / "Elhovo 2010-12-12" / "2009",
            BASE_DIR / "Kazanluk" / "2009"
        ]
    elif year == 2010:
        year_dir_patterns = [
            BASE_DIR / "Kazanluk" / "2010"
        ]
    elif year == 2011:
        year_dir_patterns = [
            BASE_DIR / "Kazanluk" / "2011-11-30"
        ]

    for year_dir in year_dir_patterns:
        if not year_dir.exists():
            continue

        # Look for Project Records/Team X/FieldRecords
        team_dir = year_dir / "Project Records" / f"Team {team}"
        if not team_dir.exists():
            continue

        field_records_dir = team_dir / "FieldRecords"
        if not field_records_dir.exists():
            continue

        # Daily progress summary files
        summary_files = (
            list(field_records_dir.glob(f"{team}_*Summary.pdf")) +
            list(field_records_dir.glob(f"*Summary.pdf")) +
            list(field_records_dir.glob("Day_*.pdf"))
        )
        results['daily_progress'].extend(summary_files)

        # Survey unit files with date in filename
        survey_files = (
            list(field_records_dir.glob(f"{team}_{date_yyyymmdd}.pdf")) +
            list(field_records_dir.glob(f"*{date_yyyymmdd}*.pdf")) +
            list(field_records_dir.glob(f"{team}{date_yyyymmdd}.pdf"))
        )
        results['survey_unit'].extend(survey_files)

    # Remove duplicates
    results['daily_progress'] = list(set(results['daily_progress']))
    results['survey_unit'] = list(set(results['survey_unit']))

    return results


def load_missing_walkers() -> List[Dict[str, str]]:
    """Load the list of date/team combinations that need walker data."""
    records = []
    with open(INPUT_CSV, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            if row['Date'] and row['Team']:  # Skip empty rows
                records.append(row)
    return records


def save_results(results: List[Dict[str, str]]):
    """Save extracted walker data to CSV."""
    fieldnames = ['Date', 'Team', 'Walkers', 'Team_Leader', 'Author',
                  'PDF_Source', 'Extraction_Notes']

    with open(OUTPUT_CSV, 'w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(results)

    print(f"Results saved to: {OUTPUT_CSV}")
    print(f"Total records extracted: {len(results)}")


def main():
    """Main extraction workflow."""
    print("=" * 80)
    print("TRAP Phase 2b: PDF Walker Extraction")
    print("=" * 80)

    # Load missing walkers list
    missing_records = load_missing_walkers()
    print(f"\nLoaded {len(missing_records)} date/team combinations to process")

    # This script will prepare the file search logic
    # The actual PDF reading and extraction will be done interactively
    # using Claude Code's vision capabilities

    print("\nSearching for PDF files...")

    # Test the search function with a known date (2010-03-17 Team B)
    test_records = [
        {"Date": "2010-03-17", "Team": "C"},
        {"Date": "2010-03-19", "Team": "B"},
        {"Date": "2009-10-12", "Team": "A"},
    ]

    for i, record in enumerate(test_records, 1):
        date_str = record['Date']
        team = record['Team']
        print(f"\n{i}. {date_str} Team {team}:")

        pdf_files = find_pdf_files(date_str, team)

        if pdf_files['daily_progress']:
            print(f"   Daily Progress: {len(pdf_files['daily_progress'])} file(s)")
            for pdf in pdf_files['daily_progress']:
                print(f"     - {pdf.relative_to(BASE_DIR)}")

        if pdf_files['survey_unit']:
            print(f"   Survey Unit: {len(pdf_files['survey_unit'])} file(s)")
            for pdf in pdf_files['survey_unit']:
                print(f"     - {pdf.relative_to(BASE_DIR)}")

        if not pdf_files['daily_progress'] and not pdf_files['survey_unit']:
            print("   No PDF files found")

    print("\n" + "=" * 80)
    print("PDF file search complete. Ready for vision-based extraction.")
    print("=" * 80)


if __name__ == "__main__":
    main()
