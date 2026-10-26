# Diff fence nesting

**Change Style:** Formal

## Intent

Give the map a source for how a surfaced diff is shown, including fence nesting and small changes on long lines.

## Change Specification

Targets inline below; each replaces or joins its live counterpart at Build.

### Diffs, new (`ndd.map.md`, after Engagement Rule)

````markdown
# Diffs

[↑ Engagement Rule](#engagement-rule)

```yaml
id: d7f
approvals:
  tearne: {at: 2026-10-26, hash: da360f8c}
```

The agent shows every edit it puts up for approval as a diff in chat, so the user sees what changed alongside the new state. This holds for any file, not only the map. Something wholly new is shown whole, and a whole rewrite may be.

**Detail**

The diff sits in a `diff`-fenced block whose fence has more backticks than any fence inside it, so a quoted yaml block or code fence cannot close it early and strip its colouring. When a long line changes by only a word or two, the changed words are listed beneath the diff, since a line-level diff otherwise reads as a repeat.
````

### Engagement Rule (`ndd.map.md`)

````markdown
# Engagement Rule

[↑ Edit Governance](#edit-governance) \
[Diffs](#diffs)

```yaml
id: n3g
approvals:
  tearne: {at: 2026-10-26, hash: b4bd8360}
```

[Orient Then Focus](#orient-then-focus) applied to the map. Nodes are
1. drafted,
2. surfaced with [character count](#node-sizing), plus a [diff](#diffs) for an edit,
3. written as [Drafts](#drafts) directs, and
4. treated as settled only once the reply is [approval](#approval), which [stamps](#sign-off) the node where the map carries stamps.

No edit is silent or made in bulk. Corrections that change no meaning — a typo, spacing, a stale link — are applied and reported rather than surfaced, but only if every item in hand is one.

The rule binds the agent, not the user, who edits the map freely and unannounced. Their edit needs no approval, but the agent is expected to review it in one pass: running [Tidy](#tidy) over it as it directs, commenting on anything it would question, and logging it only if it changes what the build must do.
````

### Diffs rule (`AGENT-RULES.md`, replacing *Engagement Rule: Diffs*)

````markdown
### Diffs

Show every edit you put up for approval, to a map node or any other file, as a diff in chat, with what changed alongside the new state. Fence it as `diff` with more backticks than any fence inside it, and beneath a long line that changes only a little, list the changed words. Something wholly new is shown whole; a whole rewrite may be too. [Diffs](ndd.map.md#diffs), [Change Specification](ndd.map.md#change-specification).
````

### Rule Layout (`map.md`)

````markdown
# Rule Layout

[↑ Agent Rules](#agent-rules)

```yaml
id: r4l
approvals:
  tearne: {at: 2026-10-26, hash: 3e1b375e}
```

The rendering gathers by trigger what the map holds by concept, so an agent finds everything for one trigger in one rule. The trigger is named in each rule's first sentence, as [Rule Phrasing](#rule-phrasing) sets out; the concept is named in its heading.

- Each rule sits under a short level-3 heading naming its source node. Where several rules come from one node, each heading adds what that rule covers, as in *Engagement Rule: Corrections*. Agents cite rules by heading, and a node name takes the reader straight to the map, where a number leaves them to look it up.

- Each rule closes with a link to its source node.

- A rule with an occasional trigger, such as a session's start or a move between lifecycle stages, points to its node to be read and keeps only what shows it was followed. A rule that holds on every turn or fires often carries its substance in full, as a read each time would be skipped.
````

## Context

Raised as an aside (2026-10-16).

The *Engagement Rule: Diffs* rule's "```diff-fenced block" has no source in the map: the Engagement Rule says only "plus a diff for an edit". Noticed during change 091 (2026-10-17); the user expects it to fit in the Engagement Rule's *Detail*.

During change 070 (2026-10-26), a diff whose long line changed by a word or two hid the change, and the user read it as unchanged. Listing the changed words beneath the diff fixed it; the Engagement Rule's *Detail* could say so alongside the fence-nesting rule.
