#!/usr/bin/env -S uv run --script --
# /// script
# requires-python = "==3.12.*"
# ///

# Map viewer, a proof of concept, self-contained: serves a map in the browser so it can be read
# node by node, with who has approved each node and, for a stale approval, what has changed since
# it. It only reads: approvals and edits are made through the agent in the same ssh
# session. Listens on 127.0.0.1 only, since there is no login; reach it from elsewhere
# by port forwarding (e.g. ssh -L 8080:127.0.0.1:8080 host).
#
# Shipped with the method, so in a project NDD is installed in, from the project root:
#
#   ndd/method/util/map_viewer.py                 # the map.md in the current directory
#   ndd/method/util/map_viewer.py path/to/map.md  # a given map
#   ndd/method/util/map_viewer.py --port 9000
#
# It needs uv (https://docs.astral.sh/uv/), which fetches Python 3.12 if it is missing,
# and git for what changed since an approval. In the NDD repository, it is method/util/map_viewer.py.

import argparse
import difflib
import hashlib
import html
import os
import re
import shlex
import subprocess
import sys
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from urllib.parse import parse_qs, quote, urlparse

VERSION = "0.3.0"

GREEN, YELLOW, RED = "32", "33", "31"  # ANSI colour codes

FENCE = re.compile(r"^```")
LINK_ONLY_LINE = re.compile(r"^\[[^\]]+\]\([^)]+\)\s*\\?\s*$")
# A stamp key may hold spaces; one with a colon or leading punctuation is quoted.
STAMP = re.compile(r"^\s+(?:\"([^\"]+)\"|'([^']+)'|([^\s\"'][^:]*?))\s*:\s*\{.*?\bhash:\s*([0-9a-f]{8})\b")


def main():
    args = parse_args()
    entry = find_map(Path(args.map))
    global ROOT, ENTRY
    ROOT, ENTRY = entry.parent, entry.name
    server = ThreadingHTTPServer(("127.0.0.1", args.port), Handler)
    print(f"Serving {entry}")
    success(f"Open http://127.0.0.1:{args.port}/ (forward the port to view it from another machine)")
    server.serve_forever()


# The map being served: its directory, which bounds every file read, and its entry file.
ROOT: Path
ENTRY: str


class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.answer(self.get)

    # A bad request gets an error page rather than a dropped connection.
    def answer(self, handle) -> None:
        try:
            handle()
        except PermissionError:
            self.send_error(403, "Outside the map's directory")
        except (KeyError, FileNotFoundError):
            self.send_error(404, "No such map file or node")

    def get(self):
        url = urlparse(self.path)
        query = {k: v[0] for k, v in parse_qs(url.query, keep_blank_values=True).items()}
        if url.path == "/":
            self.redirect(node_url(ENTRY, root_node(read_map(ENTRY))))
        elif url.path in ("/node", "/approval"):
            title, body = view(url.path, query)
            side = side_pane(query["side"]) if "side" in query else None
            self.send_page(page(title, body, tree_html((query["file"], query["name"])), side))
        else:
            self.send_error(404)

    def send_page(self, body: str) -> None:
        data = body.encode("utf-8")
        self.send_response(200)
        self.send_header("Content-Type", "text/html; charset=utf-8")
        self.send_header("Content-Length", str(len(data)))
        self.end_headers()
        self.wfile.write(data)

    def redirect(self, location: str) -> None:
        self.send_response(303)
        self.send_header("Location", location)
        self.end_headers()

    def log_message(self, format, *args):
        pass  # quiet: a line per request would bury anything worth reading


# --- Pages ---

# A page's title and content: a node, or what changed in it since someone approved it.
def view(path: str, query: dict[str, str]) -> tuple[str, str]:
    lines = read_map(query["file"])
    if path == "/node":
        return node_view(query["file"], query["name"], lines)
    at, hash_ = stamp_details(node_lines(lines, query["name"]))[query["who"]]
    history = node_history(query["file"], query["name"])
    return approval_view(query["file"], query["name"], query["who"], at, hash_, lines, history)


# The second pane: the view its link names, such as /node?file=…&name=…, or, when it names
# none yet, a note on how to fill it.
def side_pane(target: str) -> str:
    if not target:
        return "<p class=hint>Links followed in the node on the left open here.</p>"
    url = urlparse(target)
    if url.path not in ("/node", "/approval"):
        raise KeyError(target)
    return view(url.path, {k: v[0] for k, v in parse_qs(url.query).items()})[1]


def node_view(file: str, name: str, lines: list[str]) -> tuple[str, str]:
    node = node_lines(lines, name)
    current = fingerprint(node)
    body = render_markdown(strip_scaffolding(node[1:]), file)
    return name, f"""
<h1>{html.escape(name)}</h1>
{body}
<section class="meta">
<p>Current fingerprint <code>{current}</code></p>
{approvals_html(file, name, lines, current)}
</section>"""


# Who has approved the node, and whether the text has changed since. Contents is a tree
# overview kept in step with the navigation links, so it is never stamped or due.
def approvals_html(file: str, name: str, lines: list[str], current: str) -> str:
    if name == "Contents":
        return "<p>Contents is a tree overview of the navigation links, so it is never stamped and never due.</p>"
    rows = "".join(approval_row(file, name, who, at, hash_, current)
                   for who, (at, hash_) in stamp_details(node_lines(lines, name)).items())
    return f"""<table><tr><th>Approver</th><th>At</th><th>Approved fingerprint</th><th>Status</th></tr>{rows or '<tr><td colspan=4>No stamps</td></tr>'}</table>"""


# A stale approval's row is tinted, and its fingerprint links to what changed since.
def approval_row(file: str, name: str, who: str, at: str, hash_: str, current: str) -> str:
    if hash_ == current:
        return f"<tr><td>{html.escape(who)}</td><td>{html.escape(at)}</td><td><code>{hash_}</code></td><td class=ok>current</td></tr>"
    diff = f"/approval?file={quote(file)}&name={quote(name)}&who={quote(who)}"
    return (f'<tr class=stale-row><td>{html.escape(who)}</td><td>{html.escape(at)}</td>'
            f'<td><a href="{diff}" title="What changed since"><code>{hash_}</code></a></td><td class=stale>stale</td></tr>')


# What changed since someone approved a node: the details of both versions, the changed
# passages, the whole node as it stands with the same highlights, then the approvals.
def approval_view(file: str, name: str, who: str, at: str, hash_: str, lines: list[str],
                  history: list[tuple[str, str, list[str] | None]]) -> tuple[str, str]:
    now = node_lines(lines, name)
    current = fingerprint(now)
    approved = introduced(history, hash_)
    # The current text counts as committed only if the newest commit holds it.
    committed_now = bool(history) and history[0][2] is not None and fingerprint(history[0][2]) == current
    present = introduced(history, current) if committed_now else None
    # A stamp records no commit: each version's is the first commit holding that text.
    approved_commit, approved_date = (f"<code>{approved[0]}</code>", approved[1]) if approved else ("not in this file's git history", "—")
    current_commit, current_date = (f"<code>{present[0]}</code>", present[1]) if present else ("not yet committed", "—")
    # No page title: it opens with two tables, what is being compared on the left and the
    # two versions' details on the right.
    head = f"""<header class="diff-head">
<table class="about"><tr><th colspan="2">Approval Diff</th></tr>
<tr><th>Node</th><td><a href="{node_url(file, name)}">{html.escape(name)}</a></td></tr>
<tr><th>Approver</th><td>{html.escape(who)}</td></tr>
<tr><th>File</th><td>{html.escape(file)}</td></tr>
</table>
<table class="compare"><tr><th></th><th class="was">Approved</th><th class="now">Current</th></tr>
<tr><th>Fingerprint</th><td class="was"><code>{hash_}</code></td><td class="now"><code>{current}</code></td></tr>
<tr><th>Stamp date</th><td class="was">{html.escape(at)}</td><td class="now">—</td></tr>
<tr><th>First committed</th><td class="was">{approved_commit}</td><td class="now">{current_commit}</td></tr>
<tr><th class="sub">on</th><td class="was">{approved_date}</td><td class="now">{current_date}</td></tr>
</table></header>"""
    if approved is None:
        diff = "<p>The approved text isn't in this file's git history, so there is nothing to compare against.</p>"
    else:
        old = approved[2]
        delta = changed_passages([old[0]] + strip_scaffolding(old[1:]), [now[0]] + strip_scaffolding(now[1:]))
        diff = f'{delta}<h3 class="section">Current Node</h3><pre class=diff>{word_diff("".join(old), "".join(now))}</pre>'
    footer = f'<section class="meta">{approvals_html(file, name, lines, current)}</section>'
    return f"Approval Diff: {name}", head + diff + footer


# The commit where a version of the node was introduced: in the newest run of commits
# holding text with this fingerprint, the oldest. Returns (commit, date, node lines) or None.
def introduced(history: list[tuple[str, str, list[str] | None]], hash_: str) -> tuple[str, str, list[str]] | None:
    found = None
    for commit, date, node in history:
        if node is not None and fingerprint(node) == hash_:
            found = (commit, date, node)
        elif found:
            break
    return found


# Only the lines that differ, each run word-diffed, with a line of context either side.
def changed_passages(old: list[str], new: list[str]) -> str:
    runs = []
    for op, i1, i2, j1, j2 in difflib.SequenceMatcher(None, old, new, autojunk=False).get_opcodes():
        if op == "equal":
            continue
        before = html.escape(old[i1 - 1].rstrip()) if i1 > 0 else ""
        after = html.escape(new[j2].rstrip()) if j2 < len(new) else ""
        body = word_diff("".join(old[i1:i2]), "".join(new[j1:j2]))
        runs.append(f'<pre class=diff><span class=context>{before}</span>\n{body}<span class=context>{after}</span></pre>')
    return "".join(runs) or "<p>No difference in the approved text.</p>"


# A pane's back and forward buttons; the page script enables them as its history allows.
def steps(pane: str) -> str:
    return (f'<button class="back" data-pane="{pane}" title="Back in this pane" disabled>◀</button>'
            f'<button class="forward" data-pane="{pane}" title="Forward in this pane" disabled>▶</button>')


# The tree, the node, and, once the page is split, a second pane beside it.
def page(title: str, body: str, sidebar: str, side: str | None = None) -> str:
    split = side is not None
    tools = (f'<div class="pane-tools">{steps("left")}'
             '<button class="split" title="Open a second pane for the links this node holds">Split</button></div>')
    side_html = (f'<section id="side"><div class="pane-tools">{steps("side")}'
                 '<button class="swap" title="Swap the two panes">⇄ Swap</button>'
                 f'<button class="close" title="Close this pane">× Close</button></div>{side}</section>') if split else ""
    return (f'<!doctype html><html><head><meta charset="utf-8"><title>{html.escape(title)}</title>'
            f'<style>{STYLE}</style></head><body{" class=split" if split else ""}><aside>{sidebar}</aside>'
            f"<main>{tools}{body}</main>{side_html}<script>{SCRIPT}</script></body></html>")


STYLE = r"""
body { font-family: system-ui, sans-serif; margin: 0; line-height: 1.5; display: flex; }
main { max-width: 52rem; padding: 2rem 1.5rem; flex: 1; min-width: 0; }
pre { background: #f4f4f4; padding: .75rem; overflow-x: auto; white-space: pre-wrap; }
table { border-collapse: collapse; }
td, th { border: 1px solid #ccc; padding: .2rem .5rem; text-align: left; }
blockquote { margin: 1rem 0; padding: 0 1rem; border-left: 4px solid #ddd; color: #555; }
.alert { margin: 1rem 0; padding: .1rem 1rem; border-left: 4px solid; }
.alert-title { font-weight: 600; margin: .5rem 0 0; }
.alert-note { border-color: #4078c0; } .alert-note .alert-title { color: #4078c0; }
.alert-tip { border-color: #2a8a3a; } .alert-tip .alert-title { color: #2a8a3a; }
.alert-important { border-color: #8250df; } .alert-important .alert-title { color: #8250df; }
.alert-warning { border-color: #b8860b; } .alert-warning .alert-title { color: #b8860b; }
.alert-caution { border-color: #c03030; } .alert-caution .alert-title { color: #c03030; }

/* The tree */
aside { width: 18rem; flex: none; height: 100vh; overflow-y: auto; position: sticky; top: 0; box-sizing: border-box;
        border-right: 1px solid #ddd; font-size: .85rem; padding: 1rem .5rem; }
aside ul { list-style: none; padding-left: .9rem; margin: 0; }
aside > ul { padding-left: 0; margin-bottom: .6rem; }
aside a { text-decoration: none; }
aside a.here { font-weight: bold; background: #e3ecff; border-radius: 3px; padding: 0 .25rem; }
aside summary { list-style: none; cursor: pointer; }
aside summary::-webkit-details-marker { display: none; }
aside summary::before, aside li.leaf::before { display: inline-block; width: 1em; color: #999; }
aside summary::before { content: "▸"; }
aside details[open] > summary::before { content: "▾"; }
aside li.leaf::before { content: ""; }
aside li.branch { position: relative; border-radius: 4px; padding: .1rem 0; }
aside .branch-file { display: none; position: absolute; top: 0; right: .3rem; font-size: .7rem; color: #888; }
aside li.branch:hover > .branch-file { display: block; }
aside .below { visibility: hidden; margin-left: .3rem; }
aside summary:hover .below { visibility: visible; }
aside .below button { font-size: .7rem; line-height: 1; padding: 0 .3rem; border: 1px solid #ccc; background: #fff;
                      border-radius: 3px; cursor: pointer; }

/* The second pane, scrolled on its own beside the node */
#side { flex: 1; min-width: 0; max-width: 52rem; box-sizing: border-box; padding: 2rem 1.5rem; height: 100vh;
        overflow-y: auto; position: sticky; top: 0; border-left: 1px solid #ddd; background: #fcfcfc; }
.pane-tools { float: right; display: flex; gap: .3rem; margin-left: 1rem; }
.pane-tools button { font-size: .75rem; padding: .1rem .5rem; border: 1px solid #ccc; background: #fff;
                     border-radius: 3px; cursor: pointer; color: #555; }
body.split main .split { display: none; }
.pane-tools button:disabled { opacity: .35; cursor: default; }
.hint { color: #888; font-style: italic; }

/* Footer: fingerprint and approvals */
.meta { border-top: 1px solid #ccc; margin-top: 2rem; padding-top: 1rem; color: #888; font-size: .9rem; }
.meta a { color: #779; }
.ok { color: green; }
.stale { color: #b8860b; }
.stale-row { background: #fff1e0; }

/* Approval diff */
del { background: #fdd; }
ins { background: #dfd; text-decoration: none; }
.context { color: #999; }
.section { font-size: .85rem; color: #666; margin: 1.5rem 0 .3rem; }
.diff-head { font-size: .85rem; display: flex; justify-content: space-between; gap: 2rem; align-items: flex-start;
             flex-wrap: wrap; border: 1px solid #ddd; border-radius: 4px; padding: .8rem 1rem; background: #fafafa; }
.about th, .about td, .compare th, .compare td { border: none; padding: .1rem .5rem; text-align: left; }
.about th, .compare th { color: #888; font-weight: normal; }
.about td { font-weight: 600; }
.about tr:first-child th, .compare tr:first-child th.was, .compare tr:first-child th.now { color: #555; font-weight: bold; }
.compare th.sub { padding-left: 1.2rem; }
.compare .was { background: #fff1e0; }
.compare .now { background: #e9f6e9; }
"""

SCRIPT = r"""
// A branch's button folds it and everything below it when any of that is open, and opens it all
// only once all of it is folded.
function toggleAll(event) {
  event.preventDefault();
  event.stopPropagation();
  const branch = branchOf(event.target.closest("details"));
  const open = !branch.some(d => d.open);
  branch.forEach(d => d.open = open);
}
function branchOf(details) {
  return [details, ...details.querySelectorAll("details")];
}
// Each button shows what it would do, kept up to date however the tree was opened or folded.
function labelButtons() {
  document.querySelectorAll("aside details").forEach(d => {
    const button = d.querySelector(":scope > summary .below button");
    const anyOpen = branchOf(d).some(x => x.open);
    button.textContent = anyOpen ? "−" : "+";
    button.title = anyOpen ? "Fold this and everything below" : "Open this and everything below";
  });
}
function bindTree() {
  document.querySelectorAll("aside details").forEach(d => d.addEventListener("toggle", labelButtons));
  labelButtons();
}

// Moving between pages swaps only the page content, so the tree keeps whatever was folded.
// The destination's branches are opened, and nothing else. The URL holds the node on the
// left and, once split, the side pane's link as its side parameter, empty until one is followed.
function panes(url) {
  const u = new URL(url, location.href);
  const side = u.searchParams.get("side");
  u.searchParams.delete("side");
  return {left: u.pathname + u.search, side};
}

function urlOf(left, side) {
  const u = new URL(left, location.href);
  if (side !== null) u.searchParams.set("side", side);
  return u;
}

// Each pane's history, a list of the views it has shown and where it is in that list, kept
// in the browser's history entry so pane steps, browser steps and reloads agree.
let state = history.state || {left: start(panes(location.href).left),
                               side: panes(location.href).side === null ? null : start(panes(location.href).side)};
history.replaceState(state, "");

function start(url) { return {stack: [url], at: 0}; }

// A pane's history after it moves to url: anything forward of here is dropped. An empty
// side pane's place is taken by the first link followed into it.
function moved(pane, url) {
  if (!pane) return start(url);
  const stack = pane.stack.slice(0, pane.at + 1);
  if (stack[pane.at] === "") stack[pane.at] = url; else stack.push(url);
  return {stack, at: stack.length - 1};
}

function stepped(pane, by) {
  return {stack: pane.stack, at: pane.at + by};
}

function urlFor(next) {
  return urlOf(next.left.stack[next.left.at], next.side ? next.side.stack[next.side.at] : null);
}

function go(next, changed) {
  show(urlFor(next), changed, next);
}

// Tree links load on the left. Links in the side pane load there, and so do the node's own
// links once the page is split.
document.addEventListener("click", event => {
  if (event.defaultPrevented || event.button !== 0 || event.metaKey || event.ctrlKey || event.shiftKey || event.altKey) return;
  const button = event.target.closest("button");
  if (button?.matches(".split")) return go({left: state.left, side: start("")}, "side");
  if (button?.matches(".close")) return go({left: state.left, side: null}, "side");
  if (button?.matches(".swap") && state.side && state.side.stack[state.side.at])
    return go({left: state.side, side: state.left}, "both");
  if (button?.matches(".back, .forward")) {
    const pane = button.dataset.pane, by = button.matches(".back") ? -1 : 1;
    return go({...state, [pane]: stepped(state[pane], by)}, pane);
  }
  const link = event.target.closest("a[href]");
  if (!link) return;
  const url = new URL(link.href, location.href);
  if (url.origin !== location.origin || !["/node", "/approval"].includes(url.pathname)) return;
  event.preventDefault();
  const target = url.pathname + url.search;
  const inSide = link.closest("#side") || (link.closest("main") && state.side);
  if (inSide) go({...state, side: moved(state.side, target)}, "side");
  else go({...state, left: moved(state.left, target)}, "left");
});
window.addEventListener("popstate", event => {
  show(new URL(location.href), "both", event.state || state, false);
});

async function show(url, changed, next, addToHistory = true) {
  let response;
  try {
    response = await fetch(url);
  } catch {
    location.href = url;  // let the browser report it
    return;
  }
  if (!response.ok) {
    location.href = url;  // the server's error page, loaded whole
    return;
  }
  const page = new DOMParser().parseFromString(await response.text(), "text/html");
  state = next;
  if (addToHistory) history.pushState(state, "", url);
  document.title = page.title;
  document.body.className = page.body.className;
  if (changed !== "side") {
    document.querySelector("main").replaceWith(page.querySelector("main"));
    window.scrollTo(0, 0);
    updateTree(page.querySelector("aside"));
  }
  if (changed !== "left") showSide(page.querySelector("#side"));
  enableSteps();
}

function enableSteps() {
  document.querySelectorAll("button.back, button.forward").forEach(button => {
    const pane = state[button.dataset.pane];
    button.disabled = !pane || (button.matches(".back") ? pane.at === 0 : pane.at === pane.stack.length - 1);
  });
}

function showSide(nextSide) {
  const side = document.querySelector("#side");
  if (side && nextSide) side.replaceWith(nextSide);
  else if (nextSide) document.querySelector("main").after(nextSide);
  else side?.remove();
}

// The tree is redrawn only if the map's shape changed; otherwise the current node's mark moves
// and its branches open.
function updateTree(nextAside) {
  const aside = document.querySelector("aside");
  if (!aside || !nextAside) return;
  if (treeShape(aside) !== treeShape(nextAside)) {
    aside.replaceWith(nextAside);
    bindTree();
  } else {
    const href = nextAside.querySelector("a.here")?.getAttribute("href");
    aside.querySelectorAll("a.here").forEach(a => a.classList.remove("here"));
    const here = href && [...aside.querySelectorAll("a")].find(a => a.getAttribute("href") === href);
    if (here) {
      here.classList.add("here");
      for (let d = here.parentElement.closest("details"); d; d = d.parentElement.closest("details")) {
        if (here.closest("summary")?.parentElement !== d) d.open = true;
      }
    }
  }
  document.querySelector("aside a.here")?.scrollIntoView({block: "nearest"});
}

// The tree's links in order, with their nesting, ignoring which is marked current or folded.
function treeShape(aside) {
  return [...aside.querySelectorAll("a")].map(a => {
    let depth = 0;
    for (let li = a.closest("li"); li; li = li.parentElement.closest("li")) depth++;
    return depth + " " + a.getAttribute("href");
  }).join("\n");
}

bindTree();
enableSteps();
document.querySelector("aside a.here")?.scrollIntoView({block: "center"});
"""


# --- The map ---

# Node names in file order.
def nodes_of(lines: list[str]) -> list[str]:
    return list(node_index(lines))


def node_lines(lines: list[str], name: str) -> list[str]:
    start, end = node_index(lines)[name]
    return lines[start:end]


# Each node's line range, by name, in file order. A file read through read_map is indexed
# once and kept with its text, so drawing the tree doesn't rescan it per lookup; other
# text, such as an old version from git, is indexed afresh.
def node_index(lines: list[str]) -> dict[str, tuple[int, int]]:
    cached = _index_cache.get(id(lines))
    if cached and cached[0] is lines:
        return cached[1]
    return index_of(lines)


# The first node of each name wins, as a link to a repeated heading reaches the first.
def index_of(lines: list[str]) -> dict[str, tuple[int, int]]:
    index: dict[str, tuple[int, int]] = {}
    for name, span in node_ranges(lines):
        index.setdefault(name, span)
    return index


def node_ranges(lines: list[str]) -> list[tuple[str, tuple[int, int]]]:
    starts, in_fence = [], False
    for i, line in enumerate(lines):
        if FENCE.match(line):
            in_fence = not in_fence
        elif not in_fence and line.startswith("# "):
            starts.append((line[2:].strip(), i))
    ends = [i for _, i in starts[1:]] + [len(lines)]
    return [(name, (start, end)) for (name, start), end in zip(starts, ends)]


# The root is the node with no parent link; failing that, the first node.
def root_node(lines: list[str]) -> str:
    for name in nodes_of(lines):
        if not any(line.startswith("[↑") for line in node_lines(lines, name)[1:6]):
            return name
    return nodes_of(lines)[0]


def id_of(node: list[str]) -> str | None:
    for line in scaffolding_block(node[1:]):
        if m := re.match(r"^id:\s*(\S+)", line):
            return m.group(1)
    return None


# Each approver's stamp date and fingerprint. Stamps are read from the scaffolding block only,
# so an example quoted later in the node is never taken for one.
def stamp_details(node: list[str]) -> dict[str, tuple[str, str]]:
    found = {}
    for line in scaffolding_block(node[1:]):
        m = STAMP.match(line)
        if m:
            at = re.search(r"\bat:\s*([0-9-]+)", line)
            found[m.group(1) or m.group(2) or m.group(3)] = (at.group(1) if at else "", m.group(4))
    return found


# --- Fingerprints, as method/util/fingerprint.py computes them ---
# Carried here so the viewer runs on its own; tests/fingerprint_test.py checks the two agree.

# Heading line to the line before the next heading, scaffolding block and navigation-link
# lines dropped, every whitespace character removed, first eight hex digits of SHA-256.
def fingerprint(node_lines: list[str]) -> str:
    text = re.sub(r"\s+", "", "".join([node_lines[0]] + strip_scaffolding(node_lines[1:])))
    return hashlib.sha256(text.encode("utf-8")).hexdigest()[:8]


def scaffolding_block(body: list[str]) -> list[str]:
    i = skip_nav(body)
    if i < len(body) and body[i].startswith("```yaml"):
        return body[i:end_of_fence(body, i) + 1]
    return []


def strip_scaffolding(body: list[str]) -> list[str]:
    i = skip_nav(body)
    if i < len(body) and body[i].startswith("```yaml"):
        i = end_of_fence(body, i) + 1
    return body[i:]


def skip_nav(body: list[str]) -> int:
    i = 0
    while i < len(body) and (body[i].strip() == "" or LINK_ONLY_LINE.match(body[i])):
        i += 1
    return i


def end_of_fence(lines: list[str], start: int) -> int:
    for i in range(start + 1, len(lines)):
        if FENCE.match(lines[i]):
            return i
    return len(lines) - 1


# The contents tree, followed from the entry map's root through each node's child links.
# Every other map file linked from a map in the tree, such as one the entry links to only
# in prose, gets its own file's tree beneath, so the tree is the same on every page.
def tree_html(current: tuple[str, str]) -> str:
    seen: set = set()
    trees = [tree_item(ENTRY, root_node(read_map(ENTRY)), current, seen)]
    for file in maps_linked_beyond(seen) + ([current[0]] if current[0] else []):
        if file not in {f for f, _ in seen}:
            trees.append(tree_item(file, root_node(read_map(file)), current, seen))
    return "".join(f"<ul>{t}</ul>" for t in trees)


# The map files linked from the maps already in the tree, and from those in turn, in the
# order first found, that the tree's child links don't reach.
def maps_linked_beyond(seen: set) -> list[str]:
    found = list(dict.fromkeys(f for f, _ in seen))
    for file in found:
        found.extend(f for f in linked_maps(file) if f not in found)
    in_tree = {f for f, _ in seen}
    return [f for f in found if f not in in_tree]


def linked_maps(file: str) -> list[str]:
    targets = re.findall(r"\]\(([^)#]+\.md)#", "".join(read_map(file)))
    linked = []
    for target in targets:
        path = os.path.normpath(Path(file).parent / target)
        try:
            map_path(path).stat()
        except (OSError, PermissionError):
            continue
        if path not in linked:
            linked.append(path)
    return linked


# Each file's part of the tree is shaded, its file name at the top right on hover. Shades
# alternate grey and green as the tree crosses from file to file, so neighbours differ.
FILE_SHADES = ["#f3f3f3", "#eaf5ea"]


def tree_item(file: str, name: str, current: tuple[str, str], seen: set,
              parent_file: str = "", shade: int = -1) -> str:
    seen.add((file, name))
    kids = [k for k in children(file, name) if k not in seen]
    seen.update(kids)
    mark = ' class="here"' if (file, name) == current else ""
    label = f'<a href="{node_url(file, name)}"{mark}>{html.escape(name)}</a>'
    classes, shade_style, file_tag = [] if kids else ["leaf"], "", ""
    if file != parent_file:
        shade += 1
        classes.append("branch")
        shade_style = f' style="background: {FILE_SHADES[shade % len(FILE_SHADES)]}"'
        file_tag = f'<span class="branch-file">{html.escape(file)}</span>'
    attrs = f' class="{" ".join(classes)}"' if classes else ""
    if not kids:
        return f"<li{attrs}{shade_style}>{file_tag}{label}</li>"
    inner = "".join(tree_item(f, n, current, seen, file, shade) for f, n in kids)
    # Beside the triangle: one button that folds this node and everything below it, or opens it all.
    below = '<span class="below"><button onclick="toggleAll(event)">−</button></span>'
    return f'<li{attrs}{shade_style}>{file_tag}<details open><summary>{label}{below}</summary><ul>{inner}</ul></details></li>'


def children(file: str, name: str) -> list[tuple[str, str]]:
    body = node_lines(read_map(file), name)[1:]
    found = []
    for line in body[:skip_nav(body)]:
        m = re.match(r"^\[([^\]]+)\]\(([^)]+)\)", line)
        if m and not m.group(1).startswith("↑") and (target := resolve(m.group(2), file)):
            found.append(target)
    return found


# --- Rendering ---

# The markdown maps use, rendered block by block: paragraphs, headings, nested and numbered
# lists, blockquotes and GitHub alerts, tables and fenced code. Hand-rolled rather than a
# library so the script still runs anywhere with no network.
def render_markdown(lines: list[str], file: str) -> str:
    return "\n".join(blocks_of([line.rstrip("\n") for line in lines], file))


LIST_ITEM = re.compile(r"^( *)([-*+]|\d+[.)]) +(.*)")
HEADING = re.compile(r"^(#{2,6}) +(.*?)\s*#*\s*$")
CODE_FENCE = re.compile(r"^\s*(`{3,})")
ALERT = re.compile(r"^\[!(NOTE|TIP|IMPORTANT|WARNING|CAUTION)\]\s*$", re.IGNORECASE)


def blocks_of(lines: list[str], file: str) -> list[str]:
    out, i = [], 0
    while i < len(lines):
        if not lines[i].strip():
            i += 1
            continue
        block, i = block_at(lines, i, file)
        out.append(block)
    return out


# The block starting at line i, rendered, and the line after it.
def block_at(lines: list[str], i: int, file: str) -> tuple[str, int]:
    text = lines[i]
    if m := CODE_FENCE.match(text):
        return code_block(lines, i, m.group(1))
    if m := HEADING.match(text):
        return f"<h{len(m.group(1))}>{inline(m.group(2), file)}</h{len(m.group(1))}>", i + 1
    if text.startswith(">"):
        return blockquote(lines, i, file)
    if text.startswith("|"):
        end = run_end(lines, i, lambda line: line.startswith("|"))
        return render_table(lines[i:end], file), end
    if m := LIST_ITEM.match(text):
        return list_block(lines, i, m, file)
    end = run_end(lines, i + 1, lambda line: line.strip() and not starts_block(line))
    return f"<p>{inline(' '.join(line.strip() for line in lines[i:end]), file)}</p>", end


def starts_block(line: str) -> bool:
    return bool(CODE_FENCE.match(line) or HEADING.match(line) or LIST_ITEM.match(line)
                or line.startswith((">", "|")))


def run_end(lines: list[str], i: int, belongs) -> int:
    while i < len(lines) and belongs(lines[i]):
        i += 1
    return i


# A fence closes on a line of at least as many backticks, so a fence can quote a shorter one.
def code_block(lines: list[str], i: int, ticks: str) -> tuple[str, int]:
    end = run_end(lines, i + 1, lambda line: not (line.strip().startswith(ticks) and set(line.strip()) == {"`"}))
    code = "".join(html.escape(line) + "\n" for line in lines[i + 1:end])
    return f"<pre><code>{code}</code></pre>", end + 1


# A GitHub alert, a blockquote opening with [!IMPORTANT] or the like, gets its kind as a title.
def blockquote(lines: list[str], i: int, file: str) -> tuple[str, int]:
    end = run_end(lines, i, lambda line: line.startswith(">"))
    inner = [re.sub(r"^> ?", "", line) for line in lines[i:end]]
    if inner and (m := ALERT.match(inner[0])):
        kind = m.group(1).lower()
        body = "\n".join(blocks_of(inner[1:], file))
        return f'<div class="alert alert-{kind}"><p class="alert-title">{kind.title()}</p>{body}</div>', end
    return f"<blockquote>{chr(10).join(blocks_of(inner, file))}</blockquote>", end


# A run of items sharing one indent and one kind, bulleted or numbered. An item holds what
# follows it indented deeper, so a nested list or a second paragraph renders inside it.
# Items with no blank line between them are tight: their text is not wrapped in paragraphs.
def list_block(lines: list[str], i: int, first: re.Match, file: str) -> tuple[str, int]:
    indent, ordered = len(first.group(1)), first.group(2)[0].isdigit()
    items, loose, item = [], False, first
    while True:
        body, i = list_item(lines, i, item, indent)
        items.append(body)
        loose = loose or "" in body
        after = run_end(lines, i, lambda line: not line.strip())
        item = LIST_ITEM.match(lines[after]) if after < len(lines) else None
        if not (item and len(item.group(1)) == indent and item.group(2)[0].isdigit() == ordered):
            break
        loose = loose or after > i
        i = after
    rendered = "".join(f"<li>{item_html(body, loose, file)}</li>" for body in items)
    if not ordered:
        return f"<ul>{rendered}</ul>", i
    start = int(first.group(2)[:-1])
    return f'<ol{f" start={start}" if start != 1 else ""}>{rendered}</ol>', i


# One item's lines with its marker removed and its continuation de-indented, and the line after it.
def list_item(lines: list[str], i: int, item: re.Match, indent: int) -> tuple[list[str], int]:
    content_indent = item.start(3)
    body, i = [item.group(3)], i + 1
    while i < len(lines):
        line = lines[i]
        if not line.strip():
            after = run_end(lines, i, lambda line: not line.strip())
            if after == len(lines) or indentation(lines[after]) <= indent:
                break
            body.extend([""] * (after - i))
            i = after
        elif indentation(line) > indent:
            body.append(line[min(content_indent, indentation(line)):])
            i += 1
        else:
            break
    return body, i


def item_html(body: list[str], loose: bool, file: str) -> str:
    blocks = blocks_of(body, file)
    if not loose and blocks and blocks[0].startswith("<p>"):
        blocks[0] = blocks[0][3:-4]
    return "\n".join(blocks)


def indentation(line: str) -> int:
    return len(line) - len(line.lstrip(" "))


def render_table(rows: list[str], file: str) -> str:
    cells = [[c.strip() for c in row.strip("|").split("|")] for row in rows if not re.match(r"^\|[-\s|]+\|$", row)]
    head, *body = cells
    return ("<table><tr>" + "".join(f"<th>{inline(c, file)}</th>" for c in head) + "</tr>"
            + "".join("<tr>" + "".join(f"<td>{inline(c, file)}</td>" for c in r) + "</tr>" for r in body) + "</table>")


def inline(text: str, file: str) -> str:
    codes = []
    text = re.sub(r"`([^`]+)`", lambda m: codes.append(m.group(1)) or f"\x00{len(codes) - 1}\x00", text)
    text = html.escape(text, quote=False)
    text = re.sub(r"\[([^\]]+)\]\(([^)]+)\)", lambda m: link(m.group(1), html.unescape(m.group(2)), file), text)
    text = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", text)
    text = re.sub(r"(?<!\w)\*(.+?)\*(?!\w)", r"<em>\1</em>", text)
    return re.sub(r"\x00(\d+)\x00", lambda m: f"<code>{html.escape(codes[int(m.group(1))])}</code>", text)


# A link to a node, here or in another map file, opens in the viewer; anything else is shown as text.
def link(text: str, target: str, file: str) -> str:
    found = resolve(target, file)
    return f'<a href="{node_url(*found)}">{text}</a>' if found else text


# The (file, node name) a link points at, or None if it isn't a node.
def resolve(target: str, file: str) -> tuple[str, str] | None:
    path, _, anchor = target.partition("#")
    target_file = os.path.normpath(Path(file).parent / path) if path else file
    if not (anchor and target_file.endswith(".md")):
        return None
    try:
        lines = read_map(target_file)
    except (OSError, PermissionError):
        return None
    name = next((n for n in nodes_of(lines) if slug(n) == anchor), None)
    return (target_file, name) if name else None


# Every map file is read through here, from under the map's directory only. Files are read
# often while drawing the tree, so each is kept until it changes on disk.
_read_cache: dict[str, tuple[int, list[str]]] = {}
# Keyed by the text's id; the entry holds the text itself, so the id can't be reused.
_index_cache: dict[int, tuple[list[str], dict[str, tuple[int, int]]]] = {}


def read_map(file: str) -> list[str]:
    path = map_path(file)
    mtime = path.stat().st_mtime_ns
    if file not in _read_cache or _read_cache[file][0] != mtime:
        if file in _read_cache:
            _index_cache.pop(id(_read_cache[file][1]), None)
        lines = path.read_text(encoding="utf-8").splitlines(keepends=True)
        _read_cache[file] = (mtime, lines)
        _index_cache[id(lines)] = (lines, index_of(lines))
    return _read_cache[file][1]


def map_path(file: str) -> Path:
    path = (ROOT / file).resolve()
    if not path.is_relative_to(ROOT.resolve()):
        raise PermissionError(file)
    return path


# The node in each commit of its file, newest first, found by id or else by name: a list
# of (commit, date, node lines), the lines None where the node is absent. Every version of
# the file comes from one git process, so a long history still answers quickly. Run per
# request, so not echoed.
def node_history(file: str, name: str) -> list[tuple[str, str, list[str] | None]]:
    path = map_path(file)
    node_id = id_of(node_lines(read_map(file), name))
    log = subprocess.run(f"git log --format='%h %as' -n 500 -- {shlex.quote(path.name)}", shell=True,
                         cwd=path.parent, capture_output=True, text=True)
    commits = [entry.split() for entry in log.stdout.splitlines()]
    versions = file_versions([commit for commit, _ in commits], path)
    return [(commit, date, node_in(old, node_id, name)) for (commit, date), old in zip(commits, versions)]


# The file's text at each commit, read through a single git cat-file --batch.
def file_versions(commits: list[str], path: Path) -> list[list[str]]:
    if not commits:
        return []
    request = "".join(f"{commit}:./{path.name}\n" for commit in commits)
    shown = subprocess.run("git cat-file --batch", shell=True, cwd=path.parent, input=request.encode("utf-8"),
                           capture_output=True).stdout
    versions, at = [], 0
    for _ in commits:
        header_end = shown.index(b"\n", at)
        header = shown[at:header_end].split()
        if header[-1] == b"missing":
            versions.append([])
            at = header_end + 1
            continue
        size = int(header[2])
        versions.append(shown[header_end + 1:header_end + 1 + size].decode("utf-8").splitlines(keepends=True))
        at = header_end + 1 + size + 1  # each object is followed by a newline
    return versions


# The node with this id in an old version of the file, or else the one with this name.
def node_in(old: list[str], node_id: str | None, name: str) -> list[str] | None:
    ranges = node_ranges(old)
    by_id = [old[start:end] for _, (start, end) in ranges if node_id and id_of(old[start:end]) == node_id]
    by_name = [old[start:end] for node, (start, end) in ranges if node == name]
    return (by_id or by_name or [None])[0]


def word_diff(before: str, after: str) -> str:
    a, b = re.split(r"(\s+)", before), re.split(r"(\s+)", after)
    out = []
    for op, i1, i2, j1, j2 in difflib.SequenceMatcher(None, a, b, autojunk=False).get_opcodes():
        if op in ("delete", "replace"):
            out.append(f"<del>{html.escape(''.join(a[i1:i2]))}</del>")
        if op in ("insert", "replace"):
            out.append(f"<ins>{html.escape(''.join(b[j1:j2]))}</ins>")
        if op == "equal":
            out.append(html.escape("".join(a[i1:i2])))
    return "".join(out)


def node_url(file: str, name: str) -> str:
    return f"/node?file={quote(file)}&name={quote(name)}"


def slug(heading: str) -> str:
    return re.sub(r"[^a-z0-9 -]", "", heading.lower()).replace(" ", "-")


def find_map(path: Path) -> Path:
    if path.is_dir():
        path = path / "map.md"
    if not path.is_file():
        error(f"No map at {path}. Pass a map file, or run beside a map.md.")
        sys.exit(1)
    return path.resolve()


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Serve a map, read-only, for reading and reviewing changes and approvals.")
    parser.add_argument("map", nargs="?", default=".", help="a map file, or a directory holding map.md (default: here)")
    parser.add_argument("--port", type=int, default=8080, help="port to listen on, on 127.0.0.1 (default: 8080)")
    parser.add_argument("--version", action="version", version=f"%(prog)s {VERSION}")
    return parser.parse_args()


def success(text: str) -> None:
    print(styled(f"✓ {text}", GREEN, sys.stdout))


def warn(text: str) -> None:
    print(styled(f"⚠ {text}", YELLOW, sys.stdout))


def error(text: str) -> None:
    print(styled(f"✗ {text}", RED, sys.stderr), file=sys.stderr)


def styled(text: str, code: str, stream) -> str:
    if stream.isatty() and "NO_COLOR" not in os.environ:
        return f"\033[{code}m{text}\033[0m"
    return text


if __name__ == "__main__":
    if not os.environ.get("VIRTUAL_ENV"):
        error("No virtual environment detected. Run this script via './map_viewer.py' (requires uv), or activate a virtual environment first.")
        sys.exit(100)
    try:
        main()
    except (KeyboardInterrupt, EOFError):
        print()
        warn("Aborted.")
        sys.exit(130)
