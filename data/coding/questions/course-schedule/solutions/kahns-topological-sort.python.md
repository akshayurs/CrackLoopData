A different way to see the same graph: a course with zero remaining prerequisites is safe to take right now. Take it, then "remove" it — which lowers the prerequisite count of every course that depended on it — and repeat. If this process can eventually take every course, there was no cycle; if it stalls with courses left over, those remaining courses are stuck in a cycle.

This is Kahn's algorithm for topological sorting. Track each course's in-degree (how many prerequisites it still needs), seed a queue with the courses that need none, and process the queue while decrementing in-degrees of dependents.

```python
from collections import deque

def can_finish(num_courses, prerequisites):
    graph = [[] for _ in range(num_courses)]
    indegree = [0] * num_courses
    for course, pre in prerequisites:
        graph[pre].append(course)
        indegree[course] += 1

    queue = deque(c for c in range(num_courses) if indegree[c] == 0)
    taken = 0

    while queue:
        course = queue.popleft()
        taken += 1
        for dependent in graph[course]:
            indegree[dependent] -= 1
            if indegree[dependent] == 0:
                queue.append(dependent)

    return taken == num_courses
```

## Why it works

A course only enters the queue once every one of its prerequisites has already been taken, so the order courses are dequeued in is always a valid schedule. If the graph is acyclic, this process empties the queue only after every course has been taken. If a cycle exists, every course in it perpetually needs at least one prerequisite that never finishes, so it is never enqueued — leaving `taken < num_courses`.

## Complexity

- Time: O(V + E) — every course is enqueued once and every edge relaxes one in-degree.
- Space: O(V + E) — the adjacency list, in-degree array, and queue.
