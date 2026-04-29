# Score Trajectory Protocol

**Status**: v3.3
**Used by**: `agente_orquestador_pipeline`, `agente_sintetizador_editorial`
**Applies at**: Etapa 3' (RE-REVIEW) and Etapa 4' (RE-REVISE)

---

## Propósito

Tracks how rubric scores change across revision rounds. Detects score regressions — dimensions where the revised paper scores lower than the original — which indicate that a revision fix inadvertently damaged another aspect of the paper.

Inspired by PaperOrchestra's Content Refinement Agent (Song et al., 2026), which accepts revisions only when overall score increases and reverts when any sub-axis shows net negative gain.

---

## How it works

### At Etapa 3 (REVIEW)

The `agente_sintetizador_editorial` produces dimension scores in the Review Report (Schema 6). These are the **baseline scores**.

### At Etapa 3' (RE-REVIEW)

The `agente_sintetizador_editorial` produces new dimension scores. The `agente_orquestador_pipeline` computes deltas:

```
For each dimension d in {originality, methodological_rigor, evidence_sufficiency,
  argument_coherence, writing_quality, literature_integration, significance_impact, overall}:
  delta[d] = score_re_review[d] - score_review[d]

Note: Dimensions match the 7 universal review dimensions from
articulo-academico-reviewer/referencias/review_criteria_framework.md plus overall.
```

### Decision rules

| Condition | Action |
|-----------|--------|
| All deltas >= 0 | Normal: revision improved or maintained all dimensions |
| Any delta < 0 but >= -3 | Warning: "Dimension X decreased slightly (delta = Y). Verify this is acceptable." Surface at punto de control. |
| Any delta < -3 | **Regression detected**: "Dimension X regressed significantly (delta = Y). The revision may have damaged this aspect." Trigger MANDATORY punto de control. |
| Overall delta < 3 AND no P0 issues | Early-stop eligible (existing v3.2 criterion). Suggest stopping revision loop. |

### Regression punto de control

When regression is detected, the MANDATORY punto de control presents:
1. The dimension(s) that regressed and by how much
2. The reviewer's comments on those dimensions (from the re-review report)
3. Three options:
   - **Proceed**: Accept the regression as a tradeoff (recorded in Etapa 6 audit)
   - **Targeted fix**: Return to Etapa 4' to fix only the regressed dimension(s)
   - **Revert**: Restore the pre-revision version for the regressed section(s)

---

## Integration with existing early-stopping

The v3.2 early-stopping criterion (delta < 3 + no P0) remains unchanged. Score trajectory extends it:
- Early-stopping checks the **overall** delta
- Trajectory tracking checks **per-dimension** deltas
- Both can fire at the same punto de control: "Overall improvement is small (suggest stopping) AND dimension X regressed (suggest investigating)"

---

## Etapa 6 reporting

The Process Summary includes a "Score Trajectory" subsection showing all rounds:

```markdown
### Score Trajectory

| Dimension | Review (Etapa 3) | Re-Review (Etapa 3') | Delta | Status |
|-----------|-------------------|----------------------|-------|--------|
| Originality | 3.5 | 3.8 | +0.3 | Improved |
| Methodological Rigor | 4.2 | 4.0 | -0.2 | Warning |
| Evidence Sufficiency | 3.0 | 3.8 | +0.8 | Improved |
| Argument Coherence | 2.8 | 3.5 | +0.7 | Improved |
| Writing Quality | 3.5 | 3.6 | +0.1 | Improved |
| Literature Integration | 3.8 | 4.0 | +0.2 | Improved |
| Significance & Impact | 3.0 | 3.2 | +0.2 | Improved |
| Overall | 3.4 | 3.7 | +0.3 | Improved |

Regressions detected: 1 (Methodological Rigor, -0.2, within tolerance)
Early-stop eligible: No (overall delta = 4 >= 3)
```

---

## Referencias

- Song, Y. et al. (2026). PaperOrchestra. *arXiv:2604.05018*. — Section 4 Step 5 (Content Refinement Agent: score-driven accept/revert).
