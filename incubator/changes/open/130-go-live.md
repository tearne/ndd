# Go-live reorg

**Mode:** _(to propose after Intent approval)_

## Intent

Flip the repo from incubation to the live method, so the repository itself *is* NDD rather than a framework incubated inside it. Today the live method lives in `incubator/` while the repo root still holds the superseded COD framework (`agent/`, the old root `opt-in.py`, `PRINCIPLES.md`, old root `README`/`CHANGELOG`, `CLAUDE.md.bk`, and the old root `changes/`). Go-live lifts `incubator/`'s contents to the root and retires the old framework, then renames the GitHub repo to `ndd`, makes it public, and proves the clone-and-run `opt-in.py` install end-to-end against the live repo. The blocking work has landed: distribution fixes (120), standards migration (125, now `standards/`), and the installer switch (128, which retired `install.sh` for `opt-in.py`) — so the install proof is the local-clone flow, not `curl … | bash`.

Note: repo rename, visibility change, and any branch/merge/push are user-performed — the agent never runs git-write or GitHub-admin operations on its own initiative.

<!-- ============================================================= -->
<!-- SCRATCH / WIP — parity check in progress. Not yet Approach.   -->
<!-- Resume point: disposition the true orphans (§C), then get     -->
<!-- Intent approval, propose Mode, write Approach + worklist.      -->
<!-- ============================================================= -->

## Planning notes (WIP)

**Lifecycle status:** 130 is in Plan. Intent has been **revised to current reality** (above) but is **not yet approved**. No Mode proposed. No active lock. Next: settle orphan dispositions, then Intent approval → Mode → Approach → worklist.

### User decisions taken this session

- **Keep COD changelog history.** NDD is COD's continuation, so present one lineage: NDD semver entries on top, COD's dated history preserved below (e.g. under a "Predecessor: COD" heading). **Open sub-decision:** does NDD 1.0.0 stay as-is or re-anchor onto COD's version line? Touches the VERSIONING standard — resolve in Approach.
- **Keep the old `changes/archive/`** (37 COD change records) — the method's development record. Lift into the unified `changes/archive/` (or a marked `archive/cod/`), don't drop.

### A. Cleanly replaced — safe to delete on go-live

- `agent/ADDITIONAL/{POS,RUST,VERSIONING}.md`, `agent/STYLE.md` → **identical** in `incubator/standards/`.
- `agent/ADDITIONAL/CHANGELOG.md` → `incubator/standards/CHANGELOG.md`; loading semantics (`ADDITIONAL/README.md`) → map **Standards (s9d)**.
- old root `opt-in.py` → `incubator/opt-in.py` (128).
- `agent/MAP-GUIDANCE.md` → **fully covered** by map Specification subtree (24/24 rules mapped: Node, Navigation Links, Map Structure, Node Sizing, Conceptual Writing, Formatting, Node Sections, Callouts, Sync Rule, Engagement Rule, Edit Governance, Conceptual Drift, etc.).
- `agent/KEYWORDS.md` → **fully covered** by map **Process Keyword** + **Aside Keyword**.
- `agent/PROCESS.md` → ~28/32 covered by Change-Management subtree; residual gaps in §C.
- `agent/README.md` → Startup Scan / Gates / Cadences cover it; its "version-upgrade procedure" is **covered in `BOOTSTRAP.md` → Staying up to date** (agent missed this — verified present, line 31). Not an orphan.
- `CLAUDE.md.bk` (`@README.md` + `@agent/README.md`) → obsolete; new entry is `incubator/CLAUDE.md` → `@ndd/BOOTSTRAP.md`.
- `changes/process-feedback.md` → empty (header only), nothing to preserve.
- `incubator/changes/agent/2026-06-10/` → legacy pre-128 snapshot of the `agent/` files; superseded by `ndd/` vendoring (128 log deferred its cleanup to 130).

### B. History (decided: keep — see user decisions)

- root `CHANGELOG.md` (124 lines, COD method history) — absorb into NDD changelog.
- root `changes/archive/` (37 records) — lift/keep.

### C. TRUE ORPHANS — need disposition before deleting source (RESUME HERE)

Each: decide fold-into-map vs. preserve-doc vs. accept-loss.

1. **PRINCIPLES.md rationale depth.** All *principles* are covered as concepts in the **Principles (p4c)** subtree, but the deeper *rationale/urgency* narrative is dropped: (a) the paradigm-progression analogy (type systems → FP → ownership/borrow → conceptual maintainability), (b) the unbundling diagnosis (why production stopped carrying comprehension; why specs go unread), (c) the peak-tree urgency (agents emit graph-shaped code from day one, skipping the phase that felt good), (d) the explicit "three binding constraints" framing. Map is intentionally terse (Node Sizing ~800), so *some* loss is by-design — but decide which of these to fold in (candidate home: Principles node overview or new child) vs. accept.
2. **Wander Conclusion length exception.** Old PROCESS: Conclusion soft-trigger 500, **but 1000 for Wander** (it carries Approach work retrospectively). Map **Conclude (o4j)** states ~500 universally. Decide: restore the Wander exception in the map, or accept universal 500.
3. **`**Mode:**` line convention.** Change docs use a `**Mode:** <name>` line under the title (128/129/130 all do); the map never documents this convention (not in Plan/Cadences). Decide: document it (Cadences/Plan) or leave tacit.
4. **"Read the codebase" in Approach + no-map projects.** Old PROCESS Approach said "Read the codebase; if a map exists, read it… identify coverage gaps." Map **Approach (a2r)** has no read-the-codebase instruction and assumes a map always exists. Decide: add the research instruction (and the no-map degradation) or accept.

### Also fold into 130 scope (already noted)

- `incubator/README.md` has stale lower sections ("Boundary", "Self-contained COD project") referencing the old `agent/` model — clean during go-live, not just lift.
- Git-write / GitHub-admin steps (branch, merge, repo rename, make public, install proof) are **user-performed**.
