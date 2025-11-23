# Contributing to TRAP Attribution Extraction

**Thank you for your interest in contributing to this project!**

This document provides guidelines for contributing to the TRAP Attribution Extraction repository. We welcome contributions that improve data quality, enhance documentation, fix bugs, or add new features.

---

## Table of Contents

- [Code of Conduct](#code-of-conduct)
- [Getting Started](#getting-started)
- [Types of Contributions](#types-of-contributions)
- [Development Workflow](#development-workflow)
- [Coding Standards](#coding-standards)
- [Documentation Requirements](#documentation-requirements)
- [Testing Guidelines](#testing-guidelines)
- [Commit Message Conventions](#commit-message-conventions)
- [Pull Request Process](#pull-request-process)
- [Contact](#contact)

---

## Code of Conduct

### Our Pledge

We are committed to providing a welcoming and inclusive environment for all contributors, regardless of background, identity, or experience level.

### Expected Behaviour

- Use welcoming and inclusive language
- Respect differing viewpoints and experiences
- Accept constructive criticism gracefully
- Focus on what is best for the project and community
- Show empathy towards other community members

### Unacceptable Behaviour

- Harassment, discrimination, or personal attacks
- Trolling, insulting comments, or off-topic discussions
- Publishing private information without consent
- Other conduct inappropriate for a professional setting

### Enforcement

Violations may be reported to the project maintainer (shawn.ross@mq.edu.au). All reports will be reviewed confidentially.

---

## Getting Started

### Prerequisites

- **Python 3.9+** installed on your system
- **Git** for version control
- **pandas>=1.3.0** (see requirements.txt)
- Familiarity with archaeological survey data (helpful but not required)

### Setup

1. **Fork the repository** on GitHub

2. **Clone your fork:**
   ```bash
   git clone https://github.com/YOUR-USERNAME/trap-extraction.git
   cd trap-extraction/claude_extraction
   ```

3. **Create a virtual environment:**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

4. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

5. **Create a feature branch:**
   ```bash
   git checkout -b feature/your-feature-name
   ```

---

## Types of Contributions

### Data Quality Improvements

- **Name corrections:** Update name-mapping.csv with canonical names
- **Date verification:** Cross-check dates against diary sources
- **Source validation:** Verify source references in attribution.csv
- **Missing data:** Fill gaps using available documentation

**Process:** Create backup before changes, document evidence, update QA_Notes field

### Documentation Enhancements

- **Code documentation:** Add docstrings, comments, or README improvements
- **Data dictionary:** Clarify field definitions or add examples
- **Standards compliance:** Update FAIR/FAIR4RS documentation
- **User guides:** Create tutorials or usage examples

**Process:** Follow markdown linting rules (see `.claude/CLAUDE.md`), use UK/Australian spelling

### Bug Fixes

- **Script errors:** Fix bugs in extraction scripts
- **Data inconsistencies:** Correct errors in attribution.csv
- **Documentation errors:** Fix typos or broken links

**Process:** Create issue first, reference issue in commit message

### New Features

- **Extraction tools:** Add scripts for new data sources
- **Analysis tools:** Create scripts for data analysis
- **Integration:** Link attribution data to GIS or publications
- **Automation:** Improve extraction efficiency

**Process:** Discuss proposal with maintainer before significant development

---

## Development Workflow

### Branch Naming

Use descriptive branch names with prefixes:

- `feature/` - New features or enhancements
- `fix/` - Bug fixes
- `docs/` - Documentation updates
- `refactor/` - Code refactoring
- `test/` - Test additions or improvements

**Examples:**
- `feature/zenodo-integration`
- `fix/date-parsing-error`
- `docs/api-documentation`

### Development Process

1. **Create issue** describing the problem or enhancement
2. **Create branch** from `master` (or appropriate base branch)
3. **Make changes** following coding standards (see below)
4. **Add tests** if applicable (see testing guidelines)
5. **Update documentation** as needed
6. **Commit changes** with clear messages (see commit conventions)
7. **Push to your fork** and create pull request
8. **Address review feedback** if requested

---

## Coding Standards

### General Principles

All code must follow these standards (defined in `.claude/CLAUDE.md`):

1. **UK/Australian spelling** in all code, comments, and documentation
   - Examples: colour, behaviour, organisation, analyse, optimise
   - Use Oxford comma in lists

2. **Verbose comments**
   - Scripts require header blocks
   - Functions require docstrings
   - Complex logic requires inline comments

3. **Python style**
   - Follow **PEP 8** style guide
   - Use **type hints** for function signatures
   - Prefer **pathlib** over os.path
   - Maximum line length: **100 characters**

### Code Example

```python
#!/usr/bin/env python3
"""
Extract walker data from TRAP field diaries.

This script processes daily diary entries to extract field walker names,
handling both Bulgarian Cyrillic and English text formats.

Author: Your Name
Date: 2025-11-XX
License: Apache-2.0
"""

from pathlib import Path
from typing import List, Optional
import pandas as pd


def extract_walkers(diary_path: Path, date: str) -> Optional[List[str]]:
    """
    Extract walker names from diary entry for specified date.

    Args:
        diary_path: Path to diary file
        date: Date in ISO 8601 format (YYYY-MM-DD)

    Returns:
        List of walker names if found, None otherwise

    Example:
        >>> extract_walkers(Path("diary.txt"), "2009-03-16")
        ['Elena Bozhinova', 'Nadya Kecheva', 'Vanya Gencheva']
    """
    # Implementation with inline comments for complex logic
    pass
```

### Backup Creation

**Always create backups before modifying data files:**

```python
from pathlib import Path
import shutil
from datetime import datetime


def create_backup(file_path: Path) -> Path:
    """Create timestamped backup of file."""
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    backup_path = file_path.with_suffix(f".csv.backup_{timestamp}")
    shutil.copy2(file_path, backup_path)
    print(f"Backup created: {backup_path}")
    return backup_path
```

### Date Handling

**Use ISO 8601 format for all dates:**

```python
from datetime import datetime


def parse_date(date_str: str) -> str:
    """Parse date string to ISO 8601 format (YYYY-MM-DD)."""
    formats = ['%d.%m.%Y', '%Y-%m-%d', '%d/%m/%Y']
    for fmt in formats:
        try:
            dt = datetime.strptime(date_str, fmt)
            return dt.strftime('%Y-%m-%d')  # ISO 8601
        except ValueError:
            continue
    raise ValueError(f"Could not parse date: {date_str}")
```

---

## Documentation Requirements

### Code Documentation

1. **Header blocks** for all scripts:
   ```python
   """
   Script purpose (one line summary).

   Detailed description of what the script does, including:
   - Input sources
   - Processing steps
   - Output format

   Author: Your Name
   Date: YYYY-MM-DD
   License: Apache-2.0
   """
   ```

2. **Docstrings** for all functions:
   ```python
   def function_name(param: type) -> return_type:
       """
       Brief description.

       Detailed explanation if needed.

       Args:
           param: Parameter description

       Returns:
           Return value description

       Raises:
           ErrorType: When this error occurs

       Example:
           >>> function_name(value)
           expected_output
       """
   ```

3. **Inline comments** for complex logic:
   ```python
   # Extract walker names using regex pattern
   # Format: "Walkers: Name1, Name2, Name3"
   pattern = r"Walkers:\s*([^\n]+)"
   match = re.search(pattern, text)
   ```

### Markdown Documentation

1. **Follow linting rules:**
   - MD022: Blank lines around headings
   - MD031: Blank lines around fenced code blocks
   - MD032: Blank lines around lists
   - MD040: Language specifiers for code blocks

2. **Expand acronyms** on first usage:
   - ✅ "Tundzha Regional Archaeological Project (TRAP)"
   - ❌ "TRAP" (without expansion)

3. **Use lowercase with hyphens** for filenames:
   - ✅ `extraction-guide.md`
   - ❌ `Extraction_Guide.md`

---

## Testing Guidelines

### Manual Testing

Before submitting changes:

1. **Run affected scripts** with test data
2. **Verify outputs** match expected results
3. **Check for regressions** in existing functionality
4. **Review backups** created by your changes

### Unit Tests (Optional but Encouraged)

Add unit tests for new functions:

```python
# test_extraction.py
import unittest
from extraction import parse_date


class TestDateParsing(unittest.TestCase):
    """Test date parsing functionality."""

    def test_parse_bulgarian_format(self):
        """Test parsing Bulgarian date format (DD.MM.YYYY)."""
        result = parse_date("16.03.2009")
        self.assertEqual(result, "2009-03-16")

    def test_parse_iso_format(self):
        """Test parsing ISO 8601 format."""
        result = parse_date("2009-03-16")
        self.assertEqual(result, "2009-03-16")


if __name__ == '__main__':
    unittest.main()
```

**Run tests:**
```bash
python -m unittest discover -s tests -p 'test_*.py'
```

---

## Commit Message Conventions

### Format

Use **Conventional Commits** format:

```
type(scope): subject

body

Co-Authored-By: Your Name <your.email@example.com>
```

### Types

- **feat** - New feature
- **fix** - Bug fix
- **docs** - Documentation changes
- **style** - Code formatting (no logic change)
- **refactor** - Code restructuring (no behaviour change)
- **test** - Test additions or improvements
- **chore** - Maintenance tasks

### Examples

**Good commit messages:**

```
feat(extraction): Add Kazanluk 2009 narrative parser

Implemented parser for general diary narrative sections that lack
structured daily entries. Uses pattern matching to identify walker
lists in prose text.

- Added extract_narrative_walkers.py script
- Extracted 3 records from 2009 general diary
- Updated attribution.csv with walker data

Co-Authored-By: Your Name <your.email@example.com>
```

```
fix(data): Correct 2011-11-10 date error to 2011-10-21

Investigation of Team D diary revealed date entry error in source
Excel file. Team D diary ends 2 November; Day 8 entry explicitly
states 21.10.2011 with units 41088-41152.

Evidence documented in kazanluk-2011-date-error-report.md

Co-Authored-By: Your Name <your.email@example.com>
```

```
docs(readme): Update coverage statistics to 100%

Updated README.md to reflect completion of walker data extraction.
All 268 records now have complete attribution data.

Co-Authored-By: Your Name <your.email@example.com>
```

**Poor commit messages:**

```
updated file              # Too vague
fixed bug                 # No context
WIP                       # Not descriptive
```

---

## Pull Request Process

### Before Submitting

1. **Ensure all tests pass** (if tests exist)
2. **Update documentation** to reflect changes
3. **Create backups** of any modified data files
4. **Check code style** follows PEP 8 and project standards
5. **Verify commit messages** follow conventions

### Pull Request Template

**Title:** Brief description (50 characters or less)

**Description:**

```markdown
## Purpose
Brief explanation of what this PR does and why.

## Changes
- Bullet point list of specific changes
- Include file names and line numbers if applicable

## Testing
How was this tested? What are the results?

## Documentation
What documentation was updated or added?

## Related Issues
Fixes #123 (if applicable)

## Checklist
- [ ] Code follows project style guidelines
- [ ] Documentation updated
- [ ] Tests added/updated (if applicable)
- [ ] Backups created (if data modified)
- [ ] Commit messages follow conventions
```

### Review Process

1. **Maintainer reviews** PR for quality and alignment with project goals
2. **Feedback provided** if changes requested
3. **Author addresses** feedback in new commits
4. **Approval granted** once changes meet standards
5. **Merge** to master branch

**Expected timeline:** 3-7 days for initial review

---

## Licensing

### Contribution Agreement

By contributing to this project, you agree that:

1. **Your contributions** will be licensed under:
   - **Apache License 2.0** for code/scripts
   - **CC-BY 4.0 International** for data/documentation

2. **You have the right** to submit the contribution

3. **You understand** contributions become part of the public repository

### Co-Authorship

Significant contributions (>100 lines of code, major features, substantial data improvements) may be recognised with:

- **Co-authorship** in commit messages
- **Contributor listing** in README.md and CITATION.cff
- **Acknowledgement** in PROJECT-COMPLETION.md

---

## Communication

### Preferred Channels

1. **GitHub Issues** - Bug reports, feature requests, questions
2. **Pull Requests** - Code contributions, documentation updates
3. **Email** - shawn.ross@mq.edu.au (for private/sensitive matters)

### Issue Templates

**Bug Report:**
```markdown
**Description:** Clear description of the bug

**Steps to Reproduce:**
1. Step 1
2. Step 2
3. Step 3

**Expected Behaviour:** What should happen

**Actual Behaviour:** What actually happens

**Environment:**
- Python version:
- OS:
- Dependencies:
```

**Feature Request:**
```markdown
**Feature Description:** What feature you'd like to see

**Use Case:** Why this feature is useful

**Proposed Implementation:** Ideas for how to implement (optional)

**Alternatives Considered:** Other approaches you've thought about
```

---

## Recognition

Contributors will be acknowledged in:

- **README.md** - Contributors section
- **CITATION.cff** - Contributor metadata
- **PROJECT-COMPLETION.md** - Acknowledgements section
- **Git commit history** - Co-authorship in commit messages

Significant contributions may warrant ORCID identifier inclusion in CITATION.cff.

---

## Questions?

If you have questions about contributing:

1. **Check existing documentation** (README.md, DATA-DICTIONARY.md, scripts/README.md)
2. **Search GitHub issues** for similar questions
3. **Create a new issue** with the "question" label
4. **Email the maintainer** (shawn.ross@mq.edu.au) for private queries

---

## Thank You!

Your contributions help improve the quality and reusability of archaeological field data. Every improvement—whether code, documentation, or data quality—makes this dataset more valuable to the research community.

**We appreciate your time and expertise!**

---

**Maintainer:** Shawn Ross (Macquarie University)
**Email:** shawn.ross@mq.edu.au
**Repository:** https://github.com/saross/trap-extraction
**License:** Apache-2.0 (code) + CC-BY-4.0 (data)

**Last Updated:** 23 November 2025
