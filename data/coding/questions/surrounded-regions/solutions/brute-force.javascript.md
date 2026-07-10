The direct reading of the problem: an `'O'` survives only if its connected region touches the border. So for every `'O'` cell, run an independent flood fill from that single cell and check whether it ever reaches row 0, the last row, column 0, or the last column. If it never does, that cell gets flipped.

This is wasteful — cells in the same region repeat almost the same traversal from different starting points — but it is the honest first pass before noticing the traversals can be shared.

```javascript
function solve(board) {
  if (!board || !board.length || !board[0].length) return;
  const m = board.length, n = board[0].length;

  function touchesBorder(sr, sc) {
    const stack = [[sr, sc]];
    const seen = new Set([`${sr},${sc}`]);
    let touches = false;
    while (stack.length) {
      const [r, c] = stack.pop();
      if (r === 0 || r === m - 1 || c === 0 || c === n - 1) touches = true;
      for (const [dr, dc] of [[1, 0], [-1, 0], [0, 1], [0, -1]]) {
        const nr = r + dr, nc = c + dc;
        const key = `${nr},${nc}`;
        if (nr >= 0 && nr < m && nc >= 0 && nc < n && board[nr][nc] === 'O' && !seen.has(key)) {
          seen.add(key);
          stack.push([nr, nc]);
        }
      }
    }
    return touches;
  }

  const toFlip = [];
  for (let i = 0; i < m; i++) {
    for (let j = 0; j < n; j++) {
      if (board[i][j] === 'O' && !touchesBorder(i, j)) toFlip.push([i, j]);
    }
  }

  for (const [i, j] of toFlip) board[i][j] = 'X';
}
```

## Why it works

`touchesBorder` explores the full connected region reachable from `(sr, sc)` and reports whether any cell in it lies on an edge of the board. Collecting flips into `toFlip` before mutating avoids changing `board` mid-scan, which would corrupt later flood fills. Since every `'O'` in a captured region individually fails the border check, all of them end up in `toFlip` and get turned to `'X'`.

## Complexity

- Time: O((m·n)²) — in the worst case every `'O'` cell re-explores an entire region of size O(m·n).
- Space: O(m·n) — the stack and `seen` set for a single flood fill.
