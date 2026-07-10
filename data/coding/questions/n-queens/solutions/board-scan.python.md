Place queens one row at a time. Before dropping a queen into a cell, scan every queen already placed in earlier rows and reject the cell if it shares a column or either diagonal. This is the most literal reading of the rules — no bookkeeping beyond the board itself.

Once a row is filled successfully all the way to the last row, the current board is a valid layout; record a copy of it and keep backtracking to find the rest.

```python
def solve_n_queens(n):
    results = []
    board = [["."] * n for _ in range(n)]

    def is_safe(row, col):
        for r in range(row):
            c = board[r].index("Q")
            if c == col or abs(c - col) == row - r:
                return False
        return True

    def place(row):
        if row == n:
            results.append(["".join(r) for r in board])
            return
        for col in range(n):
            if is_safe(row, col):
                board[row][col] = "Q"
                place(row + 1)
                board[row][col] = "."

    place(0)
    return results
```

## Why it works

`is_safe` re-derives every earlier queen's column with `index("Q")` and checks it against the candidate column and both diagonals (`abs(c - col) == row - r` catches both diagonal directions at once). Backtracking undoes a placement the moment a row is finished exploring, so every combination of columns is tried and only fully safe boards are recorded — in row-major, left-to-right column order.

## Complexity

- Time: O(n! * n) — roughly n! placements are attempted, and each safety check rescans up to n earlier rows.
- Space: O(n^2) — the board plus recursion depth up to n.
