Instead of recursing, work outward from the courses that are already free to take. Count how many prerequisites each course still has left (its in-degree); any course with zero prerequisites can go into the schedule right now. Whenever a course is scheduled, "cross it off" for everything that depended on it, and any course whose count drops to zero joins the queue.

This is Kahn's algorithm. If we ever run out of zero-prerequisite courses before scheduling everyone, the remaining courses are stuck in a cycle.

```python
from collections import deque

def find_order(num_courses, prerequisites):
    graph = [[] for _ in range(num_courses)]
    indegree = [0] * num_courses
    for course, prereq in prerequisites:
        graph[prereq].append(course)
        indegree[course] += 1

    queue = deque(c for c in range(num_courses) if indegree[c] == 0)
    order = []

    while queue:
        course = queue.popleft()
        order.append(course)
        for nxt in graph[course]:
            indegree[nxt] -= 1
            if indegree[nxt] == 0:
                queue.append(nxt)

    return order if len(order) == num_courses else []
```

## Why it works

A course only enters the queue once every one of its prerequisites has already been scheduled, so the emitted `order` always respects the dependency edges. Seeding the queue by scanning `0` to `numCourses - 1`, and always draining it FIFO, makes the resulting order deterministic for a given graph. If a cycle exists, the courses inside it never reach in-degree zero, so `order` ends up shorter than `numCourses` and we report failure with `[]`.

## Complexity

- Time: O(V + E) — every course is enqueued once and every edge is relaxed once.
- Space: O(V + E) — the adjacency list, in-degree array, and queue.
