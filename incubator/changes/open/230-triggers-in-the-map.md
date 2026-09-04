# Triggers in the map

## Intent

The map is organised by concept, which is right for comprehension but leaves the moments a rule fires scattered and implicit. Rendering the rules for agent compliance (change 220) surfaced this: several rules had to be attached to whichever neighbouring rule already fired, because the triggering moment was not a first-class thing anywhere. Consider a structure that represents triggers directly.

## Context

Raised during change 220 while selecting rules to render. Three cases forced the workaround: the map-maintenance checks fire only once a change is archived, so they were folded into the archiving rule; bootstrapping fires only when `map.md` is absent, so it was folded into the startup rule; and the writing-style check had no honest trigger at all and was removed from the per-edit order. In each case the rule was fine and the trigger was homeless.
