# Agent rules

The short form of Non-Dead Design, rendered from the method map. It carries only the rules that apply in almost every session, whose observance can be checked, and whose breach is costly; everything else stays in the map. The map is the source: `ndd/ndd.md` explains each rule, and where the two disagree the map wins. Each rule below ends with a link to its home node in the map.

## Orientation

- Two maps are in play. `ndd/ndd.md` is the **method map**: how NDD works, read-only. Each rule links to its source node in the NDD method map; follow it when you need the reasoning behind a rule, not before. `map.md` in the project root is the **project map**: the project itself, built with the user. It is a tree of nodes; start at the root — the one with no parent link — and follow child links.
- Everything under `ndd/` is a vendored snapshot that `install.py` regenerates. Change the method at its source and re-run the installer; hand edits here vanish on the next install. The version you are running is the semver at the top of `ndd/CHANGELOG.md`.
- Re-read this file whenever your instructions are re-injected after a compaction, and at the start of every Build.

## Rules

### 1. Startup Scan

Start every session with the Startup Scan. Read everything in `changes/open/`, place each change in its lifecycle, announce whether you are planning or building, and propose the next step. If there is no `map.md` and no `changes/` tree the project has not started: offer to bootstrap instead. Nothing else happens first, because the open changes are where the state lives. [Startup Scan](ndd.md#startup-scan), [Bootstrapping](ndd.md#bootstrapping).

### 2. Build Lock

Take the lock only when an approved plan enters Build. Build begins on the user's approval of the plan and not before. On that approval, write the change file name into `changes/open/active.md` and report it. If the file already exists, stop and say so: another change is mid-build. [Build Lock](ndd.md#build-lock).

### 3. Active Change

Write project files only under an active change. With no `active.md`, write inside `changes/` and nowhere else. The one exception is a map edit that describes what already exists. If a needed write fits neither case, stop and ask rather than making it. [Gates and Permissions](ndd.md#gates-and-permissions), [Edit Governance](ndd.md#edit-governance).

### 4. Git Writes

Leave git writes to the user. Commit, push, branch and reset happen only on an explicit instruction in this session. When a step seems to need one, name the command and wait. [Gates and Permissions](ndd.md#gates-and-permissions).

### 5. Approval

Treat only a clear yes as approval, and only for what was shown. Approval is an affirmative given in reply to your asking. Silence, a tangent, or a reply that raises new questions is not approval. It covers what was surfaced and no more: agreeing to draft prose is not approval of the prose, and delivering a draft — in chat or written in place — is never approval of it. [Approval](ndd.md#approval).

### 6. Map Edit Order

Make every map edit in one order: draft, surface with its count, write on approval. Surface the drafted node text and its character count, then write only when the reply is approval. No map edit is silent and none is made in bulk, because the user's comprehension is built in the negotiation of each one. If the edit is urgent and the user is absent, wait; do not write it. [Engagement Rule](ndd.md#engagement-rule).

### 7. Corrections

Apply corrections without surfacing only when every item in hand is one. A typo, spacing, or a stale link that changes no meaning is applied and reported. If any item in the batch changes meaning, the whole batch goes through rule 6, because a batch inherits its fastest path. [Engagement Rule](ndd.md#engagement-rule).

### 8. Node Count

Count and report characters on every node you edit. Count the body plus *Detail*, inline links as their visible text, excluding navigation links, *See also*, tables and diagrams. Report the number in your message. Over about 800, flag it and leave the split to the user. The reported number is how the user sees the rule was followed. [Node Sizing](ndd.md#node-sizing).

### 9. Map Describes Reality

Write the map as what exists, never what is planned. An edit describing unbuilt work waits until the work is built. If the user asks for a forward-looking map edit, say why it waits and offer to hold the text in the change instead. [Sync Rule](ndd.md#sync-rule).

### 10. Plan Parts

Surface plan parts one at a time. Draft the Intent, get approval, then the Approach, then the Worklist. Each part waits for the previous one's approval, because a plan approved whole is a plan not read. [Plan](ndd.md#plan).

### 11. Caps

Count against the caps each time you surface a part. Intent about 500 characters, Approach about 2000 excluding Unresolved, Conclude about 500 excluding a changelog entry. Report the number. Past the cap, ask the user to adjudicate rather than trimming silently or presenting it as final. [Intent](ndd.md#intent), [Approach](ndd.md#approach), [Conclude](ndd.md#conclude).

### 12. Follow the Plan

In Build, follow the plan and log the unexpected. Execute the approved plan rather than revising it mid-flight. Append to the change's Log any surprise, deviation, blocker or partial progress, so a resuming session can pick up; routine progress needs no entry. If the plan proves wrong, stop and offer to return the change to planning. [Build](ndd.md#build).

### 13. Held

Empty Held before Conclude. Fold each held item into the change, park it as its own change, or have the user discard it. Nothing is concluded with material outstanding, because Held is where things are lost. [Held](ndd.md#held).

### 14. Archiving

On an approved Conclude, archive, release the lock, then offer what follows. Move the file to `changes/archive/` renamed with the ISO date in place of its number and delete `active.md`. Then offer the Consistency Upkeep and Judgement Scan, and if the project map defines release steps, ask whether it is time to run them. [Archiving](ndd.md#archiving), [Map Maintenance](ndd.md#map-maintenance).

### 15. Keywords

Honour the two keywords in a line and carry on. A message starting `process:` is appended to `changes/process-feedback.md`, dated, without acting on it. One starting `aside:` becomes a new parked change in `changes/open/` holding an Intent only. Confirm each in one line and return to the work. [Process Keyword](ndd.md#process-keyword), [Aside Keyword](ndd.md#aside-keyword).

### 16. Orient Then Focus

Orient, then focus. With any set to present — unresolved items, a worklist, the open changes, several nodes to edit — show the whole set in summary first, then work through it one item at a time while holding the rest. Introduce each item by name and its place in the set, such as *3 of 7*. A message asks at most one question and ends where it asks it. Attention dies under overwhelm, and item-by-item alone loses the user's place. [Orient Then Focus](ndd.md#orient-then-focus).

### 17. Typography

Typeset map prose by the conventions. One continuous line per paragraph with no hard wraps. A blank line between bullets that wrap. Two blank lines before a node title. *Italics* for a named section or element, **bold** only to introduce a term of art on first use. An inline link when a sentence names another node in passing, a *See also* entry with its own reason otherwise. [Formatting](ndd.md#formatting).

### 18. User Map Edits

When the user has edited the map, re-read the node before doing anything else with it. Report its new count and any knock-on you can see — a link that no longer resolves, a sibling that now overlaps — and log it only if it changes what the build must do. The user edits freely and unannounced; the rule binds you, not them, so never treat their edit as something to approve. [Engagement Rule](ndd.md#engagement-rule).
