Cloning is naturally recursive: to clone a node, make a copy of it, then clone each of its neighbors and attach the copies. The one wrinkle is cycles — the graph is undirected, so following neighbors blindly would recurse forever. A hash map keyed by `val` fixes that: before cloning a node, check whether a copy already exists and reuse it instead of recursing again.

The map also doubles as the "visited" set, so every node is cloned exactly once no matter how many other nodes point back to it.

```java
import java.util.HashMap;
import java.util.Map;

class Solution {
    public Node cloneGraph(Node node) {
        return dfs(node, new HashMap<>());
    }

    private Node dfs(Node cur, Map<Integer, Node> clones) {
        if (cur == null) return null;
        if (clones.containsKey(cur.val)) return clones.get(cur.val);
        Node copy = new Node(cur.val);
        clones.put(cur.val, copy);
        for (Node neighbor : cur.neighbors) {
            copy.neighbors.add(dfs(neighbor, clones));
        }
        return copy;
    }
}
```

## Why it works

`clones` maps an original node's value to its clone. The first time a value is seen, a new `Node` is created and registered in the map *before* its neighbors are visited — so if a cycle leads back to this node, the lookup short-circuits the recursion and returns the already-created copy instead of looping forever. Every reachable node ends up with exactly one clone, and every edge in the original is mirrored by adding the corresponding clone to `neighbors`.

## Complexity

- Time: O(V + E) — each node is cloned once and each edge is traversed once.
- Space: O(V) — the `clones` map plus the recursion stack, both bounded by the number of nodes.
