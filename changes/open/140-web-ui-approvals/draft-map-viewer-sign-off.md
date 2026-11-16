On a node's page, beside its sign-offs, a *Sign off* button records a sign-off for each name ticked in its drop-down. Whoever presses it need not be among them: sharing the screen in a meeting, the user records each stakeholder's sign-off in front of them.

The drop-down lists every handle in the map's stamps, plus any name added in that browser, which stays until removed there; only added names can be removed. The names ticked last are ticked again.

Each name gets its line under the node's `approvals:` key: today's date and the fingerprint the server computed when rendering the page. Nothing else is written, and nothing is committed. The page sends that fingerprint back as a receipt, and the server recomputes it from disk, refusing if the node changed since, so no one signs off text they were not shown. An approval diff has no button, as it shows an old version. Writes are guarded as [Map Viewer Security](#map-viewer-security) describes.
