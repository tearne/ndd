# Fixture

[Plain Prose](#plain-prose)
[Full Sections](#full-sections)
[Bare Heading](#bare-heading)
[Changed Prose](#changed-prose)

```yaml
id: fx1
approvals:
  expected: {at: 2026-09-11T12:00:00+01:00, hash: ab9e6f02}
```

A small map whose only purpose is to pin the Fingerprint rule. Each node carries a stamp for a person called `expected` holding its own fingerprint, so the whole file is a Sign-off with nothing due. The copy beside it, `fixture-edited.map.md`, applies edits that must not change a fingerprint, and two that must.


# Plain Prose

[↑ Fixture](#fixture)

```yaml
id: fx2
approvals:
  expected: {at: 2026-09-11T12:00:00+01:00, hash: bcf6b47b}
```

One paragraph of prose is the common case. Its fingerprint must survive being re-wrapped, re-indented or given a stamp, because none of that changes what a reader sees.


# Full Sections

[↑ Fixture](#fixture)
[Child](#child)

```yaml
id: fx3
approvals:
  expected: {at: 2026-09-11T12:00:00+01:00, hash: 3a096aaf}
```

A node using every optional section. Renaming its child changes the link line below the heading but nothing this node says, so its fingerprint holds while the child's own changes.

> [!IMPORTANT] A callout is part of what the reader sees and so is hashed.

**Detail**

A fenced block inside *Detail* is prose to the reader, hashed like the rest, and a `#` inside it is not a heading:

```yaml
id: k7f  # an example, not this node's scaffolding
approvals:
  alice: {at: 2026-09-10T14:05:00+01:00, hash: 3f9a1c2e}
```

**See also**

- [Plain Prose](#plain-prose) — the minimal case this one extends.


# Child

[↑ Full Sections](#full-sections)

```yaml
id: fx4
approvals:
  expected: {at: 2026-09-11T12:00:00+01:00, hash: 250ae92a}
```

A child whose name will change in the edited copy. A rename changes its heading, and the heading is hashed, so the renamed node is due even though its prose is untouched.


# Bare Heading

[↑ Fixture](#fixture)

A hand-drafted node with no scaffolding block yet. When Tidy adds one the fingerprint must not move.


# Changed Prose

[↑ Fixture](#fixture)

```yaml
id: fx6
approvals:
  expected: {at: 2026-09-11T12:00:00+01:00, hash: 275d67bd}
```

A node whose prose gains one word in the edited copy. That is a real change, so it must fall due.
