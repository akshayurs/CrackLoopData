Instead of recursing, work outward from the courses that are already free to take. Count how many prerequisites each course still has left (its in-degree); any course with zero prerequisites can go into the schedule right now. Whenever a course is scheduled, "cross it off" for everything that depended on it, and any course whose count drops to zero joins the queue.

This is Kahn's algorithm. If we ever run out of zero-prerequisite courses before scheduling everyone, the remaining courses are stuck in a cycle.

```java
import java.util.ArrayList;
import java.util.LinkedList;
import java.util.List;
import java.util.Queue;

class Solution {
    public int[] findOrder(int numCourses, int[][] prerequisites) {
        List<List<Integer>> graph = new ArrayList<>();
        for (int i = 0; i < numCourses; i++) graph.add(new ArrayList<>());
        int[] indegree = new int[numCourses];
        for (int[] p : prerequisites) {
            graph.get(p[1]).add(p[0]);
            indegree[p[0]]++;
        }

        Queue<Integer> queue = new LinkedList<>();
        for (int c = 0; c < numCourses; c++) if (indegree[c] == 0) queue.add(c);

        int[] order = new int[numCourses];
        int idx = 0;
        while (!queue.isEmpty()) {
            int course = queue.poll();
            order[idx++] = course;
            for (int next : graph.get(course)) {
                if (--indegree[next] == 0) queue.add(next);
            }
        }

        return idx == numCourses ? order : new int[0];
    }
}
```

## Why it works

A course only enters the queue once every one of its prerequisites has already been scheduled, so the emitted `order` always respects the dependency edges. Seeding the queue by scanning `0` to `numCourses - 1`, and always draining it FIFO, makes the resulting order deterministic for a given graph. If a cycle exists, the courses inside it never reach in-degree zero, so `idx` ends up smaller than `numCourses` and we report failure with an empty array.

## Complexity

- Time: O(V + E) — every course is enqueued once and every edge is relaxed once.
- Space: O(V + E) — the adjacency list, in-degree array, and queue.
