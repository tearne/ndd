# NDD

[↑ NDD Project](map.md#ndd-project) \
[Contents](#contents) \
[Principles](#principles) \
[Map](#map) \
[Change-Management](#change-management) \
[Maintenance](#maintenance) \
[Tooling](#tooling) \
[Standards](#standards)

```yaml
id: a3k
approvals:
  tearne: {at: 2026-10-07, hash: 34571557}
```

NDD, Non-Dead Design, aims to improve knowledge management for agentic software development. The name reflects the [three deaths](#three-deaths) it seeks to prevent: of specifications, of structural thinking, and of comprehension.

The map is the one artefact that keeps all three alive: a conceptual **map** of the system, acting as the hub for specification and change management rather than a document off to one side.

- **Principles** — the founding rationale in more detail.
- **Map** — the developer's conceptual model of the system, and the primary specification.
- **Change-Management** — how the spec evolves, through a change lifecycle and user-owned gates.
- **Maintenance** — the reviews that keep the map, the code and the backlog in step.
- **Tooling** — the generic markdown tooling the format is designed to exploit.
- **Standards** — suggested coding standards NDD ships for the code agents write on a project.


# Contents

[↑ NDD](#ndd)

```yaml
id: ct5
```

- [NDD](#ndd)
  - [Principles](#principles)
    - [Three Deaths](#three-deaths)
    - [Comprehension is an Activity](#comprehension-is-an-activity)
    - [Intent Memory](#intent-memory)
    - [Enjoyment](#enjoyment)
    - [Local Sufficiency](#local-sufficiency)
      - [Trees over Graphs](#trees-over-graphs)
    - [Cross-Agent Falsifiability](#cross-agent-falsifiability)
    - [Orient Then Focus](#orient-then-focus)
  - [Map](#map)
    - [Node](#node)
      - [Node Identity](#node-identity)
      - [Navigation Links](#navigation-links)
      - [Node Sections](#node-sections)
        - [Callouts](#callouts)
      - [Approval Stamp](#approval-stamp)
        - [Fingerprint](#fingerprint)
          - [Fingerprint Helper](#fingerprint-helper)
    - [Map Structure](#map-structure)
      - [Map Files](#map-files)
    - [Node Sizing](#node-sizing)
    - [Writing Style](#writing-style)
      - [Conceptual Writing](#conceptual-writing)
      - [Formatting](#formatting)
      - [Economy](#economy)
    - [Edit Governance](#edit-governance)
      - [Sync Rule](#sync-rule)
      - [Engagement Rule](#engagement-rule)
  - [Change-Management](#change-management)
    - [Change Lifecycle](#change-lifecycle)
      - [Lifecycle Flow Reads](#lifecycle-flow-reads)
      - [Plan](#plan)
        - [Intent](#intent)
        - [Context](#context)
        - [Unresolved](#unresolved)
      - [Build](#build)
        - [Build Lock](#build-lock)
        - [Log](#log)
      - [Conclude](#conclude)
        - [Archiving](#archiving)
      - [Companion Folder](#companion-folder)
      - [Caps](#caps)
    - [Change Style](#change-style)
      - [Trivial](#trivial)
      - [Vibe](#vibe)
        - [Bounds](#bounds)
      - [Emergent](#emergent)
        - [Focus](#focus)
      - [Formal](#formal)
        - [Change Specification](#change-specification)
        - [Implementation Plan](#implementation-plan)
        - [Formal Build](#formal-build)
        - [Formal Conclude](#formal-conclude)
    - [Versioning](#versioning)
    - [Discussion](#discussion)
      - [Discussion Records](#discussion-records)
      - [Discussion Conclude](#discussion-conclude)
    - [Startup Scan](#startup-scan)
    - [Bootstrapping](#bootstrapping)
    - [Gates and Permissions](#gates-and-permissions)
      - [Approval](#approval)
        - [Drafts](#drafts)
    - [Keywords](#keywords)
      - [Process Keyword](#process-keyword)
      - [Aside Keyword](#aside-keyword)
      - [Pause Keyword](#pause-keyword)
    - [Thought Management](#thought-management)
  - [Maintenance](#maintenance)
    - [Map Review](#map-review)
      - [Tidy](#tidy)
      - [Shape](#shape)
      - [Consistency](#consistency)
      - [Rendering](#rendering)
    - [Backlog Review](#backlog-review)
    - [Sign-off](#sign-off)
      - [Approver](#approver)
  - [Tooling](#tooling)
  - [Standards](#standards)


# Principles

[↑ NDD](#ndd) \
[Three Deaths](#three-deaths) \
[Comprehension is an Activity](#comprehension-is-an-activity) \
[Intent Memory](#intent-memory) \
[Enjoyment](#enjoyment) \
[Local Sufficiency](#local-sufficiency) \
[Cross-Agent Falsifiability](#cross-agent-falsifiability) \
[Orient Then Focus](#orient-then-focus)

```yaml
id: p4c
```

The method's founding case, in three moves.

- **What broke.** Agent-augmented development split writing code from understanding it: production no longer carries comprehension along.

- **What the method does.** It restores a deliberate comprehension-building activity, maintaining the map, and passes rendering to the agent.

- **What follows.** Working at the structural level, the map surfaces logic bugs, wrong flows, missing cases, bad boundaries, before any code is written, and conceptual maintainability earns first-class standing alongside correctness.

The principles below are the binding constraints every change answers to, and the home other nodes point at instead of restating a reason.


# Three Deaths

[↑ Principles](#principles)

```yaml
id: d3t
```

The three deaths the method's name refers to, each a way understanding is lost once agents write the code.

- **Specifications die** as documents when they sit off the critical path — unread, unmaintained, drifting into fiction.

- **Structural thinking dies** when the human no longer authors the codebase and the agent's output has nowhere to be reasoned about.

- **Comprehension dies** when the developer's role stops being architecturally fun, because understanding is sustained by engagement, not discipline.


# Comprehension is an Activity

[↑ Principles](#principles)

```yaml
id: c8a
```

No artifact substitutes for the activity of structural thinking itself. Reading a spec doesn't build the model; maintaining the map does — the deliberate construction that keeps the user's structural grasp growing as fast as agents produce code.


# Intent Memory

[↑ Principles](#principles)

```yaml
id: q3v
```

Code records what a system does, never why it is shaped that way. The reasoning behind a boundary or a trade-off lives in the author's head and leaves when they do. The map is where intent is remembered — prose that carries the why, so a decision survives past the moment and the person that made it.


# Enjoyment

[↑ Principles](#principles)

```yaml
id: j2e
```

Structural thinking must stay enjoyable — it's the part strong practitioners value, and a process that reduces the user to reviewing agent diffs destroys engagement. Engagement, not discipline, is what sustains comprehension over time: you keep understanding a system because staying in the structural thinking is rewarding, not by willpower. Enjoyment is a binding constraint, not a bonus.

Its corollary is **artifact economy**: every word in a change document or map node competes for the reader's attention, so bloat and duplication turn a dialogic activity with the agent into a wading exercise.


# Local Sufficiency

[↑ Principles](#principles) \
[Trees over Graphs](#trees-over-graphs)

```yaml
id: s3l
```

Reasoning about one part must not require holding the rest in mind — the mind registering that working memory suffices is what makes a system feel manageable. Cross-cutting concerns are the enemy: when one fact has consequences everywhere, no local model is ever enough. The cure is to promote each into a first-class named object, referenced locally rather than left implicit.


# Trees over Graphs

[↑ Local Sufficiency](#local-sufficiency)

```yaml
id: g6t
```

A tree delivers local sufficiency for free: every node has one parent, one home, one context. Real domains have cross-cutting relations, but those are references between nodes, not extra parent edges — and complex internal behaviour (cycles, fan-out, retries) lives *inside* a node, not between them. The "peak tree", where a system's shape feels like a clean logical tree, is a real cognitive state; agents produce graph-shaped code from day one and skip past it, so the map preserves it deliberately.


# Cross-Agent Falsifiability

[↑ Principles](#principles)

```yaml
id: f9x
```

If the map is the source of truth, independent agents can render it — and differences between renderings test its quality. A good map renders consistently where it matters; a bad one doesn't, exposing abstraction leaks and model-vs-reality drift without the user reading code.

Full cross-rendering is expensive, kept for high-stakes moments. Its everyday forms are two [Maintenance](#maintenance) checks. The **ambiguity test** asks whether a fresh agent could build a node without guessing, and [Consistency](#consistency) applies it from the map side. [Rendering](#rendering) tests the one rendering that exists against the map from the code side.


# Orient Then Focus

[↑ Principles](#principles)

```yaml
id: r5i
approvals:
  tearne: {at: 2026-10-26, hash: be13ae7a}
```

**Attention dies under overwhelm.** So whenever the agent has a set to present — a worklist, open changes, map nodes to edit — it first summarises the whole set, then works through it one item at a time, holding the rest itself.

The whole set at once is more than anyone can hold, and item-by-item alone leaves the user unsure where they are; together they keep the user oriented and the agent from outpacing them. Each item is introduced by name and its place in the set, such as *3 of 7*, and a message asks at most one question, ending where it asks it.

The focused items are where comprehension is built; skip them and the user is reduced to approving map diffs instead of code diffs — a better abstraction, but still passive review.

**See also**

- [Engagement Rule](#engagement-rule) — the map-edit instance: nodes named up front, then settled one by one.
- [Enjoyment](#enjoyment) — attention lost to overwhelm is how comprehension stops being sustained by engagement.
- [Thought Management](#thought-management) — the practice that keeps the user's place when a thought interrupts the item in hand.


# Map

[↑ NDD](#ndd) \
[Node](#node) \
[Map Structure](#map-structure) \
[Node Sizing](#node-sizing) \
[Writing Style](#writing-style) \
[Edit Governance](#edit-governance)

```yaml
id: sp1
approvals:
  tearne: {at: 2026-10-07, hash: 531a6b23}
```

The map is the developer's conceptual model of the system. NDD assumes that any specification can be effectively expressed as a map, holding the system's design as a tree of concepts, structured the way the user thinks rather than how code is organised. Agents render it into code. Everything else in the method — how it changes, how it's viewed — serves this map.

**See also**

- [Comprehension is an Activity](#comprehension-is-an-activity) — maintaining the map is the comprehension-building activity this node's primacy serves.


# Node

[↑ Map](#map) \
[Node Identity](#node-identity) \
[Navigation Links](#navigation-links) \
[Node Sections](#node-sections) \
[Approval Stamp](#approval-stamp)

```yaml
id: nd1
```

A node represents **one** concept and includes a heading, name-anchored navigation links to its parent and children, an agent-maintained scaffolding block holding its metadata, and terse prose leading with the mental picture. Optional *Detail* and *See also* sections follow.

The format is a strict superset of a plain-markdown section — strip the scaffolding and links and what remains is an ordinary heading with prose, so a map renders and navigates as plain markdown in any tool.

**See also**

- [Trees over Graphs](#trees-over-graphs) — nodes form the tree; a concept's complexity is kept inside its node rather than spread across links.


# Node Identity

[↑ Node](#node)

```yaml
id: w9c
approvals:
  tearne: {at: 2026-10-26, hash: 6c2ed09f}
```

A node's name can change; its identity can't. A small immutable token in the yaml scaffolding block survives node renames and moves. [Navigation](#navigation-links) never uses it, nor does agent output — references name the heading, so the id can be meaningless.

**Detail**

The **scaffolding block** is fenced YAML directly under the navigation links containing the `id` and any [approval stamps](#approval-stamp). It's agent-maintained. The `id:` key is map-unique, lowercase alphanumeric, three or more characters (e.g. `k7f`) - a token rather than a readable slug to avoid edit or link temptation. A user may hand-draft a node without a block; [Tidy](#tidy) adds the block and reports it, so identity is never silently missing.


# Navigation Links

[↑ Node](#node)

```yaml
id: b3q
approvals:
  tearne: {at: 2026-10-26, hash: 2d48a853}
```

The tree is defined by its links. Each node names its parent and each child. Siblings aren't listed directly.

> [!IMPORTANT] Links resolve by node name, so ordinary markdown tooling navigates them.

**Detail**

The parent link comes first, its text the target's name prefixed with `↑`; only the map's root has none. Child link text is the target node's actual name. Each line but the last ends with ` \`, so the block renders one link per line. A user may omit links while drafting; [Tidy](#tidy) adds them and reports it.

Child order belongs to the parent, in natural reading order.

Because links resolve by name, renaming a node means re-pointing the links that named it, and every heading must be unambiguous within its [map file](#map-files); a link into another file carries that file's path, so it resolves from where it sits.

**See also**

- [Trees over Graphs](#trees-over-graphs) — links encode the one-parent tree that keeps navigation walkable.


# Node Sections

[↑ Node](#node) \
[Callouts](#callouts)

```yaml
id: s8r
```

The main user-facing parts of a node are each optional and include, in a fixed order: **prose**, **Callouts**, **Detail**, and **See also**. Prose is the mental picture and usually the only part the user must read, but even it can be dropped — a node may carry only *Detail*, for instance. A node using none of these is just a heading: an ordinary markdown section.

**Detail**

*Callouts* flag a load-bearing point and get their own child node. *Detail* is marked with bold `**Detail**` and holds implementation-level precision the user can stop before, such as parameters, thresholds, and algorithms. *See also* is marked with bold `**See also**` and lists cross-cutting references that aren't parent or child, each saying why the relationship matters.


# Callouts

[↑ Node Sections](#node-sections)

```yaml
id: c5k
```

A callout is a "don't skim this" flag on a point the prose already makes. It marks the load-bearing moments where skimming would lose the reader, such as a design trade-off, a non-obvious assumption, or a constraint that shapes the whole node.

**Detail**

Rendered as a `> [!IMPORTANT]` blockquote, never as a highlighter for every notable fact.


# Approval Stamp

[↑ Node](#node) \
[Fingerprint](#fingerprint)

```yaml
id: p8m
approvals:
  tearne: {at: 2026-09-13, hash: 69e508f0}
```

An approval stamp records that one person approved one node. Stamps live in the node's scaffolding block under an `approvals:` mapping keyed by a name or handle, so each person holds exactly one and a re-approval overwrites it. Because they are in the node rather than a separate ledger, they follow it through renames and moves. A node without the mapping is simply unapproved, and most maps never gain one.

**Detail**

Each value holds `at`, an ISO 8601 date, and `hash`, the [fingerprint](#fingerprint) of the text approved. Drift uses only the hash; the date says when, and the hash finds the version a person saw. Quote the key if it contains a colon or starts with punctuation.

```yaml
id: w9c
approvals:
  alice: {at: 2026-09-10, hash: 3f9a1c2e}
  bob: {at: 2026-08-02, hash: 8d02b7e4}
```

**See also**

- [Sign-off](#sign-off) — the check that reads the stamps.
- [Node Identity](#node-identity) — the other thing the scaffolding block holds.


# Fingerprint

[↑ Approval Stamp](#approval-stamp) \
[Fingerprint Helper](#fingerprint-helper)

```yaml
id: h4q
```

A fingerprint is a hash of what a reader sees in a node. It covers the heading, prose, callouts, *Detail* and *See also*; it excludes the scaffolding block and navigation links.

Comparing fingerprints is a test of equality: a node put back to earlier text regains its old fingerprint, and so clears for whoever approved that text.

**Detail**

Take the node from its heading line to the line before the next heading. Drop the scaffolding block and the navigation-link lines whole; inline links in the prose stay as written, markdown included. Remove every whitespace character. The fingerprint is the first eight hex digits of the SHA-256 of that UTF-8 string. An agent computes it with the shipped `util/fingerprint.py`, never by reasoning; [Fingerprint Check](testing.map.md#fingerprint-check) is the reference that pins the rule.


# Fingerprint Helper

[↑ Fingerprint](#fingerprint)

```yaml
id: u6h
```

`util/fingerprint.py` is the script an agent runs to compute node fingerprints: to write an [approval stamp](#approval-stamp), and at [Sign-off](#sign-off) to find what is due.

- Given a map file it prints every node's fingerprint beside its name.
- Given a node name it prints that one fingerprint alone.
- With `--due` and a person's name it reads the stamps and prints the nodes due for them, in map order.

It reads only; stamps are still written by the agent.

**Detail**

Example usage:

```
ndd/util/fingerprint.py map.md
ndd/util/fingerprint.py map.md "Node Name"
ndd/util/fingerprint.py map.md --due "Alice Smith"
```

A [POS-style](standards/POS.md) script run with `uv`, one map file at a time, so a map in several files takes one run per file. A name with spaces is quoted on the command line only.


# Map Structure

[↑ Map](#map) \
[Map Files](#map-files)

```yaml
id: m6x
approvals:
  tearne: {at: 2026-10-26, hash: f98b856b}
```

The map's shape is shown at a glance by a **tree overview**: a nested list of links, one per node, in a *Contents* node that is the first child of each [map file](#map-files)'s top node. Nodes not yet written are marked `(TODO)`, so the intended shape shows before the content does. The overview is only a convenience: the real tree is the navigation links, and [Tidy](#tidy) keeps the two in step.

**Detail**

The root defaults to the project's name, preferring a term that carries domain information over a generic label like "Application". When that name clashes with a prominent internal node, disambiguate with whichever reads best: a scoping term for the root, a suffix, a parenthetical, or a more specific name for the internal node.

**See also**

- [Trees over Graphs](#trees-over-graphs) — why the shape is a tree, not a general graph.


# Map Files

[↑ Map Structure](#map-structure)

```yaml
id: k2v
```

A project has one map; a file is only where a branch of it lives. The entry point is `map.md` in the project root, the one file whose top node has no parent link. Any node's children may live beside or beneath it in a file with a name related to the node, with the extension `.map.md`: a *Testing* node's branch would likely be `testing.map.md`. The hanging node's child links point into that file and the branch's top node keeps a parent link back, so the tree is still read by following links, and the hanging node's prose explains the branch's scope.

A branch is split out for size, or for a conceptual boundary worth seeing in the file list.

**Detail**

A file's *Contents* lists the nodes in that file; a branch that continues in another file is linked into it and the list stops there.

**See also**

- [Navigation Links](#navigation-links) — the links that carry the tree, within a file and across.


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


# Writing Style

[↑ Map](#map) \
[Conceptual Writing](#conceptual-writing) \
[Formatting](#formatting) \
[Economy](#economy)

```yaml
id: p4h
```

How map prose is written, so nodes stay readable and durable. Three sides:

- Conceptual Writing: what the prose *says*

- Formatting: how it's typeset

- Economy: how much it says


# Conceptual Writing

[↑ Writing Style](#writing-style)

```yaml
id: h3v
approvals:
  tearne: {at: 2026-09-13, hash: e9c897d0}
```

A handful of habits shape how a node reads, and one trap to avoid:

- **Write about the referent, not the node** — make the real subject do something: "The installer script is run from the client's project", not "The script that a client runs".

- **Lead with the mental picture** before any implementation detail.

- **Name the boxes before explaining them** — say "there are three mechanisms" and then give each its own node or bullet point.

- **Flow sentences unbroken** — prefer keeping a sentence whole over interrupting it. A parenthetical em-dash pair reads fine when the aside is one short clause, but once the middle grows long and multi-part the reader loses the opening before the sentence resumes: split it into separate sentences instead.

- **Bullet a set the reader will scan** — when a node names a small set of parts, options, or questions, list them as bullets rather than an in-sentence enumeration, so each is scannable and individually referenceable.

- Don't **couple to code structure**: prose may name a technical concept when load-bearing, but the map tracks the user's model, not the code's shape — so it shouldn't break when code is refactored.


# Formatting

[↑ Writing Style](#writing-style)

```yaml
id: f2n
approvals:
  tearne: {at: 2026-09-13, hash: 2f20a597}
```

Typographic conventions for map prose.

- Write each paragraph as one continuous line with no hard wraps, so it reflows under soft-wrap.

- Separate bullet points with a blank line when they run long enough to wrap; short single-line points don't need it.

- Two blank lines before a node title, so node boundaries stand out when scrolling a single-file map.

- Use *italics* when a sentence refers to a named section or element (*Callouts*, *Detail*, *See also*), and reserve **bold** for introducing a term of art on first use, so references don't read as competing sub-headings.

- Prefer an inline cross-reference link when a sentence already names another node in passing; reserve a *See also* entry for a standalone pointer the prose doesn't already invoke, each with its own reason it matters.


# Economy

[↑ Writing Style](#writing-style)

```yaml
id: e2c
approvals:
  tearne: {at: 2026-10-26, hash: 98082826}
```

A node says each thing once, and nothing the reader already has. The ways it fails, most often:

- A sentence restating its neighbour.

- A *See also* entry repeating the prose or its target, where an inline link would do.

- Provenance, such as what came first or why it was chosen, which belongs in the change record.

- An example the linked node already gives.

- Flourish.

Across nodes the same holds: a fact touching several nodes has one owner, and the rest link to it. Which node owns it is the map's own choice; one workable convention is that a concept owns its facts, and a procedure lists its steps as links. Where a link holds a step's detail, the wording says so, as in "as [Pause Keyword](#pause-keyword) directs", so the reader knows to follow it.

**See also**

- [Enjoyment](#enjoyment) — artifact economy: why every word competes for the reader's attention.


# Edit Governance

[↑ Map](#map) \
[Sync Rule](#sync-rule) \
[Engagement Rule](#engagement-rule)

```yaml
id: e7m
```

The rules for changing the artefact itself. Three questions govern every edit:

- *what* may be written — the [Sync Rule](#sync-rule);

- *how* the change is made — the [Engagement Rule](#engagement-rule);

- *when* a node is due for work — [Maintenance](#maintenance).

Because these edits describe reality rather than intent, they fall outside the active-change requirement — the **map exemption**: no open change is needed, and they may happen at any time. That exemption lifts only the active-change constraint; the [Engagement Rule](#engagement-rule)'s per-node negotiation for map updates still applies.

**See also**

- [Gates and Permissions](#gates-and-permissions) — the active-change requirement this exemption stands against.


# Sync Rule

[↑ Edit Governance](#edit-governance)

```yaml
id: s5y
```

The map describes what exists, never what is planned: an edit describing work not yet built waits until the work is built.


# Engagement Rule

[↑ Edit Governance](#edit-governance)

```yaml
id: n3g
approvals:
  tearne: {at: 2026-10-26, hash: 97fa4876}
```

[Orient Then Focus](#orient-then-focus) applied to the map. Nodes are
1. drafted,
2. surfaced with [character count](#node-sizing), plus a diff for an edit,
3. written as [Drafts](#drafts) directs, and
4. treated as settled only once the reply is [approval](#approval), which [stamps](#sign-off) the node where the map carries stamps.

No edit is silent or made in bulk. Corrections that change no meaning — a typo, spacing, a stale link — are applied and reported rather than surfaced, but only if every item in hand is one.

The rule binds the agent, not the user, who edits the map freely and unannounced. Their edit needs no approval, but the agent is expected to review it in one pass: running [Tidy](#tidy) over it as it directs, commenting on anything it would question, and logging it only if it changes what the build must do.


# Change-Management

[↑ NDD](#ndd) \
[Change Lifecycle](#change-lifecycle) \
[Change Style](#change-style) \
[Versioning](#versioning) \
[Discussion](#discussion) \
[Startup Scan](#startup-scan) \
[Bootstrapping](#bootstrapping) \
[Gates and Permissions](#gates-and-permissions) \
[Keywords](#keywords) \
[Thought Management](#thought-management)

```yaml
id: cm4
approvals:
  tearne: {at: 2026-10-22, hash: 0dba9d9f}
```

How the project evolves, its map and code alike: through changes, each drafted in `changes/open/`, taken through its [lifecycle](#change-lifecycle), then archived to `changes/archive/` under a date prefix. Beside them, `changes/open/active.md` holds the build lock and `changes/resume.md` any [pause](#pause-keyword) entries.

**Detail**

A change's file name is its title in two to five hyphenated words, optionally behind a leading number that helps sequence the queue. Neither is an identity: rename an open change freely as it evolves, repointing `active.md` if it names it.


# Change Lifecycle

[↑ Change-Management](#change-management) \
[Lifecycle Flow Reads](#lifecycle-flow-reads) \
[Plan](#plan) \
[Build](#build) \
[Conclude](#conclude) \
[Companion Folder](#companion-folder) \
[Caps](#caps)

```yaml
id: l5g
approvals:
  tearne: {at: 2026-10-26, hash: a09ed9b7}
```

A change is a single markdown document that advances through three phases:

1. **[Plan](#plan)** — producing the change document, in the shape its [Change Style](#change-style) sets.
2. **[Build](#build)** — doing the work against the Plan, the same whichever style made it.
3. **[Conclude](#conclude)** — a retrospective once the work is accepted.

Each phase is surfaced for the user's explicit approval before the next begins.

The document is the single carrier of state: where a change sits is read from what it contains, not from any status field. A part reaches the document once [approved](#approval), or sooner if the user asks for the draft in place.

The Plan → Build boundary is the load-bearing gate: the change's own work waits for an approved plan, apart from the [map exemption](#edit-governance).


# Lifecycle Flow Reads

[↑ Change Lifecycle](#change-lifecycle)

```yaml
id: l9t
approvals:
  tearne: {at: 2026-10-22, hash: fe163e61}
```

At each move between lifecycle stages the agent first reads the governing map node: the [Discussion](#discussion) node when a discussion is to become a change, the next plan part's node before drafting it, the [Conclude](#conclude) node when the user confirms the build is done, and the [Archiving](#archiving) node when a Conclude is approved. These **flow reads** keep the method's shape live in the agent's attention; they are distinct from the **reasoning reads** done only when a rule's rationale is in doubt.


# Plan

[↑ Change Lifecycle](#change-lifecycle) \
[Intent](#intent) \
[Context](#context) \
[Unresolved](#unresolved)

```yaml
id: v3d
approvals:
  tearne: {at: 2026-10-26, hash: 15d534c5}
```

The plan builds up in **parts**, each drafted then surfaced for approval before the next. Every plan starts with the [Intent](#intent); the parts that follow are set by its [Change Style](#change-style).

What may be written meanwhile is set by [Gates and Permissions](#gates-and-permissions). Two further sections sit outside the parts sequence, ungated: [Context](#context), which explains why the change exists, and [Unresolved](#unresolved), which holds what the plan has yet to settle.

A Plan need not be fully formed to exist. A change may sit at any degree of formation — from an [Intent](#intent)-only draft just parked via [aside](#aside-keyword), up to a completed preparation section awaiting approval.


# Intent

[↑ Plan](#plan)

```yaml
id: i8b
approvals:
  tearne: {at: 2026-10-22, hash: 30406eab}
```

The opening part: what the change must achieve, in domain language, stated so the user can approve it. Not how it will be delivered unless relevant to the requirement, and not why it is needed: every *why* — history, provenance, the reasoning that led here — belongs in [Context](#context). Kept brief and requiring user approval before anything else proceeds. For a [Trivial](#trivial) change the Intent is the whole plan.

Its prose has a [cap](#caps), so the opening scans in seconds. Once the change's preparation section — [Bounds](#bounds), [Focus](#focus), or [Change Specification](#change-specification) — is approved, the agent re-reads the Intent and cuts whatever it now carries, surfacing the trimmed Intent with its count. Trivial changes have no preparation section and no trim step.


# Context

[↑ Plan](#plan)

```yaml
id: c7d
approvals:
  tearne: {at: 2026-10-26, hash: 7c90e111}
```

An optional section of the change document, sitting under the [Intent](#intent): the history, provenance and prior attempts a reader needs to make sense of why the change exists. Keeping it here is what lets the Intent stay one quick paragraph.

Context is written to last and travels to the archive with the change, unlike [Unresolved](#unresolved), which is emptied before Build.

Keep it to the least that lets a later reader rediscover the full detail for themselves: enough flavour and pointers to pick the trail back up, never a retelling.


# Unresolved

[↑ Plan](#plan)

```yaml
id: n8u
approvals:
  tearne: {at: 2026-10-26, hash: d6de2a7c}
```

A section at the foot of the change document listing what the plan has yet to settle: open items the agent cannot settle alone, and on-topic material that arrived before its part, such as a scope note during the [Intent](#intent). Writing an item down on arrival costs nothing and survives a lost session.

Opening each part, the agent moves into it whatever now belongs; the part is ready for approval only once none of its items remain. Items are settled [one at a time](#orient-then-focus): folded into a part, parked as a change of their own, or discarded if the user chooses. Resolving one can send the plan back to an earlier part. The section is empty before the plan goes up for approval, so uncertainty shapes the change rather than waiting beside it.

**Detail**

An empty section is deleted; its absence is the signal that the plan is ready.


# Build

[↑ Change Lifecycle](#change-lifecycle) \
[Build Lock](#build-lock) \
[Log](#log)

```yaml
id: u6k
approvals:
  tearne: {at: 2026-10-26, hash: ee9b3f1a}
```

The agent executes the plan against the real project files rather than changing it mid-flight, posting concise updates. It interrupts only when something warrants it — a planned pause, surprise, ambiguity, an error in the plan, or a task that [edits the map](#engagement-rule).

Only one change builds at a time, held by the [build lock](#build-lock), and its progress is kept in the [Log](#log).

**Detail**

A [versioned](#versioning) project agrees a bump kind on build start and sets a dev version at each hand-back for testing.

The change can be returned to planning for rewriting any time the user chooses.


# Build Lock

[↑ Build](#build)

```yaml
id: b7n
approvals:
  tearne: {at: 2026-10-26, hash: 804ffd4f}
```

What keeps one change building at a time. [Build](#build) begins only on the user's approval of the plan; on that approval the agent takes the lock by writing the change file name into `changes/open/active.md`, reporting success — or, if the file already exists, stopping without touching it, since another change is already mid-build.

Releasing the lock deletes the file. A build that changed code keeps the lock even when handed back to planning; only an untouched one may release it, so unfinished work is never silently abandoned.

At the [Startup Scan](#startup-scan), a lock on a change whose work is unfinished marks an interrupted build: the agent reads the change's [Log](#log) to recover context rather than restarting. A Log recording a return to planning means the change is planning, though it still holds the lock.


# Log

[↑ Build](#build)

```yaml
id: g2l
approvals:
  tearne: {at: 2026-10-26, hash: 63a3f7e4}
```

A running record at the foot of the change document, kept during [Build](#build) so a resuming session can see how far the build got. The agent writes a terse line for each plan item as it settles, without asking, and records the unexpected: surprises, deviations, blockers, partial progress.

Any items put to one side during Build are logged as open and must be resolved before [Concluding](#conclude): each folded into the build, parked as a change of its own, or discarded if the user chooses. Nothing open is carried past Build.


# Conclude

[↑ Change Lifecycle](#change-lifecycle) \
[Archiving](#archiving)

```yaml
id: o4j
approvals:
  tearne: {at: 2026-10-26, hash: 6419b68c}
```

The closing note, written only once the user confirms the build is done. It records the delta from the plan — deviations, surprises, documents touched — not a summary of what the plan already said.

Open items in the [Log](#log) are resolved before Conclude begins, as it directs.

When there's nothing to add, "Completed." is enough. Conclude has a [cap](#caps).

Its mere presence is the marker that the change is finished.

**See also**

- [Enjoyment](#enjoyment) — artifact economy: why Conclude is capped short and never re-tells the journey.


# Archiving

[↑ Conclude](#conclude)

```yaml
id: a9v
approvals:
  tearne: {at: 2026-10-22, hash: 44491f2f}
```

Archiving closes a change once its [Conclude](#conclude) note is approved. Its steps, in order:

1. Add the change's entry to the changelog, if the project is [versioned](#versioning).
2. Run [Tidy](#tidy) across the map.
3. Move the change from `changes/open/` to `changes/archive/`, dropping any leading number and adding the ISO date it concluded, so `140-config-file-format.md` becomes `2026-05-14-config-file-format.md`. Its [companion folder](#companion-folder) goes with it.
4. Release the [build lock](#build-lock).
5. Review any pause entries in `changes/resume.md`, as [Pause Keyword](#pause-keyword) directs.
6. Ask what next: a [Map Review](#map-review), the project's release steps if its map defines any, or something else.


# Companion Folder

[↑ Change Lifecycle](#change-lifecycle)

```yaml
id: c2f
approvals:
  tearne: {at: 2026-10-26, hash: c2a58f17}
```

A folder beside a change document in `changes/open/`, named to match it, holding supporting material that would crowd the document, such as evidence, experiments, or the map copy on which a [Formal](#formal) change drafts its specification. A change of any style may have one, created only when warranted. At [Archiving](#archiving) a retain-or-drop review keeps useful evidence and rationale and drops disposable experiments; the folder then moves with the change, renamed to match, or is removed if nothing is retained.


# Caps

[↑ Change Lifecycle](#change-lifecycle)

```yaml
id: c5p
approvals:
  tearne: {at: 2026-10-26, hash: 1d26b720}
```

Some parts of a change or discussion carry a cap, listed below, to keep them quick to read. Every cap is soft. The agent counts a capped text as [Node Sizing](#node-sizing) does, each time it surfaces it, and reports the number; past the cap it asks the user to adjudicate rather than trimming silently or presenting the text as final. For [Bounds](#bounds) or [Focus](#focus), an overrun also suggests another [Change Style](#change-style) fits better.

| Text | Cap |
|------|-----|
| [Intent](#intent) | ~500, *Context* excluded |
| [Bounds](#bounds) | ~200 |
| [Focus](#focus) | ~300 |
| [Change Specification](#change-specification) | each node per [Node Sizing](#node-sizing) |
| [Implementation Plan](#implementation-plan) | each node per [Node Sizing](#node-sizing) if map-shaped, else its own convention |
| [Conclude](#conclude) | ~500, a changelog entry excluded |
| [Discussion Conclude](#discussion-conclude) | ~500 |


# Discussion

[↑ Change-Management](#change-management) \
[Discussion Records](#discussion-records) \
[Discussion Conclude](#discussion-conclude)

```yaml
id: q7p
approvals:
  tearne: {at: 2026-09-29, hash: 533c26a0}
```

A durable home for unfinished thinking that precedes an [Intent](#intent). A discussion begins with a provisional title and a thought; threads can change without losing ideas or return points, and partial thinking can inform related concepts without becoming commitments. It runs alongside changes but has no plan parts, no [build lock](#build-lock), and produces zero or more [parked changes](#plan) when a candidate inside it is [promoted at Conclude](#discussion-conclude). The user owns the concepts; the agent maintains the [record](#discussion-records).


# Discussion Records

[↑ Discussion](#discussion)

```yaml
id: r7b
approvals:
  tearne: {at: 2026-10-18, hash: 65003849}
```

The record itself. Kept concise, in whatever prose shape fits the topic — agreements with their essential reasoning, open questions, options and links to related work. The agent prunes and rewrites the record freely to reflect current thinking, outside the [Engagement Rule](#engagement-rule): Discussion edits are not drafted-surfaced-settled or counted. Git history holds the deep archive, and past reasoning is retained only where its loss would risk revisiting a dead-end or where an idea is worth flagging for later resurfacing.

On a [pause](#pause-keyword) the agent leaves a **Resume** anchor with return points and a pointer to current thinking; the anchor is trimmed on resumption. The agent flags meaningful connections and discusses uncertain or consequential relationships before settling them.


# Discussion Conclude

[↑ Discussion](#discussion)

```yaml
id: d9k
approvals:
  tearne: {at: 2026-10-26, hash: 127cbc1d}
```

The closing note for a discussion, proposed by either party: the agent when the discussion looks near its end, the user when they say so. Within its [cap](#caps), it states what the discussion produced — understanding, decisions, promoted candidates linked to their new [parked changes](#plan) — what was dropped, and any ideas worth resurfacing later. The user approves before archiving.

First the agent reviews anything in the record that could become its own change; the user promotes each to a parked change (Intent only) or drops it, and none is left hanging.

On approval the file, a readable slug ending `-discussion.md`, is prefixed with the ISO date and moved to `changes/archive/`, its links updated.


# Change Style

[↑ Change-Management](#change-management) \
[Trivial](#trivial) \
[Vibe](#vibe) \
[Emergent](#emergent) \
[Formal](#formal)

```yaml
id: e3n
approvals:
  tearne: {at: 2026-10-22, hash: 8eb92b8d}
```

Each change is worked in one of four styles, each giving the [Plan](#plan) its own shape after [Intent](#intent). [Build](#build) and [Conclude](#conclude) are the same whichever is chosen. The agent proposes a style once Intent is approved — default **Formal** — and the user confirms. The chosen style is recorded as a `**Change Style:** <name>` line beneath the change's title, before the Intent.

| Style | Preparation before Build |
|-------|--------------------------|
| **Trivial** | none — Intent is the whole plan |
| **Vibe** | [Bounds](#bounds) |
| **Emergent** | [Focus](#focus) |
| **Formal** | [Change Specification](#change-specification) and optional [Implementation Plan](#implementation-plan) |

The four are not a ladder: the agent proposes the style whose shape fits, not the lightest that might do. Style may be revisited if the change turns out to want a different shape, in which case the agent returns to planning.


# Trivial

[↑ Change Style](#change-style)

```yaml
id: t0v
approvals:
  tearne: {at: 2026-10-22, hash: d1e60a67}
```

Uses [Intent](#intent) only — the whole plan. The lightest of the four styles. Chosen when a change has virtually no substantive ambiguity — the domain outcome is clear, and the agent finds no decision along the way that would reasonably need surfacing for approval. During [Build](#build) the agent verifies proportionately to what is being changed and reports results; anything consequential that emerges is surfaced rather than absorbed silently.


# Vibe

[↑ Change Style](#change-style) \
[Bounds](#bounds)

```yaml
id: v2m
approvals:
  tearne: {at: 2026-10-22, hash: 4d35bbc8}
```

Uses [Intent](#intent) and a light [Bounds](#bounds) section. Chosen when the user opts to let the agent decide the shape of the work as it goes; the safeguard is the agent's judgement about when to escalate, not an upfront specification. For example, stakes may be low enough that tighter specification isn't worth the effort. Bounds is kept brief on purpose — a short shared understanding of anything context-specific worth naming, and nothing more. Wordy Bounds would drain the very attention Vibe was chosen to save.

During [Build](#build) the agent works within the agreed envelope and escalates on its own judgement when something turns up that Bounds could not have anticipated.


# Bounds

[↑ Vibe](#vibe)

```yaml
id: b3n
approvals:
  tearne: {at: 2026-10-22, hash: fdd6b4a5}
```

The preparation section for a [Vibe](#vibe) change: a brief shared understanding, agreed after [Intent](#intent), of anything context-specific worth naming before [Build](#build) begins. The agent proposes Bounds. The safeguard is the agent's judgement to escalate when the stakes rise, not an attempt to enumerate every case.

Bounds are context-dependent — a hard constraint, a performance sensitive piece of adjacent code, a checkpoint the user wants surfaced, or a specific decision to reserve.

Bounds has a [cap](#caps).


# Emergent

[↑ Change Style](#change-style) \
[Focus](#focus)

```yaml
id: e5x
approvals:
  tearne: {at: 2026-10-15, hash: 089de978}
```

Uses [Intent](#intent) and [Focus](#focus) sections. Chosen when what the change should produce is best found by doing the work step by step, each step informing the next, rather than specified first. Focus names the work pursued; there is no worklist or done-when, because knowing when to close is part of the work.

Emergent is real-time collaboration on a moving target: user and agent shape the work together, adjusting as understanding shifts. [Build](#build) delivers within the change as the work emerges, each map edit under the [Engagement Rule](#engagement-rule). An artefact, understanding, a decision, or a handoff to a further change is each a complete outcome.


# Focus

[↑ Emergent](#emergent)

```yaml
id: f2q
approvals:
  tearne: {at: 2026-10-22, hash: ea35d754}
```

The preparation section for an [Emergent](#emergent) change: the work being pursued. The agent proposes it; the user amends and confirms.

Focus is a lightweight artefact — a sentence or two, not a plan. The work may be something to build or a question the pair is trying to understand. Judging whether it is done is part of the work, made as it goes rather than at a set point; Focus names a checkpoint only when one is genuinely useful, such as a milestone or a time limit.

If the work shifts, Focus can be re-agreed rather than the change concluded. Focus has a [cap](#caps).


# Formal

[↑ Change Style](#change-style) \
[Change Specification](#change-specification) \
[Implementation Plan](#implementation-plan) \
[Formal Build](#formal-build) \
[Formal Conclude](#formal-conclude)

```yaml
id: f8p
approvals:
  tearne: {at: 2026-09-30, hash: 5af3bc71}
```

Uses Intent, [Change Specification](#change-specification) and optionally [Implementation Plan](#implementation-plan) sections. Chosen when it is worth agreeing what "done" looks like before [Build](#build) begins. The Change Specification captures the target — what must hold when the change lands — and Build is executed against it. When delivery choices warrant explicit agreement in their own right, an Implementation Plan follows the Change Specification; otherwise none is needed.

Formal is the default when the agent is unsure which style fits, and is particularly valuable for high-value work where drafting the map structure upfront pays back many times over.


# Change Specification

[↑ Formal](#formal)

```yaml
id: s7q
approvals:
  tearne: {at: 2026-10-17, hash: 73f49c5e}
```

The preparation section for a [Formal](#formal) change: specifying what must hold when the change lands.

The specification consists of map nodes, plus target versions of any agreed non-map assets, inline or in the [companion folder](#companion-folder) with a one-line relative path specified. When the specification will touch multiple nodes, the agent proposes a sub-map or whole-map file copy, kept in the companion folder, pausing to give opportunity to check in so diffs are effective during planning. Once built the live map must describe the completed result.

Node approval follows the normal [Engagement Rule](#engagement-rule), with approval stamps that transfer to the live map during Build. Each non-map target is surfaced as a diff and approved likewise, and questioned if it takes over the map's job of describing the system.


# Implementation Plan

[↑ Formal](#formal)

```yaml
id: ip5
approvals:
  tearne: {at: 2026-10-26, hash: 8d4aea6a}
```

An optional preparation section for a [Formal](#formal) change, added when consequential delivery choices remain after the [Change Specification](#change-specification) is agreed. Captures decisions about how to deliver — sequencing, staging, dependencies, rollback — rather than a step-by-step checklist. Omitted when the delivery path is obvious.

The agent proposes an Implementation Plan when the specification alone does not settle delivery. If added, Build follows it; deviations go to the [Log](#log), and material rework re-agrees the plan with the [Build Lock](#build-lock) kept, resuming against the revised plan — a full return to planning is reserved for abandoning Formal.


# Formal Build

[↑ Formal](#formal)

```yaml
id: fb9
approvals:
  tearne: {at: 2026-10-17, hash: 2a078af1}
```

Layered onto general [Build](#build); the Formal additions follow.

Before proposing Build, the agent reconciles the [Change Specification](#change-specification) against current reality; revisions required by intervening work return the change to spec development, as do issues uncovered during the build. Build-time re-agreement keeps the [Build Lock](#build-lock), resuming against the revised target when agreed.

Build lands non-map assets in place, matching any approved non-map targets. Last of all, approved nodes on the Change Specification target promote into the live map. Where the live map has drifted from the baseline, promotion goes per node so drift surfaces before Conclude.


# Formal Conclude

[↑ Formal](#formal)

```yaml
id: q4m
approvals:
  tearne: {at: 2026-10-26, hash: a87154e6}
```

Layered onto general [Conclude](#conclude) and [Archiving](#archiving); the Formal additions follow.

At Conclude, verification checks the [Change Specification](#change-specification) against the built result; drift on any per-node approved element triggers re-engagement of that node.

At Archiving, the retain-or-drop review drops whole-map copies in full — promoted content lives in the live map, and the copy was only a development aid, not a document to maintain.


# Versioning

[↑ Change-Management](#change-management)

```yaml
id: vr6
approvals:
  tearne: {at: 2026-10-20, hash: e298df05}
```

A versioned project keeps a changelog and uses semver. Each change carries its own version, and a release gathers several. The number moves at four moments:

- At [Build](#build) start the change claims a new version, bumped by the kind agreed then and suffixed `-dev` until release.

- Each hand-back for testing numbers the suffix, `-dev.N`, restarting per change, so the tester knows which build they are looking at.

- At [Archiving](#archiving) the changelog entry uses the final dev version, such as `## 2.3.1-dev.3`, surfaced and approved on its own; nothing earlier in the build touches the changelog.

- Release folds the dev headings into one dated heading under the latest number, without suffix, since the interim versions were never a releasable state.


# Startup Scan

[↑ Change-Management](#change-management)

```yaml
id: x7t
approvals:
  tearne: {at: 2026-10-22, hash: f34db38b}
```

First in every session, the agent reads the project's change status. It then announces the session's mode — planning, building, discussing, or a combination — reports what it found, and proposes the next step.

**Detail**

The report covers:

- Each open change, placed by lifecycle position, and each [discussion](#discussion), by topic and whether it is nearing [Conclude](#discussion-conclude). A change named in `active.md` is placed as [Build Lock](#build-lock) directs.

- In a [versioned](#versioning) project, the dev headings awaiting release.

- Each [pause](#pause-keyword) entry, with its date.

- Any [draft markers](#drafts), as unapproved.

- If no work is already in progress, an offer of a [Backlog Review](#backlog-review).

A project with no `map.md` and no `changes/` tree hasn't started; the agent [bootstraps](#bootstrapping) it instead.


# Bootstrapping

[↑ Change-Management](#change-management)

```yaml
id: b6t
approvals:
  tearne: {at: 2026-10-26, hash: 7802eb3c}
```

How a project acquires its first map. A fresh install vendors only the method under `ndd/`, so with no `map.md` and no `changes/` tree the ordinary lifecycle has nothing to stand on; the [Startup Scan](#startup-scan) spots this and offers to bootstrap.

The agent scaffolds the [`changes/` tree](#change-management) and seeds the project map, `map.md` in the project root, from discussion and any existing documentation. How much to seed is the user's call: a single root node named for the system, or a fuller sketch.

Adopting an existing codebase adds a survey: the agent reads its assets and proposes nodes one at a time per the [Engagement Rule](#engagement-rule). These edits fall under the [map exemption](#edit-governance) and need no active change, though wrapping a migration in one can keep it systematic.


# Gates and Permissions

[↑ Change-Management](#change-management) \
[Approval](#approval)

```yaml
id: g5m
```

Two rules gating what the agent may do without asking:

- **Approval** — what counts as the user saying yes.

- **Write permission** — what the agent may change at each point.

Writing is gated by phase and by an active change. During [Plan](#plan) the agent writes only inside `changes/`; project files are read-only. Writing a project file needs a change under [build](#build), recorded in `active.md`, unless the [map exemption](#edit-governance) applies. Reading anything is always allowed.

**Detail**

Git write operations — commit, push, branch, reset — always require explicit user instruction; the agent never does them on its own initiative.


# Approval

[↑ Gates and Permissions](#gates-and-permissions) \
[Drafts](#drafts)

```yaml
id: k4d
approvals:
  tearne: {at: 2026-10-18, hash: d44461c7}
```

Approval requires a clear affirmative in response to the agent asking. Silence, a tangent, or a reply that raises new questions is not approval. It only covers what was surfaced and no more: agreeing to draft prose is not approval of the prose, and what counts as surfaced is set by [Drafts](#drafts).


# Drafts

[↑ Approval](#approval)

```yaml
id: d4r
approvals:
  tearne: {at: 2026-10-26, hash: 04f8905c}
```

A draft is only the text surfaced; an action named alongside it, such as a log entry or a new file, needs its own draft. Drafts go to chat by default, or in place if the user says *write*, after which the agent stops until the user next replies, then reviews any edit they made as the [Engagement Rule](#engagement-rule) directs. A bare *write* covers one draft; only an instruction saying so covers the session. *Write* is never approval and never a cue to move on.

**Detail**

A draft written in place sits between `<!-- draft -->` and `<!-- /draft -->`, visible in the raw file and hidden when rendered, so a lost session cannot leave it reading as settled. Approval deletes the markers; declining deletes the region.

A marker quoted in code, as here, is a mention, not a marker.


# Keywords

[↑ Change-Management](#change-management) \
[Process Keyword](#process-keyword) \
[Aside Keyword](#aside-keyword) \
[Pause Keyword](#pause-keyword)

```yaml
id: k9y
approvals:
  tearne: {at: 2026-10-18, hash: feeef867}
```

Words that let the user trigger a defined action. A keyword is recognised by clear intent, not by position or punctuation:

- [process](#process-keyword) captures an observation about the method itself;
- [aside](#aside-keyword) sets a separate thought aside for later, as a parked change or in a [discussion](#discussion);
- [pause](#pause-keyword) stops the work and leaves a note for resuming.

The first two are side-actions: the agent handles them, confirms in a line, and returns to what it was doing.


# Process Keyword

[↑ Keywords](#keywords)

```yaml
id: r4c
approvals:
  tearne: {at: 2026-10-18, hash: c875d9f6}
```

A message flagged `process` records an observation about the method or the agent's conduct — friction, a suggestion, something to revisit — without acting on it. The agent appends it to `changes/process-feedback.md`, confirms in a line, and carries on with whatever was under way.

**Detail**

The entry is dated and captures the observation plus any surrounding context (phase, active change, topic) that would otherwise be lost; the agent may rephrase for later readability. The file is append-only and created with a header if absent. It lives in the repository as an ordinary versioned file — not git-ignored — so the feedback is shared between collaborators; committing it stays a user action, like any git write.


# Aside Keyword

[↑ Keywords](#keywords)

```yaml
id: y2f
approvals:
  tearne: {at: 2026-10-26, hash: 9b127ccb}
```

A message flagged `aside` parks a topic for later without breaking the current flow. The agent scans open [discussions](#discussion) and changes for overlap and routes by content: appends to an existing discussion when the aside continues that thread; else opens a new parked change with an [Intent](#intent) only if the aside is Intent-shaped; else opens a new [discussion](#discussion) record. Placement is confirmed in one line. Overlap noticed with an existing change is named in the confirmation without attaching, so the change's owner can fold it in on resumption. Material belonging to the *current* change goes to its [Unresolved](#unresolved) instead, or to its [Log](#log) during Build.


# Pause Keyword

[↑ Keywords](#keywords)

```yaml
id: p6r
approvals:
  tearne: {at: 2026-10-26, hash: 1ecbac2d}
```

When the user says `pause`, the agent adds a dated entry to `changes/resume.md` naming what was in progress, where it sits and anything unapproved, then stops. An entry is only a pointer: a discussion keeps its detail in its [*Resume* anchor](#discussion-records) and a build in its [Log](#log), while a change paused mid-planning has neither, so the entry names the part being drafted.

Resuming an entry's work by any route deletes it, and an empty file with it. Otherwise an entry stays until the user asks for its deletion, never inside a yes to something else. At [Archiving](#archiving) the agent reviews the entries one at a time, offering to delete one naming the archived change and to keep, delete or move into a change or discussion any other. The file is committed like any file.

**Detail**

*Pause*, not *park*, which names an Intent-only change.


# Thought Management

[↑ Change-Management](#change-management)

```yaml
id: t4m
approvals:
  tearne: {at: 2026-10-26, hash: 30205476}
```

The user may throw out a thought at any time, and the agent keeps the breadcrumb trail. Each thought goes to one of four places, and the agent says in a line which, asking only when unclear:
- answered now, when a line will do;
- a digression, for as long as it earns, ending by naming the item returned to;
- noted in the current change's [Unresolved](#unresolved), or its [Log](#log) during Build; or
- parked as a change or discussion of its own, as the [aside keyword](#aside-keyword) does.

While a set is in progress, every message ends with a **status line** showing the stack: the set and item, each level stepped off it, and the count of open items, if any. With nothing in progress there is no line.

**Detail**

`map edits 3 of 7` on the item; `map edits 3 of 7 > aside` while placing a stray thought; `map edits 3 of 7 · open 2` with two open items.


# Maintenance

[↑ NDD](#ndd) \
[Map Review](#map-review) \
[Backlog Review](#backlog-review) \
[Sign-off](#sign-off)

```yaml
id: t7v
approvals:
  tearne: {at: 2026-10-26, hash: e6e91eef}
```

The upkeep of the map and the backlog, put to the user as three reviews. Each is one yes-or-no at its moment, and each opens a list of findings taken one item at a time.

| Review | Reads | Moment |
|--------|-------|--------|
| [Map Review](#map-review) | The tree and the text, and before a release the ideas and the code too | Offered after an archive and before a release |
| [Backlog Review](#backlog-review) | The parked changes in `changes/open/` | Offered at the Startup Scan |
| [Sign-off](#sign-off) | The approval stamps, for a named stakeholder | On request |

Deferring upkeep for a stretch — an emergency fix, a push elsewhere — is safe because nothing is marked: each moment re-offers its review, and a release brings the full scope.


# Map Review

[↑ Maintenance](#maintenance) \
[Tidy](#tidy) \
[Shape](#shape) \
[Consistency](#consistency) \
[Rendering](#rendering)

```yaml
id: m3r
approvals:
  tearne: {at: 2026-10-22, hash: d958a19d}
```

Map Review is offered by the agent as a yes-or-no at the moments in the table below, each setting its scope.

[Tidy](#tidy) has already run and reported by then, so a yes opens the **findings list**: everything the Tidy and Map Review checks found that needs a judgement, summarised first and then considered one item at a time by [Orient Then Focus](#orient-then-focus). A finding quotes what it faults and what already covers it, so the overlap is seen rather than asserted.

Findings are not stored. A review recomputes from the map, so a deferred finding reappears next time and costs a word to dismiss again. The checks stay askable by name, as is a scope, for anyone who wants less or more than the moment offers.

| Scope | Checks | Moment |
|-------|--------|--------|
| Light | [Shape](#shape), and prose against [Writing Style](#writing-style) | Offered after an [archive](#archiving) |
| Full | Light plus [Consistency](#consistency), [Rendering](#rendering) | Offered before a release |


# Tidy

[↑ Map Review](#map-review)

```yaml
id: u8k
approvals:
  tearne: {at: 2026-10-22, hash: cc4f2516}
```

Agent-run housekeeping, run on the nodes the user has edited as soon as the agent is told or notices, before it asks anything else, and across the whole map before an [archive](#archiving). The agent needs no prompting and reports briefly every fix made and every count it took. It is restricted to [corrections](#engagement-rule), never changes of meaning; anything needing judgement is either left for a subsequent [Map Review](#map-review) or handed back to the user immediately.

It fixes and reports a [tree overview](#map-structure) out of step with the navigation links, a missing scaffolding [id](#node-identity) or [navigation link](#navigation-links), a link left behind by a rename, and an unambiguous grammatical slip. It reports the count of nodes over the [size bound](#node-sizing) that Node Sizing would flag. It reports, without removing, any [draft markers](#drafts) other than those around a draft awaiting the user.


# Shape

[↑ Map Review](#map-review)

```yaml
id: d4p
approvals:
  tearne: {at: 2026-09-13, hash: 08d1997e}
```

A check on how the map is cut: whether the tree's divisions still match how the user thinks of the system.

It looks for:

- A node carrying more ideas than its heading implies; a node the approver has [stamped](#sign-off) as it stands is not raised.

- Sibling nodes that say too little apart and should merge.

- The top-level division of the map no longer matching how the user thinks of the system.

- Child order that no longer reads as a natural sequence.


# Consistency

[↑ Map Review](#map-review)

```yaml
id: k4c
```

A check on whether the map's ideas hold together. It reads across nodes rather than within one, so it costs more than a check on one node.

It looks for:

- Two nodes that contradict each other.

- Competing concepts left untreated — two ways of seeing the same thing, neither chosen.

- Redundancy — the same thing said in two places.

- A concept in use with no definition or natural home.

- A node that fails the ambiguity test — could a fresh agent build it without guessing?

**Detail**

The ambiguity test is the everyday form of [Cross-Agent Falsifiability](#cross-agent-falsifiability): a node it flags is a map-quality gap, not an implementation problem.


# Rendering

[↑ Map Review](#map-review)

```yaml
id: r3n
```

A check on whether what exists still reads as a rendering of the map. The agent compares an agreed scope — the whole map, or one area — against the code and files, and reports each place they disagree. Each disagreement is settled one way or the other: the map corrected to what exists, or the code corrected under a change.

It looks for:

- A node describing what is no longer there.

- Something built that no node describes.

- A mechanism the map tells one way and the code another.

- A node the code could have satisfied several ways — ambiguity seen from the code side, for the map to close.

It is the single-agent form of [Cross-Agent Falsifiability](#cross-agent-falsifiability). Because it reads the code it is the costliest check, and the catch-up when map upkeep has been deferred for a while.


# Backlog Review

[↑ Maintenance](#maintenance)

```yaml
id: b7k
approvals:
  tearne: {at: 2026-10-26, hash: 2e262881}
```

Backlog Review is offered by the agent as a yes-or-no at the [Startup Scan](#startup-scan). It covers parked changes and [discussions](#discussion) in `changes/open/`, taken one at a time. A parked change is settled — kept, updated, renumbered, merged, or discarded. A discussion has its agreements, open questions, and anything that could become a change surfaced; the user chooses what to take forward.

It looks for:

- A change or discussion citing a node or change that no longer exists.
- A change the project has moved past.
- Two changes that overlap and should merge, or a change that overlaps an open discussion.
- Numbers that no longer say what should come next — the remedy is renumbering.


# Sign-off

[↑ Maintenance](#maintenance) \
[Approver](#approver)

```yaml
id: f2s
approvals:
  tearne: {at: 2026-10-26, hash: 4ecad464}
```

A stakeholder approves the map a few nodes at a time. Each node can carry an [approval stamp](#approval-stamp) per person, recording when they approved it and a [fingerprint](#fingerprint) of the text they saw. A stamp is scaffolding, written and reported rather than negotiated.

Nothing is marked when a node changes. Drift is found by comparing: a node is *due* for a person when its fingerprint no longer matches their stamp, or it has none for them. A map with no stamps shows nothing, and gains its first only when the user asks for one; from then on every approval of a node edit stamps it for the [approver](#approver).

**See also**

- [Orient Then Focus](#orient-then-focus) — due nodes are summarised, then taken one at a time.
- [Node Sizing](#node-sizing) — re-approval is a re-read of one short node, which is what keeps it humane.


# Approver

[↑ Sign-off](#sign-off)

```yaml
id: v7a
approvals:
  tearne: {at: 2026-10-22, hash: 08cd2805}
```

The approver is the person a [sign-off](#sign-off) stamp is written for, named by a handle. The agent resolves the handle the first time a stamp is needed, not at the [Startup Scan](#startup-scan), and says which handle it is using. Git's `user.name` is the handle unless the map already carries stamps and none match that name; then, or when git has no name, the agent asks rather than guessing.

The user can override the handle, for one approval or for the rest of the session, as when pairing with another person. A one-off override lasts one stamp and the handle then returns to the session default; a session override holds until changed. Whenever the handle changes, the agent names it again.


# Tooling

[↑ NDD](#ndd)

```yaml
id: g8l
```

The method needs no bespoke application — it rides generic markdown tooling. In an editor with a markdown language server (marksman, in Helix), the name-anchored [navigation links](#navigation-links) become jump-to-definition targets: `gd` walks the tree parent-to-child, and the symbol picker (Helix `Space+s`) lists every node by name for a direct jump anywhere. The format is kept deliberately plain so richer surfaces stay cheap to build on top later.


# Standards

[↑ NDD](#ndd)

```yaml
id: s9d
approvals:
  tearne: {at: 2026-10-16, hash: af27ef94}
```

Guidance for the code written by agents on user projects, distinct from the map spec that governs the *map*. NDD ships a set of **suggested** standards a project adopts, adapts, or ignores — installed as plain markdown under `ndd/standards/`, not folded into the map. This node is the index: an agent scans it to see what exists and opens only the guide a task touches. The code **Style** guide is an always-on default (deviate only when flagged and approved); the rest load on reference.

**Detail**

| Guide | Covers | When to load |
|-------|--------|--------------|
| `STYLE.md` | Core coding style | Always on |
| `RUST.md` | Rust addendum to Style | Writing Rust |
| `POS.md` | Python as a readable alternative to shell scripts for admin/small tasks | Writing a system-administration or small utility script |
| `CHANGELOG.md` | Changelog format | Drafting a changelog entry |
