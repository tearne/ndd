# Changelog

A changelog records notable changes to the project, newest at the top. It complements git history by surfacing what's worth knowing at a glance. A project that keeps one is versioned, in [semver](https://semver.org/); if it already has an established changelog layout, keep the layout and use semver headings.

## Headings

Each heading is a released version or a change awaiting release.

- Each entry is an `H2` heading with a version: `## 1.2.0`.
- A change awaiting release is entered under its final dev version: `## 1.2.1-dev.3`, or `## 1.2.1-dev` where the changelog is the only version record.
- At release, the dev headings fold into one heading under the latest number without suffix, with the date: `## 1.3.0 — 2026-04-24`.
- Entries are added to the top of the file.
- For the bump kind and dev versions, follow [Versioning](../ndd.map.md#versioning).

Example:

```
## 1.3.0-dev.2

- Added `--dry-run` mode to the build script.

## 1.2.1-dev.1

- Fixed the exit code on a missing config file.

## 1.2.0 — 2026-04-10

- Added the `export` subcommand.
```

## Writing an entry

- Trivial changes — typo fixes, minor doc wording — may not warrant a new section. Substantive changes do.
- One line per change; start with the affected file or a verb.
- Keep it brief: the reader is scanning. Detailed rationale belongs in the change document and the commit message.
- If downstream migration steps are needed, include them as a short paragraph below the bullets for that entry.
