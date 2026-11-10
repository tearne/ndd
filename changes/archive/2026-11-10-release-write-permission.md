# Release write permission

**Change Style:** Vibe

## Intent

A release step the user has confirmed should be able to write the files it names, such as the changelog fold, without a change in Build, so a release never stalls on the project-file gate or slips past it.

## Bounds

One map node changes, *Gates and Permissions* or *Versioning*, chosen with the user before drafting, plus the *Active Change* rule, A/B tested before it ships.

## Context

Seen in 107's rule A/B test (2026-11-10): agents asked to run a release stopped before the changelog fold, since no change was in Build and the map exemption does not cover `CHANGELOG.md`.

## Log

- 2026-11-10: Plan approved; Build Lock taken.
- 2026-11-10: Minor bump agreed, claiming 3.3.0-dev.
- 2026-11-10: *Gates and Permissions* gains the confirmed-release-step exemption, stamped (d70f41f6); 822 characters, over the bound.
- 2026-11-10: *Gates and Permissions: Active Change* rewording approved; A/B test running before it lands.
- 2026-11-10: A/B test of the Active Change rule: on an overall "release" instruction the new wording folded the changelog without surfacing a draft. User wants release writes to follow an approved draft; *Gates and Permissions* re-agreed to "a release step whose draft the user has approved", re-stamped (da547e37).
- 2026-11-10: Rule A/B test, 3 tasks × current/new wording. Confirmed fold: both wrote it, README untouched, commit and tag asked for. README typo with no change in Build: both stopped and asked. Overall "release" instruction: current stopped and asked; new folded without a draft (above). Revised wording re-run on that task: surfaced the fold as a draft and waited for approval. Revised rule kept.
- 2026-11-10: *Gates and Permissions: Active Change* landed in `method/AGENT-RULES.md`.

## Conclude

Built within Bounds in *Gates and Permissions*, touching `method/ndd.map.md` and `method/AGENT-RULES.md`. The A/B test showed "confirmed" was too loose: an overall release instruction let the fold skip its draft, so the exemption was re-agreed in Build to a release step whose surfaced draft the user has approved. The node ends at about 832 characters, over the bound.
