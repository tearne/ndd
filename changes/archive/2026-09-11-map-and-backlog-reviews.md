# Map and backlog reviews

**Cadence:** Explore

## Intent

_(Approved 2026-09-11.)_

Replace the seven named maintenance checks the user is offered with two reviews: a **map review** and a **backlog review**. The objective work runs unprompted after every archive and is reported in a line, counts included. Each review is one yes-or-no at its moment: the map review after an archive, in a light scope, and before a release, in a full scope that adds the cross-node and code checks; the backlog review at the Startup Scan. A yes opens one findings list of the subjective items, walked one at a time. The checks survive as what a review looks for, askable by name.

## Context

Raised on 2026-09-11 after change 250 concluded and the agent recited the standing offers — Shape, Prose, Consistency, Rendering, release steps — which the user found too much to hold: "if I can't do it users won't be able to." The discussion settled two axes that need no user-facing names: objective versus subjective decides whether a finding is fixed and reported or put to the user; cheap versus expensive decides the scope, light after an archive and full before a release. Sign-off stays separate as the stakeholder's review. Touches Maintenance and its six children, Archiving, Release Steps, Startup Scan and agent rules 1 and 14.

## Approach

_(Approved 2026-09-11.)_

- **Two review nodes under Maintenance, beside Sign-off, which is untouched.** *Map Review* and *Backlog Review* are what the user is offered and asks for by name; the existing check nodes re-parent under Map Review unchanged in content, so the map keeps its description of what each looks for without the user having to choose among them. Backlog is renamed Backlog Review and keeps its text.

- **Tidy is the objective pass and keeps its name.** It runs unprompted after every archive as now, with one addition: its one-line report always carries the counts, such as nodes over size, so the state is known whether or not the review is accepted.

- **Scope is set by the moment, never asked.** Light after an archive: Shape and Prose. Full before a release: Consistency and Rendering added. Map Review holds a two-row table saying which checks each scope runs; the user overrides only by asking for a scope or a check by name.

- **One findings list, walked by Orient Then Focus.** A yes produces the list in chat, summarised first, then one item at a time; each is taken, deferred or dismissed. Taking one leads into the Engagement Rule for the edit it implies.

- **Nothing about findings is stored.** Every review recomputes from the map, so a deferred finding simply reappears next time and costs one word to dismiss again. This is the Sign-off principle applied to the map's own hygiene, and it avoids a findings file to maintain; recording a standing exemption such as "this node earns its length" is left out and noted as a possible follow-up.

- **Three trigger nodes change their wording only.** Archiving: Tidy runs and a map review is offered. Release Steps: a full map review is offered before the steps. Startup Scan: a backlog review is offered. Agent rules 1 and 14 follow in `dist/AGENT-RULES.md`.

- **Maintenance's table shrinks to the three reviews**, one row each, with the check-by-check table moving into Map Review; the prose keeps the point that deferring upkeep is safe because nothing is marked and each moment re-offers.

## Topics

_(Approved 2026-09-11. Build started the same day.)_

1. **Map Review node.** New child of Maintenance: the two scopes, the findings walk, and the table of which checks each scope runs. Shape, Prose, Consistency, Rendering and Tidy re-parent beneath it.
2. **Backlog Review.** The Backlog node renamed, its text kept, links re-pointed.
3. **Maintenance.** Prose rewritten around three reviews; the table reduced to one row each.
4. **Tidy.** One sentence: the report always carries the counts.
5. **Trigger wording.** Archiving, Release Steps and Startup Scan, then agent rules 1 and 14 in `dist/AGENT-RULES.md`, with a rebuild and reinstall.

**Done when:** every edit is written and approved with its count; the Contents lists and links in both files are in step; a dry run of the post-archive moment reads as one Tidy line and one offer, "Map review?", and nothing else; the agent rules match the map.

## Log

- 2026-09-11 — Tidy gains three moments instead of one: on hand-back over the nodes the user edited, at the Startup Scan and after an archive across the whole map. The hand-back check in the Engagement Rule is recognised as Tidy scoped to those nodes. Its report lists every fix and count, one line only when there is nothing. User raised it during topic 4; adds a sentence to Tidy, a pointer in Engagement Rule, and a line in Startup Scan (already in topic 5).
- 2026-09-11 — Startup Scan moment dropped from Tidy at the user's request: it would put housekeeping ahead of the user's agenda. Tidy keeps two moments, hand-back and before an archive.

## Conclude

_(Approved 2026-09-11.)_

Maintenance is now three reviews: Map Review with the five checks beneath it, Backlog Review, and Sign-off. Tidy runs on hand-back or before an archive, never at the Startup Scan, which was dropped for putting housekeeping ahead of the user's agenda. Archiving, Release Steps, Startup Scan and agent rules 1 and 14 say so. Two follow-ups were parked into the next change: the rules-update obligation and shipping the sources.
