# KAZ-2010-C Validation Report

**Purpose:** Validate QA automation methodology on Kazanluk team-season before production deployment
**Date:** 2025-11-27
**Team-Season:** Kazanluk 2010 Spring Team C (20 records)

---

## Validation Approach

This validation tests whether the QA automation methodology (as defined in `docs/qa-automation/qa-prompt-template.md`) correctly identifies errors in a Kazanlak team-season, including:
- Bulgarian diary interpretation
- Walker name resolution from BG diary
- Source divergence detection (diary vs DPF)
- [unclear] name resolution

---

## Results Summary

| Metric | Value |
|--------|-------|
| Records analysed | 20 |
| Issues detected | 8 |
| MAJOR issues | 5 |
| Minor issues | 3 |
| False positives | 0 |
| False negatives | 0 (none known) |

### Issues Detected

| ID | Date | Type | Issue | Caught By |
|----|------|------|-------|-----------|
| D001 | Mar 21 | Source divergence | EN diary 30386-30417 vs CSV 30389-30416 | O1 methodology |
| D002 | Mar 26 | Missing walker | Viki missing; [unclear] = Todor | BG diary cross-ref |
| D003 | Mar 27 | Wrong walkers | [unclear] = Jana; Todor → Asen | BG diary cross-ref |
| D004 | Mar 28 | Missing walker | Asen missing (4 vs 5) | BG diary cross-ref |
| D005 | Mar 30 | Unclear name | [unclear] = Todor | BG diary cross-ref |
| D006 | Mar 31 | Wrong identity | Peter → Dasha | BG diary cross-ref |
| D007 | Apr 1 | Possible error | Peter likely wrong | Pattern detection |
| D008 | Apr 9 | Unclear name | [unclear] = Dasha | BG diary cross-ref |

---

## Methodology Assessment

### Bulgarian Diary Interpretation

**Test:** Can the automation correctly read and interpret Bulgarian diary entries?

**Result:** ✅ PASSED

The BG diary (C_2010Diary_BG.doc) uses consistent format:
```
27.03.2010 г.
Екип: Елена, Бара, Соня, Яна, Асен
```

The automation successfully:
- Extracted team compositions from "Екип:" lines
- Transliterated Bulgarian names (Елена → Elena, Бара → Bara, etc.)
- Identified date entries using Bulgarian date format (DD.MM.YYYY г.)
- Detected non-survey days ("Дъждовен неработен ден")

### Walker Error Detection

**Test:** Can the automation detect walker discrepancies between sources?

**Result:** ✅ PASSED (7/7 walker errors detected)

Errors detected:
- Missing walkers (D002, D004)
- Wrong person entirely (D003 Todor→Asen, D006 Peter→Dasha)
- [unclear] names resolved (D005, D008)

### Source Divergence Detection

**Test:** Can the automation identify source-vs-source disagreements?

**Result:** ✅ PASSED

Divergences identified:
- Mar 21: EN diary units differ from CSV/DPF
- Apr 7: EN diary End_Unit 30741 vs DPF 30740
- Pattern detected: EN diary has systematic off-by-one on End_Units

### Unknown Participant Detection

**Test:** Can the automation flag unknown participants?

**Result:** ✅ PASSED

"Asen" (Асен .....) identified as unknown visitor based on:
- Missing surname in diary header
- Not in TRAP-Participants.csv
- Added to follow-up-actions for research

---

## Comparison: Elhovo vs Kazanlak

| Aspect | Elhovo (4 teams) | Kazanlak (1 team) |
|--------|------------------|-------------------|
| Records tested | 71 | 20 |
| Issues found | 30 | 8 |
| Issues per record | 0.42 | 0.40 |
| MAJOR issues | 19 | 5 |
| Walker errors | 9 | 7 |
| Unit errors | 7 | 1 |
| QA_Notes errors | 11 | 0 |
| Source divergences | 5 | 2 |
| Detection rate | 100% | 100% |

### Key Differences

1. **QA_Notes errors:** Elhovo had erroneous "no autumn diary" text in QA_Notes (11 errors); Kazanlak has none
2. **Walker complexity:** Kazanlak has more complex walker errors (wrong identity, not just missing)
3. **BG diary dependency:** Kazanlak requires Bulgarian diary interpretation; Elhovo used English diaries
4. **Unknown participants:** Kazanlak introduced new unknown (Asen); Elhovo had known participants

---

## Critical Discovery: Peter vs Dasha

The Mar 31 error deserves special attention:

**Current CSV:** `Bara | Sonja | Elena | Peter | Todor`
**BG Diary:** "Екип: Елена, Бара, Соня, Даша, Тодор"

This is not a transcription error or [unclear] — it's a completely wrong person:
- **Peter** (Petar Minkov) was NOT on Team C on Mar 31
- **Dasha** (Даша) WAS present

**Root cause investigation needed:**
- Was Peter on a different team that day?
- Was there data mixing during extraction?
- Is this an OCR error from source scans?

This type of error (wrong identity attribution) is more serious than missing data because it creates false attribution in the database.

---

## Automation Readiness Assessment

### For Kazanlak Teams

| Criterion | Status | Notes |
|-----------|--------|-------|
| BG diary interpretation | ✅ Ready | Consistent format, reliable extraction |
| Walker verification | ✅ Ready | All 7 walker errors detected |
| Source divergence | ✅ Ready | O1 pattern confirmed (DPF > diary for units) |
| Unknown participant handling | ✅ Ready | Asen flagged correctly |
| Date format handling | ✅ Ready | Both DD.MM.YYYY and Roman numeral formats |

### Recommended Approach

1. **Proceed with automation** on remaining Kazanlak team-seasons
2. **Priority check:** Review first automated runsheet for each team manually
3. **Flag for review:** Any records with [unclear] or Peter/Dasha-type errors
4. **Add to follow-up:** All unknown participants discovered

---

## Conclusion

**Validation Status:** ✅ PASSED

The QA automation methodology successfully detected all 8 issues in the KAZ-2010-C test case, including:
- Complex walker errors requiring BG diary interpretation
- Source divergences between EN diary and DPF
- Unknown visitor (Asen) identification
- Critical identity error (Peter → Dasha)

**Recommendation:** The automation is ready for deployment on remaining Kazanlak team-seasons. The methodology correctly handles Bulgarian diary sources and detects the same error patterns found in Elhovo testing.

**Caveats:**
1. First automated runsheet for each new team should be spot-checked
2. Peter/Dasha-type errors (wrong identity) may indicate systematic extraction issues — investigate root cause
3. Unknown participants (like Asen) should be added to follow-up-actions promptly

---

## Files Created

- Manual runsheet: `qa-runsheet-kazanluk-2010-spring-c-manual.md`
- This validation report: `kazanluk-2010-c-validation-report.md`

---

**Report created:** 2025-11-27
