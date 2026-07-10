A tree is just a connected graph with no cycles, so check both conditions directly. Build an adjacency list, then DFS from node 0 while remembering the node you arrived from — if you ever reach a node you've already visited (and it isn't the one you just came from), you've found a cycle.

Once the DFS finishes, confirm every node got visited. If any node is unreached, the graph is split into more than one component and can't be a single tree.

```java
import java.util.ArrayList;
import java.util.List;

class Solution {
    public boolean validTree(int n, int[][] edges) {
        if (edges.length != n - 1) return false;

        List<List<Integer>> graph = new ArrayList<>();
        for (int i = 0; i < n; i++) graph.add(new ArrayList<>());
        for (int[] edge : edges) {
            graph.get(edge[0]).add(edge[1]);
            graph.get(edge[1]).add(edge[0]);
        }

        boolean[] visited = new boolean[n];
        if (n == 0) return true;
        if (!dfs(0, -1, graph, visited)) return false;

        for (boolean v : visited) {
            if (!v) return false;
        }
        return true;
    }

    private boolean dfs(int node, int parent, List<List<Integer>> graph, boolean[] visited) {
        visited[node] = true;
        for (int neighbor : graph.get(node)) {
            if (neighbor == parent) continue;
            if (visited[neighbor]) return false;
            if (!dfs(neighbor, node, graph, visited)) return false;
        }
        return true;
    }
}
```

## Why it works

An undirected graph is a valid tree exactly when it is connected and acyclic. The DFS tracks the parent so that walking back along the edge you just used isn't mistaken for a cycle; any other repeat visit means two distinct paths reach the same node, which is a cycle. After the walk, scanning `visited` confirms connectivity — every node was reachable from node 0. The early edge-count check is a cheap short-circuit but the DFS alone is what actually proves the tree property.

## Complexity

- Time: O(n + e) — each node and edge is visited a constant number of times.
- Space: O(n + e) — adjacency list plus the recursion stack and visited array.
