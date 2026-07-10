Flip the direction of the search. Instead of asking "where can water starting at cell X go?" for every cell, start from the oceans and ask "which cells could have sent water here?" Water flows downhill-or-equal, so walking backward from a border means moving to a neighbor whose height is greater than or equal to the current one.

Seed a BFS with every Pacific-border cell at once, and a separate BFS with every Atlantic-border cell at once. Each visits, in a single O(m*n) sweep, exactly the set of cells that can reach that ocean. The answer is the intersection of the two sets — no cell is ever re-explored across different starting points.

```javascript
function pacificAtlantic(heights) {
  if (!heights.length || !heights[0].length) return [];
  const m = heights.length, n = heights[0].length;

  function bfs(starts) {
    const seen = new Set(starts.map(([r, c]) => r * n + c));
    const queue = [...starts];
    let head = 0;
    while (head < queue.length) {
      const [r, c] = queue[head++];
      for (const [dr, dc] of [[1, 0], [-1, 0], [0, 1], [0, -1]]) {
        const nr = r + dr, nc = c + dc, key = nr * n + nc;
        if (nr >= 0 && nr < m && nc >= 0 && nc < n && !seen.has(key) &&
            heights[nr][nc] >= heights[r][c]) {
          seen.add(key);
          queue.push([nr, nc]);
        }
      }
    }
    return seen;
  }

  const pacificStarts = [];
  const atlanticStarts = [];
  for (let c = 0; c < n; c++) {
    pacificStarts.push([0, c]);
    atlanticStarts.push([m - 1, c]);
  }
  for (let r = 0; r < m; r++) {
    pacificStarts.push([r, 0]);
    atlanticStarts.push([r, n - 1]);
  }

  const pacific = bfs(pacificStarts);
  const atlantic = bfs(atlanticStarts);

  const result = [];
  for (let r = 0; r < m; r++) {
    for (let c = 0; c < n; c++) {
      const key = r * n + c;
      if (pacific.has(key) && atlantic.has(key)) result.push([r, c]);
    }
  }
  return result;
}
```

## Why it works

Reversing the flow condition (`>=` instead of `<=`) turns "can this cell send water to the ocean" into "can the ocean's backward search reach this cell," and the two are equivalent by symmetry of the adjacency relation. Since each BFS explores every cell at most once, running it from all border cells simultaneously still costs one pass over the grid instead of one pass per cell. Building the result by scanning rows then columns keeps it sorted without a separate sort step.

## Complexity

- Time: O(m * n) — each of the two BFS traversals visits every cell and edge at most once.
- Space: O(m * n) — the two visited sets and BFS queues.
