# Suggested standards as indexed map nodes

**Mode:** Formal

## Intent

The NDD map drops COD's `ADDITIONAL/` class of guidance — style, versioning, changelog format, and language or domain standards like Rust and POS. Preserve them as a convention: NDD ships a set of **suggested** standards a project can adopt, adapt, or ignore, rather than mandates.

The standards stay as **ordinary markdown guides** — not rewritten into map-node format. The map carries only a **Standards index** that points to them, surfaced through the Contents overview so an agent discovers what is available and opens just the guide a task actually touches — never loading the rest into context. This mirrors COD's `ADDITIONAL/README`, now expressed as a map node.

Depended on by go-live (130): the superseded `STYLE.md` and `ADDITIONAL/*` must land here before COD is retired.

## Approach

### A top-level Standards node holds the convention and the index

The map gains a **Standards** node, sibling of Tooling and listed in Contents. It states the convention — NDD ships standards that a project applies or loads on reference — and carries the index table (guide, one-line description, loading cue). Two tiers: always-on **defaults** like the code Style guide, which apply unless a deviation is flagged and approved, and **on-reference** suggestions loaded when a task touches them (passive or prompted). Top-level because guidance for the *rendered code* is its own concern, distinct from the map spec, the change process, and editor tooling. Authored through per-node negotiation.

### Guides ship as plain markdown under `standards/`

The guides keep their existing markdown verbatim (no framework coupling was found) in `standards/`, shipped to `ndd/standards/`. Consumers get the suggested set locally to adopt or adapt.

### The installer fetches the guides in its existing fetch list

`install.sh` fetches each guide into `ndd/standards/` alongside the map, bootstrap, and changelog it already fetches — adding a standard is a one-line edit in the same place. No manifest, no separate machinery; the installer mock test asserts the expected guides land, so a forgotten line fails the test.

### The suggested set carried over from COD

Style, Rust, POS, Versioning, and Changelog-format — COD's `ADDITIONAL/` set plus the code Style guide. Style is the always-on default; the rest load on reference. Versioning/Changelog serve a *consumer's own* project; NDD's own choice is already fixed.

## Plan

- [x] Copy the five guides into `standards/` (`STYLE.md`, `RUST.md`, `POS.md`, `VERSIONING.md`, `CHANGELOG.md`) from COD's `agent/STYLE.md` and `agent/ADDITIONAL/`.
- [x] Add a top-level `Standards` node to `map.md` (convention + index table), with the root child link and Contents tree updated — via per-node negotiation.
- [x] Extend `install.sh` to fetch each guide into `ndd/standards/`.
- [x] Re-test the installer mock, asserting the five guides land in `ndd/standards/`.

## Conclusion

Completed as planned. The `Standards` node landed as a top-level sibling of Tooling with an index table; the only notable refinement during build was recharacterising the guides by *what they're for* rather than by name — POS's loading cue became "writing a system-administration or small utility script" so an agent can judge applicability without opening the file.

No version bump — this folds into the unreleased `1.0.0`, so no changelog entry.

Documentation impact: none beyond the map node itself. Go-live (130) can now retire COD's `STYLE.md` + `ADDITIONAL/*`, since they are preserved here.
