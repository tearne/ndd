# Parking and session state

**Change Style:** Formal

## Intent

Let work be paused on request and resumed without misreading its state. A pause leaves a note that the Startup Scan reports; a draft written in place is marked until approved; Build logs each settled plan item. All keywords are recognised by clear intent rather than as a message prefix.

## Context

Promoted from discussion [parking and session loss](../archive/2026-10-17-parking-and-session-loss-discussion.md) (2026-10-17), which records the reasoning and the 020 incident behind it. The Startup Scan is already weighty, so its additions stay minimal.
## Change Specification

Targets: whole-map copy `090-parking-and-session-state/ndd.map.md` and `090-parking-and-session-state/AGENT-RULES.md`, dropped at archiving.

## Log

- Build started; minor bump, claiming 2.7.0-dev. Live map unchanged since baseline, so promotion goes in bulk (2026-10-18).
- AGENT-RULES target landed in `AGENT-RULES.md`.
- Map target promoted in bulk into `ndd.map.md`; all eleven stamps hold (none due), tests pass.

## Conclude

Pause became Pause Keyword, under Keywords. Recognition by clear intent rather than prefix spread to all keywords, so `process` and `aside` lost their colons, and the aside summary in Keywords was fixed. The resume note is deleted when the paused work resumes, not at the first write; other work first prompts keep or delete, and a pause onto a note asks for guidance. Approval split, drafts and markers moving to a new Drafts node. Tidy reports stray draft markers. 070 widened to cover the Startup Scan.
