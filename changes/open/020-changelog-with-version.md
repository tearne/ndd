# Changelog with version

**Change Style:** Formal

## Intent

Agree a change's changelog entry together with its version, so each versioned build carries its own heading and no pending heading is needed. Say when the entry is drafted, how it relates to the patch bump at each hand-back and to the entry at Archiving, and what Release Steps still does once Build writes the version.

Raised as an aside (2026-10-14).

## Context

Three places touch the version. Build's *Detail* agrees a bump kind at build start and bumps patch every hand-back; Archiving proposes a changelog entry before the move; Release Steps in `map.md` bumps the version with a new top entry. Changes 340 and 010 skipped Build's bump, so their entries collected under an ad hoc `## Pending` heading in `CHANGELOG.md`.

## Change Specification

Targets: whole-map copies at `020-changelog-with-version/ndd.map.md` and `020-changelog-with-version/map.md`.

## Held

- The existing `## Pending` section in `CHANGELOG.md`, holding entries from 340 and 010, must be given a version when this change lands.

- Candidate heading form: the version written at build start with a marker, such as `## 2.4.0 — PENDING`, replaced by the date when it ships.
