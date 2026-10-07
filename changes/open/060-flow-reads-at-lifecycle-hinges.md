# Flow reads at lifecycle hinges

## Intent

AGENT-RULES.md's orientation preamble currently discourages map reads except for rule reasoning (*"Follow a link when you need the reasoning behind a rule, not before"*). It should distinguish two kinds of read: *reasoning* reads happen only when needed, but *flow* reads happen whenever a lifecycle hinge is about to be crossed (Discussion → change, between plan parts, Build → Conclude, Conclude → archive). Noticed 2026-10-06 when the agent skipped *Discussion Conclude* while closing `formal-specification-pacing-discussion.md`.
