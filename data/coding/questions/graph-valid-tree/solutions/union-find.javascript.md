Instead of building an adjacency list and doing a separate traversal plus a separate connectivity check, process the edges one at a time with a Union-Find (disjoint set) structure. Each edge either joins two previously separate components or reconnects two nodes already in the same component — and that second case is exactly a cycle, discovered the instant it happens.

Start by rejecting immediately if there aren't exactly `n - 1` edges, since a tree on `n` nodes has no other option. Then union every edge; if any union finds both endpoints already share a root, stop and report false. Surviving every edge with exactly `n - 1` of them guarantees a single connected, cycle-free component — no follow-up scan required.

```javascript
function validTree(n, edges) {
    if (edges.length !== n - 1) return false;

    const parent = Array.from({ length: n }, (_, i) => i);

    function find(x) {
        while (parent[x] !== x) {
            parent[x] = parent[parent[x]];
            x = parent[x];
        }
        return x;
    }

    for (const [a, b] of edges) {
        const rootA = find(a);
        const rootB = find(b);
        if (rootA === rootB) return false;
        parent[rootA] = rootB;
    }

    return true;
}
```

## Why it works

`edges.length === n - 1` is necessary but not sufficient on its own — it also has to be true that no edge ever reconnects two nodes that already share a root, since that would mean a cycle exists somewhere and, with only `n - 1` edges total, some other node would then be left disconnected. Processing edges with union-find catches a cycle the moment it forms, so passing every edge with exactly `n - 1` of them is proof enough that the graph is a single connected, acyclic component — a valid tree — without any separate connectivity pass.

## Complexity

- Time: O(n · α(n)) — near-constant per union/find with path compression.
- Space: O(n) — the parent array.
