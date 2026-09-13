# Navigation line breaks

**Cadence:** Wander

## Intent

Every navigation link line ends with a backslash, so a renderer breaks the line after each link instead of folding the block into one paragraph. The fingerprint helper and reference test still drop such lines whole, so no hash moves. Formatting and Navigation Links state the convention.

### Context

- Raised 2026-09-13 after seeing GitHub fold a node's navigation into one line. Set aside: two trailing spaces, invisible and stripped by editors; a one-line breadcrumb with separators, which changes the one-link-per-line rule and the tooling; blank lines between links, which makes the block tall; a bullet list, which would read like the Contents and move every fingerprint.

## Log

- 2026-09-13: A backslash on the last line of a paragraph renders as a literal backslash in CommonMark, so the convention is every navigation line but the last; a one-link block carries none. 81 lines carry one across the maps and fixtures. Helper and test patterns allow the optional backslash; every fingerprint identical before and after; both tests pass.
- 2026-09-13: The convention lives in Navigation Links only; the Formatting bullet was added, approved, then moved out on the user's call, since the backslash is specific to navigation blocks. Intent overstated the scope in naming both nodes.

## Conclude

Completed. The convention ended up in Navigation Links alone, not Formatting as well.
