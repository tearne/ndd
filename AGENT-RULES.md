# Agent rules

The short form of Non-Dead Design, rendered from the method map. It carries only the rules that apply in almost every session, whose observance can be checked, and whose breach is costly; everything else stays in the map. The map is the source: `ndd.map.md`, beside this file, explains each rule, and where the two disagree the map wins. Each rule below ends with a link to its home node in the map.

## Orientation

- In a client project two maps are in play: the project's own, entered at `map.md` in the project root and built with the user; and NDD's, vendored under `ndd/`, whose method branch `ndd.map.md` sits beside this file and is what every rule below links to, read-only. Follow a link when you need the reasoning behind a rule, not before. A map is a tree of nodes; start at the root, the one with no `↑` link, and follow child links, into other `*.map.md` files where a branch continues. [Distribution](map.md#distribution).
- `ndd/` is a vendored snapshot that `install.py` regenerates: change the method at its source and re-run the installer, since hand edits there vanish. In the NDD repository itself the two maps are one, and this file and the maps beside it are the sources. The version you are running is the semver at the top of `CHANGELOG.md` beside this file.
- Re-read this file whenever your instructions are re-injected after a compaction, and at the start of every Build.
- A draft goes to chat unless the user says *write*, which means put it in place and stop until they hand back, then run Tidy over what changed before asking anything. *Write* is never approval and never a cue to move on, even when it arrives in reply to an "Approve?" ask — the stamp follows a separate yes. A bare *write* covers one draft; only an instruction that says so, such as "write everything from here", covers the session. [Approval](ndd.map.md#approval).

## Rules

### 1. Startup Scan

Start every session with the Startup Scan. Read every change and discussion in `changes/open/`, place each in its lifecycle, announce whether you are planning, building or discussing (in any combination), offer a [Backlog Review](ndd.map.md#backlog-review), and propose the next step. If there is no `map.md` and no `changes/` tree the project has not started: offer to bootstrap instead. Nothing else happens first, because the open items are where the state lives. [Startup Scan](ndd.map.md#startup-scan), [Discussion](ndd.map.md#discussion), [Bootstrapping](ndd.map.md#bootstrapping).

### 2. Build Lock

Take the lock only when an approved plan enters Build. Build begins on the user's approval of the plan and not before. On that approval, write the change file name into `changes/open/active.md` and report it. If the file already exists, stop and say so: another change is mid-build. [Build Lock](ndd.map.md#build-lock).

### 3. Active Change

Write project files only under an active change. With no `active.md`, write inside `changes/` and nowhere else. The one exception is a map edit that describes what already exists. If a needed write fits neither case, stop and ask rather than making it. [Gates and Permissions](ndd.map.md#gates-and-permissions), [Edit Governance](ndd.map.md#edit-governance).

### 4. Git Writes

Leave git writes to the user. Commit, push, branch and reset happen only on an explicit instruction in this session. When a step seems to need one, name the command and wait. [Gates and Permissions](ndd.map.md#gates-and-permissions).

### 5. Approval

Treat only a clear yes as approval, and only for what was shown. Approval is an affirmative given in reply to your asking. Silence, a tangent, or a reply that raises new questions is not approval. It covers what was surfaced and no more: agreeing to draft prose is not approval of the prose, and delivering a draft — in chat or written in place — is never approval of it. [Approval](ndd.map.md#approval).

### 6. Map Edit Order

Make every map edit in one order: draft, surface with its count, settle on approval. Surface the drafted node text and its character count, then treat it as settled only when the reply is approval. On a map that carries stamps, settling also writes the approver's stamp, computed with the shipped fingerprint script, and reports its hash beside the count. Say which handle you are using the first time you stamp; take it from git's `user.name` unless the map's stamps exist and none match that name, and ask when it is missing or unmatched. No map edit is silent and none is made in bulk, because the user's comprehension is built in the negotiation of each one. With nobody to approve, wait. [Engagement Rule](ndd.map.md#engagement-rule), [Approver](ndd.map.md#approver).

### 7. Diff-Shaped Surfaces

Surface a map-node edit as a diff in chat, showing what changed alongside the new state — use a ```diff-fenced block. A wholly new node is surfaced whole; a whole-node rewrite may be too. [Engagement Rule](ndd.map.md#engagement-rule).

### 8. Corrections

Apply corrections without surfacing only when every item in hand is one. A typo, spacing, or a stale link that changes no meaning is applied and reported. If any item in the batch changes meaning, the whole batch goes through rule 6, because a batch inherits its fastest path. [Engagement Rule](ndd.map.md#engagement-rule).

### 9. Node Count

Count and report characters on every node you edit. Count the body plus *Detail*, inline links as their visible text, excluding navigation links, *See also*, tables and diagrams. Report the number in your message. Over about 800, flag it and leave the split to the user. The reported number is how the user sees the rule was followed. [Node Sizing](ndd.map.md#node-sizing).

### 10. Map Describes Reality

Write the map as what exists, never what is planned. An edit describing unbuilt work waits until the work is built. If the user asks for a forward-looking map edit, say why it waits and offer to hold the text in the change instead. [Sync Rule](ndd.map.md#sync-rule).

### 11. Plan Parts

Surface plan parts one at a time, each drafted, surfaced with its count, and settled by approval before the next begins. A plan approved whole is a plan not read. In order:

1. Intent — draft, surface, get approval.
2. Change Style — propose one after the Intent is approved; the user confirms.
3. Preparation section — determined by the Change Style:
   - Trivial: none.
   - Vibe: Bounds.
   - Exploratory: Focus.
   - Formal: Change Specification, and optionally Implementation Plan.
4. Intent trim — once the preparation section is approved, re-read the Intent, cut what the preparation now carries, and surface the trimmed Intent with its count. Trivial has no preparation and no trim step.

[Plan](ndd.map.md#plan), [Change Style](ndd.map.md#change-style), [Intent](ndd.map.md#intent).

### 12. Caps

Count each part against its cap when you surface it, report the number, and past a cap ask the user to adjudicate rather than trimming silently or presenting it as final.

- Intent: ~500 characters.
- Bounds: ~200 characters (soft — overrun signals the wrong style).
- Focus: ~300 characters (soft — overrun signals Formal is the fit).
- Change Specification: map-shape — each node follows the [Node Sizing](ndd.map.md#node-sizing) conventions.
- Implementation Plan: format-dependent — a map-shape part follows the [Node Sizing](ndd.map.md#node-sizing) conventions per node; a prose or table part carries its own convention where a cap is meaningful.
- Conclude: ~500 characters, excluding a changelog entry.

Unresolved sits beside a part and is excluded from that part's count.

[Intent](ndd.map.md#intent), [Bounds](ndd.map.md#bounds), [Focus](ndd.map.md#focus), [Change Specification](ndd.map.md#change-specification), [Conclude](ndd.map.md#conclude).

### 13. Follow the Plan

In Build, follow the plan and log the unexpected. Execute the approved plan rather than revising it mid-flight. Append to the change's Log any surprise, deviation, blocker or partial progress, so a resuming session can pick up; routine progress needs no entry. If the plan proves wrong, stop and offer to return the change to planning — or, for a Formal change, re-agree just the Change Specification while keeping the Build Lock. [Build](ndd.map.md#build), [Formal Build](ndd.map.md#formal-build).

### 14. Held

Empty Held before Conclude. Fold each held item into the change, park it as its own change, or have the user discard it. Nothing is concluded with material outstanding, because Held is where things are lost. [Held](ndd.map.md#held).

### 15. Conclude Content

Conclude records the delta from the plan — deviations, surprises, documents touched — not a summary of what the plan already said. When there's nothing to add, "Completed." is enough. [Conclude](ndd.map.md#conclude).

### 16. Archiving

On an approved Conclude: if the project map defines a CHANGELOG, add an entry and get it approved; then run Tidy, archive, release the lock, and offer one review. Run [Tidy](ndd.map.md#tidy) across the map and report it, move the file to `changes/archive/` renamed with the ISO date in place of its number, delete `active.md`, then offer a [Map Review](ndd.map.md#map-review) as one yes-or-no. If the project map defines release steps, ask whether it is time to run them, and if so offer a full Map Review first. [Archiving](ndd.map.md#archiving), [Maintenance](ndd.map.md#maintenance).

### 17. Keywords

Honour the two keywords in a line and carry on. A message starting `process:` is appended to `changes/process-feedback.md`, dated, without acting on it. One starting `aside:` is routed by content: appended to an existing discussion if it continues that thread, opened as a new parked change with an Intent only if it is Intent-shaped, or opened as a new discussion otherwise; an overlap with an existing change is named in the confirmation without attaching. Confirm each in one line and return to the work. [Process Keyword](ndd.map.md#process-keyword), [Aside Keyword](ndd.map.md#aside-keyword).

### 18. One Item at a Time

Orient, then focus. With any set to present — unresolved items, a worklist, the open changes, several nodes to edit — show the whole set in summary first, then work through it one item at a time while holding the rest. Introduce each item by name and its place in the set, such as *3 of 7*. A message asks at most one question and ends where it asks it. Attention dies under overwhelm, and item-by-item alone loses the user's place. While a set is in progress, end every message with a status line showing the stack, such as *map edits 3 of 7 > aside*, with *· held 2* when Held is not empty. [Orient Then Focus](ndd.map.md#orient-then-focus), [Thought Management](ndd.map.md#thought-management).

### 19. Typography

Typeset map prose by the conventions. One continuous line per paragraph with no hard wraps. A blank line between bullets that wrap. Two blank lines before a node title. *Italics* for a named section or element, **bold** only to introduce a term of art on first use. An inline link when a sentence names another node in passing, a *See also* entry with its own reason otherwise. [Formatting](ndd.map.md#formatting).

### 20. User Map Edits

When the user has edited or reviewed the map, re-read the current node from disk before continuing work on it. Report its new count and any knock-on you can see — a link that no longer resolves, a sibling that now overlaps — and log it only if it changes what the build must do. The user edits freely and unannounced; the rule binds you, not them, so never treat their edit as something to approve. [Engagement Rule](ndd.map.md#engagement-rule).
