# NDD Project

[Contents](#contents)
[Distribution](#distribution)
[Testing](testing.map.md#testing)
[NDD](ndd.map.md#ndd)

```yaml
id: p1j
```

The repository that develops and ships Non-Dead Design. The method itself is the [NDD](ndd.map.md#ndd) branch, kept in its own file because it is what ships: a client receives that branch alone, as its method map. This trunk holds what stays behind: how the method is built into a distributable, released and installed. The reasoning behind the method is under [Principles](ndd.map.md#principles).

- **Distribution** — how NDD reaches a client project: the shipped layout, the release checklist, the installer and the agent rules.

- **Testing** — how this repository checks itself: the checks, their runnable forms under `tests/`, shipped so clients have access to tests which matter.

- **NDD** — the method, in `ndd.map.md`.


# Contents

[↑ NDD Project](#ndd-project)

```yaml
id: ct6
```

- [NDD Project](#ndd-project)
  - [Distribution](#distribution)
    - [Release Steps](#release-steps)
    - [Installer](#installer)
    - [Agent Rules](#agent-rules)
      - [Rule Form](#rule-form)
      - [Rule Selection](#rule-selection)
  - [Testing](testing.map.md#testing)
  - [NDD](ndd.map.md#ndd)


# Distribution

[↑ NDD Project](#ndd-project)
[Release Steps](#release-steps)
[Installer](#installer)
[Agent Rules](#agent-rules)

```yaml
id: d5v
```

NDD is distributed as a git checkout: the user clones this repository and runs its [installer](#installer) from within their own project, which vendors the method into an `ndd/` subdirectory there. Upgrading is `git pull` in the checkout, then the same run.

A client project then holds two maps: its own in the project root, and NDD's under `ndd/`, whose `map.md` is this project map and whose `ndd.map.md` is the part the agent rules link to. Nothing is rendered on the way, so a client reads exactly what this repository reads.

`main` is the single moving edge — no cut releases; the shipped `CHANGELOG.md` names the current version.


# Release Steps

[↑ Distribution](#distribution)

```yaml
id: l2s
```

The checklist for a new version of NDD, published by moving `main`. After [archiving](ndd.map.md#archiving) the agent asks whether it is time for one and the user decides. If several changes are obviously shipping together no need to ask. If releasing, a full [Map Review](ndd.map.md#map-review) is offered first, then the agent confirms the user wants each of the following:

1. Bump the version: a new entry at the top of `CHANGELOG.md`.
2. Run every test under [Testing](testing.map.md#testing) and see it pass, so what ships is what its nodes say.


# Installer

[↑ Distribution](#distribution)

```yaml
id: n5w
```

A [POS-style](standards/POS.md) `install.py` script at the root of this project, run by a consumer from their own project to install or upgrade NDD. It:

- copies every file git tracks in this checkout into `ndd/`, scripts still executable, except `CLAUDE.md` and `AGENTS.md`; a changed `ndd.map.md` is backed up as `ndd.prev.map.md` and retired files are removed;

- points `CLAUDE.md` and `AGENTS.md` at `ndd/AGENT-RULES.md`; a file that only contains pointers into `ndd/` is replaced, anything else is left with a warning;

- ensures `ndd/`, the two agent entry files and `.claude/` are in `.gitignore`.

It owns `ndd/` outright but never overwrites other files in the consumer's project.

**Detail**

It refuses to run from its own checkout directory; this repository reads its sources directly and is never installed into itself.


# Agent Rules

[↑ Distribution](#distribution)
[Rule Form](#rule-form)
[Rule Selection](#rule-selection)

```yaml
id: r8d
```

`AGENT-RULES.md` is a rendering of the core rules within this map, optimised for agents; an agent follows instructions best with concrete rules based on clear triggers. This map remains authoritative. It is hand-maintained at the checkout root, where its links to `ndd.map.md` resolve exactly as they do in a client's `ndd/`. A change that edits a node an agent rule cites updates the rule in the same build, since nothing mechanical keeps the rendering in step. Each agent rule names its source node, and the agent is instructed to read it on demand, not preemptively at start.

**Detail**

The agent re-reads the file at the start of every [Build](ndd.map.md#build) and after any context compaction. Which rules it carries is settled by [Rule Selection](#rule-selection). Its orientation paragraph has [Distribution](#distribution) as its source.


# Rule Form

[↑ Agent Rules](#agent-rules)

```yaml
id: f7m
```

Each rule in the rendering is phrased to maximise compliance.

- Each rule sits under a short, numbered level-3 heading, so markdown tooling can navigate and rules can be named.

- Its first sentence states the act as a trigger the agent can recognise, or says that it applies to everything the agent writes. The rest gives the reason — agents generalise from explanation rather than bare instruction.

- A rule that forbids something names the required alternative instead — "leave git writes to the user", not "never commit" — because a bare prohibition raises the salience of the thing it forbids.

- A rule with no exception ends by saying what to do when it cannot be followed, usually to stop and ask; an unconditional "always" invites the agent to fabricate compliance.

- The rule closes with a link to its source node.


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

If, at rendering time, the agent reviewing the rules set identifies they are sub-optimal the issues should be traced upstream to this map and discussed.
