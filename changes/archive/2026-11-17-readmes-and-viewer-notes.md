# Readmes and viewer notes

**Change Style:** Formal \
**Version:** 3.7.1-dev

## Intent

The shipped method should open with a thin introductory readme for those using NDD in a project, and this repository's README should keep to what concerns the repository, such as installing and developing NDD; both point into the map rather than restate it. The map should carry concise notes on using the map viewer, and the method's readme should point to them.

## Context

Raised by the user on 2026-11-17 after 140 Web UI approvals. Reaching the viewer in an incus container took three hops: `incus config device add myContainer port8081 proxy listen=tcp:127.0.0.1:8081 connect=tcp:127.0.0.1:8080` on the host, `LocalForward 8082 localhost:8081` in the SSH config, then `localhost:8082` in the browser. Not every setup works this way, but developers working with NDD want introductory notes. The method map's *Map Viewer* *Detail* already gives the run commands and a one-hop `ssh -L`.

The root `README.md` already ships into a client's `ndd/` (*Shipped Assets*), though it speaks mostly of installing. What goes in which readme is for the plan to settle.

## Change Specification

Drafted in a companion folder on copies of `method/ndd.map.md`, `map.md` and `README.md`, taken 2026-11-17 before any edit, beside the new `README.ndd.md`; promoted in Build, and the folder dropped at Archiving. Each approved and stamped there:

1. *Map Viewer Access* (method map, new, under *Map Viewer*): reaching the viewer by forwarding one hop at a time, the browser addressing 127.0.0.1 or localhost; direct SSH and SSH to an Incus container as examples. 780 characters, stamped 960692e9.
2. *Map Viewer* (method map): a child link to it, and its *Detail* pointing there for forwarding. 768 characters, stamped 320e5c6c.
3. *Installation* (method map): `README.md` in `ndd/` introduces the method. 814 characters, stamped ac7cb95d.
4. `README.ndd.md` (new): the method readme, at the repository root so its links to `method/` resolve both here and in `ndd/`, shipped as `ndd/README.md`.
5. `README.md` (root): kept to the repository, installing and developing NDD, pointing to `README.ndd.md`; no longer shipped.
6. *Shipped Assets* (project map): `README.ndd.md` ships as `README.md`, the root `README.md` stays in the checkout. 617 characters, stamped 6be4dbca.
7. *NDD Project* (project map): its *Map Viewer* line no longer says read-only, stale since 140. 728 characters, stamped 4b86776e.

Building it also changes the installer's shipped list and has the Install Check confirm that `ndd/README.md` is the method readme. A method map *Contents* entry for *Map Viewer Access*, approved 2026-11-17. No Implementation Plan proposed: no consequential delivery choices remain.

## Conclude

Completed. The install test's link check passes only after promotion, since the shipped readme links to *Map Viewer Access*, new in the method map.

## Log

- 2026-11-17: Build Lock taken; live maps and README unchanged since the baseline.
- 2026-11-17: version 3.7.1-dev claimed, a patch bump.
- 2026-11-17: `README.ndd.md` added at the root and `README.md` replaced, both as approved.
- 2026-11-17: installer ships `README.ndd.md` as `ndd/README.md` (`RENAMED`), the root `README.md` no longer; the install test's shipped list follows, and it checks `ndd/README.md` is the method readme. Its link check failed until promotion, as `Map Viewer Access` was only in the copy.
- 2026-11-17: promoted whole files, the live maps not having drifted: `map.md` (*NDD Project*, *Shipped Assets*), `method/ndd.map.md` (*Map Viewer*, *Map Viewer Access*, *Installation*, *Contents*). Each live fingerprint matches its stamp. All four test scripts pass.
- 2026-11-17: handed back for testing as 3.7.1-dev.1.
