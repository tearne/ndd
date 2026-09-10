# Map checks

**Cadence:** Explore

## Intent

Standardise the map's checks as a table under Map Maintenance: each check named, scoped, and given its trigger. Every check is available on demand, and some are offered at key points in the change cycle — after archival, and when choosing the next change. Review the two existing checks for name and scope, then add the missing ones. Deferred map upkeep is the motivating case: with a reliable catch-up check, skipping upkeep for a while is safe rather than silent rot.

_(Intent approved 2026-09-10; Approach approved 2026-09-10. Reshaped from "Deferred map maintenance / catch-up", parked via `aside:` on 2026-08-28.)_

## Approach

- **Map Maintenance becomes Standard Checks and carries a table** — columns *Check*, *Looks for*, *Trigger* — replacing its two-bullet list. The rename is because the catalogue covers the backlog as well as the map; one place shows it all, and the agent rules render their offers from it.

- **Trigger is a fixed vocabulary**: *runs after archival* (unprompted, mechanical only), *offered after archival*, *offered at Startup Scan*, *offered before release*, and *on demand*, which every check has. Release is already a moment in the cycle and takes the expensive whole-map checks — Rendering, Consistency, full cross-agent falsifiability. This is the whole answer to deferred upkeep: nothing is marked, each key point re-offers, and release gates the lot.

- **A check gets a node only when its row cannot carry the scope**, keeping Standard Checks under the size bound.

- **Bare one-word names** under the *Check* column. Consistency Upkeep becomes **Tidy**, reserving *Consistency* for the conceptual check: contradictions, competing concepts left untreated, redundancy. Tidy's three tiers (fixed, reported, escalated) stay.

- **Rendering** asks whether what exists still reads as a rendering of the map — a named scope compared against code and files, each disagreement reported, edits then through the Engagement Rule. "Rendering" is the map's own word for what agents make of it; Cross-Agent Falsifiability becomes its multi-rendering form.

- **Backlog** reads every parked change for stale references, order, a moved-on environment, and pruning. Offered at the Startup Scan straight after the status report, when the backlog has just been read.

- **Consistency absorbs Judgement Scan's two conceptual items** — the homeless concept and the ambiguity test — so each check answers one question. What remains becomes **Shape**: splits, verbosity, top-level boxes, style, child order.

- **Each existing check is reviewed with the user one at a time**, name then scope, before any new row is written.

- **The agent rules re-render** once the table settles: rule 14 names the archival offers, rule 1 the Startup Scan offer.

## Topics

_(Approved 2026-09-10.)_

1. **The five checks, one at a time** — Tidy, Shape, Consistency, Rendering, Backlog: settle name, *Looks for* and *Trigger* with the user, and whether each keeps or gains a node.

2. **Standard Checks** — the renamed Map Maintenance node with its table; the Edit Governance parent and Contents entry follow.

3. **The trigger points** — one sentence each in Archiving, Startup Scan and Release Steps pointing at the table; the Release Steps typos go with it. Cross-Agent Falsifiability restated as Rendering's multi-rendering form.

4. **Agent rules** — re-render rules 1 and 14 from the settled table.

**Done when:** every check has a row, no node still says Map Maintenance, Consistency Upkeep or Judgement Scan, each trigger point names the table, and the agent rules match.

## Log

- 2026-09-10 — Build started.
- 2026-09-10 — Working write-then-review at the user's instruction: drafts are written into the map for review in the editor, approval follows the review (see change 260). Tidy written: node renamed from Consistency Upkeep, body extended, seven inbound references re-pointed.
- 2026-09-10 — Tidy approved after review ("mechanical" replaced "computable"). Shape written: Judgement Scan renamed, its two conceptual items and the *Detail* removed pending Consistency; five inbound references re-pointed. Cross-Agent Falsifiability still cites Judgement Scan — left for Topic 3 when Consistency exists to point at.
- 2026-09-10 — Shape reviewed (opening rewritten to avoid recursion). Consistency written as a new node (id k4c) after Shape, with the two items and the *Detail* that left Shape; added to Contents and Map Maintenance links.
- 2026-09-10 — Shape approved after user edits (link to Tidy, scope line moved to end). Consistency rewritten to match Shape's judgement wording, 844 chars, flagged over bound.
- 2026-09-10 — Stray thought parked as change 270 (agent as stack manager) during Consistency review.
- 2026-09-10 — Consistency approved after user edits: the misc-bucket *Detail* removed (a misc bucket can be right, with care), homeless-concept bullet now "no definition or natural home"; 747 chars. Rendering written as a new node (id r3n) after Consistency; added to Contents and Map Maintenance links.
- 2026-09-10 — Rendering approved with a fourth bullet (ambiguity from the code side), 813 chars. Backlog written as a new node (id b7k) after Rendering — given a node rather than a row only, so the Startup Scan has something to point at; added to Contents and Map Maintenance links.
- 2026-09-10 — Backlog approved with renumbering made explicit, 587 chars. Topic 1 done.
- 2026-09-10 — Topic 2: Map Maintenance renamed Standard Checks with the table; Contents, Edit Governance and the five child parent-links re-pointed.
- 2026-09-10 — Standard Checks approved ("boxes" replaced by "top-level division" in Shape and the table). Topic 2 done.
- 2026-09-10 — Topic 3 written: Archiving (post-archival checks and before-release offer), Startup Scan (Backlog offer), Release Steps (before-release offer; two typos fixed), Cross-Agent Falsifiability (Consistency and Rendering as its everyday forms; dangling Judgement Scan link resolved).
- 2026-09-10 — Topic 3 approved.
- 2026-09-10 — Topic 4: rules 1 and 14 re-rendered in dist/AGENT-RULES.md (the maintained copy). ndd/AGENT-RULES.md is the vendored copy and stays stale until the next install.py run at release.
- 2026-09-10 — Deviation from plan, user-directed: Shape split into Shape (how the map is cut: split, merge, top-level division, child order) and a new Prose check (id p2w: writing conventions, wordiness). Six checks. Table, Contents, Standard Checks links, Writing Style see-also, Archiving and rule 14 updated.
- 2026-09-10 — Standard Checks table gains a *Reads* column grouping checks by subject (tree, text, ideas, code, backlog); opening sentence names the grouping. Chosen over a mechanical-versus-subjective by structure-versus-writing grid, which fits Tidy/Shape/Prose but leaves empty cells for the rest.
- 2026-09-10 — Shape, Prose, the regrouped table and rules 1 and 14 approved. All topics done; done-when met.

## Conclude

Standard Checks replaces Map Maintenance: a table of six checks grouped by what they read, each with a trigger. Tidy and Shape are the old Consistency Upkeep and Judgement Scan renamed and rescoped; Prose, Consistency, Rendering and Backlog are new. Archiving, Startup Scan, Release Steps and Cross-Agent Falsifiability name the table; rules 1 and 14 re-rendered in `dist/` only. Deviation: Shape split into Shape and Prose mid-build. Two thoughts parked as changes 260 and 270.
