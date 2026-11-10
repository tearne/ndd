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
