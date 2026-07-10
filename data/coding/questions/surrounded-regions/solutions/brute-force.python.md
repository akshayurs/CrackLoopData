The direct reading of the problem: an `'O'` survives only if its connected region touches the border. So for every `'O'` cell, run an independent flood fill from that single cell and check whether it ever reaches row 0, the last row, column 0, or the last column. If it never does, that cell gets flipped.

This is wasteful — cells in the same region repeat almost the same traversal from different starting points — but it is the honest first pass before noticing the traversals can be shared.

```python
def solve(board):
    if not board or not board[0]:
        return
    m, n = len(board), len(board[0])

    def touches_border(sr, sc):
        stack, seen = [(sr, sc)], {(sr, sc)}
        touches = False
        while stack:
            r, c = stack.pop()
            if r == 0 or r == m - 1 or c == 0 or c == n - 1:
                touches = True
            for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                nr, nc = r + dr, c + dc
                if 0 <= nr < m and 0 <= nc < n and board[nr][nc] == 'O' and (nr, nc) not in seen:
                    seen.add((nr, nc))
                    stack.append((nr, nc))
        return touches

    to_flip = []
    for i in range(m):
        for j in range(n):
            if board[i][j] == 'O' and not touches_border(i, j):
                to_flip.append((i, j))

    for i, j in to_flip:
        board[i][j] = 'X'
```

## Why it works

`touches_border` explores the full connected region reachable from `(sr, sc)` and reports whether any cell in it lies on an edge of the board. Collecting flips into `to_flip` before mutating avoids changing `board` mid-scan, which would corrupt later flood fills. Since every `'O'` in a captured region individually fails the border check, all of them end up in `to_flip` and get turned to `'X'`.

## Complexity

- Time: O((m·n)²) — in the worst case every `'O'` cell re-explores an entire region of size O(m·n).
- Space: O(m·n) — the stack and `seen` set for a single flood fill.
