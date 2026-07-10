The recursive flood fill can blow the call stack on a grid where one island spans hundreds of rows. Swap recursion for an explicit queue: when a new `'1'` is found, push it, then repeatedly shift a cell off the front, mark it visited, and push its unvisited land neighbors until the queue drains.

The counting logic is identical to the DFS version — only the mechanics of "sink this island" change, from a call stack to a queue.

```javascript
function numIslands(grid) {
  const rows = grid.length;
  const cols = grid[0].length;
  const g = grid.map((row) => row.split(''));
  const dirs = [[1, 0], [-1, 0], [0, 1], [0, -1]];

  function sink(sr, sc) {
    const queue = [[sr, sc]];
    g[sr][sc] = '0';
    let head = 0;
    while (head < queue.length) {
      const [r, c] = queue[head++];
      for (const [dr, dc] of dirs) {
        const nr = r + dr, nc = c + dc;
        if (nr >= 0 && nr < rows && nc >= 0 && nc < cols && g[nr][nc] === '1') {
          g[nr][nc] = '0';
          queue.push([nr, nc]);
        }
      }
    }
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

Every cell pulled from the queue is expanded exactly once, and a cell is only ever pushed after being marked `'0'`, so no cell is enqueued twice. The queue drains precisely when every cell reachable from the starting land cell has been visited, which is the same connected component the DFS version would have covered — just explored breadth-first instead of depth-first.

## Complexity

- Time: O(rows * cols) — every cell is enqueued and dequeued at most once.
- Space: O(rows * cols) — worst case queue size if the whole grid is one island.
