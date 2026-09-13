# Approved nodes exempt from size flag

**Cadence:** Formal

## Intent

Stop flagging a node as oversize when it carries a stamp for the approver of the current session, matching the text as it stands: the size judgement was theirs and has been made.

### Context

- Parked from the Map Review of 2026-09-13, where all 16 oversize nodes were judged to stay and Conceptual Writing was stamped for tearne. Without this, every review re-raises the same 16.
- Depends on change 050, built and archived 2026-09-13, for the approver.

## Approach

_(Approved 2026-09-13.)_

**Only on a map that carries stamps.** A stamp-free map, where sign-off is not in use, is flagged exactly as today, and Tidy never resolves an approver on it. Everything below applies once the map has its first stamp.

**The exemption is "not due".** A node is exempt for the session's approver exactly when it is not *due* for them in Sign-off's sense: it carries their stamp and the fingerprint matches. That reuses one definition instead of adding a second, and the shipped fingerprint script's `--due` already answers it, so no tooling changes.

**Node Sizing states the rule.** It is where flagging is defined, so the exemption sits beside it in one sentence. Tidy and Shape each gain a clause pointing at it rather than restating it: Tidy counts the oversize nodes not cleared for the approver, and Shape says the stamp records the user's decision that a node earns its length.

**Editing still flags.** AGENT-RULES rule 8 is unchanged. An edited node has a new fingerprint and is due again for everyone, so the edit-time flag never needs the exemption; only review-time checks do.

**Tidy resolves the approver like any stamp would.** On a stamped map Tidy needs the handle, so it triggers the Approver's lazy resolution. When that would mean asking, Tidy reports the full oversize count and says the handle is unknown, since Tidy is meant to need no prompting; Map Review, which follows and does ask, can resolve it.

## Worklist

- [x] Edit Node Sizing: on a map that carries stamps, a node not due for the session's approver is not flagged at review; link to Sign-off and Approver.
- [x] Edit Tidy: the oversize count excludes nodes cleared for the approver, and when the handle would need asking Tidy reports the full count and says so.
- [x] Edit Shape: a stamp records the user's decision that an oversize node earns its length.

## Log

- 2026-09-13: Beyond the plan, Tidy gained a sentence letting it name a judgement item early rather than wait for Map Review, at the user's request during review of item 2.
- 2026-09-13: Shape's first bullet trimmed with the user during review: the split clause, the stale "size table" phrase and the oversize remark all cut; the stamp clause now covers the whole finding, not size alone.

## Conclude

Completed.
