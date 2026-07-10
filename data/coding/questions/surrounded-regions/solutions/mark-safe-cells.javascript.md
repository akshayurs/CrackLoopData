Flip the question around: instead of asking "does this region touch the border?" for every cell, start from the border itself. Any `'O'` reachable from a border cell can never be captured, so flood fill outward from every border `'O'` and mark everything you reach with a placeholder like `'#'`. Whatever is still `'O'` afterward was never reachable from the border, so it gets flipped to `'X'` — and every `'#'` gets restored back to `'O'`.

Each cell is visited a constant number of times across the whole algorithm, so the redundant re-traversal from the brute-force approach disappears entirely.

```javascript
function solve(board) {
  if (!board || !board.length || !board[0].length) return;
  const m = board.length, n = board[0].length;

  function markSafe(sr, sc) {
    const stack = [[sr, sc]];
    board[sr][sc] = '#';
    while (stack.length) {
      const [r, c] = stack.pop();
      for (const [dr, dc] of [[1, 0], [-1, 0], [0, 1], [0, -1]]) {
        const nr = r + dr, nc = c + dc;
        if (nr >= 0 && nr < m && nc >= 0 && nc < n && board[nr][nc] === 'O') {
          board[nr][nc] = '#';
          stack.push([nr, nc]);
        }
      }
    }
  }

  for (let i = 0; i < m; i++) {
    for (const j of [0, n - 1]) {
      if (board[i][j] === 'O') markSafe(i, j);
    }
  }
  for (let j = 0; j < n; j++) {
    for (const i of [0, m - 1]) {
      if (board[i][j] === 'O') markSafe(i, j);
    }
  }

  for (let i = 0; i < m; i++) {
    for (let j = 0; j < n; j++) {
      if (board[i][j] === 'O') board[i][j] = 'X';
      else if (board[i][j] === '#') board[i][j] = 'O';
    }
  }
}
```

## Why it works

Any `'O'` connected to the border by a path of `'O'`s cannot be surrounded, so `markSafe` floods outward from every border `'O'` and stamps `'#'` on the whole reachable set. After that pass, an `'O'` still standing had no path to any border cell, so it belongs to a captured region and is flipped to `'X'`; the `'#'` cells are restored to `'O'` since they were only a temporary marker.

## Complexity

- Time: O(m·n) — each cell is pushed onto the stack at most once across all flood fills.
- Space: O(m·n) — the stack can hold up to every cell in the worst case (one giant border-connected region).
