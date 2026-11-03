# Rule rendering test

## Intent

When the agent rules are re-rendered, test each new or reworded rule by giving subagents the same task with the old rule and with the new one, and comparing what they produce, so a rule that backfires is caught before it ships.

## Context

Raised during 085's planning (2026-11-03). Paired subagent runs on a node draft and a small edit to a flawed node showed the draft *Node Standard* rule bundling an unasked rewrite and dropping a design reason; neither showed on reading the rule. The check would likely sit under *Agent Rules* in `map.md`.
