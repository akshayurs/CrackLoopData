Reach for BFS/DFS the moment a problem sounds like any of these:

- **"Grid of 0s/1s, count islands / regions / connected areas"** — Number of Islands, Max Area of Island, Surrounded Regions. DFS or BFS flood fill from each unvisited land cell.
- **"Shortest path / minimum steps / fewest moves"** on an unweighted graph or grid — BFS, because it explores by distance layers.
- **"Spreads over time" / "how long until everything is X"** — Rotting Oranges, multi-source BFS from all starting points simultaneously.
- **"Can you finish all courses / tasks given prerequisites?"** — Course Schedule, cycle detection via DFS coloring or topological sort via Kahn's algorithm.
- **"Clone / copy this graph"** — DFS or BFS with a visited → clone map so you never re-create the same node twice.
- **"Is there a path from A to B?"** — Find if Path Exists in Graph, plain reachability via either traversal.
- **"Valid tree" / "connected components"** — n nodes, n-1 edges, no cycle, and everything reachable = a tree; count components with DFS/union-find.
- **"Two-color / divide into groups with no conflicting neighbors"** — Is Graph Bipartite?, BFS/DFS coloring alternately.

Signal words: *"grid"*, *"neighbors"*, *"adjacent"*, *"connected"*, *"reachable"*, *"shortest path"*, *"prerequisite"*, *"dependency"*, *"levels"*, *"minimum number of steps/moves"*. If the input is described as cells, rooms, courses, or "a list of edges", think graph traversal before anything else. Word Ladder and Open the Lock look like string/array puzzles but are BFS over an implicit graph of one-character transformations.
