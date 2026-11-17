# Testing

[↑ NDD Project](map.md#ndd-project) \
[Contents](#contents) \
[Fingerprint Check](#fingerprint-check) \
[Install Check](#install-check) \
[Map Viewer Check](#map-viewer-check) \
[Map Viewer Browser Check](#map-viewer-browser-check)

```yaml
id: t4k
approvals:
  tearne: {at: 2026-11-16, hash: 710420b9}
```

This repository checks itself with tests, each a node in this branch stating what must hold and how it is verified. Each test's runnable form sits under `tests/` rather than in the map, so the map stays a description of what exists.

- **[Fingerprint Check](#fingerprint-check)** — the reference implementation of the [Fingerprint](method/ndd.map.md#fingerprint) rule and the cases that pin it.

- **[Install Check](#install-check)** — the installer run end to end into a scratch project, fresh and as an upgrade.

- **[Map Viewer Check](#map-viewer-check)** — the viewer's pages served from the demo map and checked against what each demo node shows.

- **[Map Viewer Browser Check](#map-viewer-browser-check)** — the page script driven in a headless browser on the same demo map.


# Contents

[↑ Testing](#testing)

```yaml
id: ct7
```

- [Testing](#testing)
  - [Fingerprint Check](#fingerprint-check)
  - [Install Check](#install-check)
  - [Map Viewer Check](#map-viewer-check)
  - [Map Viewer Browser Check](#map-viewer-browser-check)


# Fingerprint Check

[↑ Testing](#testing)

```yaml
id: c5m
approvals:
  tearne: {at: 2026-11-10, hash: 80ee4e2f}
```

Every agent must produce the same fingerprint for the same node text, or approval stamps cannot be compared. `tests/fingerprint_test.py` holds the reference: a second, independent implementation of the [Fingerprint](method/ndd.map.md#fingerprint) rule, standard library only and short enough to read whole. It passes when its fingerprints match the table in *Detail* and the shipped [helper](method/ndd.map.md#fingerprint-helper) agrees, both on those fingerprints and on which nodes are due for a person, and the [map viewer](map.md#map-viewer) on the fingerprints. The test and its fixtures stay in the NDD checkout, where a maintainer changing the helper runs them.

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
  tearne: {at: 2026-11-16, hash: f2e62af9}
```

`tests/install_test.py` runs the [installer](map.md#installer) into a temporary directory and asserts that:

- run from its own checkout, it exits non-zero and writes no `ndd/`;

- what lands in `ndd/` is exactly the [shipped assets](map.md#shipped-assets), scripts still executable;

- `CLAUDE.md` and `AGENTS.md` are pointers, and `.gitignore` covers `ndd/`, both entry files and `.claude/`;

- every link in a shipped file resolves within what ships;

- a second run over a changed `ndd.map.md` and a stray file keeps the old map as `ndd.prev.map.md` and clears the stray, and so does a run over the flat layout from before 3.0.0;

- an entry file the project already had is left out of `.gitignore`;

- the shipped [map viewer](map.md#map-viewer), run from the project's root, serves its map.

It prints the shipped files, so a stray one is seen.


# Map Viewer Check

[↑ Testing](#testing)

```yaml
id: v8c
approvals:
  tearne: {at: 2026-11-17, hash: 8de533ff}
```

`tests/map_viewer/map_viewer_test.py` builds the demo map with `build_demo_map.py` beside it, serves it with the [map viewer](map.md#map-viewer) on a free port of 127.0.0.1, and checks each page against what its demo node says it shows: stamps and approval diffs, one tree across files, markdown rendering, the page shape the page script swaps, a split page's second pane, and answers to bad requests. On a copy of the demo map, it checks that a [sign-off](map.md#map-viewer-sign-off) writes its stamp, and that the file is left untouched when a sign-off is for a node changed since its page was shown, lacks the run's token, is not a POST, or comes from a foreign Host or Origin. Where node is installed, it also checks that the page script parses.

It needs no internet access, so it runs wherever the viewer does.


# Map Viewer Browser Check

[↑ Testing](#testing)

```yaml
id: v9b
approvals:
  tearne: {at: 2026-11-17, hash: 490f0ceb}
```

`tests/map_viewer/browser_test.py` drives the [map viewer](map.md#map-viewer)'s page script in headless Chromium, on the demo map [Map Viewer Check](#map-viewer-check) serves. It checks the tree keeping its folds across links and back and forward, never redrawn; the fold button; an approval diff swapped in; the second pane through split, reload, swap and close; and each pane's history. On a copy of the demo map, it checks the *Sign off* button: its drop-down's names, one added and removed, the last ticked ticked again, the stamps current once pressed, and none on an approval diff; and the red light while the repository has uncommitted changes. Any script error fails it.

It needs Playwright, pinned to the version whose Chromium is installed, and skips when that browser is missing; its header says how to set both up.
