# Write-then-review as a normal mode

**Cadence:** Wander

## Intent

_(Approved 2026-09-11, narrowed from the parked Intent below. Build started the same day.)_

Make write-then-review a stated mode rather than a per-request ask. The default is chat. A bare "write" switches for the item in hand only; a session-wide switch must say so, such as "write everything from here", and the agent never infers one from the other. "Write" means: put the draft in place, then stop until the user hands back; it is never approval and never a cue to move on. On hand-back the agent runs Tidy over what changed, then asks. A draft written in place stands provisional and is reverted if not approved. Agent rule 6 follows. The git-staging idea is dropped.

## Context

Parked via `aside:` during change 150's planning (2026-09-10) as: the user often asks the agent to write a draft in place to review in an editor; consider making this a normal mode; this may justify revisiting the no-git-writes rule, with the agent staging the existing version so the change shows as a diff. By 2026-09-11 change 150 had made delivery-in-place the user's choice in the Approval node, and the mode was in constant use. What remained was the Engagement Rule's order sentence, which still said write only after approval, and the meaning of the word "write", which the user did not want mistaken for approval to move on. The staging idea was dropped: work in progress is committed before hand-off, so the editor already shows the diff.

## Log

- 2026-09-11 — Engagement Rule order sentence, Approval delivery paragraph, agent rule 6 and a new Orientation bullet written; the *write* definition lives in Approval and the bullet links to it.

## Conclude

_(Approved 2026-09-11.)_

*Write* is now a defined term in Approval and a general mode in the agent rules' Orientation: a draft in place, then stop until hand-back, never approval. The Engagement Rule and rule 6 say an edit is settled on approval rather than written on it. The staging idea was dropped. Approval sits over the size bound at 822.
