You must take `numCourses` courses, labeled `0` to `numCourses - 1`. You are given `prerequisites`, where `prerequisites[i] = [a, b]` means you must finish course `b` before you can start course `a`. Return `true` if it is possible to finish every course, or `false` if the prerequisites form a cycle that makes it impossible.

## Examples

```text
Input:  numCourses = 2, prerequisites = [[1, 0]]
Output: true          # take course 0, then course 1
```

```text
Input:  numCourses = 2, prerequisites = [[1, 0], [0, 1]]
Output: false         # 0 needs 1 and 1 needs 0 — a cycle
```

```text
Input:  numCourses = 4, prerequisites = [[1, 0], [2, 0], [3, 1], [3, 2]]
Output: true          # e.g. order 0, 1, 2, 3
```

## Constraints

- 1 <= numCourses <= 10^5
- 0 <= prerequisites.length <= min(numCourses * (numCourses - 1), 5000)
- prerequisites[i].length == 2
- 0 <= a, b < numCourses, a != b
- All pairs `[a, b]` are unique.

## Follow-up

Can you also reconstruct a valid course order, not just say whether one exists?
