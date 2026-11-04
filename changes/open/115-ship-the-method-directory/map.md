# NDD Project

[Contents](#contents) \
[Distribution](#distribution) \
[Testing](testing.map.md#testing) \
[Method Map Form](#method-map-form)

```yaml
id: p1j
approvals:
  tearne: {at: 2026-11-04, hash: 1b3b9b8b}
```

The repository that develops and ships Non-Dead Design. The method itself has its own map, [NDD](method/ndd.map.md#ndd), which this project builds and ships as an asset rather than as a branch. This map describes how the method is distributed, released and installed. The reasoning behind the method is under [Principles](method/ndd.map.md#principles).

- **[Distribution](#distribution)** — how NDD reaches a client project: the shipped layout, the release checklist, the installer and the agent rules.

- **[Testing](testing.map.md#testing)** — how this repository checks itself: the checks and their runnable forms under `tests/`.

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
  - [Method Map Form](#method-map-form)


# Distribution

[↑ NDD Project](#ndd-project) \
[Release Steps](#release-steps) \
[Installer](#installer) \
[Agent Rules](#agent-rules)

```yaml
id: d5v
approvals:
  tearne: {at: 2026-11-04, hash: f34ff91c}
```

NDD is distributed as a git checkout: the user clones this repository and runs its [installer](#installer) from within their own project, which vendors the method into an `ndd/` subdirectory there, as [Installation](method/ndd.map.md#installation) describes from the client's side.

Only the method ships, as [Shipped Assets](#shipped-assets) lists; this project map and the testing map stay here. Nothing is rendered on the way, so a client reads exactly what this repository reads.

`main` is the single moving edge — no cut releases; the shipped `CHANGELOG.md` names the current version.


# Release Steps

[↑ Distribution](#distribution)

```yaml
id: l2s
approvals:
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
approvals:
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
approvals:
  tearne: {at: 2026-11-04, hash: 40393b0e}
```

The installer copies into a client's `ndd/` only what the agent and user need at run time:

- `method/`, holding the agent rules, the method map, the fingerprint helper and the standards.
- `CHANGELOG.md`, `README.md` and `LICENSE`, from the root.

Everything else stays in the checkout, for example `map.md`, `changes/`, `tests/` and `install.py`. The [Install Check](testing.map.md#install-check) catches a shipped file linking outside what ships.


# Agent Rules

[↑ Distribution](#distribution) \
[Rule Layout](#rule-layout) \
[Rule Phrasing](#rule-phrasing) \
[Rule Selection](#rule-selection) \
[Rule Testing](#rule-testing)

```yaml
id: r8d
approvals:
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
approvals:
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
approvals:
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
approvals:
  tearne: {at: 2026-11-04, hash: 42050ea7}
```

A rule can read well and still backfire, because what an agent does with it shows only in use. Each new or reworded rule is therefore tested before it ships: subagents are given the same task, some with the rule as it stood, or without it, and some with the new wording, and what they produce is compared.

**Detail**

The task tempts the failures the rule targets and probes where it might overreach, in two forms: a fresh draft, and a small edit to text that already breaks the rule, which shows whether the rule pushes an unasked rewrite. The subagents see the rule but not the map, since in use an agent works from the rule rather than the node behind it. A difference that matters sends the rule back to drafting, and the outcome goes in the change's [Log](method/ndd.map.md#log).


# Method Map Form

[↑ NDD Project](#ndd-project)

```yaml
id: f3c
approvals:
  tearne: {at: 2026-11-04, hash: b9fd3121}
```

NDD's own method map is concept-first: each fact is owned by the concept it concerns, and a node for a moment in the workflow, such as [Archiving](method/ndd.map.md#archiving) or the [Startup Scan](method/ndd.map.md#startup-scan), lists its steps as links to their owners. This is the [Economy](method/ndd.map.md#economy) convention chosen for this project, not one NDD imposes. The [agent rules](#agent-rules) take the other axis, gathering by trigger, as [Rule Layout](#rule-layout) sets out.
