"""
Phase 2: Extract team composition and roles from diary Word documents.

Processes diary files (.doc, .docx) to extract:
- Team composition (Walkers)
- PDA operator
- Paper recorder
- Geospatial data editor
- Digitiser

Prioritizes English diaries (_En.doc, _En.docx).

Output: phase2_roles.csv
"""

import os
import sys
import re
import pandas as pd
import logging
import subprocess
from pathlib import Path

# Add scripts directory to path
sys.path.insert(0, os.path.dirname(__file__))
from utils import setup_logging, extract_names, normalize_date, normalize_team, find_files_by_pattern


BASE_DIR = "/media/shawn/191c3b96-5fa5-4d0d-8805-0cf05d3d8468/synology/Adela/TRAP-WD-2020-04"
OUTPUT_DIR = os.path.join(os.path.dirname(os.path.dirname(__file__)), "outputs")
LOG_DIR = os.path.join(os.path.dirname(os.path.dirname(__file__)), "logs")


def extract_docx_text(file_path):
    """
    Extract text from .docx file using python-docx.
    
    Args:
        file_path: Path to .docx file
        
    Returns:
        Full text content as string
    """
    try:
        from docx import Document
        doc = Document(file_path)
        return "\n".join([p.text for p in doc.paragraphs])
    except Exception as e:
        logging.error(f"Error reading .docx {file_path}: {e}")
        return ""


def extract_doc_text(file_path):
    """
    Extract text from .doc file using strings command.
    
    Args:
        file_path: Path to .doc file
        
    Returns:
        Full text content as string
    """
    try:
        result = subprocess.run(['strings', file_path], capture_output=True, text=True, timeout=30)
        return result.stdout
    except Exception as e:
        logging.error(f"Error reading .doc {file_path}: {e}")
        return ""


def parse_diary_text(text, file_name):
    """
    Parse diary text to extract dates, team members, and roles.
    
    Args:
        text: Full diary text
        file_name: Name of the diary file (for team extraction)
        
    Returns:
        List of dictionaries with extracted data
    """
    extracted = []
    
    # Extract team from filename (e.g., "A_Diary_En.doc" -> "A")
    team_match = re.search(r'([A-E])_.*Diary', file_name, re.IGNORECASE)
    team_from_file = team_match.group(1).upper() if team_match else None
    
    # Date patterns to look for
    date_patterns = [
        r'\b(\d{4}-\d{2}-\d{2})\b',  # YYYY-MM-DD
        r'\b(\d{1,2}\s+(?:Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)[a-z]*\s+\d{4})\b',  # 16 March 2009
        r'\b(\d{1,2}/\d{1,2}/\d{4})\b',  # DD/MM/YYYY
    ]
    
    lines = text.split('\n')
    current_date = None
    current_entry = {
        'Date': None,
        'Team': team_from_file,
        'Walkers': '',
        'PDA_Operator': '',
        'Paper_Recorder': '',
        'Data_Editor': '',
        'Digitiser': '',
        'Source': file_name,
        'Context_Walkers': '',
        'Context_PDA': '',
        'Context_Paper': '',
        'Context_Editor': '',
        'Context_Digitiser': ''
    }
    
    for line in lines:
        line = line.strip()
        if not line:
            continue
        
        # Check for date
        date_found = False
        for pattern in date_patterns:
            date_match = re.search(pattern, line, re.IGNORECASE)
            if date_match:
                # Save previous entry if we have a date
                if current_date and current_entry['Date']:
                    extracted.append(current_entry.copy())
                
                # Start new entry
                current_date = normalize_date(date_match.group(1))
                current_entry = {
                    'Date': current_date,
                    'Team': team_from_file,
                    'Walkers': '',
                    'PDA_Operator': '',
                    'Paper_Recorder': '',
                    'Data_Editor': '',
                    'Digitiser': '',
                    'Source': file_name,
                    'Context_Walkers': '',
                    'Context_PDA': '',
                    'Context_Paper': '',
                    'Context_Editor': '',
                    'Context_Digitiser': ''
                }
                date_found = True
                break
        
        if date_found:
            continue
        
        # Only extract info if we have a current date
        if not current_date:
            continue
        
        line_lower = line.lower()
        
        # Extract team members/walkers
        if re.search(r'(team\s*members?|walkers?|crew):', line_lower):
            # Extract everything after the colon
            parts = line.split(':', 1)
            if len(parts) > 1:
                names = extract_names(parts[1])
                if names:
                    current_entry['Walkers'] = names
                    current_entry['Context_Walkers'] = line[:200]  # First 200 chars
        
        # Extract PDA operator
        if re.search(r'\bpda\b', line_lower):
            # Look for patterns like "PDA: Name" or "Name operated PDA"
            if ':' in line:
                parts = line.split(':', 1)
                if 'pda' in parts[0].lower():
                    names = extract_names(parts[1])
                    if names:
                        current_entry['PDA_Operator'] = names
                        current_entry['Context_PDA'] = line[:200]
            else:
                names = extract_names(line)
                if names:
                    current_entry['PDA_Operator'] = names
                    current_entry['Context_PDA'] = line[:200]
        
        # Extract paper recorder
        if re.search(r'(paper|forms?|recorder|recording)', line_lower):
            names = extract_names(line)
            if names:
                current_entry['Paper_Recorder'] = names
                current_entry['Context_Paper'] = line[:200]
        
        # Extract digitiser
        if re.search(r'(digitis|digitiz|enter.*data|attributes)', line_lower):
            names = extract_names(line)
            if names:
                current_entry['Digitiser'] = names
                current_entry['Context_Digitiser'] = line[:200]
        
        # Extract geospatial data editor
        if re.search(r'(gis|geospatial|editor|polygon|fix.*polygon)', line_lower):
            names = extract_names(line)
            if names:
                current_entry['Data_Editor'] = names
                current_entry['Context_Editor'] = line[:200]
    
    # Don't forget the last entry
    if current_date and current_entry['Date']:
        extracted.append(current_entry)
    
    return extracted


def main():
    """Main execution function for Phase 2."""
    # Setup logging
    os.makedirs(LOG_DIR, exist_ok=True)
    setup_logging(os.path.join(LOG_DIR, 'phase2_extraction.log'))
    
    logging.info("=" * 80)
    logging.info("PHASE 2: Extracting from diary Word documents")
    logging.info("=" * 80)
    
    # Find all diary files
    all_diaries = find_files_by_pattern(BASE_DIR, r'Diary.*\.(doc|docx)$')
    
    # Prioritize English diaries
    english_diaries = [f for f in all_diaries if re.search(r'_En\.(doc|docx)$', f, re.IGNORECASE)]
    other_diaries = [f for f in all_diaries if f not in english_diaries]
    
    # Filter out non-2009-2011 diaries
    relevant_years = ['2009', '2010', '2011']
    english_diaries = [f for f in english_diaries if any(year in f for year in relevant_years)]
    
    logging.info(f"Found {len(english_diaries)} English diary files from 2009-2011")
    logging.info(f"Found {len(other_diaries)} other diary files (will skip)")
    
    all_data = []
    
    for file_path in english_diaries:
        logging.info(f"Processing: {os.path.basename(file_path)}")
        
        # Extract text based on file type
        if file_path.lower().endswith('.docx'):
            text = extract_docx_text(file_path)
        else:
            text = extract_doc_text(file_path)
        
        if not text:
            logging.warning(f"No text extracted from {os.path.basename(file_path)}")
            continue
        
        # Parse the diary text
        data = parse_diary_text(text, os.path.basename(file_path))
        all_data.extend(data)
        logging.info(f"Extracted {len(data)} entries from {os.path.basename(file_path)}")
    
    # Create output directory
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    
    # Convert to DataFrame and save
    if all_data:
        df = pd.DataFrame(all_data)
        
        # Sort by date and team
        df = df.sort_values(['Date', 'Team'])
        
        # Filter to 2009-2011
        df['Year'] = pd.to_datetime(df['Date'], errors='coerce').dt.year
        df = df[df['Year'].isin([2009, 2010, 2011])]
        df = df.drop('Year', axis=1)
        
        output_path = os.path.join(OUTPUT_DIR, 'phase2_roles.csv')
        df.to_csv(output_path, index=False)
        
        logging.info(f"\n{'=' * 80}")
        logging.info(f"Phase 2 complete!")
        logging.info(f"Total entries extracted: {len(df)}")
        logging.info(f"Output saved to: {output_path}")
        logging.info(f"{'=' * 80}\n")
        
        # Print summary statistics
        logging.info("Summary by diary:")
        for source in df['Source'].unique():
            count = len(df[df['Source'] == source])
            logging.info(f"  {source}: {count} entries")
    else:
        logging.warning("No data extracted!")


if __name__ == "__main__":
    main()
