Reach for weighted-graph or union-find machinery the moment a problem sounds like any of these:

- **"Cheapest / shortest / minimum cost path"** with weighted edges — Dijkstra if weights are non-negative, Bellman-Ford if negative weights are possible or you have a strict **"at most K stops/edges"** constraint.
- **"Connect all points/cities at minimum total cost"** — MST via Prim's or Kruskal's.
- **"Are these two nodes/accounts/emails connected?"** or **"how many groups/provinces/islands of connections are there?"** — union-find, one union per given relationship, then count distinct roots.
- **"Redundant connection" / "will adding this edge create a cycle?"** — union-find; if `find(u) == find(v)` before you union, that edge is the redundant one.
- **"Order these items given pairwise constraints"** (alien dictionary, course prerequisites, build order) — topological sort (Kahn's BFS with in-degrees, or DFS post-order).
- **"Visit every edge exactly once"** (reconstruct an itinerary, route inspection) — Euler path/circuit via Hierholzer's algorithm.
- **"Maximize probability / minimize maximum edge on a path"** — Dijkstra variant with a different relaxation rule (multiply probabilities, or track the max edge instead of the sum).

Signal words: *"weighted"*, *"cost"*, *"minimum cost to connect"*, *"same group/circle/network"*, *"union"*, *"prerequisite"*, *"topological"*, *"at most k stops"*, *"critical connection" / "bridge"*. If the graph has edge weights or the question is fundamentally about grouping/merging, that's your cue — plain BFS/DFS won't be enough.
