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
│ └ Node
│   └ Callouts (TODO)
├ Change-Management
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

The conceptual map is the primary artefact. It holds the system's shape as a tree of concepts, structured the way the user thinks rather than how code is organised. Maintaining it is the comprehension-building activity; agents render it into code. Everything else in the method — how it changes, how it's viewed — serves this map.

The map's unit is the **Node**.

# Node

```yaml
id: nd1
```

[Specification](#specification)
[Callouts](#callouts)

A node is one concept: a heading, an agent-maintained scaffolding block, name-anchored navigation links to its parent and children, and terse prose leading with the mental picture. Optional **Detail** and **See also** sections follow. The format is a strict superset of a plain-markdown section — a node using none of the machinery is exactly an ordinary heading with prose, so simple maps stay plain.

Identity lives in the scaffolding block as a stable, opaque ID, assigned once and never rewritten — not on rename, not on move. Navigation resolves by name, never by ID, so ordinary markdown navigators work; the ID's only job is durable identity across renames, so later approval and drift state stays bound to the node.

**See also**

- [MAP-GUIDANCE.md](MAP-GUIDANCE.md) — the authoritative anatomy, identity rules, and degradation spec.

# Change-Management

[Unified Map Method](#unified-map-method)

How the spec evolves: proposals move through modes and explicit user gates, and land as changes to the map. A node's build-state is expressed by *where it lives* — a proposal artefact versus the main map — not by a status field, keeping both surfaces plain markdown that differ only by a diff.

This node carries no scaffolding block — a plain, name-only node — exercising the degradation guarantee: the superset format costs nothing until a project reaches for identity.
