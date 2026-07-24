The most direct reading of the problem: simulate the minutes one at a time. On each minute, scan the whole grid, mark every fresh orange that touches a rotten one, then flip all of those marks to rotten at once — never rot mid-scan, or a fresh orange could rot twice in the same minute.

Keep going until a scan finds no fresh oranges left (done) or a scan finds fresh oranges but rots none of them (stuck forever).

```python
def oranges_rotting(grid):
    rows, cols = len(grid), len(grid[0])
    minutes = 0
    while True:
        fresh_left = False
        to_rot = []
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    fresh_left = True
                    for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                        nr, nc = r + dr, c + dc
                        if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 2:
                            to_rot.append((r, c))
                            break
        if not fresh_left:
            return minutes
        if not to_rot:
            return -1
        for r, c in to_rot:
            grid[r][c] = 2
        minutes += 1
```

## Why it works

Each full pass over the grid corresponds to exactly one minute, because `to_rot` is collected first and applied only after the scan finishes — so newly-rotted cells never infect a neighbor within the same minute. The loop terminates either when no fresh orange remains (`fresh_left` is `False`) or when a pass changes nothing (`to_rot` is empty), which means the remaining fresh oranges are unreachable.

## Complexity

- Time: O((rows * cols)²) — up to `rows * cols` minutes may be needed, and each minute rescans the whole grid.
- Space: O(rows * cols) — for the `to_rot` list built each minute.
