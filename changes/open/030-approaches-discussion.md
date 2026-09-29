# Approaches and Formal specification

## Status and purpose

This is an active Discussion, not an approved implementation plan. `ndd.map.md` and `AGENT-RULES.md` remain unedited; Build is not authorized. Discussion approval is not implementation approval.

It proposes replacing **Cadence** with **Approach** — Trivial / Vibe / Exploratory / Formal, each carrying its own preparation section after Intent — and settles the mechanics of Formal specification (target approval, verification into the map, supporting-asset cleanup).

Split on 2026-09-29 from earlier `340-change-formality.md`. The Discussion artefact itself is now `020-introducing-discussion.md`.

## Approaches

Approach replaces Cadence as the term for Trivial, Vibe, Exploratory and Formal. As understanding develops, the agent proposes a fitting approach with a simple question. The user can accept or keep refining; the approaches are not a mandatory ladder.

| Approach | Meaning and agreement |
|---|---|
| Trivial | Intent is the whole plan. Virtually no substantive ambiguity; routine implementation choices remain delegated. The agent verifies proportionately during work and reports results. Surface consequential ambiguity if it emerges. |
| Vibe | After Intent, agree Bounds: agent-proposed discretion, consequential boundaries and review points. |
| Exploratory | After Intent, agree Focus: the conceptual question and a useful point to take stock. Coding a spike requires separate authorization. |
| Formal | After Intent, agree Specification, then an optional Implementation Plan when consequential delivery decisions warrant it. |

The agent proposes parameters from context rather than requiring users to anticipate every constraint. Trivial selection and agreement may fit one short exchange. Readiness does not authorize work.

Approved section names after Intent are **Bounds**, **Focus**, **Specification** and optional **Implementation Plan**; Trivial has no second planning section. Build log and Conclude remain for every Approach, including Trivial.

## Formal specification

Agree Intent -> choose Formal -> develop and approve the specification -> authorize Build and take the lock -> implement -> verify and conclude.

Once Specification is agreed, the agent may propose an Implementation Plan for consequential delivery choices or sequencing. If none is needed, no extra section is required. Build still needs explicit authorization.

Specification development stays with the change and its assets, without locking project assets. Before proposing Build, check it against current reality and surface revisions required by intervening work.

Use a map, sub-map, whole-map copy, table, flow diagram or prose as appropriate. Independent agents should be able to implement the same required behaviours and constraints; delegated implementation details may differ.

Keep the approved target separate from the current project map until verified. Whatever the specification format, the map must describe the completed result. Prefer one change file; use a same-name companion folder for supporting assets when warranted. At archival, retain useful evidence and rationale and remove disposable experiments.

If specification stalls, identify the uncertainty and propose conceptual exploration, a Vibe spike or smaller scope. A spike supplies learning, not automatic acceptance as the final implementation.

## Execution

Retain existing execution and completion rules where they suffice. Return to discussion when the agreement no longer fits, preserving completed work. Account for outstanding threads and require user acceptance before concluding, including Trivial work.

## Remaining decisions

- Detailed target-specification approval, verification into the current map and supporting-asset cleanup.

## Resume here

This is an active Discussion. The Approach names and preparation sections are settled; Formal specification's target-approval, map-verification and asset-cleanup mechanics are the open thread. Companion work: `020-introducing-discussion.md` (Discussion artefact), `010-unresolved-at-any-stage.md` (Unresolved rule adjustment).
