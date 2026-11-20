# Test setup

## Intent

The testing map should say what the checks need to run — uv, git, Node, and Playwright with its Chromium — which are optional, and what is skipped without each, in one node under *Testing* that the checks link to rather than each mentioning its own.

## Context

Raised as an aside on 2026-11-19 during 310. *Map Viewer Check*'s page-script parse check was skipped as "node not installed", though Node was on the machine through pyright's nodeenv (`~/.cache/pyright-python/nodeenv/bin`), just not on the PATH. Setup is currently spread across script headers and single sentences in *Map Viewer Check* and *Map Viewer Browser Check*; exact commands and version pins may stay in the headers. Also seen in 320: `tests/fingerprint_test.py` finds the helper only when run from `tests/`, as it builds its paths from the working directory. Also from 330 (2026-11-20): *Map Viewer Check*'s sentence "It needs no internet access, so it runs wherever the viewer does." was cut for size; this change should carry that fact.
