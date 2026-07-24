Model the courses as a directed graph: an edge from a course to each of its prerequisites. Finishing every course is possible exactly when this graph has no cycle — a cycle means a group of courses that all depend on each other, so none of them can ever be first.

Run a depth-first search from each course, coloring nodes as we go: unvisited, currently on the recursion stack ("visiting"), or fully processed ("done"). If the search ever reaches a node that is already "visiting", we have looped back onto the current path — a cycle.

```java
import java.util.ArrayList;
import java.util.List;

class Solution {
    private List<List<Integer>> graph;
    private int[] state;
    private static final int UNVISITED = 0, VISITING = 1, DONE = 2;

    public boolean canFinish(int numCourses, int[][] prerequisites) {
        graph = new ArrayList<>();
        for (int i = 0; i < numCourses; i++) graph.add(new ArrayList<>());
        for (int[] p : prerequisites) graph.get(p[0]).add(p[1]);

        state = new int[numCourses];
        for (int course = 0; course < numCourses; course++) {
            if (hasCycle(course)) return false;
        }
        return true;
    }

    private boolean hasCycle(int node) {
        if (state[node] == VISITING) return true;
        if (state[node] == DONE) return false;
        state[node] = VISITING;
        for (int prereq : graph.get(node)) {
            if (hasCycle(prereq)) return true;
        }
        state[node] = DONE;
        return false;
    }
}
```

## Why it works

A node marked "visiting" is an ancestor of the node currently being explored in the DFS tree; revisiting it means the graph has a back edge, which is precisely what defines a cycle in a directed graph. Once a node is marked "done", every path out of it has already been checked, so later searches can skip it safely. Running the search from every unvisited course guarantees disconnected parts of the graph are all covered.

## Complexity

- Time: O(V + E) — each course and each prerequisite edge is visited once.
- Space: O(V + E) — the adjacency list plus the recursion stack and state array.
