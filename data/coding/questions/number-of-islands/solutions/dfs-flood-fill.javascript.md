Scan every cell. Whenever you land on an unvisited `'1'`, you've found a new island — sink it entirely with a depth-first search that recursively visits its up/down/left/right neighbors, marking each visited cell as `'0'` so it's never counted again.

Because the flood fill consumes the whole island before the outer scan moves on, each connected blob of land triggers exactly one increment of the island counter.

```javascript
function numIslands(grid) {
  const rows = grid.length;
  const cols = grid[0].length;
  const g = grid.map((row) => row.split(''));

  function sink(r, c) {
    if (r < 0 || r >= rows || c < 0 || c >= cols || g[r][c] !== '1') return;
    g[r][c] = '0';
    sink(r + 1, c);
    sink(r - 1, c);
    sink(r, c + 1);
    sink(r, c - 1);
  }

  let count = 0;
  for (let r = 0; r < rows; r++) {
    for (let c = 0; c < cols; c++) {
      if (g[r][c] === '1') {
        count++;
        sink(r, c);
      }
    }
  }
  return count;
}
```

## Why it works

The outer double loop guarantees every cell is inspected. The first time it meets a `'1'` that hasn't already been erased, that cell must belong to an island the scan hasn't counted yet, so the counter increments once and `sink` erases every cell reachable from it via land moves — preventing the scan from ever re-counting the same island.

## Complexity

- Time: O(rows * cols) — every cell is visited by the outer loop once and sunk at most once.
- Space: O(rows * cols) — worst case recursion depth if the whole grid is one island.
