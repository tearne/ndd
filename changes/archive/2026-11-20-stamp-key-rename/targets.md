# Sign-off Stamp

[↑ Node](#node) \
[Fingerprint](#fingerprint) \
[Stamp States](#stamp-states)

```yaml
id: p8m
signers:
  tearne: {at: 2026-11-20, hash: 6b3fa92c}
```

A sign-off stamp records one person's sign-off of one node, or a request for one. Stamps live in the node's scaffolding block under a `signers:` mapping keyed by each [signer](#signer)'s name or handle, so each person holds exactly one and a new sign-off overwrites it. Because they are in the node rather than a separate ledger, they follow it through renames and moves. A node without the mapping is simply not signed off, and most maps never gain one.

**Detail**

Each value holds `at`, an ISO 8601 date, and `hash`, the [fingerprint](#fingerprint) of the text signed off. A [requested](#stamp-states) stamp has `hash: null`, and `at` is the date of the request. Quote the key if it contains a colon or starts with punctuation.

An older map's `approvals:` key is read as `signers:`, and renamed to it whenever a stamp is written.

```yaml
id: w9c
signers:
  alice: {at: 2026-09-10, hash: 3f9a1c2e}
  bob: {at: 2026-08-02, hash: 8d02b7e4}
```

**See also**

- [Sign-off](#sign-off) — the check that reads the stamps.
- [Node Identity](#node-identity) — the other thing the scaffolding block holds.


# Fingerprint Helper

[↑ Fingerprint](#fingerprint)

```yaml
id: u6h
signers:
  tearne: {at: 2026-11-20, hash: 9e1df54b}
```

`util/fingerprint.py` helps generate [sign-off stamps](#sign-off-stamp) and identify what's due for [Sign-off](#sign-off).

- Given a map file it prints every node's fingerprint, or given a node name, that one alone.
- With `--due` it reads the stamps and prints the nodes due for a name, those [stale or requested](#stamp-states).
- With `--migrate` it renames an older map's `approvals:` key to `signers:`; no fingerprint moves.

Besides migrating, it reads only; stamps are written by the agent or the [map viewer](#map-viewer).

**Detail**

Example usage:

```
ndd/method/util/fingerprint.py map.md
ndd/method/util/fingerprint.py map.md "Node Name"
ndd/method/util/fingerprint.py map.md --due "Alice Smith"
ndd/method/util/fingerprint.py map.md --migrate
```

A [POS-style](standards/POS.md) script, run on one map file at a time.


# Sign-off Button

[↑ Map Viewer](#map-viewer)

```yaml
id: vs1
signers:
  tearne: {at: 2026-11-20, hash: b562b2ef}
```

On a node's page, beside its sign-offs, a *Sign off* button opens a drop-down of names to tick, with *Sign off* to record a sign-off for each and *Request* to write a [request](method/ndd.map.md#stamp-states) for each with no stamp on the node. A sign-off diff, showing an old version, has no button.

The drop-down lists every handle in the map's stamps and any name added in that browser, kept there until removed; only added names are removable. The last names ticked are ticked again.

Each name gets its line under the node's `signers:` key, dated today and, for a sign-off, with the fingerprint of the text shown; nothing else is written, and writes are guarded as [Request Guards](#request-guards) describes. Committing is left to the user, prompted by a red light at the page's top right whose tooltip says the repository has uncommitted changes.


# Fingerprint Check

[↑ Testing](#testing)

```yaml
id: c5m
signers:
  tearne: {at: 2026-11-20, hash: b7905cbd}
```

`tests/fingerprint_test.py` holds the reference: a second, independent implementation of the [Fingerprint](method/ndd.map.md#fingerprint) rule. It passes when its fingerprints match the table in *Detail* and the shipped [helper](method/ndd.map.md#fingerprint-helper) agrees, both on those fingerprints and on which nodes are due for a person, and the [map viewer](map.md#map-viewer) on the fingerprints.

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


# Map Viewer Check

[↑ Testing](#testing)

```yaml
id: v8c
signers:
  tearne: {at: 2026-11-20, hash: 9affd6ea}
```

`tests/map_viewer/map_viewer_test.py` builds the demo map, serves it with the [map viewer](map.md#map-viewer) on a free port of 127.0.0.1, and checks each page against what its demo node says it shows: stamps, including one under an older `approvals:` key, and sign-off diffs, one tree across files, markdown rendering, the page shape the page script swaps, a split page's second pane, and answers to bad requests. On a copy of the demo map, it checks that a [sign-off](map.md#sign-off-button) writes its stamp, renaming an older `approvals:` key, and that the file is left untouched when a sign-off is for a node changed since its page was shown, lacks the run's token, is not a POST, or comes from a foreign Host or Origin. Where node is installed, it also checks that the page script parses.
