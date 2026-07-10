The most direct reading of the problem: simulate the minutes one at a time. On each minute, scan the whole grid, mark every fresh orange that touches a rotten one, then flip all of those marks to rotten at once — never rot mid-scan, or a fresh orange could rot twice in the same minute.

Keep going until a scan finds no fresh oranges left (done) or a scan finds fresh oranges but rots none of them (stuck forever).

```javascript
function orangesRotting(grid) {
  const rows = grid.length, cols = grid[0].length;
  let minutes = 0;
  while (true) {
    let freshLeft = false;
    const toRot = [];
    for (let r = 0; r < rows; r++) {
      for (let c = 0; c < cols; c++) {
        if (grid[r][c] === 1) {
          freshLeft = true;
          for (const [dr, dc] of [[1, 0], [-1, 0], [0, 1], [0, -1]]) {
            const nr = r + dr, nc = c + dc;
            if (nr >= 0 && nr < rows && nc >= 0 && nc < cols && grid[nr][nc] === 2) {
              toRot.push([r, c]);
              break;
            }
          }
        }
      }
    }
    if (!freshLeft) return minutes;
    if (toRot.length === 0) return -1;
    for (const [r, c] of toRot) grid[r][c] = 2;
    minutes++;
  }
}
```

## Why it works

Each full pass over the grid corresponds to exactly one minute, because `toRot` is collected first and applied only after the scan finishes — so newly-rotted cells never infect a neighbor within the same minute. The loop terminates either when no fresh orange remains (`freshLeft` is `false`) or when a pass changes nothing (`toRot` is empty), which means the remaining fresh oranges are unreachable.

## Complexity

- Time: O((rows * cols)²) — up to `rows * cols` minutes may be needed, and each minute rescans the whole grid.
- Space: O(rows * cols) — for the `toRot` array built each minute.
