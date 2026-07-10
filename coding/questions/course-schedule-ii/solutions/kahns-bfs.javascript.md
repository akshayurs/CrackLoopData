Instead of recursing, work outward from the courses that are already free to take. Count how many prerequisites each course still has left (its in-degree); any course with zero prerequisites can go into the schedule right now. Whenever a course is scheduled, "cross it off" for everything that depended on it, and any course whose count drops to zero joins the queue.

This is Kahn's algorithm. If we ever run out of zero-prerequisite courses before scheduling everyone, the remaining courses are stuck in a cycle.

```javascript
function findOrder(numCourses, prerequisites) {
  const graph = Array.from({ length: numCourses }, () => []);
  const indegree = new Array(numCourses).fill(0);
  for (const [course, prereq] of prerequisites) {
    graph[prereq].push(course);
    indegree[course]++;
  }

  const queue = [];
  for (let c = 0; c < numCourses; c++) if (indegree[c] === 0) queue.push(c);

  const order = [];
  let head = 0;
  while (head < queue.length) {
    const course = queue[head++];
    order.push(course);
    for (const next of graph[course]) {
      if (--indegree[next] === 0) queue.push(next);
    }
  }

  return order.length === numCourses ? order : [];
}
```

## Why it works

A course only enters the queue once every one of its prerequisites has already been scheduled, so the emitted `order` always respects the dependency edges. Seeding the queue by scanning `0` to `numCourses - 1`, and always draining it FIFO (via the `head` pointer), makes the resulting order deterministic for a given graph. If a cycle exists, the courses inside it never reach in-degree zero, so `order` ends up shorter than `numCourses` and we report failure with `[]`.

## Complexity

- Time: O(V + E) — every course is enqueued once and every edge is relaxed once.
- Space: O(V + E) — the adjacency list, in-degree array, and queue.
