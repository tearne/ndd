# All git writes gated

**Change Style:** Vibe

## Intent

`git mv` and `git rm` should be allowed wherever the agent may already move or delete the file. Every other git command that changes the repository, its index or its history, not only commit, push, branch and reset, should be left to the user unless they ask for it. The agent may name one in passing but should neither ask nor wait, so the work flows on.

## Bounds

Only *Gates and Permissions* and the *Git Writes* rule change; *Process Keyword*'s "like any git write" stays as it reads. The reworded rule is A/B tested before it ships.

## Context

Agents run `git mv` or `git rm` unasked, then catch and report it as a breach. *Gates and Permissions* names only commit, push, branch and reset, so it reads as a closed list yet leaves these two unclear.

## Log

- 2026-11-10: Plan approved; Build Lock taken.
- 2026-11-10: Minor bump agreed, claiming 3.2.0-dev.
- 2026-11-10: *Gates and Permissions* git-writes line reworded and stamped (b2c61377); 814 characters, accepted over the bound.
- 2026-11-10: *Gates and Permissions: Git Writes* rewording approved; A/B test running before it lands.
- 2026-11-10: Rule A/B test, 3 tasks × current/new wording, scratch git repos. Archiving: current used plain mv/rm, new used `git mv`/`git rm`; neither committed, both named the commit in passing. Release needing a tag: current named the commands for the user to run; new said it would ask for each when reached. Plain Build edit: neither asked to commit; new mentioned it in passing. No backfire. Rule kept as approved.
- 2026-11-10: *Gates and Permissions: Git Writes* landed in `method/AGENT-RULES.md`.

## Conclude

Built within Bounds, touching `method/ndd.map.md` and `method/AGENT-RULES.md`. Added in Build at the user's request: where the task itself needs a git write, the agent asks for it, since the Intent's never-ask applies only to day-to-day work. *Gates and Permissions* ends at 814 characters, accepted over the bound.
