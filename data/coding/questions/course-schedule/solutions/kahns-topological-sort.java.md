A different way to see the same graph: a course with zero remaining prerequisites is safe to take right now. Take it, then "remove" it — which lowers the prerequisite count of every course that depended on it — and repeat. If this process can eventually take every course, there was no cycle; if it stalls with courses left over, those remaining courses are stuck in a cycle.

This is Kahn's algorithm for topological sorting. Track each course's in-degree (how many prerequisites it still needs), seed a queue with the courses that need none, and process the queue while decrementing in-degrees of dependents.

```java
import java.util.ArrayDeque;
import java.util.ArrayList;
import java.util.List;
import java.util.Queue;

class Solution {
    public boolean canFinish(int numCourses, int[][] prerequisites) {
        List<List<Integer>> graph = new ArrayList<>();
        for (int i = 0; i < numCourses; i++) graph.add(new ArrayList<>());
        int[] indegree = new int[numCourses];
        for (int[] p : prerequisites) {
            graph.get(p[1]).add(p[0]);
            indegree[p[0]]++;
        }

        Queue<Integer> queue = new ArrayDeque<>();
        for (int c = 0; c < numCourses; c++) {
            if (indegree[c] == 0) queue.add(c);
        }

        int taken = 0;
        while (!queue.isEmpty()) {
            int course = queue.poll();
            taken++;
            for (int dependent : graph.get(course)) {
                if (--indegree[dependent] == 0) queue.add(dependent);
            }
        }

        return taken == numCourses;
    }
}
```

## Why it works

A course only enters the queue once every one of its prerequisites has already been taken, so the order courses are polled in is always a valid schedule. If the graph is acyclic, this process empties the queue only after every course has been taken. If a cycle exists, every course in it perpetually needs at least one prerequisite that never finishes, so it is never enqueued — leaving `taken < numCourses`.

## Complexity

- Time: O(V + E) — every course is enqueued once and every edge relaxes one in-degree.
- Space: O(V + E) — the adjacency list, in-degree array, and queue.
