#!/usr/bin/env python3
"""
Analyse coverage of walker extraction against missing walkers list.
"""

import csv
from pathlib import Path
from collections import defaultdict

BASE_DIR = Path("/media/shawn/191c3b96-5fa5-4d0d-8805-0cf05d3d8468/synology/Adela/TRAP-WD-2020-04")
OUTPUT_DIR = BASE_DIR / "claude_extraction" / "outputs"

# Load missing walkers
missing = set()
with open(OUTPUT_DIR / "missing_walkers.csv", 'r', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    for row in reader:
        if row['Date'] and row['Team']:
            missing.add((row['Date'], row['Team']))

print(f"Total missing records: {len(missing)}")

# Load extracted walkers
extracted = set()
extraction_by_pdf = defaultdict(int)
with open(OUTPUT_DIR / "phase2b_pdf_walkers.csv", 'r', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    for row in reader:
        if row['Date'] and row['Team'] and row['Date'] != '':
            extracted.add((row['Date'], row['Team']))
            extraction_by_pdf[row['PDF_Source']] += 1

print(f"Total extracted records: {len(extracted)}")
print(f"\nExtracted by PDF source:")
for pdf, count in sorted(extraction_by_pdf.items()):
    print(f"  {pdf}: {count} records")

# Find covered and still missing
covered = missing & extracted
still_missing = missing - extracted

print(f"\nCovered from missing list: {len(covered)}")
print(f"Still missing: {len(still_missing)}")

# Group still missing by year and team
by_year_team = defaultdict(list)
for date, team in sorted(still_missing):
    year = date.split('-')[0]
    by_year_team[(year, team)].append(date)

print(f"\nStill missing by year/team:")
for (year, team), dates in sorted(by_year_team.items()):
    print(f"  {year} Team {team}: {len(dates)} dates")
    print(f"    Date range: {min(dates)} to {max(dates)}")

print(f"\nDetailed list of still missing:")
for (year, team), dates in sorted(by_year_team.items()):
    print(f"\n{year} Team {team}:")
    for date in sorted(dates):
        print(f"  {date}")
