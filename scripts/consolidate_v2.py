#!/usr/bin/env python3
"""
Consolidation script v2: Merge all extraction phases into final attribution CSV.

Merges:
- Phase 1: Survey summaries (Start/End Units, Leader)
- Phase 2b: PDF/Diary walker extraction (Walkers, Team_Leader, Author)
- Phase 3: Cleaned role data (PDA_Operator, Paper_Recorder, etc.)

Output: final_attribution_v2.csv
"""

import os
import sys
import pandas as pd
import logging
from pathlib import Path

# Add scripts directory to path
sys.path.insert(0, os.path.dirname(__file__))
from utils import setup_logging

OUTPUT_DIR = Path(__file__).parent.parent / "outputs"
LOG_DIR = Path(__file__).parent.parent / "logs"


def load_data_sources():
    """Load all data sources and return as dictionary."""
    sources = {}

    # Phase 1: Survey summaries
    phase1_path = OUTPUT_DIR / 'phase1_summary.csv'
    if phase1_path.exists():
        sources['phase1'] = pd.read_csv(phase1_path)
        logging.info(f"Loaded Phase 1: {len(sources['phase1'])} records")
    else:
        logging.warning("Phase 1 data not found")
        sources['phase1'] = pd.DataFrame()

    # Phase 2b: PDF/Diary walker extraction
    phase2b_path = OUTPUT_DIR / 'phase2b_pdf_walkers.csv'
    if phase2b_path.exists():
        sources['phase2b'] = pd.read_csv(phase2b_path)
        logging.info(f"Loaded Phase 2b: {len(sources['phase2b'])} records")
    else:
        logging.warning("Phase 2b data not found")
        sources['phase2b'] = pd.DataFrame()

    # Phase 3: Cleaned role data
    phase3_path = OUTPUT_DIR / 'phase3_cleaned.csv'
    if phase3_path.exists():
        sources['phase3'] = pd.read_csv(phase3_path)
        logging.info(f"Loaded Phase 3: {len(sources['phase3'])} records")
    else:
        logging.info("Phase 3 data not found (optional)")
        sources['phase3'] = pd.DataFrame()

    return sources


def merge_walker_data(row_walkers, row_leader, phase2b_walkers, phase2b_leader):
    """
    Intelligently merge walker and leader data from multiple sources.

    Priority: phase2b (most complete) > existing data
    """
    # Walkers
    final_walkers = None
    if pd.notna(phase2b_walkers) and phase2b_walkers != '':
        final_walkers = phase2b_walkers
    elif pd.notna(row_walkers) and row_walkers != '':
        final_walkers = row_walkers

    # Leader
    final_leader = None
    if pd.notna(phase2b_leader) and phase2b_leader != '':
        final_leader = phase2b_leader
    elif pd.notna(row_leader) and row_leader != '':
        final_leader = row_leader

    return final_walkers, final_leader


def consolidate_data(sources):
    """
    Consolidate all data sources into final attribution dataframe.

    Args:
        sources: Dictionary of dataframes from each phase

    Returns:
        Consolidated dataframe
    """
    # Start with Phase 1 as base (survey summaries)
    if len(sources['phase1']) > 0:
        df = sources['phase1'].copy()
        logging.info(f"Starting with Phase 1 base: {len(df)} records")
    else:
        # If no Phase 1, start with empty dataframe
        df = pd.DataFrame(columns=['Date', 'Team'])
        logging.info("Starting with empty base (no Phase 1 data)")

    # Ensure we have standard columns
    for col in ['Walkers', 'Leader', 'Start Unit', 'End Unit']:
        if col not in df.columns:
            df[col] = None

    # Add columns for phase2b data
    df['Author'] = None
    df['PDF_Source'] = None
    df['Extraction_Notes'] = None

    # Merge Phase 2b walker data
    if len(sources['phase2b']) > 0:
        logging.info("Merging Phase 2b walker data...")

        # For each phase2b record
        for idx, p2b_row in sources['phase2b'].iterrows():
            date = p2b_row['Date']
            team = p2b_row['Team']

            # Find matching row in df
            mask = (df['Date'] == date) & (df['Team'] == team)

            if mask.any():
                # Update existing row
                row_idx = df[mask].index[0]

                # Merge walker data intelligently
                walkers, leader = merge_walker_data(
                    df.loc[row_idx, 'Walkers'],
                    df.loc[row_idx, 'Leader'],
                    p2b_row['Walkers'],
                    p2b_row['Team_Leader']
                )

                df.loc[row_idx, 'Walkers'] = walkers
                if leader:
                    df.loc[row_idx, 'Leader'] = leader
                df.loc[row_idx, 'Author'] = p2b_row['Author']
                df.loc[row_idx, 'PDF_Source'] = p2b_row['PDF_Source']
                df.loc[row_idx, 'Extraction_Notes'] = p2b_row['Extraction_Notes']
            else:
                # Add new row
                new_row = {
                    'Date': date,
                    'Team': team,
                    'Walkers': p2b_row['Walkers'],
                    'Leader': p2b_row['Team_Leader'],
                    'Author': p2b_row['Author'],
                    'PDF_Source': p2b_row['PDF_Source'],
                    'Extraction_Notes': p2b_row['Extraction_Notes'],
                    'Start Unit': None,
                    'End Unit': None
                }
                df = pd.concat([df, pd.DataFrame([new_row])], ignore_index=True)

        logging.info(f"After Phase 2b merge: {len(df)} records")

    # Merge Phase 3 role data
    if len(sources['phase3']) > 0:
        logging.info("Merging Phase 3 role data...")

        # Add role columns if not present
        for col in ['PDA_Operator', 'Paper_Recorder', 'Data_Editor', 'Digitiser']:
            if col not in df.columns:
                df[col] = None

        # For each phase3 record
        for idx, p3_row in sources['phase3'].iterrows():
            date = p3_row['Date']
            team = p3_row['Team']

            # Find matching row in df
            mask = (df['Date'] == date) & (df['Team'] == team)

            if mask.any():
                row_idx = df[mask].index[0]

                # Update role fields (only if empty or phase3 has better data)
                for role_col in ['PDA_Operator', 'Paper_Recorder', 'Data_Editor', 'Digitiser']:
                    if pd.notna(p3_row.get(role_col)) and p3_row.get(role_col) != '':
                        df.loc[row_idx, role_col] = p3_row[role_col]

        logging.info(f"After Phase 3 merge: {len(df)} records")

    return df


def add_quality_notes(df):
    """
    Add quality and completeness notes to each record.

    Args:
        df: Consolidated dataframe

    Returns:
        DataFrame with added QA_Notes column
    """
    notes = []

    for idx, row in df.iterrows():
        note_parts = []

        # Check data completeness
        if pd.isna(row.get('Walkers')) or row.get('Walkers') == '':
            note_parts.append("MISSING: Walkers")

        if pd.isna(row.get('Leader')) or row.get('Leader') == '':
            note_parts.append("MISSING: Leader")

        if pd.isna(row.get('Start Unit')) or row.get('Start Unit') == '':
            note_parts.append("MISSING: Survey units")

        # Check for role data
        has_roles = False
        for role_col in ['PDA_Operator', 'Paper_Recorder', 'Data_Editor', 'Digitiser']:
            if pd.notna(row.get(role_col)) and row.get(role_col) != '':
                has_roles = True
                break

        if not has_roles:
            note_parts.append("No role data available")

        # Check extraction notes for issues
        if pd.notna(row.get('Extraction_Notes')) and row.get('Extraction_Notes') != '':
            notes_lower = str(row.get('Extraction_Notes')).lower()
            if 'unclear' in notes_lower or 'uncertain' in notes_lower or '[?]' in notes_lower:
                note_parts.append("UNCERTAIN: Check extraction notes")

        notes.append(" | ".join(note_parts) if note_parts else "Complete")

    df['QA_Notes'] = notes
    return df


def generate_statistics(df):
    """Generate and log statistics about the consolidated data."""
    logging.info("\n" + "=" * 80)
    logging.info("CONSOLIDATION STATISTICS")
    logging.info("=" * 80)

    logging.info(f"\nTotal records: {len(df)}")

    # By year
    df['Year'] = pd.to_datetime(df['Date']).dt.year
    logging.info(f"\nRecords by year:")
    for year in sorted(df['Year'].unique()):
        count = len(df[df['Year'] == year])
        logging.info(f"  {year}: {count} records")

    # By team
    logging.info(f"\nRecords by team:")
    for team in sorted(df['Team'].unique()):
        count = len(df[df['Team'] == team])
        logging.info(f"  Team {team}: {count} records")

    # Completeness
    walkers_count = df['Walkers'].notna().sum()
    leader_count = df['Leader'].notna().sum()
    units_count = df['Start Unit'].notna().sum()

    logging.info(f"\nData completeness:")
    logging.info(f"  Has Walkers: {walkers_count}/{len(df)} ({100*walkers_count/len(df):.1f}%)")
    logging.info(f"  Has Leader: {leader_count}/{len(df)} ({100*leader_count/len(df):.1f}%)")
    logging.info(f"  Has Survey Units: {units_count}/{len(df)} ({100*units_count/len(df):.1f}%)")

    # Role data
    role_count = 0
    for role_col in ['PDA_Operator', 'Paper_Recorder', 'Data_Editor', 'Digitiser']:
        if role_col in df.columns:
            role_count += df[role_col].notna().sum()

    logging.info(f"  Has any role data: {role_count} field entries across all records")

    # QA notes
    complete_count = len(df[df['QA_Notes'] == 'Complete'])
    logging.info(f"\nQuality assessment:")
    logging.info(f"  Complete records: {complete_count}/{len(df)} ({100*complete_count/len(df):.1f}%)")

    missing_walkers = len(df[df['QA_Notes'].str.contains('MISSING: Walkers', na=False)])
    uncertain = len(df[df['QA_Notes'].str.contains('UNCERTAIN', na=False)])

    logging.info(f"  Missing walker data: {missing_walkers}")
    logging.info(f"  Uncertain extractions: {uncertain}")


def main():
    """Main execution function."""
    # Setup logging
    LOG_DIR.mkdir(exist_ok=True)
    setup_logging(LOG_DIR / 'consolidate_v2.log')

    logging.info("=" * 80)
    logging.info("CONSOLIDATION V2: Merging all extraction phases")
    logging.info("=" * 80)

    # Load data sources
    sources = load_data_sources()

    # Consolidate
    df = consolidate_data(sources)

    # Add quality notes
    df = add_quality_notes(df)

    # Sort by date and team
    df = df.sort_values(['Date', 'Team'])

    # Reorder columns for readability
    column_order = [
        'Date', 'Team', 'Leader', 'Walkers',
        'Start Unit', 'End Unit',
        'PDA_Operator', 'Paper_Recorder', 'Data_Editor', 'Digitiser',
        'Author', 'PDF_Source', 'Extraction_Notes',
        'QA_Notes'
    ]

    # Add any remaining columns
    for col in df.columns:
        if col not in column_order:
            column_order.append(col)

    # Reorder (only include columns that exist)
    column_order = [col for col in column_order if col in df.columns]
    df = df[column_order]

    # Save output
    output_path = OUTPUT_DIR / 'final_attribution_v2.csv'
    df.to_csv(output_path, index=False)

    # Generate statistics
    generate_statistics(df)

    logging.info(f"\n{'=' * 80}")
    logging.info(f"Consolidation complete!")
    logging.info(f"Output saved to: {output_path}")
    logging.info(f"{'=' * 80}\n")


if __name__ == "__main__":
    main()
