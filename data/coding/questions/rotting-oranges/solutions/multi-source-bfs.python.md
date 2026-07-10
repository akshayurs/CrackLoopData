Instead of rescanning the whole grid every minute, start a breadth-first search from *every* rotten orange at once, tagging each queued cell with the minute it rotted. Layer by layer, a BFS naturally spreads outward one minute at a time — exactly the way the infection spreads — so a single pass through the queue gives the answer.

Count the fresh oranges up front; every time the BFS rots one, decrement the count. If any are left when the queue empties, they were unreachable.

```python
from collections import deque

def oranges_rotting(grid):
    rows, cols = len(grid), len(grid[0])
    queue = deque()
    fresh = 0
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 2:
                queue.append((r, c, 0))
            elif grid[r][c] == 1:
                fresh += 1

    minutes = 0
    while queue:
        r, c, minute = queue.popleft()
        minutes = max(minutes, minute)
        for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            nr, nc = r + dr, c + dc
            if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1:
                grid[nr][nc] = 2
                fresh -= 1
                queue.append((nr, nc, minute + 1))

    return minutes if fresh == 0 else -1
```

## Why it works

Seeding the queue with every rotten orange at minute 0 means the BFS explores in expanding "rings" of increasing minute count, matching how the real infection spreads simultaneously from all sources. Each cell is enqueued at most once — the moment it's marked rotten — so the final `minutes` is the largest minute stamp reached, and `fresh` reaching zero confirms every orange was infected rather than some being stranded behind empty cells.

## Complexity

- Time: O(rows * cols) — every cell is enqueued and processed at most once.
- Space: O(rows * cols) — the queue can hold every rotten cell at once.
