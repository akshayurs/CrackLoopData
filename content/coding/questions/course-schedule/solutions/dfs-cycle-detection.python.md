Model the courses as a directed graph: an edge from a course to each of its prerequisites. Finishing every course is possible exactly when this graph has no cycle — a cycle means a group of courses that all depend on each other, so none of them can ever be first.

Run a depth-first search from each course, coloring nodes as we go: unvisited, currently on the recursion stack ("visiting"), or fully processed ("done"). If the search ever reaches a node that is already "visiting", we have looped back onto the current path — a cycle.

```python
def can_finish(num_courses, prerequisites):
    graph = [[] for _ in range(num_courses)]
    for course, pre in prerequisites:
        graph[course].append(pre)

    UNVISITED, VISITING, DONE = 0, 1, 2
    state = [UNVISITED] * num_courses

    def has_cycle(node):
        if state[node] == VISITING:
            return True
        if state[node] == DONE:
            return False
        state[node] = VISITING
        for prereq in graph[node]:
            if has_cycle(prereq):
                return True
        state[node] = DONE
        return False

    return not any(has_cycle(course) for course in range(num_courses))
```

## Why it works

A node marked "visiting" is an ancestor of the node currently being explored in the DFS tree; revisiting it means the graph has a back edge, which is precisely what defines a cycle in a directed graph. Once a node is marked "done", every path out of it has already been checked, so later searches can skip it safely. Running the search from every unvisited course guarantees disconnected parts of the graph are all covered.

## Complexity

- Time: O(V + E) — each course and each prerequisite edge is visited once.
- Space: O(V + E) — the adjacency list plus the recursion stack and state array.
