# Withdraw requests

**Change Style:** Vibe

## Intent

A user should be able to withdraw requests for sign-off from the map viewer, on one node or many. Only a requested stamp is ever removed, never a current or stale one.

## Bounds

A withdrawal is checked and written as a request is, behind the same guards: a node lacking a request is skipped, one that can't be written refuses the whole. Where *Withdraw* sits is the user's call, shown before it is settled.

## Context

Raised on 2026-11-25 after 360 Bulk request in the tree: a request is now cleared only by signing off or by deleting its line by hand. Suggested shape: a `/withdraw` endpoint mirroring `request_signoffs`, and *Withdraw* beside *Apply* in the request bar and perhaps beside *Request* in the *Sign off* drop-down. Agreed in chat: withdrawing the last stamp leaves `signers:` empty rather than removing the key. The method map gains a minimal statement that a request may be withdrawn, likely in *Stamp States*, if it can be said briefly.

## Progress

- 2026-11-25: Intent approved.
- 2026-11-25: Change Style Vibe confirmed.
- 2026-11-25: Bounds approved.
- 2026-11-25: plan approved; Build Lock taken. Claims 3.12.0-dev (minor); map viewer 0.8.0 → 0.9.0.
- First cut, 3.12.0-dev.1: `/withdraw` endpoint shares `request_signoffs`, which removes each ticked name's requested stamp, passes by a node with no request (or no scaffolding block), and refuses the whole for a node that can't be written; `signers:` stays when emptied. *Withdraw* placed beside *Request* in the *Sign off* drop-down and beside *Apply* in the request bar, plain-styled, for the user to judge. Back-end checks `withdraw_removes_requests` and `withdraw_refusals`, browser check `withdraw_requests` added; all pass. Surprise: a BrokenPipe traceback in the browser run's server log, from a page closed mid-response; the run passes, and whether it predates this change is unchecked.
- Second cut, 3.12.0-dev.2, from user feedback: the request bar's *Withdraw* button replaced by a *request* / *withdraw* radio on its second row, between the count and *children*, so *Apply* does either; it resets to *request* each time the bar opens. *Withdraw* in the *Sign off* drop-down unchanged. Browser check updated; all tests pass.
- Third cut, 3.12.0-dev.3, from user feedback: the *Sign off* drop-down's three buttons replaced by a *sign off* / *request* / *withdraw* radio and one *Apply* (blue, as *Sign off* was); the drop-down widened to 15rem to fit, and opens set to *sign off*. Each drop-down's radio group is named uniquely, as two panes may each show one. Browser checks updated, with one that it reopens set to sign off; all pass. Surprises: removing an added name closes the drop-down, since the removed row is no longer inside it when the click-outside check runs — pre-existing, open; the *fold button* check failed once in four runs, then passed three times — flaky, untouched by this change, open.
- Fourth cut, 3.12.0-dev.4, from user feedback: the request bar's count of nodes picked removed; its second row holds the mode radio and *children*. All tests pass.
- Open item resolved: removing an added name no longer closes its drop-down; both click-outside handlers ignore a click whose target has left the page. Browser check added; all pass.
- Open item resolved: the fold button relabels as soon as it is clicked, not on the toggle events that follow, which raced the *fold button* check. Five browser runs pass.
- 2026-11-25: map edit 1 settled — *Stamp States* (method map): withdrawing a request deletes the stamp; stamped d33dfff9.
- 2026-11-25: map edit 2 (*Sign-off Button*, bulleted, 821) written in place as a draft at the user's *write*; awaiting review.
- 2026-11-25: map edit 2 settled — *Sign-off Button*: the mode choice as bullets (user's verbs, withdraw matched); stamped 5f6d903f.
- 2026-11-25: map edit 3 settled — *Request Bar*: withdraws too, mode choice replaces the count; stamped ceab9d20.
- 2026-11-25: map edit 4 settled — *Write Checks*: both checks cover withdrawal; Partial write names what stops a node taking the write; stamped 21e2ed15.
- 2026-11-25: map edit 5a settled — *Map Viewer Write Check*: Withdrawal bullet; stamped f5b78cf7.
- 2026-11-25: map edit 5b settled — *Map Viewer Browser Check*: drop-down stays open on removal, reopens set to sign off; stamped adaa2da5.
- 2026-11-25: map edit 5c settled — *Map Viewer Due Check*: withdrawing in the drop-down and the bar; stamped cddd2b67. Map edits done; Conclude next.
- 2026-11-25: map edit 6 (*Map Viewer* Sign off and Request bullets) written in place as a draft at the user's *write*; awaiting review.
- 2026-11-25: *Map Viewer* opening without "A prototype" written in place as a draft at the user's *write*; awaiting review with the bullets.
- 2026-11-25: map edit 6 settled — *Map Viewer*: opening drops "A prototype"; Sign off and Request bullets cover withdrawing; stamped c6f692ec. Map edits done; Conclude next.

## Conclude

Built over four cuts to 3.12.0-dev.4, from user feedback: Withdraw buttons gave way to a request/withdraw radio with one Apply, the Sign off drop-down gaining sign off/request/withdraw likewise, and the request bar's count was dropped. Two fixes off-topic but in touched code: removing a name no longer closes its drop-down, and the fold button relabels at once, ending a flaky check. Touched beyond the plan: Write Checks, Map Viewer (no longer called a prototype) and three testing-map nodes.
- 2026-11-25: Archiving paused at Tidy: reported counts were wrong for five nodes (Map Viewer Write Check 930, not ~790). To trim it, `withdraw_refusals` gained no-token, foreign Origin and foreign Host cases, so the node can state the guards once for all writes; all pass.
- 2026-11-25: *Map Viewer Write Check* trimmed to 690, guards stated once; stamped 8adcbe3e. Archiving resumes at step 3.
- 2026-11-25: Archiving steps 3–5 found done after a disconnect: change moved to archive, no `active.md` (lock released), no `changes/resume.md` (no pause entries). Archiving complete.
