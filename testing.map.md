# Testing

[↑ NDD Project](map.md#ndd-project) \
[Contents](#contents) \
[Fingerprint Check](#fingerprint-check) \
[Install Check](#install-check)

```yaml
id: t4k
approvals:
  tearne: {at: 2026-11-04, hash: 7288292a}
```

This repository checks itself with tests, each a node in this branch stating what must hold and how it is verified. Each test's runnable form sits under `tests/` rather than in the map, so the map stays a description of what exists.

- **[Fingerprint Check](#fingerprint-check)** — the reference implementation of the [Fingerprint](method/ndd.map.md#fingerprint) rule and the cases that pin it.

- **[Install Check](#install-check)** — the installer run end to end into a scratch project, fresh and as an upgrade.


# Contents

[↑ Testing](#testing)

```yaml
id: ct7
```

- [Testing](#testing)
  - [Fingerprint Check](#fingerprint-check)
  - [Install Check](#install-check)


# Fingerprint Check

[↑ Testing](#testing)

```yaml
id: c5m
approvals:
  tearne: {at: 2026-11-04, hash: 5a165bce}
```

Every agent must produce the same fingerprint for the same node text, or approval stamps cannot be compared. `tests/fingerprint_test.py` holds the reference: a second, independent implementation of the [Fingerprint](method/ndd.map.md#fingerprint) rule, standard library only and short enough to read whole. It passes when its fingerprints match the table in *Detail* and the shipped [helper](method/ndd.map.md#fingerprint-helper) agrees, both on those fingerprints and on which nodes are due for a person. The test and its fixtures stay in the NDD checkout, where a maintainer changing the helper runs them.

**Detail**

`fixture.map.md` is a small map exercising every node section; `fixture-edited.map.md` is the same map after edits that must not move a fingerprint and three that must. A further case checks that a stamp quoted in a node's prose is not read as one.

| Node | Original | Edited | Edit made |
|---|---|---|---|
| Fixture | 11f6836e | c332f293 | prose changed |
| Plain Prose | bcf6b47b | bcf6b47b | paragraph re-wrapped and indented |
| Full Sections | 188f743f | 188f743f | child link renamed |
| Child, then Renamed Child | 250ae92a | 103b2b33 | heading renamed |
| Bare Heading | 6bcce17f | 6bcce17f | scaffolding block and stamp added |
| Changed Prose | 275d67bd | 618c09de | one word added |


# Install Check

[↑ Testing](#testing)

```yaml
id: k3w
approvals:
  tearne: {at: 2026-11-04, hash: 9b993f6e}
```

`tests/install_test.py` runs the [installer](map.md#installer) into a temporary directory and asserts that:

- run from its own checkout, it exits non-zero and writes no `ndd/`;

- what lands in `ndd/` is exactly the [shipped assets](map.md#shipped-assets), scripts still executable;

- `CLAUDE.md` and `AGENTS.md` are pointers, and `.gitignore` covers `ndd/`, both entry files and `.claude/`;

- every link in a shipped file resolves within what ships;

- a second run over a changed `ndd.map.md` and a stray file keeps the old map as `ndd.prev.map.md` and clears the stray, and so does a run over the flat layout from before 3.0.0;

- an entry file the project already had is left out of `.gitignore`.

It prints the shipped files, so a stray one is seen.
