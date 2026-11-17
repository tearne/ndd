#!/usr/bin/env -S uv run --script --
# /// script
# requires-python = "==3.12.*"
# dependencies = ["playwright==1.65.0"]  # matches the Chromium build installed (1254)
# ///

# Drives the viewer's page script in headless Chromium, on the demo map that
# map_viewer_test.py serves: the tree keeping its folds across moves, the fold button, the
# second pane and each pane's history, and, on a copy, the Sign off button and the light shown
# while the repository has uncommitted changes. Optional, since it needs Playwright and its
# Chromium: with the browser missing it says so and passes, and map_viewer_test.py, which
# needs neither, still checks the pages themselves.
#
# Setting up, once per machine:
#   1. Install uv (https://docs.astral.sh/uv/). It installs Playwright itself on the first
#      run, at the version pinned above.
#   2. Download the Chromium that version drives, into ~/.cache/ms-playwright:
#        uv run --with playwright==1.65.0 playwright install chromium
#   3. On a Linux machine that has never run Chromium, add the system libraries it needs
#      (uses sudo):
#        uv run --with playwright==1.65.0 playwright install-deps chromium
# Then run ./browser_test.py from this directory. On moving the pin to a newer Playwright,
# repeat step 2 with the new version, as each drives its own Chromium build.

import importlib.util
import os
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

HERE = Path(__file__).resolve().parent


def main():
    from playwright.sync_api import Error, sync_playwright
    suite = load_suite()
    with tempfile.TemporaryDirectory() as scratch, sync_playwright() as playwright:
        demo = Path(scratch) / "demo"
        suite.build_demo(demo)
        base = suite.serve(demo)
        # Sign-offs write to the map, so they are tried on a copy served on its own.
        global COPY, SIGNING
        COPY = Path(scratch) / "copy"
        shutil.copytree(demo, COPY)
        SIGNING = suite.serve(COPY)
        try:
            browser = playwright.chromium.launch()
        except Error as error:
            print("skip browser checks: no Chromium for this Playwright; "
                  "install it with: uv run --with playwright==1.65.0 playwright install chromium")
            return
        failures = 0
        for check in [folds_survive_moves, tree_never_redrawn, approval_diff_swapped, fold_button,
                      second_pane, pane_history, signoff_button, uncommitted_light]:
            page = browser.new_page()
            page.set_default_timeout(5000)
            errors = []
            page.on("pageerror", lambda error: errors.append(str(error)))
            try:
                failures += check(page, base, suite)
            except Error as error:  # a step that never happened, such as a pane that never filled
                failures += suite.expect(check.__name__, False, " ".join(error.message.split()))
            failures += suite.expect(check.__name__, not errors, f"no script errors, saw {errors}")
            page.close()
        browser.close()
    if failures:
        print(f"{failures} check(s) failed")
        sys.exit(1)
    print("OK")


# map_viewer_test.py, for its demo, server and helpers.
def load_suite():
    spec = importlib.util.spec_from_file_location("map_viewer_test", HERE / "map_viewer_test.py")
    suite = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(suite)
    return suite


# --- Checks, each returning its number of failures ---

# A fold made in the tree survives following a tree link, a body link and browser back, with
# no page load; only the destination's branches open.
def folds_survive_moves(page, base, suite) -> int:
    page.goto(base + suite.node_path("map.md", "Demo"))
    mark_page(page)
    fold(page, "Approval States")
    fold(page, "Changes")
    tree_link(page, "Branch Leaf").click()
    wait_for_title(page, "Branch Leaf")
    failures = suite.expect("tree link", is_folded(page, "Approval States"), "a folded branch stays folded")
    tree_link(page, "Rendering").click()
    wait_for_title(page, "Rendering")
    page.locator("main a:text-is('Current')").click()
    wait_for_title(page, "Current")
    failures += suite.expect("body link", is_open(page, "Approval States"), "the destination's branch opens")
    failures += suite.expect("body link", is_folded(page, "Changes"), "other folds kept")
    page.go_back()
    wait_for_title(page, "Rendering")
    failures += suite.expect("browser back", is_folded(page, "Changes"), "folds kept going back")
    page.go_forward()
    wait_for_title(page, "Current")
    return failures + suite.expect("moves", same_page(page), "no page was loaded whole")


# Every linked map is in the tree from the start, so moving into one and back never redraws it.
def tree_never_redrawn(page, base, suite) -> int:
    page.goto(base + suite.node_path("map.md", "Demo"))
    page.evaluate("document.querySelector('aside').dataset.drawn = 'first'")
    page.locator("main a", has_text="further map").click()
    wait_for_title(page, "Linked Map")
    tree_link(page, "Demo").click()
    wait_for_title(page, "Demo")
    return suite.expect("linked map", page.evaluate("document.querySelector('aside').dataset.drawn") == "first",
                        "the tree is the one first drawn")


# A stale stamp's fingerprint link swaps in the approval diff, with no page load.
def approval_diff_swapped(page, base, suite) -> int:
    page.goto(base + suite.node_path("map.md", "Stale"))
    mark_page(page)
    page.locator("main .stale-row a").first.click()
    page.wait_for_selector("main .diff-head")
    return suite.expect("approval diff", same_page(page), "the diff swapped in, no page load")


# A branch's button folds everything below while any of it is open, and opens it all only once
# all is folded; its label says which it would do.
def fold_button(page, base, suite) -> int:
    page.goto(base + suite.node_path("map.md", "Demo"))
    button = branch(page, "Demo").locator(":scope > summary .below button")
    below = branch(page, "Demo").locator("details")
    failures = suite.expect("fold button", button.text_content() == "−", "− while anything is open")
    page.evaluate("[...document.querySelectorAll('aside details details')][0].open = false")
    button.click(force=True)
    failures += suite.expect("fold button", below.evaluate_all("ds => ds.every(d => !d.open)"),
                             "with one part folded, folds all below")
    failures += suite.expect("fold button", button.text_content() == "+", "+ once all is folded")
    button.click(force=True)
    return failures + suite.expect("fold button", below.evaluate_all("ds => ds.every(d => d.open)"),
                                   "with all folded, opens all below")


# Split opens a second pane; the node's links then load there, tree links on the left. The URL
# holds the pair, so reload keeps it; Swap and Close act on it.
def second_pane(page, base, suite) -> int:
    page.goto(base + suite.node_path("map.md", "Rendering"))
    page.locator("main button.split").click()
    page.wait_for_selector("#side .hint")
    page.locator("main a", has_text="Current").first.click()
    page.wait_for_selector("#side h1:has-text('Current')")
    failures = suite.expect("split", heading(page, "main") == "Rendering", "a node's link loads in the side pane")
    tree_link(page, "Stale").click()
    wait_for_title(page, "Stale")
    failures += suite.expect("split", heading(page, "#side") == "Current", "a tree link loads on the left")
    page.reload()
    failures += suite.expect("reload", (heading(page, "main"), heading(page, "#side")) == ("Stale", "Current"),
                             "both panes kept")
    page.locator("#side button.swap").click()
    page.wait_for_selector("main h1:has-text('Current')")
    failures += suite.expect("swap", heading(page, "#side") == "Stale", "the panes trade places")
    page.locator("#side button.close").click()
    page.wait_for_selector("#side", state="detached")
    return failures + suite.expect("close", "side=" not in page.url, "the side pane leaves the URL")


# Each pane steps through its own history with its ◀ ▶, disabled at either end, and a pane
# step is a browser step too.
def pane_history(page, base, suite) -> int:
    page.goto(base + suite.node_path("map.md", "Rendering"))
    page.locator("main button.split").click()
    page.wait_for_selector("#side .hint")
    page.locator("main a", has_text="Current").first.click()
    page.wait_for_selector("#side h1:has-text('Current')")
    page.locator("main a", has_text="Branch Leaf").first.click()
    page.wait_for_selector("#side h1:has-text('Branch Leaf')")
    back, forward = page.locator("#side button.back"), page.locator("#side button.forward")
    failures = suite.expect("pane steps", forward.is_disabled(), "▶ disabled at the newest")
    back.click()
    page.wait_for_selector("#side h1:has-text('Current')")
    failures += suite.expect("pane steps", back.is_disabled(), "◀ disabled at the first, the empty pane replaced")
    failures += suite.expect("pane steps", heading(page, "main") == "Rendering", "the left pane is untouched")
    forward.click()
    page.wait_for_selector("#side h1:has-text('Branch Leaf')")
    page.go_back()
    page.wait_for_selector("#side h1:has-text('Current')")
    failures += suite.expect("browser back", page.locator("#side button.forward").is_enabled(),
                             "browser back is a pane step, and the buttons agree")
    return failures + suite.expect("left steps", page.locator("main button.back").is_disabled(),
                                   "the left pane has nowhere to go back to")


# The Sign off button: the drop-down lists the map's handles, a name added there can be
# removed, pressing stamps the node for the names ticked, which are ticked again on the next
# node, and an approval diff has no button.
def signoff_button(page, base, suite) -> int:
    page.goto(SIGNING + suite.node_path("map.md", "Unstamped"))
    mark_page(page)
    box = page.locator("main .signoff")
    box.locator("summary").click()
    failures = suite.expect("names", names_listed(box) == ["alice", "bob", "carol: qa"], f"the map's handles, saw {names_listed(box)}")
    failures += suite.expect("names", box.locator("button.sign").is_disabled(), "Sign off disabled with none ticked")
    box.locator(".new-name").fill("dave")
    box.locator("button.add-name").click()
    failures += suite.expect("add", names_listed(box)[-1] == "dave" and box.locator("li", has_text="dave").locator(".remove").count() == 1,
                             "an added name listed, removable")
    failures += suite.expect("add", box.locator("li", has_text="bob").locator(".remove").count() == 0, "a map handle not removable")
    box.locator("li", has_text="dave").locator(".remove").click()
    failures += suite.expect("remove", "dave" not in names_listed(box), "a removed name gone")
    box.locator("li", has_text="alice").locator("input").check()
    box.locator("li", has_text="bob").locator("input").check()
    box.locator("button.sign").click()
    page.wait_for_selector("main .meta td:text-is('alice')")
    failures += suite.expect("sign off", page.locator("main .meta .ok").count() == 2, "both stamps shown current")
    failures += suite.expect("sign off", same_page(page), "the node redrawn in place, no page load")
    tree_link(page, "Mixed").click()
    wait_for_title(page, "Mixed")
    box = page.locator("main .signoff")
    ticked = box.locator("ul input:checked").evaluate_all("ts => ts.map(t => t.value)")
    failures += suite.expect("ticked again", ticked == ["alice", "bob"], f"the last names ticked, saw {ticked}")
    page.locator("main .stale-row a").first.click()
    page.wait_for_selector("main .diff-head")
    return failures + suite.expect("approval diff", page.locator("main .signoff").count() == 0, "no button on an approval diff")


# The red light shows, with its tooltip, while the repository has uncommitted changes, and is
# gone once they are committed.
def uncommitted_light(page, base, suite) -> int:
    page.goto(SIGNING + suite.node_path("map.md", "Demo"))
    light = page.locator("#uncommitted")
    failures = suite.expect("light", light.is_visible() and "uncommitted" in light.get_attribute("title"),
                            "shown with its tooltip while there are uncommitted changes")
    subprocess.run("git add -A && git -c user.name=demo -c user.email=demo@example.com commit -qm signed",
                   shell=True, cwd=COPY, check=True)
    page.reload()
    return failures + suite.expect("light", page.locator("#uncommitted").count() == 0, "gone once committed")


# --- Helpers ---

def names_listed(box) -> list[str]:
    return box.locator("ul input").evaluate_all("ts => ts.map(t => t.value)")


def mark_page(page) -> None:
    page.evaluate("window.loadedOnce = true")


def same_page(page) -> bool:
    return page.evaluate("window.loadedOnce === true")


def tree_link(page, name: str):
    return page.locator(f"aside a:text-is('{name}')").first


def branch(page, name: str):
    return page.locator("aside details", has=page.locator(f":scope > summary a:text-is('{name}')")).first


def fold(page, name: str) -> None:
    branch(page, name).evaluate("d => d.open = false")


def is_folded(page, name: str) -> bool:
    return not branch(page, name).evaluate("d => d.open")


def is_open(page, name: str) -> bool:
    return branch(page, name).evaluate("d => d.open")


def heading(page, pane: str) -> str:
    return page.locator(f"{pane} h1").first.text_content()


def wait_for_title(page, name: str) -> None:
    page.wait_for_selector(f"main h1:text-is('{name}')")


if __name__ == "__main__":
    if not os.environ.get("VIRTUAL_ENV"):
        print("No virtual environment detected. Run this script via './browser_test.py' (requires uv), or activate a virtual environment first.", file=sys.stderr)
        sys.exit(100)
    main()
