# Triggers in the map

## Intent

The map is organised by concept, which is right for comprehension but leaves the moments a rule fires scattered and implicit. Rendering the rules for agent compliance (change 220) surfaced this: several rules had to be attached to whichever neighbouring rule already fired, because the triggering moment was not a first-class thing anywhere. Consider a structure that represents triggers directly.

## Context

Raised during change 220 while selecting rules to render. Three cases forced the workaround: the map-maintenance checks fire only once a change is archived, so they were folded into the archiving rule; bootstrapping fires only when `map.md` is absent, so it was folded into the startup rule; and the writing-style check had no honest trigger at all and was removed from the per-edit order. In each case the rule was fine and the trigger was homeless.

### Paper exercise (2026-09-09)

Placing the 17 rendered rules under the moments an agent can recognise, to test whether a Moments index (a META sibling of Contents: one line per moment, links to the rules that fire) would carry the trigger structure without re-rooting the map.

| Moment | Rules that fire |
|---|---|
| Session starts | 1 Startup Scan (bootstrap folded in) |
| Instructions re-injected after compaction | re-read the rules (orientation, unnumbered) |
| Plan approved, entering Build | 2 Build Lock |
| About to write a project file | 3 Active Change |
| A step seems to need git | 4 Git Writes |
| Reading the reply to anything surfaced | 5 Approval |
| About to edit a map node | 6 Edit Order, 7 Corrections, 8 Node Count, 9 Map Describes Reality, 17 Typography |
| About to surface a plan part | 10 Plan Parts, 11 Caps |
| Executing a Build task | 12 Follow the Plan |
| Conclude about to be drafted | 13 Held |
| Conclude approved | 14 Archiving (maintenance checks and release steps folded in) |
| Message starts with a keyword | 15 Keywords |
| About to present a set | 16 Orient Then Focus |
| Composing any message | 16's one-question clause; 17's conventions if map prose |

Findings:

- Every rule finds exactly one moment, except 16 and 17, which split between a moment and a standing constraint on all output. **Not every rule is trigger-shaped**: some are invariants (message shape, typography). A Moments index needs a place for invariants or they go homeless again.
- One moment is overloaded: *about to edit a map node* carries five rules. It is the core act, so the load may be honest, but it is the case for the cluster having one home — which is roughly what the Engagement Rule already is.
- Moments the map knows but the rendering does not: *the user has edited the map* (Engagement Rule, second paragraph — re-read, recount, report knock-ons; unrendered and arguably should be, given this session's experience); *the user asks for a forward-looking map edit* (rule 9's escape clause); *a maintenance check is requested*. The first is a candidate for the rendering.
- The folded-in cases from 220 (bootstrap into startup, maintenance checks into archiving) become explicit rows, which is the original complaint answered without changing any concept node.
- Falsifiability test to apply if built: regenerate the rendering from the Moments index plus linked nodes; a rule with no moment, or a moment with no rule, is a defect in one or the other.

## Log

- 2026-09-09: Plan approved as a Wander; the paper exercise answered the Intent — no Moments index. Build: (1) one sentence in [Rule Form](#rule-form) distinguishing trigger rules from standing ones; (2) rule 18 in the rendering for the moment *the user has edited the map*, sourced from the [Engagement Rule](#engagement-rule)'s second paragraph. Then Conclude.

## Conclude

Investigated and answered: no trigger structure is added to the map. Placing the rendered rules under recognisable moments showed the rendering already carries the trigger view — each rule's first sentence names its moment — so a Moments index would be that skeleton copied into the map, a third artefact to keep in sync. Two findings landed instead: Rule Form distinguishes rules that fire at a moment from standing ones, and rule 18, User Map Edits, renders the one moment the file lacked. The placement table stays in Context.
