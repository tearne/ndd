# Map viewer iteration

**Change Style:** Emergent

## Intent

Iterate on the map viewer, exploring options to fix its issues and add features, until the user judges it good enough for now.

## Focus

The viewer issues and features the user raises, taken one at a time: options explored, one chosen, built and tried before the next. *Map Viewer Check* should keep passing.

## Log

- Build Lock taken; version claimed as 3.5.3-dev (patch), viewer VERSION to 0.3.0 once a feature lands.
- Item 1, raised: folding tree branches is lost on moving to another node, which reopens everything; only the branches needed to reach the destination should open.
- Open, for later: the user runs the viewer outside this container; how it's run there to be discussed.
- Item 1, option C chosen (no page reload): links to nodes and approval diffs fetch the page and swap in its content; the tree keeps its folds, opening only the destination's branches, and is redrawn only if the map's shape changed. Back and forward handled; an error falls back to a full load. JS untested here (no browser in the container); the test checks each page has the one <main> and <aside> the swap needs. VERSION 0.3.0.
- Item 1 checked in headless Chromium (Playwright, user-installed, scratch script outside the repo): folds survive tree and body links, only the destination's branches open, back/forward and approval-diff links work, no reloads, no script errors.
- Item 2, raised: a map reached only by prose links, such as the method map, joins the tree only while one of its nodes is shown, so leaving it redraws the tree and loses the folds; the user suggests every linked map always be in the tree.
- Item 2 built as the user suggested: every map file linked from a map in the tree, transitively, is drawn as its own tree beneath, so the tree is the same on every page and is never redrawn. Demo gained linked.map.md, linked only in Demo's prose; the test checks it is drawn and that two pages share one tree (fails on the previous viewer). Checked in Chromium on this repo: method map → main → method map keeps folds, no redraw. Demo VERSION 0.3.0.
- Item 3, raised: a branch's +/− button opens everything below when any of it is folded, and folds only when all is open; the user wants it the other way round.
- Item 3 built: the button folds the branch and all below while any of it is open, and opens it all only once all is folded; its label follows (− while anything is open). Checked in Chromium.
- Item 4, raised: keep one node in view while following a link it holds, such as a term's definition; the user proposes a second pane, with links clicked in the left pane loading into the right.
- Item 4 built (two panes, the user's proposal with the agent's defaults): a Split button opens a second pane; the node's links then load there, as do the pane's own; tree links load on the left. Swap and Close buttons; the URL's side parameter holds the second pane, so back, forward and reload keep the pair. Pages restructured so a view (node or approval diff) can fill either pane. Bug found in Chromium and fixed: parse_qs dropped the empty side parameter. Test gained side-pane checks.
- Item 5, raised: back and forward buttons on each pane. Agreed: each pane walks its own history, kept in the browser history entry so pane buttons, browser back and reload agree; a pane step is itself a browser step; Swap swaps histories, Close drops the side's.
- Item 5 built as agreed: ◀ ▶ in each pane's bar, disabled at either end; histories held in history.state. Checked in Chromium through pane steps, browser back, reload, Swap and Close; no script errors. The empty pane Split opens is replaced, not pushed, by the first link followed into it.
- Architecture review, at the user's request; findings, most pressing first:
  1. Parsing scales badly: `node_lines` rescans the whole file per call, so drawing the tree runs `node_ranges` ~200 times, 0.14 s a page on this repo and growing with map size squared. A per-file node index cached with the text would make lookups constant.
  2. The page script and styles live in Python strings: ~175 lines of JavaScript with no syntax check, and a non-raw string, so a backslash means something different from what it reads as (`"\\n"` already needed).
  3. The browser checks that found real bugs live only in `/tmp`; the suite cannot see the script. An optional Playwright check in `tests/map_viewer/`, skipped when Playwright is missing, would keep them.
  4. The server's HTML and the script share an unwritten contract (`main`, `#side`, `aside`, `a.here`, button classes, the `side` parameter); nothing names it in one place.
  5. Loose tuples carry the data — `(file, name)`, `(commit, date, lines)`, `(at, hash)` — where small named types would read better.
  6. Any `KeyError` while rendering answers 404, so a bug can pass for a missing node.
  7. Tree drawing sits in the map-reading section; sections no longer follow one concern each.
- Paused 2026-11-11 awaiting the user's choice of review findings; recommended 1–3 now, 4 alongside 3, 5–7 as tidying. Nothing unapproved.
- Resumed 2026-11-13; pause entry deleted.
- Findings 1–3 chosen, taken in order; 4–7 not chosen for now.
- Finding 1 built: read_map keeps a node index with each file's text, so lookups no longer rescan; a repeated heading still resolves to the first. Tree on this repo 142 ms → 26 ms, file scans per tree 202 → 0. Map Viewer Check passes.
- Finding 2, the user chose: keep one file, make the script and styles raw strings, and have the test syntax-check the script with node when present.
- Finding 2, the user's reason: for now the viewer should stay a self-contained single-file server.
- Finding 2 built: STYLE and SCRIPT are raw strings (the script's "\\n" now reads "\n"), served text unchanged. Test gained script_parses: node --check on the served script, skipped when node is absent (as in this container). Tried with the node pyright bundles: passes, and fails on a deliberately broken script. Map Viewer Check passes.
- Finding 3 built: tests/map_viewer/browser_test.py, a uv script declaring Playwright, drives the page script in headless Chromium on map_viewer_test.py's demo and server: folds across tree links, body links and back/forward; the tree never redrawn; the approval diff swapped in; the fold button; split, reload, Swap, Close; each pane's history. Any script error fails it; with no matching Chromium it skips and says how to install. Each check failed when its behaviour was broken in the viewer.
- Surprise: unpinned, uv takes the newest Playwright, whose Chromium build (1255) isn't the one installed here (1254, Playwright 1.65.0), so by default it skips in this container; run here with uv run --with 'playwright==1.65.0' --script browser_test.py, which passes. Not pinned in the file.
- Open: Map Viewer Check in testing.map.md no longer describes the suite (no side pane, page shape, script parse or browser checks); to be brought up to date once the build settles.
- Playwright pinned to 1.65.0 in browser_test.py at the user's approval, matching the installed Chromium (1254); ./browser_test.py now runs its checks here and passes.
- Map Viewer Check tightened to one sentence of checks, covering the new ones; 513 characters, stamped 1fa6c24d.
- Setup steps added, at the user's request, as header comments in both tests: uv and git for map_viewer_test.py, Node.js optional; for browser_test.py, uv, then playwright install chromium and, on a fresh Linux machine, install-deps, repeated when the pin moves.
- Map Viewer Browser Check written to testing.map.md, 508 characters, stamped 9b9603d8.
- Testing gained the Map Viewer Browser Check link and entry, 659 characters, stamped 710420b9.
- Contents gained the Map Viewer Browser Check entry. Open item on Map Viewer Check closed.
- Item 6, raised: ship the viewer so users can easily run it in their own project.
- Item 7, raised: revisit approving from the web UI.
- Item 6 agreed: move the viewer alone to method/util/map_viewer.py, so the installer ships it; tests stay in tests/ and only point at the new path; Install Check checks it ships and starts; Map Viewer and the changelog drop "not shipped".
- Item 6 built: viewer moved (git mv) to method/util/map_viewer.py, its header giving the ndd/method/util/ path to run and its needs (uv, git); tools/ removed. fingerprint_test, map_viewer_test and viewer_demo point at the new path. install_test gained viewer_serves_the_project: the shipped viewer, run from a scratch project's root, serves its map.md (fails when broken). All four suites pass.
- Aside, not this change: the installer ships whatever sits under method/, so a local method/util/__pycache__/fingerprint.cpython-312.pyc ships too (pre-existing; .gitignore keeps it out of git, not out of the install).
- Map Viewer: ships, run as ndd/method/util/map_viewer.py; alert and demo sentence cut; 783 characters, stamped c72b6a08.
- Install Check gained the shipped-viewer bullet, 784 characters, stamped f2e62af9.
- Method map gained Map Viewer, for users: what it shows, read-only, how to run it from the project root; 759 characters, stamped 4058d54d.
- Map Viewer moved under Tooling, at the user's choice, from Sign-off; the stamp holds, as navigation links aren't fingerprinted.
- Tooling gained the Map Viewer child link and names it as a richer surface; stamped b2bce1d0.
- Open, deferred by the user: the map lacks the viewer's design reasons (read-only, single file), navigation (page swap, folds, linked maps, fold button) and the second pane with its histories; to be documented later, as a parked change if not here.
- Method map Contents gained Map Viewer under Tooling.
- Version re-claimed as 3.6.0-dev (minor), at the user's approval, since item 6 ships a new tool and method-map node; nothing depended on 3.5.3-dev. Map edits for item 6 done; the changelog entry waits for Archiving.
- Item 7 spun out at the user's request as parked change 140 Web UI approvals.
- Installer leaves out __pycache__ (open item 2 resolved, at the user's agreement); install_test expects the same and fails if a cache ships (checked by removing the filter). All suites pass.
- Shipped Assets names the map viewer and the caches left out; 503 characters, stamped 18d10271.
- Installer reviewed at the user's question: shipping needed no code beyond the __pycache__ skip. A pointer to the viewer in the installer's output or README offered and declined for now.
- Open item resolved: the viewer's design documentation parked as 150 Map viewer design in the map.
- Open item resolved: running the viewer outside this container, closed by the user as covered by item 6 (method map Map Viewer gives the run and port-forward steps).

## Conclude

Beyond the Intent's viewer iteration, the viewer now ships, as `method/util/map_viewer.py`, so the version was re-claimed as minor, 3.6.0-dev, and the method map gained *Map Viewer* under *Tooling*. The installer now leaves out bytecode caches. A Playwright browser check was added, pinned to the installed Chromium. Approving in the web UI was parked as 140, and documenting the viewer's design as 150. Of the review's findings, 4–7 were not taken.
