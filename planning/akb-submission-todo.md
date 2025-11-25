# AKB Submission To-Do List

**Purpose:** Final preparation of attribution.csv for Archaeological Knowledge Base submission
**Status:** In progress - Tasks 1-4, 7-8 completed (25 Nov 2025)
**Priority:** High
**Last updated:** 2025-11-25

---

## 1. Fill in Missing Survey Unit Numbers ✓

**Task:** Extract and verify survey unit numbers for 83 records flagged with "MISSING: Survey units"

**Approach:**
- Check field forms (if available and legible)
- Cross-reference with GIS polygon shapefiles
- Verify unit sequences for gaps or overlaps
- Check project summary PDFs for unit listings

**Records affected:** 83 (2009-2011 seasons)

**Status:** ✓ Completed 2025-11-24

**Results:**
- Successfully extracted: 54/83 records (65.1%)
- Fully explained: 28 records (33.7%) - alternative survey methods, weather cancellations, non-survey days
- Pending investigation: 1 record (1.2%) - six-digit to five-digit unit renumbering mapping
- Final coverage: 239/268 (89.18%, up from 69.0%)

**Outputs:**
- `outputs/attribution.csv` updated with 54 extracted survey units
- `outputs/extraction-report.md` comprehensive extraction documentation
- `outputs/task-completion-final-summary.md` task completion summary
- `outputs/survey-unit-coverage-report.txt` coverage verification

**Remaining gaps fully documented:**
- 28 records explained with alternative survey methods, weather cancellations, or non-survey activities
- 1 record pending renumbering investigation (2009-03-12 Team C: six-digit to five-digit unit mapping)

---

## 2. Ensure Team Leader for Every Day ✓

**Task:** Verify all 268 records have team leader populated

**Approach:**
- Check for any blank Leader column entries
- Cross-reference with diary entries
- Verify leader names are standardised

**Status:** ✓ Completed 2025-11-25

**Results:**
- 267/268 records have Leader populated (99.6%)
- 1 empty record: 2010-04-06 Team B (non-survey rainy day - acceptable)
- All Leader names standardised to canonical "First Last" format
- 253 Leader values updated during standardisation
- Multiple leaders now use pipe separators (e.g., "Julia Tzvetkova | Bara Weissová")

**Outputs:**
- `outputs/leader-role-standardisation-report.md` - comprehensive report
- `scripts/standardise-leaders-roles.py` - standardisation script

---

## 3. Standardise All Names to Name-Mapping Document ✓

**Task:** Apply consistent name standardisation across all personnel columns using authoritative name-mapping document

**Status:** ✓ Completed 2025-11-25

**Results:**
- `outputs/name-mapping.csv` contains 698 name mappings (authoritative location)
- Walker standardisation: 268 records with Walkers_Standardised column
- Leader standardisation: 253 changes (all to canonical "First Last" format)
- Role columns standardised: PDA_Operator (44), Paper_Recorder (43), Data_Editor (8), GPS_Operator (37), Photographer (14), Author (194)
- Total: 593 values standardised across Leader and 6 role columns
- Metadata entries cleared: Images, Track Log, Diary (from Paper_Recorder)
- Placeholders cleared: No, Note, Hm, Vitaha (from Data_Editor)
- Only 2 unmapped names remain: Lizzy (uncertain identity), Lindsay Prazak (since resolved)

**Outputs:**
- `outputs/walker-standardisation-report.md` - walker standardisation report
- `outputs/leader-role-standardisation-report.md` - leader/role standardisation report
- `scripts/standardise-walkers.py` - walker standardisation script
- `scripts/standardise-leaders-roles.py` - leader/role standardisation script

---

## 4. Extract Role Information via Thorough NLP Diary Analysis ✓

**Task:** Systematically extract all available role data (PDA operator, paper recorder, etc.) using comprehensive diary analysis

**Status:** ✓ Completed 2025-11-24

**Results:**
- 145 role extractions consolidated from 6 source files
- 80 records matched in attribution.csv
- 76 new role fields populated (empty fields only)
- 69 fields skipped (already had data)

**Coverage improvements:**

| Role | Before | After | Change |
|------|--------|-------|--------|
| Author | 210 (78.4%) | 217 (81.0%) | +7 (+2.6%) |
| PDA_Operator | 30 (11.2%) | 44 (16.4%) | +14 (+5.2%) |
| GPS_Operator | 25 (9.3%) | 37 (13.8%) | +12 (+4.5%) |
| Paper_Recorder | 11 (4.1%) | 43 (16.0%) | +32 (+11.9%) |
| Data_Editor | 8 (3.0%) | 8 (3.0%) | +0 (no change) |
| Photographer | 3 (1.1%) | 14 (5.2%) | +11 (+4.1%) |

**Key findings:**
- 2009 Kazanlak diaries use narrative style without role documentation
- 2009 Elhovo diaries have richest role documentation ("usual setup" patterns)
- 2011 Kazanlak Team B diary provides excellent explicit role assignments
- Paper_Recorder had largest improvement (+11.9%)
- Data_Editor remains at 3% (rarely documented in field diaries)

**Outputs:**
- `archive/intermediate-data/role-extractions/` - 8 extraction CSV files
- `archive/planning/role-extraction-checklist.md` - detailed checklist
- `scripts/extract-roles-regex.py` - regex extraction script
- `scripts/apply-role-extractions.py` - application script

---

## 5. Plan and Complete QA Exercise

**Task:** Comprehensive quality assurance covering accuracy and completeness

### 5.1 Accuracy QA

**Data Validation:**
- [ ] All dates valid and in correct format (YYYY-MM-DD)
- [ ] All team identifiers valid (A, B, C, D, E)
- [ ] Survey unit sequences logical (no impossible gaps/overlaps)
- [ ] Leader names exist in participant list
- [ ] Walker names exist in participant list
- [ ] All role names exist in participant list

**Cross-Reference Checks:**
- [ ] Compare against source Excel summaries (Kaz09/10/11_SurveySummary)
- [ ] Verify walker counts against diary entries
- [ ] Check leader assignments against diary metadata
- [ ] Validate date sequences (no duplicates, gaps explained)

**Source Citation Verification:**
- [ ] All Extraction_Notes cite specific sources
- [ ] All PDF_Source and XLS_Source values are valid files
- [ ] All manual extractions documented

### 5.2 Completeness QA

**Column Coverage:**
- [ ] Leader: 268/268 (100%)
- [ ] Walkers: 268/268 (100%) ✅ Already achieved
- [ ] Survey units: Target 268/268 (currently 250/268)
- [ ] PDA_Operator: Maximise coverage
- [ ] Paper_Recorder: Maximise coverage
- [ ] GPS_Operator: Maximise coverage
- [ ] Photographer: Maximise coverage
- [ ] Author: Maximise coverage

**QA_Notes Review:**
- [ ] All flags still valid and necessary
- [ ] No contradictory flags
- [ ] Clear documentation for all non-standard records

**Metadata Completeness:**
- [ ] All records have source attribution
- [ ] All corrections documented
- [ ] All non-survey days explained

### 5.3 Generate QA Report

**Output:**
- Coverage statistics by column
- List of remaining gaps with explanations
- Confidence assessment by record
- Recommendations for further improvement

**Status:** ⏸️ Pending

---

## 6. Package for Secondary QA (Gemini 3)

**Task:** Prepare outputs and source materials for independent LLM-based quality assurance

### 6.1 Package Contents

**Core Data:**
- attribution.csv (final version)
- Data dictionary/column definitions
- QA report from step 5

**Source Materials:**
- All diary files used (English and Bulgarian)
- Excel summary files (Kaz09/10/11_SurveySummary)
- PDF summary forms
- TRAP-Participants.csv
- Name-mapping.csv

**Documentation:**
- Extraction methodology document
- Source inventory (source-inventory.md)
- Data quality summary (archive/reports/final/data-quality-summary.md)
- Extraction notes compilation

**Scripts:**
- All 6 key extraction/QA scripts
- Requirements.txt for dependencies

### 6.2 QA Instructions for Gemini

**Create qa-instructions.md:**
- Specific checks to perform
- Expected coverage levels
- How to interpret QA_Notes flags
- What constitutes acceptable vs. problematic entries
- Random sampling strategy (e.g., 10% of records)
- Specific areas of concern to focus on

### 6.3 Delivery Format

**Structure:**
```
akb-submission-qa-package/
├── README.md (overview)
├── data/
│   ├── attribution.csv
│   └── data-dictionary.csv
├── sources/
│   ├── diaries/
│   ├── summaries/
│   └── participants/
├── documentation/
│   ├── methodology.md
│   ├── qa-report.md
│   └── source-inventory.md
├── scripts/
└── qa-instructions.md
```

**Packaging:**
- ZIP archive for easy distribution
- Include checksums for data integrity
- Version number and date

**Status:** ⏸️ Pending

---

## Additional Recommended Actions

### 7. Create Data Dictionary ✓

**Task:** Formal documentation of all columns in attribution.csv

**Status:** ✓ Completed 2025-11-23

**Results:**
- `DATA-DICTIONARY.md` created at repository root (400+ lines)
- All 17 columns fully documented with:
  - Column name and data type
  - Description and purpose
  - Allowed values/format (controlled vocabularies)
  - Source of data
  - Coverage expectation
  - Notes on interpretation
- FAIR-compliant metadata format
- Includes examples and edge cases

---

### 8. Verify Participant Name Spelling ✓

**Task:** Cross-check all names against TRAP-Participants.csv for spelling accuracy

**Status:** ✓ Completed 2025-11-25 (via name standardisation)

**Results:**
- All names cross-referenced with `inputs/TRAP-Participants.csv`
- `outputs/name-mapping.csv` contains 698 entries mapping variants to canonical names
- Bulgarian transliterations verified and standardised
- Only 2 uncertain identities remain:
  - Lizzy (Czech volunteer, 2009-autumn) - full name being researched
  - Lindsay Prazak - since resolved and corrected
- Invalid OCR entries identified and cleared (6 entries)
- Silvia Ivanova added to TRAP-Participants.csv

---

### 9. Review and Finalise Extraction_Notes

**Task:** Ensure all Extraction_Notes are clear, complete, and cite sources properly

**Quality checks:**
- All source citations complete
- Bulgarian text properly transliterated where included
- Ambiguities clearly flagged
- Confidence levels indicated where appropriate

**Status:** ⏸️ Pending (suggested addition)

---

### 10. Create Submission Metadata

**Task:** Prepare metadata for AKB submission

**Content:**
- Dataset title
- Description/abstract
- Authors and contributors
- Temporal coverage (2009-2011)
- Spatial coverage (Kazanluk Valley, Bulgaria)
- Methodology summary
- Licence and usage terms
- Related publications
- Contact information
- Version and date

**Status:** ⏸️ Pending (suggested addition)

---

## Priority Order for Execution

1. **High Priority (Core Data Quality):**
   - Task 2: Verify team leaders complete
   - Task 1: Fill missing survey units
   - Task 3: Standardise all names
   - Task 8: Verify participant name spelling

2. **Medium Priority (Enhanced Data):**
   - Task 4: Extract role information via NLP
   - Task 9: Review Extraction_Notes

3. **High Priority (Quality Assurance):**
   - Task 5: QA exercise
   - Task 7: Create data dictionary

4. **Medium Priority (Submission Preparation):**
   - Task 10: Create submission metadata
   - Task 6: Package for secondary QA

---

## Notes

- Name-mapping document location: `outputs/name-mapping.csv` (698 entries, authoritative)
- Role extraction (Task 4) completed - 76 new fields populated, <50% coverage due to source limitations
- Name standardisation (Task 3) completed - all personnel columns standardised
- Remaining tasks: QA exercise (5), Extraction notes review (9), Submission packaging (6, 10)

---

## Success Criteria

**Minimum acceptable for submission:**
- [x] 100% leader coverage ✓ (267/268, 1 acceptable empty)
- [x] 100% walker coverage ✓ (268/268)
- [ ] >95% survey unit coverage (currently 89.18% - 239/268)
- [x] All names standardised against authority file ✓ (698 mappings applied)
- [ ] QA report shows <5% error rate (pending QA exercise)
- [x] All data dictionary columns defined ✓ (DATA-DICTIONARY.md)
- [ ] Submission metadata complete (CITATION.cff exists, may need enhancement)

**Stretch goals:**
- [ ] >50% role data coverage (currently <20% due to source limitations)
- [ ] Independent QA confirms <2% error rate
- [ ] All source citations verified

---

**Document created:** 23 November 2025
**Last updated:** 25 November 2025
**Status:** Tasks 1-4, 7-8 completed; Tasks 5, 6, 9, 10 pending
