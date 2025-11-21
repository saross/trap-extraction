#!/usr/bin/env python3
"""
QA Validation script for final attribution data.

Performs comprehensive quality checks including:
- Data format validation
- Duplicate detection
- Completeness checks
- Spot-check sampling
- Name pattern validation
- Date range validation

Output: qa_validation_report.txt
"""

import os
import sys
import pandas as pd
import re
import random
from datetime import datetime
from pathlib import Path
from collections import Counter

OUTPUT_DIR = Path(__file__).parent.parent / "outputs"
REPORTS_DIR = Path(__file__).parent.parent / "outputs"


def validate_data_format(df):
    """Validate basic data format and structure."""
    issues = []

    print("\n" + "=" * 80)
    print("1. DATA FORMAT VALIDATION")
    print("=" * 80)

    # Check required columns
    required_cols = ['Date', 'Team', 'Leader', 'Walkers']
    missing_cols = [col for col in required_cols if col not in df.columns]

    if missing_cols:
        issues.append(f"Missing required columns: {missing_cols}")
        print(f"  ✗ Missing columns: {missing_cols}")
    else:
        print(f"  ✓ All required columns present")

    # Check date format
    try:
        dates = pd.to_datetime(df['Date'], errors='coerce')
        invalid_dates = df[dates.isna()]['Date'].tolist()

        if invalid_dates:
            issues.append(f"Invalid date formats: {invalid_dates[:5]}")
            print(f"  ✗ {len(invalid_dates)} invalid date formats")
        else:
            print(f"  ✓ All dates valid (YYYY-MM-DD format)")
    except Exception as e:
        issues.append(f"Date validation error: {e}")
        print(f"  ✗ Date validation error: {e}")

    # Check team values
    valid_teams = ['A', 'B', 'C', 'D', 'E']
    invalid_teams = df[~df['Team'].isin(valid_teams)]['Team'].unique()

    if len(invalid_teams) > 0:
        issues.append(f"Invalid team values: {invalid_teams}")
        print(f"  ✗ Invalid team values: {invalid_teams}")
    else:
        print(f"  ✓ All team values valid (A-E)")

    # Check for required data
    empty_dates = df['Date'].isna().sum()
    empty_teams = df['Team'].isna().sum()

    if empty_dates > 0 or empty_teams > 0:
        issues.append(f"Empty required fields: {empty_dates} dates, {empty_teams} teams")
        print(f"  ✗ Empty required fields: {empty_dates} dates, {empty_teams} teams")
    else:
        print(f"  ✓ No empty required fields")

    return issues


def check_duplicates(df):
    """Check for duplicate Date+Team combinations."""
    issues = []

    print("\n" + "=" * 80)
    print("2. DUPLICATE DETECTION")
    print("=" * 80)

    # Check for duplicate Date+Team
    duplicates = df[df.duplicated(subset=['Date', 'Team'], keep=False)]

    if len(duplicates) > 0:
        issues.append(f"Found {len(duplicates)} duplicate Date+Team combinations")
        print(f"  ✗ {len(duplicates)} duplicate Date+Team combinations found:")

        # Show first few duplicates
        dup_groups = duplicates.groupby(['Date', 'Team']).size().head(5)
        for (date, team), count in dup_groups.items():
            print(f"    - {date}, Team {team}: {count} occurrences")
            issues.append(f"Duplicate: {date}, Team {team}")
    else:
        print(f"  ✓ No duplicate Date+Team combinations")

    return issues


def check_completeness(df):
    """Check data completeness across all fields."""
    issues = []

    print("\n" + "=" * 80)
    print("3. DATA COMPLETENESS")
    print("=" * 80)

    # Check each major field
    fields_to_check = {
        'Walkers': 'Walker data',
        'Leader': 'Team leader',
        'Start Unit': 'Survey units',
        'Author': 'Form author',
        'PDA_Operator': 'PDA operator',
        'Paper_Recorder': 'Paper recorder'
    }

    for field, name in fields_to_check.items():
        if field in df.columns:
            filled = df[field].notna() & (df[field] != '')
            count = filled.sum()
            pct = 100 * count / len(df)

            status = "✓" if pct >= 80 else "✗" if pct < 50 else "⚠"
            print(f"  {status} {name}: {count}/{len(df)} ({pct:.1f}%)")

            if pct < 80:
                issues.append(f"{name} completeness: {pct:.1f}%")
        else:
            print(f"  - {name}: Column not present")

    return issues


def validate_walker_names(df):
    """Validate walker name patterns and formats."""
    issues = []

    print("\n" + "=" * 80)
    print("4. WALKER NAME VALIDATION")
    print("=" * 80)

    walkers_with_data = df[df['Walkers'].notna() & (df['Walkers'] != '')]

    if len(walkers_with_data) == 0:
        print("  ✗ No walker data to validate")
        issues.append("No walker data available")
        return issues

    # Extract all individual names
    all_names = []
    suspicious_patterns = []

    for idx, row in walkers_with_data.iterrows():
        walkers = str(row['Walkers'])

        # Split by pipe
        names = [n.strip() for n in walkers.split('|')]
        all_names.extend(names)

        # Check for suspicious patterns
        if 'one mound' in walkers.lower() or 'not count' in walkers.lower():
            suspicious_patterns.append(f"Row {idx}: {walkers[:50]}")

        # Check for very long entries (likely noise)
        if len(walkers) > 200:
            suspicious_patterns.append(f"Row {idx}: Very long entry ({len(walkers)} chars)")

    # Analyse name patterns
    name_counter = Counter(all_names)
    total_names = len(all_names)
    unique_names = len(name_counter)

    print(f"  ✓ Total walker entries: {total_names}")
    print(f"  ✓ Unique names: {unique_names}")
    print(f"  ✓ Average names per record: {total_names/len(walkers_with_data):.1f}")

    # Show top names
    print(f"\n  Top 10 most frequent walker names:")
    for name, count in name_counter.most_common(10):
        print(f"    {name}: {count} occurrences")

    # Report suspicious patterns
    if suspicious_patterns:
        print(f"\n  ⚠ {len(suspicious_patterns)} suspicious patterns found:")
        for pattern in suspicious_patterns[:5]:
            print(f"    {pattern}")
        issues.extend(suspicious_patterns[:5])
    else:
        print(f"\n  ✓ No suspicious patterns found")

    return issues


def validate_date_ranges(df):
    """Validate date ranges are reasonable."""
    issues = []

    print("\n" + "=" * 80)
    print("5. DATE RANGE VALIDATION")
    print("=" * 80)

    try:
        dates = pd.to_datetime(df['Date'])

        min_date = dates.min()
        max_date = dates.max()

        print(f"  ✓ Date range: {min_date.date()} to {max_date.date()}")

        # Check for expected range (2009-2011)
        if min_date.year < 2009 or max_date.year > 2011:
            issues.append(f"Date range outside expected 2009-2011: {min_date.date()} to {max_date.date()}")
            print(f"  ⚠ Date range outside expected 2009-2011")
        else:
            print(f"  ✓ All dates within expected range (2009-2011)")

        # Check for outliers
        date_diff = (max_date - min_date).days
        print(f"  ✓ Span: {date_diff} days ({date_diff/365:.1f} years)")

        # Check distribution by year
        print(f"\n  Distribution by year:")
        for year in sorted(dates.dt.year.unique()):
            count = (dates.dt.year == year).sum()
            print(f"    {year}: {count} records")

    except Exception as e:
        issues.append(f"Date validation error: {e}")
        print(f"  ✗ Error validating dates: {e}")

    return issues


def perform_spot_checks(df, num_samples=10):
    """Perform spot-checks on random sample of records."""
    issues = []

    print("\n" + "=" * 80)
    print(f"6. SPOT-CHECK SAMPLING ({num_samples} random records)")
    print("=" * 80)

    # Sample records
    if len(df) < num_samples:
        sample = df
    else:
        sample = df.sample(n=num_samples, random_state=42)

    for idx, (_, row) in enumerate(sample.iterrows(), 1):
        print(f"\n  Record {idx}:")
        print(f"    Date: {row['Date']}, Team: {row['Team']}")
        print(f"    Leader: {row.get('Leader', 'N/A')}")
        print(f"    Walkers: {str(row.get('Walkers', 'N/A'))[:60]}...")

        # Check for issues
        record_issues = []

        if pd.isna(row.get('Walkers')) or row.get('Walkers') == '':
            record_issues.append("Missing walkers")

        if pd.isna(row.get('Leader')) or row.get('Leader') == '':
            record_issues.append("Missing leader")

        if row.get('QA_Notes') and 'UNCERTAIN' in str(row.get('QA_Notes')):
            record_issues.append("Marked as uncertain")

        if record_issues:
            print(f"    ⚠ Issues: {', '.join(record_issues)}")
        else:
            print(f"    ✓ No issues detected")

    return issues


def check_source_attribution(df):
    """Check source attribution completeness."""
    issues = []

    print("\n" + "=" * 80)
    print("7. SOURCE ATTRIBUTION")
    print("=" * 80)

    # Check PDF_Source column
    if 'PDF_Source' in df.columns:
        with_source = df['PDF_Source'].notna() & (df['PDF_Source'] != '')
        count = with_source.sum()
        pct = 100 * count / len(df)

        print(f"  ✓ Records with source attribution: {count}/{len(df)} ({pct:.1f}%)")

        # Show source distribution
        if count > 0:
            sources = df[with_source]['PDF_Source'].value_counts()
            print(f"\n  Top 10 sources:")
            for source, cnt in sources.head(10).items():
                print(f"    {source}: {cnt} records")

        if pct < 50:
            issues.append(f"Low source attribution: {pct:.1f}%")
    else:
        print(f"  - No PDF_Source column found")

    return issues


def generate_qa_report(df, all_issues):
    """Generate comprehensive QA report."""
    report_path = REPORTS_DIR / 'qa-validation-report.md'

    with open(report_path, 'w', encoding='utf-8') as f:
        f.write("# QA Validation Report\n\n")
        f.write(f"**Generated:** {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
        f.write(f"**Dataset:** final_attribution_v2_cleaned.csv\n")
        f.write(f"**Total Records:** {len(df)}\n\n")

        f.write("---\n\n")

        # Summary
        f.write("## Summary\n\n")

        if len(all_issues) == 0:
            f.write("✓ **All validation checks passed!**\n\n")
        else:
            f.write(f"⚠ **{len(all_issues)} issues found**\n\n")

        # Coverage statistics
        f.write("### Data Coverage\n\n")

        walkers_count = (df['Walkers'].notna() & (df['Walkers'] != '')).sum()
        leader_count = (df['Leader'].notna() & (df['Leader'] != '')).sum()
        units_count = (df['Start Unit'].notna() if 'Start Unit' in df.columns else pd.Series([False])).sum()

        f.write(f"- **Walkers:** {walkers_count}/{len(df)} ({100*walkers_count/len(df):.1f}%)\n")
        f.write(f"- **Leader:** {leader_count}/{len(df)} ({100*leader_count/len(df):.1f}%)\n")
        f.write(f"- **Survey Units:** {units_count}/{len(df)} ({100*units_count/len(df):.1f}%)\n\n")

        # Issues list
        if all_issues:
            f.write("### Issues Found\n\n")
            for i, issue in enumerate(all_issues, 1):
                f.write(f"{i}. {issue}\n")
            f.write("\n")

        # Recommendations
        f.write("---\n\n")
        f.write("## Recommendations\n\n")

        if walkers_count / len(df) < 0.9:
            f.write("1. **Improve walker data coverage** - Currently at {:.1f}%\n".format(100*walkers_count/len(df)))
            f.write("   - Review missing_walkers.csv for remaining gaps\n")
            f.write("   - Check additional diary sources\n\n")

        if all_issues:
            f.write("2. **Address validation issues** - Review items listed above\n\n")

        f.write("3. **Manual spot-check** - Verify random sample of 20-30 records against source documents\n\n")

        f.write("4. **Cross-reference with field notes** - Validate team compositions with project PIs\n\n")

    print(f"\n✓ QA report saved to: {report_path}")

    return report_path


def main():
    """Main execution function."""
    print("=" * 80)
    print("QA VALIDATION - Final Attribution Data")
    print("=" * 80)

    # Load data
    data_path = OUTPUT_DIR / 'final_attribution_v2_cleaned.csv'

    if not data_path.exists():
        print(f"\n✗ Error: {data_path} not found")
        print("  Please run consolidate_v2.py first")
        return

    df = pd.read_csv(data_path)
    print(f"\n✓ Loaded: {len(df)} records")

    # Run all validation checks
    all_issues = []

    all_issues.extend(validate_data_format(df))
    all_issues.extend(check_duplicates(df))
    all_issues.extend(check_completeness(df))
    all_issues.extend(validate_walker_names(df))
    all_issues.extend(validate_date_ranges(df))
    all_issues.extend(perform_spot_checks(df, num_samples=10))
    all_issues.extend(check_source_attribution(df))

    # Generate report
    print("\n" + "=" * 80)
    print("GENERATING QA REPORT")
    print("=" * 80)

    report_path = generate_qa_report(df, all_issues)

    # Summary
    print("\n" + "=" * 80)
    print("QA VALIDATION COMPLETE")
    print("=" * 80)

    if len(all_issues) == 0:
        print("\n✓ All validation checks passed!")
    else:
        print(f"\n⚠ {len(all_issues)} issues found - see report for details")

    print(f"\nReport: {report_path}")
    print("=" * 80 + "\n")


if __name__ == "__main__":
    main()
