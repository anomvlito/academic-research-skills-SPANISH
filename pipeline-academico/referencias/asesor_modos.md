# Mode Advisor — Unified Cross-Skill Decision Tree

## Propósito

Helps users (and the pipeline orchestrator) select the right skill and mode for their current situation. Eliminates the most common routing mistakes by mapping user intent to the optimal entry point.

---

## Quick Decision Matrix

| What do you want? | How far along? | Time? | Skill + Mode |
|-------------------|---------------|-------|--------------|
| Explore a topic | Starting fresh | 30 min | investigacion-profunda quick |
| Explore a topic | Starting fresh | 2+ hr | investigacion-profunda full |
| Think through a research idea | Have vague idea | Any | investigacion-profunda socratic |
| Systematic review | Have clear PICO | 3+ hr | investigacion-profunda systematic-review |
| Verify claims | Have specific claims | 30 min | investigacion-profunda fact-check |
| Write a paper | Have research done | 2+ hr | articulo-academico full |
| Plan a paper step by step | Have RQ, need structure | 1+ hr | articulo-academico plan |
| Fix citations | Have draft | 30 min | articulo-academico citation-check |
| Convert format | Have final draft | 15 min | articulo-academico format-convert |
| Review a paper | Have paper to evaluate | 1 hr | articulo-academico-reviewer full |
| Check revision quality | Have revised draft | 30 min | articulo-academico-reviewer re-review |
| Full pipeline (zero to publication) | Starting fresh | 5+ hr | pipeline-academico |
| Handle real reviewer feedback | Have review comments | 1+ hr | pipeline-academico (Etapa 4 entry) |

---

## Common Misconceptions

| User Says | They Probably Need | Why |
|-----------|-------------------|-----|
| "Write me a paper on X" | investigacion-profunda first, THEN articulo-academico | Writing without research produces shallow papers with unsupported claims |
| "Review my paper" (but no draft exists) | articulo-academico plan mode | They need to write first, not review |
| "Check my citations" (but paper isn't done) | articulo-academico full mode | Finish writing first, then check citations as a separate pass |
| "I need a systematic review" | investigacion-profunda systematic-review mode | NOT articulo-academico lit-review structure (different methodology: PRISMA vs narrative) |
| "Just give me a quick paper" | investigacion-profunda quick + articulo-academico full | Quick research is fine, but paper writing still needs the full mode for quality |
| "Format my paper as APA" | articulo-academico format-convert mode | Not a rewrite; purely formatting transformation |
| "I got reviewer comments" | pipeline-academico Etapa 4 entry (External Review) | Needs structured intake + strategic coaching, not just "fix what they said" |

---

## User Archetype Recommendations

| Archetype | Recommended Workflow | Rationale |
|-----------|---------------------|-----------|
| Graduate student (first paper) | investigacion-profunda socratic -> articulo-academico plan -> full pipeline | Socratic mode builds research thinking; plan mode structures the paper incrementally; pipeline ensures quality gates |
| Experienced researcher (submission prep) | pipeline-academico (full, from Etapa 1 or mid-entry) | Knows what they want; benefits from the automated quality assurance and integrity checks |
| Advisor reviewing student work | articulo-academico-reviewer full | Provides structured multi-perspective feedback the advisor can use in mentoring |
| Quick literature scan | investigacion-profunda quick or lit-review | Fast turnaround; no need for full pipeline overhead |
| Journal revision response | pipeline-academico (Etapa 4 entry with review comments) | External Review Protocol handles real reviewer feedback with strategic coaching |
| Conference paper (short deadline) | investigacion-profunda quick -> articulo-academico full (conference type) | Compressed timeline; quick research + full writing with conference structure |
| Thesis chapter | investigacion-profunda full -> articulo-academico full | Each chapter treated as a standalone paper; full depth needed |
| Policy brief | investigacion-profunda quick -> articulo-academico full (policy_brief type) | Evidence-based but concise; quick research sufficient for policy scope |

---

## Skill Capability Boundaries

Understanding what each skill can and cannot do prevents misrouting:

| Skill | Can Do | Cannot Do |
|-------|--------|-----------|
| investigacion-profunda | Literature search, synthesis, PI refinement, fact-checking | Write papers, review papers, format documents |
| articulo-academico | Write papers, revise papers, format documents, check citations | Conduct original research, review papers (as reviewer), verify integrity |
| articulo-academico-reviewer | Review papers (5-person panel), re-review revisions | Write papers, conduct research, fix issues (only identifies them) |
| pipeline-academico | Orchestrate all stages, manage transitions, track state | Perform any substantive work (purely dispatching and coordinating) |
| agente_verificacion_integridad | Verify references, citations, data, originality | Fix issues (only identifies them), review paper quality |

---

## Decision Flowchart

```
START: What does the user want?
  |
  +--> "I want to research/explore/investigate"
  |      |
  |      +--> Have specific claims to verify? --> investigacion-profunda fact-check
  |      +--> Have clear PICO/systematic question? --> investigacion-profunda systematic-review
  |      +--> Want guided exploration? --> investigacion-profunda socratic
  |      +--> Want direct results, have time? --> investigacion-profunda full
  |      +--> Want direct results, short on time? --> investigacion-profunda quick
  |
  +--> "I want to write a paper"
  |      |
  |      +--> Have research/literature ready? --> articulo-academico (plan or full)
  |      +--> No research done yet? --> investigacion-profunda FIRST, then articulo-academico
  |      +--> Want full quality assurance? --> pipeline-academico (from Etapa 1)
  |
  +--> "I want someone to review my paper"
  |      |
  |      +--> Have a complete draft? --> articulo-academico-reviewer full
  |      +--> Want integrity check + review? --> pipeline-academico (Etapa 2.5 entry)
  |      +--> No draft yet? --> articulo-academico first
  |
  +--> "I need to revise based on feedback"
  |      |
  |      +--> From AI reviewers (pipeline)? --> Continue pipeline (Etapa 4)
  |      +--> From real journal reviewers? --> pipeline-academico Etapa 4 entry (External Review)
  |
  +--> "I want the full treatment (research to publication)"
         |
         +--> pipeline-academico (Etapa 1 entry)
```

---

## Pipeline Stage Entry Points

For users entering the pipeline mid-stream, this table clarifies what materials are needed:

| Entry Point | Required Materials | What Gets Skipped | Integrity Implications |
|------------|-------------------|-------------------|----------------------|
| Etapa 1 (RESEARCH) | None | Nothing | Full pipeline |
| Etapa 2 (WRITE) | PI Brief + Bibliography | Etapa 1 | Full pipeline from Etapa 2 |
| Etapa 2.5 (INTEGRITY) | Paper draft | Stages 1-2 | Integrity check runs on provided draft |
| Etapa 3 (REVIEW) | Verified paper + integrity report | Stages 1-2.5 | User must provide integrity evidence |
| Etapa 4 (REVISE) | Paper + review comments | Stages 1-3 | Pipeline runs Etapa 4 -> 3' -> 4' -> 4.5 -> 5 |
| Etapa 5 (FINALIZE) | Paper + integrity pass report | Stages 1-4.5 | Must show Etapa 4.5 passed |

---

## Anti-Patrones

These are common workflow mistakes to avoid:

| Anti-Pattern | Problem | Correct Approach |
|-------------|---------|-----------------|
| Skipping research | Paper lacks evidence depth | Always do al menos investigacion-profunda quick |
| Writing then researching | Confirmation bias in source selection | Research first, write second |
| Reviewing before integrity check | Wasted review effort on fabricated citations | Always Etapa 2.5 before Etapa 3 |
| Accepting all reviewer comments blindly | May introduce inconsistencies or weaken valid arguments | Use External Review Protocol's strategic coaching |
| Running pipeline for a 1-page abstract | Overhead far exceeds benefit | Use articulo-academico full directly |
| Using fact-check mode for literature review | Different purpose and methodology | Use investigacion-profunda full or systematic-review |
