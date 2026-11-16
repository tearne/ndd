# Web UI approvals

## Intent

A stakeholder reviewing in the map viewer should be able to approve a node there, rather than only through the agent. Settle what such an approval is under the method's *Approval* rule, which today is a yes given in reply to the agent asking, with the agent writing the stamp; how the approver is identified, given the viewer has no login; and what the viewer may write.

## Context

Raised as item 7 of 002 Map viewer iteration on 2026-11-16 and spun out at the user's request. It reverses a decision: tooling development (archived 2026-11-10) first built an approve form, then re-agreed the viewer as read-only, for security and because review edits are better made through the agent. The viewer serves on 127.0.0.1 only, reached by port forwarding.
