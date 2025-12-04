# Known Corrections Reference

**Purpose:** Reference document for QA verification - prevents re-flagging of resolved issues
**Source:** `outputs/qa-corrections-manifest-comprehensive.json`
**Last updated:** 2025-12-03

---

## Summary

**Total corrections:** 89

| Type | Count | QA Action |
|------|-------|-----------|
| VERIFY_NO_CHANGE | 7 | Do not re-flag - CSV confirmed correct despite source discrepancy |
| CORRECTION | 72 | Do not re-flag - already applied to CSV |
| ADD_RECORD | 8 | Do not flag as missing - record already added |
| FLAG_ONLY | 2 | Known unresolvable issue |

---

## Elhovo 2009 Autumn Team A (4 corrections)

| Date | ID | Type | Description | Resolution |
|------|-----|------|-------------|------------|
| 2009-10-21 | ELH09A-D015 | VERIFY_NO_CHANGE | Diary transcription error - CSV Start_Unit 60195 con... | CSV confirmed correct |
| 2009-10-26 | ELH09A-D016 | CORRECTION | Walker substitution - Eric departed Oct 25, Tereza D... | Applied |
| 2009-10-30 | ELH09A-D017 | VERIFY_NO_CHANGE | Erroneous QA_Notes check - Team A records did not co... | CSV confirmed correct |
| 2009-11-09 | ELH09A-D018 | CORRECTION | Missing Diary_Author field | Applied |

## Elhovo 2009 Autumn Team B (4 corrections)

| Date | ID | Type | Description | Resolution |
|------|-----|------|-------------|------------|
| 2009-11-02 | ELH09B-D011 | CORRECTION | Missing unit numbers - data available in diary | Applied |
| 2009-11-03 | ELH09B-D012 | CORRECTION | Missing unit numbers - data available in diary | Applied |
| 2009-11-05 | ELH09B-D013 | CORRECTION | Missing unit numbers - data available in diary | Applied |
| 2009-11-09 | ELH09B-D014 | FLAG_ONLY | Unmapped walker 'Lizzy' - full name unknown | Documented |

## Elhovo 2009 Autumn Team C (6 corrections)

| Date | ID | Type | Description | Resolution |
|------|-----|------|-------------|------------|
| 2009-10-14 | ELH09C-D019 | CORRECTION | Erroneous QA_Notes - remove incorrect 'No autumn sur... | Applied |
| 2009-10-15 | ELH09C-D020 | VERIFY_NO_CHANGE | Diary End_Unit 80103 is transcription error - CSV 80... | CSV confirmed correct |
| 2009-10-22 | ELH09C-D021 | CORRECTION | Remove Georgi from walker list - diary says he was away | Applied |
| 2009-11-09 | ELH09C-V001 | CORRECTION | Start Unit error - CSV shows 80796, SU form 80795 cl... | Applied |
| 2009-11-12 | ELH09C-D022 | VERIFY_NO_CHANGE | End_Unit off by 1 (diary 80938, CSV 80939) - accepte... | CSV confirmed correct |
| 2009-11-13 | ELH09C-D023 | CORRECTION | Start_Unit typo - 80839 should be 80939 | Applied |

## Elhovo 2010 Autumn Team A (2 corrections)

| Date | ID | Type | Description | Resolution |
|------|-----|------|-------------|------------|
| 2010-10-24 | ELH10A-OV1 | FLAG_ONLY | Unit 61549 duplicate - field recording error where s... | Documented |
| A | ELH10-DEDUP | CORRECTION | Walker de-duplication - leader appearing twice in Wa... | Applied |

## Elhovo 2010 Autumn Team B (5 corrections)

| Date | ID | Type | Description | Resolution |
|------|-----|------|-------------|------------|
| 2010-11-03 | ELH10B-D006 | CORRECTION | Start_Unit error - 71245 should be 71525 | Applied |
| 2010-11-04 | ELH10B-D007 | CORRECTION | End_Unit error - 71650 should be 71649 | Applied |
| 2010-11-06 | ELH10B-D008 | CORRECTION | Missing unit numbers - data available in PDF and diary | Applied |
| 2010-11-07 | ELH10B-D009 | ADD_RECORD | Entire record missing from CSV | Record added |
| 2010-11-10 | ELH10B-D010 | ADD_RECORD | Entire record missing from CSV | Record added |

## Global Corrections (1 corrections)

| Date | ID | Type | Description | Resolution |
|------|-----|------|-------------|------------|
| 2010-10-27 | NAME-STD-001 | CORRECTION | Ashley Chee-Quee name standardisation - hyphen added... | Applied |

## Kazanlak 2009 Spring Team A (4 corrections)

| Date | ID | Type | Description | Resolution |
|------|-----|------|-------------|------------|
| 2009-03-06 | KAZ09A-D001 | CORRECTION | Unit range error - CSV shows placeholder 10000-10000... | Applied |
| 2009-03-08 | KAZ09A-D002 | CORRECTION | Unit range error - CSV range too small (8 units vs 3... | Applied |
| 2009-03-09 | KAZ09A-D003 | CORRECTION | Unit range error - CSV shows single unit 10197 inste... | Applied |
| 2009-03-23 | KAZ09A-D004 | CORRECTION | Start unit error - CSV 10410 should be 10445 | Applied |

## Kazanlak 2009 Spring Team B (7 corrections)

| Date | ID | Type | Description | Resolution |
|------|-----|------|-------------|------------|
| 2009-03-04 | KAZ09B-D001 | CORRECTION | Date correction - record incorrectly dated as Mar 03 | Applied |
| 2009-03-08 | KAZ09B-D002 | ADD_RECORD | Missing record - entire day missing from CSV | Record added |
| 2009-03-08 | KAZ09B-D002-WALKERS | CORRECTION | Walker data populated for QA-added record - inferred... | Applied |
| 2009-03-16 | KAZ09B-D003 | CORRECTION | Start Unit error - off by 1 | Applied |
| 2009-03-19 | KAZ09B-D004 | CORRECTION | End Unit error - off by 1 | Applied |
| 2009-03-25 | KAZ09B-D005 | CORRECTION | Start Unit error - significant difference (14 units) | Applied |
| 2009-03-26 | KAZ09B-D006 | CORRECTION | Start Unit error - off by 4 | Applied |

## Kazanlak 2009 Spring Team C (5 corrections)

| Date | ID | Type | Description | Resolution |
|------|-----|------|-------------|------------|
| 2009-03-06 | KAZ09C-D004 | ADD_RECORD | Add separate record for mountain survey | Record added |
| 2009-03-20 | KAZ09C-D001 | CORRECTION | Six-digit mountain survey - misread as five-digit | Applied |
| 2009-03-23 | KAZ09C-D002a | CORRECTION | Unit range correction for intensive survey | Applied |
| 2009-03-23 | KAZ09C-D002b | ADD_RECORD | Add separate record for mountain survey | Record added |
| 2009-03-25 | KAZ09C-D003 | CORRECTION | Missing units - incorrectly marked as non-standard s... | Applied |

## Kazanlak 2009 Spring Team D (16 corrections)

| Date | ID | Type | Description | Resolution |
|------|-----|------|-------------|------------|
| 2009-03-04 | KAZ09D-D001 | CORRECTION | End Unit error - 43 unit difference | Applied |
| 2009-03-07 | KAZ09D-V001 | CORRECTION | Unit range completely wrong - CSV shows 40031-40032,... | Applied |
| 2009-03-08 | KAZ09D-V002 | ADD_RECORD | Missing record - entire day missing from CSV | Record added |
| 2009-03-08 | KAZ09D-V002-WALKERS | CORRECTION | Walker data populated for QA-added record - from BG ... | Applied |
| 2009-03-15 | KAZ09D-V003 | CORRECTION | Unit range errors - CSV shows 40039-40065, DPF shows... | Applied |
| 2009-03-16 | KAZ09D-V004 | ADD_RECORD | Missing record - entire day missing from CSV | Record added |
| 2009-03-16 | KAZ09D-V004-WALKERS | CORRECTION | Walker data populated for QA-added record - from BG ... | Applied |
| 2009-03-19 | KAZ09D-D002 | CORRECTION | Unit range completely wrong | Applied |
| 2009-03-20 | KAZ09D-D003 | CORRECTION | End Unit error - 13 unit difference | Applied |
| 2009-03-23 | KAZ09D-D004 | CORRECTION | Unit range completely wrong | Applied |
| 2009-03-23 | KAZ09D-V005 | CORRECTION | End Unit error - CSV shows 40104, DPF shows 40111 (m... | Applied |
| 2009-03-25 | KAZ09D-D005 | CORRECTION | End Unit error - 3 unit difference | Applied |
| 2009-03-25 | KAZ09D-V006 | CORRECTION | End Unit error - REVERTS RS011 KAZ09D-D005 which inc... | Applied |
| 2009-03-26 | KAZ09D-V007 | CORRECTION | End Unit error - CSV shows 40214, DPF shows 40217 | Applied |
| 2009-03-27 | KAZ09D-V008 | CORRECTION | Start Unit error - CSV shows 40218, DPF shows 40219 ... | Applied |
| 2009-03-27 | KAZ09D-LEADER | VERIFY_NO_CHANGE | Missing leader investigation - diary explicitly show... | CSV confirmed correct |

## Kazanlak 2009 Spring Team E (1 corrections)

| Date | ID | Type | Description | Resolution |
|------|-----|------|-------------|------------|
| 2009-03-25 | KAZ09E-V001 | CORRECTION | End Unit error - CSV 50249 should be 50246 per DPF | Applied |

## Kazanlak 2010 Spring Team A (1 corrections)

| Date | ID | Type | Description | Resolution |
|------|-----|------|-------------|------------|
| 2010-03-28 | KAZ10A-V001 | CORRECTION | Start Unit error - CSV shows 11037, SU forms show 11... | Applied |

## Kazanlak 2010 Spring Team B (1 corrections)

| Date | ID | Type | Description | Resolution |
|------|-----|------|-------------|------------|
| 2010-03-26 | KAZ10B-V001 | CORRECTION | End Unit error - CSV shows 21407, SU forms show sequ... | Applied |

## Kazanlak 2010 Spring Team C (12 corrections)

| Date | ID | Type | Description | Resolution |
|------|-----|------|-------------|------------|
| 2010-03-21 | KAZ10C-D001 | VERIFY_NO_CHANGE | Unit divergence - CSV confirmed correct via continui... | CSV confirmed correct |
| 2010-03-26 | KAZ10C-D002 | CORRECTION | Missing walkers Viki and Todor; [unclear] resolved | Applied |
| 2010-03-27 | KAZ10C-D003 | CORRECTION | Wrong walkers - Todor should be Asen; [unclear] shou... | Applied |
| 2010-03-28 | KAZ10C-D004 | CORRECTION | Missing 5th walker - should be Asen (source conflict... | Applied |
| 2010-03-30 | KAZ10C-D005 | CORRECTION | [unclear] resolved to Todor | Applied |
| 2010-03-31 | KAZ10C-D006 | CORRECTION | Wrong walker identity - Peter should be Dasha (Dagma... | Applied |
| 2010-04-01 | KAZ10C-D007 | CORRECTION | Wrong walker identity - Peter should be Dasha (Dagma... | Applied |
| 2010-04-02 | KAZ10C-D009 | VERIFY_NO_CHANGE | Unit divergence - CSV confirmed correct via continui... | CSV confirmed correct |
| 2010-04-07 | KAZ10C-V001 | CORRECTION | End Unit error - CSV shows 30740, SU form shows 3074... | Applied |
| 2010-04-08 | KAZ10C-DATE | CORRECTION | Date error correction - erroneous 2010-03-08 deleted... | Applied |
| 2010-04-09 | KAZ10C-D008 | CORRECTION | [unclear] resolved to Jiri (Jiří Musil) | Applied |
| 2010-04-13 | KAZ10C-D010 | ADD_RECORD | Entire record missing from CSV | Record added |

## Kazanlak 2010 Spring Team D (1 corrections)

| Date | ID | Type | Description | Resolution |
|------|-----|------|-------------|------------|
| 2010-03-26 | KAZ10D-D001 | CORRECTION | Start Unit error - transcription error (6 misread as 7) | Applied |

## Kazanlak 2011 Autumn Team A (5 corrections)

| Date | ID | Type | Description | Resolution |
|------|-----|------|-------------|------------|
| 2011-10-29 | KAZ11A-A001 | CORRECTION | Walker list incorrect - CSV shows wrong team (Phase ... | Applied |
| 2011-10-30 | KAZ11A-A002 | CORRECTION | Walker list incorrect - CSV shows wrong team composi... | Applied |
| 2011-10-31 | KAZ11A-A003 | CORRECTION | Walker list incorrect - CSV shows wrong team (5 peop... | Applied |
| 2011-11-01 | KAZ11A-A004 | CORRECTION | Walker list incorrect - should show foreign student ... | Applied |
| 2011-11-02 | KAZ11A-A005 | CORRECTION | Walker list incorrect - should show foreign student ... | Applied |

## Kazanlak 2011 Autumn Team B (1 corrections)

| Date | ID | Type | Description | Resolution |
|------|-----|------|-------------|------------|
| 2011-11-16 | KAZ11B-V001 | CORRECTION | Unit range data mixing error - CSV shows 72088-72206... | Applied |

## Kazanlak 2011 Autumn Team C (2 corrections)

| Date | ID | Type | Description | Resolution |
|------|-----|------|-------------|------------|
| 2011-11-18 | KAZ11C-V001 | CORRECTION | Start Unit OCR error - '6' written over incorrect '5... | Applied |
| 2011-11-18 | KAZ11C-V002 | CORRECTION | End Unit error - CSV shows 31342, SU form shows 3134... | Applied |

## Kazanlak 2011 Autumn Team D (11 corrections)

| Date | ID | Type | Description | Resolution |
|------|-----|------|-------------|------------|
| 2011-10-15 | KAZ11D-D001 | CORRECTION | Missing walker - Hristina Pavkova not in CSV | Applied |
| 2011-10-16 | KAZ11D-D002 | CORRECTION | Missing walker - Hristina Pavkova not in CSV | Applied |
| 2011-10-19 | KAZ11D-D003 | CORRECTION | Missing walker - Anani Antonov not in CSV | Applied |
| 2011-10-20 | KAZ11D-D004 | CORRECTION | Missing walker - Anani Antonov not in CSV | Applied |
| 2011-10-21 | KAZ11D-DATE | CORRECTION | Date error correction - erroneous 2011-11-10 deleted... | Applied |
| 2011-10-22 | KAZ11D-D005 | CORRECTION | Missing walker - Anani Antonov not in CSV | Applied |
| 2011-10-23 | KAZ11D-D006 | CORRECTION | Missing walker - Anani Antonov not in CSV | Applied |
| 2011-10-25 | KAZ11D-D007 | CORRECTION | Missing walker - Anani Antonov not in CSV | Applied |
| 2011-10-26 | KAZ11D-D008 | CORRECTION | Missing walker - Anani Antonov not in CSV | Applied |
| 2011-10-27 | KAZ11D-D009 | CORRECTION | Missing walker - Anani Antonov not in CSV | Applied |
| 2011-10-28 | KAZ11D-D010 | CORRECTION | Missing walker - Anani Antonov not in CSV | Applied |

---

## Usage in QA Verification

When running QA verification, check this reference before flagging issues:

1. **VERIFY_NO_CHANGE:** The apparent discrepancy between diary/DPF and CSV
   has been investigated. CSV value is confirmed correct. Do not re-flag.

2. **CORRECTION:** The issue has been fixed. Verify the correction was
   applied correctly (value matches what's documented here).

3. **ADD_RECORD:** The missing record has been added. Verify it exists
   in CSV with correct data.

4. **FLAG_ONLY:** Known issues that cannot be resolved with available sources.
   Document but do not attempt to fix.

---

## Not Tracked in This Manifest

The following bulk operations are documented elsewhere:

- **Name standardisation (66 corrections):** See `outputs/name-mapping.csv`
- **Walker standardisation:** Batch operation documented in extraction reports
- **Role extraction:** Batch operation documented in extraction reports

These are data pipeline operations, not individual QA corrections.
