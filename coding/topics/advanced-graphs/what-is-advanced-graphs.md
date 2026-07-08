Plain BFS/DFS answer "is it reachable?" and "what's the fewest edges?" **Advanced graphs** kick in the moment edges carry weight, direction matters for ordering, or you need to merge/split groups dynamically — shortest weighted path, minimum spanning tree, topological order, or "are these two nodes in the same component?"

Three families cover almost everything:

- **Weighted shortest path** — Dijkstra (non-negative weights, greedy + min-heap) or Bellman-Ford (handles negative weights, or a hard cap on the number of edges/stops).
- **Minimum spanning tree (MST)** — connect all nodes with minimum total edge weight, via Prim's or Kruskal's (Kruskal leans on union-find to skip edges that would form a cycle).
- **Union-Find (Disjoint Set Union)** — track which nodes belong to the same group under repeated "union these two" operations, answering "same component?" in near O(1).

A typical Dijkstra shape:

```
dist = map(node -> infinity), dist[start] = 0
minHeap = [(0, start)]
while minHeap not empty:
    d, u = pop smallest from minHeap
    if d > dist[u]: continue
    for (v, weight) in neighbors[u]:
        if dist[u] + weight < dist[v]:
            dist[v] = dist[u] + weight
            push (dist[v], v) to minHeap
```

Union-Find's core trade is **path compression + union by rank**, which flattens the "who's my parent?" chains so both `find` and `union` amortize to nearly O(1) instead of O(n) in a skewed tree.
