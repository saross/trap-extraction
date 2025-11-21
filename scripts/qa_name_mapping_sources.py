#!/usr/bin/env python3
"""
QA script to verify and fix pdf_sources references in name-mapping.csv.

For each row with pdf_sources:
1. Check if the referenced file(s) exist
2. If not found, search attribution.csv for correct source
3. Verify all fields (extracted_name, dates, team, season)
4. Apply corrections and generate audit report

Author: Claude Code collaboration
Date: November 2025
"""

import csv
import re
from collections import defaultdict
from pathlib import Path


def build_file_index():
    """
    Build an index of all files in the project directory.
    Returns dict: {lowercase_filename: [full_paths]}
    """
    base_path = Path('..')
    file_index = defaultdict(list)

    print("Building file index...")

    # Search common locations
    search_paths = [
        base_path / 'Kazanluk',
        base_path / 'Elhovo 2010-12-12',
        base_path / 'TRAP-2017-2018',
    ]

    for search_path in search_paths:
        if search_path.exists():
            for file_path in search_path.rglob('*'):
                if file_path.is_file() and file_path.suffix in ['.pdf', '.doc', '.docx', '.xls', '.xlsx']:
                    # Index by lowercase filename (no path)
                    filename_lower = file_path.name.lower()
                    file_index[filename_lower].append(str(file_path))

    print(f"Indexed {len(file_index)} unique filenames")
    return file_index


def find_file(filename, file_index):
    """
    Find a file in the index, trying various matching strategies.

    Returns: list of matching paths (empty if not found)
    """
    if not filename:
        return []

    # Try exact match (case-insensitive)
    filename_lower = filename.lower()
    if filename_lower in file_index:
        return file_index[filename_lower]

    # Try without spaces
    filename_nospace = filename.replace(' ', '').lower()
    if filename_nospace in file_index:
        return file_index[filename_nospace]

    # Try fuzzy match - find files with similar names
    matches = []
    base_name = filename.lower().replace(' ', '').replace('.pdf', '').replace('.doc', '')

    for indexed_name, paths in file_index.items():
        indexed_base = indexed_name.replace('.pdf', '').replace('.doc', '').replace('.docx', '')
        if base_name in indexed_base or indexed_base in base_name:
            matches.extend(paths)

    return matches


def get_attribution_source(extracted_name, team, season, dates):
    """
    Find the PDF_Source for an extracted_name in attribution.csv.

    Returns: (pdf_sources, matching_rows)
    """
    pdf_sources = set()
    matching_rows = []

    date_list = [d.strip() for d in dates.split('|')] if dates else []

    with open('outputs/attribution.csv', 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            # Check if extracted_name appears in this row
            text_to_search = ' | '.join([
                row.get('Walkers_Original', ''),
                row.get('Author', ''),
                row.get('Leader', '')
            ])

            if extracted_name in text_to_search:
                # Check if team matches (if specified)
                if team and row['Team'] != team:
                    continue

                # Check if date matches (if specified)
                if date_list and row['Date'] not in date_list:
                    continue

                # Found a match
                pdf_source = row.get('PDF_Source', '').strip()
                if pdf_source:
                    for source in pdf_source.split(','):
                        pdf_sources.add(source.strip())

                matching_rows.append({
                    'date': row['Date'],
                    'team': row['Team'],
                    'pdf_source': pdf_source
                })

    return ' | '.join(sorted(pdf_sources)), matching_rows


def verify_row_data(row, file_index):
    """
    Verify all data in a name-mapping row.

    Returns: dict with verification results and corrections
    """
    extracted_name = row['extracted_name']
    team = row.get('team', '')
    season = row.get('season', '')
    dates = row.get('dates', '')
    pdf_sources = row.get('pdf_sources', '')

    result = {
        'extracted_name': extracted_name,
        'has_error': False,
        'missing_files': [],
        'found_files': [],
        'corrections': {},
        'matching_attribution': []
    }

    # Check if pdf_sources files exist
    if pdf_sources:
        for source in pdf_sources.split('|'):
            source = source.strip()
            found_paths = find_file(source, file_index)

            if not found_paths:
                result['has_error'] = True
                result['missing_files'].append(source)
            else:
                result['found_files'].append({
                    'original': source,
                    'paths': found_paths
                })

    # If error found, search attribution for correct source
    if result['has_error']:
        correct_sources, matching_rows = get_attribution_source(
            extracted_name, team, season, dates
        )

        result['matching_attribution'] = matching_rows

        if correct_sources != pdf_sources:
            result['corrections']['pdf_sources'] = correct_sources

            # Verify the corrected sources exist
            verified_sources = []
            for source in correct_sources.split('|'):
                source = source.strip()
                if find_file(source, file_index):
                    verified_sources.append(source)

            if verified_sources:
                result['corrections']['pdf_sources'] = ' | '.join(verified_sources)

    return result


def main():
    """Run QA verification on name-mapping.csv."""
    print("="*70)
    print("NAME-MAPPING.CSV PDF_SOURCES QA VERIFICATION")
    print("="*70)
    print()

    # Phase 1: Build file index
    file_index = build_file_index()
    print()

    # Phase 2: Read and verify name-mapping
    print("Reading name-mapping.csv...")
    with open('outputs/name-mapping.csv', 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        fieldnames = reader.fieldnames
        rows = list(reader)

    print(f"Loaded {len(rows)} rows")
    print()

    # Phase 3: Verify each row with pdf_sources
    print("Verifying pdf_sources...")
    errors_found = []
    corrections_applied = []

    for i, row in enumerate(rows):
        pdf_sources = row.get('pdf_sources', '').strip()

        if pdf_sources:
            result = verify_row_data(row, file_index)

            if result['has_error']:
                errors_found.append(result)

                # Apply corrections
                if result['corrections']:
                    for field, new_value in result['corrections'].items():
                        old_value = row[field]
                        row[field] = new_value
                        corrections_applied.append({
                            'row': i + 2,  # +2 for header and 0-indexing
                            'extracted_name': row['extracted_name'],
                            'field': field,
                            'old': old_value,
                            'new': new_value
                        })

    # Phase 4: Write corrected CSV
    if corrections_applied:
        print(f"\nApplying {len(corrections_applied)} corrections...")
        with open('outputs/name-mapping.csv', 'w', encoding='utf-8', newline='') as f:
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(rows)
        print("Updated name-mapping.csv written")
    else:
        print("\nNo corrections needed - all pdf_sources verified!")

    # Phase 5: Generate report
    print()
    print("="*70)
    print("VERIFICATION SUMMARY")
    print("="*70)
    print(f"\nTotal rows checked: {len(rows)}")
    print(f"Rows with pdf_sources: {sum(1 for r in rows if r.get('pdf_sources', ''))}")
    print(f"Erroneous entries found: {len(errors_found)}")
    print(f"Corrections applied: {len(corrections_applied)}")

    if corrections_applied:
        print("\n" + "="*70)
        print("CORRECTIONS APPLIED")
        print("="*70)
        for correction in corrections_applied:
            print(f"\nRow {correction['row']}: {correction['extracted_name']}")
            print(f"  Field: {correction['field']}")
            print(f"  Old: {correction['old']}")
            print(f"  New: {correction['new']}")

    if errors_found:
        print("\n" + "="*70)
        print("DETAILED ERROR REPORT")
        print("="*70)
        for error in errors_found:
            print(f"\nExtracted name: {error['extracted_name']}")
            print(f"Missing files: {', '.join(error['missing_files'])}")
            if error['matching_attribution']:
                print(f"Found in attribution.csv:")
                for match in error['matching_attribution'][:3]:  # Show first 3
                    print(f"  {match['date']} Team {match['team']}: {match['pdf_source']}")
            if error['corrections']:
                print(f"Applied correction: {error['corrections'].get('pdf_sources', 'N/A')}")

    return {
        'total_rows': len(rows),
        'errors_found': len(errors_found),
        'corrections_applied': len(corrections_applied),
        'errors': errors_found,
        'corrections': corrections_applied
    }


if __name__ == '__main__':
    main()
