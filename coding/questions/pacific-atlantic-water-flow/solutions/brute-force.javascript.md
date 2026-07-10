The direct reading of the problem: for every single cell, simulate where its water can go. Run a DFS from that cell following only downhill-or-equal moves, and check whether the reachable set ever touches the top/left border (Pacific) and separately whether it touches the bottom/right border (Atlantic).

This retraces huge amounts of shared ground — cells near the middle of the grid get re-explored once per starting cell — but it mirrors the problem statement almost line for line, which makes it a solid first answer before optimizing.

```javascript
function pacificAtlantic(heights) {
  if (!heights.length || !heights[0].length) return [];
  const m = heights.length, n = heights[0].length;

  function reaches(sr, sc, isTarget) {
    const seen = new Set([sr * n + sc]);
    const stack = [[sr, sc]];
    let touched = isTarget(sr, sc);
    while (stack.length) {
      const [r, c] = stack.pop();
      for (const [dr, dc] of [[1, 0], [-1, 0], [0, 1], [0, -1]]) {
        const nr = r + dr, nc = c + dc, key = nr * n + nc;
        if (nr >= 0 && nr < m && nc >= 0 && nc < n && !seen.has(key) &&
            heights[nr][nc] <= heights[r][c]) {
          seen.add(key);
          stack.push([nr, nc]);
          touched = touched || isTarget(nr, nc);
        }
      }
    }
    return touched;
  }

  const pacific = (r, c) => r === 0 || c === 0;
  const atlantic = (r, c) => r === m - 1 || c === n - 1;

  const result = [];
  for (let r = 0; r < m; r++) {
    for (let c = 0; c < n; c++) {
      if (reaches(r, c, pacific) && reaches(r, c, atlantic)) {
        result.push([r, c]);
      }
    }
  }
  return result;
}
```

## Why it works

Each DFS from a cell visits exactly the set of cells reachable by non-increasing steps, which is precisely the water-flow rule in the problem. A cell qualifies once its own reachable set includes at least one Pacific-border cell and at least one Atlantic-border cell — including itself. Iterating cells in row-major order keeps the output naturally sorted.

## Complexity

- Time: O(m^2 * n^2) — a DFS over up to m*n cells is run from every one of the m*n starting cells.
- Space: O(m * n) — the visited set and stack for a single DFS.
