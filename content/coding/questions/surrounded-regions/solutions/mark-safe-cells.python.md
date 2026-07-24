Flip the question around: instead of asking "does this region touch the border?" for every cell, start from the border itself. Any `'O'` reachable from a border cell can never be captured, so flood fill outward from every border `'O'` and mark everything you reach with a placeholder like `'#'`. Whatever is still `'O'` afterward was never reachable from the border, so it gets flipped to `'X'` — and every `'#'` gets restored back to `'O'`.

Each cell is visited a constant number of times across the whole algorithm, so the redundant re-traversal from the brute-force approach disappears entirely.

```python
def solve(board):
    if not board or not board[0]:
        return
    m, n = len(board), len(board[0])

    def mark_safe(sr, sc):
        stack = [(sr, sc)]
        board[sr][sc] = '#'
        while stack:
            r, c = stack.pop()
            for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                nr, nc = r + dr, c + dc
                if 0 <= nr < m and 0 <= nc < n and board[nr][nc] == 'O':
                    board[nr][nc] = '#'
                    stack.append((nr, nc))

    for i in range(m):
        for j in (0, n - 1):
            if board[i][j] == 'O':
                mark_safe(i, j)
    for j in range(n):
        for i in (0, m - 1):
            if board[i][j] == 'O':
                mark_safe(i, j)

    for i in range(m):
        for j in range(n):
            if board[i][j] == 'O':
                board[i][j] = 'X'
            elif board[i][j] == '#':
                board[i][j] = 'O'
```

## Why it works

Any `'O'` connected to the border by a path of `'O'`s cannot be surrounded, so `mark_safe` floods outward from every border `'O'` and stamps `'#'` on the whole reachable set. After that pass, an `'O'` still standing had no path to any border cell, so it belongs to a captured region and is flipped to `'X'`; the `'#'` cells are restored to `'O'` since they were only a temporary marker.

## Complexity

- Time: O(m·n) — each cell is pushed onto the stack at most once across all flood fills.
- Space: O(m·n) — the stack can hold up to every cell in the worst case (one giant border-connected region).
