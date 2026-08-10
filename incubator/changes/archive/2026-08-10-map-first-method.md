# Map-first method

**Mode:** Explore

## Intent

The method should live in the map, not in prose beside it. Today `AGENT`, `PROCESS`, `KEYWORDS`, and `MAP-GUIDANCE` carry the process as markdown, and `map.md` describes the same concepts as nodes — the two have already drifted, with `map.md` badly stale. This change explores collapsing that duplication: express as much of the method as possible *as the map*, so the map is the primary artefact the agent reads to understand how to work, leaving only a minimal markdown shell that points the agent at the map and tells it to read and follow it. That is the true dogfooding test — the method describing itself in its own form.

## Approach

### The shell holds only what the agent needs before it trusts the map

`BOOTSTRAP.md` carries the bare minimum: what an agent must know before reading the map. The test is timing — needed before reading goes in the shell, everything else goes in the map. Two things qualify: the safety rules (no git writes, no project edits without an active change) and one directive — the map is authoritative, read it and follow it. Everything the agent does after reading is a map candidate.

### Write the shell fresh, don't trim AGENT.md

Drafting a new file forces us to reason the minimum from scratch instead of inheriting it. `AGENT.md` and the process docs stay as the working method for now; retiring them into the map is the follow-up's job.

### This change stops at the handoff

Scope ends at a working shell→map handoff. Moving the lifecycle, gates, and seeds into map nodes — and finding out whether one map can hold both a system and its own method — is a separate change.



## Plan

**Topics**

- Draft `BOOTSTRAP.md`: the safety rules, and the directive to read and follow the map as authoritative — nothing an agent only needs after reading the map.

- Sort every fact currently in `AGENT.md` into shell-or-map, confirming the shell keeps only the before-reading minimum and recording where the rest lands in the follow-up.

- Confirm the handoff reads coherently on paper — an agent landing on `BOOTSTRAP.md` is sent to the map with enough to proceed safely. `CLAUDE.md` stays on `AGENT.md`; going live waits for the follow-up that builds the map out.

**Done when** `BOOTSTRAP.md` carries only the safety rules and the read-the-map directive, every other `AGENT.md` fact is accounted for as either kept (justified) or logged for the follow-up migration, and the shell→map handoff is coherent — with `CLAUDE.md` and the live docs untouched.

## Log

- Sorted every `AGENT.md` fact. **Kept in shell** (needed before reading the map): the two safety rules — no git writes without instruction, no project edits without an active change (with the reading / `changes/` exemptions). **To the map (follow-up migration):** the startup scan (seeds vs. changes, lifecycle, `active.md`), the version-update procedure, the "map is primary frame" conventions pointer, the `changes/open` + `changes/archive` folder layout, and the `@`-imports of `PROCESS`/`MAP-GUIDANCE`/`KEYWORDS` — the shell replaces those imports with a single "read the map" directive.
- Dropped from the shell the change-management-decision rule and the detailed exemption list: both are process the agent only needs after reading the map. Shell keeps only the git-write and active-change gates in terse form.
- Handoff coherence: an agent landing on `BOOTSTRAP.md` learns the two hard safety limits, then is sent to `map.md` as authoritative. This is correct on paper but not yet live — `map.md` does not yet carry the process, so `CLAUDE.md` stays on `AGENT.md` until the follow-up builds the map out.
- Review: BOOTSTRAP's "map is authoritative" reworded twice. Dropped the "defines this project — what the system is and how work is done" framing (grating, and inaccurate once a client project has its own domain map). Final wording points at "the `map.md` alongside this file" so file-tree position, not prose, says which map.
- Captured seed `separate-method-map-by-placement.md` (kind: idea, anchor a3k): ship the process map + BOOTSTRAP under `changes/agent/` so placement distinguishes the method map from a client's domain map — for the map build-out follow-up to settle.
- Added a minimal map-reading primer to BOOTSTRAP (tree of nodes, start at the root, follow child links) — the irreducible before-reading navigation facts. Full conventions stay in the map for the follow-up.
- Noted: the primer assumes the map's node format (parent/child links, root has no parent), a dependency the follow-up must honour when it migrates conventions into the map.
- Captured seed `map-file-organisation-vs-traversal.md` (kind: idea, anchor a3k — Tooling has no ID yet): weigh single-file vs node-per-file against agent traversal/context cost during the map build-out.

## Conclusion

Delivered `BOOTSTRAP.md`: the irreducible shell — two safety gates (git writes, active-change) plus a pointer to the co-located `map.md` and a minimal primer for reading it (tree of nodes, start at root, follow child links). Every other `AGENT.md` fact was sorted and logged as method content for the map build-out follow-up; nothing went live — `CLAUDE.md` and the existing docs are untouched.

Two design questions surfaced and were captured as seeds rather than resolved here: separating the method map from a client's domain map by file placement (`separate-method-map-by-placement.md`), and weighing map file organisation against agent traversal cost (`map-file-organisation-vs-traversal.md`) — both for the follow-up.

The bootstrap primer assumes the map's node format (parent/child links, root has no parent); the follow-up must honour that when it moves conventions into the map.
