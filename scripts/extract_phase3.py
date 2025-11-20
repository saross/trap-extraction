"""
Phase 3: Clean noisy extractions using NLP cues and verb analysis.

This script processes Phase 2 output to:
1. Extract names from noisy text using verb cues (e.g., "Nadja drew" → PDA operator)
2. Deduplicate names in walkers list
3. Move misplaced names to appropriate fields
4. Clean up noise like "One mound was registered"

Output: phase3_cleaned.csv
"""

import os
import sys
import pandas as pd
import re
import logging
from pathlib import Path

# Add scripts directory to path
sys.path.insert(0, os.path.dirname(__file__))
from utils import setup_logging, extract_names


BASE_DIR = "/media/shawn/191c3b96-5fa5-4d0d-8805-0cf05d3d8468/synology/Adela/TRAP-WD-2020-04"
OUTPUT_DIR = os.path.join(os.path.dirname(os.path.dirname(__file__)), "outputs")
LOG_DIR = os.path.join(os.path.dirname(os.path.dirname(__file__)), "logs")


# Verb cues for role assignment
ROLE_CUES = {
    'PDA_Operator': [
        r'(\w+)\s+(drew|operated|used|ran|handled)\s+(pda|polygons?)',
        r'(\w+)\s+(was|is)\s+(pda|operating)',
    ],
    'Paper_Recorder': [
        r'(\w+)\s+(wrote|filled|recorded|kept)\s+(forms?|records?|paper)',
        r'(\w+)\s+(was|is)\s+(recording|writing)',
    ],
    'Data_Editor': [
        r'(\w+)\s+(edited|fixed|corrected|updated)\s+(polygons?|gis|data)',
        r'(\w+)\s+(did|made)\s+(gis|editing)',
    ],
    'Digitiser': [
        r'(\w+)\s+(digitised|digitized|entered|typed)\s+(data|attributes|forms?)',
        r'(\w+)\s+(was|is)\s+(digitising|digitizing|entering)',
    ]
}


def extract_names_with_cues(text, context):
    """
    Extract names from text using verb cues to determine roles.
    
    Args:
        text: The noisy text containing names
        context: The full context line for additional cues
        
    Returns:
        Dictionary with role assignments and cleaned walker list
    """
    result = {
        'names': [],
        'PDA_Operator': '',
        'Paper_Recorder': '',
        'Data_Editor': '',
        'Digitiser': ''
    }
    
    if not text or pd.isna(text):
        return result
    
    # Combine text and context for analysis
    full_text = f"{text} {context}" if context and not pd.isna(context) else text
    
    # Check for role cues
    for role, patterns in ROLE_CUES.items():
        for pattern in patterns:
            matches = re.finditer(pattern, full_text, re.IGNORECASE)
            for match in matches:
                name = match.group(1)
                # Validate it's a name (starts with capital, not a common word)
                if re.match(r'^[A-Z][a-z]+', name) and name.lower() not in ['one', 'the', 'and', 'was', 'were', 'did', 'made']:
                    if result[role]:
                        result[role] += f" | {name}"
                    else:
                        result[role] = name
    
    # Extract all potential names (for walkers list)
    # Split by common delimiters
    parts = re.split(r'[,;\&|/\n\t]', text)
    
    for part in parts:
        part = part.strip()
        
        # Skip noise phrases
        noise_phrases = [
            'one mound', 'was registered', 'not count', 'maybe sometimes',
            'drew huge', 'did not', 'could be', 'looks like', 'found',
            'there were', 'it was', 'we had', 'they did'
        ]
        
        if any(noise in part.lower() for noise in noise_phrases):
            continue
        
        # Extract names from the part
        # Look for capitalized words that could be names
        name_matches = re.findall(r'\b([A-Z][a-z]+(?:\s+[A-Z][a-z]+)?)\b', part)
        for name in name_matches:
            # Filter out common non-name words
            if name.lower() not in ['team', 'date', 'unit', 'units', 'start', 'end', 'leader', 'one', 'the']:
                if name not in result['names']:
                    result['names'].append(name)
    
    return result


def clean_field(text, context=''):
    """
    Clean a single field by extracting names and removing noise.
    
    Args:
        text: The field text to clean
        context: Optional context for better extraction
        
    Returns:
        Cleaned text with only names
    """
    if not text or pd.isna(text) or text == '':
        return ''
    
    # Use extract_names_with_cues to get structured data
    extracted = extract_names_with_cues(text, context)
    
    # Return pipe-separated names
    return " | ".join(extracted['names']) if extracted['names'] else ''


def process_row(row):
    """
    Process a single row to clean and reassign names based on cues.
    
    Args:
        row: DataFrame row
        
    Returns:
        Cleaned row
    """
    # Extract with cues from each field
    walkers_data = extract_names_with_cues(row.get('Walkers', ''), row.get('Context_Walkers', ''))
    pda_data = extract_names_with_cues(row.get('PDA_Operator', ''), row.get('Context_PDA', ''))
    paper_data = extract_names_with_cues(row.get('Paper_Recorder', ''), row.get('Context_Paper', ''))
    editor_data = extract_names_with_cues(row.get('Data_Editor', ''), row.get('Context_Editor', ''))
    digitiser_data = extract_names_with_cues(row.get('Digitiser', ''), row.get('Context_Digitiser', ''))
    
    # Collect all names for walkers (deduplicated)
    all_walker_names = set()
    for data in [walkers_data, pda_data, paper_data, editor_data, digitiser_data]:
        all_walker_names.update(data['names'])
    
    # Assign roles based on cues (priority: specific role assignment over general walker)
    cleaned_row = row.copy()
    
    # Map role names to context column suffixes
    role_to_context = {
        'PDA_Operator': 'PDA',
        'Paper_Recorder': 'Paper',
        'Data_Editor': 'Editor',
        'Digitiser': 'Digitiser'
    }
    
    # Update roles with cue-based assignments
    for role in ['PDA_Operator', 'Paper_Recorder', 'Data_Editor', 'Digitiser']:
        role_names = []
        for data in [pda_data, paper_data, editor_data, digitiser_data]:
            if data[role]:
                role_names.append(data[role])
        
        if role_names:
            cleaned_row[role] = " | ".join(set(" | ".join(role_names).split(" | ")))
        else:
            # If no cue-based assignment, keep original but clean it
            context_col = f'Context_{role_to_context[role]}'
            cleaned_row[role] = clean_field(row.get(role, ''), row.get(context_col, ''))
    
    # Update walkers with all names
    cleaned_row['Walkers'] = " | ".join(sorted(all_walker_names)) if all_walker_names else ''
    
    return cleaned_row


def main():
    """Main execution function for Phase 3."""
    # Setup logging
    os.makedirs(LOG_DIR, exist_ok=True)
    setup_logging(os.path.join(LOG_DIR, 'phase3_cleaning.log'))
    
    logging.info("=" * 80)
    logging.info("PHASE 3: Cleaning noisy extractions using NLP cues")
    logging.info("=" * 80)
    
    # Load Phase 2 data
    phase2_path = os.path.join(OUTPUT_DIR, 'phase2_roles.csv')
    if not os.path.exists(phase2_path):
        logging.error(f"Phase 2 output not found: {phase2_path}")
        logging.error("Please run extract_phase2.py first")
        return
    
    df = pd.read_csv(phase2_path)
    logging.info(f"Loaded Phase 2 data: {len(df)} records")
    
    # Process each row
    cleaned_rows = []
    for idx, row in df.iterrows():
        cleaned_row = process_row(row)
        cleaned_rows.append(cleaned_row)
    
    df_cleaned = pd.DataFrame(cleaned_rows)
    
    # Save cleaned output
    output_path = os.path.join(OUTPUT_DIR, 'phase3_cleaned.csv')
    df_cleaned.to_csv(output_path, index=False)
    
    logging.info(f"\n{'=' * 80}")
    logging.info(f"Phase 3 complete!")
    logging.info(f"Cleaned {len(df_cleaned)} records")
    logging.info(f"Output saved to: {output_path}")
    logging.info(f"{'=' * 80}\n")
    
    # Print improvement statistics
    original_noisy = 0
    cleaned_noisy = 0
    
    noise_words = ['one', 'mound', 'registered', 'not', 'count', 'maybe', 'sometimes', 'drew', 'huge']
    
    for col in ['Walkers', 'PDA_Operator', 'Paper_Recorder', 'Data_Editor', 'Digitiser']:
        if col in df.columns:
            original_noisy += df[col].astype(str).str.lower().str.contains('|'.join(noise_words), na=False).sum()
        if col in df_cleaned.columns:
            cleaned_noisy += df_cleaned[col].astype(str).str.lower().str.contains('|'.join(noise_words), na=False).sum()
    
    logging.info(f"Noise reduction: {original_noisy} → {cleaned_noisy} noisy entries")


if __name__ == "__main__":
    main()
