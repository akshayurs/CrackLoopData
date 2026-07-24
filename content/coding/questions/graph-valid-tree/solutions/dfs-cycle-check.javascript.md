A tree is just a connected graph with no cycles, so check both conditions directly. Build an adjacency list, then DFS from node 0 while remembering the node you arrived from — if you ever reach a node you've already visited (and it isn't the one you just came from), you've found a cycle.

Once the DFS finishes, confirm every node got visited. If any node is unreached, the graph is split into more than one component and can't be a single tree.

```javascript
function validTree(n, edges) {
    if (edges.length !== n - 1) return false;

    const graph = Array.from({ length: n }, () => []);
    for (const [a, b] of edges) {
        graph[a].push(b);
        graph[b].push(a);
    }

    const visited = new Array(n).fill(false);

    function dfs(node, parent) {
        visited[node] = true;
        for (const neighbor of graph[node]) {
            if (neighbor === parent) continue;
            if (visited[neighbor]) return false;
            if (!dfs(neighbor, node)) return false;
        }
        return true;
    }

    if (n === 0) return true;
    if (!dfs(0, -1)) return false;
    return visited.every(Boolean);
}
```

## Why it works

An undirected graph is a valid tree exactly when it is connected and acyclic. The DFS tracks the parent so that walking back along the edge you just used isn't mistaken for a cycle; any other repeat visit means two distinct paths reach the same node, which is a cycle. After the walk, `visited.every(Boolean)` confirms connectivity — every node was reachable from node 0. The early edge-count check is a cheap short-circuit but the DFS alone is what actually proves the tree property.

## Complexity

- Time: O(n + e) — each node and edge is visited a constant number of times.
- Space: O(n + e) — adjacency list plus the recursion stack and visited array.
