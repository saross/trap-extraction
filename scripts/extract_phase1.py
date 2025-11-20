"""
Phase 1: Extract team leader and composition from SurveySummary Excel files.

Processes Excel files to extract:
- Date (ISO YYYY-MM-DD format)
- Team (letter designation)
- Start Unit (5-digit number)
- End Unit (5-digit number)
- Leader (name/initials)
- Source file reference

Output: phase1_summary.csv
"""

import os
import sys
import pandas as pd
import logging
from pathlib import Path

# Add scripts directory to path
sys.path.insert(0, os.path.dirname(__file__))
from utils import setup_logging, extract_names, normalize_date, normalize_team, validate_unit, find_files_by_pattern


BASE_DIR = "/media/shawn/191c3b96-5fa5-4d0d-8805-0cf05d3d8468/synology/Adela/TRAP-WD-2020-04"
OUTPUT_DIR = os.path.join(os.path.dirname(os.path.dirname(__file__)), "outputs")
LOG_DIR = os.path.join(os.path.dirname(os.path.dirname(__file__)), "logs")


def extract_from_excel(file_path):
    """
    Extract data from a single SurveySummary Excel file.
    
    Args:
        file_path: Path to Excel file
        
    Returns:
        List of dictionaries with extracted data
    """
    logging.info(f"Processing: {file_path}")
    extracted_data = []
    
    try:
        xls = pd.ExcelFile(file_path)
        
        for sheet_name in xls.sheet_names:
            # Skip sheets that are clearly not survey progress
            if sheet_name.lower() in ['object sheet', 'sample sheet', 'sheet2', 'sheet3']:
                continue
            
            # Read first 15 rows to find header
            df_preview = pd.read_excel(xls, sheet_name=sheet_name, header=None, nrows=15)
            
            header_row_idx = None
            for idx, row in df_preview.iterrows():
                row_str = row.astype(str).str.lower().tolist()
                # Look for header row with 'date' and 'team'
                if any('date' in s for s in row_str) and any('team' in s for s in row_str):
                    header_row_idx = idx
                    break
            
            if header_row_idx is None:
                logging.warning(f"No header found in sheet '{sheet_name}' of {os.path.basename(file_path)}")
                continue
            
            # Read with proper header
            df = pd.read_excel(xls, sheet_name=sheet_name, header=header_row_idx)
            
            # Normalize column names
            df.columns = [str(c).strip().lower() for c in df.columns]
            
            # Identify relevant columns with flexible matching
            date_col = next((c for c in df.columns if 'date' in c), None)
            team_col = next((c for c in df.columns if 'team' in c), None)
            
            # Flexible unit column matching
            start_col = next((c for c in df.columns if 'start' in c and ('unit' in c or 'su' in c)), None)
            end_col = next((c for c in df.columns if 'end' in c and ('unit' in c or 'su' in c)), None)
            
            leader_col = next((c for c in df.columns if 'leader' in c), None)
            
            if not date_col or not team_col:
                logging.warning(f"Missing required columns in sheet '{sheet_name}' of {os.path.basename(file_path)}")
                continue
            
            logging.info(f"Found columns - Date: {date_col}, Team: {team_col}, Start: {start_col}, End: {end_col}, Leader: {leader_col}")
            
            # Extract data from each row
            for _, row in df.iterrows():
                if pd.notna(row[date_col]) and pd.notna(row[team_col]):
                    # Normalize data
                    date_normalized = normalize_date(row[date_col])
                    team_normalized = normalize_team(row[team_col])
                    
                    # Skip if date or team couldn't be normalized
                    if not date_normalized or not team_normalized:
                        continue
                    
                    # Extract and validate units
                    start_unit = validate_unit(row[start_col]) if start_col and pd.notna(row[start_col]) else None
                    end_unit = validate_unit(row[end_col]) if end_col and pd.notna(row[end_col]) else None
                    
                    # Extract leader name
                    leader = extract_names(row[leader_col]) if leader_col and pd.notna(row[leader_col]) else ""
                    
                    extracted_data.append({
                        'Date': date_normalized,
                        'Team': team_normalized,
                        'Start Unit': start_unit,
                        'End Unit': end_unit,
                        'Leader': leader,
                        'Source': os.path.basename(file_path)
                    })
    
    except Exception as e:
        logging.error(f"Error processing {file_path}: {e}")
    
    return extracted_data


def main():
    """Main execution function for Phase 1."""
    # Setup logging
    os.makedirs(LOG_DIR, exist_ok=True)
    setup_logging(os.path.join(LOG_DIR, 'phase1_extraction.log'))
    
    logging.info("=" * 80)
    logging.info("PHASE 1: Extracting from SurveySummary Excel files")
    logging.info("=" * 80)
    
    # Find all SurveySummary files
    summary_files = find_files_by_pattern(BASE_DIR, r'SurveySummary.*\.(xls|xlsx)$')
    
    # Filter to only the main summary files (exclude team-specific ones for now)
    priority_files = [
        'ELH09 SurveySummary.xls',
        'Yam10_SurveySummary.xls',
        'Kaz10_SurveySummary.xls',
        'Kaz11_SurveySummary.xlsx',
        'KAZ09_SurveySummary.xls'
    ]
    
    # Prioritize main files, then add others
    main_files = [f for f in summary_files if any(pf in f for pf in priority_files)]
    other_files = [f for f in summary_files if f not in main_files]
    
    logging.info(f"Found {len(main_files)} priority SurveySummary files")
    logging.info(f"Found {len(other_files)} additional SurveySummary files")
    
    all_data = []
    
    # Process priority files first
    for file_path in main_files:
        data = extract_from_excel(file_path)
        all_data.extend(data)
        logging.info(f"Extracted {len(data)} records from {os.path.basename(file_path)}")
    
    # Create output directory
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    
    # Convert to DataFrame and save
    if all_data:
        df = pd.DataFrame(all_data)
        
        # Sort by date and team
        df = df.sort_values(['Date', 'Team'])
        
        # Filter to 2009-2011
        df['Year'] = pd.to_datetime(df['Date']).dt.year
        df = df[df['Year'].isin([2009, 2010, 2011])]
        df = df.drop('Year', axis=1)
        
        output_path = os.path.join(OUTPUT_DIR, 'phase1_summary.csv')
        df.to_csv(output_path, index=False)
        
        logging.info(f"\n{'=' * 80}")
        logging.info(f"Phase 1 complete!")
        logging.info(f"Total records extracted: {len(df)}")
        logging.info(f"Output saved to: {output_path}")
        logging.info(f"{'=' * 80}\n")
        
        # Print summary statistics
        logging.info("Summary by field season:")
        for source in df['Source'].unique():
            count = len(df[df['Source'] == source])
            logging.info(f"  {source}: {count} records")
    else:
        logging.warning("No data extracted!")


if __name__ == "__main__":
    main()
