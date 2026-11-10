# POS output practices

**Change Style:** Formal

## Intent

Update the POS standard with the terminal-output, secrets and interrupt practices proposed from a client project, keeping only what earns its place. POS should stay short and its scripts as simple and readable as today: prefer a rule to code, a few lines of code to many, and drop anything a reader of a POS script would have to learn without gaining clarity. NDD's own POS scripts should follow the result.

## Change Specification

Target: [140-pos-output-practices/POS.md](140-pos-output-practices/POS.md), a copy of `method/standards/POS.md`.

`install.py` and `method/util/fingerprint.py` follow the target: `rich` is dropped from their dependencies, their messages go through the target's `success()`, `warn()` and `error()` or plain `print()`, and their main guards match it.

## Implementation Plan

Before POS.md lands, the new `sudo()` is checked in a scratch POS script in `/tmp`, run three ways: as root, with passwordless sudo, and with a password. Sudo here needs a password, so the user runs that one and the root case; passwordless is checked in a container if one is to hand, else flagged. The two scripts change next and the tests run; POS.md lands last.

## Context

Proposed as a nine-item delta to `POS.md` from a client project's terminal colour scheme change (2026-11-10). Taken whole, it would nearly double the standard's 8.4k.

## Settled items

- 6. Output scheme: adapted to an *Output* section of one paragraph and three helpers plus `styled()` (841 characters); dropped banner/step/detail/prompt/stderr kinds, log mirroring and leading-newline handling. Colour codes named (`GREEN, YELLOW, RED, CYAN`).
- 1. `run()` echo: through a named `echo_command(cmd)` helper; a polled command calls it once before the loop.
- 2 + 10. `sudo()`: one path, root echoed as `# cmd` via `echo_command(cmd, root=True)`, failure through `error()`; fixes passwordless sudo running without sudo. Verify in Build as root, passwordless and with a password.
- 3 + 9. Main guard: venv error through `error()`; Ctrl-C/Ctrl-D caught only there, `print()` then `warn("Aborted.")`, exit 130.
- 7. Secrets: rule (commands never logged) plus an optional `run(cmd, secrets={name: value})` that echoes `<name>`; registry and log filter dropped.
- 8. Interpolated values: one bullet, quote and attach with `=`.
- 4. Libraries: one clause; helpers need only the standard library.
- 5. `append_or_conflict`: dropped; principle 3 already allows warning and keeping the user's value.

## Log

- 2026-11-10: Plan approved; Build Lock taken. Reconciled: live `POS.md` unchanged since the target copy was taken.
- 2026-11-10: Minor bump agreed, claiming 3.5.0-dev.
- 2026-11-10: `sudo()` checked in a scratch script: password and root cases pass (echo, live streaming, no stray prompt, `✗ FAILED` on error), run by the user. Passwordless not checked: no passwordless sudo or container here; its path differs from the password case only in passing no stdin. Open.
- 2026-11-10: `install.py` and `method/util/fingerprint.py` moved to the target's helpers and main guard; `rich` dropped. `install.py`'s per-status colours collapsed: a conflict is a warning, every other status a plain line. `fingerprint.py` bumped to 1.1.0. Both tests pass; error, success and install output smoke-tested.
- 2026-11-10: `method/standards/POS.md` landed from the target.
- 2026-11-10: Passwordless `sudo()` left untested at the user's choice; noted in Conclude. Nothing open.
- 2026-11-10: Revised with the user: `install.py` status words keep colour by state, green for done, yellow for conflict, plain for already present.

## Conclude

Built as specified; POS.md grows 27%, from 8.4k to 10.7k, against nearly double for the proposal as made. Passwordless `sudo()` is untested, left at the user's choice; password and root cases pass. `install.py`'s status words now take colour by state (done green, conflict yellow), and `fingerprint.py` is at 1.1.0.
