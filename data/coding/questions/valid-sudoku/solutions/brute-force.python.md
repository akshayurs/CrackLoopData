The three rules are independent, so the most direct approach is to check them one at a time: sweep the nine rows, then the nine columns, then the nine boxes. Each group is a collection of nine cells, and a group is legal exactly when its filled digits are all distinct.

Reduce every group to "does this list of digits contain a duplicate?" — drop the dots, then compare the count of digits against the count of *distinct* digits. If they ever differ, the board is invalid.

```python
def is_valid_sudoku(board):
    def group_ok(cells):
        digits = [c for c in cells if c != "."]
        return len(digits) == len(set(digits))

    for r in range(9):
        if not group_ok(board[r]):
            return False
    for c in range(9):
        if not group_ok([board[r][c] for r in range(9)]):
            return False
    for br in range(0, 9, 3):
        for bc in range(0, 9, 3):
            box = [board[br + i][bc + j] for i in range(3) for j in range(3)]
            if not group_ok(box):
                return False
    return True
```

## Why it works

A Sudoku filling is valid iff none of the 27 groups (9 rows + 9 columns + 9 boxes) repeats a digit. `group_ok` collects the non-empty cells of one group and reports whether they are all unique. Because the three sweeps together visit exactly these 27 groups, passing all of them certifies the whole board; the first offending group short-circuits to `False`.

## Complexity

For an `N×N` board (here `N = 9`):

- Time: O(N²) — each of the three sweeps touches all N² cells once.
- Space: O(N) — one temporary group of at most N digits exists at a time.
