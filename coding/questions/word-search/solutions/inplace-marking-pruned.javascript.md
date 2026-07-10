Drop the separate `visited` set entirely — mark the current cell by overwriting it with a sentinel character while it is part of the path, then restore the original letter on the way back out. That removes an O(L) hash set and its lookups without changing what gets explored.

Before searching at all, count the letters in `word` and in `board`. If `word` needs more of some letter than the board has, no trace can possibly exist, so the search is skipped entirely — a cheap check that rejects many impossible cases in O(m·n) instead of paying for a failed DFS.

```javascript
function exist(board, word) {
  const rows = board.length;
  const cols = board[0].length;

  const boardCounts = new Map();
  for (const row of board) {
    for (const ch of row) boardCounts.set(ch, (boardCounts.get(ch) || 0) + 1);
  }
  const wordCounts = new Map();
  for (const ch of word) wordCounts.set(ch, (wordCounts.get(ch) || 0) + 1);
  for (const [ch, need] of wordCounts) {
    if (need > (boardCounts.get(ch) || 0)) return false;
  }

  function dfs(r, c, i) {
    if (i === word.length) return true;
    if (r < 0 || r >= rows || c < 0 || c >= cols || board[r][c] !== word[i]) return false;

    const original = board[r][c];
    board[r][c] = "#";
    const found =
      dfs(r + 1, c, i + 1) || dfs(r - 1, c, i + 1) ||
      dfs(r, c + 1, i + 1) || dfs(r, c - 1, i + 1);
    board[r][c] = original;
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

Overwriting `board[r][c]` with `"#"` — a value that can never equal a letter of `word` — is equivalent to marking it visited, since the very next comparison in `dfs` rejects that cell for the rest of the current path. Restoring the original letter after the recursive calls return is the backtrack step, so sibling branches and later starting cells see the untouched board. The letter-count check is a necessary condition for a trace to exist: skipping the DFS whenever it fails costs O(m·n) instead of the full search, while never rejecting a board that does contain a valid trace.

## Complexity

- Time: O(m · n · 4^L) worst case (O(m · n · 3^(L-1)) in practice, since the cell just entered from can't be revisited) — the frequency check adds only O(m · n + L).
- Space: O(L) — recursion depth only; the board is mutated in place instead of allocating a visited structure.
