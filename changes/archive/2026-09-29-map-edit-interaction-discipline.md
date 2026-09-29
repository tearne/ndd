# Map-edit interaction discipline

**Cadence:** Formal

## Intent

Tighten interaction discipline for map-edit engagements — approval semantics for *write*, diff-shaped surfaces, re-read after user edits, and one-at-a-time end-of-Build.

## Context

Three-way merge of earlier asides parked during build 020 on 2026-09-29 (tighten write directive, present node edits clearly, surface one thing at a time). Combined because all concerns are interaction-discipline tweaks touching the same rules and nodes; a single Build cycle can settle them coherently.

## Approach

- **Extend the top-of-AGENT-RULES.md *write* clause** to make the trap explicit: even in reply to an "Approve?" ask, *write* is put-in-place, never approval — the stamp follows a separate yes.

- **Amend Engagement Rule (map)** — when surfacing an edit, show what changed alongside the new state.

- **Add a new AGENT-RULES.md rule** for ```diff-fenced node-edit surfaces (the chat-rendering of the map principle above).

- **Amend Conclude (map)** — Conclude note, changelog entry and Map Review offer are surfaced one at a time.

- **Amend Rule 18 (AGENT-RULES.md)** — re-read node after user reviews or edits, before continuing work on it.

- **No changes to Rule 14** — its "then offer one review" already implies the sequence; the substantive fix lives in the Conclude node.

- **Amend Conclude node (map, second amendment)** — sharpen the opening to name Conclude as a delta from the plan, guarding against restatement. Add a matching **Conclude Content** rule in AGENT-RULES.md rendering the concept.

## Worklist

- Extend the top-of-AGENT-RULES.md *write* clause for the "Approve?" trap.
- Amend Engagement Rule node — surface an edit alongside what changed.
- Amend Conclude node — Conclude note, changelog entry and Map Review offer surfaced one at a time.
- Add new AGENT-RULES.md rule (between Rules 6 and 7) requiring diff-fenced node-edit surfaces. Renumber subsequent rules.
- Amend AGENT-RULES.md Rule 18 to require re-reading a node before continuing work on it.
- Amend Conclude node — rewrite first paragraph to name Conclude as a delta from the plan.
- Add new AGENT-RULES.md rule (Conclude Content) between current Rules 14 (Held) and 15 (Archiving). Renumber subsequent rules.

## Log

2026-09-29 — Returned to planning mid-build: Conclude drafts kept restating the plan, exposing that the Conclude node's opening paragraph invites recap. Added worklist items 6 and 7 to sharpen the map node and render a matching rule in AGENT-RULES.md.

## Conclude

Completed. Plan grew mid-build by two items when recurring restatement drafts exposed that the original Conclude opening invited recap; sharpened it, and added Rule 15 (Conclude Content) to render the fix.
