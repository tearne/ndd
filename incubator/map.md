# Unified Map Method

```yaml
id: a3k
```

[Specification](#specification)
[Change-Management](#change-management)
[Tooling](#tooling)

The specification is the primary artefact. A navigable map of concepts — structured the way the user thinks, not the way code is organised — is what the user builds and maintains to hold the system's shape; agents render it into code. Maintaining that map *is* the comprehension-building activity, and it is also where change is reasoned about. This method unifies the two: the same map that carries understanding is the surface on which change is planned and tracked.

> [!IMPORTANT] "Unified Map Method" is a working name only; the real name is still open. The root carries a stable id, so choosing the name later is a rename that keeps the node's identity intact.

Three top-level concerns:

- **Specification** — the conceptual map as the primary comprehension artefact.
- **Change-Management** — how the spec evolves, through a change lifecycle and explicit gates.
- **Tooling** — the generic markdown tooling the format is designed to exploit.

```
Unified Map Method
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
├ Change-Management
│ ├ Cadences
│ ├ Change Lifecycle
│ │ ├ Plan
│ │ │ ├ Intent
│ │ │ └ Approach
│ │ ├ Build
│ │ └ Conclude
│ ├ Startup Scan
│ ├ Gates and Permissions
│ └ Keywords
│   ├ Process Keyword
│   └ Aside Keyword
└ Tooling
```

**See also**

- [PRINCIPLES.md](PRINCIPLES.md) — the founding rationale (comprehension as an activity) this method embodies.

# Specification

```yaml
id: sp1
```

[Unified Map Method](#unified-map-method)
[Node](#node)
[Map Structure](#map-structure)
[Node Sizing](#node-sizing)
[Writing Style](#writing-style)
[Edit Governance](#edit-governance)

The conceptual map is the primary artefact. It holds the system's shape as a tree of concepts, structured the way the user thinks rather than how code is organised. Maintaining it is the comprehension-building activity; agents render it into code. Everything else in the method — how it changes, how it's viewed — serves this map.

The map's unit is the **Node**.

# Node

```yaml
id: nd1
```

[Specification](#specification)
[Node Identity](#node-identity)
[Navigation Links](#navigation-links)
[Node Sections](#node-sections)

A node represents **one** concept and includes a heading, an agent-maintained scaffolding block holding its metadata, name-anchored navigation links to its parent and children, and terse prose leading with the mental picture. Optional **Detail** and **See also** sections follow.

The format is a strict superset of a plain-markdown section — strip the scaffolding and links and what remains is an ordinary heading with prose, so a map renders and navigates as plain markdown in any tool.

**See also**

- [MAP-GUIDANCE.md](MAP-GUIDANCE.md) — the authoritative anatomy and identity rules.

# Change-Management

```yaml
id: cm4
```

[Unified Map Method](#unified-map-method)
[Cadences](#cadences)
[Change Lifecycle](#change-lifecycle)
[Startup Scan](#startup-scan)
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

# Navigation Links

```yaml
id: b3q
```

[Node](#node)

The tree lives in the links, not in a separate index or the file layout. Each node names its one parent and each of its children, so following links *is* walking the tree. Siblings aren't listed directly — you reach them by stepping up to the parent, whose child links name them all.

> [!IMPORTANT] Links resolve by node name, never by ID, so ordinary markdown tooling navigates them and a node's identity token never appears as a link target.

**Detail**

The parent link is omitted only by the root; every other node has exactly one. Link text is the target node's actual name, so an editor with a markdown LSP (e.g. marksman) jumps straight there with `gd`. Because links are name-anchored, renaming a node is a mechanical re-point of the links that named it, and the ID never appears in a link. A user may omit links while drafting; the agent proposes them on review.

# Node Sections

```yaml
id: s8r
```

[Node](#node)
[Callouts](#callouts)

The main user-facing parts of a node are each optional and include, in a fixed order: **prose**, **Callouts**, **Detail**, and **See also**. Prose is the mental picture and usually the only part the user must read, but even it can be dropped — a node may carry only Detail, for instance. A node using none of these is just a heading: an ordinary markdown section.

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

The map's shape is shown at a glance by a **tree overview** — a box-drawing sketch of the whole node tree — kept at the end of the root node. Nodes not yet written are marked `(TODO)`, so the intended shape is visible before the content is. The rendering is only a convenience: the real tree is encoded in the navigation links, and the overview is kept in step with them.

**Detail**

The overview is a fenced code block using box-drawing characters. A map is one file by default, splitting across several (linked by relative paths) only when size makes one file unwieldy; navigation works the same either way.

# Node Sizing

```yaml
id: z9p
```

[Specification](#specification)

Keep nodes small and focussed on one concept. The rough upper bound for size is around 800 characters, but the real test is felt: if a node starts wanting sub-sections, it's outgrown one concept and should split into children.

**Detail**

Character counts exclude tables and diagrams. When a node runs over, the agent flags it rather than silently trimming, so splitting-versus-keeping stays the user's call.

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

# Conceptual Writing

```yaml
id: h3v
```

[Writing Style](#writing-style)

Two habits shape how a node reads, and one trap to avoid:

- **Lead with the mental picture** before any implementation detail.

- **Name the boxes before explaining them** — say "there are three mechanisms: A, B, C" and then give each its own node or bullet point.

- Don't **couple to code structure**: prose may name a technical concept when load-bearing, but the map tracks the user's model, not the code's shape — so it shouldn't break when code is refactored.

# Formatting

```yaml
id: f2n
```

[Writing Style](#writing-style)

Typographic conventions for map prose.

- Write each paragraph as one continuous line with no hard wraps, so it reflows under soft-wrap.

- Separate bullet points with a blank line for readability.

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

Because these edits describe reality rather than intent, they fall outside the active-change requirement: no open change is needed, and they may happen at any time.

**See also**

- [Gates and Permissions](#gates-and-permissions) — the active-change requirement this exemption stands against.

# Sync Rule

```yaml
id: s5y
```

[Edit Governance](#edit-governance)

The map tracks reality. It may be edited to match reality at any time, but never *ahead* of it: an edit describing work not yet built waits until it is. Pending work is held as parked changes in `changes/`, off the map, so the map stays a record of what exists.

# Engagement Rule

```yaml
id: n3g
```

[Edit Governance](#edit-governance)

Every map edit is negotiated with the user, one node at a time — never silent, never in bulk. When a change touches several nodes they are named up front and settled one by one. The prompts are comprehension checks — "does that fit your mental model?" — not yes/no gates, because the aim is a shared mental picture, not sign-off.

# Map Maintenance

```yaml
id: t7v
```

[Edit Governance](#edit-governance)

Keeping the map useful means constant engagement to keep the mental model accurate. Watch for the signals that a node has drifted from its job, such as:

- It starts wanting sub-sections — split it into children.

- It has grown verbose — cut hard, push precision into Detail.

- A new concept has no natural home — the decomposition needs rethinking, not a misc bucket.

- The top-level boxes stop matching how the user thinks — restructure, because the map follows the user's model, not the code's.

**Detail**

A recurring check — the *ambiguity test*: for each node in the area you're touching, ask yourself if a fresh agent could build from it without guessing. If it couldn't, that's a map-quality gap to flag, not an implementation problem.

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

The worklist lists only the actions to take, not the reasons for them — those belong in the [Approach](#approach).

**Detail**

Before surfacing the worklist the agent prunes it against fixed rules: one task per atomic outcome, no restated "why", no obvious sub-steps, no ceremony tasks (a bare "review" or "double-check") unless they mark a real gate, and no file paths the task name already implies.


# Intent

```yaml
id: i8b
```

[Plan](#plan)

The opening part: why the change is needed expressed in domain language, not how it will be delivered unless relevant to the requirement. Kept brief and requiring user approval before anything else proceeds. For a [Wander](#cadences) change the Intent is the whole plan.

An Intent can also be captured and **parked** — left on its own in `changes/open/` until someone picks it up and the lifecycle resumes. A parked Intent may optionally reference the map node(s) it concerns as *name (id)* — the name to navigate to now, the id in brackets to stay recoverable if the name later changes — but nothing requires it.

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

# Build

```yaml
id: u6k
```

[Change Lifecycle](#change-lifecycle)
[Conclude](#conclude)

Executing the approved plan against the real project files. The agent follows the plan rather than redesigning mid-flight — working through it in whatever shape it took, marking progress as each piece lands and posting concise updates without pausing step by step. It interrupts only when something warrants it — a surprise, an ambiguity, or a plan that turns out wrong. If the path forward is unclear the agent stops, records the blocker, and hands back rather than improvising.

Only one change builds at a time, held by a lock. Throughout, the agent keeps a running **Log** at the foot of the document — a terse record of the unexpected (surprises, deviations, blockers, partial progress), so a resuming session knows what the plan alone doesn't convey. Routine execution going to plan needs no entry.

**Detail**

The lock is `changes/open/active.md`, naming the one change under build; if it already exists, stop. On entering Build a versioned project agrees a bump kind, and every later hand-back for testing bumps patch. If the user later agrees the Plan needs revisiting, the agent writes a **Feedback** block — status (implemented / partial / not), notes on what to reconsider, and documentation impact — which returns the change to planning. A build that changed code keeps the lock even when handed back; only an untouched one may release it.


# Conclude

```yaml
id: o4j
```

[Build](#build)

The closing note, written only once the user confirms the build is done. It states where the change landed — not a story of how it got there.

Any [aside](#aside-keyword) still open from the build is settled before Conclude begins; nothing is wrapped up with asides outstanding.

It records only what the plan and the Log don't already convey: deviations, documents touched, surprises. When there's nothing to add, "Completed." is enough.

A [Wander](#cadences) change has no Approach, but its Build [Log](#build) already carries what happened, so Conclude still just names the landing point — and may rename the change to match where the work ended up.

Its mere presence is the marker that the change is finished.

**Detail**

For a versioned project with substantive change the draft also proposes a changelog entry. On the user's approval the change is archived to `changes/archive/` (prefixed `YYYY-MM-DD-`), the `active.md` lock is removed, and any approved changelog entry is added.


# Startup Scan

```yaml
id: x7t
```

[Change-Management](#change-management)

What the agent does first in every session: read everything in `changes/open/` and orient. Each change is placed by where it sits in the [lifecycle](#change-lifecycle): still in [Plan](#plan) — formed anywhere from a just-parked [Intent](#intent) to a worklist awaiting approval — or under [build](#build). The `active.md` lock names the change currently building, if any.

From that the agent announces whether it's planning or building, reports what's open, and proposes the next step — resuming an interrupted build, or picking up a parked Intent.

**Detail**

An interrupted build is recognised by `active.md` pointing at a change whose work is unfinished; the agent reads that change's [Log](#build) to recover context rather than restarting. A change carrying [Feedback](#build) but no [Conclusion](#conclude) has been handed back to planning and needs replanning.

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

[Unified Map Method](#unified-map-method)

The method needs no bespoke application — it rides generic markdown tooling. In an editor with a markdown language server (marksman, in Helix), the name-anchored [navigation links](#navigation-links) become jump-to-definition targets: `gd` walks the tree parent-to-child, and the symbol picker (Helix `Space+s`) lists every node by name for a direct jump anywhere. Nothing custom is required; the format is kept deliberately plain so richer surfaces stay cheap to build on top later.
