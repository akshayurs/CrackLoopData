Place queens one row at a time. Before dropping a queen into a column, scan every queen placed in earlier rows and reject the spot if it shares a column or lies on either diagonal (row and column offsets are equal in magnitude). If a full board is completed, that's one valid arrangement.

This is the natural first attempt: no clever bookkeeping, just an explicit safety check against the queens already on the board.

```python
def count_queens(n):
    def is_safe(cols, row):
        col = row
        for r, c in enumerate(cols):
            if c == col or abs(c - col) == abs(r - len(cols)):
                return False
        return True

    def backtrack(cols):
        if len(cols) == n:
            return 1
        total = 0
        for col in range(n):
            if is_safe(cols, col):
                cols.append(col)
                total += backtrack(cols)
                cols.pop()
        return total

    return backtrack([])
```

## Why it works

`cols[r]` records the column of the queen in row `r`. For a candidate column at the next row, `is_safe` rejects it if some earlier queen shares that column (`c == col`) or sits on a diagonal (the row gap equals the column gap). Trying every column at every row and recursing only on safe choices, then undoing the choice on the way back (`cols.pop()`), explores every legal partial placement exactly once and counts the ones that fill all `n` rows.

## Complexity

- Time: O(n! · n) — roughly n! candidate placements are explored, and each safety check scans up to n previously placed queens.
- Space: O(n) — the recursion depth and the `cols` list both hold at most n entries.
