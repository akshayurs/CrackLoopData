Treat prerequisites as directed edges — course `a` depends on course `b` means an edge `a -> b`. If we finish course `b`'s own dependencies first and only add a course to the order *after* every one of its prerequisites has been added, the order we build is already a valid schedule. That's a depth-first postorder walk of the dependency graph.

Each node is marked `visiting` while it's on the current recursion stack and `done` once its whole subtree is resolved. Hitting a `visiting` node again means we've looped back onto ourselves — a cycle — so no schedule exists.

```javascript
function findOrder(numCourses, prerequisites) {
  const graph = Array.from({ length: numCourses }, () => []);
  for (const [course, prereq] of prerequisites) {
    graph[course].push(prereq);
  }

  const UNVISITED = 0, VISITING = 1, DONE = 2;
  const state = new Array(numCourses).fill(UNVISITED);
  const order = [];

  function dfs(course) {
    state[course] = VISITING;
    for (const prereq of graph[course]) {
      if (state[prereq] === VISITING) return false;
      if (state[prereq] === UNVISITED && !dfs(prereq)) return false;
    }
    state[course] = DONE;
    order.push(course);
    return true;
  }

  for (let course = 0; course < numCourses; course++) {
    if (state[course] === UNVISITED && !dfs(course)) return [];
  }
  return order;
}
```

## Why it works

`dfs(course)` only pushes `course` onto `order` after every prerequisite reachable from it has already been pushed, so by construction every prerequisite precedes the courses that need it. Scanning courses `0` to `numCourses - 1` and recursing in that fixed order makes the resulting order deterministic. The three-color marking (`unvisited` / `visiting` / `done`) detects a cycle the moment the recursion revisits a node still on its own stack, letting us bail out with `[]` immediately.

## Complexity

- Time: O(V + E) — each course and each prerequisite edge is visited once.
- Space: O(V + E) — the adjacency list plus the recursion stack and state array.
