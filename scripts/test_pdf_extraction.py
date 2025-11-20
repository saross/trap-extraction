"""
Test script for Phase 2b: Vision-based PDF extraction.

Tests extraction from two sample PDFs:
1. Daily Progress Form: B_2010Summary.pdf (3 forms per page)
2. Survey Unit Form: B_20100317.pdf (multiple pages)

This script validates the approach before implementing full Phase 2b.
"""

import os
import sys
from pdf2image import convert_from_path
from PIL import Image
import pytesseract
import re

# Test files
TEST_FILES = {
    'daily_progress': '/media/shawn/191c3b96-5fa5-4d0d-8805-0cf05d3d8468/synology/Adela/TRAP-WD-2020-04/Kazanluk/2010/Project Records/Team B/FieldRecords/B_2010Summary.pdf',
    'survey_unit': '/media/shawn/191c3b96-5fa5-4d0d-8805-0cf05d3d8468/synology/Adela/TRAP-WD-2020-04/Kazanluk/2010/Project Records/Team B/FieldRecords/B_20100317.pdf'
}


def extract_date_from_filename(filename):
    """Extract ISO date from filename like 'B_20100317.pdf' or 'B_2010Summary.pdf'"""
    # Try YYYYMMDD format
    match = re.search(r'(\d{4})(\d{2})(\d{2})', filename)
    if match:
        year, month, day = match.groups()
        return f"{year}-{month}-{day}"
    return None


def extract_team_from_path(filepath):
    """Extract team letter from folder path"""
    match = re.search(r'Team\s+([A-E])', filepath, re.IGNORECASE)
    if match:
        return match.group(1).upper()
    return None


def extract_from_daily_progress_form(image, page_num):
    """
    Extract from Daily Progress Form (3 forms per page).
    
    Target areas:
    - Upper right corner: Team letter, Date (to left), Team leader (below)
    - Walkers box
    - Author field
    """
    width, height = image.size
    
    # Since there are 3 forms per page, divide into thirds vertically
    form_height = height // 3
    
    results = []
    
    for form_idx in range(3):
        print(f"\n  Processing form {form_idx + 1}/3 on page {page_num}...")
        
        # Calculate this form's vertical bounds
        y_start = form_idx * form_height
        y_end = (form_idx + 1) * form_height
        
        # Extract upper right corner (roughly right 30%, top 20% of this form)
        upper_right = image.crop((
            int(width * 0.7),  # right 30%
            y_start,
            width,
            y_start + int(form_height * 0.2)
        ))
        
        # OCR the upper right corner
        upper_right_text = pytesseract.image_to_string(upper_right)
        print(f"    Upper right text:\n{upper_right_text[:200]}")
        
        # Extract walkers box (roughly center-right, middle section)
        walkers_box = image.crop((
            int(width * 0.5),
            y_start + int(form_height * 0.2),
            width,
            y_start + int(form_height * 0.5)
        ))
        
        walkers_text = pytesseract.image_to_string(walkers_box)
        print(f"    Walkers box text:\n{walkers_text[:200]}")
        
        results.append({
            'form_idx': form_idx,
            'upper_right': upper_right_text,
            'walkers': walkers_text
        })
    
    return results


def extract_from_survey_unit_form(image, page_num):
    """
    Extract from Survey Unit Form.
    
    Target: Bottom-most data entry grid, lower left corner (bottom row).
    Handle rotation.
    """
    width, height = image.size
    
    print(f"\n  Processing survey unit form page {page_num}...")
    print(f"    Image size: {width}x{height}")
    
    # Try to detect if rotated by checking aspect ratio
    # Most forms are portrait, if width > height, likely rotated
    if width > height:
        print("    Detected rotation (landscape), rotating 90 degrees...")
        image = image.rotate(90, expand=True)
        width, height = image.size
    
    # Extract bottom section (bottom 15% of page, left 50%)
    bottom_left = image.crop((
        0,
        int(height * 0.85),
        int(width * 0.5),
        height
    ))
    
    # OCR the bottom left section
    bottom_text = pytesseract.image_to_string(bottom_left)
    print(f"    Bottom left text:\n{bottom_text[:300]}")
    
    # Also try bottom right in case of different layout
    bottom_right = image.crop((
        int(width * 0.5),
        int(height * 0.85),
        width,
        height
    ))
    
    bottom_right_text = pytesseract.image_to_string(bottom_right)
    print(f"    Bottom right text:\n{bottom_right_text[:300]}")
    
    return {
        'bottom_left': bottom_text,
        'bottom_right': bottom_right_text
    }


def test_daily_progress_form():
    """Test extraction from Daily Progress Form"""
    print("=" * 80)
    print("TEST 1: Daily Progress Form (B_2010Summary.pdf)")
    print("=" * 80)
    
    pdf_path = TEST_FILES['daily_progress']
    
    if not os.path.exists(pdf_path):
        print(f"ERROR: File not found: {pdf_path}")
        return
    
    print(f"Converting PDF to images...")
    images = convert_from_path(pdf_path, dpi=300, first_page=1, last_page=2)  # Test first 2 pages
    
    print(f"Converted {len(images)} pages")
    
    for page_num, image in enumerate(images, 1):
        print(f"\nPage {page_num}:")
        results = extract_from_daily_progress_form(image, page_num)
        
        # Save cropped images for manual inspection
        for form_idx, result in enumerate(results):
            print(f"\n  Form {form_idx + 1} summary:")
            print(f"    Upper right: {result['upper_right'][:100]}...")
            print(f"    Walkers: {result['walkers'][:100]}...")


def test_survey_unit_form():
    """Test extraction from Survey Unit Form"""
    print("\n" + "=" * 80)
    print("TEST 2: Survey Unit Form (B_20100317.pdf)")
    print("=" * 80)
    
    pdf_path = TEST_FILES['survey_unit']
    
    if not os.path.exists(pdf_path):
        print(f"ERROR: File not found: {pdf_path}")
        return
    
    # Extract metadata from filename
    date = extract_date_from_filename(os.path.basename(pdf_path))
    team = extract_team_from_path(pdf_path)
    
    print(f"Extracted from filename/path:")
    print(f"  Date: {date}")
    print(f"  Team: {team}")
    
    print(f"\nConverting PDF to images...")
    images = convert_from_path(pdf_path, dpi=300, first_page=1, last_page=3)  # Test first 3 pages
    
    print(f"Converted {len(images)} pages")
    
    all_initials = []
    
    for page_num, image in enumerate(images, 1):
        print(f"\nPage {page_num}:")
        result = extract_from_survey_unit_form(image, page_num)
        
        # Combine bottom left and right
        combined_text = result['bottom_left'] + " " + result['bottom_right']
        
        # Extract potential initials (2-3 uppercase letters)
        initials = re.findall(r'\b[A-Z]{2,3}\b', combined_text)
        print(f"    Extracted initials: {initials}")
        
        all_initials.extend(initials)
    
    # Deduplicate
    unique_initials = list(set(all_initials))
    print(f"\n  Combined unique initials from all pages: {unique_initials}")


def main():
    """Run both tests"""
    print("PHASE 2B PDF EXTRACTION - TEST SCRIPT")
    print("Testing vision-based extraction on sample PDFs\n")
    
    # Test 1: Daily Progress Form
    test_daily_progress_form()
    
    # Test 2: Survey Unit Form
    test_survey_unit_form()
    
    print("\n" + "=" * 80)
    print("TEST COMPLETE")
    print("=" * 80)
    print("\nNext steps:")
    print("1. Review the extracted text above")
    print("2. Verify if the target areas are being captured correctly")
    print("3. Adjust crop coordinates if needed")
    print("4. Implement full Phase 2b script based on these results")


if __name__ == "__main__":
    main()
