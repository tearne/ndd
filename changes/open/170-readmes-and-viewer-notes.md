# Readmes and viewer notes

**Change Style:** Formal

## Intent

The shipped method should open with a thin introductory readme for those using NDD in a project, and this repository's README should keep to what concerns the repository, such as installing and developing NDD; both point into the map rather than restate it. The map should carry concise notes on using the map viewer, including reaching it through a container's port proxy and an SSH forward, and the method's readme should point to them.

## Context

Raised by the user on 2026-11-17 after 140 Web UI approvals. Reaching the viewer in an incus container took three hops: `incus config device add myContainer port8081 proxy listen=tcp:127.0.0.1:8081 connect=tcp:127.0.0.1:8080` on the host, `LocalForward 8082 localhost:8081` in the SSH config, then `localhost:8082` in the browser. Not every setup works this way, but developers working with NDD want introductory notes. The method map's *Map Viewer* *Detail* already gives the run commands and a one-hop `ssh -L`.

The root `README.md` already ships into a client's `ndd/` (*Shipped Assets*), though it speaks mostly of installing. What goes in which readme is for the plan to settle.

## Change Specification

Drafted in copies in [170-readmes-and-viewer-notes/](170-readmes-and-viewer-notes/): `method/ndd.map.md`, `map.md` and `README.md`, taken 2026-11-17 before any edit; `method/README.md` drafted there new. Planned:

1. *Map Viewer Access* (method map, new, under *Map Viewer*): reaching the viewer from another machine, one hop by `ssh -L` and through a container's port proxy, the port at each hop, and that the browser's Host must stay 127.0.0.1 or localhost.
2. *Map Viewer* (method map): the child link; its *Detail* keeps the run commands, the forwarding line moving to the new node.
3. *Installation* (method map): names the method readme as where a project's people start.
4. `method/README.md` (new, shipped): a thin introduction for a project using NDD, pointing into the map.
5. `README.md` (root): kept to the repository, installing and developing NDD, pointing to the method readme.
6. *Shipped Assets* (project map): the method readme, and whether the root README still ships.

## Unresolved

1. Whether the root `README.md` still ships into `ndd/` once the method has its own readme.
