Treat prerequisites as directed edges — course `a` depends on course `b` means an edge `a -> b`. If we finish course `b`'s own dependencies first and only add a course to the order *after* every one of its prerequisites has been added, the order we build is already a valid schedule. That's a depth-first postorder walk of the dependency graph.

Each node is marked `visiting` while it's on the current recursion stack and `done` once its whole subtree is resolved. Hitting a `visiting` node again means we've looped back onto ourselves — a cycle — so no schedule exists.

```cpp
#include <vector>
using namespace std;

class Solution {
public:
    vector<int> findOrder(int numCourses, vector<vector<int>>& prerequisites) {
        vector<vector<int>> graph(numCourses);
        for (auto& p : prerequisites) graph[p[0]].push_back(p[1]);

        vector<int> state(numCourses, 0); // 0=unvisited, 1=visiting, 2=done
        vector<int> order;
        order.reserve(numCourses);

        for (int course = 0; course < numCourses; course++) {
            if (state[course] == 0 && !dfs(course, graph, state, order)) {
                return {};
            }
        }
        return order;
    }

private:
    bool dfs(int course, vector<vector<int>>& graph, vector<int>& state, vector<int>& order) {
        state[course] = 1;
        for (int prereq : graph[course]) {
            if (state[prereq] == 1) return false;
            if (state[prereq] == 0 && !dfs(prereq, graph, state, order)) return false;
        }
        state[course] = 2;
        order.push_back(course);
        return true;
    }
};
```

## Why it works

`dfs(course)` only pushes `course` onto `order` after every prerequisite reachable from it has already been pushed, so by construction every prerequisite precedes the courses that need it. Scanning courses `0` to `numCourses - 1` and recursing in that fixed order makes the resulting order deterministic. The three-color marking (`unvisited` / `visiting` / `done`) detects a cycle the moment the recursion revisits a node still on its own stack, letting us bail out with an empty vector immediately.

## Complexity

- Time: O(V + E) — each course and each prerequisite edge is visited once.
- Space: O(V + E) — the adjacency list plus the recursion stack and state array.
