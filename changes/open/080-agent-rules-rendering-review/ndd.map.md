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
      - [Plan](#plan)
        - [Intent](#intent)
        - [Context](#context)
        - [Held](#held)
        - [Unresolved](#unresolved)
      - [Build](#build)
        - [Build Lock](#build-lock)
      - [Conclude](#conclude)
        - [Archiving](#archiving)
    - [Change Style](#change-style)
      - [Trivial](#trivial)
      - [Vibe](#vibe)
        - [Bounds](#bounds)
      - [Exploratory](#exploratory)
        - [Focus](#focus)
      - [Formal](#formal)
        - [Change Specification](#change-specification)
        - [Implementation Plan](#implementation-plan)
        - [Formal Build](#formal-build)
    - [Discussion](#discussion)
      - [Discussion Records](#discussion-records)
      - [Discussion Conclude](#discussion-conclude)
    - [Startup Scan](#startup-scan)
    - [Bootstrapping](#bootstrapping)
    - [Gates and Permissions](#gates-and-permissions)
      - [Approval](#approval)
    - [Keywords](#keywords)
      - [Process Keyword](#process-keyword)
      - [Aside Keyword](#aside-keyword)
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
```

**Attention dies under overwhelm.** So whenever the agent has a set of items to present — a worklist, open changes, map nodes to edit — it surfaces them in summary (e.g. bullet points), so the user is oriented, then works through it one item at a time, holding the stack itself.

The set alone is more than anyone can hold, but item-by-item alone would leave the user unsure where they are. Together they give orientation and prevent the agent from advancing faster than the user can follow. Each item is introduced by name and by its place in the set, such as *3 of 7*. A message asks at most one question, ending where it asks it.

The focused items are where comprehension is built; skip that and the user's role degrades to approving map diffs instead of code diffs — a better level of abstraction, but still passive review.

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
  tearne: {at: 2026-10-07, hash: 1ca3b28f}
```

A node's name can change; its identity can't. A small immutable token in the yaml scaffolding block survives node renames and moves. [Navigation](#navigation-links) never uses it, nor does agent output — references name the heading, so the id can be meaningless.

**Detail**

The **scaffolding block** is fenced YAML directly under the navigation links containing the `id` and any [approval stamps](#approval-stamp). It's agent-maintained. The `id:` key is map-unique, lowercase alphanumeric, three or more characters (e.g. `k7f`) - a token rather than a readable slug to avoid edit or link temptation. A user may hand-draft a node without a block; the [mechanical review](#tidy) adds one and reports it, so identity is never silently missing.


# Navigation Links

[↑ Node](#node)

```yaml
id: b3q
approvals:
  tearne: {at: 2026-09-13, hash: dc036cd6}
```

The tree is defined by its links. Each node names its parent and each child. Siblings aren't listed directly.

> [!IMPORTANT] Links resolve by node name, never by ID, so ordinary markdown tooling navigates them and a node's identity token never appears as a link target.

**Detail**

The parent link comes first, its text the target's name prefixed with `↑`; only the map's root has none. Child link text is the target node's actual name, so a markdown language server jumps straight there. Each line but the last ends with ` \`, so the block renders one link per line. Because links are name-anchored, renaming a node is a mechanical re-point of the links that named it. A user may omit links while drafting; the [mechanical review](#tidy) adds them and reports it.

Child order belongs to the parent, in natural reading order.

Because links resolve by name, every heading must be unambiguous within its [map file](#map-files); a link into another file names the file before the anchor.

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
```

The map's shape is shown at a glance by a **tree overview**, a nested list of links one per node, held in a *Contents* node, the first child of each [map file](#map-files)'s top node. Nodes not yet written are marked `(TODO)`, so the intended shape is visible before the content is. The rendering is only a convenience: the real tree is encoded in the navigation links, and the overview is kept in step with them by [Tidy](#tidy).

**Detail**

A map is one file until a branch is split out into its own [map file](#map-files); navigation works the same either way.

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
  tearne: {at: 2026-09-13, hash: cfaf5824}
```

Keep nodes small and focussed on one concept. The rough upper bound for size is around 800 characters, but the real test is felt during review.

Each time the agent edits a node it counts and reports the characters, including the *Detail* section and taking an inline link as the length of its visible text. The [navigation links](#navigation-links), *See also*, tables and diagrams are excluded. If over the bound the agent flags the node rather than silently trimming pre-existing text. On a map that carries stamps, a review does not flag a node that is not [due](#sign-off) for the session's [approver](#approver): the call was previously made and signed off.

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
```

A node says each thing once, and nothing the reader already has. The ways it fails, most often:

- A sentence restating its neighbour.

- A *See also* entry repeating the prose or its target, where an inline link would do.

- Provenance, such as what came first or why it was chosen, which belongs in the change record.

- An example the linked node already gives.

- Flourish.

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
  tearne: {at: 2026-09-29, hash: c62bea61}
```

[Orient Then Focus](#orient-then-focus) applied to the map. Nodes are
1. drafted,
2. surfaced with [character count](#node-sizing), plus a diff for an edit,
3. written in chat or in place as the user has asked, and
4. treated as settled only once the reply is [approval](#gates-and-permissions).

On a map that carries stamps, approval also counts as [sign-off](#sign-off). No edit is silent or made in bulk. Corrections that change no meaning — a typo, spacing, a stale link — are applied and reported rather than surfaced, but only if every item in hand is one.

The rule binds the agent, not the user, who edits the map freely and unannounced. After being told or noticing an edit, the agent runs [Tidy](#tidy) over the node — its new count and any knock-on it can see, what it owes for its own edits — and logs it only if it changes what the build must do.


# Change-Management

[↑ NDD](#ndd) \
[Change Lifecycle](#change-lifecycle) \
[Change Style](#change-style) \
[Discussion](#discussion) \
[Startup Scan](#startup-scan) \
[Bootstrapping](#bootstrapping) \
[Gates and Permissions](#gates-and-permissions) \
[Keywords](#keywords) \
[Thought Management](#thought-management)

```yaml
id: cm4
```

How the spec evolves: a change is a single markdown file, drafted in `changes/open/`, that moves through a lifecycle under user-owned gates — then it's archived to `changes/archive/` under a date prefix. Beside it, `changes/open/active.md` holds the build lock.

**Detail**

A change's file name is its title in two to five hyphenated words, optionally behind a leading number that helps sequence the queue. Neither is an identity: rename an open change freely as it evolves, repointing `active.md` if it names it.


# Change Lifecycle

[↑ Change-Management](#change-management) \
[Lifecycle Flow Reads](#lifecycle-flow-reads) \
[Plan](#plan) \
[Build](#build) \
[Conclude](#conclude)

```yaml
id: l5g
```

A change is a single markdown document that advances through three phases:

1. **[Plan](#plan)** — the write-only phase that produces the change document; the [Change Style](#change-style) sets its internal shape.
2. **[Build](#build)** — doing the work against whatever the Plan produced, the same whichever style made it.
3. **[Conclude](#conclude)** — a retrospective once the work is accepted.

Each phase is drafted into the document, then surfaced for the user's explicit approval before the next begins.

The document is the single carrier of state: where a change sits is read from what it contains, not from any status field. A part reaches the document once [approved](#approval), or sooner if the user asks for the draft in place.

The Plan → Build boundary is the load-bearing gate: the change's own work waits until a plan is approved, apart from the [map exemption](#edit-governance).


# Lifecycle Flow Reads

[↑ Change Lifecycle](#change-lifecycle)

```yaml
id: l9t
approvals:
  tearne: {at: 2026-10-07, hash: 30539b07}
```

At each lifecycle hinge the agent reads the governing map node before moving: the [Discussion](#discussion) node when a discussion is to become a change, the next plan part's node before drafting it, the [Conclude](#conclude) node when Build hands back, and the [Archiving](#archiving) node when a Conclude is approved. These **flow reads** keep the method's shape live in the agent's attention; they are distinct from the **reasoning reads** done only when a rule's rationale is in doubt.


# Plan

[↑ Change Lifecycle](#change-lifecycle) \
[Intent](#intent) \
[Context](#context) \
[Held](#held) \
[Unresolved](#unresolved)

```yaml
id: v3d
approvals:
  tearne: {at: 2026-09-30, hash: b2d28fbf}
```

The plan builds up in **parts**, each drafted then surfaced for approval before the next. Every plan starts with the [Intent](#intent); what follows is set by the [Change Style](#change-style):

- **Trivial**: nothing more — Intent is the whole plan.
- **Vibe**: [Bounds](#bounds).
- **Exploratory**: [Focus](#focus).
- **Formal**: [Change Specification](#change-specification) and optional [Implementation Plan](#implementation-plan).

What may be written meanwhile is set by [Gates and Permissions](#gates-and-permissions). Two further sections sit outside the parts sequence, ungated: [Context](#context), which explains why the change exists, and [Held](#held), which catches material arriving before its part.

A Plan need not be fully formed to exist. A change may sit at any degree of formation — from an [Intent](#intent)-only draft just parked via [aside](#aside-keyword), up to a completed preparation section awaiting approval.


# Intent

[↑ Plan](#plan)

```yaml
id: i8b
approvals:
  tearne: {at: 2026-09-30, hash: 7e7fdf89}
```

The opening part: what the change must achieve, in domain language, stated so the user can approve it. Not how it will be delivered unless relevant to the requirement, and not why it is needed: every *why* — history, provenance, the reasoning that led here — belongs in [Context](#context). Kept brief and requiring user approval before anything else proceeds. For a [Trivial](#trivial) change the Intent is the whole plan.

Its prose is capped at ~500 characters; Context is outside the cap, so the opening scans in seconds. Once the change's preparation section — [Bounds](#bounds), [Focus](#focus), or [Change Specification](#change-specification) — is approved, the agent re-reads the Intent and cuts whatever it now carries, surfacing the trimmed Intent with its count. Trivial changes have no preparation section and no trim step.


# Context

[↑ Plan](#plan)

```yaml
id: c7d
```

An optional section of the change document, sitting under the [Intent](#intent): the history, provenance and prior attempts a reader needs to make sense of why the change exists. Keeping it here is what lets the Intent stay one quick paragraph, and the Intent's cap does not reach it.

It is the durable counterpart of [Held](#held). Context is written to last and travels to the archive with the change; Held is transient and must be empty before [Conclude](#conclude). Material waiting to be placed is held, material explaining why the change exists is Context.

Keep it to the least that lets a later reader rediscover the full detail for themselves: enough flavour and pointers to pick the trail back up, never a retelling.


# Held

[↑ Plan](#plan)

```yaml
id: h5d
approvals:
  tearne: {at: 2026-09-30, hash: 39c319a5}
```

A section at the foot of the change document holding on-topic material that arrived before its part — a scope note during the [Intent](#intent), a task while a preparation section is still settling. Writing it down when it arrives costs nothing and survives a lost session; it is exempt from the parts' caps, since nothing is meant to stay there.

Opening each new part, the agent releases into it whatever now belongs. Anything still in Held at [Conclude](#conclude) becomes an item in [Unresolved](#unresolved), blocking completion until placed or dropped.

**See also**

- [Aside Keyword](#aside-keyword) — the other half of the split: a *separate* proposal is parked, not held.
- [Context](#context) — the durable counterpart: material that explains the change rather than waiting to be placed.


# Unresolved

[↑ Plan](#plan)

```yaml
id: n8u
approvals:
  tearne: {at: 2026-09-29, hash: 51f94c56}
```

The open items in a plan part that the agent cannot settle alone. The agent surfaces the full list in chat so the user sees everything outstanding, then walks through them [one at a time](#orient-then-focus). Each answer folds back into the part's prose and the list shrinks; the part is ready for approval only once the list is empty. It may appear wherever a part is being settled, and items may be cross-cutting: resolving one can send the plan back to an earlier part.

**Detail**

The list is deleted when its part is settled; its absence is the signal that the part is ready.


# Build

[↑ Change Lifecycle](#change-lifecycle) \
[Build Lock](#build-lock)

```yaml
id: u6k
```

When executing the plan against the real project files the agent follows the plan rather than changing the plan mid-flight, marking progress and posting concise updates. It interrupts only when something warrants it — a planned pause, surprise, ambiguity, an error in the plan, or a task that [edits the map](#engagement-rule).

Only one change builds at a time, held by the [build lock](#build-lock). Throughout, the agent keeps a running **Log** at the foot of the document — a terse record of the unexpected (surprises, deviations, blockers, partial progress), so a resuming session has the necessary context. Routine execution going to plan needs no entry.

**Detail**

A versioned project agrees a bump kind on build start, and bumps patch every hand-back for testing.

The change can be returned to planning for rewriting any time the user chooses.


# Build Lock

[↑ Build](#build)

```yaml
id: b7n
```

What keeps one change building at a time. [Build](#build) begins only on the user's approval of the plan; on that approval the agent takes the lock by writing the change file name into `changes/open/active.md`, reporting success — or, if the file already exists, stopping without touching it, since another change is already mid-build.

Releasing the lock deletes the file. A build that changed code keeps the lock even when handed back to planning; only an untouched one may release it, so unfinished work is never silently abandoned.


# Conclude

[↑ Change Lifecycle](#change-lifecycle) \
[Archiving](#archiving)

```yaml
id: o4j
approvals:
  tearne: {at: 2026-09-29, hash: e8ce6710}
```

The closing note, written only once the user confirms the build is done. It records the delta from the plan — deviations, surprises, documents touched — not a summary of what the plan already said.

Anything still [Held](#held) is released before Conclude begins — folded into the change, spun off as its own [parked change](#plan), or discarded by the user.

When there's nothing to add, "Completed." is enough. Capped at ~500 characters, counted and reported when surfacing the draft; past the cap the agent asks the user to adjudicate. The note is surfaced on its own; any changelog entry follows separately after approval, then [Archiving](#archiving) proceeds.

Its mere presence is the marker that the change is finished.

**See also**

- [Enjoyment](#enjoyment) — artifact economy: why Conclude is capped short and never re-tells the journey.


# Archiving

[↑ Conclude](#conclude)

```yaml
id: a9v
```

Once the user approves the [Conclude](#conclude) note, the change leaves `changes/open/` for `changes/archive/`, losing any leading number and gaining the ISO date it concluded — `140-config-file-format.md` becomes `2026-05-14-config-file-format.md`. The [build lock](#build-lock) is then released.

A versioned project with substantive change also proposes a changelog entry with the draft note, added on the same approval. [Tidy](#tidy) runs before the move; after it the agent offers a [Map Review](#map-review) in its light scope. If the project map defines release steps, the agent asks whether it is time to run them, and if so offers a full Map Review first.


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
  tearne: {at: 2026-10-02, hash: cfc11369}
```

The record itself. Kept concise, in whatever prose shape fits the topic — agreements with their essential reasoning, open questions, options and links to related work. The agent prunes and rewrites the record freely to reflect current thinking, outside the [Engagement Rule](#engagement-rule): Discussion edits are not drafted-surfaced-settled or counted. Git history holds the deep archive, and past reasoning is retained only where its loss would risk revisiting a dead-end or where an idea is worth flagging for later resurfacing.

On pause the agent leaves a **Resume** anchor with return points and a pointer to current thinking; the anchor is trimmed on resumption. The agent flags meaningful connections and discusses uncertain or consequential relationships before settling them.


# Discussion Conclude

[↑ Discussion](#discussion)

```yaml
id: d9k
approvals:
  tearne: {at: 2026-09-29, hash: 292cf7d6}
```

The closing note for a discussion. Either party may propose it — the agent when nearing-conclusion looks reached, the user when they say so. The agent drafts a short prose (capped ~500 characters, counted and reported when surfaced) stating what the discussion produced (understanding, decisions, promoted candidates with links to their new [parked changes](#plan)), what was dropped, and any ideas worth flagging for later resurfacing. The user approves before archiving.

At this moment the agent walks anything in the record that could become its own change; the user promotes each to a parked change (Intent only) or drops it. A discussion is not concluded with any left hanging.

A discussion's filename is a readable slug ending `-discussion.md`; on approval it is prefixed with the ISO date and moved to `changes/archive/` (`<slug>-discussion.md` → `YYYY-MM-DD-<slug>-discussion.md`). Links are updated on rename.


# Change Style

[↑ Change-Management](#change-management)

```yaml
id: e3n
approvals:
  tearne: {at: 2026-09-30, hash: a694e161}
```

Each change is worked in one of four styles, each giving the [Plan](#plan) its own shape after [Intent](#intent). [Build](#build) and [Conclude](#conclude) are the same whichever is chosen. The agent proposes a style once Intent is approved — default **Formal** — and the user confirms. The chosen style is recorded as a `**Change Style:** <name>` line beneath the change's title, before the Intent. The four styles are [Trivial](#trivial), [Vibe](#vibe), [Exploratory](#exploratory) and [Formal](#formal); each names the preparation section it agrees before Build.

| Style | Preparation before Build |
|-------|--------------------------|
| **Trivial** | none — Intent is the whole plan |
| **Vibe** | [Bounds](#bounds) |
| **Exploratory** | [Focus](#focus) |
| **Formal** | [Change Specification](#change-specification) and optional [Implementation Plan](#implementation-plan) |

The four are not a ladder: the agent proposes the style whose shape fits, not the lightest that might do. Style may be revisited if the change turns out to want a different shape, in which case the agent returns to planning.


# Trivial

[↑ Change Style](#change-style)

```yaml
id: t0v
approvals:
  tearne: {at: 2026-09-30, hash: 4aebc61c}
```

Uses [Intent](#intent) only — the whole plan. The lightest of the four styles. Chosen when a change has virtually no substantive ambiguity — the domain outcome is clear, and the agent finds no decision along the way that would reasonably need surfacing for approval. During [Build](#build) the agent verifies proportionately to what is being changed and reports results; anything consequential that emerges is surfaced rather than absorbed silently.

Trivial is not a shortcut around thinking — a change that starts here and turns out to hide substantive ambiguity returns to planning under a different style.


# Vibe

[↑ Change Style](#change-style)

```yaml
id: v2m
approvals:
  tearne: {at: 2026-09-30, hash: c8e6015d}
```

Uses [Intent](#intent) and a light [Bounds](#bounds) section. Chosen when the user opts to let the agent decide the shape of the work as it goes; the safeguard is the agent's judgement about when to escalate, not an upfront specification. For example, stakes may be low enough that tighter specification isn't worth the effort. Bounds is kept brief on purpose — a short shared understanding of anything context-specific worth naming, and nothing more. Wordy Bounds would drain the very attention Vibe was chosen to save.

During [Build](#build) the agent works within the agreed envelope and escalates on its own judgement when something turns up that Bounds could not have anticipated. If a tighter shape turns out to be needed, the change returns to planning under Exploratory or Formal.


# Bounds

[↑ Vibe](#vibe)

```yaml
id: b3n
approvals:
  tearne: {at: 2026-09-30, hash: cce230ea}
```

The preparation section for a [Vibe](#vibe) change: a brief shared understanding, agreed after [Intent](#intent), of anything context-specific worth naming before [Build](#build) begins. The agent proposes Bounds. The safeguard is the agent's judgement to escalate when the stakes rise, not an attempt to enumerate every case.

Bounds are context-dependent — a hard constraint, a performance sensitive piece of adjacent code, a checkpoint the user wants surfaced, or a specific decision to reserve.

Bounds has a soft anchor of ~200 characters. Overrun is not a cap breach — it is a signal that the wrong style was chosen.


# Exploratory

[↑ Change Style](#change-style)

```yaml
id: e5x
approvals:
  tearne: {at: 2026-09-30, hash: 9638b306}
```

Uses Intent and [Focus](#focus) sections. Chosen when trying to predict the path upfront costs more than taking it step by step, with each step informing the next. Focus names the conceptual question being pursued and a useful point at which to take stock; there is no worklist or done-when, because knowing when to close is part of the work.

Exploratory is real-time collaboration on a moving target: user and agent think through the question together, adjusting as understanding shifts. If executing code is part of learning, that is authorized separately — the exploration itself stays in dialogue. When the question resolves and delivery follows, the change concludes and delivery is planned as its own change.


# Focus

[↑ Exploratory](#exploratory)

```yaml
id: f2q
approvals:
  tearne: {at: 2026-09-30, hash: 45a7caa6}
```

The preparation section for an [Exploratory](#exploratory) change: the conceptual question being pursued, and a useful point at which to take stock. The agent proposes it; the user amends and confirms.

Focus is a lightweight artefact — a sentence or two on each part, not a plan. The question is what the pair is actually trying to understand; the stocktake point is when to pause and assess whether the exploration is landing (a specific milestone, a duration, or a natural checkpoint in the material).

If the stocktake reveals the question has shifted, Focus can be re-agreed rather than the change concluded. Focus has a soft anchor of ~300 characters. Overrun is not a cap breach — it is a signal that the shape wants Formal rather than Exploratory.


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
  tearne: {at: 2026-10-07, hash: 6baee183}
```

The preparation section for a [Formal](#formal) change: the target — what must hold when the change lands.

The target is expressed as proposed map nodes. When the specification will touch multiple nodes, the agent proposes a sub-map or whole-map file copy as the target so edits are visible in editor diffs against a committed baseline, pausing to give opportunity to check in. Whatever the shape, once built the live map must describe the completed result. Development happens in the change file, with a companion folder for supporting material if warranted.

Nodes are approved per-node under the [Engagement Rule](#engagement-rule), with stamps written on the target that transfer to the live map at Build's closing act.

If the Change Specification stalls, the agent proposes conceptual exploration, a [Vibe](#vibe) spike or a smaller scope.


# Implementation Plan

[↑ Formal](#formal)

```yaml
id: ip5
approvals:
  tearne: {at: 2026-10-07, hash: 46e61232}
```

An optional preparation section for a [Formal](#formal) change, added when consequential delivery choices remain after the [Change Specification](#change-specification) is agreed. Captures decisions about how to deliver — sequencing, staging, dependencies, rollback — rather than a step-by-step checklist. Omitted when the delivery path is obvious.

The agent proposes an Implementation Plan when the specification alone does not settle delivery. If added, Build follows it; deviations go to the [Log](#build), and material rework re-agrees the plan with the [Build Lock](#build-lock) kept, resuming against the revised plan — a full return to planning is reserved for abandoning Formal.


# Formal Build

[↑ Formal](#formal)

```yaml
id: fb9
approvals:
  tearne: {at: 2026-10-07, hash: 0b0dfd56}
```

Layered onto general [Build](#build); the Formal additions follow.

Before proposing Build, the agent reconciles the [Change Specification](#change-specification) against current reality; revisions required by intervening work return the change to spec development, as do issues uncovered during the build. Build-time re-agreement keeps the [Build Lock](#build-lock), resuming against the revised target when agreed.

Build lands non-map assets in place; as its closing act, approved node texts and stamps on the Change Specification target promote into the live map, so divergence surfaces before Conclude.


# Formal Conclude

[↑ Formal](#formal)

```yaml
id: q4m
approvals:
  tearne: {at: 2026-10-07, hash: 4744bcf2}
```

Layered onto general [Conclude](#conclude) and [Archiving](#archiving); the Formal additions follow.

At Conclude, verification walks the [Change Specification](#change-specification) against the built result; drift on any per-node approved element triggers re-engagement of that node.

At Archiving, useful evidence and rationale are retained; disposable experiments are removed via a curated retain-or-drop asset walk. Whole-map copies are disposable in full — promoted content lives in the live map, and the copy was only a development aid, not a document to maintain.


# Startup Scan

[↑ Change-Management](#change-management)

```yaml
id: x7t
approvals:
  tearne: {at: 2026-09-29, hash: a8a5f1ed}
```

What the agent does first in every session: orient from `changes/open/`. A project with no `map.md` and no `changes/` tree hasn't started yet — the agent [bootstraps](#bootstrapping) it. Otherwise it reads every change and [discussion](#discussion) and places each — a change by lifecycle position, a discussion by topic and whether nearing-[Conclude](#discussion-conclude).

From that the agent announces the session's mode — planning, building, discussing, or a combination — reports what's open, offers a [Backlog Review](#backlog-review), and proposes the next step.

**Detail**

An interrupted build is recognised by `active.md` pointing at a change whose work is unfinished; the agent reads that change's [Log](#build) to recover context rather than restarting. A plan reopened mid-build says so in its [Log](#build) — with no [Conclude](#conclude) note yet, the change is back in planning.


# Bootstrapping

[↑ Change-Management](#change-management)

```yaml
id: b6t
```

How a project acquires its first map. A fresh install vendors only the method under `ndd/`, leaving the project itself empty — no `map.md`, no `changes/` tree — so the ordinary lifecycle has nothing to stand on. The agent detects this at the [Startup Scan](#startup-scan) and offers to bootstrap rather than proceeding as normal.

It scaffolds the [`changes/` tree](#change-management) and seeds the project map — `map.md` in the project root, distinct from the read-only method map at `ndd/ndd.map.md` — through discussion and any pre-existing documentation. How much to seed is the user's call: a single root node named for the system, or a fuller sketch.

Adopting an existing codebase adds a survey: the agent reads existing assets and proposes nodes one at a time per the [Engagement Rule](#engagement-rule). Reality-reflecting map edits need no active change (see [Edit Governance](#edit-governance)), though wrapping a migration in one can keep it systematic.


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

[↑ Gates and Permissions](#gates-and-permissions)

```yaml
id: k4d
```

Approval requires a clear affirmative given in response to the agent asking ("yes", "ok", "go ahead"). Silence, a tangent, or a reply that raises new questions is not approval. It only covers what was surfaced and no more: agreeing to draft prose is not approval of the prose.

How a draft is delivered is the user's choice. The default is chat; a bare "write" asks for this one draft in place, and only an instruction that says so, such as "write everything from here", switches the rest of the session. *Write* means put it in place and stop until the user hands back, when the agent runs [Tidy](#tidy) over what changed before asking anything; *write* is never approval and never a cue to move on. However a draft arrives it stands provisional until the user accepts or amends it, and one written in place is reverted if declined.


# Keywords

[↑ Change-Management](#change-management) \
[Process Keyword](#process-keyword) \
[Aside Keyword](#aside-keyword)

```yaml
id: k9y
```

Two message prefixes that let the user trigger a small side-action without derailing the current work. The agent handles the aside, confirms in a line, and returns to what it was doing. There are two:

- [process](#process-keyword) captures an observation about the method itself;
- [aside](#aside-keyword) parks a **separate** proposal as its own draft change ([Intent](#intent) only).


# Process Keyword

[↑ Keywords](#keywords)

```yaml
id: r4c
```

A message starting with `process:` records an observation about the method or the agent's conduct — friction, a suggestion, something to revisit — without acting on it. The agent appends it to `changes/process-feedback.md`, confirms in a line, and carries on with whatever was under way.

**Detail**

The entry is dated and captures the observation plus any surrounding context (phase, active change, topic) that would otherwise be lost; the agent may rephrase for later readability. The file is append-only and created with a header if absent. It lives in the repository as an ordinary versioned file — not git-ignored — so the feedback is shared between collaborators; committing it stays a user action, like any git write.


# Aside Keyword

[↑ Keywords](#keywords)

```yaml
id: y2f
approvals:
  tearne: {at: 2026-09-29, hash: 57352dbc}
```

A message starting with `aside:` parks a topic for later without breaking the current flow. The agent scans open [discussions](#discussion) and changes for overlap and routes by content: appends to an existing discussion when the aside continues that thread; else opens a new parked change with an [Intent](#intent) only if the aside is Intent-shaped; else opens a new [discussion](#discussion) record. Placement is confirmed in one line. Overlap noticed with an existing change is named in the confirmation without attaching, so the change's owner can fold it in on resumption. Material belonging to the *current* change is [Held](#held) instead.


# Thought Management

[↑ Change-Management](#change-management)

```yaml
id: t4m
```

The user may throw out a thought at any point — a question, a digression, an idea for later — and the agent keeps the breadcrumb trail. A thought goes to one of four places:
- answered now, when a line will do;
- taken as a digression, for as long as it earns, that ends by naming the item returned to;
- [held](#held), when it belongs to the current change; or
- parked as a change of its own, as the [aside keyword](#aside-keyword) does.

The agent says in a line where it went, and asks only when unclear.

While a set is in progress, every message ends with a **status line** showing the stack: the set and the item, one `>` per level stepped off it, and the count of held items after a `·` when there are any. Returning pops a level; with nothing in progress there is no line.

**Detail**

`map edits 3 of 7` on the item; `map edits 3 of 7 > aside` while placing a stray thought; `map edits 3 of 7 · held 2` with two items in Held.


# Maintenance

[↑ NDD](#ndd) \
[Map Review](#map-review) \
[Backlog Review](#backlog-review) \
[Sign-off](#sign-off)

```yaml
id: t7v
```

The upkeep of the map and the backlog, put to the user as three reviews. Each is one yes-or-no at its moment, and each opens a list of findings walked one item at a time.

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
```

Map Review is offered by the agent as a yes-or-no at two moments, and the moment sets the scope:
- after an [archive](#archiving) the light scope,
- before a release the full scope.

[Tidy](#tidy) has already run and reported by then, so a yes opens the **findings list**: everything the Tidy and Map Review checks found that needs a judgement, summarised first and then considered one item at a time by [Orient Then Focus](#orient-then-focus). A finding quotes what it faults and what already covers it, so the overlap is seen rather than asserted.

Findings are not stored. A review recomputes from the map, so a deferred finding reappears next time and costs a word to dismiss again. The checks stay askable by name, as is a scope, for anyone who wants less or more than the moment offers.

| Scope | Checks | Moment |
|-------|--------|--------|
| Light | [Shape](#shape), and prose against [Writing Style](#writing-style) | Offered after an archive |
| Full | Light plus [Consistency](#consistency), [Rendering](#rendering) | Offered before a release |


# Tidy

[↑ Map Review](#map-review)

```yaml
id: u8k
approvals:
  tearne: {at: 2026-09-13, hash: d1cf8a9d}
```

Agent-run housekeeping, run on the nodes the user edited when they hand back, and across the whole map before an [archive](#archiving). The agent needs no prompting and reports briefly every fix made and every count it took. It is restricted to [corrections](#engagement-rule), never changes of meaning; anything needing judgement is either left for a subsequent [Map Review](#map-review) or handed back to the user immediately.

It fixes and reports a [tree overview](#map-structure) out of step with the navigation links, a missing scaffolding [id](#node-identity) or [navigation link](#navigation-links), a link left behind by a rename, and an unambiguous grammatical slip. It reports only the count of nodes over the [size bound](#node-sizing), not counting those cleared for the session's [approver](#approver); with no handle to hand it counts them all and says so.


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
  tearne: {at: 2026-09-29, hash: c21465c5}
```

Backlog Review is offered by the agent as a yes-or-no at the [Startup Scan](#startup-scan), once the open items have been reported. It covers parked changes and [discussions](#discussion) in `changes/open/`, walked one at a time. A parked change is settled — kept, updated, renumbered, merged, or discarded. A discussion has its agreements, open questions, and anything that could become a change surfaced; the user chooses what to take forward.

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
  tearne: {at: 2026-09-13, hash: 407154f5}
```

A stakeholder approves the map a few nodes at a time. Each node can carry an [approval stamp](#approval-stamp) per person, recording when they approved it and a [fingerprint](#fingerprint) of the text they saw. A stamp is scaffolding, written and reported rather than negotiated.

Nothing is marked when a node changes. Drift is found by comparing: a node is *due* for a person when its fingerprint no longer matches their stamp, or it has none for them. A map with no stamps shows nothing, and gains its first only when the user asks for one; from then on every approval of a node edit stamps it for the [approver](#approver).

**See also**

- [Orient Then Focus](#orient-then-focus) — due nodes are summarised, then walked one at a time.
- [Node Sizing](#node-sizing) — re-approval is a re-read of one short node, which is what keeps it humane.


# Approver

[↑ Sign-off](#sign-off)

```yaml
id: v7a
approvals:
  tearne: {at: 2026-09-13, hash: 4fb46bea}
```

The approver is the person a [sign-off](#sign-off) stamp is written for, named by a handle. The agent resolves the handle the first time a stamp is needed, not at the [Startup Scan](#startup-scan), and says which handle it is using the first time it does. Git's `user.name` is the handle unless the map already carries stamps and none match that name; then, or when git has no name, the agent asks rather than guessing.

The user can override the handle, for one approval or for the rest of the session, as when pairing with another person. Before stamping, the agent says which handle it will use. A one-off override lasts one stamp and the handle then returns to the session default; a session override holds until changed.


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
```

Guidance for the code written by agents on user projects, distinct from the map spec that governs the *map*. NDD ships a set of **suggested** standards a project adopts, adapts, or ignores — installed as plain markdown under `ndd/standards/`, not folded into the map. This node is the index: an agent scans it to see what exists and opens only the guide a task touches. The code **Style** guide is an always-on default (deviate only when flagged and approved); the rest load on reference.

**Detail**

| Guide | Covers | When to load |
|-------|--------|--------------|
| `STYLE.md` | Core coding style | Always on |
| `RUST.md` | Rust addendum to Style | Writing Rust |
| `POS.md` | Python as a readable alternative to shell scripts for admin/small tasks | Writing a system-administration or small utility script |
| `VERSIONING.md` | Semver conventions | Prompted: project setup, changes accumulating, or a breaking change |
| `CHANGELOG.md` | Changelog format (dated or semver) | Drafting a changelog entry |
