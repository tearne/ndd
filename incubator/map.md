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
│ │ ├ Navigation Links (TODO)
│ │ ├ Node Sections (TODO)
│ │ │ └ Callouts (TODO)
│ │ └ Degradation (TODO)
│ ├ Map Structure (TODO)
│ ├ Node Sizing (TODO)
│ ├ Content Principles (TODO)
│ └ Map Maintenance (TODO)
├ Change-Management
│ ├ Modes (TODO)
│ ├ Change Lifecycle (TODO)
│ │ ├ Intent (TODO)
│ │ ├ Approach (TODO)
│ │ ├ Plan (TODO)
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
[Content Principles](#content-principles)
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
[Degradation](#degradation)

A node is one concept: a heading, an agent-maintained scaffolding block, name-anchored navigation links to its parent and children, and terse prose leading with the mental picture. Optional **Detail** and **See also** sections follow. The format is a strict superset of a plain-markdown section — a node using none of the machinery is exactly an ordinary heading with prose, so simple maps stay plain.

Identity lives in the scaffolding block as a stable, opaque ID, assigned once and never rewritten — not on rename, not on move. Navigation resolves by name, never by ID, so ordinary markdown navigators work; the ID's only job is durable identity across renames, so later approval and drift state stays bound to the node.

**See also**

- [MAP-GUIDANCE.md](MAP-GUIDANCE.md) — the authoritative anatomy, identity rules, and degradation spec.

# Change-Management

[Unified Map Method](#unified-map-method)
[Modes](#modes)
[Change Lifecycle](#change-lifecycle)
[Seeds](#seeds)
[Startup Scan](#startup-scan)
[Gates and Permissions](#gates-and-permissions)
[Keywords](#keywords)

How the spec evolves: proposals move through modes and explicit user gates, and land as changes to the map. A node's build-state is expressed by *where it lives* — a proposal artefact versus the main map — not by a status field, keeping both surfaces plain markdown that differ only by a diff.

This node carries no scaffolding block — a plain, name-only node — exercising the degradation guarantee: the superset format costs nothing until a project reaches for identity.

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

(TODO)

# Node Sections

```yaml
id: s8r
```

[Node](#node)
[Callouts](#callouts)

(TODO)

# Callouts

```yaml
id: c5k
```

[Node Sections](#node-sections)

(TODO)

# Degradation

```yaml
id: d2m
```

[Node](#node)

(TODO)

# Map Structure

```yaml
id: m6x
```

[Specification](#specification)

(TODO)

# Node Sizing

```yaml
id: z9p
```

[Specification](#specification)

(TODO)

# Content Principles

```yaml
id: p4h
```

[Specification](#specification)

(TODO)

# Map Maintenance

```yaml
id: t7v
```

[Specification](#specification)

(TODO)

# Modes

```yaml
id: e3n
```

[Change-Management](#change-management)

(TODO)

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

(TODO)

# Intent

```yaml
id: i8b
```

[Change Lifecycle](#change-lifecycle)

(TODO)

# Approach

```yaml
id: a2r
```

[Change Lifecycle](#change-lifecycle)

(TODO)

# Plan

```yaml
id: p9d
```

[Change Lifecycle](#change-lifecycle)

(TODO)

# Build

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
