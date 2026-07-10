The recursive flood fill can blow the call stack on a grid where one island spans hundreds of rows. Swap recursion for an explicit queue: when a new `'1'` is found, push it, then repeatedly pop a cell, mark it visited, and push its unvisited land neighbors until the queue drains.

The counting logic is identical to the DFS version — only the mechanics of "sink this island" change, from a call stack to a queue.

```python
from collections import deque

def num_islands(grid):
    rows, cols = len(grid), len(grid[0])
    grid = [list(row) for row in grid]

    def sink(sr, sc):
        queue = deque([(sr, sc)])
        grid[sr][sc] = '0'
        while queue:
            r, c = queue.popleft()
            for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == '1':
                    grid[nr][nc] = '0'
                    queue.append((nr, nc))

    count = 0
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == '1':
                count += 1
                sink(r, c)
    return count
```

## Why it works

Every cell pulled off the queue is expanded exactly once, and a cell is only ever pushed after being marked `'0'`, so no cell is enqueued twice. The queue drains precisely when every cell reachable from the starting land cell has been visited, which is the same connected component the DFS version would have covered — just explored breadth-first instead of depth-first.

## Complexity

- Time: O(rows * cols) — every cell is enqueued and dequeued at most once.
- Space: O(rows * cols) — worst case queue size if the whole grid is one island.
