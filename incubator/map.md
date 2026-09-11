# NDD Project

```yaml
id: p1j
```

[Contents](#contents)
[Distribution](#distribution)
[NDD](ndd.map.md#ndd)

The repository that develops and ships Non-Dead Design. The method itself is the [NDD](ndd.map.md#ndd) branch, kept in its own file because it is what ships: a client receives that branch alone, as its method map. This trunk holds what stays behind: how the method is built into a distributable, released and installed. The reasoning behind the method is under [Principles](ndd.map.md#principles).

- **Distribution** — how NDD reaches a client project: the shipped layout, the release checklist, the installer and the agent rules.
- **NDD** — the method, in `ndd.map.md`.


# Contents

```yaml
id: ct6
```

[↑ NDD Project](#ndd-project)

- [NDD Project](#ndd-project)
  - [Distribution](#distribution)
    - [Dist Directory](#dist-directory)
    - [Release Steps](#release-steps)
    - [Installer](#installer)
    - [Agent Rules](#agent-rules)
      - [Rule Form](#rule-form)
      - [Rule Selection](#rule-selection)
  - [NDD](ndd.map.md#ndd)


# Distribution

```yaml
id: d5v
```

[↑ NDD Project](#ndd-project)
[Dist Directory](#dist-directory)
[Release Steps](#release-steps)
[Installer](#installer)
[Agent Rules](#agent-rules)

NDD is distributed as a git checkout. The consumer clones the NDD repository and runs `install.py` from their own project; it copies the contents of the checked-in [`dist/`](#dist-directory) directory into `ndd/`, file for file, and writes the agent entry files, leaving the project's own map and changes untouched. Upgrading is `git pull` in the checkout, then the same run.

`main` is the single moving edge — no cut releases; the shipped changelog names the current version, and the previous map is kept alongside as the agent's migration diff. See [Dist Directory](#dist-directory) for what ships, how `build.py` renders it and why it is laid out as it is, [Release Steps](#release-steps) for what happens before it ships, [Installer](#installer) for the mechanics, and [Agent Rules](#agent-rules) for the one shipped file that is not a copy of a source.


# Dist Directory

```yaml
id: d8r
```

[↑ Distribution](#distribution)

The checked-in `dist/` directory is what ships on client installation. It holds a branch of this repository's map, but a branch cannot ship as it stands: its top node links up to NDD Project, which a consumer does not have. `dist/` holds the shipped layout after modification, so installing is a plain file copy rather than files being quietly modified by an installer.

`build.py`, at the root beside the installer, renders the map branch: `ndd.map.md` is copied with its top node's parent link dropped, so it arrives as a root, and `CHANGELOG.md` and the `standards/` guides are copied unchanged. The one file it does not touch is `dist/AGENT-RULES.md`, which is maintained there directly because its links target `ndd.map.md` and resolve only in that layout. `build.py --check` reports what is stale against what the build would write.


# Release Steps

```yaml
id: l2s
```

[↑ Distribution](#distribution)

The checklist for cutting a release of NDD. After [archiving](ndd.map.md#archiving) the agent asks whether it is time to release and the user decides. If several changes are obviously shipping together no need to ask. If releasing, the [Maintenance](ndd.map.md#maintenance) due before release are offered, then the agent confirms the user wants each of the following:

1. Bump the version: a new entry at the top of `CHANGELOG.md`.
2. Run `./build.py` so `dist/` matches the sources.
3. Run `./install.py` from this checkout. It refuses a stale `dist/`, so a clean run is the pre-ship test, and it refreshes the self-vendored `ndd/` the agent reads here.
4. Report if any file in `dist/` which should ship is ignored.

Nothing enforces the order but the agent; the [Installer](#installer)'s refusal is the backstop if a step is skipped.


# Installer

```yaml
id: n5w
```

[↑ Distribution](#distribution)

A [POS-style](standards/POS.md) installer script, `install.py` at the root of the NDD repo, is run by a consumer from their own project to install or upgrade NDD. It owns `ndd/` but never overwrites other files in the consumer's project. It:

- copies [`dist/*`](#dist-directory) into `ndd/`, keeping a changed `ndd.map.md` as `ndd.prev.map.md` and removing retired files;

- points `CLAUDE.md` and `AGENTS.md` at `ndd/AGENT-RULES.md`; a file that is only a pointer into `ndd/` is replaced, anything else is left with a warning;

- ensures `ndd/`, the two entry files and `.claude/` are in `.gitignore`.

**Detail**

It aborts if `dist/` is stale against its sources, or if the target `ndd/` would overwrite this project's root itself; any other target is allowed, which lets this repository dogfood by self-vendoring. `install.py --version` reads the top `CHANGELOG.md` heading.


# Agent Rules

```yaml
id: r8d
```

[↑ Distribution](#distribution)
[Rule Form](#rule-form)
[Rule Selection](#rule-selection)

`AGENT-RULES.md` is a rendering of the core rules within this map, optimised for agents; an agent follows instructions best with concrete rules based on clear triggers. This map remains authoritative. Each agent rule names its source node, and the agent is instructed to read it on demand, not preemptively at start.

**Detail**

The agent re-reads the file at the start of every [Build](ndd.map.md#build) and after any context compaction. Which rules it carries is settled by [Rule Selection](#rule-selection).


# Rule Form

```yaml
id: f7m
```

[↑ Agent Rules](#agent-rules)

Each rule in the rendering is phrased to maximise compliance.

- Each rule sits under a short, numbered level-3 heading, so markdown tooling can navigate and rules can be named.

- Its first sentence states the act as a trigger the agent can recognise, or says that it applies to everything the agent writes. The rest gives the reason — agents generalise from explanation rather than bare instruction.

- A rule that forbids something names the required alternative instead — "leave git writes to the user", not "never commit" — because a bare prohibition raises the salience of the thing it forbids.

- A rule with no exception ends by saying what to do when it cannot be followed, usually to stop and ask; an unconditional "always" invites the agent to fabricate compliance.

- The rule closes with a link to its source node.


# Rule Selection

```yaml
id: q7s
```

[↑ Agent Rules](#agent-rules)

A rule earns its place in the rendering by three tests:

- It applies in almost every session
- A reader can tell whether it was followed
- Getting it wrong is costly or already has been

The second test carries most weight: a rule whose observance leaves a trace in the agent's message — a count, a named file — holds, while one satisfied by silence slips unnoticed.

Everything else stays in the map. A rule that fails a test should be adapted, cut, or as a last resort, left in the map at the risk of not being followed.

The rendering stays short because adherence degrades with instruction count, and across all rules at once, so each rule kept taxes the rest.

If, at rendering time, the agent reviewing the rules set identifies they are sub-optimal the issues should be traced upstream to this map and discussed.
