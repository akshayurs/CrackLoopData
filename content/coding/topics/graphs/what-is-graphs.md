A **graph** is a set of nodes connected by edges — grids, adjacency lists, and adjacency matrices are all just graphs in disguise. A 2D grid of cells is a graph where each cell is a node connected to its up/down/left/right neighbors. Most interview graph questions boil down to one traversal, run correctly.

**BFS (breadth-first search)** explores level by level using a queue. It is the tool for **shortest path in an unweighted graph** — the first time you reach a node, that is the shortest path to it.

**DFS (depth-first search)** explores as deep as possible before backtracking, using recursion or an explicit stack. It is the natural tool for **connectivity, counting components, and exhaustive exploration** (flood fill, marking every cell in an island).

Both share the same skeleton — a **visited set** to avoid revisiting a node, and a frontier (queue for BFS, stack/call-stack for DFS) to drive exploration:

```
visited = empty set
frontier = {start}
mark start visited
while frontier not empty:
    node = frontier.pop()          # dequeue for BFS, pop for DFS
    for neighbor of node:
        if neighbor not in visited:
            mark neighbor visited
            frontier.add(neighbor)
```

The two other recurring shapes: **topological sort** (order nodes so every edge points forward — course prerequisites) via BFS with in-degree counting (Kahn's algorithm) or DFS with post-order reversal, and **multi-source BFS** (start the queue with *all* sources at once — rotting oranges, walls-and-gates) to compute distance from the nearest of several starting points in one pass.
