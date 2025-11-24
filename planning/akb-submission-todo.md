# AKB Submission To-Do List

**Purpose:** Final preparation of attribution.csv for Archaeological Knowledge Base submission
**Status:** Not started - awaiting execution
**Priority:** High
**Estimated completion time:** TBD

---

## 1. Fill in Missing Survey Unit Numbers

**Task:** Extract and verify survey unit numbers for 18 records flagged with "MISSING: Survey units"

**Approach:**
- Check field forms (if available and legible)
- Cross-reference with GIS polygon shapefiles
- Verify unit sequences for gaps or overlaps
- Check project summary PDFs for unit listings

**Records affected:** 18 (mostly from 2009-2010 seasons)

**Status:** ⏸️ Pending

---

## 2. Ensure Team Leader for Every Day

**Task:** Verify all 268 records have team leader populated

**Approach:**
- Check for any blank Leader column entries
- Cross-reference with diary entries
- Verify leader names are standardised

**Current status:** Believed complete (standardisation pass completed)

**Verification needed:** Run automated check

**Status:** ⏸️ Pending verification

---

## 3. Standardise All Names to Name-Mapping Document

**Task:** Apply consistent name standardisation across all personnel columns using authoritative name-mapping document

**Prerequisites:**
- ⚠️ Locate name-mapping.csv (currently in archive/name-disambiguation/)
- Review and complete name-mapping document if necessary
- Verify all variants are captured

**Approach:**
- Load name-mapping.csv as authority file
- Apply standardised names to all columns:
  - Leader
  - Walkers_Original
  - Walkers_Transliterated
  - PDA_Operator
  - Paper_Recorder
  - Data_Editor
  - GPS_Operator
  - Photographer
  - Author
- Cross-reference with TRAP-Participants.csv
- Handle edge cases (multiple people with same name)

**Status:** ⏸️ Pending

---

## 4. Extract Role Information via Thorough NLP Diary Analysis

**Task:** Systematically extract all available role data (PDA operator, paper recorder, etc.) using comprehensive diary analysis

**Current coverage:** 200+ records flagged "No role data available"

**Approach (Tiered Source Strategy):**

### Tier 1: Primary Diaries (Team-specific English/Bulgarian)
- Team A diaries (English + Bulgarian)
- Team B diaries (English + Bulgarian)
- Team C diaries (English + Bulgarian)
- Team D diaries (Bulgarian)
- Team E diary (English)

### Tier 2: Supplemental Diaries
- Team summary documents
- Project-wide diaries (if exist)
- Field notes

### Tier 3: Secondary Sources
- PDF summary forms (already used for walkers)
- Scanned field forms (if role info visible)
- Project reports

**NLP Analysis Requirements:**
- Search for role-specific keywords in context:
  - "PDA" / "GPS" / "pda operator" / "GPS operator"
  - "paper" / "records" / "form" / "recording"
  - "data entry" / "editor" / "transcription"
  - "photo" / "camera" / "photographer"
  - "author" / "wrote" / "diary"
- Extract person names adjacent to role mentions
- Handle narrative descriptions (e.g., "Hamish was taking pictures")
- Track role assignments across diary entries
- Cross-reference with participant roles from TRAP-Participants.csv

**Quality Assurance:**
- Verify extractions against source text
- Document extraction confidence level
- Flag ambiguous role assignments
- Preserve source citations in extraction notes

**Status:** ⏸️ Pending

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

### 7. Create Data Dictionary

**Task:** Formal documentation of all columns in attribution.csv

**Content:**
- Column name
- Data type
- Description
- Allowed values/format
- Source of data
- Coverage expectation
- Notes on interpretation

**Status:** ⏸️ Pending (suggested addition)

---

### 8. Verify Participant Name Spelling

**Task:** Cross-check all names against TRAP-Participants.csv for spelling accuracy

**Approach:**
- Extract unique names from all personnel columns
- Compare against official participant list
- Flag any names not found in participant list
- Verify transliteration from Bulgarian

**Status:** ⏸️ Pending (suggested addition)

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

- Name-mapping document location: Currently in `archive/name-disambiguation/name-mapping.csv` - may need to be moved to active location
- Role extraction (Task 4) is most time-intensive but provides significant value
- Consider running automated checks before manual review to prioritise effort
- Secondary QA package can be prepared incrementally as tasks complete

---

## Success Criteria

**Minimum acceptable for submission:**
- [ ] 100% leader coverage
- [ ] 100% walker coverage (already achieved)
- [ ] >95% survey unit coverage (currently ~93%)
- [ ] All names standardised against authority file
- [ ] QA report shows <5% error rate
- [ ] All data dictionary columns defined
- [ ] Submission metadata complete

**Stretch goals:**
- [ ] >50% role data coverage (PDA, paper recorder, etc.)
- [ ] Independent QA confirms <2% error rate
- [ ] All source citations verified

---

**Document created:** 23 November 2025
**Last updated:** 23 November 2025
**Status:** Ready for execution
