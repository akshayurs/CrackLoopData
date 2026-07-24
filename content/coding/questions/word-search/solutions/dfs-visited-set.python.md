Try every starting cell and, from there, walk the board one letter at a time, only stepping to a neighbor that matches the next character of `word`. A `visited` set keeps the current path from stepping on a cell twice; removing a cell from the set when a branch fails is what makes this backtracking rather than a plain walk.

This is the direct translation of the problem statement into code — no attempt yet to prune the search or avoid the extra memory the set costs.

```python
def exist(board, word):
    rows, cols = len(board), len(board[0])
    visited = set()

    def dfs(r, c, i):
        if i == len(word):
            return True
        if r < 0 or r >= rows or c < 0 or c >= cols:
            return False
        if (r, c) in visited or board[r][c] != word[i]:
            return False
        visited.add((r, c))
        found = (dfs(r + 1, c, i + 1) or dfs(r - 1, c, i + 1) or
                 dfs(r, c + 1, i + 1) or dfs(r, c - 1, i + 1))
        visited.remove((r, c))
        return found

    for r in range(rows):
        for c in range(cols):
            if dfs(r, c, 0):
                return True
    return False
```

## Why it works

`dfs(r, c, i)` succeeds if the board can spell `word[i:]` starting at `(r, c)`. It checks bounds and the current letter, then tries all four neighbors for the next character. Adding `(r, c)` to `visited` before recursing stops the path from doubling back on itself; removing it right after the recursive calls return is the backtrack step, restoring the cell so a *different* path — one that never visited it — can still use it. Trying every cell as a start covers every possible trace.

## Complexity

- Time: O(m · n · 4^L) — up to m·n starting cells, each exploring up to 4 directions per one of L letters.
- Space: O(L) — the visited set and the recursion stack each hold at most one entry per letter of the current path.
