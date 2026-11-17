#!/usr/bin/env -S uv run --script --
# /// script
# requires-python = "==3.12.*"
# ///

# Serves the demo map that build_demo_map.py beside it builds and checks the viewer's pages
# against what each demo node says it shows, then, on a copy, that sign-offs are written and
# refused as they should be. Standard library only, and offline: the
# server runs in this process on a free port of 127.0.0.1.
#
# Setting up: install uv (https://docs.astral.sh/uv/) and git, then run ./map_viewer_test.py
# from this directory. The check that the page script parses also wants Node.js on the PATH
# (https://nodejs.org/, or a package manager's nodejs); without it that check is skipped.

import difflib
import html
import importlib.util
import json
import os
import re
import shutil
import subprocess
import sys
import tempfile
import threading
import urllib.error
import urllib.request
from datetime import date
from http.server import ThreadingHTTPServer
from pathlib import Path
from urllib.parse import quote, urlparse

HERE = Path(__file__).resolve().parent
VIEWER = HERE.parents[1] / "method" / "util" / "map_viewer.py"


def main():
    with tempfile.TemporaryDirectory() as scratch:
        demo = Path(scratch) / "demo"
        build_demo(demo)
        base = serve(demo)
        # Sign-offs write to the map, so they are checked on a copy served on its own.
        copy = Path(scratch) / "copy"
        shutil.copytree(demo, copy)
        signing = serve(copy)
        failures = sum(check() for check in [
            lambda: root_redirects_to_demo(base),
            lambda: stamps_show_their_state(base),
            lambda: stale_stamp_links_to_its_diff(base),
            lambda: diff_shows_changed_words(base),
            lambda: renamed_node_found_by_id(base),
            lambda: uncommitted_approval_explained(base),
            lambda: contents_never_due(base),
            lambda: tree_crosses_files(base),
            lambda: markdown_rendered(base),
            lambda: bad_requests_answered(base),
            lambda: pages_swappable(base),
            lambda: side_pane_served(base),
            lambda: script_parses(base),
            lambda: signoff_writes_stamps(signing, copy),
            lambda: signoff_refusals(signing, copy),
            lambda: foreign_host_refused(base),
        ])
    if failures:
        print(f"{failures} check(s) failed")
        sys.exit(1)
    print("OK")


def build_demo(demo: Path) -> None:
    subprocess.run(f"{sys.executable} {HERE / 'build_demo_map.py'} {demo}", shell=True, check=True,
                   capture_output=True)


# The viewer, loaded as a module and serving the demo from a background thread.
def serve(demo: Path) -> str:
    spec = importlib.util.spec_from_file_location("map_viewer", VIEWER)
    viewer = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(viewer)
    viewer.ROOT, viewer.ENTRY = demo.resolve(), "map.md"
    server = ThreadingHTTPServer(("127.0.0.1", 0), viewer.Handler)
    threading.Thread(target=server.serve_forever, daemon=True).start()
    return f"http://127.0.0.1:{server.server_address[1]}"


# --- Checks, each returning its number of failures ---

def root_redirects_to_demo(base: str) -> int:
    with urllib.request.urlopen(base + "/") as response:
        return expect("root", response.url.endswith(node_path("map.md", "Demo")), "/ should open the root node, Demo")


def stamps_show_their_state(base: str) -> int:
    return (expect("Current", page(base, "Current").count("class=ok>current") == 2, "alice and bob both current")
            + expect("Stale", "class=stale>stale" in page(base, "Stale"), "alice's stamp stale")
            + expect("Mixed", "class=ok>current" in (mixed := page(base, "Mixed")) and "class=stale>stale" in mixed,
                     "one stamp current, one stale")
            + expect("Unstamped", "No stamps" in page(base, "Unstamped"), "no stamps listed")
            + expect("Quoted Handle", "carol: qa" in page(base, "Quoted Handle"), "the quoted handle shown"))


def stale_stamp_links_to_its_diff(base: str) -> int:
    return expect("Stale", f'href="{approval_path("Stale", "alice")}"' in page(base, "Stale"),
                  "the stale fingerprint links to its approval diff")


def diff_shows_changed_words(base: str) -> int:
    diff = fetch(base + approval_path("Edited", "alice"))
    return (expect("Edited diff", "<del>removed.</del><ins>removed; now they are highlighted where added too.</ins>" in diff,
                   "the changed words marked")
            + expect("Edited diff", "<ins>This paragraph is new." in diff, "the new paragraph marked")
            + expect("Edited diff", "not yet committed" in diff, "the current text reported as uncommitted"))


def renamed_node_found_by_id(base: str) -> int:
    diff = fetch(base + approval_path("Renamed", "alice"))
    return expect("Renamed diff", "<del>Old Name</del><ins>Renamed</ins>" in diff,
                  "the old heading found by id and shown as replaced")


def uncommitted_approval_explained(base: str) -> int:
    diff = fetch(base + approval_path("Lost Approval", "bob"))
    return expect("Lost Approval diff", "isn't in this file's git history" in diff, "nothing to compare, said so")


def contents_never_due(base: str) -> int:
    return expect("Contents", "never stamped and never due" in page(base, "Contents"), "Contents is never due")


def tree_crosses_files(base: str) -> int:
    leaf = page(base, "Branch Leaf", "branch.map.md")
    return (expect("Branch Leaf", '<span class="branch-file">branch.map.md</span>' in leaf, "the branch file tagged")
            + expect("Branch Leaf", 'class="here">Branch Leaf</a>' in leaf, "the current node marked in the tree")
            + expect("Demo", '<span class="branch-file">linked.map.md</span>' in page(base, "Demo"),
                     "a map linked only in prose drawn as its own tree")
            + expect("tree", without_mark(leaf) == without_mark(page(base, "Demo")), "the same tree on every page"))


def markdown_rendered(base: str) -> int:
    rendering = page(base, "Rendering")
    expected = {
        "italics and bold": "<em>italics</em> and <strong>bold</strong>",
        "inline code": "<code>inline code</code>",
        "a link to another node": f'<a href="{node_path("map.md", "Current")}">Current</a>',
        "a nested list inside its item": "<li>A nested bullet\n<ol><li>A numbered item, nested deeper</li>",
        "a numbered list keeping its start": "<ol start=3><li>A numbered list starting at three</li>",
        "heading levels": "<h2>A Heading</h2>",
        "a smaller heading": "<h3>A Smaller Heading</h3>",
        "a blockquote": "<blockquote><p>A blockquote.</p></blockquote>",
        "an alert": '<div class="alert alert-important"><p class="alert-title">Important</p>',
        "a table": "<tr><td>one</td><td>1</td></tr>",
        "a fence quoting a shorter one": "<pre><code>```python\n",
    }
    return sum(expect("Rendering", html in rendering, what) for what, html in expected.items())


def bad_requests_answered(base: str) -> int:
    return (expect("unknown node", status(base + node_path("map.md", "No Such Node")) == 404, "404")
            + expect("outside the map", status(base + node_path("../outside.md", "X")) == 403, "403"))


# The page script moves between nodes by swapping one page's <main> and <aside> into the
# other, so every page must have exactly one of each.
def pages_swappable(base: str) -> int:
    pages = [page(base, "Demo"), page(base, "Branch Leaf", "branch.map.md"), fetch(base + approval_path("Edited", "alice"))]
    return sum(expect("page shape", p.count("<main>") == 1 and p.count("<aside>") == 1, "one <main> and one <aside>")
               for p in pages)


# A split page carries a second pane, named by its side parameter: a node, or, when empty,
# a note on how to fill it.
def side_pane_served(base: str) -> int:
    split = fetch(base + node_path("map.md", "Rendering") + "&side=" + quote(node_path("map.md", "Current")))
    empty = fetch(base + node_path("map.md", "Rendering") + "&side=")
    side_of = lambda html: html[html.index('<section id="side">'):] if '<section id="side">' in html else ""
    return (expect("split page", "<h1>Current</h1>" in side_of(split) and "<h1>Rendering</h1>" in split,
                   "both nodes shown, Current in the side pane")
            + expect("split page", "Links followed in the node on the left open here" in side_of(empty),
                     "an empty side pane says how to fill it")
            + expect("split page", status(base + node_path("map.md", "Rendering") + "&side=" + quote("/elsewhere")) == 404,
                     "a side pane naming no view answered 404")
            + expect("unsplit page", '<section id="side">' not in page(base, "Rendering"), "no side pane"))


# The page script, as served, parses as JavaScript. Checked with node when it is installed,
# and skipped otherwise, so the suite still runs on the standard library alone.
def script_parses(base: str) -> int:
    if not shutil.which("node"):
        print("skip script parses: node not installed")
        return 0
    served = page(base, "Demo")
    script = served[served.index("<script>") + len("<script>"):served.index("</script>")]
    with tempfile.NamedTemporaryFile("w", suffix=".js", delete=False) as js:
        js.write(script)
    try:
        checked = subprocess.run(["node", "--check", js.name], capture_output=True, text=True)
    finally:
        os.unlink(js.name)
    return expect("page script", checked.returncode == 0, f"parses as JavaScript: {checked.stderr.strip()}")


# A sign-off writes one stamp per name under the node's approvals: key, adding the key if
# absent, replacing that name's earlier stamp, quoting a handle with a colon, and nothing else.
def signoff_writes_stamps(base: str, copy: Path) -> int:
    today = date.today().isoformat()
    before = (copy / "map.md").read_text(encoding="utf-8")
    code_new = sign(base, "Unstamped", ["dave", "eve: ops"])
    code_again = sign(base, "Stale", ["alice"])
    after = (copy / "map.md").read_text(encoding="utf-8")
    unstamped, stale = page(base, "Unstamped"), page(base, "Stale")
    fingerprint = signoff_data(unstamped)["fingerprint"]
    changed = [line for line in difflib.ndiff(before.splitlines(), after.splitlines()) if line[:2] in ("- ", "+ ")]
    return (expect("sign-off", (code_new, code_again) == (200, 200), f"accepted, got {code_new}, {code_again}")
            + expect("sign-off", f"approvals:\n  dave: {{at: {today}, hash: {fingerprint}}}\n"
                     f'  "eve: ops": {{at: {today}, hash: {fingerprint}}}\n```' in after,
                     "a stamp per name, under an approvals: key added for them, the colon quoted")
            + expect("sign-off", unstamped.count("class=ok>current") == 2, "both new stamps shown current")
            + expect("sign-off", "class=stale>stale" not in stale and stale.count("<td>alice</td>") == 1,
                     "alice's stale stamp replaced, not added beside")
            + expect("sign-off", len(changed) == 5, f"only the stamp lines and the key changed, saw {changed}"))


# Each refusal leaves the file untouched: a node changed since its page was shown, a
# missing or wrong token, anything but POST, or a foreign Host or Origin.
def signoff_refusals(base: str, copy: Path) -> int:
    before = (copy / "map.md").read_text(encoding="utf-8")
    data = signoff_data(page(base, "Current"))
    host = urlparse(base).netloc
    cases = {
        "a node changed since its page was shown": (sign(base, "Current", ["dave"], fingerprint="00000000"), 409),
        "no token": (sign(base, "Current", ["dave"], token=""), 403),
        "a wrong token": (sign(base, "Current", ["dave"], token=data["token"][:-1] + "x"), 403),
        "a GET": (status(base + "/signoff"), 405),
        "a PUT": (send(base, "PUT", signoff_body(base, "Current", ["dave"]), {}), 501),
        "a foreign Origin": (sign(base, "Current", ["dave"], headers={"Origin": "http://evil.example"}), 403),
        "no Origin": (sign(base, "Current", ["dave"], headers={"Origin": None}), 403),
        "a foreign Host": (sign(base, "Current", ["dave"], headers={"Host": f"evil.example:{host.split(':')[1]}"}), 403),
        "an Origin not matching its Host": (sign(base, "Current", ["dave"], headers={"Origin": "http://localhost:1"}), 403),
    }
    failures = sum(expect("refused sign-off", got == want, f"{what}: {want}, got {got}") for what, (got, want) in cases.items())
    return failures + expect("refused sign-off", (copy / "map.md").read_text(encoding="utf-8") == before,
                             "the file untouched")


# A page reached through a name rebound to 127.0.0.1 can't read the map either, while
# localhost and another local port, as a port forward gives, are served.
def foreign_host_refused(base: str) -> int:
    read = lambda host: code_of(urllib.request.Request(base + node_path("map.md", "Demo"), headers={"Host": host}))
    return (expect("foreign Host", read("evil.example") == 403, "a page read under another host refused")
            + expect("foreign Host", read("127.0.0.1.evil.example:80") == 403, "a name merely starting 127.0.0.1 refused")
            + expect("local Host", (read("localhost:9000"), read("127.0.0.1:9000")) == (200, 200),
                     "localhost and another local port served"))


# --- Helpers ---

# The sign-off box's data: the file, node, rendered fingerprint, the run's token and handles.
def signoff_data(html_page: str) -> dict:
    box = re.search(r'<details class="signoff" ([^>]*)>', html_page).group(1)
    return {k: html.unescape(v) for k, v in re.findall(r'data-(\w+)="([^"]*)"', box)}


def signoff_body(base: str, name: str, names: list, **overrides) -> dict:
    data = signoff_data(page(base, name))
    body = {"token": data["token"], "file": data["file"], "name": data["name"],
            "fingerprint": data["fingerprint"], "names": names}
    return body | overrides


# Sends a sign-off as the viewer's own page would, with any headers overridden (None drops one).
def sign(base: str, name: str, names: list, headers: dict | None = None, **overrides) -> int:
    body = signoff_body(base, name, names, **overrides)
    return send(base, "POST", body, {"Origin": base} | (headers or {}))


def send(base: str, method: str, body: dict, headers: dict) -> int:
    request = urllib.request.Request(base + "/signoff", data=json.dumps(body).encode("utf-8"), method=method,
                                     headers={"Content-Type": "application/json"})
    for key, value in headers.items():
        if value is not None:
            request.add_header(key, value)
    return code_of(request)


def code_of(request) -> int:
    try:
        with urllib.request.urlopen(request) as response:
            return response.status
    except urllib.error.HTTPError as error:
        return error.code


def page(base: str, name: str, file: str = "map.md") -> str:
    return fetch(base + node_path(file, name))


def without_mark(html: str) -> str:
    return html[html.index("<aside>"):html.index("</aside>")].replace(' class="here"', "")


def fetch(url: str) -> str:
    with urllib.request.urlopen(url) as response:
        return response.read().decode("utf-8")


def status(url: str) -> int:
    try:
        with urllib.request.urlopen(url) as response:
            return response.status
    except urllib.error.HTTPError as error:
        return error.code


def node_path(file: str, name: str) -> str:
    return f"/node?file={quote(file)}&name={quote(name)}"


def approval_path(name: str, who: str) -> str:
    return f"/approval?file=map.md&name={quote(name)}&who={quote(who)}"


def expect(where: str, condition: bool, what: str) -> int:
    if condition:
        return 0
    print(f"FAIL {where}: {what}")
    return 1


if __name__ == "__main__":
    if not os.environ.get("VIRTUAL_ENV"):
        print("No virtual environment detected. Run this script via './map_viewer_test.py' (requires uv), or activate a virtual environment first.", file=sys.stderr)
        sys.exit(100)
    try:
        main()
    except (KeyboardInterrupt, EOFError):
        print()
        sys.exit(130)
