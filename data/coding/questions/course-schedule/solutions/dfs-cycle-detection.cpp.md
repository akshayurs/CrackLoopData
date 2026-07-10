Model the courses as a directed graph: an edge from a course to each of its prerequisites. Finishing every course is possible exactly when this graph has no cycle — a cycle means a group of courses that all depend on each other, so none of them can ever be first.

Run a depth-first search from each course, coloring nodes as we go: unvisited, currently on the recursion stack ("visiting"), or fully processed ("done"). If the search ever reaches a node that is already "visiting", we have looped back onto the current path — a cycle.

```cpp
#include <vector>
using namespace std;

class Solution {
public:
    bool canFinish(int numCourses, vector<vector<int>>& prerequisites) {
        graph.assign(numCourses, {});
        for (auto& p : prerequisites) {
            graph[p[0]].push_back(p[1]);
        }

        state.assign(numCourses, UNVISITED);
        for (int course = 0; course < numCourses; course++) {
            if (hasCycle(course)) return false;
        }
        return true;
    }

private:
    enum { UNVISITED = 0, VISITING = 1, DONE = 2 };
    vector<vector<int>> graph;
    vector<int> state;

    bool hasCycle(int node) {
        if (state[node] == VISITING) return true;
        if (state[node] == DONE) return false;
        state[node] = VISITING;
        for (int prereq : graph[node]) {
            if (hasCycle(prereq)) return true;
        }
        state[node] = DONE;
        return false;
    }
};
```

## Why it works

A node marked "visiting" is an ancestor of the node currently being explored in the DFS tree; revisiting it means the graph has a back edge, which is precisely what defines a cycle in a directed graph. Once a node is marked "done", every path out of it has already been checked, so later searches can skip it safely. Running the search from every unvisited course guarantees disconnected parts of the graph are all covered.

## Complexity

- Time: O(V + E) — each course and each prerequisite edge is visited once.
- Space: O(V + E) — the adjacency list plus the recursion stack and state array.
