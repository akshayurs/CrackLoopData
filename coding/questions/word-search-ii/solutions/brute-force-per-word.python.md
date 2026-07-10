The direct reading of the problem: treat each word independently. For every word, scan every cell of the board as a possible starting point and run a backtracking DFS that follows the word letter by letter through neighboring cells, marking a cell visited while it's part of the current path and unmarking it on the way back out.

This is exactly "Word Search I" repeated once per word, so it never shares work between words — the same board region gets re-explored from scratch for every entry in the list.

```python
def find_words(board, words):
    if not board or not board[0]:
        return []
    rows, cols = len(board), len(board[0])

    def exists(word):
        def dfs(r, c, i):
            if i == len(word):
                return True
            if r < 0 or r >= rows or c < 0 or c >= cols or board[r][c] != word[i]:
                return False
            tmp, board[r][c] = board[r][c], "*"
            found = (dfs(r + 1, c, i + 1) or dfs(r - 1, c, i + 1) or
                     dfs(r, c + 1, i + 1) or dfs(r, c - 1, i + 1))
            board[r][c] = tmp
            return found

        return any(dfs(r, c, 0) for r in range(rows) for c in range(cols))

    return sorted(word for word in words if exists(word))
```

## Why it works

`dfs` walks the word index by index, only stepping to a neighbor whose letter matches the next required character and refusing to step onto a cell already used in the current path (marked `"*"`). Restoring the cell after exploring each direction lets the same cell be reused by a different starting point or a different word. A word is kept only if some starting cell leads to a complete match; results are sorted so the output is deterministic regardless of `words` order.

## Complexity

- Time: O(W · m · n · 4^L) — for each of the W words, every cell can start a search that branches up to 4 ways per letter of length L.
- Space: O(L) — recursion depth is bounded by the word length (board mutation is in place).
