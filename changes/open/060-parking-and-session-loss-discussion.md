# Parking and session loss

## Purpose

Work needs a defined way to be parked — stopping for the day, a reboot — and to survive an unplanned loss of session with as little lost or misread as possible. Raised 2026-10-16 after change 020 entered Build on scope nobody approved.

## What happened in 020

The baseline commit had no *Status* section. One was added afterwards, probably when the user asked to stop and resume later, and grew with each pause into a running plan summary: approvals, checks done, and a list of non-map work for Build (AGENT-RULES rules 1 and 19, both standards). At the next Startup Scan the agent placed the change from that section, reported "plan complete", and on the user's approval landed the listed edits without surfacing them.

## Gaps in the map

- **No planning pause record.** Build has its *Log* and Discussion its *Resume* anchor, trimmed on resumption; a change mid-planning has nothing, and *park* already means something else (a separate Intent-only change). The agent improvised, and nothing trimmed what it wrote.

- **Invented sections.** Nothing says a change document carries only the sections the method defines, though Change Lifecycle says state is read from contents, "not from any status field".

- **Formal's non-map deliverables.** Since 2.3.0 the Change Specification is map-only; with no Implementation Plan, non-map work had no approved home and its scope landed in the invented section.

- **Non-map method prose.** Formal Build lands non-map assets in place, and Map Edit Order covers only map nodes, so AGENT-RULES and the standards — method prose in this repository — could be written unseen.

- **Build progress is invisible.** Build says the agent marks progress, but the *Log* takes only the unexpected and "routine execution going to plan needs no entry", so settled plan items leave no trace on disk. In 020 the user asked for one Log line per settled item, written without asking (2026-10-16); whether the method should require that, and where, is open.

## Open questions

- What does parking a change mid-planning write, where, and what removes it on resumption? Should it share a shape with the Resume anchor?

- Unplanned loss gives no chance to write a pause record. What must already be on disk at every point so a fresh session reads the true state — e.g. approvals recorded as they happen, drafts marked as drafts, uncommitted work noticed at the Startup Scan?

- Should the Startup Scan distrust anything that is not a plan part, and say so when it finds it?

- Does the fix for Formal's non-map work belong in Change Specification, Implementation Plan, or Formal Build?
