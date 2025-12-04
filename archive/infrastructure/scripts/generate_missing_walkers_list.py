"""
Generate list of date/team combinations missing walker data.

This script identifies which records need PDF extraction by finding
all date/team combinations that don't have walker information.

Output: missing_walkers.csv for Claude Code to process
"""

import os
import pandas as pd

OUTPUT_DIR = "../outputs"

def main():
    """Generate list of missing walker data."""
    
    # Load final attribution data
    final_path = os.path.join(OUTPUT_DIR, 'final_attribution.csv')
    
    if not os.path.exists(final_path):
        print(f"ERROR: {final_path} not found")
        print("Please run the extraction pipeline first")
        return
    
    df = pd.read_csv(final_path)
    
    print(f"Loaded {len(df)} total records")
    
    # Find records missing walker data
    missing_walkers = df[
        (df['Walkers'].isna()) | (df['Walkers'] == '')
    ][['Date', 'Team']].copy()
    
    # Remove duplicates
    missing_walkers = missing_walkers.drop_duplicates()
    
    # Sort by date and team
    missing_walkers = missing_walkers.sort_values(['Date', 'Team'])
    
    print(f"\nFound {len(missing_walkers)} date/team combinations missing walker data")
    
    # Save to CSV
    output_path = os.path.join(OUTPUT_DIR, 'missing_walkers.csv')
    missing_walkers.to_csv(output_path, index=False)
    
    print(f"Saved to: {output_path}")
    
    # Print summary by year
    missing_walkers['Year'] = pd.to_datetime(missing_walkers['Date']).dt.year
    print("\nBreakdown by year:")
    print(missing_walkers['Year'].value_counts().sort_index())
    
    # Print summary by team
    print("\nBreakdown by team:")
    print(missing_walkers['Team'].value_counts().sort_index())
    
    print("\n" + "=" * 80)
    print("Next steps:")
    print("1. Open this folder in Claude Code")
    print("2. Provide Claude Code with CLAUDE_CODE_INSTRUCTIONS.md")
    print("3. Claude Code will process the PDFs and create phase2b_pdf_walkers.csv")
    print("4. Run the integration script to merge the results")
    print("=" * 80)


if __name__ == "__main__":
    main()
