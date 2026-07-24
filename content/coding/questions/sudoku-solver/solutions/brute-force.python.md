Scan the board in row-major order for the first empty cell, then try digits `1`-`9` there. Before committing a digit, check its legality by re-scanning the whole row, the whole column, and the 3x3 box the cell belongs to. If a digit works, place it and recurse into the rest of the board; if the recursion later fails, undo the placement and try the next digit.

This is the most direct translation of the rules into code — no bookkeeping beyond the board itself, so it is the natural first draft in an interview before optimizing the validity check.

```python
def solve_sudoku(board):
    def is_valid(r, c, ch):
        for i in range(9):
            if board[r][i] == ch or board[i][c] == ch:
                return False
        br, bc = 3 * (r // 3), 3 * (c // 3)
        for i in range(br, br + 3):
            for j in range(bc, bc + 3):
                if board[i][j] == ch:
                    return False
        return True

    def backtrack():
        for r in range(9):
            for c in range(9):
                if board[r][c] == '.':
                    for ch in '123456789':
                        if is_valid(r, c, ch):
                            board[r][c] = ch
                            if backtrack():
                                return True
                            board[r][c] = '.'
                    return False
        return True

    backtrack()
    return board
```

## Why it works

`backtrack` always resolves the first empty cell it finds. For each candidate digit that passes `is_valid`, it commits the digit and recurses; a `True` bubbling up means every later cell was also filled successfully, so the whole board is done. If none of the nine digits lead to a full solution, the cell is reset to `.` and the function reports failure so the caller — the cell filled just before it — tries its next candidate. Because a solution is guaranteed to exist, this exhaustive trial-and-undo eventually reaches the unique completed grid.

## Complexity

- Time: O(9^k) worst case, where k is the number of empty cells — each one may try up to 9 digits before backtracking; every `is_valid` call rescans a fixed 9+9+9 cells, an added constant factor since the board size never changes.
- Space: O(k) for the recursion stack, at most 81 for a fully empty board.
