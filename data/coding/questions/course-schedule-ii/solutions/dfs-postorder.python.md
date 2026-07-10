Treat prerequisites as directed edges — course `a` depends on course `b` means an edge `a -> b`. If we finish course `b`'s own dependencies first and only add a course to the order *after* every one of its prerequisites has been added, the order we build is already a valid schedule. That's a depth-first postorder walk of the dependency graph.

Each node is marked `visiting` while it's on the current recursion stack and `done` once its whole subtree is resolved. Hitting a `visiting` node again means we've looped back onto ourselves — a cycle — so no schedule exists.

```python
def find_order(num_courses, prerequisites):
    graph = [[] for _ in range(num_courses)]
    for course, prereq in prerequisites:
        graph[course].append(prereq)

    UNVISITED, VISITING, DONE = 0, 1, 2
    state = [UNVISITED] * num_courses
    order = []

    def dfs(course):
        state[course] = VISITING
        for prereq in graph[course]:
            if state[prereq] == VISITING:
                return False
            if state[prereq] == UNVISITED and not dfs(prereq):
                return False
        state[course] = DONE
        order.append(course)
        return True

    for course in range(num_courses):
        if state[course] == UNVISITED:
            if not dfs(course):
                return []
    return order
```

## Why it works

`dfs(course)` only appends `course` to `order` after every prerequisite reachable from it has already been appended, so by construction every prerequisite precedes the courses that need it. Scanning courses `0` to `numCourses - 1` and recursing in that fixed order makes the resulting order deterministic. The three-color marking (`unvisited` / `visiting` / `done`) detects a cycle the moment the recursion revisits a node still on its own stack, letting us bail out with `[]` immediately.

## Complexity

- Time: O(V + E) — each course and each prerequisite edge is visited once.
- Space: O(V + E) — the adjacency list plus the recursion stack and state array.
