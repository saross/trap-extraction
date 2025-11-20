"""
Utility functions for TRAP data extraction.
Provides shared functionality for name extraction, date normalization, and validation.
"""

import re
import logging
from datetime import datetime
import pandas as pd


def setup_logging(log_file):
    """
    Configure logging to both file and console.
    
    Args:
        log_file: Path to log file
    """
    logging.basicConfig(
        filename=log_file,
        level=logging.INFO,
        format='%(asctime)s - %(levelname)s - %(message)s'
    )
    console = logging.StreamHandler()
    console.setLevel(logging.INFO)
    logging.getLogger('').addHandler(console)


def extract_names(text):
    """
    Extract names/initials from text using NLP/regex, filtering out common words.
    
    Args:
        text: Input text that may contain names mixed with other words
        
    Returns:
        Pipe-separated string of extracted names/initials, or empty string
        
    Examples:
        >>> extract_names("Team leader: Adela Sobotkova")
        "Adela Sobotkova"
        >>> extract_names("PDA operator: JD")
        "JD"
        >>> extract_names("Walkers: Martin, Petra, Bara")
        "Martin | Petra | Bara"
    """
    if not text or pd.isna(text):
        return ""
    
    text = str(text).strip()
    
    # Remove common prefixes/suffixes and noise words
    noise_patterns = [
        r'\b(Team|Members|Walkers|Crew|Leader|Operator)\b',
        r'\b(with|using|and|of|the|in|on|at|by|for|to|from)\b',
        r'\b(PDA|GPS|Recorder|Forms|Digitiser|Digitizing|Photography|Photos)\b',
        r'\b(GIS|Geospatial|Editor|Polygons|Data|Paper)\b',
        r'\b(Number|of|walkers|people|person)\b',
        r'\b(worked|did|made|took|entered|fixed)\b',
    ]
    
    for pattern in noise_patterns:
        text = re.sub(pattern, ' ', text, flags=re.IGNORECASE)
    
    # Split by common delimiters
    parts = re.split(r'[,;\&|/\n\t]', text)
    names = []
    
    for part in parts:
        part = part.strip()
        
        # Skip empty or very short parts
        if len(part) < 2:
            continue
            
        # Pattern 1: Capitalized names (e.g., "Adela", "Shawn Ross", "J.D.")
        # Allow letters, dots, hyphens, spaces, apostrophes
        if re.match(r'^[A-Z][a-zA-Z\.\-\s\']+$', part):
            # Filter out remaining noise words
            if part.lower() not in ['team', 'date', 'unit', 'units', 'start', 'end', 'leader']:
                names.append(part)
        
        # Pattern 2: Initials (e.g., "JD", "SR", "NK")
        elif re.match(r'^[A-Z]{2,4}$', part):
            names.append(part)
        
        # Pattern 3: Initials with dots (e.g., "J.D.", "S.R.")
        elif re.match(r'^[A-Z]\.([A-Z]\.?)+$', part):
            names.append(part)
    
    return " | ".join(names) if names else ""


def normalize_date(date_input):
    """
    Normalize various date formats to ISO YYYY-MM-DD format.
    
    Args:
        date_input: Date as string, datetime object, or numeric value
        
    Returns:
        ISO formatted date string (YYYY-MM-DD) or None if invalid
        
    Examples:
        >>> normalize_date("20091012")
        "2009-10-12"
        >>> normalize_date("16 March 2009")
        "2009-03-16"
    """
    if pd.isna(date_input):
        return None
    
    # If already a datetime object
    if isinstance(date_input, datetime):
        return date_input.strftime('%Y-%m-%d')
    
    date_str = str(date_input).strip()
    
    # Try pandas to_datetime (handles many formats)
    try:
        dt = pd.to_datetime(date_str, errors='coerce')
        if pd.notna(dt):
            return dt.strftime('%Y-%m-%d')
    except:
        pass
    
    # Handle YYYYMMDD format (e.g., "20091012" or "20091012.0")
    match = re.match(r'^(\d{4})(\d{2})(\d{2})(\.0)?$', date_str)
    if match:
        year, month, day = match.group(1), match.group(2), match.group(3)
        try:
            dt = datetime(int(year), int(month), int(day))
            return dt.strftime('%Y-%m-%d')
        except:
            pass
    
    return None


def normalize_team(team_input):
    """
    Normalize team designation to single uppercase letter.
    
    Args:
        team_input: Team designation (e.g., "Team A", "TEAM B", "a", "TeamC")
        
    Returns:
        Single uppercase letter (A-E) or None if invalid
        
    Examples:
        >>> normalize_team("Team A")
        "A"
        >>> normalize_team("TEAM B")
        "B"
        >>> normalize_team("a")
        "A"
    """
    if pd.isna(team_input):
        return None
    
    team_str = str(team_input).strip().upper()
    
    # Extract single letter from various formats
    match = re.search(r'\b([A-E])\b', team_str)
    if match:
        return match.group(1)
    
    return None


def validate_unit(unit_input):
    """
    Validate and format survey unit number as 5-digit string.
    
    Args:
        unit_input: Unit number as string or numeric
        
    Returns:
        5-digit string or None if invalid
        
    Examples:
        >>> validate_unit("60000")
        "60000"
        >>> validate_unit(60000.0)
        "60000"
        >>> validate_unit("rainy day")
        None
    """
    if pd.isna(unit_input):
        return None
    
    unit_str = str(unit_input).strip()
    
    # Remove .0 suffix from floats
    unit_str = re.sub(r'\.0+$', '', unit_str)
    
    # Check if it's a 5-digit number
    if re.match(r'^\d{5}$', unit_str):
        return unit_str
    
    # Handle cases like "60000-60038" (take first number)
    match = re.match(r'^(\d{5})', unit_str)
    if match:
        return match.group(1)
    
    return None


def find_files_by_pattern(base_dir, pattern):
    """
    Recursively find files matching a regex pattern.
    
    Args:
        base_dir: Base directory to search
        pattern: Regex pattern to match filenames
        
    Returns:
        List of absolute file paths
    """
    import os
    matches = []
    for root, _, files in os.walk(base_dir):
        for file in files:
            if re.search(pattern, file, re.IGNORECASE):
                matches.append(os.path.join(root, file))
    return matches
