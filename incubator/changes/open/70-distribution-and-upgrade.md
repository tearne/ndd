# Distribution and upgrade path

## Intent

A project that adopts COD needs a way to pull later improvements to the method, or it ossifies at whatever version it first installed. The reworked, map-based method has no distribution story yet: the old model — `opt-in.py` copying versioned snapshots into `changes/agent/<version>/`, the agent diffing `CLAUDE.md`'s pointer to surface migration concerns on update — was built for the document-based method and doesn't carry over. We need to decide how the method reaches adopting projects and how they upgrade in place.

Open questions this change must settle: whether adoption is still an installer copying files, or a project tracking the method repo directly; whether the method ships as discrete versioned snapshots or a moving edge; and — the hard part — how an upgrade reconciles with a project's *own* `map.md` and in-flight changes, since the method's files and the project's content now share the same map surface. Graceful upgrade matters most where a project has customised or extended what it adopted.

Flagged **critical before public go-live** — releasing the reworked method for adoption without an upgrade path strands early adopters. It does *not* gate the incubator's own internal go-live (dogfooding its map-based bootstrap), which ships nothing to anyone. Parked as its own change because it is a sizeable design area independent of the `map-build-out` migration.
