"""
Consolidation script: Merge Phase 1 and Phase 2 data and produce final CSV.

Merges data on Date + Team combination, handles duplicates, and validates output.

Output: final_attribution.csv
"""

import os
import sys
import pandas as pd
import logging
from pathlib import Path

# Add scripts directory to path
sys.path.insert(0, os.path.dirname(__file__))
from utils import setup_logging


BASE_DIR = "/media/shawn/191c3b96-5fa5-4d0d-8805-0cf05d3d8468/synology/Adela/TRAP-WD-2020-04"
OUTPUT_DIR = os.path.join(os.path.dirname(os.path.dirname(__file__)), "outputs")
LOG_DIR = os.path.join(os.path.dirname(os.path.dirname(__file__)), "logs")


def merge_duplicate_rows(group):
    """
    Merge duplicate rows for the same Date+Team, preferring non-empty values.
    
    Args:
        group: DataFrame group with same Date and Team
        
    Returns:
        Single row with merged data
    """
    result = {}
    
    for col in group.columns:
        # For each column, take the first non-empty value
        non_empty = group[col].dropna()
        non_empty = non_empty[non_empty != '']
        
        if len(non_empty) > 0:
            result[col] = non_empty.iloc[0]
        else:
            result[col] = None
    
    return pd.Series(result)


def add_interpolation_notes(df):
    """
    Add notes suggesting where interpolation might be helpful.
    
    Args:
        df: DataFrame with attribution data
        
    Returns:
        DataFrame with added Notes column
    """
    notes = []
    
    for idx, row in df.iterrows():
        note_parts = []
        
        # Check for missing walkers
        if pd.isna(row.get('Walkers')) or row.get('Walkers') == '':
            note_parts.append("Missing walker data - consider PDF fallback")
        
        # Check for missing roles
        role_cols = ['PDA operator', 'Paper recorder', 'Data editor', 'Digitiser']
        missing_roles = [col for col in role_cols if pd.isna(row.get(col)) or row.get(col) == '']
        if len(missing_roles) == len(role_cols):
            note_parts.append("No role information - may need interpolation from adjacent dates")
        
        # Check for partial role information
        elif len(missing_roles) > 0 and len(missing_roles) < len(role_cols):
            note_parts.append(f"Partial role info - missing: {', '.join(missing_roles)}")
        
        notes.append("; ".join(note_parts) if note_parts else "")
    
    df['Notes'] = notes
    return df


def main():
    """Main execution function for consolidation."""
    # Setup logging
    os.makedirs(LOG_DIR, exist_ok=True)
    setup_logging(os.path.join(LOG_DIR, 'consolidation.log'))
    
    logging.info("=" * 80)
    logging.info("CONSOLIDATION: Merging Phase 1 and Phase 3 (cleaned) data")
    logging.info("=" * 80)
    
    # Load Phase 1 data
    phase1_path = os.path.join(OUTPUT_DIR, 'phase1_summary.csv')
    if not os.path.exists(phase1_path):
        logging.error(f"Phase 1 output not found: {phase1_path}")
        logging.error("Please run extract_phase1.py first")
        return
    
    df_phase1 = pd.read_csv(phase1_path)
    logging.info(f"Loaded Phase 1 data: {len(df_phase1)} records")
    
    # Load Phase 3 data (cleaned)
    phase3_path = os.path.join(OUTPUT_DIR, 'phase3_cleaned.csv')
    if not os.path.exists(phase3_path):
        logging.warning(f"Phase 3 output not found: {phase3_path}")
        logging.warning("Trying Phase 2 data instead...")
        
        phase2_path = os.path.join(OUTPUT_DIR, 'phase2_roles.csv')
        if not os.path.exists(phase2_path):
            logging.warning(f"Phase 2 output not found either")
            logging.warning("Proceeding with Phase 1 data only")
            df_phase_roles = pd.DataFrame()
        else:
            df_phase_roles = pd.read_csv(phase2_path)
            logging.info(f"Loaded Phase 2 data: {len(df_phase_roles)} records")
    else:
        df_phase_roles = pd.read_csv(phase3_path)
        logging.info(f"Loaded Phase 3 cleaned data: {len(df_phase_roles)} records")
    
    # Merge Phase 1 and Phase 3/2
    if not df_phase_roles.empty:
        # Rename Phase 3/2 columns to match final output
        df_phase_roles = df_phase_roles.rename(columns={
            'PDA_Operator': 'PDA operator',
            'Paper_Recorder': 'Paper recorder',
            'Data_Editor': 'Data editor',
            'Digitiser': 'Digitiser',
            'Source': 'Diary_Source'
        })
        
        # Rename Phase 1 source column
        df_phase1 = df_phase1.rename(columns={'Source': 'SurveySummary_Source'})
        
        # Select columns to merge
        merge_cols = ['Date', 'Team', 'Walkers', 'PDA operator', 'Paper recorder', 'Data editor', 'Digitiser', 'Diary_Source']
        
        # Add context columns if they exist
        context_cols = ['Context_Walkers', 'Context_PDA', 'Context_Paper', 'Context_Editor', 'Context_Digitiser']
        available_context = [col for col in context_cols if col in df_phase_roles.columns]
        merge_cols.extend(available_context)
        
        # Merge on Date and Team
        df_merged = pd.merge(
            df_phase1,
            df_phase_roles[merge_cols],
            on=['Date', 'Team'],
            how='outer'
        )
    else:
        df_merged = df_phase1.copy()
        df_merged = df_merged.rename(columns={'Source': 'SurveySummary_Source'})
        # Add empty columns for roles
        df_merged['Walkers'] = ''
        df_merged['PDA operator'] = ''
        df_merged['Paper recorder'] = ''
        df_merged['Data editor'] = ''
        df_merged['Digitiser'] = ''
        df_merged['Diary_Source'] = ''
    
    logging.info(f"Merged data: {len(df_merged)} records")
    
    # Handle duplicates (same Date + Team)
    if df_merged.duplicated(subset=['Date', 'Team']).any():
        logging.info("Handling duplicate Date+Team combinations...")
        df_merged = df_merged.groupby(['Date', 'Team'], as_index=False).apply(merge_duplicate_rows)
        logging.info(f"After deduplication: {len(df_merged)} records")
    
    # Add interpolation notes
    df_merged = add_interpolation_notes(df_merged)
    
    # Reorder columns to match specification
    final_columns = [
        'Date', 'Team', 'Start Unit', 'End Unit', 'Leader', 'Walkers',
        'PDA operator', 'Paper recorder', 'Data editor', 'Digitiser',
        'Notes', 'SurveySummary_Source', 'Diary_Source',
        'Context_Walkers', 'Context_PDA', 'Context_Paper', 'Context_Editor', 'Context_Digitiser'
    ]
    
    # Only include columns that exist
    available_columns = [col for col in final_columns if col in df_merged.columns]
    df_final = df_merged[available_columns]
    
    # Sort by date and team
    df_final = df_final.sort_values(['Date', 'Team'])
    
    # Save final output
    output_path = os.path.join(OUTPUT_DIR, 'final_attribution.csv')
    df_final.to_csv(output_path, index=False)
    
    logging.info(f"\n{'=' * 80}")
    logging.info(f"Consolidation complete!")
    logging.info(f"Final output: {len(df_final)} records")
    logging.info(f"Saved to: {output_path}")
    logging.info(f"{'=' * 80}\n")
    
    # Print data quality summary
    logging.info("Data Quality Summary:")
    logging.info(f"  Records with Leader: {df_final['Leader'].notna().sum()}")
    logging.info(f"  Records with Walkers: {(df_final['Walkers'].notna() & (df_final['Walkers'] != '')).sum()}")
    logging.info(f"  Records with Start Unit: {df_final['Start Unit'].notna().sum()}")
    logging.info(f"  Records with End Unit: {df_final['End Unit'].notna().sum()}")
    logging.info(f"  Records with PDA operator: {(df_final['PDA operator'].notna() & (df_final['PDA operator'] != '')).sum()}")
    logging.info(f"  Records with Paper recorder: {(df_final['Paper recorder'].notna() & (df_final['Paper recorder'] != '')).sum()}")
    logging.info(f"  Records with Data editor: {(df_final['Data editor'].notna() & (df_final['Data editor'] != '')).sum()}")
    logging.info(f"  Records with Digitiser: {(df_final['Digitiser'].notna() & (df_final['Digitiser'] != '')).sum()}")
    
    # Identify gaps
    missing_walkers = df_final[(df_final['Walkers'].isna()) | (df_final['Walkers'] == '')]
    if len(missing_walkers) > 0:
        logging.info(f"\n{len(missing_walkers)} records missing walker data (candidates for PDF fallback)")


if __name__ == "__main__":
    main()
