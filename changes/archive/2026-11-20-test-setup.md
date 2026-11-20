# Test setup

**Change Style:** Vibe \
**Version:** 3.9.2-dev

## Intent

The testing map should say, in one node under *Testing* that the checks link to rather than each mentioning its own, what the checks need to run — uv, git, Node, and Playwright with its Chromium — roughly what each is needed for, which are optional, what is skipped without each, and that once set up none needs internet access.

## Bounds

Edit the map, and the viewer test's header only to say how to put an installed Node on the PATH; leave the checks' code as it is, and keep exact commands and version pins in the script headers, which the new node points to.

## Context

Raised as an aside on 2026-11-19 during 310. *Map Viewer Check*'s page-script parse check was skipped as "node not installed", though Node was on the machine through pyright's nodeenv (`~/.cache/pyright-python/nodeenv/bin`), just not on the PATH. Setup is currently spread across script headers and single sentences in *Map Viewer Check* and *Map Viewer Browser Check*; exact commands and version pins may stay in the headers. Also from 330 (2026-11-20): *Map Viewer Check*'s sentence "It needs no internet access, so it runs wherever the viewer does." was cut for size; this change should carry that fact.

## Log

- 2026-11-20, plan approved, Build Lock taken.
- Version 3.9.2-dev claimed, a patch bump. Map edits planned: 1 new *Test Setup*, 2 *Testing*, 3 *Contents*, 4 *Map Viewer Check*, 5 *Map Viewer Browser Check*.
- 1 *Test Setup* added to the testing map, ~650, stamped 24b3715f; install commands kept in the script headers (moving them ~+560 and would duplicate the Playwright pin).
- 2 *Testing*: child link and bullet for *Test Setup*, ~781, stamped 3478cec5.
- Bounds loosened mid-build at the user's request, ~205, approved: the viewer test's header may say how to put an installed Node on the PATH.
- Viewer test header: how to put an installed Node on the PATH for good, via ~/.profile.
- 3 *Contents*: *Test Setup* added to the overview (a correction, reported).
- 4 *Map Viewer Check*: Node linked to *Test Setup*, ~775, restamped 3cfab9ac.
- 5 *Map Viewer Browser Check*: setup sentence replaced by a link to *Test Setup*, ~585, restamped 1ad1fbe5.
- Beyond the Intent, at the user's request, made in one go: the script names in *Fingerprint Check*, *Install Check*, *Map Viewer Check*, *Map Viewer Browser Check* and *Map Viewer Due Check* linked to their files; counts unchanged, each restamped. The viewer shows such links as text.

## Conclude

Completed. Beyond the plan: Bounds was loosened mid-build so `map_viewer_test.py`'s header says how to put an installed Node on the PATH for good, and the testing map's script names now link to their files. In hx these open with `gf`, not `gd`, as marksman follows markdown links only; the map viewer shows them as text.
