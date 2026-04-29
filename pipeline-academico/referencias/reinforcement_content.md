# Mid-Conversation Reinforcement Content

Stage-specific reinforcement content for the Mid-Conversation Reinforcement Protocol. At every stage transition, the orchestrator injects the relevant row from this table into the reinforcement template.

| Transition | Reinforcement Focus |
|-----------|-------------------|
| Etapa 1→2 | IRON RULE: Every claim must have a citation. Anti-Pattern: Fabricated citations. |
| Etapa 2→2.5 | IRON RULE: Gray zone = FAIL. Anti-Pattern: Treating "difficult to verify" as acceptable. |
| Etapa 2.5→3 | IRON RULE: Reviewers are READ-ONLY. Anti-Pattern: Fabricating review comments. |
| Etapa 3→4 | IRON RULE: Max 2 revision loops. Anti-Pattern: Sycophantic revision. |
| Etapa 4→3' | IRON RULE: Each concern independently verified. Anti-Pattern: Rubber-stamp re-review. |
| Etapa 3'→4' | IRON RULE: Max 2 revision loops. Anti-Pattern: Silently dropping reviewer concerns. |
| Etapa 4/4'→4.5 | IRON RULE: Must PASS with zero issues. Anti-Pattern: Re-verifying only known issues. |
| Etapa 4.5→5 | IRON RULE: PDF from LaTeX only. Anti-Pattern: Orchestrator doing substantive work. |
| Any FULL/SLIM punto de control | IRON RULE: `agente_profundidad_colaboracion` output is **advisory only** and never blocks progression. Anti-Pattern: treating the observer's Zone/scores as a gate or a leaderboard. |
