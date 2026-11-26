# NDD Project

[Contents](#contents) \
[Distribution](#distribution) \
[Testing](testing.map.md#testing) \
[Map Viewer](#map-viewer) \
[Method Map Form](#method-map-form)

```yaml
id: p1j
signers:
  tearne: {at: 2026-11-25, hash: dde5957a}
```

The repository that develops and ships Non-Dead Design. The method itself has its own map, [NDD](method/ndd.map.md#ndd), which this project builds and ships as an asset rather than as a branch. This map describes how the method is distributed, released and installed, and the tooling built beside it. The reasoning behind the method is under [Principles](method/ndd.map.md#principles).

- **[Distribution](#distribution)** — how NDD reaches a client project: the shipped layout, the release checklist, the installer and the agent rules.

- **[Testing](testing.map.md#testing)** — how this repository checks itself: the checks and their runnable forms under `tests/`.

- **[Map Viewer](#map-viewer)** — a tool that serves a map in the browser for review and sign-off.

- **[Method Map Form](#method-map-form)** — the convention this project's method map follows.


# Contents

[↑ NDD Project](#ndd-project)

```yaml
id: ct6
```

- [NDD Project](#ndd-project)
  - [Distribution](#distribution)
    - [Release Steps](#release-steps)
    - [Installer](#installer)
      - [Shipped Assets](#shipped-assets)
    - [Agent Rules](#agent-rules)
      - [Rule Layout](#rule-layout)
      - [Rule Phrasing](#rule-phrasing)
      - [Rule Selection](#rule-selection)
      - [Rule Testing](#rule-testing)
  - [Testing](testing.map.md#testing)
  - [Map Viewer](#map-viewer)
    - [Sign-off Button](#sign-off-button)
    - [Request Guards](#request-guards)
    - [Write Checks](#write-checks)
    - [Due Nodes](#due-nodes)
    - [Request Bar](#request-bar)
    - [Navigation](#navigation)
  - [Method Map Form](#method-map-form)


# Distribution

[↑ NDD Project](#ndd-project) \
[Release Steps](#release-steps) \
[Installer](#installer) \
[Agent Rules](#agent-rules)

```yaml
id: d5v
signers:
  tearne: {at: 2026-11-04, hash: f34ff91c}
```

NDD is distributed as a git checkout: the user clones this repository and runs its [installer](#installer) from within their own project, which vendors the method into an `ndd/` subdirectory there, as [Installation](method/ndd.map.md#installation) describes from the client's side.

Only the method ships, as [Shipped Assets](#shipped-assets) lists; this project map and the testing map stay here. Nothing is rendered on the way, so a client reads exactly what this repository reads.

`main` is the single moving edge — no cut releases; the shipped `CHANGELOG.md` names the current version.


# Release Steps

[↑ Distribution](#distribution)

```yaml
id: l2s
signers:
  tearne: {at: 2026-11-04, hash: f3e0e188}
```

The checklist for a new version of NDD, published by moving `main`, and one of the next steps offered at [Archiving](method/ndd.map.md#archiving). If releasing, the agent confirms the user wants each of the following:

1. Run [Tidy](method/ndd.map.md#tidy) across the maps and offer the full [Map Review](method/ndd.map.md#map-review).
2. Run every test under [Testing](testing.map.md#testing) and see it pass.
3. Fold the dev headings in `CHANGELOG.md` into one dated heading, as [Versioning](method/ndd.map.md#versioning) describes.


# Installer

[↑ Distribution](#distribution) \
[Shipped Assets](#shipped-assets)

```yaml
id: n5w
signers:
  tearne: {at: 2026-11-04, hash: d1da4379}
```

A [POS-style](method/standards/POS.md) `install.py` at this project's root, run from a consumer's project to install or upgrade NDD; [Installation](method/ndd.map.md#installation) gives the consumer's side. It:

- clears the consumer's `ndd/` and copies the [shipped assets](#shipped-assets) into it from this checkout's disk, uncommitted edits included and scripts still executable; the last installed `ndd.map.md` that differs from the new one is kept beside it as `ndd.prev.map.md`;

- points `CLAUDE.md` and `AGENTS.md` at `ndd/method/AGENT-RULES.md`, replacing a file that only points into `ndd/` and warning on anything else;

- adds `ndd/` to `.gitignore`, with each entry file it created, and `.claude/` unless files under it are tracked.

**Detail**

It refuses to run from its own checkout. It checks that every shipped asset is present before touching `ndd/`, so a broken checkout leaves an install as it was.


# Shipped Assets

[↑ Installer](#installer)

```yaml
id: s4h
signers:
  tearne: {at: 2026-11-17, hash: 6be4dbca}
```

The installer copies into a client's `ndd/` only what the agent and user need at run time:

- `method/`, holding the agent rules, the method map, the fingerprint helper, the [map viewer](#map-viewer) and the standards, without the Python bytecode caches running its scripts leaves behind.
- `CHANGELOG.md` and `LICENSE` from the root, and `README.ndd.md` as `README.md`, so a project's people find the method's introduction at the top of `ndd/`.

Everything else stays in the checkout, for example `map.md`, `changes/`, `tests/`, `install.py` and the root `README.md`. The [Install Check](testing.map.md#install-check) catches a shipped file linking outside what ships.


# Agent Rules

[↑ Distribution](#distribution) \
[Rule Layout](#rule-layout) \
[Rule Phrasing](#rule-phrasing) \
[Rule Selection](#rule-selection) \
[Rule Testing](#rule-testing)

```yaml
id: r8d
signers:
  tearne: {at: 2026-11-04, hash: add5868a}
```

`AGENT-RULES.md` is a rendering of the core rules within the method map, optimised for agents; an agent follows instructions best with concrete rules based on clear triggers. The map remains authoritative, and how a client's agent uses the rendering is set out in [Installation](method/ndd.map.md#installation). A rule's source node is read on demand rather than preemptively at start.

**Detail**

It is hand-maintained in `method/`, where its links to `ndd.map.md` resolve exactly as they do in a client's `ndd/method/`. A change that edits a node an agent rule cites updates the rule in the same build; drift noticed otherwise is corrected on sight.

Which rules it carries is settled by [Rule Selection](#rule-selection).


# Rule Layout

[↑ Agent Rules](#agent-rules)

```yaml
id: r4l
signers:
  tearne: {at: 2026-11-03, hash: 44ba6e37}
```

The rendering gathers by trigger what the map holds by concept, so an agent finds everything for one trigger in one rule. The trigger is named in each rule's first sentence, as [Rule Phrasing](#rule-phrasing) sets out; the concept is named in its heading.

- Each rule sits under a short level-3 heading naming its source node. Where several rules come from one node, each heading adds what that rule covers, as in *Engagement Rule: Corrections*.

- Each rule closes with links to the nodes it renders, unless it already links them inline as nodes to be read.

- A rule with an occasional trigger, such as a session's start or a move between lifecycle stages, points to its node to be read and keeps only what shows it was followed. A rule that holds on every turn or fires often carries its substance in full, as a read each time would be skipped.


# Rule Phrasing

[↑ Agent Rules](#agent-rules)

```yaml
id: f7m
signers:
  tearne: {at: 2026-10-22, hash: 340edf62}
```

Phrasing is intended to maximise compliance.

- Each rule is trigger-centred: its first sentence states the act as a trigger the agent can recognise, or says that it applies to everything the agent writes. The rest gives the reason — agents generalise from explanation rather than bare instruction.

- A rule that forbids something names the required alternative instead — "leave git writes to the user", not "never commit" — because a bare prohibition raises the salience of the thing it forbids.

- A rule with no exception ends by saying what to do when it cannot be followed, usually to stop and ask; an unconditional "always" invites the agent to fabricate compliance.


# Rule Selection

[↑ Agent Rules](#agent-rules)

```yaml
id: q7s
```

A rule earns its place in the rendering by three tests:

- It applies in almost every session
- A reader can tell whether it was followed
- Getting it wrong is costly or already has been

The second test carries most weight: a rule whose observance leaves a trace in the agent's message — a count, a named file — holds, while one satisfied by silence slips unnoticed.

Everything else stays in the map. A rule that fails a test should be adapted, cut, or as a last resort, left in the map at the risk of not being followed.

The rendering stays short because adherence degrades with instruction count, and across all rules at once, so each rule kept taxes the rest.

If, at rendering time, the agent reviewing the rule set finds it sub-optimal, the issues should be traced upstream to this map and discussed.


# Rule Testing

[↑ Agent Rules](#agent-rules)

```yaml
id: t5r
signers:
  tearne: {at: 2026-11-04, hash: 42050ea7}
```

A rule can read well and still backfire, because what an agent does with it shows only in use. Each new or reworded rule is therefore tested before it ships: subagents are given the same task, some with the rule as it stood, or without it, and some with the new wording, and what they produce is compared.

**Detail**

The task tempts the failures the rule targets and probes where it might overreach, in two forms: a fresh draft, and a small edit to text that already breaks the rule, which shows whether the rule pushes an unasked rewrite. The subagents see the rule but not the map, since in use an agent works from the rule rather than the node behind it. A difference that matters sends the rule back to drafting, and the outcome goes in the change's [Log](method/ndd.map.md#log).


# Map Viewer

[↑ NDD Project](#ndd-project) \
[Sign-off Button](#sign-off-button) \
[Request Guards](#request-guards) \
[Write Checks](#write-checks) \
[Due Nodes](#due-nodes) \
[Request Bar](#request-bar) \
[Navigation](#navigation)

```yaml
id: mv4
signers:
  tearne: {at: 2026-11-26, hash: fc370aa0}
```

`method/util/map_viewer.py` is a [POS](method/standards/POS.md) script serving a map in the browser for review. Having no login, it listens on 127.0.0.1 only, and it writes nothing but the stamps in a node's [scaffolding block](method/ndd.map.md#node-identity).

- **Tree** — the contents beneath the entry map's root heading, followed through child links, each file's part shaded and named.

- **Node** — the node rendered, with each signer's [stamp state](method/ndd.map.md#stamp-states) marked.

- **Sign-off diff** — for a stale stamp, the signed-off text found in git by its fingerprint, and what changed since.

- **[Sign off](#sign-off-button)** — on a node, a button stamping it, or requesting or withdrawing a request, for the names ticked.

- **[Due for](#due-nodes)** — the nodes due for the people ticked, marked in the tree.

- **[Request](#request-bar)** — the nodes picked in the tree, requested from the people ticked or their requests withdrawn.

It carries its own copy of the [Fingerprint](method/ndd.map.md#fingerprint) rule, kept in step by [Fingerprint Check](testing.map.md#fingerprint-check).


# Sign-off Button

[↑ Map Viewer](#map-viewer)

```yaml
id: vs1
signers:
  tearne: {at: 2026-11-26, hash: fe49cfea}
```

Beside a node's sign-offs, a *Sign off* button opens a drop-down of names to tick and a choice of what *Apply* does for each, set to *sign off* on opening:

- **sign off** — stamp the fingerprint of the text shown;

- **request** — add a [request](method/ndd.map.md#stamp-states), if the name has no stamp;

- **withdraw** — remove the name's request.

A sign-off diff, showing an old version, has no button.

The drop-down lists every handle in the map's stamps and any name added in that browser, which alone are removable and are kept there until removed. The last names ticked are ticked again.

Each stamp is a line under the node's `signers:` key, dated today; the key is added if missing, or renamed from an older `approvals:`, and nothing else is written; writes are guarded as [Request Guards](#request-guards) and [Write Checks](#write-checks) describe. Committing is left to the user, prompted by a red light at the page's top right while anything is uncommitted.


# Request Guards

[↑ Map Viewer](#map-viewer)

```yaml
id: vs2
signers:
  tearne: {at: 2026-11-24, hash: fc9768cb}
```

- **Forged form** — another site could have a visitor's browser post a write to the viewer, unseen. Each run picks a random token, carried only in the viewer's own pages, which other sites cannot read; a write is accepted only by POST and only with the token.

- **DNS rebinding** — a site could point its own name at 127.0.0.1, so that the browser treats it as the viewer and lets it read and write the map. Every request is refused unless its Host is 127.0.0.1 or localhost, and every write unless its Origin is too.


# Write Checks

[↑ Map Viewer](#map-viewer)

```yaml
id: vw3
signers:
  tearne: {at: 2026-11-25, hash: 21e2ed15}
```

- **Stale page** — if a node changed on disk after its page was rendered, someone could sign off text they were not shown. The page carries the node's fingerprint as rendered, returned with a sign-off as a receipt, and the server refuses if it differs from the fingerprint on disk. A request or its withdrawal needs no receipt: neither records a fingerprint or touches a sign-off.

- **Partial write** — a request or withdrawal on several nodes, across map files, could be written for some nodes and not others. Every node is checked before anything is written: if any cannot take the write — a missing file or node, *Contents*, or for a request no scaffolding block — nothing is, and the reply names each such node and why. A name already stamped, or with no request to withdraw, is skipped, not counted as a failure.


# Due Nodes

[↑ Map Viewer](#map-viewer)

```yaml
id: vd5
signers:
  tearne: {at: 2026-11-25, hash: c148157e}
```

Above the tree, *Due for …* toggles a bar holding a drop-down of the [signers](method/ndd.map.md#signer) in the map's stamps, which closes on a click elsewhere, and a count. Each node [due](method/ndd.map.md#sign-off) for any person ticked is shaded orange in the tree, so what awaits their sign-off shows at a glance, and the count is of those nodes. Opening it closes the [request bar](#request-bar). Whether it is open, and who is ticked, are kept in that browser.


# Request Bar

[↑ Map Viewer](#map-viewer)

```yaml
id: vr6
signers:
  tearne: {at: 2026-11-25, hash: ceab9d20}
```

Above the tree, *Request …* toggles a bar to request sign-off on several nodes at once, or withdraw requests. While it is open, each node in the tree gains a box to pick it by, and with *children* ticked, picking a node picks everything below it too. The bar holds:

- a drop-down of names, offering the same as [Sign off](#sign-off-button)'s and closing like [Due for](#due-nodes)'s;

- a choice of *request* or *withdraw*, as in Sign off's, set to *request* on opening;

- an *Apply* button.

*Apply* acts as chosen for each name ticked on each node picked, checked as [Write Checks](#write-checks) describes. The bar then closes, clearing the picks, and *Due for* opens on the names ticked. Opening the bar closes the Due for bar, and whether *children* is ticked is kept in that browser.


# Navigation

[↑ Map Viewer](#map-viewer)

```yaml
id: vn7
signers:
  tearne: {at: 2026-11-25, hash: 1f1dbdb3}
```

Following a link replaces only the page's content, so the tree keeps its folds, and the current node is marked in it and scrolled into view. A branch's button, shown on hover, folds it and everything below, or opens it all once all of it is folded.

*Split* opens a second pane beside the node, where the node's links then open, as do the pane's own. Each pane scrolls on its own and has its own back and forward buttons. *Swap* exchanges the panes and *Close* shuts the second.


# Method Map Form

[↑ NDD Project](#ndd-project)

```yaml
id: f3c
signers:
  tearne: {at: 2026-11-04, hash: b9fd3121}
```

NDD's own method map is concept-first: each fact is owned by the concept it concerns, and a node for a moment in the workflow, such as [Archiving](method/ndd.map.md#archiving) or the [Startup Scan](method/ndd.map.md#startup-scan), lists its steps as links to their owners. This is the [Economy](method/ndd.map.md#economy) convention chosen for this project, not one NDD imposes. The [agent rules](#agent-rules) take the other axis, gathering by trigger, as [Rule Layout](#rule-layout) sets out.
