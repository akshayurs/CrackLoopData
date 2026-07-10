Instead of rescanning the whole grid every minute, start a breadth-first search from *every* rotten orange at once, tagging each queued cell with the minute it rotted. Layer by layer, a BFS naturally spreads outward one minute at a time — exactly the way the infection spreads — so a single pass through the queue gives the answer.

Count the fresh oranges up front; every time the BFS rots one, decrement the count. If any are left when the queue empties, they were unreachable.

```javascript
function orangesRotting(grid) {
  const rows = grid.length, cols = grid[0].length;
  const queue = [];
  let fresh = 0;
  for (let r = 0; r < rows; r++) {
    for (let c = 0; c < cols; c++) {
      if (grid[r][c] === 2) queue.push([r, c, 0]);
      else if (grid[r][c] === 1) fresh++;
    }
  }

  let minutes = 0;
  let head = 0;
  while (head < queue.length) {
    const [r, c, minute] = queue[head++];
    minutes = Math.max(minutes, minute);
    for (const [dr, dc] of [[1, 0], [-1, 0], [0, 1], [0, -1]]) {
      const nr = r + dr, nc = c + dc;
      if (nr >= 0 && nr < rows && nc >= 0 && nc < cols && grid[nr][nc] === 1) {
        grid[nr][nc] = 2;
        fresh--;
        queue.push([nr, nc, minute + 1]);
      }
    }
  }

  return fresh === 0 ? minutes : -1;
}
```

## Why it works

Seeding the queue with every rotten orange at minute 0 means the BFS explores in expanding "rings" of increasing minute count, matching how the real infection spreads simultaneously from all sources. Each cell is enqueued at most once — the moment it's marked rotten — so the final `minutes` is the largest minute stamp reached, and `fresh` reaching zero confirms every orange was infected rather than some being stranded behind empty cells.

## Complexity

- Time: O(rows * cols) — every cell is enqueued and processed at most once.
- Space: O(rows * cols) — the queue can hold every rotten cell at once.
