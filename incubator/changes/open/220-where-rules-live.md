# Where the rules live

## Intent

The map cannot enforce the rules it states: it is read when the agent chooses to read it, while `BOOTSTRAP.md` is loaded every session unconditionally. Rules that must fire at a particular moment — the edit order, what an approval covers, what a batch may contain — therefore live in the artefact least able to trigger them. Split the carriers: the map explains the method, the always-loaded file carries the short imperative form.

## Context

Evidence from change 210, which fixed the map's unenforceable wording and then watched the same defect recur one level up. Two failures in one session, both after the fix had landed:

- Several edits were batched into one script and applied without being surfaced. One item in the batch was a legitimately mechanical correction, and the whole batch inherited that fast path — the exemption added minutes earlier was the hole it fell through.
- "Agreed, archiving node" was read as approving prose that did not yet exist. Approval of a decision is not approval of its wording, and the edit order does not say so.

The rule that never slipped all session was the character count, because it emits something visible in the agent's message that the user notices missing. Compliance that leaves no trace failed repeatedly; compliance that produces an artefact held. That asymmetry is the thread to pull.
