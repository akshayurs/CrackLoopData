Instead of revisiting the grid three times, notice that every filled cell belongs to exactly one row, one column, and one box — and its box index is fully determined by its coordinates as `(r // 3) * 3 + c // 3`. So a single scan can update all three memberships at once.

Keep nine sets for rows, nine for columns, and nine for boxes. When a digit lands, check whether it already lives in its row's, column's, or box's set; if any says yes, we have found a repeat and can stop. Otherwise record it in all three.

```python
def is_valid_sudoku(board):
    rows = [set() for _ in range(9)]
    cols = [set() for _ in range(9)]
    boxes = [set() for _ in range(9)]
    for r in range(9):
        for c in range(9):
            v = board[r][c]
            if v == ".":
                continue
            b = (r // 3) * 3 + c // 3
            if v in rows[r] or v in cols[c] or v in boxes[b]:
                return False
            rows[r].add(v)
            cols[c].add(v)
            boxes[b].add(v)
    return True
```

## Why it works

The box formula maps each cell to the index of the 3×3 block that contains it, so `boxes[b]` accumulates exactly the digits of that block. A conflict in *any* of the three rules shows up the moment the offending digit is placed, because its partner was recorded earlier in the same scan. Reaching the end with no conflict means all 27 groups stayed duplicate-free.

## Complexity

For an `N×N` board (here `N = 9`):

- Time: O(N²) — one pass over the N² cells, each doing O(1) set work.
- Space: O(N²) — the row, column, and box sets together retain every filled digit.
