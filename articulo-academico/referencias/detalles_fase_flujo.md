# Orchestration Workflow — Phase Details

Detailed per-phase agent behavior and output descriptions for the 8-phase orchestration workflow.

---

## Phase 0: CONFIG (Interactive)

**Agent**: `agente_admision`
**Output**: Paper Configuration Record

- Paper type (IMRaD / Lit Review / Theoretical / Case Study / Policy Brief / Conference)
- Discipline and sub-field
- Target journal (optional)
- Citation format (APA 7 / Chicago / MLA / IEEE / Vancouver)
- Output format (LaTeX / DOCX / PDF / Markdown / Combined)
- Language (EN / zh-TW / bilingual sections)
- Bilingual abstract (Yes / EN-only / zh-TW-only)
- Word count target
- Existing materials (RQ, data, drafts, lit)

**punto de control**: User confirms configuration.

---

## Phase 1: RESEARCH

**Agent**: `agente_estratega_literatura`
**Output**: Search Strategy + Source Corpus

- Database selection + search strings
- Inclusion/exclusion criteria
- Source screening + annotated bibliography
- Literature matrix (Source x Theme)
- Research gap mapping

**punto de control**: User reviews sources (optional add/remove).

---

## Phase 2: ARCHITECTURE

**Agent**: `agente_arquitecto_estructura`
**Output**: Paper Outline + Evidence Map

- Structure pattern selection (from paper_structure_patterns.md)
- Section-by-section outline with word count allocation
- Evidence-to-section assignment
- Transition logic between sections

**punto de control**: User approves outline.

---

## Phase 3: ARGUMENTATION

**Agent**: `agente_constructor_argumentos`
**Output**: Argument Blueprint

- Central thesis + sub-arguments
- Claim-Evidence-Reasoning chains per section
- Counter-argument identification + rebuttal strategy
- Logical flow diagram

---

## Phase 4: DRAFTING

**Agent**: `agente_redactor_borrador`
**Output**: Complete Draft

- Section-by-section writing following outline
- Register adjustment for discipline
- In-text citations integrated
- Word count tracking per section
- Transition paragraphs between sections

---

## Phase 5a & 5b: CITATIONS + ABSTRACT (Parallel)

### Phase 5a: Citations

**Agent**: `agente_cumplimiento_citas`
**Output**: Citation Audit Report

- In-text <-> reference list cross-check (zero orphans)
- Format compliance (per selected style)
- DOI/URL verification
- Self-citation ratio check
- Auto-correction of detected errors

### Phase 5b: Abstract

**Agent**: `agente_resumen_bilingue`
**Output**: Bilingual Abstract + Keywords

- English abstract (150-300 words, structured)
- Traditional Chinese abstract (300-500 characters, structured)
- EN keywords (5-7)
- zh-TW keywords (5-7)
- Independent writing (not mechanical translation)

---

## Phase 6: PEER REVIEW

**Agent**: `agente_revisor_pares`
**Output**: Review Report + Revision Instructions

- 5-dimension scoring:
  Originality (20%) | Methodological Rigor (25%) | Evidence Sufficiency (25%)
  Argument Coherence (15%) | Writing Quality (15%)
- Verdict: Accept / Minor Revision / Major Revision / Reject
- Line-level feedback with suggested fixes
- Max 2 revision loops -> back to Phase 4 [agente_redactor_borrador] (limited to 1 round in pipeline-academico)

---

## Phase 7: FORMAT

**Agent**: `agente_formateador`
**Output**: Final Output Package

- Target format conversion (LaTeX + .bib / DOCX / PDF / Markdown)
- Journal-specific formatting (if target journal specified)
- Cover letter (if journal submission)
- AI disclosure statement
- Final quality checklist
