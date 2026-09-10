# Write-then-review as a normal mode

## Intent

The user often asks the agent to write a draft in place so it can be reviewed in an editor rather than in chat. Consider making this a normal mode of operation rather than a per-request ask: the agent writes the draft, the user reviews it in their editor, approval follows. This may justify revisiting the "no git writes" rule — for example, the agent staging the existing version of a file before writing the new one, so the change shows in the editor as a diff against what was there. Untested; needs a trial to see whether the staging trick actually produces the diff wanted.

Parked via `aside:` during change 150's planning (2026-09-10).
