# Integrity Review Protocol (Added in v2.0)

## Etapa 2.5: First Integrity Check (Pre-Review Integrity)

**Trigger**: After Etapa 2 (WRITE) completion, before Etapa 3 (REVIEW)
**Purpose**: Ensure all references and data are not fabricated or erroneous before submission for review

```
Execution steps:
1. agente_verificacion_integridad executes Mode 1 (initial verification) on the paper
2. Verification scope:
   - Phase A: 100% reference existence + bibliographic accuracy + ghost citations
   - Phase B: >= 30% citation context spot-check
   - Phase C: 100% statistical data verification
   - Phase D: >= 30% originality spot-check + self-plagiarism check
   - Phase E: 30% claim verification spot-check (minimum 10 claims)
3. Result handling:
   - PASS -> punto de control -> Etapa 3
   - FAIL -> produce correction list -> fix item by item -> re-verify corrected items
   - PASS after corrections -> punto de control -> Etapa 3
   - Still FAIL after 3 rounds -> notify user, list unverifiable items
```

## Etapa 4.5: Final Integrity Check (Post-Revision Final Check)

**Trigger**: After Etapa 4' (RE-REVISE) or Etapa 3' (RE-REVIEW, Accept) completion, before Etapa 5 (FINALIZE)
**Purpose**: Confirm the revised paper is 100% correct and ready for publication

```
Execution steps:
1. agente_verificacion_integridad executes Mode 2 (final verification) on the revised draft
2. Verification scope:
   - Phase A: 100% reference verification (including those added during revision)
   - Phase B: 100% citation context verification (not spot-check, full check)
   - Phase C: 100% statistical data verification
   - Phase D: >= 50% originality spot-check (100% for newly added/modified paragraphs)
   - Phase E: 100% claim verification (zero MAJOR_DISTORTION + zero UNVERIFIABLE required)
3. Special check: Compare with Etapa 2.5 results to confirm all previous issues are resolved
4. Result handling:
   - PASS (zero issues) -> punto de control -> Etapa 5
   - FAIL -> fix -> re-verify -> PASS -> Etapa 5
5. ⚠️ **IRON RULE**: Must PASS with zero issues to proceed to Etapa 5
```

## Score Trajectory Tracking (v3.3)

Reference: `pipeline-academico/referencias/score_trajectory_protocolo.md`

At Etapa 3' (RE-REVIEW), the `agente_orquestador_pipeline` tracks per-dimension score deltas and triggers a MANDATORY punto de control on regressions. Results stored in Integrity Report `score_trajectory` field (Schema 5).
