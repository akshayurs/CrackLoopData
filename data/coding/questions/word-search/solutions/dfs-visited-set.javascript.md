Try every starting cell and, from there, walk the board one letter at a time, only stepping to a neighbor that matches the next character of `word`. A `visited` set keeps the current path from stepping on a cell twice; removing a cell from the set when a branch fails is what makes this backtracking rather than a plain walk.

This is the direct translation of the problem statement into code — no attempt yet to prune the search or avoid the extra memory the set costs.

```javascript
function exist(board, word) {
  const rows = board.length;
  const cols = board[0].length;
  const visited = new Set();

  function dfs(r, c, i) {
    if (i === word.length) return true;
    if (r < 0 || r >= rows || c < 0 || c >= cols) return false;
    const key = r * cols + c;
    if (visited.has(key) || board[r][c] !== word[i]) return false;

    visited.add(key);
    const found =
      dfs(r + 1, c, i + 1) || dfs(r - 1, c, i + 1) ||
      dfs(r, c + 1, i + 1) || dfs(r, c - 1, i + 1);
    visited.delete(key);
    return found;
  }

  for (let r = 0; r < rows; r++) {
    for (let c = 0; c < cols; c++) {
      if (dfs(r, c, 0)) return true;
    }
  }
  return false;
}
```

## Why it works

`dfs(r, c, i)` succeeds if the board can spell `word.slice(i)` starting at `(r, c)`. It checks bounds and the current letter, then tries all four neighbors for the next character. Adding the cell's key to `visited` before recursing stops the path from doubling back on itself; deleting it right after the recursive calls return is the backtrack step, restoring the cell so a *different* path — one that never visited it — can still use it. Trying every cell as a start covers every possible trace.

## Complexity

- Time: O(m · n · 4^L) — up to m·n starting cells, each exploring up to 4 directions per one of L letters.
- Space: O(L) — the visited set and the recursion stack each hold at most one entry per letter of the current path.
