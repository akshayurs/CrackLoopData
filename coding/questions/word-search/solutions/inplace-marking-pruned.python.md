Drop the separate `visited` set entirely — mark the current cell by overwriting it with a sentinel character while it is part of the path, then restore the original letter on the way back out. That removes an O(L) hash set and its lookups without changing what gets explored.

Before searching at all, count the letters in `word` and in `board`. If `word` needs more of some letter than the board has, no trace can possibly exist, so the search is skipped entirely — a cheap check that rejects many impossible cases in O(m·n) instead of paying for a failed DFS.

```python
from collections import Counter

def exist(board, word):
    rows, cols = len(board), len(board[0])

    board_counts = Counter(ch for row in board for ch in row)
    word_counts = Counter(word)
    if any(word_counts[ch] > board_counts.get(ch, 0) for ch in word_counts):
        return False

    def dfs(r, c, i):
        if i == len(word):
            return True
        if r < 0 or r >= rows or c < 0 or c >= cols or board[r][c] != word[i]:
            return False

        original = board[r][c]
        board[r][c] = "#"
        found = (dfs(r + 1, c, i + 1) or dfs(r - 1, c, i + 1) or
                 dfs(r, c + 1, i + 1) or dfs(r, c - 1, i + 1))
        board[r][c] = original
        return found

    for r in range(rows):
        for c in range(cols):
            if dfs(r, c, 0):
                return True
    return False
```

## Why it works

Overwriting `board[r][c]` with `"#"` — a value that can never equal a letter of `word` — is equivalent to marking it visited, since the very next comparison in `dfs` rejects that cell for the rest of the current path. Restoring the original letter after the recursive calls return is the backtrack step, so sibling branches and later starting cells see the untouched board. The letter-count check is a necessary condition for a trace to exist: skipping the DFS whenever it fails costs O(m·n) instead of the full search, while never rejecting a board that does contain a valid trace.

## Complexity

- Time: O(m · n · 4^L) worst case (O(m · n · 3^(L-1)) in practice, since the cell just entered from can't be revisited) — the frequency check adds only O(m · n + L).
- Space: O(L) — recursion depth only; the board is mutated in place instead of allocating a visited structure.
