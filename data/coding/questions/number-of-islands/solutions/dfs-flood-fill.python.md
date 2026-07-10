Scan every cell. Whenever you land on an unvisited `'1'`, you've found a new island — sink it entirely with a depth-first search that recursively visits its up/down/left/right neighbors, marking each visited cell as `'0'` so it's never counted again.

Because the flood fill consumes the whole island before the outer scan moves on, each connected blob of land triggers exactly one increment of the island counter.

```python
def num_islands(grid):
    rows, cols = len(grid), len(grid[0])
    grid = [list(row) for row in grid]

    def sink(r, c):
        if r < 0 or r >= rows or c < 0 or c >= cols or grid[r][c] != '1':
            return
        grid[r][c] = '0'
        sink(r + 1, c)
        sink(r - 1, c)
        sink(r, c + 1)
        sink(r, c - 1)

    count = 0
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == '1':
                count += 1
                sink(r, c)
    return count
```

## Why it works

The outer double loop guarantees every cell is inspected. The first time it meets a `'1'` that hasn't already been erased, that cell must belong to an island the scan hasn't counted yet, so the counter increments once and `sink` erases every cell reachable from it via land moves — preventing the scan from ever re-counting the same island.

## Complexity

- Time: O(rows * cols) — every cell is visited by the outer loop once and sunk at most once.
- Space: O(rows * cols) — worst case recursion depth if the whole grid is one island.
