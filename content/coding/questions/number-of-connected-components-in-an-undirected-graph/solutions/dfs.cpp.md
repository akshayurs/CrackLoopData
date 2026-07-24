Build an adjacency list from the edge list, then walk the nodes `0..n-1` in order. Whenever a node hasn't been visited yet, it must be the start of a brand-new component, so run a DFS from it to mark every node it can reach, and bump the component count once for that whole excursion.

Each node is visited exactly once across all the DFS calls combined, since a visited node is never explored again.

```cpp
#include <vector>
using namespace std;

class Solution {
public:
    int countComponents(int n, vector<vector<int>>& edges) {
        vector<vector<int>> graph(n);
        for (auto& edge : edges) {
            graph[edge[0]].push_back(edge[1]);
            graph[edge[1]].push_back(edge[0]);
        }

        vector<bool> visited(n, false);
        int count = 0;
        for (int node = 0; node < n; node++) {
            if (!visited[node]) {
                count++;
                dfs(node, graph, visited);
            }
        }
        return count;
    }

private:
    void dfs(int node, vector<vector<int>>& graph, vector<bool>& visited) {
        visited[node] = true;
        for (int neighbor : graph[node]) {
            if (!visited[neighbor]) dfs(neighbor, graph, visited);
        }
    }
};
```

## Why it works

Two nodes belong to the same component exactly when one is reachable from the other via edges. Starting a DFS from an unvisited node discovers and marks its entire component in one pass, so the outer loop only ever triggers a fresh DFS when it lands on a node from a component it hasn't counted yet — giving one increment per component.

## Complexity

- Time: O(n + e) — building the adjacency list is O(e), and DFS visits every node and edge at most once.
- Space: O(n + e) — the adjacency list plus the `visited` array and recursion stack.
