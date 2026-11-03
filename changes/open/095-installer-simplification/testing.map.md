# Testing

[↑ NDD Project](map.md#ndd-project) \
[Contents](#contents) \
[Fingerprint Check](#fingerprint-check) \
[Install Check](#install-check)

```yaml
id: t4k
approvals:
  tearne: {at: 2026-11-03, hash: d356e923}
```

This repository checks itself with tests, each a node in this branch stating what must hold and how it is verified. Its runnable form sits under `tests/` rather than in the map, so the map stays a description of what exists.

- **[Fingerprint Check](#fingerprint-check)** — the reference implementation of the [Fingerprint](ndd.map.md#fingerprint) rule and the cases that pin it.

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
  tearne: {at: 2026-09-13, hash: a4340fad}
```

Every agent must produce the same fingerprint for the same node text, or approval stamps cannot be compared. `tests/fingerprint_test.py` is the reference implementation of the [Fingerprint](ndd.map.md#fingerprint) rule, standard library only and short enough to read whole, run against two fixtures beside it: `fixture.map.md`, a small map exercising every node section, and `fixture-edited.map.md`, the same map after edits that must not move a fingerprint and three that must. It passes when every node's fingerprint is the one tabled in *Detail*. An agent about to trust any other implementation, its own included, runs that implementation over the fixtures and compares with the table.

**Detail**

| Node | Original | Edited | Edit made |
|---|---|---|---|
| Fixture | ab9e6f02 | 5fd5a260 | prose changed |
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
  tearne: {at: 2026-11-03, hash: 8b40920b}
```

`tests/install_test.py` runs the [installer](map.md#installer) into a temporary directory and asserts that:

- run from its own checkout, it exits non-zero and writes nothing;

- what lands in `ndd/` is exactly the [shipped assets](map.md#shipped-assets), scripts still executable;

- `CLAUDE.md` and `AGENTS.md` are pointers, and `.gitignore` covers `ndd/`, both entry files and `.claude/`;

- every link in the installed maps resolves;

- a second run over a changed `ndd.map.md` and a stray file keeps the old map as `ndd.prev.map.md` and clears the stray;

- an entry file the project already had is left out of `.gitignore`.

It prints the shipped files, so a stray one is seen.
