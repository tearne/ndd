# Building when the map is the product

## Intent

*Build (u6k)* tells the agent to work through an approved plan without pausing step by step; the *Engagement Rule (n3g)* forbids map edits made in bulk and demands per-node negotiation. In a project whose product is the map itself, every worklist task is a map edit and the two rules contradict each other outright. The method should say which governs, and when.

### Context

Surfaced during change 180's build: six nodes were edited in one pass on the strength of an approved worklist naming each. The user noticed the missing per-node negotiation and declined a replay, but the rule conflict stands.

An ordinary project doesn't hit this — code is built, and map catch-up follows at Conclude under per-node negotiation, as the *Sync Rule (s5y)* has it. NDD's own repo hits it on every change, so the method is least governed exactly where it is most used.
