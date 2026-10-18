# Parking and session loss

## Purpose

Work needs a defined way to be parked — stopping for the day, a reboot — and to survive an unplanned loss of session with as little lost or misread as possible. Raised 2026-10-16 after change 020 entered Build on scope nobody approved.

## What happened in 020

The baseline commit had no *Status* section. One was added afterwards, probably when the user asked to stop and resume later, and grew with each pause into a running plan summary: approvals, checks done, and a list of non-map work for Build (AGENT-RULES rules 1 and 19, both standards). At the next Startup Scan the agent placed the change from that section, reported "plan complete", and on the user's approval landed the listed edits without surfacing them.

## Gaps in the map

- **No planning pause record.** Build has its *Log* and Discussion its *Resume* anchor, trimmed on resumption; a change mid-planning has nothing, and *park* already means something else (a separate Intent-only change). The agent improvised, and nothing trimmed what it wrote.

- **Invented sections.** Nothing says a change document carries only the sections the method defines, though Change Lifecycle says state is read from contents, "not from any status field".

- **Formal's non-map deliverables.** Since 2.3.0 the Change Specification is map-only; with no Implementation Plan, non-map work had no approved home and its scope landed in the invented section.

- **Non-map method prose.** Formal Build lands non-map assets in place, and Map Edit Order covers only map nodes, so AGENT-RULES and the standards — method prose in this repository — could be written unseen.

- **Build progress is invisible.** Build says the agent marks progress, but the *Log* takes only the unexpected and "routine execution going to plan needs no entry", so settled plan items leave no trace on disk. In 020 the user asked for one Log line per settled item, written without asking (2026-10-16).

## Agreements

- **Unapproved work may be lost on an unplanned disconnection.** The method need not protect chat-side drafts against session loss (2026-10-17).

- **Parking is user-requested and writes a resume file.** On request the agent records overall status: which change, where it sits in its lifecycle, and anything unapproved. It should be similar in shape to the existing pause records (2026-10-17).

- **The resume note is `changes/resume.md`, consumed on read.** It is kept separate from `active.md` so that file's existence still means only the Build Lock. It sits at the root of `changes/` so the Startup Scan, which treats everything in `open/` as a change or discussion, needs no exemption for it. The Startup Scan reports the note with its date. The note is deleted at the first write after resuming, not at the scan, so a start-and-quit restart keeps it. Anything lasting belongs in the Log or the discussion record. Pausing is requested with a `pause:` keyword or in plain words; *park* is avoided because it already names Intent-only changes (2026-10-17).

- **Two layers: the note points, the item holds the detail.** `changes/resume.md` names what was in progress and where it sits. Detail stays with the item: the *Resume* anchor for a discussion, the *Log* for a build. A change parked mid-planning has no anchor of its own and needs no new section, so the note itself carries which part was being drafted and what was unapproved. Both layers are trimmed on read (2026-10-17).

- **Drafts written in place sit between a marker pair.** On an unplanned loss, an in-place draft would otherwise read as settled. Proposed syntax: `<!-- draft -->` and `<!-- /draft -->`, which are visible in the raw file and invisible when rendered. Approval deletes the markers, and declining deletes the whole region. The Startup Scan reports anything inside a pair as unapproved. Chosen over a git-based check because it works without git. The markers apply wherever a draft is written in place: change documents and map nodes alike (2026-10-17).

- **Invented sections are left alone for now.** A fixed section set is too rigid. A rule that extra sections are "never read as state" protects little, being another reading rule of the kind 020 bypassed. A Startup Scan check adds weight to a node that is already heavy. The bet is that `changes/resume.md` removes the motive: in 020 the *Status* section stood in for a missing pause mechanism. Revisit if invented sections recur (2026-10-17).

- **Keep the Startup Scan light.** It is growing weighty, and the resume note and draft-marker reporting both add to it. The change that specifies them should keep those additions minimal (2026-10-17).

- **Change Specification may hold non-map targets.** The 2.3.0 map-only restriction (see archived `2026-10-07-formal-specification-as-map-content`) guarded against a parallel specification, meaning prose competing with the map. A target version of a non-map asset, derived or supplementary, does not compete with the map. Excluding such targets is what left 020's non-map work without an approved home. Non-map targets sit inline or in the companion folder, and each is surfaced as a diff and approved like a node. The map stays authoritative, and a target that overlaps the map's job is questioned. Which assets get specified upfront is negotiated as part of the change. This closes both the "no approved home" gap and the "landed unseen" gap (2026-10-17).

- **Build logs one line per settled plan item.** The agent writes it without asking, as each item lands, so a resuming session can see how far the build got even after an unplanned loss. This adopts the practice the user asked for in 020 (2026-10-17).

## Open questions

## Conclude

Produced two parked changes. [090, parking and session state](2026-10-18-parking-and-session-state.md): a `pause:` request writes `changes/resume.md`, deleted at the first write after resuming; in-place drafts sit between draft markers; Build logs each settled item. [091, non-map specification targets](2026-10-17-non-map-specification-targets.md): a Formal Change Specification may hold non-map assets, each approved as a diff. Dropped: a fixed section set or Startup Scan check for invented sections, betting the resume note removes the motive. Revisit if they recur.
