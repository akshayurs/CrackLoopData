The most direct way to measure an island is to stand on a land cell and explore outward, counting every connected `1` you can reach. Recursion expresses that exploration naturally: visiting a cell means visiting its four neighbors too.

To avoid recounting cells, sink each visited land cell to `0` as you leave it, so the grid itself doubles as the visited set. Scan every cell as a potential island start and keep the largest area seen.

```python
def max_area_of_island(grid):
    rows, cols = len(grid), len(grid[0])

    def dfs(r, c):
        if r < 0 or r >= rows or c < 0 or c >= cols or grid[r][c] == 0:
            return 0
        grid[r][c] = 0
        return 1 + dfs(r + 1, c) + dfs(r - 1, c) + dfs(r, c + 1) + dfs(r, c - 1)

    best = 0
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 1:
                best = max(best, dfs(r, c))
    return best
```

## Why it works

`dfs(r, c)` returns 0 immediately for out-of-bounds or water cells, otherwise it claims the current cell (sinking it to `0`) and adds the areas returned by its four neighbors. Because visited land is zeroed out, no cell is ever counted twice, so summing the recursive calls yields exactly the size of the connected component containing `(r, c)`. Iterating over every cell guarantees every island gets a starting point, and tracking a running maximum finds the largest one.

## Complexity

- Time: O(m·n) — each cell is visited and sunk at most once.
- Space: O(m·n) — worst case the recursion stack holds every land cell (a grid that is entirely one island).
