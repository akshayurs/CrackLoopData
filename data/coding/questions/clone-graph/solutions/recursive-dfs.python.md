Cloning is naturally recursive: to clone a node, make a copy of it, then clone each of its neighbors and attach the copies. The one wrinkle is cycles — the graph is undirected, so following neighbors blindly would recurse forever. A hash map keyed by `val` fixes that: before cloning a node, check whether a copy already exists and reuse it instead of recursing again.

The map also doubles as the "visited" set, so every node is cloned exactly once no matter how many other nodes point back to it.

```python
def clone_graph(node):
    if node is None:
        return None

    clones = {}

    def dfs(cur):
        if cur.val in clones:
            return clones[cur.val]
        copy = Node(cur.val)
        clones[cur.val] = copy
        for neighbor in cur.neighbors:
            copy.neighbors.append(dfs(neighbor))
        return copy

    return dfs(node)
```

## Why it works

`clones` maps an original node's value to its clone. The first time a value is seen, a new `Node` is created and registered in the map *before* its neighbors are visited — so if a cycle leads back to this node, the lookup short-circuits the recursion and returns the already-created copy instead of looping forever. Every reachable node ends up with exactly one clone, and every edge in the original is mirrored by appending the corresponding clone to `neighbors`.

## Complexity

- Time: O(V + E) — each node is cloned once and each edge is traversed once.
- Space: O(V) — the `clones` map plus the recursion stack, both bounded by the number of nodes.
