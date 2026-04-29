# Pipeline State Machine v2.0 — Complete Definition

Este documento defines all legal states, transition conditions, transition actions, and exception handling for pipeline-academico v2.0.

---

## State Definitions

### Stage States

| State | Description |
|-------|------------|
| `pending` | Not yet started, waiting for prerequisite stage to complete |
| `in_progress` | Currently executing |
| `completed` | Completed, deliverables recorded |
| `skipped` | User chose to skip (only for non-mandatory stages) |
| `blocked` | Preconditions not met (e.g., integrity check FAIL) |

### Pipeline Global States

| State | Description |
|-------|------------|
| `initializing` | Detecting entry point and materials |
| `running` | Pipeline executing (al menos one stage is in_progress) |
| `awaiting_confirmation` | Stage complete, waiting for user to confirm punto de control |
| `paused` | User paused, can resume at any time |
| `completed` | All required stages complete, final paper produced |
| `aborted` | User abandoned (e.g., chose to abandon after Reject) |

---

## State Transition Diagram (ASCII)

```
                        +-------------+
                        | INITIALIZING|
                        +------+------+
                               |
                    [Detect entry point & materials]
                               |
         +----------+----------+----------+----------+
         |          |          |          |          |
         v          v          v          v          v
    +--------+ +--------+ +--------+ +--------+ +--------+
    |Etapa 1 | |Etapa 2 | |Stg 2.5 | |Etapa 3 | |Etapa 4 |
    |RESEARCH| | WRITE  | |INTEGRIT| | REVIEW | | REVISE |
    +---+----+ +---+----+ +---+----+ +---+----+ +---+----+
        |          |          |          |          |
   [punto de control]   [punto de control]   |     [punto de control]  |
        |          |          |          |          |
        v          v          v          v          v
   +--------+ +--------+ +---+----+    |          |
   |Etapa 2 | |Stg 2.5 | |PASS?   |    |          |
   | WRITE  | |INTEGRIT| +---+----+    |          |
   +---+----+ +---+----+     |         |          |
                         +----+----+    |          |
                         |         |    |          |
                        Yes       No    |          |
                         |     [Fix]    |          |
                         |   [Re-verify]|          |
                    [punto de control]   |    |          |
                         |         |    |          |
                         v         |    |          |
                    +--------+     |    |          |
                    |Etapa 3 | <---+    |          |
                    | REVIEW |          |          |
                    +---+----+          |          |
                        |               |          |
                   [DECISION]           |          |
                        |               |          |
              +---------+---------+     |          |
              |         |         |     |          |
            Accept    Minor     Major   |          |
              |       Revision  Revision|          |
              |         |         |     |          |
              |    [punto de control]  [punto de control]      |
              |         |         |     |          |
              |         v         v     |          |
              |    +--------+ +--------+|          |
              |    |Etapa 4 | |Etapa 4 ||          |
              |    | REVISE | | REVISE ||          |
              |    +---+----+ +---+----+|          |
              |        |          |     |          |
              |   [punto de control]   [punto de control]      |
              |        |          |     |          |
              |        v          v     |          |
              |    +--------+ +--------+           |
              |    |Stg 3'  | |Stg 3'  |           |
              |    |RE-REV. | |RE-REV. |           |
              |    +---+----+ +---+----+           |
              |        |          |                 |
              |   [DECISION]  [DECISION]            |
              |        |          |                 |
              |     Accept      Major               |
              |     /Minor        |                 |
              |        |     [punto de control]           |
              |        |          |                 |
              |        |          v                 |
              |        |     +--------+             |
              |        |     |Stg 4'  |             |
              |        |     |RE-REVIS|             |
              |        |     +---+----+             |
              |        |          |                 |
              |   [punto de control]  [punto de control]        |
              |        |          |                 |
              v        v          v                 |
         +----+--------+----------+-----+           |
         |     Etapa 4.5                |           |
         |   FINAL INTEGRITY            |           |
         +----------+------------------+           |
                    |                               |
               [PASS? Zero issues]                  |
                    |                               |
              +-----+-----+                         |
              |           |                         |
             Yes         No                         |
              |        [Fix]                         |
              |      [Re-verify]                     |
         [punto de control]     |                         |
              |           |                         |
              v           |                         |
         +--------+       |                         |
         |Etapa 5 | <-----+                         |
         |FINALIZE|                                 |
         +---+----+                                 |
             |                                      |
             v                                      |
         +-------+                                  |
         |  END  |                                  |
         +-------+                                  |
```

---

## Legal State Transitions

### Normal Flow Transitions

| From | To | Precondition | Action |
|------|----|-------------|--------|
| INIT | Etapa 1 | User confirms starting from Etapa 1 | Detect mode preference, launch investigacion-profunda |
| INIT | Etapa 2 | User has research materials, confirms skipping Etapa 1 | Detect materials, launch articulo-academico |
| INIT | Etapa 2.5 | User has complete paper | Launch agente_verificacion_integridad |
| INIT | Etapa 3 | User has verified paper + integrity report | Confirm paper language/domain, launch reviewer |
| INIT | Etapa 4 | User has review comments | Confirm paper + review comments, launch revision |
| INIT | Etapa 5 | User has final draft for format conversion | Confirm format requirements, launch format-convert |
| Etapa 1 | **punto de control** | Etapa 1 completed | Wait for user confirmation |
| punto de control | Etapa 2 | User confirms | Traspaso PI Brief + Bibliography + Synthesis |
| Etapa 2 | **punto de control** | Etapa 2 completed, Paper Draft produced | Wait for user confirmation |
| punto de control | Etapa 2.5 | User confirms | Pass Paper Draft to integrity agent |
| Etapa 2.5 | **punto de control** | PASS | Wait for user confirmation |
| Etapa 2.5 | Etapa 2.5 (retry) | FAIL | Fix issues, re-verify (max 3 rounds) |
| punto de control | Etapa 3 | User confirms | Pass verified paper to reviewer |
| Etapa 3 | **punto de control** | Decision produced | Wait for user confirmation |
| punto de control | Etapa 4 | Decision = Minor/Major, user confirms | Pass Revision Roadmap |
| punto de control | Etapa 4.5 | Decision = Accept, user confirms | Skip revision, go directly to final verification |
| Etapa 4 | **punto de control** | Etapa 4 completed | Wait for user confirmation |
| punto de control | Etapa 3' | User confirms | Pass Revised Draft + Response to Reviewers |
| Etapa 3' | **punto de control** | Decision produced | Wait for user confirmation |
| punto de control | Etapa 4.5 | Decision = Accept/Minor, user confirms | Pass final draft to final verification |
| punto de control | Etapa 4' | Decision = Major, user confirms | Pass new Revision Roadmap |
| Etapa 4' | **punto de control** | Etapa 4' completed | Wait for user confirmation |
| punto de control | Etapa 4.5 | User confirms | Pass revised draft to final verification |
| Etapa 4.5 | **punto de control** | PASS (zero issues) | Wait for user confirmation |
| Etapa 4.5 | Etapa 4.5 (retry) | FAIL | Fix issues, re-verify (max 3 rounds) |
| punto de control | Etapa 5 | User confirms | Pass final accepted draft |

### Special Flow Transitions

| From | To | Precondition | Action |
|------|----|-------------|--------|
| Etapa 3 (Reject) | Etapa 2 | User chooses to restructure | Clear Etapa 2-3 state, preserve Etapa 1 materials, restart Etapa 2 |
| Etapa 3 (Reject) | ABORT | User chooses to abandon | Save all produced materials, mark pipeline aborted |
| Etapa 3' (Major) | Etapa 4' | User confirms | Last revision opportunity |
| Etapa 4' | Etapa 4.5 | Revision complete | Go directly to final verification (no return to review) |
| Any stage | PAUSED | User says "pause" or "stop here" | Save pipeline state |
| PAUSED | Previous stage | User returns to continue | Restore pipeline state, display Dashboard |

### Prohibited Transitions (Illegal)

| From | To | Reason |
|------|----|--------|
| Etapa 1 | Etapa 3 | Cannot skip Etapa 2 and 2.5 (unless mid-entry + has paper) |
| Etapa 2 | Etapa 3 | **Cannot skip Etapa 2.5 (integrity check is mandatory)** |
| Etapa 4 | Etapa 5 | Cannot skip RE-REVIEW (revision debe ser re-reviewed) |
| Etapa 3' | Etapa 5 | **Cannot skip Etapa 4.5 (final integrity check is mandatory)** |
| Etapa 4' | Etapa 3' | Cannot return to RE-REVIEW (max 1 round of RE-REVISE) |
| Etapa 5 | Etapa 3 | Cannot roll back (no review after FINALIZE) |
| completed | in_progress | Completed stages cannot restart |

---

## Material Dependency Matrix

| Material | Produced At | Consumed At | Required/Recommended |
|----------|-----------|-------------|---------------------|
| PI Brief | Etapa 1 | Etapa 2 (Phase 0) | Recommended |
| Methodology Blueprint | Etapa 1 | Etapa 2 (Phase 0) | Recommended |
| Bibliography | Etapa 1 | Etapa 2 (Phase 1) | Recommended |
| Synthesis Report | Etapa 1 | Etapa 2 (Phase 3) | Recommended |
| Paper Draft | Etapa 2 | Etapa 2.5 (input) | **Obligatorio** |
| **Integrity Report (Pre)** | **Etapa 2.5** | **Etapa 3 (prerequisite)** | **Obligatorio** |
| **Verified Paper Draft** | **Etapa 2.5** | **Etapa 3 (Phase 0)** | **Obligatorio** |
| Review Reports (x5) | Etapa 3 | Etapa 4 (input) | Required |
| Editorial Decision | Etapa 3 | Etapa 4 (input) | Required |
| Revision Roadmap | Etapa 3 | Etapa 4 (input) | Required |
| Revised Draft | Etapa 4 | Etapa 3' (Phase 0) | Required |
| Response to Reviewers | Etapa 4 | Etapa 3' (input) | Recommended |
| **Re-Review Report** | **Etapa 3'** | **Etapa 4' (input)** | **Required (if Major)** |
| **Re-Revised Draft** | **Etapa 4'** | **Etapa 4.5 (input)** | **Required (if executed)** |
| **Integrity Report (Final)** | **Etapa 4.5** | **Etapa 5 (prerequisite)** | **Obligatorio** |
| Final Paper | Etapa 5 | END (delivery) | Required |

---

## Exception State Handling

### Timeout

If a stage shows no progress for an extended period (e.g., Socratic mode exceeds 15 rounds without convergence):
1. state_tracker marks the stage as `stalled`
2. orchestrator provides options:
   - Switch mode (socratic -> full)
   - Narrow scope
   - Skip this stage (non-mandatory stages only)

### Missing Materials

If required materials are found missing during transition:
1. state_tracker reports the material gap
2. orchestrator suggests returning to the stage that produces that material
3. User can choose: backfill / skip (at own risk, but cannot skip integrity checks)

### Integrity Check FAIL Loop

If Etapa 2.5 or 4.5 corrections exceed 3 rounds without passing:
1. List all unverifiable items
2. User decides:
   - Manually handle unverifiable items
   - Remove unverifiable citations
   - Continue to next stage (with "partially unverified" warning)

### Session Interruption

If the user leaves and returns:
1. orchestrator displays Progress Dashboard
2. Confirm whether to continue from breakpoint
3. Check if any outdated materials need refreshing

---

## Revision Loop Rules (v2.0)

### Simplified Revision Cycle

```
v2.0's revision cycle is simpler and more explicit than v1.0:

Etapa 3 (First REVIEW)
  -> Decision: Accept -> Etapa 4.5
  -> Decision: Minor/Major -> Etapa 4
      -> Etapa 4 (REVISE)
          -> Etapa 3' (RE-REVIEW, verification)
              -> Decision: Accept/Minor -> Etapa 4.5
              -> Decision: Major -> Etapa 4' (last revision)
                  -> Etapa 4.5 (go directly to final verification, no return to review)

Maximum 1 round of RE-REVISE, no infinite loops.
Unresolved issues -> Acknowledged Limitations.
```

### Differences from v1.0

| v1.0 | v2.0 |
|------|------|
| Max 2 review-revise cycles | Fixed 2 reviews (Etapa 3 + Etapa 3') + max 1 RE-REVISE |
| No integrity check | Mandatory Pre-review + Final integrity check |
| 4 reviewers | 5 reviewers (+Abogado del Diablo) |
| Can skip any stage | Etapa 2.5 and 4.5 cannot be skipped |
| No mandatory punto de controls | Every stage requires a punto de control |

## Reset-boundary transitions (v3.6.3, flag-gated)

When `ARS_PASSPORT_RESET=1`, every FULL punto de control carries an implicit state transition to a terminal `awaiting_resume` state. The next stage only starts when a new session posts `resume_desde_pasaporte=<hash>`.

Transition semantics:

```
Stage N [working]
  -> FULL punto de control
    -> [flag OFF]  Stage N+1 [working]           (pre-v3.6.3 continuation)
    -> [flag ON]   append boundary entry -> awaiting_resume
         -> resume_desde_pasaporte=<hash>
              -> append resume entry (consumes_hash=<hash>)
              -> Stage N+1 [working]              (fresh session, passport-loaded)
```

Iron rules:

- `awaiting_resume` is not persisted in `state_tracker`; it is computed from the passport ledger. A `boundary` entry with hash `H` is awaiting resume iff no later `resume` entry in `reset_boundary[]` carries `consumes_hash == H`. Single pass over the ledger, no out-of-band state.
- `systematic-review` under flag ON cannot transition `Stage N → Stage N+1` without a fresh-session resume. In-session continuation is refused.
- Other modes under flag ON allow in-session continuation as a fallback, but the orchestrator must still load Stage N+1 input strictly from the passport (no replay of prior turns).
- SLIM punto de controls never enter `awaiting_resume`.
- MANDATORY punto de controls enter `awaiting_resume` when they are also FULL and flag is ON. Integrity gates remain MANDATORY; the reset does not downgrade them. The `### Resume Instruction` subsection emitted alongside `[REINICIO-PASAPORTE: ...]` carries the passport file path and resume command — it does NOT carry the user decision prompt. The decision prompt happens on resume, after the fresh session loads the passport (see next rule).
- If a `boundary` entry carries `pending_decision`, `next` is advisory only. The user's branch choice happens AFTER `resume_desde_pasaporte=<hash>` in the fresh session, never in the reset punto de control itself. The orchestrator re-prompts the user in the new session before transitioning to any `Stage N+1`. The `resume` entry records the chosen branch via `chosen_branch`. Actual routing comes from the matched option's `next_stage`/`next_mode`; `next` is a fallback default only.

See [`passport_as_reset_boundary.md`](passport_as_reset_boundary.md) for the full protocol.
