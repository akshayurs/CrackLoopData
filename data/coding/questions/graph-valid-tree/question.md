You are given `n` nodes labeled `0` to `n - 1` and a list of undirected `edges`, where `edges[i] = [a, b]` means there is an edge between node `a` and node `b`. Return `true` if these edges form a valid tree, or `false` otherwise.

A valid tree is a connected graph with no cycles — equivalently, it has exactly `n - 1` edges and every node is reachable from every other node.

## Examples

```text
Input:  n = 5, edges = [[0, 1], [0, 2], [0, 3], [1, 4]]
Output: true          # connected, 4 edges for 5 nodes, no cycle
```

```text
Input:  n = 5, edges = [[0, 1], [1, 2], [2, 3], [1, 3], [1, 4]]
Output: false         # 1-2-3-1 forms a cycle
```

```text
Input:  n = 4, edges = [[0, 1], [2, 3]]
Output: false         # only 2 edges for 4 nodes — not connected
```

## Constraints

- 1 <= n <= 2000
- 0 <= edges.length <= 5000
- edges[i].length == 2
- 0 <= a, b < n, a != b
- There are no duplicate edges and no self-loops.

## Follow-up

Can you decide validity with a single pass over the edges, without a separate connectivity check afterward?
