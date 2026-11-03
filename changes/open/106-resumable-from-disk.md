# Resumable from disk

## Intent

A change holds on disk everything a fresh session needs to carry on with it, never relying on what the session that worked it remembers. In particular, any list of items a change works through, such as review findings, is written into the change before work on it starts. A pause leaves the work resumable from disk alone: before it stops, the agent checks that the change and the pause entry together hold everything still to do, and writes down whatever is missing.

## Context

Change 105 paused at "F 11 of 19". The findings lived only in chat, because *Map Review* stores none, 105's Log recorded only settled items, and the pause entry was a pointer. A new session had to recompute group F and found 12 items, not 9.
