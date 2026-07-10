Treat prerequisites as directed edges — course `a` depends on course `b` means an edge `a -> b`. If we finish course `b`'s own dependencies first and only add a course to the order *after* every one of its prerequisites has been added, the order we build is already a valid schedule. That's a depth-first postorder walk of the dependency graph.

Each node is marked `visiting` while it's on the current recursion stack and `done` once its whole subtree is resolved. Hitting a `visiting` node again means we've looped back onto ourselves — a cycle — so no schedule exists.

```java
import java.util.ArrayList;
import java.util.List;

class Solution {
    private static final int UNVISITED = 0, VISITING = 1, DONE = 2;

    public int[] findOrder(int numCourses, int[][] prerequisites) {
        List<List<Integer>> graph = new ArrayList<>();
        for (int i = 0; i < numCourses; i++) graph.add(new ArrayList<>());
        for (int[] p : prerequisites) graph.get(p[0]).add(p[1]);

        int[] state = new int[numCourses];
        int[] order = new int[numCourses];
        int[] idx = {0};

        for (int course = 0; course < numCourses; course++) {
            if (state[course] == UNVISITED && !dfs(course, graph, state, order, idx)) {
                return new int[0];
            }
        }
        return order;
    }

    private boolean dfs(int course, List<List<Integer>> graph, int[] state, int[] order, int[] idx) {
        state[course] = VISITING;
        for (int prereq : graph.get(course)) {
            if (state[prereq] == VISITING) return false;
            if (state[prereq] == UNVISITED && !dfs(prereq, graph, state, order, idx)) return false;
        }
        state[course] = DONE;
        order[idx[0]++] = course;
        return true;
    }
}
```

## Why it works

`dfs(course)` only writes `course` into `order` after every prerequisite reachable from it has already been written, so by construction every prerequisite precedes the courses that need it. Scanning courses `0` to `numCourses - 1` and recursing in that fixed order makes the resulting order deterministic. The three-color marking (`unvisited` / `visiting` / `done`) detects a cycle the moment the recursion revisits a node still on its own stack, letting us bail out with an empty array immediately.

## Complexity

- Time: O(V + E) — each course and each prerequisite edge is visited once.
- Space: O(V + E) — the adjacency list plus the recursion stack and state array.
