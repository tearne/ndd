# Where the rules live

## Intent

The map cannot enforce the rules it states: it is read when the agent chooses to read it, while `BOOTSTRAP.md` is loaded every session unconditionally. Rules that must fire at a particular moment — the edit order, what an approval covers, what a batch may contain — therefore live in the artefact least able to trigger them. Split the carriers: the map explains the method, the always-loaded file carries the short imperative form.

## Context

Evidence from change 210, which fixed the map's unenforceable wording and then watched the same defect recur one level up. Two failures in one session, both after the fix had landed:

- Several edits were batched into one script and applied without being surfaced. One item in the batch was a legitimately mechanical correction, and the whole batch inherited that fast path — the exemption added minutes earlier was the hole it fell through.
- "Agreed, archiving node" was read as approving prose that did not yet exist. Approval of a decision is not approval of its wording, and the edit order does not say so.

The rule that never slipped all session was the character count, because it emits something visible in the agent's message that the user notices missing. Compliance that leaves no trace failed repeatedly; compliance that produces an artefact held. That asymmetry is the thread to pull.

## Approach

- **`BOOTSTRAP.md` becomes a rendering of the map into agent-imperative form**, renamed to say so, and is derived rather than authoritative. The map is edited; the rendering follows. Nothing is ever fixed in the rendering alone.

- **Each imperative carries the address of its source node** as *name (id)*, restoring the convention deleted in 210 as unused. A rule can then be traced to its explanation, and survives the node being renamed.

- **Only rules that fire earn a place.** Explanation, rationale and definitions stay in the map. No cap on length — the file's sole measure is agent compliance, not readability.

- **Minimal orientation only** — enough to make the addresses navigable and the two maps distinguishable. Today's bootstrap and upgrade prose stays, having nowhere better to live.

- **The map gains a node for the rendering**, stating that it is derived and that the ambiguity test applies to it: two agents rendering the same map should produce the same instructions, and divergence is a map defect rather than a rendering one.

- **Fix the two failures from 210 in the map, not the rendering.** The batch boundary and the scope of an approval are rules, belonging in *Engagement Rule* and *Gates and Permissions*. Doing this first means the rendering has something correct to carry, and doubles as the first test of whether a map rule renders cleanly into an imperative.

### Unresolved

*(empty)*

## Topics

- **The map's rules** — the batch boundary (a fast path applies only to a wholly mechanical batch) and the scope of an approval (it covers what was surfaced; approving a decision authorises drafting, not writing).

- **The rendering** — its content, shape and name, and what orientation survives in it.

- **The map node** — describing the rendering as derived, with falsifiability applying to it; and restoring *name (id)* as its addressing convention.

**Done when** the renamed file contains every rule that must fire, each addressed to its source node, and the map explains the arrangement without restating the imperatives.

## Log

- **Paused 2026-09-03 with the lock held.** No map or file edits have been made under this change — the map is untouched since 210 concluded. Topic 1 was mid-proposal.
- Resume at topic 1, the map's own rules, which splits into two independent items with no ordering between them:
  1. **Approval scope** — an approval covers what was surfaced; agreeing to a decision authorises drafting the prose that carries it, not writing it. Home is [Gates and Permissions](#gates-and-permissions), already 917 and over the bound before this change touched it. The open question at the pause: add the rule and leave the node at ~1049 for the 190 backlog, or split approval into its own child node (drafted at 317, leaving Gates at 724) as part of adding it. The node's own opening — "two kinds: approval and write permission" — argues for the split.
  2. **Batch boundary** — the mechanical fast path applies only when every item in hand is a correction that changes no meaning. Home is [Engagement Rule](#engagement-rule) at 780; the drafted wording lands it at 812, or 778 if ", a lighter confirmation otherwise" is cut from the preceding sentence as now-redundant.
- Then topics 2 and 3, untouched: the rendering itself (content, shape, name, surviving orientation) and the map node describing it as derived, with *name (id)* restored as its addressing convention.
