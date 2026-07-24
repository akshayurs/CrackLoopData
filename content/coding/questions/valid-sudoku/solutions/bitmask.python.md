Each group only ever needs to answer one question about a digit: "have I seen you before?" Since there are just nine possible digits, that membership set fits in nine bits of a single integer — bit `d-1` is set once digit `d` has appeared. This replaces every hash set with one small integer.

Keep one integer per row, column, and box. For a digit `v`, form `bit = 1 << (v - 1)`; if that bit is already lit in any of the three masks, the digit repeats. Otherwise OR it into all three. One pass, and no hashing at all.

```python
def is_valid_sudoku(board):
    rows = [0] * 9
    cols = [0] * 9
    boxes = [0] * 9
    for r in range(9):
        for c in range(9):
            v = board[r][c]
            if v == ".":
                continue
            bit = 1 << (int(v) - 1)
            b = (r // 3) * 3 + c // 3
            if rows[r] & bit or cols[c] & bit or boxes[b] & bit:
                return False
            rows[r] |= bit
            cols[c] |= bit
            boxes[b] |= bit
    return True
```

## Why it works

A set of digits and a 9-bit mask are the same information: testing `mask & bit` is the membership check, and `mask |= bit` is the insertion. Because each mask tracks exactly one group and the AND test runs before the OR update, a digit that already occurs in its row, column, or box is caught immediately. Surviving all 81 cells means no group ever lit the same bit twice.

## Complexity

For an `N×N` board (here `N = 9`):

- Time: O(N²) — one pass over the N² cells with O(1) bit operations each.
- Space: O(N) — three arrays of N integers, independent of how many cells are filled.
