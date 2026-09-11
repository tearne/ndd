# NDD

```yaml
id: a3k
```

[↑ NDD Project](map.md#ndd-project)
[Principles](#principles)
[Specification](#specification)
[Change-Management](#change-management)
[Maintenance](#maintenance)
[Tooling](#tooling)
[Standards](#standards)

NDD, Non-Dead Design, aims to improve knowledge management for agentic software development. The name reflects the [three deaths](#three-deaths) it seeks to prevent: of specifications, of structural thinking, and of comprehension.

The map is the one artefact that keeps all three alive: a conceptual **map** of the system, acting as the hub for specification and change management rather than a document off to one side. The method itself is expressed as a map.

- **Principles** — the founding rationale in more detail.
- **Specification** — the conceptual map as the primary comprehension artefact.
- **Change-Management** — how the spec evolves, through a change lifecycle and user-owned gates.
- **Maintenance** — the reviews that keep the map, the code and the backlog in step.
- **Tooling** — the generic markdown tooling the format is designed to exploit.
- **Standards** — suggested coding standards NDD ships for the code agents write on a project.

```
NDD
├ Principles
│ ├ Three Deaths
│ ├ Comprehension is an Activity
│ ├ Intent Memory
│ ├ Enjoyment
│ ├ Local Sufficiency
│ │ └ Trees over Graphs
│ ├ Cross-Agent Falsifiability
│ └ Orient Then Focus
├ Specification
│ ├ Node
│ │ ├ Node Identity
│ │ ├ Navigation Links
│ │ ├ Node Sections
│ │ │ └ Callouts
│ │ └ Approval Stamp
│ │   └ Fingerprint
│ ├ Map Structure
│ │ └ Map Files
│ ├ Node Sizing
│ ├ Writing Style
│ │ ├ Conceptual Writing
│ │ └ Formatting
│ └ Edit Governance
│   ├ Sync Rule
│   └ Engagement Rule
├ Change-Management
│ ├ Change Lifecycle
│ │ ├ Plan
│ │ │ ├ Intent
│ │ │ ├ Context
│ │ │ ├ Held
│ │ │ ├ Approach
│ │ │ └ Worklist
│ │ ├ Build
│ │ │ └ Build Lock
│ │ └ Conclude
│ │   └ Archiving
│ ├ Cadences
│ ├ Startup Scan
│ ├ Bootstrapping
│ ├ Gates and Permissions
│ │ └ Approval
│ └ Keywords
│   ├ Process Keyword
│   └ Aside Keyword
├ Maintenance
│ ├ Tidy
│ ├ Shape
│ ├ Prose
│ ├ Consistency
│ ├ Rendering
│ ├ Backlog
│ └ Sign-off
├ Tooling
└ Standards
```


# Specification

```yaml
id: sp1
```

[↑ NDD](#ndd)
[Node](#node)
[Map Structure](#map-structure)
[Node Sizing](#node-sizing)
[Writing Style](#writing-style)
[Edit Governance](#edit-governance)

The conceptual map is the primary artefact. It holds the system's shape as a tree of concepts, structured the way the user thinks rather than how code is organised. Agents render it into code. Everything else in the method — how it changes, how it's viewed — serves this map.

**See also**

- [Comprehension is an Activity](#comprehension-is-an-activity) — maintaining the map is the comprehension-building activity this node's primacy serves.


# Node

```yaml
id: nd1
```

[↑ Specification](#specification)
[Node Identity](#node-identity)
[Navigation Links](#navigation-links)
[Node Sections](#node-sections)
[Approval Stamp](#approval-stamp)

A node represents **one** concept and includes a heading, an agent-maintained scaffolding block holding its metadata, name-anchored navigation links to its parent and children, and terse prose leading with the mental picture. Optional *Detail* and *See also* sections follow.

The format is a strict superset of a plain-markdown section — strip the scaffolding and links and what remains is an ordinary heading with prose, so a map renders and navigates as plain markdown in any tool.

**See also**

- [Trees over Graphs](#trees-over-graphs) — nodes form the tree; a concept's complexity is kept inside its node rather than spread across links.


# Change-Management

```yaml
id: cm4
```

[↑ NDD](#ndd)
[Change Lifecycle](#change-lifecycle)
[Cadences](#cadences)
[Startup Scan](#startup-scan)
[Bootstrapping](#bootstrapping)
[Gates and Permissions](#gates-and-permissions)
[Keywords](#keywords)

How the spec evolves: a change is a single markdown file, drafted in `changes/open/`, that moves through a lifecycle under user-owned gates — then it's archived to `changes/archive/` under a date prefix. Beside it, `changes/open/active.md` holds the build lock.

**Detail**

A change's file name is its title in two to five hyphenated words, optionally behind a leading number that helps sequence the queue. Neither is an identity: rename an open change freely as it evolves, repointing `active.md` if it names it.


# Node Identity

```yaml
id: w9c
```

[↑ Node](#node)

A node's name can change; its identity can't. A small immutable token in the yaml scaffolding block survives node renames and moves.

> [!IMPORTANT] Navigation uses node names, not the ID, so ordinary markdown tooling works and the ID is free to be meaningless.

**Detail**

The **scaffolding block** is fenced YAML directly under the heading containing the `id` and any [approval stamps](#approval-stamp). It's agent-maintained. The `id:` key is map-unique, lowercase alphanumeric, three or more characters (e.g. `k7f`) - a token rather than a readable slug to avoid edit or link temptation. A user may hand-draft a node without a block; the mechanical review adds one and reports it, so identity is never silently missing.

**See also**

- [Tidy](#tidy) — a missing id is added automatically during the mechanical review.


# Navigation Links

```yaml
id: b3q
```

[↑ Node](#node)

The tree is defined by its links, not in a separate structure. Each node names its one parent and each of its children. Siblings aren't listed directly.

> [!IMPORTANT] Links resolve by node name, never by ID, so ordinary markdown tooling navigates them and a node's identity token never appears as a link target.

**Detail**

The parent link comes first, its text the target's name prefixed with `↑`, so the root, which has none, is told apart at a glance; every other node has exactly one. Child link text is the target node's actual name, so an editor with a markdown LSP (e.g. marksman) jumps straight there with `gd`. Because links are name-anchored, renaming a node is a mechanical re-point of the links that named it, and the ID never appears in a link. A user may omit links while drafting; the mechanical review adds them and reports it.

Child order belongs to the parent; order them to reflect natural reading order.

Because links resolve by name, every heading must be unambiguous within its [map file](#map-files); a link into another file names the file before the anchor.

**See also**

- [Trees over Graphs](#trees-over-graphs) — links encode the one-parent tree that keeps navigation walkable.
- [Tidy](#tidy) — missing links are added automatically during the mechanical review; child order is a [Shape](#shape) check.


# Node Sections

```yaml
id: s8r
```

[↑ Node](#node)
[Callouts](#callouts)

The main user-facing parts of a node are each optional and include, in a fixed order: **prose**, **Callouts**, **Detail**, and **See also**. Prose is the mental picture and usually the only part the user must read, but even it can be dropped — a node may carry only *Detail*, for instance. A node using none of these is just a heading: an ordinary markdown section.

**Detail**

*Callouts* flag a load-bearing point and get their own child node. *Detail* is marked with bold `**Detail**` and holds implementation-level precision the user can stop before, such as parameters, thresholds, and algorithms. *See also* is marked with bold `**See also**` and lists cross-cutting references that aren't parent or child, each saying why the relationship matters.


# Callouts

```yaml
id: c5k
```

[↑ Node Sections](#node-sections)

A callout is a "don't skim this" flag on a point the prose already makes. It marks the load-bearing moments where skimming would lose the reader, such as a design trade-off, a non-obvious assumption, or a constraint that shapes the whole node. The prose still carries the meaning; the callout only raises a hand.

**Detail**

Rendered as a `> [!IMPORTANT]` blockquote, never as a highlighter for every notable fact.


# Approval Stamp

```yaml
id: p8m
```

[↑ Node](#node)
[Fingerprint](#fingerprint)

An approval stamp records that one person approved one node. Stamps live in the node's scaffolding block under an `approvals:` mapping keyed by a name or handle, so each person holds exactly one and a re-approval overwrites it. Because they are in the node rather than a separate ledger, they follow it through renames and moves. A node without the mapping is simply unapproved, and most maps never gain one.

**Detail**

Each value holds `at`, an ISO 8601 timestamp with offset, and `hash`, the [fingerprint](#fingerprint) of the text approved. Drift uses only the hash; the timestamp is kept so a later aid can find the version a person saw. Quote the key if it contains a colon or starts with punctuation.

```yaml
id: w9c
approvals:
  alice: {at: 2026-09-10T14:05:00+01:00, hash: 3f9a1c2e}
  bob: {at: 2026-08-02T09:30:00+01:00, hash: 8d02b7e4}
```

**See also**

- [Sign-off](#sign-off) — the check that reads the stamps.
- [Node Identity](#node-identity) — the other thing the scaffolding block holds.


# Fingerprint

```yaml
id: h4q
```

[↑ Approval Stamp](#approval-stamp)

A fingerprint is a hash of what a reader sees in a node. It covers the heading, prose, callouts, *Detail* and *See also*; it excludes the scaffolding block and navigation links.

Comparing fingerprints is a test of equality: a node put back to earlier text regains its old fingerprint, and so clears for whoever approved that text.

**Detail**

Take the node from its heading line to the line before the next heading. Drop the scaffolding block and the navigation-link lines whole; inline links in the prose stay as written, markdown included. Remove every whitespace character. The fingerprint is the first eight hex digits of the SHA-256 of that UTF-8 string. An agent computes it by running code, never by reasoning.


# Map Structure

```yaml
id: m6x
```

[↑ Specification](#specification)
[Map Files](#map-files)

The map's shape is shown at a glance by a **tree overview** — a box-drawing sketch of the whole node tree — held in the top node of each [map file](#map-files). Nodes not yet written are marked `(TODO)`, so the intended shape is visible before the content is. The rendering is only a convenience: the real tree is encoded in the navigation links, and the overview is kept in step with them.

**Detail**

The overview is a fenced code block using box-drawing characters. A map is one file until a branch is split out into its own [map file](#map-files); navigation works the same either way.

The root defaults to the project's name, preferring a term that carries domain information over a generic label like "Application". When that name clashes with a prominent internal node, disambiguate with whichever reads best: a scoping term for the root, a suffix, a parenthetical, or a more specific name for the internal node.

**See also**

- [Trees over Graphs](#trees-over-graphs) — why the sketched shape is a tree, not a general graph.
- [Tidy](#tidy) — keeping this overview in step with the navigation links is part of the mechanical review.


# Map Files

```yaml
id: k2v
```

[↑ Map Structure](#map-structure)

A project has one map; a file is only where a branch of it lives. The entry point is `map.md` in the project root, the one file whose top node has no parent link. Any node's children may live beside or beneath it in a file with a name related to the node, with the extension `.map.md`: a *Testing* node's branch would likely be `testing.map.md`. The hanging node's child links point into that file and the branch's top node keeps a parent link back, so the tree is still read by following links, and the hanging node's prose explains the branch's scope.

A branch is split out for size, or for a conceptual boundary worth seeing in the file list.

**Detail**

Each file's top node carries the overview of the nodes in that file, stopping where a branch continues in another file and naming it. A cross-file link is `[Release Steps](map.md#release-steps)`. Headings must be unambiguous within a file; across files the file name disambiguates.

**See also**

- [Navigation Links](#navigation-links) — the links that carry the tree, within a file and across.
- [Tidy](#tidy) — each file's overview is kept in step with the links in that file.


# Node Sizing

```yaml
id: z9p
```

[↑ Specification](#specification)

Keep nodes small and focussed on one concept. The rough upper bound for size is around 800 characters, but the real test is felt: if a node starts wanting sub-sections, it's outgrown one concept and should split into children.

Each time the agent edits a node it counts the characters and reports the number. The count covers the node's body and its *Detail* section, taking an inline link as the length of its visible text. The [navigation links](#navigation-links), *See also*, tables and diagrams are excluded. Over the bound the agent flags the node rather than silently trimming, so splitting-versus-keeping stays the user's call.

**Detail**

The count measures the node's own content, which is why *Detail* is included and *See also* is not: one explains the concept, the other points away from it.

**See also**

- [Local Sufficiency](#local-sufficiency) — why nodes stay small: a reader must grasp one node from the node alone.
- [Tidy](#tidy) — oversize nodes are reported in the mechanical review summary.


# Writing Style

```yaml
id: p4h
```

[↑ Specification](#specification)
[Conceptual Writing](#conceptual-writing)
[Formatting](#formatting)

How map prose is written, so nodes stay readable and durable. Two sides:

- Conceptual Writing: what the prose *says*

- Formatting: how it's typeset

**See also**

- [Prose](#prose) — prose is checked against these conventions during the check.


# Conceptual Writing

```yaml
id: h3v
```

[↑ Writing Style](#writing-style)

A handful of habits shape how a node reads, and one trap to avoid:

- **Write about the referent, not the node** — make the real subject do something: "The installer script is run from the client's project", not "The script that a client runs".

- **Lead with the mental picture** before any implementation detail.

- **Name the boxes before explaining them** — say "there are three mechanisms: A, B, C" and then give each its own node or bullet point.

- **Flow sentences unbroken** — prefer keeping a sentence whole over interrupting it. A parenthetical em-dash pair reads fine when the aside is one short clause, but once the middle grows long and multi-part the reader loses the opening before the sentence resumes: split it into separate sentences instead.

- **Bullet a set the reader will scan** — when a node names a small set of parts, options, or questions, list them as bullets rather than an in-sentence enumeration, so each is scannable and individually referenceable.

- Don't **couple to code structure**: prose may name a technical concept when load-bearing, but the map tracks the user's model, not the code's shape — so it shouldn't break when code is refactored.


# Formatting

```yaml
id: f2n
```

[↑ Writing Style](#writing-style)

Typographic conventions for map prose.

- Write each paragraph as one continuous line with no hard wraps, so it reflows under soft-wrap.

- Separate bullet points with a blank line when they run long enough to wrap; short single-line points don't need it.

- Two blank lines before a node title, so node boundaries stand out when scrolling a single-file map.

- The parent link's text starts with `↑`, the child links' does not, so the one parent and the root's lack of one show at a glance.

- Use *italics* when a sentence refers to a named section or element (*Callouts*, *Detail*, *See also*), and reserve **bold** for introducing a term of art on first use, so references don't read as competing sub-headings.

- Prefer an inline cross-reference link when a sentence already names another node in passing; reserve a *See also* entry for a standalone pointer the prose doesn't already invoke, each with its own reason it matters.


# Edit Governance

```yaml
id: e7m
```

[↑ Specification](#specification)
[Sync Rule](#sync-rule)
[Engagement Rule](#engagement-rule)

The rules for changing the artefact itself. Three questions govern every edit:

- *what* may be written — the [Sync Rule](#sync-rule);

- *how* the change is made — the [Engagement Rule](#engagement-rule);

- *when* a node is due for work — [Maintenance](#maintenance).

Because these edits describe reality rather than intent, they fall outside the active-change requirement — the **map exemption**: no open change is needed, and they may happen at any time. That exemption lifts only the active-change constraint; the [Engagement Rule](#engagement-rule)'s per-node negotiation for map updates still applies.

**See also**

- [Gates and Permissions](#gates-and-permissions) — the active-change requirement this exemption stands against.


# Sync Rule

```yaml
id: s5y
```

[↑ Edit Governance](#edit-governance)

The map describes what exists, never what is planned: an edit describing work not yet built waits until the work is built.


# Engagement Rule

```yaml
id: n3g
```

[↑ Edit Governance](#edit-governance)

[Orient Then Focus](#orient-then-focus) applied to the map: every edit runs in one order — draft it, surface it with its [character count](#node-sizing), then write only once the reply is [approval](#gates-and-permissions). No edit is silent or made in bulk. Pitch the prompt to what the edit changes — a comprehension check when it reshapes the picture. Corrections that change no meaning — a typo, spacing, a stale link — are applied and reported rather than surfaced, but only if every item in hand is one.

The rule binds the agent, not the user, who edits the map freely and unannounced. Told of such an edit, or noticing one, the agent re-reads the node and reports its new count and any knock-on it can see — what it owes for its own edits — and logs it only if it changes what the build must do.


# Cadences

```yaml
id: e3n
```

[↑ Change-Management](#change-management)

Each change runs at one of three cadences. They differ only in the shape of the [Plan](#plan) — [Build](#build) and [Conclude](#conclude) are the same whichever is chosen. The agent proposes one after Intent is approved — default **Formal** — and the user confirms.

| Cadence | Plan structure |
|---------|----------------|
| **Formal** | Intent → Approach → a task checklist |
| **Explore** | Intent → Approach → topics + a *done-when* |
| **Wander** | Intent only |

- **Formal** is the default, for work that benefits from explicit decisions and step-by-step tracking.

- **Explore** suits work where depth and coverage matter more than a fixed step list — including a change that edits map nodes, whose per-node negotiation is closer to working a topic than to ticking off tasks.

- **Wander** is for work too small or too fluid to plan; the agent flags topic drift and can offer to flush. Having no Approach, its [Conclude](#conclude) leans on the Build [Log](#build) for what happened, and may rename the change to match where the work ended up.

**Detail**

A **task checklist** is discrete tasks, each an atomic outcome ticked off as it lands. **Topics** are areas to work rather than steps to complete, closed by a single *done-when* condition instead of tick-boxes.


# Change Lifecycle

```yaml
id: l5g
```

[↑ Change-Management](#change-management)
[Plan](#plan)
[Build](#build)
[Conclude](#conclude)

A change is a single markdown document that advances through three phases:

1. **[Plan](#plan)** — the write-only phase that produces the change document; the [cadence](#cadences) sets its internal shape.
2. **[Build](#build)** — doing the work against whatever the Plan produced, the same whichever cadence made it.
3. **[Conclude](#conclude)** — a retrospective once the work is accepted.

Each phase is drafted into the document, then surfaced for the user's explicit approval before the next begins.

The document is the single carrier of state: where a change sits is read from what it contains, not from any status field. Chat carries only disclosures and summaries; the drafted text lives in the document.

The Plan → Build boundary is the load-bearing gate: the change's own work waits until a plan is approved, apart from the [map exemption](#edit-governance).


# Plan

```yaml
id: v3d
```

[↑ Change Lifecycle](#change-lifecycle)
[Intent](#intent)
[Context](#context)
[Held](#held)
[Approach](#approach)
[Worklist](#worklist)

During the plan stage project files outside `changes/` remain read-only, save for the [map exemption](#edit-governance). The plan builds up in **parts** — the [Intent](#intent), [Approach](#approach), [Worklist](#worklist) — each drafted then surfaced for approval before the next, culminating in the worklist that [Build](#build) executes. Which parts a change has is set by its [cadence](#cadences). Two further sections sit outside that sequence, ungated: [Context](#context), which explains why the change exists, and [Held](#held), which catches material arriving before its part.

A Plan need not be fully formed to exist. A change may sit at any degree of formation — from an [Intent](#intent)-only draft just parked via [aside](#aside-keyword), up to a complete worklist awaiting approval. The [Startup Scan](#startup-scan) can summarise in informal terms such as *parked at its Intent*, *mid-approach*, or *awaiting a worklist*.


# Intent

```yaml
id: i8b
```

[↑ Plan](#plan)

The opening part: why the change is needed expressed in domain language, not how it will be delivered unless relevant to the requirement. Kept brief and requiring user approval before anything else proceeds. For a [Wander](#cadences) change the Intent is the whole plan.

Its prose is capped at ~500 characters, counted and reported each time the agent surfaces it, with anything over put to the user to adjudicate rather than surfaced as final. History and provenance belong in [Context](#context), which the cap does not reach — the opening must scan in seconds.


# Context

```yaml
id: c7d
```

[↑ Plan](#plan)

An optional section of the change document, sitting under the [Intent](#intent): the history, provenance and prior attempts a reader needs to make sense of why the change exists. Keeping it here is what lets the Intent stay one quick paragraph, and the Intent's cap does not reach it.

It is the durable counterpart of [Held](#held). Context is written to last and travels to the archive with the change; Held is transient and must be empty before [Conclude](#conclude). Material waiting to be placed is held, material explaining why the change exists is Context.

Keep it to the least that lets a later reader rediscover the full detail for themselves: enough flavour and pointers to pick the trail back up, never a retelling.


# Held

```yaml
id: h5d
```

[↑ Plan](#plan)

A section at the foot of the change document holding on-topic material that arrived before its part — a scope note during the [Intent](#intent), a task while the [Approach](#approach) is still settling. Writing it down when it arrives costs nothing and survives a lost session; it is exempt from the parts' caps, since nothing is meant to stay there.

Opening each new part, the agent releases into it whatever now belongs. Anything still held once its part has passed is an unresolved issue in its own right, surfaced before [Conclude](#conclude) and blocking completion.

**See also**

- [Aside Keyword](#aside-keyword) — the other half of the split: a *separate* proposal is parked, not held.
- [Context](#context) — the durable counterpart: material that explains the change rather than waiting to be placed.


# Approach

```yaml
id: a2r
```

[↑ Plan](#plan)

How the change will be carried out, written as a list of decisions and their reasons — not a narrative and not a file-by-file rehearsal, which belongs to the [worklist](#plan). Each decision earns a line only if it carries a reason; self-evident choices need no subsection. Skipped entirely by [Wander](#cadences).

Alongside it sits an **Unresolved** list: the open items the agent can't settle alone, each pointing at the part of the Approach it affects. The agent surfaces the full list in chat so the user can see everything outstanding, then walks through them — for anything non-trivial, one at a time ("4 unresolved items […]. First one: …") rather than asking the user to address them all at once. Answers fold back into the prose and the list shrinks. An empty list means the Approach is ready for approval.

The Approach is capped at ~2000 characters, excluding Unresolved: each time the agent surfaces it, it counts them and reports the number, and past the cap asks the user to adjudicate.

**Detail**

The agent re-reads and prunes its own draft before surfacing — anything not carrying a decision-and-reason comes out — and counts again afterwards. Once the worklist is written the Unresolved section is deleted; its absence is the signal that the Approach is settled.

**See also**

- [Enjoyment](#enjoyment) — artifact economy: why the Approach is pruned to decisions-and-reasons rather than left as narrative.
- [Orient Then Focus](#orient-then-focus) — the Unresolved walkthrough is that principle applied: the whole list surfaced, then one item at a time.


# Worklist

```yaml
id: w4k
```

[↑ Plan](#plan)

The closing part of a [Plan](#plan): the list of actions [Build](#build) executes. It lists only the actions to take, not the reasons for them — those belong in the [Approach](#approach). A task that touches a mapped concept names the node rather than the file that implements it, keeping the plan anchored to the map. An [Explore](#cadences) change carries topics and a *done-when* in its place; a [Wander](#cadences) change has neither.

**Detail**

Before surfacing the worklist the agent prunes it against fixed rules: one task per atomic outcome, no restated "why", no obvious sub-steps, no ceremony tasks (a bare "review" or "double-check") unless they mark a real gate, and no file paths the task name already implies.


# Build

```yaml
id: u6k
```

[↑ Change Lifecycle](#change-lifecycle)
[Build Lock](#build-lock)

When executing the plan against the real project files the agent follows the plan rather than changing the plan mid-flight, marking progress and posting concise updates. It interrupts only when something warrants it — a planned pause, surprise, ambiguity, an error in the plan, or a task that [edits the map](#engagement-rule).

Only one change builds at a time, held by the [build lock](#build-lock). Throughout, the agent keeps a running **Log** at the foot of the document — a terse record of the unexpected (surprises, deviations, blockers, partial progress), so a resuming session has the necessary context. Routine execution going to plan needs no entry.

**Detail**

A versioned project agrees a bump kind on build start, and bumps patch every hand-back for testing.

The change can be returned to planning for rewriting any time the user chooses.


# Build Lock

```yaml
id: b7n
```

[↑ Build](#build)

What keeps one change building at a time. [Build](#build) begins only on the user's approval of the plan; on that approval the agent takes the lock by writing the change file name into `changes/open/active.md`, reporting success — or, if the file already exists, stopping without touching it, since another change is already mid-build.

Releasing the lock deletes the file. A build that changed code keeps the lock even when handed back to planning; only an untouched one may release it, so unfinished work is never silently abandoned.

**See also**

- [Startup Scan](#startup-scan) — the lock is what tells a fresh session a build was interrupted.


# Conclude

```yaml
id: o4j
```

[↑ Change Lifecycle](#change-lifecycle)
[Archiving](#archiving)

The closing note, written only once the user confirms the build is done. It states where the change landed — not a story of how it got there.

Anything still [Held](#held) is released before Conclude begins — folded into the change, spun off as its own [parked change](#plan), or discarded by the user. Nothing is wrapped up with material outstanding.

It records only what the plan and the Log don't already convey: deviations, documents touched, surprises. When there's nothing to add, "Completed." is enough. It is capped at ~500 characters, excluding any changelog entry proposed with it: the agent counts them when surfacing the draft, reports the number, and past the cap asks the user to adjudicate.

Its mere presence is the marker that the change is finished.

**See also**

- [Enjoyment](#enjoyment) — artifact economy: why Conclude is capped short and never re-tells the journey.


# Archiving

```yaml
id: a9v
```

[↑ Conclude](#conclude)

Once the user approves the [Conclude](#conclude) note, the change leaves `changes/open/` for `changes/archive/`, losing any leading number and gaining the ISO date it concluded — `140-config-file-format.md` becomes `2026-05-14-config-file-format.md`. The [build lock](#build-lock) is then released, and the project is free for the next change.

A versioned project with substantive change also proposes a changelog entry with the draft note, added on the same approval. The [Maintenance](#maintenance) due after archival then follow: Tidy runs, Shape and Prose are offered. If the project map defines release steps, the agent asks whether it is time to run them, and if so offers the checks due before release first.


# Startup Scan

```yaml
id: x7t
```

[↑ Change-Management](#change-management)

What the agent does first in every session: orient from `changes/open/`. A project with no `map.md` and no `changes/` tree hasn't started yet — the agent [bootstraps](#bootstrapping) it before anything else. Otherwise it reads everything in `changes/open/` and places each change by where it sits in the [lifecycle](#change-lifecycle). The `active.md` lock names the change currently building, if any.

From that the agent announces whether it's planning or building, reports what's open, offers the [Backlog](#backlog) check, and proposes the next step — resuming an interrupted build, or picking up a parked change.

**Detail**

An interrupted build is recognised by `active.md` pointing at a change whose work is unfinished; the agent reads that change's [Log](#build) to recover context rather than restarting. A plan reopened mid-build says so in its [Log](#build) — with no [Conclusion](#conclude) yet, the change is back in planning.


# Bootstrapping

```yaml
id: b6t
```

[↑ Change-Management](#change-management)

How a project acquires its first map. A fresh install vendors only the method under `ndd/`, leaving the project itself empty — no `map.md`, no `changes/` tree — so the ordinary lifecycle has nothing to stand on. The agent detects this at the [Startup Scan](#startup-scan) and offers to bootstrap rather than proceeding as normal.

It scaffolds the [`changes/` tree](#change-management) and seeds the project map — `map.md` in the project root, distinct from the read-only method map at `ndd/ndd.md` — through discussion and any pre-existing documentation. How much to seed is the user's call: a single root node named for the system, or a fuller sketch — they may prefer to start capturing ideas before dwelling on setup.

Adopting an existing codebase adds a survey: the agent reads existing assets and proposes nodes one at a time per the [Engagement Rule](#engagement-rule). Progress is bite-sized at the user's pace and may be postponed. Reality-reflecting map edits need no active change (see [Edit Governance](#edit-governance)), though wrapping a migration in one can keep it systematic.


# Gates and Permissions

```yaml
id: g5m
```

[↑ Change-Management](#change-management)
[Approval](#approval)

Two rules gating what the agent may do without asking:

- **Approval** — what counts as the user saying yes.

- **Write permission** — what the agent may change at each point.

Writing is gated by phase and by an active change. During [Plan](#plan) the agent writes only inside `changes/`; project files are read-only. Writing a project file needs a change under [build](#build), recorded in `active.md`, unless the [map exemption](#edit-governance) applies. Reading anything is always allowed.

**Detail**

Git write operations — commit, push, branch, reset — always require explicit user instruction; the agent never does them on its own initiative.

Editing `changes/` (capturing a parked change, drafting phases) is likewise exempt from the active-change requirement.


# Approval

```yaml
id: k4d
```

[↑ Gates and Permissions](#gates-and-permissions)

Approval requires a clear affirmative given in response to the agent asking ("yes", "ok", "go ahead"). Silence, a tangent, or a reply that raises new questions is not approval. It only covers what was surfaced and no more: agreeing to draft prose is not approval of the prose.

How a draft is delivered is the user's choice — described in chat, or written into the file to be read in place. Delivery is never approval: however it arrives, the draft stands provisional until the user accepts or amends it.


# Keywords

```yaml
id: k9y
```

[↑ Change-Management](#change-management)
[Process Keyword](#process-keyword)
[Aside Keyword](#aside-keyword)

Two message prefixes that let the user trigger a small side-action without derailing the current work. The agent handles the aside, confirms in a line, and returns to what it was doing. There are two:

- [process](#process-keyword) captures an observation about the method itself;
- [aside](#aside-keyword) parks a **separate** proposal as its own draft change ([Intent](#intent) only).


# Process Keyword

```yaml
id: r4c
```

[↑ Keywords](#keywords)

A message starting with `process:` records an observation about the method or the agent's conduct — friction, a suggestion, something to revisit — without acting on it. The agent appends it to `changes/process-feedback.md`, confirms in a line, and carries on with whatever was under way.

**Detail**

The entry is dated and captures the observation plus any surrounding context (phase, active change, topic) that would otherwise be lost; the agent may rephrase for later readability. The file is append-only and created with a header if absent. It lives in the repository as an ordinary versioned file — not git-ignored — so the feedback is shared between collaborators; committing it stays a user action, like any git write.


# Aside Keyword

```yaml
id: y2f
```

[↑ Keywords](#keywords)

A message starting with `aside:` parks a topic for later without breaking the current flow: it becomes a fresh parked change in `changes/open/`, an [Intent](#intent) and nothing more, a proposal separate from whatever is under way. The agent acknowledges placement in a line and returns to what it was doing. Material belonging to the *current* change rather than a separate one is [Held](#held) instead.

**Detail**

An aside is never silently dropped.


# Maintenance

```yaml
id: t7v
```

[↑ NDD](#ndd)
[Tidy](#tidy)
[Shape](#shape)
[Prose](#prose)
[Consistency](#consistency)
[Rendering](#rendering)
[Backlog](#backlog)
[Sign-off](#sign-off)

The reviews the agent can run or offer, grouped by what they read: the tree, the text, the ideas, the code, the backlog, and the stamps. Every check is available on demand for an agreed scope; the *Trigger* column says where in the change cycle it is also run or offered. Only Tidy runs unprompted — the rest need the user's judgement, so they are offered and taken up or declined.

| Reads | Check | Looks for | Trigger |
|-------|-------|-----------|---------|
| The tree | [Tidy](#tidy) | Tree overview, ids, links and the size table — all mechanical | Runs after archival |
| The tree | [Shape](#shape) | Nodes to split or merge, a top-level division or child order that no longer fits | Offered after archival |
| The text | [Prose](#prose) | Nodes off the writing conventions or saying more than their idea needs | Offered after archival |
| The ideas | [Consistency](#consistency) | Contradictions, untreated competing concepts, redundancy, homeless concepts, ambiguous nodes | Offered before release |
| The code | [Rendering](#rendering) | Where the code and files no longer match the map, in either direction | Offered before release |
| The backlog | [Backlog](#backlog) | Parked changes gone stale, overlapping, superseded or out of order | Offered at Startup Scan |
| The stamps | [Sign-off](#sign-off) | Nodes due for a named stakeholder — fingerprint no longer matching their stamp, or no stamp at all | On request |

Deferring map upkeep for a stretch — an emergency fix, a push elsewhere — is safe because of this table: nothing is marked, each trigger point re-offers, and release gates the whole-map checks.


# Tidy

```yaml
id: u8k
```

[↑ Maintenance](#maintenance)

The mechanical housekeeping, run across the whole map once a change is archived. The agent needs no prompting and reports everything in one summary; anything it touches is a [correction](#engagement-rule), never a change of meaning.

- **Fixed, then reported**: the [tree overview](#map-structure) brought back in step with the navigation links; a missing scaffolding [id](#node-identity) or [navigation link](#navigation-links) added; a link re-pointed after a target renamed.

- **Reported only**: a table of nodes over the [size bound](#node-sizing), since splitting-versus-keeping is the user's call, made in [Shape](#shape).

- **Escalated**: anything a mechanical fix can't settle, such as a duplicated heading that needs a rename.


# Shape

```yaml
id: d4p
```

[↑ Maintenance](#maintenance)

A check on how the map is cut: whether the tree's divisions still match how the user thinks of the system.

It looks for:

- A node carrying more ideas than its heading promises, which should be split into children. Tidy's size table feeds this, and the user may decide an oversize node earns its length.

- Sibling nodes that say too little apart and should merge.

- The top-level division of the map no longer matching how the user thinks of the system.

- Child order that no longer reads as a natural sequence.


# Prose

```yaml
id: p2w
```

[↑ Maintenance](#maintenance)

A check on how nodes read, applied even where the tree is cut well.

It looks for:

- Prose deviating from the [writing style](#writing-style) conventions.

- A node saying more than its idea needs — wordy where the [size bound](#node-sizing) is only the mechanical symptom.


# Consistency

```yaml
id: k4c
```

[↑ Maintenance](#maintenance)

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

```yaml
id: r3n
```

[↑ Maintenance](#maintenance)

A check on whether what exists still reads as a rendering of the map. The agent compares an agreed scope — the whole map, or one area — against the code and files, and reports each place they disagree. Each disagreement is settled one way or the other: the map corrected to what exists, or the code corrected under a change.

It looks for:

- A node describing what is no longer there.

- Something built that no node describes.

- A mechanism the map tells one way and the code another.

- A node the code could have satisfied several ways — ambiguity seen from the code side, for the map to close.

It is the single-agent form of [Cross-Agent Falsifiability](#cross-agent-falsifiability). Because it reads the code it is the costliest check, and the catch-up when map upkeep has been deferred for a while.


# Backlog

```yaml
id: b7k
```

[↑ Maintenance](#maintenance)

A check on the parked changes in `changes/open/`, offered at the [Startup Scan](#startup-scan) once the open changes have been reported, since they have just been read. Each parked change is settled with the user: kept as it is, updated, renumbered, merged, or discarded.

It looks for:

- A change citing a node or change that no longer exists.

- A change the project has moved past — built by other means, or no longer wanted.

- Two changes that overlap and should merge.

- Numbers that no longer say what should come next — the leading numbers are the backlog's order, so the remedy is renumbering.


# Sign-off

```yaml
id: f2s
```

[↑ Maintenance](#maintenance)

A stakeholder approves the map a few nodes at a time. Each node can carry an [approval stamp](#approval-stamp) per person, recording when they approved it and a [fingerprint](#fingerprint) of the text they saw. On approval the agent writes a fresh stamp — scaffolding, so written and reported rather than negotiated.

Nothing is marked when a node changes. Drift is found by comparing: a node is *due* for a person when its fingerprint no longer matches their stamp, or it has none for them. A map with no stamps shows nothing, and the agent never adds one unprompted.

**See also**

- [Orient Then Focus](#orient-then-focus) — due nodes are summarised, then walked one at a time.
- [Node Sizing](#node-sizing) — re-approval is a re-read of one short node, which is what keeps it humane.


# Tooling

```yaml
id: g8l
```

[↑ NDD](#ndd)

The method needs no bespoke application — it rides generic markdown tooling. In an editor with a markdown language server (marksman, in Helix), the name-anchored [navigation links](#navigation-links) become jump-to-definition targets: `gd` walks the tree parent-to-child, and the symbol picker (Helix `Space+s`) lists every node by name for a direct jump anywhere. Nothing custom is required; the format is kept deliberately plain so richer surfaces stay cheap to build on top later.


# Standards

```yaml
id: s9d
```

[↑ NDD](#ndd)

Guidance for the code written by agents on user projects, distinct from the map spec that governs the *map*. NDD ships a set of **suggested** standards a project adopts, adapts, or ignores — installed as plain markdown under `ndd/standards/`, not folded into the map. This node is the index: an agent scans it to see what exists and opens only the guide a task touches. The code **Style** guide is an always-on default (deviate only when flagged and approved); the rest load on reference.

**Detail**

| Guide | Covers | When to load |
|-------|--------|--------------|
| `STYLE.md` | Core coding style | Always on |
| `RUST.md` | Rust addendum to Style | Writing Rust |
| `POS.md` | Python as a readable alternative to shell scripts for admin/small tasks | Writing a system-administration or small utility script |
| `VERSIONING.md` | Semver conventions | Prompted: project setup, changes accumulating, or a breaking change |
| `CHANGELOG.md` | Changelog format (dated or semver) | Drafting a changelog entry |


# Principles

```yaml
id: p4c
```

[↑ NDD](#ndd)
[Three Deaths](#three-deaths)
[Comprehension is an Activity](#comprehension-is-an-activity)
[Intent Memory](#intent-memory)
[Enjoyment](#enjoyment)
[Local Sufficiency](#local-sufficiency)
[Cross-Agent Falsifiability](#cross-agent-falsifiability)
[Orient Then Focus](#orient-then-focus)

The method's founding case. Agent-augmented development broke the old bundle where writing code and understanding it were one act — production no longer carries comprehension along. The method restores a deliberate comprehension-building activity, maintaining the map, and hands rendering to the agent. Because it works at the structural level, the map also surfaces logic bugs — wrong flows, missing cases, bad boundaries — before any code is written. Conceptual maintainability thus earns first-class standing alongside correctness, never the first thing sacrificed under deadline pressure. The principles below are the binding constraints every change answers to, and the home other nodes point at instead of restating a reason.


# Three Deaths

```yaml
id: d3t
```

[↑ Principles](#principles)

The three deaths the method's name refers to, each a way understanding is lost once agents write the code.

- **Specifications die** as documents when they sit off the critical path — unread, unmaintained, drifting into fiction.

- **Structural thinking dies** when the human no longer authors the codebase and the agent's output has nowhere to be reasoned about.

- **Comprehension dies** when the developer's role stops being architecturally fun, because understanding is sustained by engagement, not discipline.

The map is the countermeasure to all three, and the [Maintenance](#maintenance) are what keep it from the first.


# Comprehension is an Activity

```yaml
id: c8a
```

[↑ Principles](#principles)

No artifact substitutes for the activity of structural thinking itself. Reading a spec doesn't build the model; maintaining the map does — the deliberate construction that keeps the user's structural grasp growing as fast as agents produce code.


# Intent Memory

```yaml
id: q3v
```

[↑ Principles](#principles)

Code records what a system does, never why it is shaped that way. The reasoning behind a boundary or a trade-off lives in the author's head and leaves when they do. The map is where intent is remembered — prose that carries the why, so a decision survives past the moment and the person that made it.


# Enjoyment

```yaml
id: j2e
```

[↑ Principles](#principles)

Structural thinking must stay enjoyable — it's the part strong practitioners value, and a process that reduces the user to reviewing agent diffs destroys engagement. Engagement, not discipline, is what sustains comprehension over time: you keep understanding a system because staying in the structural thinking is rewarding, not by willpower. Enjoyment is a binding constraint, not a bonus.

Its corollary is **artifact economy**: every word in a change document or map node competes for the reader's attention, so bloat and duplication turn a dialogic activity with the agent into a wading exercise. Concision isn't style here, it's protection.


# Local Sufficiency

```yaml
id: s3l
```

[↑ Principles](#principles)
[Trees over Graphs](#trees-over-graphs)

Reasoning about one part must not require holding the rest in mind — the mind registering that working memory suffices is what makes a system feel manageable. Cross-cutting concerns are the enemy: when one fact has consequences everywhere, no local model is ever enough. The cure is to promote each into a first-class named object, referenced locally rather than left implicit.


# Trees over Graphs

```yaml
id: g6t
```

[↑ Local Sufficiency](#local-sufficiency)

A tree delivers local sufficiency for free: every node has one parent, one home, one context. Real domains have cross-cutting relations, but those are references between nodes, not extra parent edges — and complex internal behaviour (cycles, fan-out, retries) lives *inside* a node, not between them. The "peak tree", where a system's shape feels like a clean logical tree, is a real cognitive state; agents produce graph-shaped code from day one and skip past it, so the map preserves it deliberately.


# Cross-Agent Falsifiability

```yaml
id: f9x
```

[↑ Principles](#principles)

If the map is the source of truth, independent agents can render it — and differences between renderings test its quality. A good map renders consistently where it matters; a bad one doesn't, exposing abstraction leaks and model-vs-reality drift without the user reading code.

Full cross-rendering is expensive, kept for high-stakes moments. Its everyday forms are two [Maintenance](#maintenance) checks. The **ambiguity test** asks whether a fresh agent could build a node without guessing, and [Consistency](#consistency) applies it from the map side. [Rendering](#rendering) tests the one rendering that exists against the map from the code side.


# Orient Then Focus

```yaml
id: r5i
```

[↑ Principles](#principles)

**Attention dies under overwhelm.** So whenever the agent has a set of items to present — a worklist, open changes, map nodes to edit — it surfaces them in summary (e.g. bullet points), so the user is oriented, then works through it one item at a time, holding the stack itself.

The set alone is more than anyone can hold, but item-by-item alone would leave the user unsure where they are. Together they give orientation and prevent the agent from advancing faster than the user can follow. Each item is introduced by name and by its place in the set, such as *3 of 7*. A message asks at most one question, ending where it asks it.

The focused items are where comprehension is built; skip that and the user's role degrades to approving map diffs instead of code diffs — a better level of abstraction, but still passive review.

**See also**

- [Engagement Rule](#engagement-rule) — the map-edit instance: nodes named up front, then settled one by one.
- [Enjoyment](#enjoyment) — attention lost to overwhelm is how comprehension stops being sustained by engagement.
