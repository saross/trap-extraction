#!/usr/bin/env python3
"""
Verify Survey Unit Coverage in Attribution CSV

This script analyses the attribution.csv file to verify survey unit coverage
after applying extracted units. It generates a coverage report showing:
- Total records with/without survey units
- Coverage statistics by year and team
- List of remaining missing records

Input files:
    - outputs/attribution.csv (main attribution data)

Output:
    - Console report with coverage statistics
    - outputs/survey-unit-coverage-report.txt (detailed report)

Author: Claude Code
Date: 2025-11-24
"""

import csv
from pathlib import Path
from collections import defaultdict
from datetime import datetime


def analyse_coverage(attribution_path: Path) -> dict:
    """
    Analyse survey unit coverage in attribution.csv.

    Args:
        attribution_path: Path to attribution.csv

    Returns:
        Dictionary containing coverage statistics and missing records
    """
    total_records = 0
    records_with_units = 0
    records_missing_units = []

    # Statistics by year
    by_year = defaultdict(lambda: {'total': 0, 'with_units': 0, 'missing': []})

    # Statistics by team
    by_team = defaultdict(lambda: {'total': 0, 'with_units': 0, 'missing': []})

    # Read attribution.csv
    with open(attribution_path, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)

        for row in reader:
            total_records += 1
            date = row['Date']
            team = row['Team']
            start_unit = row['Start Unit'].strip() if row['Start Unit'] else ''
            end_unit = row['End Unit'].strip() if row['End Unit'] else ''

            # Extract year
            year = date.split('-')[0] if date else 'Unknown'

            # Count records
            by_year[year]['total'] += 1
            by_team[team]['total'] += 1

            # Check if has units
            if start_unit and end_unit:
                records_with_units += 1
                by_year[year]['with_units'] += 1
                by_team[team]['with_units'] += 1
            else:
                record_info = {
                    'date': date,
                    'team': team,
                    'start_unit': start_unit,
                    'end_unit': end_unit
                }
                records_missing_units.append(record_info)
                by_year[year]['missing'].append(record_info)
                by_team[team]['missing'].append(record_info)

    # Calculate percentages
    coverage_pct = (records_with_units / total_records * 100) if total_records > 0 else 0

    return {
        'total_records': total_records,
        'records_with_units': records_with_units,
        'records_missing_units': len(records_missing_units),
        'coverage_percentage': coverage_pct,
        'missing_records': records_missing_units,
        'by_year': dict(by_year),
        'by_team': dict(by_team)
    }


def generate_report(stats: dict, output_path: Path):
    """
    Generate coverage report.

    Args:
        stats: Statistics dictionary from analyse_coverage()
        output_path: Path to save report file
    """
    lines = []

    # Header
    lines.append("=" * 80)
    lines.append("Survey Unit Coverage Report")
    lines.append("=" * 80)
    lines.append("")
    lines.append(f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    lines.append("")

    # Overall statistics
    lines.append("Overall Coverage")
    lines.append("-" * 80)
    lines.append(f"Total records:              {stats['total_records']:>6}")
    lines.append(f"Records with survey units:  {stats['records_with_units']:>6} "
                 f"({stats['coverage_percentage']:>6.2f}%)")
    lines.append(f"Records missing units:      {stats['records_missing_units']:>6} "
                 f"({100 - stats['coverage_percentage']:>6.2f}%)")
    lines.append("")

    # Coverage by year
    lines.append("Coverage by Year")
    lines.append("-" * 80)
    lines.append(f"{'Year':<10} {'Total':>8} {'With Units':>12} {'Missing':>10} {'Coverage':>12}")
    lines.append("-" * 80)

    for year in sorted(stats['by_year'].keys()):
        year_stats = stats['by_year'][year]
        total = year_stats['total']
        with_units = year_stats['with_units']
        missing = len(year_stats['missing'])
        pct = (with_units / total * 100) if total > 0 else 0

        lines.append(f"{year:<10} {total:>8} {with_units:>12} {missing:>10} {pct:>11.2f}%")

    lines.append("")

    # Coverage by team
    lines.append("Coverage by Team")
    lines.append("-" * 80)
    lines.append(f"{'Team':<10} {'Total':>8} {'With Units':>12} {'Missing':>10} {'Coverage':>12}")
    lines.append("-" * 80)

    for team in sorted(stats['by_team'].keys()):
        team_stats = stats['by_team'][team]
        total = team_stats['total']
        with_units = team_stats['with_units']
        missing = len(team_stats['missing'])
        pct = (with_units / total * 100) if total > 0 else 0

        lines.append(f"{team:<10} {total:>8} {with_units:>12} {missing:>10} {pct:>11.2f}%")

    lines.append("")

    # Missing records
    if stats['missing_records']:
        lines.append("Missing Survey Units")
        lines.append("-" * 80)
        lines.append(f"{'Date':<15} {'Team':<6} {'Start Unit':<12} {'End Unit':<12}")
        lines.append("-" * 80)

        for record in stats['missing_records']:
            date = record['date']
            team = record['team']
            start = record['start_unit'] if record['start_unit'] else '(empty)'
            end = record['end_unit'] if record['end_unit'] else '(empty)'

            lines.append(f"{date:<15} {team:<6} {start:<12} {end:<12}")

        lines.append("")

    # Footer
    lines.append("=" * 80)
    lines.append(f"Report saved to: {output_path.name}")
    lines.append("=" * 80)

    # Write to file
    report_text = "\n".join(lines)
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(report_text)

    return report_text


def main():
    """Main execution function."""
    # Set up paths
    base_dir = Path(__file__).parent.parent
    attribution_csv = base_dir / 'outputs' / 'attribution.csv'
    report_path = base_dir / 'outputs' / 'survey-unit-coverage-report.txt'

    print("Verify Survey Unit Coverage")
    print("=" * 60)
    print()

    # Analyse coverage
    print(f"Analysing: {attribution_csv.name}")
    stats = analyse_coverage(attribution_csv)
    print("✓ Analysis complete")
    print()

    # Generate report
    print("Generating coverage report...")
    report = generate_report(stats, report_path)
    print()

    # Display report
    print(report)


if __name__ == '__main__':
    main()
