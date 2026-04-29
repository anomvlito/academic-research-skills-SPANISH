# Two-Stage Review Protocol (Added in v2.0)

## Etapa 3: First Review (Full Review)

- **Input**: Paper that passed integrity check
- **Review team**: EIC + R1 (methodology) + R2 (domain) + R3 (interdisciplinary) + Abogado del Diablo
- **Output**: 5 review reports + Editorial Decision + Revision Roadmap + Socratic Revision Coaching
- **Decision branches**: Accept -> Etapa 4.5 / Minor|Major -> Revision Coaching -> Etapa 4 / Reject -> Etapa 2 or end

See `articulo-academico-reviewer/HABILIDAD.md` for review process details.

## Etapa 3 -> 4 Transition: Revision Coaching

EIC uses Socratic dialogue to guide the user in understanding review comments and planning revision strategy (max 8 rounds). User can say "just fix it for me" to skip.

## Etapa 3': Second Review (Verification Review)

- **Input**: Revised draft + Response to Reviewers + original Revision Roadmap
- **Mode**: `articulo-academico-reviewer` re-review mode
- **Output**: Revision response comparison table + new issues list + new Editorial Decision + R&R Traceability Matrix (Schema 11)
- **Decision branches**: Accept|Minor -> Etapa 4.5 / Major -> Residual Coaching -> Etapa 4'

See `articulo-academico-reviewer/HABILIDAD.md` Re-Review Mode for verification review process.

## Etapa 3' -> 4' Transition: Residual Coaching

EIC guides the user in understanding residual issues and making trade-offs (max 5 rounds). User can say "just fix it" to skip.
