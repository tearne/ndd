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

Target-specification approval is format-dependent. A map-shape target (nodes, sub-map, whole-map copy) is approved per-node under the Engagement Rule — stamps written on the target transfer at verification. A prose, table or diagram target is surfaced whole, or in named sections when a cap is meaningful. A mixed spec has each part follow its own rule.

Verification into the live map happens at Conclude, in two checkpoints. Pre-Build the target is reconciled to current reality and any drift surfaced for revision. At Conclude verification, for each node the target touches the agent compares the current live-map against what was there at pre-Build reconciliation: matching nodes are copied in mechanically with their stamps; drifted nodes are re-surfaced under the Engagement Rule with the target text as draft. This preserves the "no map edit is silent" rule without double-approving unchanged content.

Supporting assets live in a same-name companion folder next to the change file during Build. At Conclude, before archive, the agent walks each asset with a recommendation (retain or drop, with a short reason); the user approves or overrides. The folder, with only retained assets, is moved alongside the renamed change file at archival.

## Execution

Retain existing execution and completion rules where they suffice. Return to discussion when the agreement no longer fits, preserving completed work. Account for outstanding threads and require user acceptance before concluding, including Trivial work.

## Conclude

Settled the Approach rename (Trivial / Vibe / Exploratory / Formal with preparation sections) and Formal specification mechanics (format-dependent target approval, two-checkpoint verification, curated asset retain-or-drop). Promoted as parked change [050-approach-and-formal-specification](050-approach-and-formal-specification.md). Nothing dropped; nothing flagged for resurfacing.
