# Inline word diffs

## Intent

Show a surfaced edit's changes within the line, in a form the user's terminal renders: removed words in italics, and added words in bold, with each link shown as its bracketed text and no target, so links are not mistaken for removals yet stay visible as links. Inline code was tried for removals, as the terminal colours it, but it clashed with code already in the node; italics replaced it, though they clash in turn with italics in the node, and on a line already carrying bold the form failed outright, so the fenced diff remained the fallback. Settle how this sits beside the fenced form *Diffs* sets.

## Context

Set aside during 105 (2026-11-03). Line diffs in a `diff` fence were unhelpful for long lines; strikethrough and `[-…-]{+…+}` markers did not render usefully in the terminal, while inline code showed in colour.
