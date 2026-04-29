# Mode Selection Guide

This guide helps users and the `agente_admision` select the most appropriate operational mode.

---

## Mode Selection Flowchart

```
User Input →
│
├── Already have complete research?
│   ├── Yes → Want a full paper?
│   │   ├── Yes ─────────────────────────→ full mode
│   │   └── No → Just need an outline?
│   │       ├── Yes ─────────────────────→ outline-only mode
│   │       └── No → Just need an abstract?
│   │           ├── Yes ──────────────────→ abstract-only mode
│   │           └── No → Just need a literature review?
│   │               ├── Yes ─────────────→ lit-review mode
│   │               └── No ──────────────→ full mode
│   │
│   └── No → Want guided thinking?
│       ├── Yes ─────────────────────────→ plan mode ★ NEW
│       └── No ──────────────────────────→ full mode (Phase 0 will conduct an interview)
│
├── Have an existing paper to revise? ──────────────────────→ revision mode
├── Just need format conversion? ────────────────────────→ format-convert mode
└── Just need a citation check? ────────────────────────→ citation-check mode
```

---

## Detailed Description of Each Mode

### full mode — Complete Paper Writing

**Applicable Scenarios**:
- User has a clear Pregunta de Investigación and (partial) materials
- Needs to produce a complete paper from start to finish
- Includes all phases: Interview → Literature → Structure → Argumentation → Writing → Citation → Review → Formatting

**Not Applicable When**:
- User has no idea about research direction (→ use `investigacion-profunda` first)
- Only need a specific section (→ use another specialized mode)

**Expected Output**: Complete paper draft + references + bilingual abstract + review report
**Expected Duration**: Long (all 8 Phases fully executed)
**Agents Used**: All 9 + socratic_mentor (if needed)

---

### outline-only mode — Outline Generation

**Applicable Scenarios**:
- Only need the paper structure and outline
- A proposal to submit to an advisor for review
- Need to quickly plan the paper structure

**Not Applicable When**:
- Need complete paper content (→ full mode)
- Need guided thinking (→ plan mode)

**Expected Output**: Detailed outline + evidence allocation + word count distribution
**Expected Duration**: Short (Phase 0-2)
**Agents Used**: intake → literature_strategist → structure_architect

---

### plan mode — Chapter-by-Chapter Guided Planning ★ NEW

**Applicable Scenarios**:
- User has ideas but they are not yet clear enough
- Wants guided thinking for each chapter's content
- First-time academic paper writer
- Wants to think through every section before writing
- Just received materials from investigacion-profunda and needs to transform them into a paper plan

**Not Applicable When**:
- Already knows exactly what to write (→ full mode is faster)
- Only needs an outline without deep thinking (→ outline-only mode)
- Time-pressured and needs rapid output (→ full mode)

**Expected Output**: Chapter Plan + INSIGHT Collection
**Expected Duration**: Medium (Step 0-3, approximately 20-30 rounds of conversation)
**Agents Used**: intake → socratic_mentor → structure_architect → argument_builder

**Subsequent Connections**:
- Chapter Plan → full mode (produce complete paper)
- Chapter Plan → articulo-academico-reviewer (review the plan)

---

### revision mode — Paper Revision

**Applicable Scenarios**:
- Already have a completed paper draft
- Received reviewer comments requiring revision
- Feel certain sections need improvement

**Not Applicable When**:
- No existing paper draft (→ full mode)
- Only need to check citation format (→ citation-check mode)

**Expected Output**: Revised paper + revision notes (tracked changes)
**Expected Duration**: Medium
**Agents Used**: peer_reviewer → draft_writer → citation_compliance

**Prerequisite**: User must provide existing paper content

---

### abstract-only mode — Abstract Writing

**Applicable Scenarios**:
- Paper is already complete, only need an abstract
- Need to submit a conference abstract
- Need a bilingual abstract

**Not Applicable When**:
- No paper content to summarize (→ full mode or plan mode)

**Expected Output**: Abstract + keywords
**Expected Duration**: Short
**Agents Used**: intake → abstract_bilingual

---

### lit-review mode — Literature Review

**Applicable Scenarios**:
- Need a literature review on a specific topic
- Preparing the Literature Review chapter of a paper
- Need a systematic search strategy and literature matrix

**Not Applicable When**:
- Need a complete paper (→ full mode)
- Need an in-depth research investigation (→ investigacion-profunda)

**Expected Output**: Annotated bibliography + literature matrix + synthesis analysis
**Expected Duration**: Medium
**Agents Used**: intake → literature_strategist

---

### format-convert mode — Format Conversion

**Applicable Scenarios**:
- Already have paper content, need format conversion
- Markdown → LaTeX / DOCX / PDF
- Need to comply with a specific journal's formatting requirements

**Not Applicable When**:
- No existing content (→ full mode)
- Need content modifications (→ revision mode)

**Expected Output**: Document in target format
**Expected Duration**: Short
**Agents Used**: formatter used standalone

---

### citation-check mode — Citation Check

**Applicable Scenarios**:
- Already have a paper, only need to check citation format
- Final check before submission
- Switching citation format (e.g., APA → IEEE)

**Not Applicable When**:
- No existing citation list (→ full mode)
- Need to modify paper content (→ revision mode)

**Expected Output**: Citation error report + automatic correction suggestions
**Expected Duration**: Short
**Agents Used**: citation_compliance used standalone

---

## Paths from investigacion-profunda

```
investigacion-profunda completed
  │
  ├── investigacion-profunda (full mode) outputs:
  │   PI Brief + Methodology Blueprint + Annotated Bibliography + Synthesis Report
  │   │
  │   ├── Want to write the paper directly ──→ articulo-academico (full mode)
  │   │   agente_admision auto-detects materials, skips redundant questions
  │   │
  │   └── Want to plan before writing ──→ articulo-academico (plan mode)
  │       socratic_mentor leverages existing materials to accelerate guidance
  │
  └── investigacion-profunda (socratic mode) outputs:
      INSIGHT Collection + Synthesis Report
      │
      ├── INSIGHTs are sufficiently clear ──→ articulo-academico (full mode)
      │
      └── Need more guidance ──→ articulo-academico (plan mode)
          socratic_mentor continues deepening from INSIGHTs
```

## Connecting to articulo-academico-reviewer

```
articulo-academico completed
  │
  ├── full mode produces complete paper ──→ articulo-academico-reviewer (full / guided)
  │   Complete peer review + revision suggestions
  │
  ├── plan mode produces Chapter Plan ──→ articulo-academico-reviewer (guided)
  │   Review the plan's feasibility and completeness
  │
  └── reviewer feedback ──→ articulo-academico (revision mode)
      Revise paper based on review comments
```

---

## Common Misselection Scenarios

| User Says | Easily Misselected | Correct Choice | Reason |
|---------|---------|---------|------|
| "Help me write an outline" | outline-only | First confirm: Do they want a simple outline or deep planning? | May need plan mode |
| "I want to write a paper but don't know how to start" | full | plan mode | Needs guided thinking |
| "Help me revise my paper" | revision | First confirm: Are there reviewer comments? | May need full mode rewrite |
| "Help me search for literature" | lit-review | First confirm: Is it a literature review for a paper or a research investigation? | May need investigacion-profunda |
| "I have investigacion-profunda results, help me write a paper" | full (skip Phase 0 directly) | full (but intake needs to detect Traspaso) | Materials need to be properly imported |
| "I want to plan my paper step by step" | outline-only | plan mode | Needs interactive guidance |
| "The paper format is wrong" | revision | citation-check or format-convert | May only need format correction |

---

## Quick Decision Table

| What Do You Have? | What Do You Want? | Choose This Mode |
|-----------|-----------|------------|
| Nothing | Complete paper | plan mode → full mode |
| Pregunta de Investigación + literature | Complete paper | full mode |
| Pregunta de Investigación + literature | Outline | outline-only mode |
| Vague idea | Paper plan | plan mode |
| investigacion-profunda results | Complete paper | full mode (auto-Traspaso) |
| investigacion-profunda results | Guided planning | plan mode |
| Completed paper | Revision | revision mode |
| Completed paper | Abstract | abstract-only mode |
| Completed paper | Format conversion | format-convert mode |
| Completed paper | Citation check | citation-check mode |

---

### Plan to Full Mode Conversion Protocol

When a user completes `plan` mode and wants to proceed to `full` mode for actual paper writing:

#### Conversion Checklist

| Plan Mode Output | Full Mode Input | Conversion Action |
|-----------------|-----------------|-------------------|
| Chapter Plan (structure outline) | `structure_architect` agent | Map chapters → formal sections with heading levels; validate against `paper_structure_patterns.md` |
| Socratic Responses (Q&A transcripts) | `argument_builder` agent | Extract claims + evidence + warrants from dialogue; discard conversational scaffolding |
| Literature Notes (if any) | `literature_strategist` agent | Independent execution — plan mode notes serve as seed keywords only; full systematic search required |
| Argument Sketches | `argument_builder` agent | Evaluate each sketch against 4-level scoring; only `adequate` or above proceed |

#### Quality Gate

Before conversion, ALL of the following debe ser true:
- [ ] Every chapter in the Chapter Plan has al menos 1 argument sketch rated `adequate` or above
- [ ] The overall paper structure maps to a recognized pattern in `paper_structure_patterns.md`
- [ ] At least 5 potential references have been identified (seeds for `literature_strategist`)
- [ ] The Pregunta de Investigación is finalized (not still evolving from Socratic dialogue)

#### What Gets Discarded
- Conversational filler from Socratic dialogue (greetings, confirmations, repetitions)
- Tentative ideas explicitly marked as "maybe" or "not sure" by the user
- Plan mode's iterative drafts (only the final version of each chapter plan carries over)

---

## Trigger-to-Mode Mapping Examples

```
"Write a paper on SDGs in HEI"           -> full
"Give me a paper outline for..."         -> outline-only
"Revise this paper based on feedback"    -> revision
"Write an abstract for this paper"       -> abstract-only
"Do a literature review on..."           -> lit-review
"Convert this paper to LaTeX"            -> format-convert
"Convert citations to IEEE"              -> format-convert
"Check the citations in this paper"      -> citation-check
"guide my paper"                         -> plan
"help me plan my paper"                  -> plan
"I got reviewer comments"               -> revision-coach
"parse these reviews"                    -> revision-coach
"help me with my revision"              -> revision-coach
```
