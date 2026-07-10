Each group only ever needs to answer one question about a digit: "have I seen you before?" Since there are just nine possible digits, that membership set fits in nine bits of a single integer — bit `d-1` is set once digit `d` has appeared. This replaces every `Set` with one small number.

Keep one integer per row, column, and box. For a digit `v`, form `bit = 1 << (Number(v) - 1)`; if that bit is already lit in any of the three masks, the digit repeats. Otherwise OR it into all three. One pass, and no hashing at all.

```javascript
function isValidSudoku(board) {
  const rows = new Array(9).fill(0);
  const cols = new Array(9).fill(0);
  const boxes = new Array(9).fill(0);
  for (let r = 0; r < 9; r++) {
    for (let c = 0; c < 9; c++) {
      const v = board[r][c];
      if (v === ".") continue;
      const bit = 1 << (Number(v) - 1);
      const b = Math.floor(r / 3) * 3 + Math.floor(c / 3);
      if (rows[r] & bit || cols[c] & bit || boxes[b] & bit) return false;
      rows[r] |= bit;
      cols[c] |= bit;
      boxes[b] |= bit;
    }
  }
  return true;
}
```

## Why it works

A set of digits and a 9-bit mask are the same information: testing `mask & bit` is the membership check, and `mask |= bit` is the insertion. Because each mask tracks exactly one group and the AND test runs before the OR update, a digit that already occurs in its row, column, or box is caught immediately. Surviving all 81 cells means no group ever lit the same bit twice.

## Complexity

For an `N×N` board (here `N = 9`):

- Time: O(N²) — one pass over the N² cells with O(1) bit operations each.
- Space: O(N) — three arrays of N integers, independent of how many cells are filled.
