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
- **Change-Management** — how the spec evolves, through modes and gates.
- **Tooling** — the viewer and index that serve both.

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
│ └ Map Maintenance
├ Change-Management
│ ├ Modes
│ ├ Change Lifecycle
│ │ ├ Intent
│ │ ├ Approach
│ │ ├ Plan
│ │ ├ Build (TODO)
│ │ └ Conclusion (TODO)
│ ├ Seeds (TODO)
│ ├ Startup Scan (TODO)
│ ├ Gates and Permissions (TODO)
│ └ Keywords (TODO)
│   ├ Process Keyword (TODO)
│   └ Aside Keyword (TODO)
└ Tooling (TODO)
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
[Map Maintenance](#map-maintenance)

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
[Modes](#modes)
[Change Lifecycle](#change-lifecycle)
[Seeds](#seeds)
[Startup Scan](#startup-scan)
[Gates and Permissions](#gates-and-permissions)
[Keywords](#keywords)

How the spec evolves: proposals move through modes and explicit user gates, and land as changes to the map. A node's build-state is expressed by *where it lives* — a proposal artefact versus the main map — not by a status field, keeping both surfaces plain markdown that differ only by a diff.

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

# Map Maintenance

```yaml
id: t7v
```

[Specification](#specification)

The map is never finished and never append-only. Keeping it useful means constant refactoring and engagement to keep the mental model accurate. Watch for the signals that a node has drifted from its job:

- It starts wanting sub-sections — split it into children.

- It has grown verbose — cut hard, push precision into Detail.

- An only-child isn't really its own concept — fold it into its parent.

- A new concept has no natural home — the decomposition needs rethinking, not a misc bucket.

- The top-level boxes stop matching how the user thinks — restructure, because the map follows the user's model, not the code's.

**Detail**

A recurring check — the *ambiguity test*: for each node in the area you're touching, ask whether a fresh agent could build from it without guessing. Where it couldn't, that's a map-quality gap to flag, not an implementation problem.

# Modes

```yaml
id: e3n
```

[Change-Management](#change-management)

Each change can be executed using one of three approaches. The agent proposes one after Intent is approved — default **Formal** — and the user confirms.

- **Formal** — waterfall-style with an executable task checklist as its Plan. The default, for work that benefits from explicit decisions and step-by-step tracking.

- **Explore** — the same approval gates as Formal, but the Plan consists of topics plus a *done-when* condition rather than explicit tasks. For work where depth and coverage matter more than a fixed step list.

- **Wander** — jump straight from Intent to Build, with a retrospective Conclusion and no Approach or Plan. For work too small or too fluid to plan; the agent flags topic drift and can offer to flush.

**Detail**

Mode can change mid-flight: pause, rewrite the change document into the target mode's shape, resume. A discarded Wander change is deleted rather than archived, and its name may be updated to reflect where the work actually ended up.

# Change Lifecycle

```yaml
id: l5g
```

[Change-Management](#change-management)
[Intent](#intent)
[Approach](#approach)
[Plan](#plan)
[Build](#build)
[Conclusion](#conclusion)

A change is a single markdown document that advances through a fixed sequence of stages:

1. **Intent** — why the change is needed.
2. **Approach** — how it will be carried out.
3. **Plan** — the concrete steps or topics to execute.
4. **Build** — doing the work against the plan.
5. **Conclusion** — a retrospective once the work is accepted.

Each stage is drafted into the document, then surfaced for the user's explicit approval before the next begins. Which stages apply is set by the [mode](#modes) — Wander collapses the sequence to Intent → Build → Conclusion.

The document is the single carrier of state: where a change sits is read from what it contains, not from any status field. Chat carries only disclosures and summaries; the drafted stage text lives in the document.

**Detail**

The stages divide into two working postures. *Plan mode* spans Intent through Plan — research and reasoning, writing only to the change document. *Build mode* executes an approved Plan, writing to project files. The boundary is an approval gate, so no project file changes before a plan is agreed.

# Intent

```yaml
id: i8b
```

[Change Lifecycle](#change-lifecycle)

The opening stage: why the change is needed expressed in domain language, not how it will be delivered unless relevant to the requirement. Kept brief and requiring user approval before anything else proceeds. For a [Wander](#modes) change the Intent is the only planning stage.

**Detail**

Intent is capped short (a ~500-character soft trigger); past that the agent flags borderline material and asks the user to adjudicate rather than surfacing it as final.

# Approach

```yaml
id: a2r
```

[Change Lifecycle](#change-lifecycle)

How the change will be carried out, written as a list of decisions and their reasons — not a narrative and not a file-by-file rehearsal, which belongs to the [Plan](#plan). Each decision earns a line only if it carries a reason; self-evident choices need no subsection. Skipped entirely by [Wander](#modes).

Alongside it sits an **Unresolved** list: the open items the agent can't settle alone, each pointing at the part of the Approach it affects. The agent surfaces the full list in chat so the user can see everything outstanding, then walks through them — for anything non-trivial, one at a time ("4 unresolved items […]. First one: …") rather than asking the user to address them all at once. Answers fold back into the prose and the list shrinks. An empty list means the Approach is ready for approval.

**Detail**

The agent re-reads and prunes its own draft before surfacing — anything not carrying a decision-and-reason comes out — then a ~1000-character soft trigger flags borderline material for the user to adjudicate. Once the Plan is written the Unresolved section is deleted; its absence is the signal that the Approach is settled.

# Plan

```yaml
id: p9d
```

[Change Lifecycle](#change-lifecycle)

What [Build](#build) executes. The shape is set by the [mode](#modes):

- **Formal** gives a checklist of discrete tasks, each an atomic outcome ticked off as it lands;

- **Explore** gives a bulleted list of topics closed by a single *done-when* condition rather than tick-boxes.

- [Wander](#modes) has no Plan.

The Plan says only what to do, never why — the reasoning is the Approach's job.

**Detail**

before surfacing, the agent prunes the Plan against fixed rules: one task per atomic outcome, no restated "why", no obvious sub-steps, no ceremony tasks (a bare "review" or "double-check") unless they mark a real gate, and no file paths the task name already implies.

```yaml
id: u6k
```

[Change Lifecycle](#change-lifecycle)

(TODO)

# Conclusion

```yaml
id: o4j
```

[Change Lifecycle](#change-lifecycle)

(TODO)

# Seeds

```yaml
id: s3w
```

[Change-Management](#change-management)

(TODO)

# Startup Scan

```yaml
id: x7t
```

[Change-Management](#change-management)

(TODO)

# Gates and Permissions

```yaml
id: g5m
```

[Change-Management](#change-management)

(TODO)

# Keywords

```yaml
id: k9y
```

[Change-Management](#change-management)
[Process Keyword](#process-keyword)
[Aside Keyword](#aside-keyword)

(TODO)

# Process Keyword

```yaml
id: r4c
```

[Keywords](#keywords)

(TODO)

# Aside Keyword

```yaml
id: y2f
```

[Keywords](#keywords)

(TODO)

# Tooling

```yaml
id: g8l
```

[Unified Map Method](#unified-map-method)

(TODO)
