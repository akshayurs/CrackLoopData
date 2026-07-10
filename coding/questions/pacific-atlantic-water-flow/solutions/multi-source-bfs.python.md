Flip the direction of the search. Instead of asking "where can water starting at cell X go?" for every cell, start from the oceans and ask "which cells could have sent water here?" Water flows downhill-or-equal, so walking backward from a border means moving to a neighbor whose height is greater than or equal to the current one.

Seed a BFS with every Pacific-border cell at once, and a separate BFS with every Atlantic-border cell at once. Each visits, in a single O(m*n) sweep, exactly the set of cells that can reach that ocean. The answer is the intersection of the two sets — no cell is ever re-explored across different starting points.

```python
from collections import deque

def pacific_atlantic(heights):
    if not heights or not heights[0]:
        return []
    m, n = len(heights), len(heights[0])

    def bfs(starts):
        seen = set(starts)
        queue = deque(starts)
        while queue:
            r, c = queue.popleft()
            for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                nr, nc = r + dr, c + dc
                if (0 <= nr < m and 0 <= nc < n and (nr, nc) not in seen
                        and heights[nr][nc] >= heights[r][c]):
                    seen.add((nr, nc))
                    queue.append((nr, nc))
        return seen

    pacific_starts = [(0, c) for c in range(n)] + [(r, 0) for r in range(m)]
    atlantic_starts = [(m - 1, c) for c in range(n)] + [(r, n - 1) for r in range(m)]

    pacific = bfs(pacific_starts)
    atlantic = bfs(atlantic_starts)

    return [[r, c] for r in range(m) for c in range(n) if (r, c) in pacific and (r, c) in atlantic]
```

## Why it works

Reversing the flow condition (`>=` instead of `<=`) turns "can this cell send water to the ocean" into "can the ocean's backward search reach this cell," and the two are equivalent by symmetry of the adjacency relation. Since each BFS explores every cell at most once, running it from all border cells simultaneously still costs one pass over the grid instead of one pass per cell. Building the result by scanning rows then columns keeps it sorted without a separate sort step.

## Complexity

- Time: O(m * n) — each of the two BFS traversals visits every cell and edge at most once.
- Space: O(m * n) — the two visited sets and BFS queues.
