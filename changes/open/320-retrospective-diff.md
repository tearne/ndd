# Retrospective diff

## Intent

Show a stakeholder what changed in a node since their last approval, using the approval fingerprint to find the text they saw in git history. The diff is derived on demand and unavailable when that text cannot be found. This optional aid leaves approval and drift checks independent of git.

## Context

At display time, search git history for node text whose fingerprint matches the stakeholder’s approval hash, fetch that version, and diff it against current. The approval date guides the search but is not a strict cutoff: approved text may be committed later. Each stakeholder has their own baseline.

Kept separate from `approval-mechanics` because it is fundamentally a **display-time git operation with a real tooling component**, sitting between the approval stamps it consumes and the viewer that would render it. Git is load-bearing here — and only here on the approval axis — so it degrades gracefully: with no git there is no retrospective diff, while stamps, drift, and the due-queue all still work.

Decomposition item 4 of the keystone sequence in the retired `enhancement-discussion.md`, kept in git history. Depends on approval mechanics (built, archived 2026-09-10); relates to change 330 (tooling development) for the rendering surface. Renumbered from 90 on 2026-09-10 to sit with the sign-off theme at the end of the backlog.
