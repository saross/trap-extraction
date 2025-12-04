#!/usr/bin/env python3
"""
Test extraction on 3 sample records.

Sample 1: 2009-11-09 Team A (narrative EN format)
Sample 2: 2010-04-02 Team B (structured EN with roles)
Sample 3: 2010-03-21 Team D (structured BG requiring transliteration)
"""

import sys
from pathlib import Path

# Add scripts directory to path
sys.path.insert(0, str(Path(__file__).parent))

from extract_diary_walkers import extract_walkers_for_record

# Test records
TEST_RECORDS = [
    {"date": "2009-11-09", "team": "A", "source": "Diary Team A.doc", "format": "narrative_en"},
    {"date": "2010-04-02", "team": "B", "source": "B_2010Diary_En.doc", "format": "structured_en_roles"},
    {"date": "2010-03-21", "team": "D", "source": "D_2010Diary_BG.doc", "format": "structured_bg"},
]

def main():
    print("Testing extraction on 3 sample records")
    print("=" * 60)

    for i, record in enumerate(TEST_RECORDS, 1):
        print(f"\nTest {i}: {record['date']} Team {record['team']} ({record['format']})")
        print("-" * 60)

        try:
            walkers, roles, notes = extract_walkers_for_record(record)

            if walkers:
                print(f"✓ SUCCESS")
                print(f"  Walkers: {walkers}")
                if roles:
                    print(f"  Roles: {roles}")
                if notes:
                    print(f"  Notes: {notes}")
            else:
                print(f"✗ FAILED")
                print(f"  Error: {notes}")

        except Exception as e:
            print(f"✗ EXCEPTION: {e}")
            import traceback
            traceback.print_exc()

    print("\n" + "=" * 60)
    print("Test complete")

if __name__ == "__main__":
    main()
