You're given a reference to a node in a connected, undirected graph. Every node stores an integer `val` and a list of `neighbors` — the nodes it's directly wired to. Produce a **deep copy** of the whole graph: brand-new nodes carrying the same values and the same connections, with none of them shared with the original.

Each node's value is unique, so it can double as an identifier while you clone. The copy must be reachable and shaped exactly like the original from any starting point, and it must not reference a single node from the input graph.

## Examples

```text
Input:  adjList = [[2, 4], [1, 3], [2, 4], [1, 3]]
Output: [[2, 4], [1, 3], [2, 4], [1, 3]]
# Node 1 connects to 2 and 4, node 2 connects to 1 and 3, and so on.
```

```text
Input:  adjList = [[]]
Output: [[]]        # a single node with no neighbors
```

```text
Input:  adjList = []
Output: []           # empty graph, node is null
```

## Constraints

- The number of nodes is in the range [0, 100].
- 1 <= Node.val <= 100
- Each node's value is unique.
- There are no self-loops or repeated edges.
- The graph is connected, and every node is reachable from every other node.
