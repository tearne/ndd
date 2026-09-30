# Change Style and Formal specification

**Change Style:** Formal

## Intent

Restructure how a change's shape is chosen, replacing Cadence with Change Style and giving Formal a specification-based preparation.

## Context

Promoted at Conclude of Discussion `changes/archive/2026-09-29-approaches-discussion.md` on 2026-09-29, which developed the full shape. Naming refined during Build 050 to avoid "Approach" overloading: category is now Change Style. Related built changes: `010-unresolved-at-any-stage`, `020-introducing-discussion`, `040-map-edit-interaction-discipline` (all archived 2026-09-29).

## Approach

- **Rename Cadences → Change Style (map node).** Compound name mirrors Change Lifecycle and disambiguates what "style" scopes over.

- **Four style subnodes with distinct methodology, not just renames:**
  - **Trivial** (replaces Wander): Intent only. Frame shifts from "too small or too fluid to plan" to "virtually no substantive ambiguity — routine implementation choices delegated, agent verifies proportionately, surfaces consequential ambiguity if it emerges".
  - **Vibe** (new): Intent + Bounds. Agent proposes delegated discretion, consequential boundaries and review points from context.
  - **Exploratory** (replaces Explore): Intent + Focus (the conceptual question and a useful point to take stock). Replaces Explore's Approach+topics+done-when. Coding a spike requires separate authorization.
  - **Formal** (kept name, restructured): Intent + Specification + optional Implementation Plan. Replaces Formal's Approach+Worklist.

- **Retire current Approach and Worklist nodes.** Replaced by preparation sections that vary by style. The name "Approach" is freed up.

- **New plan-part nodes: Bounds, Focus, Specification, Implementation Plan.** Specification carries Formal specification mechanics from Discussion 030 (format-dependent target approval, pre-Build + Conclude verification with per-node re-engagement on drift, curated retain-or-drop asset walk).

- **Restructure Plan node.** Plan parts become conditional on the Change Style: Intent → (nothing / Bounds / Focus / Specification [+optional Implementation Plan]) → Build.

- **Change Style marker line.** Change titles' `**Cadence:** <name>` line renamed to `**Change Style:** <name>`.

- **AGENT-RULES.md updates.** Rules referencing cadence/approach/worklist names shift — Rule 11 (Plan Parts), Rule 12 (Caps), Rule 13 (Follow the Plan).

## Worklist

Under **Change-Management** (parent of Change Style):
- Rewrite the Cadences node as Change Style
- Rewrite the Wander subsection as Trivial (as a child node of Change Style)
- Add Vibe as a child node of Change Style
- Rewrite Explore as Exploratory (child node of Change Style)
- Rewrite Formal as a child node of Change Style (restructured around Specification + optional Implementation Plan)

Under the appropriate style parent (nested with the style whose preparation they are):
- Add Bounds as a child node of Vibe
- Add Focus as a child node of Exploratory
- Add Specification as a child node of Formal (format-dependent approval, drift verification, retain-or-drop asset walk)
- Add Implementation Plan as a child node of Formal (sibling of Specification)

Under **Plan**:
- Retire the Approach node (child of Plan)
- Retire the Worklist node (child of Plan)
- Rewrite the Plan node so it names Intent and points to style-specific preparation
- Update the Intent node (remove Wander reference; trim step becomes style-aware)

Sweeps:
- Sweep Build, Conclude and any other nodes for stale Approach / Worklist / Cadence references
- In the Change Style node itself, update the change-file header convention: "Cadence: X" → "Change Style: X"
- Regenerate AGENT-RULES.md for the rules whose source nodes changed

Added during Build:
- Rename existing top-level "Specification" node to "Map" (its content was always about the map's primacy); new plan-part is named "Change Specification" to avoid anchor collision. Ripple: inbound links, Contents entry, root-node section list.
- Under Formal, add a third child "Formal Build" alongside Change Specification and Implementation Plan, holding the Formal-specific overlay on Build / Conclude / Archiving (reconciliation, rework loop, drift check, retain-or-drop asset walk).

## Conclude

Two structural deviations from plan: preparation-section nodes (Bounds/Focus/Change Specification/Implementation Plan) sit under their style parents, not under Plan; and Formal gained a third child, Formal Build, holding the Formal-specific overlay on Build/Conclude/Archive.

Two renames: pre-existing Specification → Map; new plan-part → Change Specification (anchor collision).

AGENT-RULES rules 11–13 restructured with lists over prose. Parked: formal-restructure-concerns-discussion.md.
