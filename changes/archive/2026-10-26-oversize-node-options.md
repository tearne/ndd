# Oversize node options

**Change Style:** Formal

## Intent

When a node is over its size bound, have the agent propose whichever response fits best, rather than defaulting to a split.

## Change Specification

Targets inline below; each replaces its live counterpart at Build.

### Node Sizing (`ndd.map.md`)

````markdown
# Node Sizing

[↑ Map](#map)

```yaml
id: z9p
approvals:
  tearne: {at: 2026-10-26, hash: b2d72af5}
```

A node's rough upper bound is around 800 characters, but the real test is felt during review.

Each time the agent edits a node it counts and reports its characters, *Detail* included and an inline link taken as its visible text; [navigation links](#navigation-links), *See also*, tables and diagrams are excluded. Over the bound, the agent flags the node, stamped or not, since an edit reopens its length. Rather than trimming silently, it proposes the best fit: tightening the prose, cutting what another node already owns, or splitting a node that carries two concepts.

On a map that carries stamps, a review, unlike an edit, does not flag a node that is not [due](#sign-off) for the session's [approver](#approver): the call was made and signed off. When the approver is not known, every node over the bound is flagged, and the agent says so.

**See also**

- [Local Sufficiency](#local-sufficiency) — why nodes stay small: a reader must grasp one node from the node alone.
````

### Node Sizing rule (`AGENT-RULES.md`)

````markdown
### Node Sizing

Count and report characters on every node you edit. Count the body plus *Detail*, inline links as their visible text, excluding navigation links, *See also*, tables and diagrams. Report the number in your message. Over about 800, flag it, stamped or not, and rather than trimming silently propose the best fit: tighten the prose, cut what another node already owns, or split a node that carries two concepts. The reported number is how the user sees the rule was followed. [Node Sizing](ndd.map.md#node-sizing).
````

## Context

Raised as an aside (2026-10-15). Change 070 (2026-10-26) tested the responses in practice: about a dozen oversize nodes were brought under the bound by tightening and cutting owned content, and one, Build, by splitting out Log.

## Log

- 2026-10-26: Build started; lock taken. Version claimed: 2.8.1-dev (patch). Live Node Sizing and its rule matched the spec baseline, so no drift.
- Landed the *Node Sizing* rule in `AGENT-RULES.md`.
- Promoted Node Sizing into `ndd.map.md`.

## Conclude

Completed.
