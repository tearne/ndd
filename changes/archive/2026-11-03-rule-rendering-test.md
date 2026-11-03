# Rule rendering test

**Change Style:** Formal

## Intent

When the agent rules are re-rendered, test each new or reworded rule against the wording it replaces, or none, so a rule that backfires is caught before it ships.

## Context

Raised during 085's planning (2026-11-03). Paired subagent runs on a node draft and a small edit to a flawed node showed the draft *Node Standard* rule bundling an unasked rewrite and dropping a design reason; neither showed on reading the rule. The check would likely sit under *Agent Rules* in `map.md`.

## Change Specification

- Map target: `090-rule-rendering-test/map.md`, adding *Rule Testing* under *Agent Rules*, with the navigation link and *Contents* entry to match. *Agent Rules* gains no clause, since *Rule Testing* owns when the test runs.

## Log

- 2026-11-03: Build Lock taken; patch bump agreed, claiming 2.10.1-dev.
- 2026-11-03: *Rule Testing*, the *Agent Rules* navigation link and the *Contents* entry promoted into `map.md`; no drift from baseline, stamps verified.

## Conclude

Verified: the live map matches the Change Specification, and every stamp holds. Built as specified, touching `map.md`. The planned clause in *Agent Rules* was dropped while drafting, since *Rule Testing* owns when the test runs.
