import os
import pandas as pd
import re
import csv
import logging
from datetime import datetime
from pathlib import Path

# Setup logging
logging.basicConfig(
    filename='../logs/extraction.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
console = logging.StreamHandler()
console.setLevel(logging.INFO)
logging.getLogger('').addHandler(console)

BASE_DIR = "/media/shawn/191c3b96-5fa5-4d0d-8805-0cf05d3d8468/synology/Adela/TRAP-WD-2020-04"
OUTPUT_DIR = "../outputs"

def find_files(directory, pattern):
    """Recursively find files matching a pattern."""
    matches = []
    for root, _, files in os.walk(directory):
        for file in files:
            if re.search(pattern, file, re.IGNORECASE):
                matches.append(os.path.join(root, file))
    return matches

def extract_names(text):
    """Extracts names/initials from text, removing common words."""
    if not text or pd.isna(text):
        return ""
    
    text = str(text).strip()
    
    # Remove common prefixes/suffixes
    text = re.sub(r'\b(Team|Members|Walkers|Crew|with|using|and|of|the|in|on|at|by|for)\b', ' ', text, flags=re.IGNORECASE)
    text = re.sub(r'\b(PDA|GPS|Recorder|Forms|Digitiser|Digitizing|Photography|Photos)\b', ' ', text, flags=re.IGNORECASE)
    text = re.sub(r'\b(Number|of|walkers)\b', ' ', text, flags=re.IGNORECASE)
    
    # Split by common delimiters
    parts = re.split(r'[,;&|\n]', text)
    names = []
    
    for part in parts:
        part = part.strip()
        # Heuristic: Name should start with capital letter, contain letters, maybe dots/hyphens
        # Allow "J.D.", "Adela", "Shawn Ross"
        # Reject "6", "approx", "rainy"
        if re.match(r'^[A-Z][a-zA-Z\.\-\s]*$', part) and len(part) > 1:
             # Filter out remaining noise if any
             if part.lower() not in ['team', 'date', 'unit']:
                names.append(part)
        elif re.match(r'^[A-Z]+$', part): # Initials like JD, KL
            names.append(part)
            
    return " | ".join(names)

def extract_survey_summary(file_path):
    """Extracts Date, Team, Start Unit, End Unit, Leader from SurveySummary Excel files."""
    logging.info(f"Processing SurveySummary: {file_path}")
    extracted_data = []
    
    try:
        xls = pd.ExcelFile(file_path)
        for sheet_name in xls.sheet_names:
            # Read first few rows to find header
            df_preview = pd.read_excel(xls, sheet_name=sheet_name, header=None, nrows=10)
            
            header_row_idx = None
            for idx, row in df_preview.iterrows():
                row_str = row.astype(str).str.lower().tolist()
                # Look for 'date' and 'team' and ('start su' or 'start unit')
                if any('date' in s for s in row_str) and any('team' in s for s in row_str):
                    header_row_idx = idx
                    break
            
            if header_row_idx is not None:
                df = pd.read_excel(xls, sheet_name=sheet_name, header=header_row_idx)
                
                # Normalize columns
                df.columns = [str(c).strip().lower() for c in df.columns]
                
                # Identify relevant columns
                date_col = next((c for c in df.columns if 'date' in c), None)
                team_col = next((c for c in df.columns if 'team' in c), None)
                
                # Flexible Unit matching
                start_col = next((c for c in df.columns if ('start' in c and ('unit' in c or 'su' in c))), None)
                end_col = next((c for c in df.columns if ('end' in c and ('unit' in c or 'su' in c))), None)
                
                leader_col = next((c for c in df.columns if 'leader' in c), None)
                
                if date_col and team_col:
                    for _, row in df.iterrows():
                        if pd.notna(row[date_col]) and pd.notna(row[team_col]):
                            # Clean date
                            date_val = row[date_col]
                            if isinstance(date_val, datetime):
                                date_str = date_val.strftime('%Y-%m-%d')
                            else:
                                date_str = str(date_val)

                            # Clean Team
                            team_str = str(row[team_col]).strip()
                            
                            # Clean Units
                            start_unit = str(row[start_col]).strip() if start_col and pd.notna(row[start_col]) else ""
                            end_unit = str(row[end_col]).strip() if end_col and pd.notna(row[end_col]) else ""
                            
                            # Clean Leader
                            leader = str(row[leader_col]).strip() if leader_col and pd.notna(row[leader_col]) else ""
                            
                            extracted_data.append({
                                'Date': date_str,
                                'Team': team_str,
                                'Start Unit': start_unit,
                                'End Unit': end_unit,
                                'Leader': extract_names(leader),
                                'SurveySummary_Source': os.path.basename(file_path)
                            })
    except Exception as e:
        logging.error(f"Error processing {file_path}: {e}")

    return extracted_data

def extract_docx_text(file_path):
    """Extracts text from .docx files."""
    try:
        import docx
        doc = docx.Document(file_path)
        return "\n".join([p.text for p in doc.paragraphs])
    except Exception as e:
        logging.error(f"Error reading .docx {file_path}: {e}")
        return ""

def extract_doc_text(file_path):
    """Extracts text from .doc files using strings command."""
    try:
        import subprocess
        result = subprocess.run(['strings', file_path], capture_output=True, text=True)
        return result.stdout
    except Exception as e:
        logging.error(f"Error reading .doc {file_path}: {e}")
        return ""

def parse_diary_text(text, file_name):
    """Parses diary text for Date, Team, Members, and Roles."""
    extracted = []
    
    date_pattern = r'\b(\d{4}-\d{2}-\d{2})\b|\b(\d{2}/\d{2}/\d{4})\b|\b(\d{1,2}\s+(?:Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)[a-z]*\s+\d{4})\b'
    
    team_match = re.search(r'Team\s*([A-Z])', file_name, re.IGNORECASE)
    team_from_file = team_match.group(1).upper() if team_match else None
    
    lines = text.split('\n')
    current_date = None
    current_entry = {'Team': team_from_file, 'Source': file_name, 'Roles': {}}
    
    for line in lines:
        line = line.strip()
        if not line:
            continue
            
        date_match = re.search(date_pattern, line)
        if date_match:
            if current_date:
                extracted.append(current_entry)
                current_entry = {'Team': team_from_file, 'Source': file_name, 'Roles': {}}
            current_date = date_match.group(0) 
            current_entry['Date'] = current_date
            
        if re.search(r'(Team Members|Walkers|Crew):', line, re.IGNORECASE):
            members = line.split(':', 1)[1].strip()
            current_entry['Walkers'] = extract_names(members)
            
        if re.search(r'PDA', line, re.IGNORECASE):
            current_entry['Roles']['PDA'] = extract_names(line)
            
        if re.search(r'(Paper|Recorder|Forms)', line, re.IGNORECASE):
            current_entry['Roles']['Recorder'] = extract_names(line)
            
        if re.search(r'(Digitiser|Digitizing|Digitising)', line, re.IGNORECASE):
            current_entry['Roles']['Digitiser'] = extract_names(line)
            
        # Geospatial Data Editor
        if re.search(r'(GIS|Geospatial|Editor|Polygons)', line, re.IGNORECASE):
             current_entry['Roles']['Data Editor'] = extract_names(line)
            
    if current_date:
        extracted.append(current_entry)
        
    return extracted

def main():
    logging.info("Starting extraction...")
    
    # Phase 1: Survey Summaries
    summary_files = find_files(BASE_DIR, r"SurveySummary.*\.(xls|xlsx)$")
    all_summary_data = []
    
    for f in summary_files:
        data = extract_survey_summary(f)
        all_summary_data.extend(data)
        
    # Phase 2: Diaries
    diary_files = find_files(BASE_DIR, r"Diary.*\.(doc|docx)$")
    all_diary_data = []
    
    for f in diary_files:
        logging.info(f"Processing Diary: {f}")
        if f.lower().endswith('.docx'):
            text = extract_docx_text(f)
        else:
            text = extract_doc_text(f)
            
        if text:
            data = parse_diary_text(text, os.path.basename(f))
            all_diary_data.extend(data)

    # Phase 3: Consolidation
    logging.info("Starting consolidation...")
    
    if all_summary_data:
        df_summary = pd.DataFrame(all_summary_data)
    else:
        df_summary = pd.DataFrame(columns=['Date', 'Team', 'Start Unit', 'End Unit', 'Leader', 'SurveySummary_Source'])

    if all_diary_data:
        flat_data = []
        for entry in all_diary_data:
            row = {
                'Date': entry.get('Date'),
                'Team': entry.get('Team'),
                'Walkers': entry.get('Walkers'),
                'Diary_Source': entry.get('Source'),
                'PDA Operator': entry['Roles'].get('PDA'),
                'Recorder': entry['Roles'].get('Recorder'),
                'Digitiser': entry['Roles'].get('Digitiser'),
                'Data Editor': entry['Roles'].get('Data Editor')
            }
            flat_data.append(row)
        df_diary = pd.DataFrame(flat_data)
    else:
        df_diary = pd.DataFrame(columns=['Date', 'Team', 'Walkers', 'Diary_Source', 'PDA Operator', 'Recorder', 'Digitiser', 'Data Editor'])

    # Normalize Dates
    def normalize_date(d):
        if pd.isna(d): return None
        d = str(d).strip()
        try:
            dt = pd.to_datetime(d)
            return dt.strftime('%Y-%m-%d')
        except:
            return d

    df_summary['Date_Norm'] = df_summary['Date'].apply(normalize_date)
    df_diary['Date_Norm'] = df_diary['Date'].apply(normalize_date)
    
    # Normalize Team
    df_summary['Team_Norm'] = df_summary['Team'].str.upper().str.strip()
    df_diary['Team_Norm'] = df_diary['Team'].str.upper().str.strip()

    # Merge
    df_final = pd.merge(
        df_summary, 
        df_diary, 
        left_on=['Date_Norm', 'Team_Norm'], 
        right_on=['Date_Norm', 'Team_Norm'], 
        how='outer',
        suffixes=('_Summary', '_Diary')
    )
    
    # Filter Dates (2009-2011)
    def get_year(d):
        try:
            return int(d[:4])
        except:
            return 0
            
    df_final['Year'] = df_final['Date_Norm'].apply(get_year)
    df_final = df_final[df_final['Year'].isin([2009, 2010, 2011])]
    
    # Clean up columns
    final_cols = [
        'Date_Norm', 'Team_Norm', 
        'Start Unit', 'End Unit', 'Leader', 
        'Walkers', 'PDA Operator', 'Recorder', 'Data Editor', 'Digitiser',
        'SurveySummary_Source', 'Diary_Source'
    ]
    
    available_cols = [c for c in final_cols if c in df_final.columns]
    df_final = df_final[available_cols]
    
    df_final.rename(columns={'Date_Norm': 'Date', 'Team_Norm': 'Team'}, inplace=True)
    
    output_path = os.path.join(OUTPUT_DIR, 'final_attribution.csv')
    df_final.to_csv(output_path, index=False)
    logging.info(f"Consolidation complete. Saved to {output_path}")

if __name__ == "__main__":
    main()
