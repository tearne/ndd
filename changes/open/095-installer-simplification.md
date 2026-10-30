# Installer simplification

## Intent

Make the installer ship only what a client needs at run time and write it fresh each run. An explicit list replaces "every tracked file" and is copied from the checkout's disk into a cleared `ndd/`, keeping the old map as `ndd.prev.map.md` if it changed. `.gitignore` gains `ndd/`, the entry files only when the installer creates them, and `.claude/` unless already checked in. `RETIRED_FILES` and 080 go.

## Context

Agreed in discussion [090 Installer review](../archive/2026-10-30-installer-review-discussion.md) (2026-10-30), which holds the reasoning and the shipped set.
