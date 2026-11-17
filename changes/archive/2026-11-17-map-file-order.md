# Map file order

**Change Style:** Vibe \
**Version:** 3.7.5-dev

## Intent

A map file should hold its nodes in tree order, each node followed by its children depth-first as *Contents* lists them.

## Bounds

Method map only: *Map Files* should state the order and *Tidy* should restore it. Reordering changes no node's text, so Tidy should treat it as a correction.

## Context

Raised as an aside on 2026-11-17 during 120 Session conduct branch, which moved its nodes into tree order without any node asking for it. The live method map was not strictly in tree order: 130 placed *Requirement Voice* before *Intent*.

## Conclude

The rule went in *Map Structure* rather than *Map Files*, which would have reached 1,031 characters. All three maps already complied.

## Log

- 2026-11-17: Build Lock taken; version 3.7.5-dev claimed, a patch bump. Planned edits: 1 *Map Files*, 2 *Tidy*.
- 2026-11-17: deviation agreed with the user: the rule goes in *Map Structure*, not *Map Files*, which would have reached 1,031 characters. Edit 1 approved: "Each file holds its nodes in the overview's order." 765 characters, stamped 4e08bb9f.
- 2026-11-17: edit 2 approved, *Tidy* fixes a file's nodes out of the overview's order. 794 characters, stamped 19fe3790.
