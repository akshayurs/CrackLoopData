A tree is just a connected graph with no cycles, so check both conditions directly. Build an adjacency list, then DFS from node 0 while remembering the node you arrived from — if you ever reach a node you've already visited (and it isn't the one you just came from), you've found a cycle.

Once the DFS finishes, confirm every node got visited. If any node is unreached, the graph is split into more than one component and can't be a single tree.

```cpp
#include <vector>
using namespace std;

class Solution {
public:
    bool validTree(int n, vector<vector<int>>& edges) {
        if ((int)edges.size() != n - 1) return false;

        vector<vector<int>> graph(n);
        for (auto& edge : edges) {
            graph[edge[0]].push_back(edge[1]);
            graph[edge[1]].push_back(edge[0]);
        }

        vector<bool> visited(n, false);
        if (n == 0) return true;
        if (!dfs(0, -1, graph, visited)) return false;

        for (bool v : visited) {
            if (!v) return false;
        }
        return true;
    }

private:
    bool dfs(int node, int parent, vector<vector<int>>& graph, vector<bool>& visited) {
        visited[node] = true;
        for (int neighbor : graph[node]) {
            if (neighbor == parent) continue;
            if (visited[neighbor]) return false;
            if (!dfs(neighbor, node, graph, visited)) return false;
        }
        return true;
    }
};
```

## Why it works

An undirected graph is a valid tree exactly when it is connected and acyclic. The DFS tracks the parent so that walking back along the edge you just used isn't mistaken for a cycle; any other repeat visit means two distinct paths reach the same node, which is a cycle. After the walk, scanning `visited` confirms connectivity — every node was reachable from node 0. The early edge-count check is a cheap short-circuit but the DFS alone is what actually proves the tree property.

## Complexity

- Time: O(n + e) — each node and edge is visited a constant number of times.
- Space: O(n + e) — adjacency list plus the recursion stack and visited array.
