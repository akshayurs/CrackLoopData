There are `numCourses` courses labeled `0` to `numCourses - 1`. You are given an array `prerequisites` where `prerequisites[i] = [a, b]` means you must take course `b` before course `a`. Return an ordering of all courses you could take to finish every course. If no valid ordering exists (the requirements form a cycle), return an empty array.

## Examples

```text
Input:  numCourses = 2, prerequisites = [[1, 0]]
Output: [0, 1]        # course 0 has no prerequisite, so it comes first
```

```text
Input:  numCourses = 4, prerequisites = [[1, 0], [2, 0], [3, 1], [3, 2]]
Output: [0, 1, 2, 3]  # 0 unlocks 1 and 2, which both unlock 3
```

```text
Input:  numCourses = 2, prerequisites = [[1, 0], [0, 1]]
Output: []            # 0 needs 1 and 1 needs 0 — a cycle, no valid order
```

## Constraints

- 1 <= numCourses <= 2000
- 0 <= prerequisites.length <= numCourses * (numCourses - 1)
- prerequisites[i].length == 2
- 0 <= a, b < numCourses
- a != b
- All pairs `[a, b]` are distinct.

## Follow-up

Can you detect a cycle and build the order in a single traversal, without a separate validation pass?
