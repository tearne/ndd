# Target nodes file

## Intent

*Change Specification* should say when to write the planned nodes whole and stamped into a companion `targets.md`, rather than a whole-map copy: when a change touches a few nodes spread across maps, where a copy is heavy and diffs against it add little.

## Context

Raised 2026-11-20 during 330, which trials it: its targets were first written as body text without stamps, then as full nodes inside the change, which interrupted the change's flow, then moved to `archive/2026-11-20-stamp-key-rename/targets.md`, where `fingerprint.py` checks their stamps. Parked until 330 concludes, so the trial's experience of review and promotion can inform it. Likely touches *Change Specification* and perhaps *Companion Folder*.
