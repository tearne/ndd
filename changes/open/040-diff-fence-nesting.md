# Diff fence nesting

## Intent

When a surfaced diff contains a fenced block of its own, such as a node's yaml scaffolding, the inner fence closes a three-backtick outer fence early and the diff loses its colouring. Make Show Edits as Diffs, and rule 8, say to fence the diff with more backticks than any fence inside it.

Raised as an aside (2026-10-16).

## Context

Rule 8's "```diff-fenced block" has no source in the map: the Engagement Rule says only "plus a diff for an edit". Noticed during change 091 (2026-10-17); the user expects it to fit in the Engagement Rule's *Detail*.
