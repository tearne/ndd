# Testing

[↑ NDD Project](map.md#ndd-project) \
[Contents](#contents) \
[Fingerprint Check](#fingerprint-check) \
[Install Check](#install-check) \
[Map Viewer Check](#map-viewer-check) \
[Map Viewer Browser Check](#map-viewer-browser-check) \
[Map Viewer Due Check](#map-viewer-due-check) \
[Test Setup](#test-setup)

```yaml
id: t4k
signers:
  tearne: {at: 2026-11-20, hash: 3478cec5}
```

This repository checks itself with tests, each a node in this branch stating what must hold and how it is verified. Each test's runnable form sits under `tests/` rather than in the map, so the map stays a description of what exists.

- **[Fingerprint Check](#fingerprint-check)** — the reference implementation of the [Fingerprint](method/ndd.map.md#fingerprint) rule and the cases that pin it.

- **[Install Check](#install-check)** — the installer run end to end into a scratch project, fresh and as an upgrade.

- **[Map Viewer Check](#map-viewer-check)** — the viewer's pages served from the demo map and checked against what each demo node shows.

- **[Map Viewer Browser Check](#map-viewer-browser-check)** — the page script driven in a headless browser on the same demo map.

- **[Map Viewer Due Check](#map-viewer-due-check)** — due nodes and requesting, driven in the same browser.

- **[Test Setup](#test-setup)** — what the checks need to run, and what is skipped without each.


# Contents

[↑ Testing](#testing)

```yaml
id: ct7
```

- [Testing](#testing)
  - [Fingerprint Check](#fingerprint-check)
  - [Install Check](#install-check)
  - [Map Viewer Check](#map-viewer-check)
    - [Map Viewer Write Check](#map-viewer-write-check)
  - [Map Viewer Browser Check](#map-viewer-browser-check)
  - [Map Viewer Due Check](#map-viewer-due-check)
  - [Test Setup](#test-setup)


# Fingerprint Check

[↑ Testing](#testing)

```yaml
id: c5m
signers:
  tearne: {at: 2026-11-20, hash: 82b25cb7}
```

[`tests/fingerprint_test.py`](tests/fingerprint_test.py) holds the reference: a second, independent implementation of the [Fingerprint](method/ndd.map.md#fingerprint) rule. It passes when its fingerprints match the table in *Detail* and the shipped [helper](method/ndd.map.md#fingerprint-helper) agrees, both on those fingerprints and on which nodes are due for a person, and the [map viewer](map.md#map-viewer) on the fingerprints.

**Detail**

`fixture.map.md` is a small map exercising every node section; `fixture-edited.map.md` is the same map after edits that must not move a fingerprint and three that must. Further cases check that a stamp quoted in a node's prose is not read as one, that a requested stamp, `hash: null`, makes its node due, that a node with no stamp for a person is not due for them, that a stamp under an older `approvals:` key is read, and that `--migrate` renames the key and leaves every stamp current.

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
signers:
  tearne: {at: 2026-11-20, hash: aa1beedb}
```

[`tests/install_test.py`](tests/install_test.py) runs the [installer](map.md#installer) into a temporary directory and asserts that:

- run from its own checkout, it exits non-zero and writes no `ndd/`;

- what lands in `ndd/` is exactly the [shipped assets](map.md#shipped-assets), scripts still executable;

- `CLAUDE.md` and `AGENTS.md` are pointers, and `.gitignore` covers `ndd/`, both entry files and `.claude/`;

- every link in a shipped file resolves within what ships;

- a second run over a changed `ndd.map.md` and a stray file keeps the old map as `ndd.prev.map.md` and clears the stray, and so does a run over the flat layout from before 3.0.0;

- an entry file the project already had is left out of `.gitignore`;

- the shipped [map viewer](map.md#map-viewer), run from the project's root, serves its map.

It prints the shipped files, so a stray one is seen.


# Map Viewer Check

[↑ Testing](#testing) \
[Map Viewer Write Check](#map-viewer-write-check)

```yaml
id: v8c
signers:
  tearne: {at: 2026-11-24, hash: f82b2fcb}
```

[`tests/map_viewer/map_viewer_test.py`](tests/map_viewer/map_viewer_test.py) builds the demo map, serves it with the [map viewer](map.md#map-viewer) on a free port of 127.0.0.1, and checks each page against what its demo node says it shows: stamps, including one under an older `approvals:` key, and sign-off diffs, one tree across files, markdown rendering, the page shape the page script swaps, a split page's second pane, and answers to bad requests. On a copy of the demo map, it checks the writes [Map Viewer Write Check](#map-viewer-write-check) describes. Where [Node](#test-setup) is installed, it also checks that the page script parses.


# Map Viewer Write Check

[↑ Map Viewer Check](#map-viewer-check)

```yaml
id: v8d
signers:
  tearne: {at: 2026-11-25, hash: 8adcbe3e}
```

On a copy of the demo map, [Map Viewer Check](#map-viewer-check) checks each kind of write. Each is refused, leaving every file untouched, without the run's token, when not a POST, or from a foreign Host or Origin.

- **[Sign-off](map.md#sign-off-button)** — writes its stamp, renaming an older `approvals:` key; refused for a node changed since its page was shown, or with a `request` key.

- **Request for sign-off** — writes `hash: null` only for names with no stamp on the node, on one node and on several across three files; refused whole if any node refuses.

- **Withdrawal** — removes only the ticked names' requests, across two files, keeping current and stale stamps, others' requests and an emptied `signers:` key; refused whole if any node refuses.


# Map Viewer Browser Check

[↑ Testing](#testing)

```yaml
id: v9b
signers:
  tearne: {at: 2026-11-25, hash: adaa2da5}
```

[`tests/map_viewer/browser_test.py`](tests/map_viewer/browser_test.py) drives the [map viewer](map.md#map-viewer)'s page script in headless Chromium, on the demo map [Map Viewer Check](#map-viewer-check) serves. It checks the tree keeping its folds across links and back and forward, never redrawn; the fold button; a sign-off diff swapped in; the second pane through split, reload, swap and close, each pane scrolling in its own box; and each pane's history. On a copy of the demo map, it checks the *Sign off* button: its drop-down's names, one added and removed without the drop-down closing, the last ticked ticked again, the drop-down reopening set to sign off, the stamps current once pressed, and none on a sign-off diff; and the red light while the repository has uncommitted changes. Any script error fails it.

It needs Playwright and its Chromium, as [Test Setup](#test-setup) describes.


# Map Viewer Due Check

[↑ Testing](#testing)

```yaml
id: v9d
signers:
  tearne: {at: 2026-11-25, hash: cddd2b67}
```

On a copy of the demo map, [`tests/map_viewer/browser_test.py`](tests/map_viewer/browser_test.py) also checks [due nodes](map.md#due-nodes), requesting, withdrawing and the [request bar](map.md#request-bar). Ticking people in the *Due for* bar marks the nodes due for any of them and shows the count, and a sign-off clears the mark in place. In a node's *Sign off* drop-down, *request* writes a requested stamp for a ticked name with no stamp, making the node due for them, and nothing for one already stamped; *withdraw* removes the request, keeping a sign-off.

In the request bar, picking a branch picks it alone, or with *children* ticked what is below it too. *Apply* stays disabled until a name is ticked, then writes one request for each node picked, across files, clears the picks and opens *Due for* on that name; closing *Due for* clears the marks. The bar opens set to *request*; set to *withdraw*, it removes those requests alone.


# Test Setup

[↑ Testing](#testing)

```yaml
id: ts5
signers:
  tearne: {at: 2026-11-20, hash: 24b3715f}
```

What the checks need to run; exact commands and version pins are in each script's header. Once set up, none needs internet access.

- **uv**, required: every check is a script it runs, and on first use it fetches the Python they pin and Playwright.

- **git**, required by the map viewer checks, whose demo map is a repository, as the viewer reads a node's history to show what changed.

- **Node**, optional: [Map Viewer Check](#map-viewer-check) uses it to check that the page script parses, and skips that without it; it must be on the PATH.

- **Playwright with its Chromium**, optional: [Map Viewer Browser Check](#map-viewer-browser-check) and [Map Viewer Due Check](#map-viewer-due-check) drive the browser, and pass with a note when it is missing.
