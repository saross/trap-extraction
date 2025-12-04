#!/usr/bin/env python3
"""
Investigate Missing Survey Unit Dates

This script creates a systematic investigation plan for the 30 remaining dates
without survey units. For each date, it identifies which diary to examine and
prepares structured investigation notes.

The investigation will look for evidence of:
- Weather-related cancellations (rain, snow, wind)
- Non-survey activities (training, total pickups, site visits)
- Equipment problems or technical issues
- Days off or rest days
- Administrative or planning days
- Any other reason survey units wouldn't be recorded

Author: Claude Code
Date: 2025-11-24
"""

from pathlib import Path
from datetime import datetime

# The 30 missing dates from survey-unit-coverage-report.txt
MISSING_DATES = [
    ("2009-03-07", "C"),
    ("2009-03-08", "C"),
    ("2009-03-09", "C"),
    ("2009-03-11", "C"),
    ("2009-03-12", "C"),
    ("2009-03-16", "C"),
    ("2009-03-25", "C"),
    ("2009-03-27", "C"),
    ("2009-04-03", "E"),
    ("2009-04-05", "B"),
    ("2009-10-14", "C"),
    ("2009-10-16", "C"),
    ("2009-10-17", "C"),
    ("2009-10-18", "C"),
    ("2009-10-30", "A"),
    ("2009-10-31", "A"),
    ("2009-11-02", "B"),
    ("2009-11-03", "B"),
    ("2009-11-04", "A"),
    ("2009-11-05", "B"),
    ("2010-03-23", "D"),
    ("2010-03-27", "A"),
    ("2010-03-27", "B"),
    ("2010-03-29", "B"),
    ("2010-03-29", "C"),
    ("2010-04-06", "B"),
    ("2010-04-15", "C"),
    ("2010-11-06", "B"),
    ("2011-10-24", "A"),  # Already known: rainy day
    ("2011-11-12", "C"),
]

# Diary file locations
DIARY_SOURCES = {
    "A": {
        "english": "TeamA/A_Diary_En.doc",
        "bulgarian": "TeamA/A_Diary_BG.doc",
        "extracted_en": "outputs/diary-extracts/A_Diary_En.txt",
        "extracted_bg": "outputs/diary-extracts/A_Diary_BG.txt",
    },
    "B": {
        "english": "TeamB/B_Diary_En.docx",
        "bulgarian": "TeamB/B_Diary_BG.doc",
        "extracted_en": "outputs/diary-extracts/B_Diary_En.txt",
        "extracted_bg": "outputs/diary-extracts/B_Diary_BG.txt",
    },
    "C": {
        "english": "TeamC/C_Diary_En.doc",
        "bulgarian": "TeamC/C_Diary_BG.doc",
        "extracted_en": "outputs/diary-extracts/C_Diary_En.txt",
        "extracted_bg": "outputs/diary-extracts/C_Diary_BG.txt",
    },
    "D": {
        "english": None,  # No English diary for Team D
        "bulgarian": "TeamD/D Diary_BG.doc",
        "extracted_bg": "outputs/diary-extracts/D_Diary_BG.txt",
    },
    "E": {
        "english": "TeamE/E_Diary.doc",
        "bulgarian": "TeamE/E Diary_BG.doc",
        "extracted_en": "outputs/diary-extracts/E_Diary.txt",
        "extracted_bg": "outputs/diary-extracts/E_Diary_BG.txt",
    },
}


def generate_investigation_report():
    """Generate investigation report template."""
    lines = []

    lines.append("# Missing Survey Units: Diary Investigation Report")
    lines.append("")
    lines.append(f"**Generated:** {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    lines.append(f"**Purpose:** Investigate 30 remaining dates without survey units")
    lines.append("")
    lines.append("---")
    lines.append("")

    # Group by team and year
    by_team_year = {}
    for date, team in MISSING_DATES:
        year = date.split('-')[0]
        key = f"{year} Team {team}"
        if key not in by_team_year:
            by_team_year[key] = []
        by_team_year[key].append(date)

    lines.append("## Summary")
    lines.append("")
    lines.append(f"**Total dates to investigate:** {len(MISSING_DATES)}")
    lines.append("")
    lines.append("### By Team and Year")
    lines.append("")
    for key in sorted(by_team_year.keys()):
        dates = by_team_year[key]
        lines.append(f"- **{key}**: {len(dates)} dates")
    lines.append("")
    lines.append("---")
    lines.append("")

    # Investigation template for each date
    lines.append("## Investigation Notes")
    lines.append("")
    lines.append("For each date, examine relevant diaries for evidence of:")
    lines.append("- ☔ Weather cancellations (rain, snow, wind)")
    lines.append("- 📋 Non-survey activities (training, total pickups, site visits)")
    lines.append("- 🔧 Equipment or technical issues")
    lines.append("- 🏖️ Days off or rest days")
    lines.append("- 📝 Administrative or planning days")
    lines.append("- ❓ Other reasons survey units not recorded")
    lines.append("")
    lines.append("---")
    lines.append("")

    # Create investigation section for each date
    current_year = None
    current_team = None

    for date, team in sorted(MISSING_DATES):
        year = date.split('-')[0]

        # Section header for new year
        if year != current_year:
            if current_year is not None:
                lines.append("")
            lines.append(f"## {year} Investigations")
            lines.append("")
            current_year = year
            current_team = None

        # Subsection for new team
        if team != current_team:
            lines.append(f"### Team {team}")
            lines.append("")
            current_team = team

        # Investigation template for this date
        lines.append(f"#### {date} Team {team}")
        lines.append("")
        lines.append("**Diary sources:**")

        sources = DIARY_SOURCES.get(team, {})
        if sources.get("english"):
            lines.append(f"- English: `{sources['english']}`")
        if sources.get("bulgarian"):
            lines.append(f"- Bulgarian: `{sources['bulgarian']}`")

        lines.append("")
        lines.append("**Investigation findings:**")
        lines.append("")
        lines.append("[ ] Diary examined")
        lines.append("")
        lines.append("**Evidence found:**")
        lines.append("")
        lines.append("```")
        lines.append("[To be filled in with diary excerpts]")
        lines.append("```")
        lines.append("")
        lines.append("**Conclusion:**")
        lines.append("")
        lines.append("- Status: [ ] No survey conducted  [ ] Survey but no units recorded  [ ] Unclear")
        lines.append("- Reason: _____________________")
        lines.append("")
        lines.append("---")
        lines.append("")

    return "\n".join(lines)


def main():
    """Main execution function."""
    base_dir = Path(__file__).parent.parent
    output_path = base_dir / "outputs" / "missing-dates-diary-investigation.md"

    print("Missing Survey Units: Diary Investigation")
    print("=" * 60)
    print()
    print(f"Generating investigation report template...")

    report = generate_investigation_report()

    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(report)

    print(f"✓ Investigation template created: {output_path.name}")
    print()
    print(f"Total dates to investigate: {len(MISSING_DATES)}")
    print()
    print("Next step: Examine diaries for each date systematically")
    print()


if __name__ == '__main__':
    main()
