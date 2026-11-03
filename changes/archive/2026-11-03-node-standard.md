# Node standard at draft and review

**Change Style:** Formal

## Intent

Check every node against the whole standard for a node at both moments it can slip: when the agent drafts it, before surfacing, and in Map Review, which adds only the map-wide checks a single draft cannot show. The standard includes keeping the mental picture in the body and the precision in *Detail*, so the body alone gives the reader the node and the precision stays findable.

## Context

Merges two parked changes. 085 Picture and Detail check was parked from 070's *Unresolved* (2026-10-26): nothing checks the split *Node Sections* sets. 100 Writing style at draft was set aside during 095's planning (2026-11-03), after the user had to ask for a *Writing Style* review on successive drafts; it had absorbed 075 Duplication drift. During planning, the two turned out to be one gap: drafts are checked against *Formatting* and *Node Sizing* only, the light Map Review against *Writing Style*, and nothing against *Node Sections*.

## Change Specification

- Map target: `085-node-standard/ndd.map.md`, editing *Node* (names the standard and both checks), *Map Review* (light scope checks each node against the standards *Node* names) and *Economy* (how a choice was reached is provenance; the reason a choice holds stays).

- Agent rules target: `085-node-standard/AGENT-RULES.md`, where *Node Standard* replaces *Formatting*. Tested with subagents on a fresh draft and on a small edit to a flawed node; the scope clause was added after an unscoped version rewrote the whole node.

## Log

- 2026-11-03: Build Lock taken; minor bump agreed, claiming 2.10.0-dev.
- 2026-11-03: *Node Standard* landed in `AGENT-RULES.md`, replacing *Formatting*.
- 2026-11-03: *Node*, *Map Review* and *Economy* promoted into `ndd.map.md`; no drift from baseline, stamps verified.

## Conclude

Verified: the live map and agent rules match the Change Specification, and every stamp holds. Built as specified, touching `ndd.map.md` and `AGENT-RULES.md`. During planning, 100 Writing style at draft was merged in and 090 Rule rendering test was parked.
