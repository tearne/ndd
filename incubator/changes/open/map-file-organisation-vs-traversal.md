# Weigh map file organisation against agent traversal cost

**Kind:** idea
**Anchor:** a3k

BOOTSTRAP tells the agent to start at the root and follow child links. How the map is split across files decides whether that is efficient for agents. Single-file: an agent reads the whole map in one shot, links cost nothing. Node-per-file: lazy traversal costs a fetch per node but lets an agent pull only the subtree it needs, saving context on large maps. The map build-out follow-up should choose a file organisation that keeps human navigation and agent traversal both cheap — likely single-file until size forces a split. Anchored at the root as a placeholder; really a Tooling concern once that node exists.
