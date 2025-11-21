#!/usr/bin/env python3
"""
Data cleanup script: Fix identified QA issues.

Fixes:
1. Merge duplicate Date+Team combinations
2. Clean suspicious long walker entries
3. Remove noise from walker names

Output: final_attribution_v2_cleaned.csv
"""

import pandas as pd
import re
from pathlib import Path

OUTPUT_DIR = Path(__file__).parent.parent / "outputs"


def clean_long_walker_entries(walkers_str):
    """
    Clean walker entries that have narrative text mixed in.

    Args:
        walkers_str: Walker string with potential narrative text

    Returns:
        Cleaned walker string with only names
    """
    if pd.isna(walkers_str) or walkers_str == '':
        return walkers_str

    # Split by pipe
    parts = [p.strip() for p in walkers_str.split('|')]

    cleaned_parts = []

    for part in parts:
        # If part contains common narrative words/phrases, truncate
        narrative_markers = [
            'именувани',  # "named" in Bulgarian
            'разположени',  # "located" in Bulgarian
            'топографска',  # "topographic" in Bulgarian
            'обхожда',  # "walks around" in Bulgarian
            'продължи',  # "continues" in Bulgarian
            'започва',  # "starts" in Bulgarian
            'територия',  # "territory" in Bulgarian
            'мащаб',  # "scale" in Bulgarian
            'като м.',  # "as locality" in Bulgarian
        ]

        # Check if this part has narrative text
        has_narrative = any(marker in part.lower() for marker in narrative_markers)

        if has_narrative:
            # Try to extract just the name part before narrative
            # Usually names are at the start, before descriptive text
            name_match = re.match(r'^([А-ЯЁ]\.\s*[А-ЯЁ][а-яё]+|[A-Z]\.\s*[A-Z][a-z]+)', part)
            if name_match:
                cleaned_parts.append(name_match.group(1).strip())
            # Otherwise skip this part (it's pure narrative)
        else:
            # Keep parts that are just names
            if len(part) < 50:  # Names shouldn't be super long
                cleaned_parts.append(part)

    return ' | '.join(cleaned_parts) if cleaned_parts else ''


def merge_duplicates(df):
    """
    Merge duplicate Date+Team combinations by combining data from both.

    Args:
        df: DataFrame with potential duplicates

    Returns:
        DataFrame with duplicates merged
    """
    # Find duplicates
    dup_mask = df.duplicated(subset=['Date', 'Team'], keep=False)
    duplicates = df[dup_mask]

    if len(duplicates) == 0:
        print("  No duplicates to merge")
        return df

    print(f"  Found {len(duplicates)} duplicate records")

    # Group by Date+Team and merge
    merged_rows = []
    processed_keys = set()

    for idx, row in df.iterrows():
        key = (row['Date'], row['Team'])

        # Skip if already processed
        if key in processed_keys:
            continue

        # Find all records with this Date+Team
        mask = (df['Date'] == row['Date']) & (df['Team'] == row['Team'])
        group = df[mask]

        if len(group) > 1:
            # Merge: take non-null values from each column
            merged = {}

            for col in df.columns:
                # Collect non-null values
                values = group[col].dropna()
                values = values[values != '']

                if len(values) > 0:
                    # Prefer values from sources with more complete data
                    # Priority: entries with PDF_Source > entries without
                    if col in ['Walkers', 'Leader', 'Author']:
                        # For these fields, prefer data from PDF sources
                        pdf_sources = group[group['PDF_Source'].notna()]
                        if len(pdf_sources) > 0:
                            val = pdf_sources[col].iloc[0]
                            if pd.notna(val) and val != '':
                                merged[col] = val
                                continue

                    # Default: take first non-null
                    merged[col] = values.iloc[0]
                else:
                    merged[col] = None

            merged_rows.append(merged)
            processed_keys.add(key)
            print(f"    Merged: {row['Date']}, Team {row['Team']}")
        else:
            # No duplicate, keep as-is
            merged_rows.append(row.to_dict())
            processed_keys.add(key)

    return pd.DataFrame(merged_rows)


def main():
    """Main execution function."""
    print("=" * 80)
    print("DATA CLEANUP - Fixing QA Issues")
    print("=" * 80)

    # Load data
    input_path = OUTPUT_DIR / 'final_attribution_v2.csv'

    if not input_path.exists():
        print(f"\nError: {input_path} not found")
        return

    df = pd.read_csv(input_path)
    print(f"\nLoaded: {len(df)} records")

    # Step 1: Clean long walker entries
    print("\n1. Cleaning long walker entries...")

    walkers_with_data = df['Walkers'].notna() & (df['Walkers'] != '')
    long_mask = walkers_with_data & (df['Walkers'].str.len() > 200)
    long_count = long_mask.sum()

    if long_count > 0:
        print(f"  Found {long_count} long entries to clean")

        df.loc[long_mask, 'Walkers'] = df.loc[long_mask, 'Walkers'].apply(clean_long_walker_entries)

        # Check results
        still_long = (df['Walkers'].notna()) & (df['Walkers'].str.len() > 200)
        print(f"  After cleaning: {still_long.sum()} entries still >200 chars")
    else:
        print("  No long entries found")

    # Step 2: Merge duplicates
    print("\n2. Merging duplicate Date+Team combinations...")

    df = merge_duplicates(df)

    print(f"  After deduplication: {len(df)} records")

    # Step 3: Sort and reorder
    df = df.sort_values(['Date', 'Team'])

    # Save cleaned data
    output_path = OUTPUT_DIR / 'final_attribution_v2_cleaned.csv'
    df.to_csv(output_path, index=False)

    print(f"\n✓ Cleaned data saved to: {output_path}")

    # Summary
    print("\n" + "=" * 80)
    print("CLEANUP COMPLETE")
    print("=" * 80)
    print(f"  Input records: {len(pd.read_csv(input_path))}")
    print(f"  Output records: {len(df)}")
    print(f"  Records removed/merged: {len(pd.read_csv(input_path)) - len(df)}")
    print("=" * 80 + "\n")


if __name__ == "__main__":
    main()
