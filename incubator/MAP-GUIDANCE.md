# Guidance for Writing Maps

Working principles for building conceptual maps of software systems. Emerging from practice — expect these to evolve.


## Structure: a tree of nodes

A map is a tree. Each node is a `#` heading followed by navigation links, prose, and optional sections. The tree structure is encoded in the links, not in the filesystem or heading hierarchy.

A rendered tree overview at the top of the map file aids orientation — keep it in sync with the nodes below. Use box-drawing characters in a fenced code block:

```
Application
├ Deck
│ ├ Waveform Colour
│ ├ Detail Waveform
│ │ ├ Wide Buffer
│ │ └ Sliding Viewport
│ └ Transport
├ Browser (TODO)
└ Settings (TODO)
```

Mark unmapped nodes with `(TODO)`. Place the tree at the end of the root node, after its prose.

### Node format

A node is a **superset of a plain-markdown section**: everything beyond the heading and prose is optional, and a node using none of it is an ordinary markdown section. The full shape:

````markdown
# Node Name

```yaml
id: k7f
```

[Parent Name](#parent)
[Child One](#child-one)
[Child Two](#child-two)

Terse conceptual description. Lead with the mental picture.

> [!IMPORTANT] callout for a load-bearing point the reader should not skim.

**Detail**

Implementation-level precision — parameters, thresholds, protocols.
The user can stop reading before this; the agent reads through it.

**See also**

- [Other Node](#other-node) — why the relationship matters
````

Order: heading → scaffolding block → nav links → prose → optional Detail → optional See also.

### Node identity

- A node may carry a **stable ID** in a fenced YAML **scaffolding block** directly under the heading. The block holds all machine-maintained metadata — today just `id` — and is agent-maintained, like nav links; a viewer collapses it, a reader ignores it.
- The ID is an **opaque short token** (lowercase alphanumeric, 3+ chars, e.g. `k7f`) — opaque rather than a readable slug, so there is no temptation to rewrite it on rename. It is **assigned once**, **unique within the map**, and **never changed** — not on rename, not on move. Length grows only to resolve a collision.
- Identity is what lets a node's history (e.g. a seed's anchor, and later approval and drift state) survive a rename. Navigation never depends on the ID, so its only job is durable identity.

### Navigation links

Each node carries markdown links encoding its position in the tree:

- `[Parent Name](#parent)` — one link to the parent, omitted only for the root node. `[Child Name](#child)` — one per child.
- Links use the actual node name as the link text, not a generic `Up`/`Down` label, and resolve **by name** — navigable with `gd` in editors with a markdown LSP (marksman recommended). The ID is never a link target.
- To see a node's siblings, follow the parent link — the parent's child links show them all.
- Because links are name-anchored, a rename is a mechanical re-point of the affected links; the node's ID is untouched, so any history stays bound across the rename.

### Degradation

- Every part above the prose is optional. A node with **no scaffolding block** is a plain, name-only node. A map with no scaffolding blocks anywhere is a plain-markdown map, fully valid.
- A missing ID means "no stable identity — fall back to the name." Nothing requires the machinery until a project reaches for it.

### Who maintains what

- **The user maintains the content** — prose, decisions, assumptions, and conceptual relationships (what is a child of what).
- **The agent maintains the navigation links** and the scaffolding block (e.g. node IDs), and flags inconsistencies.

### Node sections

What each optional section is for, and when it earns its place:

- **Prose** — terse conceptual description, leads with the mental picture. This is what the user reads.
- **Callouts** — `[!IMPORTANT]` for load-bearing points where skimming would lose the reader: design trade-offs, non-obvious assumptions, constraints that shape the whole node. The prose carries the semantic load (words like "assume", "decided", "never"); the callout just marks "don't skim this". Not for every notable fact.
- **Detail** — implementation-level precision (parameters, thresholds, algorithms). The user can stop reading before this. Marked with bold `**Detail**`.
- **See also** — cross-cutting references that aren't parent/child. Marked with bold `**See also**`. Each entry says why the relationship matters.

### Root node naming

Default to the project's name at the root. Every file-root H1 must be unambiguous with every other heading in the map — duplicates break navigation (fragile auto-generated anchors, indistinguishable jump-picker entries).

When the project name clashes with a prominent internal concept, pick whichever form reads best:

- Domain scoping term for the root ("Audio Player", "Build Tool").
- Suffix ("Deck Application Map", "Deck Map Subtree").
- Parenthetical ("Deck (Application)").
- Rename the internal node more specifically.

Prefer a term that carries domain information over a generic "Application".

## Node sizing

Aim for under ~800 characters per node. The real test: if a node feels like it warrants sub-sections, it's too big — split into children. Flag nodes that exceed this to the user.


## The only-child preference

Prefer folding a singleton child into its parent. Keep it as its own node when it is a distinct concept in the user's model, or when its detail would bloat the parent. A useful test: if a sibling were later added, would this still be a node? If yes, keep it now.

## Content principles

- Lead with the mental picture, not the implementation.
- Name the boxes before explaining them ("three mechanisms: A, B, C" — then a node each).
- Not code-structure-coupled — may discuss technical concepts when load-bearing, but should not mirror module structure, reference function names, or break on refactor.
- Use continuous lines (no hard wraps mid-sentence) for soft-wrap compatibility.
- Blank line between bullet points for readability.


## File organisation

The format is agnostic about how nodes are distributed across files:

- **Single file** — all nodes in one file, linked by anchors. Good for smaller systems.
- **Multiple files** — nodes spread across files, linked by relative paths. Good for larger systems.
- Navigation links work identically either way — `[Up](#parent)` for same-file, `[Up](other-file.md#parent)` for cross-file.


## Seeds: future work anchored to nodes

Future work — a concrete TODO or an idea to weigh — is captured as a **seed**: a small change-document head stored in `changes/open/`, not written into `map.md`. A seed **anchors** to the node it concerns by that node's stable ID, so it stays bound across renames and moves, and the startup scan can surface a node's pending seeds when you navigate there. The map itself stays reality-only; seeds are *of* the map but not *in* it.

**Placement.** On capture the agent proposes the anchor — the node under discussion, or its nearest mapped ancestor — and the user confirms or redirects in a line. When no home is obvious the anchor falls back to the nearest existing ancestor, and failing that the root; a seed always lands on the map's spine, never in a separate backlog doc.

**Degradation.** A map with no seeds shows nothing — the mechanism is invisible until used. A node with no stable ID cannot be a precise anchor, so the seed names the nearest node that has one, or the nearest named node if the map carries no IDs at all.

See `PROCESS.md` for how a seed matures into a worked change and `KEYWORDS.md` for the `aside:` capture gesture.

## When to edit the map

Two rules govern every map edit.

**Sync rule** — *The map describes what exists, not what is proposed.* Don't edit the map ahead of the code. Edits that describe pending work defer until the code is built. Future work is instead captured as **seeds** anchored to nodes (see above), which live in `changes/` rather than on the map, so they never breach this rule.

**Engagement rule** — *Every map edit is negotiated.* One node at a time, with user engagement. Never silent, never bulk. When an edit touches two or more nodes, enumerate them in chat up front and tick through them as each is settled. Per-node approval prompts are phrased as comprehension checks — "does that fit your mental model?", "is that clear enough?" — not yes/no gates.

The map is exempt from the active-change requirement: edits that describe existing reality may happen at any time.

### Map edits and the change lifecycle

Map edits are negotiated per-node per the Engagement rule — never pre-staged as wholesale node bodies in an Approach. Map-only work happens as per-node negotiation directly, exempt from the change lifecycle alongside the existing active-change exemption.

For code changes, Approach and Plan typically don't propose map edits and Build doesn't touch the map. Map catch-up follows the build as a per-node negotiation. The completed change's Conclusion may carry a starter draft. Tightly-bound exceptions where small map work rides along a code change are allowed when it genuinely fits.

## Maintaining the map

Signals that the map needs attention:

- **A node feels like it needs sub-sections** — split into children.
- **Top-level boxes don't match the user's mental model** — restructure. The map follows the user's model, not the code's architecture.
- **A node has grown verbose** — cut aggressively. Move precision to **Detail**.
- **New concepts don't have a natural home** — the decomposition may need rethinking, not a misc section.
- **An only-child exists that isn't a distinct concept** — fold it into its parent.

Don't treat the map as append-only. Restructuring is not rework — it's what keeps the map useful.

**Ambiguity test.** Regularly ask whether each node in the affected area is sufficiently well characterised that a fresh agent could build from it without guessing. Flag ambiguities to the user — they are map quality issues, not implementation issues.
