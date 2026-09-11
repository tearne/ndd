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
- [x] Navigation Links: the cross-file link form.
- [x] Parent link marked with a leading `↑`: the rule in Navigation Links and Formatting, then every node re-typeset as a correction (added 2026-09-10; arrow chosen over a blank line).
- [x] META retired: node removed, root child link removed, orientation paragraph dropped.
- [x] Root renamed NDD; every link naming it re-pointed.
- [x] Contents retired: overview moves into the NDD node, showing the method branch.
- [x] Rationale dropped rather than re-parented (see Log).
- [x] Tidy: overview maintained per file (correction if meaning holds).
- [x] Dist Directory, Distribution, Installer, Agent Rules: `ndd.map.md`, the parent-link drop, `ndd.prev.map.md`. (Distribution and Agent Rules needed nothing; Bootstrapping's file name corrected too.)

**Restructure this repository**

- [x] `map.md` rooted at NDD Project, with Distribution and its subtree as children, the method as a branch, and the project overview.
- [x] Method branch in `ndd.map.md`, top node with a parent link to NDD Project.
- [x] Agent rules: links to `ndd.map.md#…`; the two-maps orientation line.

**Tooling**

- [x] `build.py`: copy `ndd.map.md` to `dist/` dropping the top node's parent link; `dist/ndd.md` removed.
- [x] `install.py`: back up as `ndd.prev.map.md`; `ndd.md` and `ndd.prev.md` retired on upgrade.
- [x] Build, then install from this checkout; confirm `ndd/ndd.map.md` arrives as a root, the old files are removed, and every agent-rules link resolves.

## Log

- 2026-09-10 — Map Files written, then edited by the user: branch naming relaxed to "a name related to the node", in a file beside or beneath it; the detach-on-copy rule dropped from the method. Detaching stays as NDD's own shipping step, to be described under Dist Directory in the project map (task 9), not as a method rule. The relaxed naming removes the reason given for renaming the root to NDD (task 5); user confirmed the rename stands as a preference.
- 2026-09-10 — Paused after task 2. Tasks 1 and 2 are written in map.md (Map Files at its final text after user edits; Map Structure edited). Resume at task 3, Navigation Links. Nothing is committed.
- 2026-09-10 — User asked how a reader tells the root's first child link from a parent link. Agreed a blank line between the parent link and the child links, so the root's link block has one paragraph and every other node's has two. Added as a task before the split.
- 2026-09-10 — Split done: ndd.map.md holds the method (57 nodes, NDD at the top with ↑ NDD Project), map.md holds NDD Project with the Distribution subtree (8 nodes). Rationale dropped instead of re-parented: it was a one-line pointer to Principles, which the root already names. Map Files' example cross-file link now cites the real one, map.md#release-steps. Every link in both files resolves.
- 2026-09-11 — Arrow moved inside the parent link text, `[↑ Parent](#parent)`, so the cursor lands on the link; rule wording in Navigation Links and Formatting updated, Fingerprint's clause reverted since the line is a plain link line again. 64 nodes re-typeset.
- 2026-09-11 — Overview moved out of the top nodes into a Contents node per file (first child of the top node), as a nested list of links regenerated from the navigation links; the box-drawing form is gone. Map Structure and Map Files reworded to match. User asked for a Principles link in NDD Project's prose.
- 2026-09-11 — Contents as a nested list of links is on trial; the user is unsure and may revert to the box-drawing sketch. NDD Project gained a Principles link.
- 2026-09-11 — Tidy needed no change: its wording holds per file. build.py now ships ndd.map.md detached (parent link dropped) and compares dist against rendered content; install.py backs up to ndd.prev.map.md and retires ndd.md and ndd.prev.md; dist/AGENT-RULES.md links target ndd.map.md and its orientation mentions branch files. Built and installed from this checkout: ndd/ndd.map.md arrives as a root, the two old files were removed, all 30 agent-rules links resolve. dist/CHANGELOG.md also refreshed, having been stale since change 80.

## Conclude

_(Approved 2026-09-11.)_

The map is now one tree in two files: `map.md` rooted at NDD Project holding the pipeline, `ndd.map.md` holding the method as a branch. Three conventions came in during the build and were not in the plan: the parent link marked `[↑ Parent]`, a Contents node per file, and the overview as a nested list of links, which is on trial. META and Rationale are gone rather than re-homed. The build detaches the branch for shipping; the installer retires the old file names. Formatting and Map Structure sit over the size bound.
