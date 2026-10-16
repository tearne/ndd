# Diff fence nesting

## Intent

When a surfaced diff contains a fenced block of its own, such as a node's yaml scaffolding, the inner fence closes a three-backtick outer fence early and the diff loses its colouring. Make Diff-Shaped Surfaces, and rule 8, say to fence the diff with more backticks than any fence inside it.

Raised as an aside (2026-10-16).
