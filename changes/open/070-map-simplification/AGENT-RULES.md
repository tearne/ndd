# Agent rules

The short form of Non-Dead Design, rendered from the method map. It carries only the rules that apply in almost every session, whose observance can be checked, and whose breach is costly; everything else stays in the map. The map is the source — this file is a route into it, not a destination. Where the two disagree the map wins; `ndd.map.md` beside this file explains each rule, and each rule's heading names its source node, which is how output should refer to it. Each rule below ends with a link to its home node in the map.

## Orientation

- In a client project two maps are in play: the project's own, entered at `map.md` in the project root and built with the user; and NDD's, vendored under `ndd/`, whose method branch `ndd.map.md` sits beside this file and is what every rule below links to, read-only. Follow a link when you need the reasoning behind a rule, not before. A map is a tree of nodes; start at the root, the one with no `↑` link, and follow child links, into other `*.map.md` files where a branch continues. [Distribution](map.md#distribution).
- `ndd/` is a vendored snapshot that `install.py` regenerates: change the method at its source and re-run the installer, since hand edits there vanish. In the NDD repository itself the two maps are one, and this file and the maps beside it are the sources. The version you are running is the semver at the top of `CHANGELOG.md` beside this file.
- Re-read this file whenever your instructions are re-injected after a compaction, and at the start of every Build.
- A draft is only the text you surfaced; an action named alongside it, such as writing a log entry or a new file, needs its own draft. A draft goes to chat unless the user says *write*, which means put it in place and stop until they hand back, then run Tidy over what changed before asking anything. *Write* is never approval and never a cue to move on, even when it arrives in reply to an "Approve?" ask — the stamp follows a separate yes. A bare *write* covers one draft; only an instruction that says so, such as "write everything from here", covers the session. A draft written in place sits between `<!-- draft -->` and `<!-- /draft -->` until approved: approval deletes the markers, declining deletes the region. [Drafts](ndd.map.md#drafts).

## Rules

### Startup Scan

Start every session with the Startup Scan: before anything else, read [Startup Scan](ndd.map.md#startup-scan), give the report it lists, and propose the next step. Nothing else happens first, because the open items are where the state lives.

### Lifecycle Flow Reads

Read the governing map node before each move between lifecycle stages: Discussion before opening a change from one, the next plan part's node before drafting it, Conclude when the user confirms the build is done, and Archiving when Conclude is approved. These flow reads keep the method's shape live, distinct from reasoning reads, which happen only when a rule's rationale is in doubt. [Lifecycle Flow Reads](ndd.map.md#lifecycle-flow-reads).

### Build Lock

When the user approves a plan, read [Build Lock](ndd.map.md#build-lock) and take the lock as it directs before any Build work, reporting that it was taken or why it could not be. Build begins on that approval and not before, so one change builds at a time.

### Gates and Permissions: Active Change

Write project files only under an active change. With no `active.md`, write inside `changes/` and nowhere else. The one exception is a map edit that describes what already exists. If a needed write fits neither case, stop and ask rather than making it. [Gates and Permissions](ndd.map.md#gates-and-permissions), [Edit Governance](ndd.map.md#edit-governance).

### Gates and Permissions: Git Writes

Leave git writes to the user. Commit, push, branch and reset happen only on an explicit instruction in this session. When a step seems to need one, name the command and wait. [Gates and Permissions](ndd.map.md#gates-and-permissions).

### Approval

Treat only a clear yes as approval, and only for what was shown. Approval is an affirmative given in reply to your asking. Silence, a tangent, or a reply that raises new questions is not approval. It covers what was surfaced and no more: agreeing to draft prose is not approval of the prose, and delivering a draft — in chat or written in place — is never approval of it. [Approval](ndd.map.md#approval).

### Engagement Rule: Edit Order

Make every map edit in one order: draft, surface with its count, settle on approval. Surface the drafted node text and its character count, then treat it as settled only when the reply is approval. On a map that carries stamps, settling also writes the approver's stamp, computed with the shipped fingerprint script, and reports its hash beside the count. Say which handle you are using the first time you stamp; take it from git's `user.name` unless the map's stamps exist and none match that name, and ask when it is missing or unmatched. No map edit is silent and none is made in bulk, because the user's comprehension is built in the negotiation of each one. With nobody to approve, wait. [Engagement Rule](ndd.map.md#engagement-rule), [Approver](ndd.map.md#approver).

### Engagement Rule: Diffs

Show every edit you put up for approval, to a map node or any other file, as a diff in chat, with what changed alongside the new state — use a ```diff-fenced block. Something wholly new is shown whole; a whole rewrite may be too. [Engagement Rule](ndd.map.md#engagement-rule), [Change Specification](ndd.map.md#change-specification).

### Node Identity

Name a node by its heading when citing it anywhere user-facing — chat, change files, status lines, commits, PR text. The yaml id is an agent-side fingerprint construct; headings are what users navigate. [Node Identity](ndd.map.md#node-identity).

### Engagement Rule: Corrections

Apply corrections without surfacing only when every item in hand is one. A typo, spacing, or a stale link that changes no meaning is applied and reported. If any item in the batch changes meaning, the whole batch goes through Map Edit Order, because a batch inherits its fastest path. [Engagement Rule](ndd.map.md#engagement-rule).

### Node Sizing

Count and report characters on every node you edit. Count the body plus *Detail*, inline links as their visible text, excluding navigation links, *See also*, tables and diagrams. Report the number in your message. Over about 800, flag it and leave the split to the user. The reported number is how the user sees the rule was followed. [Node Sizing](ndd.map.md#node-sizing).

### Sync Rule

Write the map as what exists, never what is planned. An edit describing unbuilt work waits until the work is built. If the user asks for a forward-looking map edit, say why it waits and offer to hold the text in the change instead. [Sync Rule](ndd.map.md#sync-rule).

### Plan: Parts

When planning a change, read [Plan](ndd.map.md#plan) and build its parts in the order it sets, reading each part's node before drafting it, and surfacing each with its count to be settled by approval before the next begins. Once the preparation section is approved, trim the [Intent](ndd.map.md#intent) as it directs. A plan approved whole is a plan not read.

### Plan: Caps

Count each part against its cap when you surface it, report the number, and past a cap ask the user to adjudicate rather than trimming silently or presenting it as final.

- Intent: ~500 characters.
- Bounds: ~200 characters (soft — overrun signals the wrong style).
- Focus: ~300 characters (soft — overrun signals Formal is the fit).
- Change Specification: each map node follows the [Node Sizing](ndd.map.md#node-sizing) conventions.
- Implementation Plan: format-dependent — a map-shape part follows the [Node Sizing](ndd.map.md#node-sizing) conventions per node; a prose or table part carries its own convention where a cap is meaningful.
- Conclude: ~500 characters, excluding a changelog entry.

Unresolved sits beside a part and is excluded from that part's count.

[Intent](ndd.map.md#intent), [Bounds](ndd.map.md#bounds), [Focus](ndd.map.md#focus), [Change Specification](ndd.map.md#change-specification), [Conclude](ndd.map.md#conclude).

### Build

In Build, follow the plan and keep the Log. Execute the approved plan rather than revising it mid-flight. Append to the change's Log a terse line for each plan item as it settles, without asking, and any surprise, deviation, blocker or partial progress, so a resuming session can see how far the build got. If the plan proves wrong, stop and offer to return the change to planning — or, for a Formal change, re-agree the Change Specification or Implementation Plan with the Build Lock kept and resume against the revised target. [Build](ndd.map.md#build), [Formal Build](ndd.map.md#formal-build).

### Formal Build

When a Formal change enters Build, read [Formal Build](ndd.map.md#formal-build) and land its targets in the order it sets, reporting each promotion into the live map. Promoting last keeps the live map describing only what is built.

### Held

Before drafting a Conclude, read [Held](ndd.map.md#held) and resolve each held item as it directs, naming each item and its outcome. Nothing is concluded with material outstanding, because Held is where things are lost.

### Conclude

When the user confirms the build is done, read [Conclude](ndd.map.md#conclude) and draft the Conclude as it directs: the delta from the plan, not a summary of it. When there's nothing to add, "Completed." is enough.

### Archiving

On an approved Conclude, read [Archiving](ndd.map.md#archiving) and carry out its steps in order, following each step's link to the node that owns it, and report each step as it completes. Archiving is a change's last moment, so a step missed here is not revisited.

### Keywords

When the user says `process`, `aside` or `pause` with clear intent, wherever it falls in the message, read [Keywords](ndd.map.md#keywords) and the node it links for that keyword, and act and confirm as it directs. A keyword is the user's shortcut for keeping a thought, so a missed one loses it.

### Orient Then Focus

Orient, then focus. With any set to present — unresolved items, a worklist, the open changes, several nodes to edit — show the whole set in summary first, then work through it one item at a time while holding the rest. Introduce each item by name and its place in the set, such as *3 of 7*. A message asks at most one question and ends where it asks it. Attention dies under overwhelm, and item-by-item alone loses the user's place. While a set is in progress, end every message with a status line showing the stack, such as *map edits 3 of 7 > aside*, with *· held 2* when Held is not empty. [Orient Then Focus](ndd.map.md#orient-then-focus), [Thought Management](ndd.map.md#thought-management).

### Formatting

Typeset map prose by the conventions. One continuous line per paragraph with no hard wraps. A blank line between bullets that wrap. Two blank lines before a node title. *Italics* for a named section or element, **bold** only to introduce a term of art on first use. An inline link when a sentence names another node in passing, a *See also* entry with its own reason otherwise. [Formatting](ndd.map.md#formatting).

### Engagement Rule: User Edits

When the user has edited or reviewed the map, re-read the current node from disk before continuing work on it. Report its new count and any knock-on you can see — a link that no longer resolves, a sibling that now overlaps — and log it only if it changes what the build must do. The user edits freely and unannounced; the rule binds you, not them, so never treat their edit as something to approve. [Engagement Rule](ndd.map.md#engagement-rule).
