Rescanning the board for every candidate cell is wasted work — a column or diagonal is either occupied or it isn't, and that fact doesn't change until you place or remove a queen. Track it directly: one set for used columns, and one set each for the two diagonal families. A cell on diagonal `row - col` (constant along a "\" diagonal) or `row + col` (constant along a "/" diagonal) is under attack the instant either value is already taken.

Placing a queen becomes three set insertions; checking a cell becomes three O(1) membership tests, so the search itself is still exponential but each step is now constant time instead of linear.

```python
def solve_n_queens(n):
    results = []
    cols, diag1, diag2 = set(), set(), set()
    board = [["."] * n for _ in range(n)]

    def place(row):
        if row == n:
            results.append(["".join(r) for r in board])
            return
        for col in range(n):
            if col in cols or (row - col) in diag1 or (row + col) in diag2:
                continue
            cols.add(col); diag1.add(row - col); diag2.add(row + col)
            board[row][col] = "Q"
            place(row + 1)
            board[row][col] = "."
            cols.remove(col); diag1.remove(row - col); diag2.remove(row + col)

    place(0)
    return results
```

## Why it works

Every queen occupies a unique row by construction (one queen is placed per recursive call), so only columns and diagonals need guarding. `row - col` is invariant for every cell on the same downward diagonal and `row + col` for every cell on the same upward diagonal, so membership in `diag1`/`diag2` is exactly the "already attacked diagonally" test. Adding to the sets on placement and removing them on backtrack keeps the sets in sync with the current partial board, and the row-major, left-to-right column order is unchanged from the naive version.

## Complexity

- Time: O(n!) — the same search tree as the brute-force version, but each visit is O(1) instead of O(n).
- Space: O(n) — the three sets and recursion depth are each bounded by n.
