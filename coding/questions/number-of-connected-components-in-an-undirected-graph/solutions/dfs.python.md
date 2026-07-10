Build an adjacency list from the edge list, then walk the nodes `0..n-1` in order. Whenever a node hasn't been visited yet, it must be the start of a brand-new component, so run a DFS from it to mark every node it can reach, and bump the component count once for that whole excursion.

Each node is visited exactly once across all the DFS calls combined, since a visited node is never explored again.

```python
def count_components(n, edges):
    graph = [[] for _ in range(n)]
    for a, b in edges:
        graph[a].append(b)
        graph[b].append(a)

    visited = [False] * n
    count = 0

    def dfs(node):
        visited[node] = True
        for neighbor in graph[node]:
            if not visited[neighbor]:
                dfs(neighbor)

    for node in range(n):
        if not visited[node]:
            count += 1
            dfs(node)

    return count
```

## Why it works

Two nodes belong to the same component exactly when one is reachable from the other via edges. Starting a DFS from an unvisited node discovers and marks its entire component in one pass, so the outer loop only ever triggers a fresh DFS when it lands on a node from a component it hasn't counted yet — giving one increment per component.

## Complexity

- Time: O(n + e) — building the adjacency list is O(e), and DFS visits every node and edge at most once.
- Space: O(n + e) — the adjacency list plus the `visited` array and recursion stack.
