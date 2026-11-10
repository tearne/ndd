# Resumable from disk

**Change Style:** Formal

## Intent

A change should hold on disk everything a fresh session needs to carry on with it, including any list it works through and, at a pause, whatever is still to do.

## Change Specification

Target map: [106-resumable-from-disk/ndd.map.md](106-resumable-from-disk/ndd.map.md).

`method/AGENT-RULES.md` target: a new rule after *Build*:

> ### Change Lifecycle: State on Disk
>
> Keep everything needed to resume a change on disk, in the change or its companion folder, never only in chat or context. Write a list the change works through, such as review findings, into the change before working through it, and before stopping on a `pause`, write down whatever still to do is missing. A fresh session sees only what is on disk. [Change Lifecycle](ndd.map.md#change-lifecycle), [Pause Keyword](ndd.map.md#pause-keyword).

## Context

Change 105 paused at "F 11 of 19". The findings lived only in chat, because *Map Review* stores none, 105's Log recorded only settled items, and the pause entry was a pointer. A new session had to recompute group F and found 12 items, not 9.

## Log

- 2026-11-10: Plan approved, no Implementation Plan; Build Lock taken. Reconciled: live map matches the baseline copy, no drift.
- 2026-11-10: Minor bump agreed, claiming 3.1.0-dev.
- 2026-11-10: Rule A/B test, 3 tasks × with/without, scratch project. Start of a 7-finding list: without the rule the findings stayed in chat (the Log held only counts, renumbered by node); with it, written into the change before item 1. Pause at 4 of 7: without, open items squeezed into one Log line by title; with, a full *Findings* section with statuses. Pause with nothing open: both wrote one Log line; no overreach, no unasked rewrite. Rule kept as approved.
- 2026-11-10: *Change Lifecycle: State on Disk* landed in `method/AGENT-RULES.md` after *Build*.
- 2026-11-10: *Change Lifecycle*, *Plan*, *Pause Keyword* and *Map Review* promoted into `method/ndd.map.md`; no drift, all four stamps hold.
- 2026-11-10: Archiving Tidy: *Plan* trimmed from 831 to about 780 and re-stamped (80a9c861).

## Conclude

Verified: the live map matches the Change Specification and all four stamps hold; the rule landed as approved after its A/B test. Built as specified, touching `method/ndd.map.md` and `method/AGENT-RULES.md`.
