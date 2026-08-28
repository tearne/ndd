# Non-Dead Design

```yaml
id: a3k
```

[META](#meta)
[Principles](#principles)
[Specification](#specification)
[Change-Management](#change-management)
[Tooling](#tooling)
[Standards](#standards)

Non-Dead Design (**NDD**) aims to improve knowledge management for agentic software development. The name reflects three deaths it seeks to prevent.

- **Specifications die** as documents when they sit off the critical path — unread, unmaintained, drifting into fiction.
- **Structural thinking dies** when the human no longer authors the codebase and the agent's output has nowhere to be reasoned about.
- **Comprehension dies** when the developer's role stops being architecturally fun, because understanding is sustained by engagement, not discipline.

The map is the one artefact that keeps all three alive: a conceptual **map** of the system, acting as the hub for specification and change management rather than a document off to one side. The method itself is expressed as a map.

- **Principles** — the founding rationale in more detail.
- **Specification** — the conceptual map as the primary comprehension artefact.
- **Change-Management** — how the spec evolves, through a change lifecycle and explicit gates.
- **Tooling** — the generic markdown tooling the format is designed to exploit.
- **Standards** — suggested coding standards NDD ships for the code agents write on a project.


# META

```yaml
id: mt7
```

[Non-Dead Design](#non-dead-design)
[Contents](#contents)
[Rationale](#rationale)
[Distribution](#distribution)

Orientation for anyone landing here without knowing the format. This document is a conceptual **map**: a tree of named nodes, each a heading with a short description and links to its parent and children. Follow the links to walk the tree; the Contents node sketches the whole shape at a glance. Nodes gathered under META describe the map or product itself rather than a domain concept or specification. Contents — the tree overview — is the one mandatory meta-node; a product Rationale, a Distribution account, and a domain Glossary are optional.


# Contents

```yaml
id: ct5
```

[META](#meta)

```
Non-Dead Design
├ META
│ ├ Contents
│ ├ Rationale
│ └ Distribution
├ Principles
│ ├ Comprehension is an Activity
│ ├ Intent Memory
│ ├ Enjoyment
│ ├ Local Sufficiency
│ │ └ Trees over Graphs
│ ├ Cross-Agent Falsifiability
│ └ Interaction Grain
├ Specification
│ ├ Node
│ │ ├ Node Identity
│ │ ├ Navigation Links
│ │ ├ Node Sections
│ │ │ └ Callouts
│ ├ Map Structure
│ ├ Node Sizing
│ ├ Writing Style
│ │ ├ Conceptual Writing
│ │ └ Formatting
│ └ Edit Governance
│   ├ Sync Rule
│   ├ Engagement Rule
│   └ Map Maintenance
│     ├ Conceptual Drift
│     └ Consistency Upkeep
├ Change-Management
│ ├ Change Lifecycle
│ │ ├ Plan
│ │ │ ├ Intent
│ │ │ └ Approach
│ │ ├ Build
│ │ └ Conclude
│ ├ Cadences
│ ├ Startup Scan
│ ├ Bootstrapping
│ ├ Gates and Permissions
│ └ Keywords
│   ├ Process Keyword
│   └ Aside Keyword
├ Tooling
└ Standards
```


# Rationale

```yaml
id: r9k
```

[META](#meta)

Why the method exists: its founding rationale is the [Principles](#principles) subtree, kept first-class among the domain concerns rather than restated here.


# Distribution

```yaml
id: d5v
```

[META](#meta)

To use NDD in a project the consumer clones the NDD repo and runs its `opt-in.py` from their own project (e.g. `../ndd/opt-in.py`); the idempotent installer vendors NDD under `ndd/` and wires the agent entry files, leaving the consumer's own map and changes untouched. `main` is the single moving edge for NDD, no cut releases; the shipped changelog names the current version, and the previous map is kept alongside as the agent's migration diff.

**Detail**

`opt-in.py` is a POS-style `uv` script (`uv` required) that copies the method from its own checkout; upgrading is `git pull` then re-run. It:
- vendors `ndd.md` (from the checkout's `map.md`), `BOOTSTRAP.md`, `CHANGELOG.md` and the whole `standards/` directory into `ndd/`;
- backs up a changed `ndd.md` as `ndd.prev.md`;
- writes `CLAUDE.md`/`AGENTS.md` only when absent or matching (warns otherwise); and
- gitignores `ndd/`, the entry files and `.claude/`.

It refuses to run if the target `ndd/` resolves to its own source directory, guarding against vendoring directly into the checked out NDD git repository; every other target is allowed, which enables this repo to dogfood by self-vendoring. `opt-in.py --version` reads the top `CHANGELOG.md` heading (semver + date).


# Specification

```yaml
id: sp1
```

[Non-Dead Design](#non-dead-design)
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

[Specification](#specification)
[Node Identity](#node-identity)
[Navigation Links](#navigation-links)
[Node Sections](#node-sections)

A node represents **one** concept and includes a heading, an agent-maintained scaffolding block holding its metadata, name-anchored navigation links to its parent and children, and terse prose leading with the mental picture. Optional *Detail* and *See also* sections follow.

The format is a strict superset of a plain-markdown section — strip the scaffolding and links and what remains is an ordinary heading with prose, so a map renders and navigates as plain markdown in any tool.

**See also**

- [Trees over Graphs](#trees-over-graphs) — nodes form the tree; a concept's complexity is kept inside its node rather than spread across links.


# Change-Management

```yaml
id: cm4
```

[Non-Dead Design](#non-dead-design)
[Change Lifecycle](#change-lifecycle)
[Cadences](#cadences)
[Startup Scan](#startup-scan)
[Bootstrapping](#bootstrapping)
[Gates and Permissions](#gates-and-permissions)
[Keywords](#keywords)

How the spec evolves: a change is drafted in `changes/`, moves through a lifecycle under explicit user gates, and updates the map as reality catches up — then it's archived.


# Node Identity

```yaml
id: w9c
```

[Node](#node)

A node's name can change; its identity can't. The identity is a small immutable token in the yaml scaffolding block which survives node renames and moves. It exists so that anything pointing to the node stays attached.

> [!IMPORTANT] Navigation uses node names, not the ID, so ordinary markdown tooling works and the ID is free to be meaningless.

**Detail**

The **scaffolding block** is fenced YAML directly under the heading containing metadata — today just `id`. It's agent-maintained, like the nav links, and a reader ignores it. The `id:` key is map-unique, lowercase alphanumeric, three or more characters (e.g. `k7f`) - a token rather than a readable slug to avoid edit or link temptation. A user may hand-draft a node without a block; the agent offers to add one when it next reviews the node, so identity is never silently missing.

**See also**

- [Consistency Upkeep](#consistency-upkeep) — proposing a missing id on review is a standing obligation.


# Navigation Links

```yaml
id: b3q
```

[Node](#node)

The tree lives in the links, not in a separate index or the file layout. Each node names its one parent and each of its children, so following links *is* walking the tree. Siblings aren't listed directly — you reach them by stepping up to the parent, whose child links name them all.

> [!IMPORTANT] Links resolve by node name, never by ID, so ordinary markdown tooling navigates them and a node's identity token never appears as a link target.

**Detail**

The parent link is listed first and omitted only by the root; every other node has exactly one. Link text is the target node's actual name, so an editor with a markdown LSP (e.g. marksman) jumps straight there with `gd`. Because links are name-anchored, renaming a node is a mechanical re-point of the links that named it, and the ID never appears in a link. A user may omit links while drafting; the agent proposes them on review.

Child order is the parent's to arrange; when its children form a natural reading sequence, order them to reflect it.

Because links resolve by name, every heading must be unambiguous across the whole map — a duplicated heading collides as an anchor and breaks navigation.

**See also**

- [Trees over Graphs](#trees-over-graphs) — links encode the one-parent tree that keeps navigation walkable.
- [Consistency Upkeep](#consistency-upkeep) — the agent proposes missing links and watches child order as standing obligations.


# Node Sections

```yaml
id: s8r
```

[Node](#node)
[Callouts](#callouts)

The main user-facing parts of a node are each optional and include, in a fixed order: **prose**, **Callouts**, **Detail**, and **See also**. Prose is the mental picture and usually the only part the user must read, but even it can be dropped — a node may carry only *Detail*, for instance. A node using none of these is just a heading: an ordinary markdown section.

**Detail**

*Callouts* flag a load-bearing point and get their own child node. *Detail* is marked with bold `**Detail**` and holds implementation-level precision the user can stop before, such as parameters, thresholds, and algorithms. *See also* is marked with bold `**See also**` and lists cross-cutting references that aren't parent or child, each saying why the relationship matters.


# Callouts

```yaml
id: c5k
```

[Node Sections](#node-sections)

A callout is a "don't skim this" flag on a point the prose already makes. It marks the load-bearing moments where skimming would lose the reader, such as a design trade-off, a non-obvious assumption, or a constraint that shapes the whole node. The prose still carries the meaning; the callout only raises a hand.

**Detail**

Rendered as a `> [!IMPORTANT]` blockquote. Used sparingly — reserved for points that genuinely reshape understanding, never as a highlighter for every notable fact.


# Map Structure

```yaml
id: m6x
```

[Specification](#specification)

The map's shape is shown at a glance by a **tree overview** — a box-drawing sketch of the whole node tree — held in the [Contents](#contents) meta-node. Nodes not yet written are marked `(TODO)`, so the intended shape is visible before the content is. The rendering is only a convenience: the real tree is encoded in the navigation links, and the overview is kept in step with them.

**Detail**

The overview is a fenced code block using box-drawing characters. A map is one file by default, splitting across several (linked by relative paths) only when size makes one file unwieldy; navigation works the same either way.

The root defaults to the project's name, preferring a term that carries domain information over a generic label like "Application". When that name clashes with a prominent internal node, disambiguate with whichever reads best: a scoping term for the root, a suffix, a parenthetical, or a more specific name for the internal node.

**See also**

- [Trees over Graphs](#trees-over-graphs) — why the sketched shape is a tree, not a general graph.
- [Consistency Upkeep](#consistency-upkeep) — keeping this overview in step with the navigation links is a standing obligation.


# Node Sizing

```yaml
id: z9p
```

[Specification](#specification)

Keep nodes small and focussed on one concept. The rough upper bound for size is around 800 characters, but the real test is felt: if a node starts wanting sub-sections, it's outgrown one concept and should split into children.

**Detail**

Character counts exclude tables and diagrams. When a node runs over, the agent flags it rather than silently trimming, so splitting-versus-keeping stays the user's call.

**See also**

- [Local Sufficiency](#local-sufficiency) — why nodes stay small: a reader must grasp one node from the node alone.
- [Consistency Upkeep](#consistency-upkeep) — flagging an oversize node is a standing obligation.


# Writing Style

```yaml
id: p4h
```

[Specification](#specification)
[Conceptual Writing](#conceptual-writing)
[Formatting](#formatting)

How map prose is written, so nodes stay readable and durable. Two sides:

- Conceptual Writing: what the prose *says*

- Formatting: how it's typeset

**See also**

- [Consistency Upkeep](#consistency-upkeep) — holding prose to these conventions is a standing obligation.


# Conceptual Writing

```yaml
id: h3v
```

[Writing Style](#writing-style)

A handful of habits shape how a node reads, and one trap to avoid:

- **Lead with the mental picture** before any implementation detail.

- **Name the boxes before explaining them** — say "there are three mechanisms: A, B, C" and then give each its own node or bullet point.

- **Flow sentences unbroken** — prefer keeping a sentence whole over interrupting it. A parenthetical em-dash pair reads fine when the aside is one short clause, but once the middle grows long and multi-part the reader loses the opening before the sentence resumes: split it into separate sentences instead.

- **Bullet a set the reader will scan** — when a node names a small set of parts, options, or questions, list them as bullets rather than an in-sentence enumeration, so each is scannable and individually referenceable.

- Don't **couple to code structure**: prose may name a technical concept when load-bearing, but the map tracks the user's model, not the code's shape — so it shouldn't break when code is refactored.


# Formatting

```yaml
id: f2n
```

[Writing Style](#writing-style)

Typographic conventions for map prose.

- Write each paragraph as one continuous line with no hard wraps, so it reflows under soft-wrap.

- Separate bullet points with a blank line when they run long enough to wrap; short single-line points don't need it.

- Two blank lines before a node title, so node boundaries stand out when scrolling a single-file map.

- Use *italics* when a sentence refers to a named section or element (*Callouts*, *Detail*, *See also*), and reserve **bold** for introducing a term of art on first use, so references don't read as competing sub-headings.

- Prefer an inline cross-reference link when a sentence already names another node in passing; reserve a *See also* entry for a standalone pointer the prose doesn't already invoke, each with its own reason it matters.


# Edit Governance

```yaml
id: e7m
```

[Specification](#specification)
[Sync Rule](#sync-rule)
[Engagement Rule](#engagement-rule)
[Map Maintenance](#map-maintenance)

The rules for changing the artefact itself. Three questions govern every edit:

- *what* may be written — the [Sync Rule](#sync-rule);

- *how* the change is made — the [Engagement Rule](#engagement-rule);

- *when* a node is due for work — [Map Maintenance](#map-maintenance).

Because these edits describe reality rather than intent, they fall outside the active-change requirement: no open change is needed, and they may happen at any time. That exemption lifts only the active-change constraint; the [Engagement Rule](#engagement-rule)'s per-node negotiation for map updates still applies.

**See also**

- [Gates and Permissions](#gates-and-permissions) — the active-change requirement this exemption stands against.


# Sync Rule

```yaml
id: s5y
```

[Edit Governance](#edit-governance)

The map tracks reality. It may be edited to match reality at any time, but never *ahead* of it: an edit describing work not yet built waits until it is. Pending work is held as parked changes in `changes/`, off the map, so the map stays a record of what exists. In a code change that means map catch-up waits until the change is concluded, then follows as its own per-node negotiation.


# Engagement Rule

```yaml
id: n3g
```

[Edit Governance](#edit-governance)

Every map edit is negotiated with the user, one node at a time — never silent, never in bulk. When a change touches several nodes they are named up front and settled one by one. Pitch each prompt to what the edit changes: a comprehension check like "does that fit your mental model?" when it reshapes the picture, a lighter or batched confirmation when it's mechanical.

**See also**

- [Interaction Grain](#interaction-grain) — why edits go one node at a time: the user's engagement can't be outrun.


# Map Maintenance

```yaml
id: t7v
```

[Edit Governance](#edit-governance)
[Conceptual Drift](#conceptual-drift)
[Consistency Upkeep](#consistency-upkeep)

When a node is due for work. Map upkeep has two faces:

- **Conceptual Drift** — whether the structure still fits the user's model, a matter of judgement.

- **Consistency Upkeep** — whether the artefact stays internally consistent, a standing checklist the agent runs without prompting.


# Conceptual Drift

```yaml
id: d4p
```

[Map Maintenance](#map-maintenance)

Watch for the signals that a node has drifted from its job, such as:

- It starts wanting sub-sections — split it into children.

- It has grown verbose — cut hard, push precision into *Detail*.

- A new concept has no natural home — the decomposition needs rethinking, not a misc bucket.

- The top-level boxes stop matching how the user thinks — restructure, because the map follows the user's model, not the code's.

**Detail**

A recurring check is the *ambiguity test* (see [Cross-Agent Falsifiability](#cross-agent-falsifiability)), run over each node in the area you're touching; a node it flags is a map-quality gap, not an implementation problem.


# Consistency Upkeep

```yaml
id: u8k
```

[Map Maintenance](#map-maintenance)

The standing mechanical obligations the agent keeps up without being asked, each defined where it lives:

- Keep the [tree overview](#map-structure) in step with the navigation links.

- Propose a scaffolding [id](#node-identity) and [navigation links](#navigation-links) on any node reviewed without them.

- Flag a node that outgrows its [size bound](#node-sizing) rather than silently trimming.

- Hold prose to the [writing style](#writing-style) conventions.

- Watch [child order](#navigation-links) for a natural reading sequence.

This node indexes; each linked node holds the detail.


# Cadences

```yaml
id: e3n
```

[Change-Management](#change-management)

Each change runs at one of three cadences. They differ only in the shape of the [Plan](#plan) — [Build](#build) and [Conclude](#conclude) are the same whichever is chosen. The agent proposes one after Intent is approved — default **Formal** — and the user confirms.

| Cadence | Plan structure |
|---------|----------------|
| **Formal** | Intent → Approach → a task checklist |
| **Explore** | Intent → Approach → topics + a *done-when* |
| **Wander** | Intent only |

- **Formal** is the default, for work that benefits from explicit decisions and step-by-step tracking.

- **Explore** suits work where depth and coverage matter more than a fixed step list.

- **Wander** is for work too small or too fluid to plan; the agent flags topic drift and can offer to flush.

**Detail**

A **task checklist** is discrete tasks, each an atomic outcome ticked off as it lands. **Topics** are areas to work rather than steps to complete, closed by a single *done-when* condition instead of tick-boxes.

Cadence can change mid-flight: pause, rewrite the change document into the target cadence's shape, resume. A discarded Wander change is deleted rather than archived, and its name may be updated to reflect where the work actually ended up.


# Change Lifecycle

```yaml
id: l5g
```

[Change-Management](#change-management)
[Plan](#plan)
[Build](#build)
[Conclude](#conclude)

A change is a single markdown document that advances through three phases:

1. **[Plan](#plan)** — the write-only phase that produces the change document; the [cadence](#cadences) sets its internal shape.
2. **[Build](#build)** — doing the work against whatever the Plan produced, the same whichever cadence made it.
3. **[Conclude](#conclude)** — a retrospective once the work is accepted.

Each phase is drafted into the document, then surfaced for the user's explicit approval before the next begins.

The document is the single carrier of state: where a change sits is read from what it contains, not from any status field. Chat carries only disclosures and summaries; the drafted text lives in the document.

The Plan → Build boundary is the load-bearing gate: project files stay untouched until a plan is approved.


# Plan

```yaml
id: v3d
```

[Change Lifecycle](#change-lifecycle)
[Intent](#intent)
[Approach](#approach)

During this phase project files outside of `changes/` remain read-only: research and reasoning that produces the change document touches nothing else. It builds up in parts, each drafted then surfaced for approval before the next, culminating in the **worklist** that [Build](#build) executes. Which parts a change has is set by its [cadence](#cadences).

A Plan need not be fully formed to exist. A change may sit at any degree of formation — from an [Intent](#intent)-only draft just parked via [aside](#aside-keyword), up to a complete worklist awaiting approval. These degrees aren't formal sub-stages, only how far the document has been drafted; but the [Startup Scan](#startup-scan) may name them to place an open change — in terms such as *parked at its Intent*, *mid-approach*, or *awaiting a worklist*.

The worklist lists only the actions to take, not the reasons for them — those belong in the [Approach](#approach). A task that touches a mapped concept names the node rather than the file that implements it, keeping the plan anchored to the map.

**Detail**

Before surfacing the worklist the agent prunes it against fixed rules: one task per atomic outcome, no restated "why", no obvious sub-steps, no ceremony tasks (a bare "review" or "double-check") unless they mark a real gate, and no file paths the task name already implies.


# Intent

```yaml
id: i8b
```

[Plan](#plan)

The opening part: why the change is needed expressed in domain language, not how it will be delivered unless relevant to the requirement. Kept brief and requiring user approval before anything else proceeds. For a [Wander](#cadences) change the Intent is the whole plan.

An Intent can also be captured and **parked** — left on its own in `changes/open/` until someone picks it up and the lifecycle resumes. A parked Intent may optionally reference the map node(s) it concerns as *name (id)*: the name to navigate to now, the id in brackets to stay recoverable if the name later changes. Nothing requires it, though.

**Detail**

Intent is capped short (a ~500-character soft trigger); past that the agent flags borderline material and asks the user to adjudicate rather than surfacing it as final.


# Approach

```yaml
id: a2r
```

[Plan](#plan)

How the change will be carried out, written as a list of decisions and their reasons — not a narrative and not a file-by-file rehearsal, which belongs to the [worklist](#plan). Each decision earns a line only if it carries a reason; self-evident choices need no subsection. Skipped entirely by [Wander](#cadences).

Alongside it sits an **Unresolved** list: the open items the agent can't settle alone, each pointing at the part of the Approach it affects. The agent surfaces the full list in chat so the user can see everything outstanding, then walks through them — for anything non-trivial, one at a time ("4 unresolved items […]. First one: …") rather than asking the user to address them all at once. Answers fold back into the prose and the list shrinks. An empty list means the Approach is ready for approval.

**Detail**

The agent re-reads and prunes its own draft before surfacing — anything not carrying a decision-and-reason comes out — then a ~1000-character soft trigger flags borderline material for the user to adjudicate. Once the worklist is written the Unresolved section is deleted; its absence is the signal that the Approach is settled.

**See also**

- [Enjoyment](#enjoyment) — artifact economy: why the Approach is pruned to decisions-and-reasons rather than left as narrative.


# Build

```yaml
id: u6k
```

[Change Lifecycle](#change-lifecycle)
[Conclude](#conclude)

Executing the approved plan against the real project files. The agent follows the plan rather than redesigning mid-flight — working through it in whatever shape it took, marking progress as each piece lands and posting concise updates without pausing step by step. It interrupts only when something warrants it — a surprise, an ambiguity, or a plan that turns out wrong. If the path forward is unclear the agent stops, records the blocker, and hands back rather than improvising.

Only one change builds at a time, held by a lock. Throughout, the agent keeps a running **Log** at the foot of the document — a terse record of the unexpected (surprises, deviations, blockers, partial progress), so a resuming session knows what the plan alone doesn't convey. Routine execution going to plan needs no entry.

**Detail**

The lock is `changes/open/active.md`, naming the one change under build; if it already exists, stop. On entering Build a versioned project agrees a bump kind, and every later hand-back for testing bumps patch. If the user later agrees the Plan needs revisiting, the agent writes a **Feedback** block: its status (implemented / partial / not), notes on what to reconsider, and any documentation impact. Writing it returns the change to planning. A build that changed code keeps the lock even when handed back; only an untouched one may release it.


# Conclude

```yaml
id: o4j
```

[Build](#build)

The closing note, written only once the user confirms the build is done. It states where the change landed — not a story of how it got there.

Any [aside](#aside-keyword) still open from the build is settled before Conclude begins; nothing is wrapped up with asides outstanding.

It records only what the plan and the Log don't already convey: deviations, documents touched, surprises. When there's nothing to add, "Completed." is enough.

If the change touched a mapped concept, its map catch-up follows here — and runs as its own per-node negotiation under the [Engagement Rule](#engagement-rule), never silently edited during conclusion.

A [Wander](#cadences) change has no Approach, but its Build [Log](#build) already carries what happened, so Conclude still just names the landing point — and may rename the change to match where the work ended up.

Its mere presence is the marker that the change is finished.

**Detail**

Conclude is capped short (a ~500-character soft trigger); past that the agent flags borderline material and asks the user to adjudicate rather than surfacing it as final.

For a versioned project with substantive change the draft also proposes a changelog entry. On the user's approval the change is archived to `changes/archive/` (prefixed `YYYY-MM-DD-`), the `active.md` lock is removed, and any approved changelog entry is added.

**See also**

- [Enjoyment](#enjoyment) — artifact economy: why Conclude is capped short and never re-tells the journey.


# Startup Scan

```yaml
id: x7t
```

[Change-Management](#change-management)

What the agent does first in every session: orient from `changes/open/`. A project with no `map.md` and no `changes/` tree hasn't started yet — the agent [bootstraps](#bootstrapping) it before anything else. Otherwise it reads everything in `changes/open/` and places each change by where it sits in the [lifecycle](#change-lifecycle): still in [Plan](#plan), formed anywhere from a just-parked [Intent](#intent) to a worklist awaiting approval, or under [build](#build). The `active.md` lock names the change currently building, if any.

From that the agent announces whether it's planning or building, reports what's open, and proposes the next step — resuming an interrupted build, or picking up a parked Intent.

**Detail**

An interrupted build is recognised by `active.md` pointing at a change whose work is unfinished; the agent reads that change's [Log](#build) to recover context rather than restarting. A change carrying [Feedback](#build) but no [Conclusion](#conclude) has been handed back to planning and needs replanning.


# Bootstrapping

```yaml
id: b6t
```

[Change-Management](#change-management)

How a project acquires its first map. A fresh install vendors only the method under `ndd/`, leaving the project itself empty — no `map.md`, no `changes/` tree — so the ordinary lifecycle has nothing to stand on. The agent detects this at the [Startup Scan](#startup-scan) and offers to bootstrap rather than proceeding as normal.

It scaffolds the missing pieces and seeds the project map — `map.md` in the project root, distinct from the read-only method map at `ndd/ndd.md` — through discussion and any pre-existing documentation. How much to seed is the user's call: a single root node named for the system, or a fuller sketch — they may prefer to start capturing ideas before dwelling on setup.

Adopting an existing codebase adds a survey: the agent reads existing assets and proposes nodes one at a time per the [Engagement Rule](#engagement-rule). Progress is bite-sized at the user's pace and may be postponed. Reality-reflecting map edits need no active change (see [Edit Governance](#edit-governance)), though wrapping a migration in one can keep it systematic.


# Gates and Permissions

```yaml
id: g5m
```

[Change-Management](#change-management)

The rules that gate what the agent may do without asking. Two kinds: **approval** — what counts as the user saying yes — and **write permission** — what the agent may change at each point.

Approval is only a clear affirmative given in direct response to the agent's ask ("yes", "ok", "go ahead"). Silence, a tangent, or a reply that raises new questions is not approval.

Writing is gated by phase and by an active change. During [Plan](#plan) the agent writes only inside `changes/`; project files are read-only. Writing a project file needs a change under [build](#build), recorded in `active.md`. Reading anything is always allowed.

**Detail**

Git write operations — commit, push, branch, reset — always require explicit user instruction; the agent never does them on its own initiative. Editing `changes/` (capturing a parked Intent, drafting phases) is exempt from the active-change requirement, as is editing the map to describe existing reality.


# Keywords

```yaml
id: k9y
```

[Change-Management](#change-management)
[Process Keyword](#process-keyword)
[Aside Keyword](#aside-keyword)

Two message prefixes that let the user trigger a small side-action without derailing the current work. The agent handles the aside, confirms in a line, and returns to what it was doing. There are two:

- [process](#process-keyword) captures an observation about the method itself;
- [aside](#aside-keyword) parks a topic in a draft change ([Intent](#intent) only) for later.


# Process Keyword

```yaml
id: r4c
```

[Keywords](#keywords)

A message starting with `process:` records an observation about the method or the agent's conduct — friction, a suggestion, something to revisit — without acting on it. The agent appends it to `changes/process-feedback.md`, confirms in a line, and carries on with whatever was under way.

**Detail**

The entry is dated and captures the observation plus any surrounding context (phase, active change, topic) that would otherwise be lost; the agent may rephrase for later readability. The file is append-only and created with a header if absent. It lives in the repository as an ordinary versioned file — not git-ignored — so the feedback is shared between collaborators; committing it stays a user action, like any git write.


# Aside Keyword

```yaml
id: y2f
```

[Keywords](#keywords)

A message starting with `aside:` parks a topic for later without breaking the current flow. The agent dispatches it one of two ways, by scope: a topic independent of the current work becomes a fresh parked [Intent](#intent) in `changes/open/`; a topic within an in-progress change is appended to an **Asides** subsection at the foot of that change document. When genuinely unsure which, the agent asks. Either way it acknowledges placement in a line and returns to what it was doing.

**Detail**

A parked Intent from an aside may carry the optional node reference an [Intent](#intent) allows. In-proposal asides raised during planning are folded in as planning reaches the part they touch. Those raised during build wait in the Asides subsection and must be settled before [Conclude](#conclude) begins: the agent surfaces any outstanding ones and the user decides each — fold in, spin off as its own parked Intent, or discard. An aside is never silently dropped.


# Tooling

```yaml
id: g8l
```

[Non-Dead Design](#non-dead-design)

The method needs no bespoke application — it rides generic markdown tooling. In an editor with a markdown language server (marksman, in Helix), the name-anchored [navigation links](#navigation-links) become jump-to-definition targets: `gd` walks the tree parent-to-child, and the symbol picker (Helix `Space+s`) lists every node by name for a direct jump anywhere. Nothing custom is required; the format is kept deliberately plain so richer surfaces stay cheap to build on top later.


# Standards

```yaml
id: s9d
```

[Non-Dead Design](#non-dead-design)

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

[Non-Dead Design](#non-dead-design)
[Comprehension is an Activity](#comprehension-is-an-activity)
[Intent Memory](#intent-memory)
[Enjoyment](#enjoyment)
[Local Sufficiency](#local-sufficiency)
[Cross-Agent Falsifiability](#cross-agent-falsifiability)
[Interaction Grain](#interaction-grain)

The method's founding case. Agent-augmented development broke the old bundle where writing code and understanding it were one act — production no longer carries comprehension along. The method restores a deliberate comprehension-building activity, maintaining the map, and hands rendering to the agent. Because it works at the structural level, the map also surfaces logic bugs — wrong flows, missing cases, bad boundaries — before any code is written. Conceptual maintainability thus earns first-class standing alongside correctness, never the first thing sacrificed under deadline pressure. The principles below are the binding constraints every change answers to, and the home other nodes point at instead of restating a reason.


# Comprehension is an Activity

```yaml
id: c8a
```

[Principles](#principles)

No artifact substitutes for the activity of structural thinking itself. Reading a spec doesn't build the model; maintaining the map does — the deliberate construction that keeps the user's structural grasp growing as fast as agents produce code.


# Intent Memory

```yaml
id: q3v
```

[Principles](#principles)

Code records what a system does, never why it is shaped that way. The reasoning behind a boundary or a trade-off lives in the author's head and leaves when they do. The map is where intent is remembered — prose that carries the why, so a decision survives past the moment and the person that made it.


# Enjoyment

```yaml
id: j2e
```

[Principles](#principles)

Structural thinking must stay enjoyable — it's the part strong practitioners value, and a process that reduces the user to reviewing agent diffs destroys engagement. Engagement, not discipline, is what sustains comprehension over time: you keep understanding a system because staying in the structural thinking is rewarding, not by willpower. Enjoyment is a binding constraint, not a bonus.

Its corollary is **artifact economy**: every word in a change document or map node competes for the reader's attention, so bloat and duplication turn a dialogic activity with the agent into a wading exercise. Concision isn't style here, it's protection.


# Local Sufficiency

```yaml
id: s3l
```

[Principles](#principles)
[Trees over Graphs](#trees-over-graphs)

Reasoning about one part must not require holding the rest in mind — the mind registering that working memory suffices is what makes a system feel manageable. Cross-cutting concerns are the enemy: when one fact has consequences everywhere, no local model is ever enough. The cure is to promote each into a first-class named object, referenced locally rather than left implicit.


# Trees over Graphs

```yaml
id: g6t
```

[Local Sufficiency](#local-sufficiency)

A tree delivers local sufficiency for free: every node has one parent, one home, one context. Real domains have cross-cutting relations, but those are references between nodes, not extra parent edges — and complex internal behaviour (cycles, fan-out, retries) lives *inside* a node, not between them. The "peak tree", where a system's shape feels like a clean logical tree, is a real cognitive state; agents produce graph-shaped code from day one and skip past it, so the map preserves it deliberately.


# Cross-Agent Falsifiability

```yaml
id: f9x
```

[Principles](#principles)

If the map is the source of truth, independent agents can render it — and differences between renderings test its quality. A good map renders consistently where it matters; a bad one doesn't, exposing abstraction leaks and model-vs-reality drift without the user reading code.

Full cross-rendering is expensive, kept for high-stakes moments; the everyday form is the **ambiguity test** — could a fresh agent build this node without guessing? — asked freely during planning or maintenance.


# Interaction Grain

```yaml
id: r5i
```

[Principles](#principles)

The agent must never advance the map faster than the user can engage with it. Every edit is negotiated one node at a time — the agent proposes, the user decides. Skip this and the user's role degrades to approving map diffs instead of code diffs: a better level of abstraction, but still passive review. Per-node negotiation is what turns map maintenance into comprehension-building, which is the whole point.
