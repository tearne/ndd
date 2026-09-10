# Maps as a file type

**Cadence:** Formal

## Intent

_(Approved 2026-09-10. Reframed from "meta.md as a second tree" on approval.)_

Define a map as a file type. A `.map.md` file is one tree: a root, a Contents node, and nodes linked by name. A project may hold several, one per concern, linked across files the way nodes link within one. The first split moves how a project builds, ships and constrains itself out of the product map into `meta.map.md`: release steps, distribution, tooling, non-functional requirements. NDD's product map then ships to clients without its own pipeline, and stakeholder sign-off covers only the specification.

## Context

Costs to weigh: two roots and two Contents; cross-file links (`meta.map.md#node`); every tool that walks the map must know every map file; Map Structure, META, Bootstrapping and the installer all assume one file. The existing META subtree (Distribution, Release Steps, Installer, Dist Directory, Agent Rules) would lift mechanically into the new root. Change 220 leaked an NDD-specific pointer into the generic Archiving node for the shipping reason; Archiving now reads generically, so check whether that leak is already gone. The naming of the product map (`map.map.md` reads oddly) and of the vendored method map is for the Approach. Later concerns such as testing (change 275) could follow the same pattern. Was to be planned alongside 80, which is built and archived (2026-09-10).

## Approach

_(Approved 2026-09-10.)_

- **One tree, several files.** A project has one map; a file is only where a branch lives. Every existing rule about roots, links and overviews stays true, with no second root or Contents to reconcile.

- **The entry point is `map.md`, unchanged.** A fixed name lets a reader and the agent find the start among several map files without opening them; a name derived from the project is exactly that lookup. Nothing moves for existing projects.

- **A branch lives in `<node>.map.md`**, lowercased, named for the node it hangs from, so the file list reads as a table of branches.

- **No new node kind.** A node whose children are in another file has cross-file child links, and the branch's top node keeps a parent link back. Links already carry the tree; the hanging node's prose explains the branch's scope.

- **Each file carries its own overview**, since a branch can ship alone. The entry Contents shows the tree down to each branch's top node and names its file.

- **Shipping detaches a branch.** `build.py` copies `ndd.map.md` to `dist/` dropping the top node's parent link, so it arrives as a root. Installer and agent rules refer to `ndd.map.md`; the previous version is kept as `ndd.prev.map.md`.

- **This repository inverts.** `map.md` becomes the project, rooted at **NDD Project** since the branch's top node, renamed **NDD** so the file rule holds without exception, takes the method's name: Distribution, Release Steps, Installer, Dist Directory and Agent Rules as its children, plus the method as a branch in `ndd.map.md`. Same rule as a client's, different proportions.

- **META is retired.** With files as branches there is nothing left that is "about the map" rather than part of it. Each file's top node carries the overview of the nodes in that file, stopping where a branch continues in another file and naming it; Tidy maintains it per file as now. Contents goes with META; Rationale becomes an ordinary node under the method's root.

- **The convention gets a node, Map Files**, child of Map Structure, because tools and the agent depend on it and Map Structure is already over the bound. Map Structure's splitting sentence becomes a pointer; Navigation Links gains a clause on the cross-file link form.

- **Dogfooding is the proof.** Build, then run the installer from this checkout; a clean run with the vendored `ndd/ndd.map.md` resolving from the agent rules is the test.

## Worklist

_(Approved 2026-09-10. Build started the same day. Map Files and the Distribution-subtree edits are done after the split they describe; the rest in order.)_

**Method map edits**

- [x] Map Files: new child of Map Structure holding the file convention.
- [x] Map Structure: overview lives in the file's top node; splitting sentence becomes a pointer to Map Files.
- [ ] Navigation Links: the cross-file link form.
- [ ] META retired: node removed, root child link removed, orientation paragraph dropped.
- [ ] Root renamed NDD; every link naming it re-pointed.
- [ ] Contents retired: overview moves into the NDD node, showing the method branch.
- [ ] Rationale re-parented under NDD.
- [ ] Tidy: overview maintained per file (correction if meaning holds).
- [ ] Dist Directory, Distribution, Installer, Agent Rules: `ndd.map.md`, the parent-link drop, `ndd.prev.map.md`.

**Restructure this repository**

- [ ] `map.md` rooted at NDD Project, with Distribution and its subtree as children, the method as a branch, and the project overview.
- [ ] Method branch in `ndd.map.md`, top node with a parent link to NDD Project.
- [ ] Agent rules: links to `ndd.map.md#…`; the two-maps orientation line.

**Tooling**

- [ ] `build.py`: copy `ndd.map.md` to `dist/` dropping the top node's parent link; `dist/ndd.md` removed.
- [ ] `install.py`: back up as `ndd.prev.map.md`; `ndd.md` and `ndd.prev.md` retired on upgrade.
- [ ] Build, then install from this checkout; confirm `ndd/ndd.map.md` arrives as a root, the old files are removed, and every agent-rules link resolves.

## Log

- 2026-09-10 — Map Files written, then edited by the user: branch naming relaxed to "a name related to the node", in a file beside or beneath it; the detach-on-copy rule dropped from the method. Detaching stays as NDD's own shipping step, to be described under Dist Directory in the project map (task 9), not as a method rule. The relaxed naming removes the reason given for renaming the root to NDD (task 5); user confirmed the rename stands as a preference.
- 2026-09-10 — Paused after task 2. Tasks 1 and 2 are written in map.md (Map Files at its final text after user edits; Map Structure edited). Resume at task 3, Navigation Links. Nothing is committed.
