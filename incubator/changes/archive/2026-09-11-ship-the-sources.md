# Ship the sources

**Cadence:** Formal

## Intent

_(Approved 2026-09-11.)_

Ship the sources as they are. The installer copies `map.md`, `ndd.map.md`, `CHANGELOG.md`, `standards/` and `AGENT-RULES.md` from the checkout root into a client's `ndd/`, with no rendering step between: `dist/`, `build.py`, the detach and the stale check all go. A client sees NDD Project above the method, and every link resolves because the files keep their names and neighbours. `AGENT-RULES.md` moves to the root, where its links resolve as they do in `ndd/`, so the agent developing the method reads the source maps directly.

## Context

Raised on 2026-09-11 at the end of change 255, after the agent proposed two sentence-sized fixes for the gap between the source maps and the vendored copy the agent reads: an obligation to update `AGENT-RULES.md` in the same build as any node a rule cites, and a self-install at every Conclude that touches the method. The user went further: if nothing is transformed, ship the sources. This retires Dist Directory and reshapes Distribution, Installer and Release Steps in the project map. The rules-update obligation still wants its sentence, in Agent Rules. A client's install then holds `ndd/map.md`, a second file of that name in their tree; Map Files makes the root one the entry point, but the reading may want a word.

## Held

_(Empty. The dogfooding question was answered in the Approach on 2026-09-11.)_

## Approach

_(Approved 2026-09-11.)_

- **The installer copies a named list from the checkout root**: `map.md`, `ndd.map.md`, `CHANGELOG.md`, `AGENT-RULES.md` and `standards/`. A list rather than everything, because the checkout also holds `changes/`, the README and the installer itself. `dist/`, `build.py`, the detach and the stale check are deleted. Run from its own checkout it refuses, since this repository reads its sources directly.

- **Only the method map is backed up**, as `ndd.prev.map.md`, since it is the migration diff the agent reads; `map.md` is pipeline, not method. `ndd.md` and `ndd.prev.md` stay retired.

- **`AGENT-RULES.md` lives at the root.** Its links name `ndd.map.md` as a sibling, true at the root and in a client's `ndd/`, so one file serves both unedited.

- **This repository reads its own sources.** `CLAUDE.md` and `AGENTS.md` point at the root `AGENT-RULES.md`, are committed, and leave `.gitignore`. That answers the held question: constant dogfooding, on purpose — the session that edits the method runs it, so a bad rule is felt at once rather than at the next release.

- **The rules-update obligation gets its sentence** in Agent Rules: a change that edits a node an agent rule cites updates the rule in the same build. Nothing mechanical enforces it, so the map must say it.

- **A client's `ndd/map.md` is named, not renamed.** Distribution says the vendored `map.md` is NDD's project map, not the client's; Map Files already makes the root one the entry point, and renaming would break the branch's parent link.

- **Map edits follow the deletions.** Dist Directory is retired; Distribution, Installer and Release Steps are rewritten to the plain copy; the release checklist becomes a version bump and a self-install.

- **Proof is an install into a scratch directory**, checking every vendored link resolves and `CLAUDE.md` there is created as a pointer; this repository is never installed into itself, and its `ndd/` is deleted.
## Worklist

_(Approved 2026-09-11. Build started the same day.)_

**Tooling and files**

- [x] `install.py`: copy the named list from the checkout root; refuse when run from its own checkout; drop the build import and stale check; back up only `ndd.map.md`.
- [x] `AGENT-RULES.md` moved from `dist/` to the root.
- [x] `dist/`, `build.py` and this repository's `ndd/` deleted.
- [x] `CLAUDE.md` and `AGENTS.md` pointed at the root rules file and removed from `.gitignore`.

**Map edits**

- [x] Dist Directory retired; Distribution's child link and the Contents list follow.
- [x] Distribution: the plain copy from the checkout, and that the vendored `map.md` is NDD's project map.
- [x] Installer: the named list, the refusal in its own checkout, the backup; self-vendoring remark gone.
- [x] Release Steps: a version bump and a scratch-directory install.
- [x] Agent Rules: the same-build update obligation.

**Proof**

- [x] Install into a scratch directory; check every vendored link resolves and `CLAUDE.md` there is a pointer.
- [x] Rule 2's "re-read at the start of every Build" and any rule naming `ndd/` still read true from the root.

## Log
- 2026-09-11 — Tooling group done. The rules file's orientation was reworded at the root (user's framing: a client has two maps, theirs and NDD's, with ndd.map.md a branch of NDD's); it now links to Distribution as its source node, so Distribution's rewrite (task 6) must carry that picture.
- 2026-09-11 — Map edits done. Distribution and Installer re-cut so the model sits in the parent and the mechanics in the child, after the user noticed the repetition. Release Steps no longer says a release is "cut", which contradicted Distribution's moving-edge line. Agent Rules carries the same-build obligation and names Distribution as the orientation's source.
- 2026-09-11 — Proof: install into an empty scratch directory created ndd/ with the five shipped items, CLAUDE.md and AGENTS.md as pointers and the four .gitignore entries; every link in the vendored rules and maps resolves; the own-checkout refusal fires here. Sources also clean: links, reciprocity, Contents.

## Conclude

_(Approved 2026-09-11.)_

Nothing is rendered any more. The installer copies the five source items from the checkout root into a client's `ndd/`, refuses to run in its own checkout, and `dist/`, `build.py` and this repository's vendored `ndd/` are gone. `AGENT-RULES.md` lives at the root with `CLAUDE.md` and `AGENTS.md` committed and pointing at it, so this repository runs the method it is editing. Dist Directory is retired; Distribution carries the client's two-maps picture as the rules' orientation source.
