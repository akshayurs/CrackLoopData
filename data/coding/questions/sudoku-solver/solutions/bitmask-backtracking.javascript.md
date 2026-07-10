Re-scanning the row, column, and box on every trial digit repeats work that never changes between calls. Instead, keep three arrays of 9-bit masks — one per row, one per column, one per 3x3 box — where bit `d-1` records whether digit `d` is already used. Placing or removing a digit becomes a single OR/XOR, and checking whether a digit is available anywhere it matters becomes a single AND, so validity no longer depends on rescanning 27 cells.

It also helps to precompute the list of empty cells once and walk that list by index instead of re-scanning the board for "the next empty cell" at every recursive call.

```javascript
function solveSudoku(board) {
  const rows = new Array(9).fill(0);
  const cols = new Array(9).fill(0);
  const boxes = new Array(9).fill(0);
  const empties = [];

  for (let r = 0; r < 9; r++) {
    for (let c = 0; c < 9; c++) {
      if (board[r][c] === '.') {
        empties.push([r, c]);
      } else {
        const bit = 1 << (Number(board[r][c]) - 1);
        rows[r] |= bit;
        cols[c] |= bit;
        boxes[Math.floor(r / 3) * 3 + Math.floor(c / 3)] |= bit;
      }
    }
  }

  function backtrack(k) {
    if (k === empties.length) return true;
    const [r, c] = empties[k];
    const b = Math.floor(r / 3) * 3 + Math.floor(c / 3);
    const used = rows[r] | cols[c] | boxes[b];
    for (let d = 1; d <= 9; d++) {
      const bit = 1 << (d - 1);
      if (used & bit) continue;
      board[r][c] = String(d);
      rows[r] |= bit; cols[c] |= bit; boxes[b] |= bit;
      if (backtrack(k + 1)) return true;
      board[r][c] = '.';
      rows[r] ^= bit; cols[c] ^= bit; boxes[b] ^= bit;
    }
    return false;
  }

  backtrack(0);
  return board;
}
```

## Why it works

`used = rows[r] | cols[c] | boxes[b]` merges the three constraints touching cell `(r, c)` into one number in constant time; any bit still clear in `used` is a digit safe to place there right now. Placing digit `d` sets that bit in all three masks so later cells see the updated constraint immediately, and undoing a failed branch clears the same bit with XOR, restoring the exact state before the attempt. Walking the precomputed `empties` array by index instead of re-scanning the grid means every recursive call jumps straight to the next cell that actually needs a value.

## Complexity

- Time: O(9^k) worst case, where k is the number of empty cells — the branching factor is unchanged from brute force, but each validity check and update is O(1) bitwise work instead of an O(27) rescan, which cuts the constant factor sharply.
- Space: O(1) extra for the three fixed-size mask arrays, plus O(k) for the recursion stack and the `empties` array.
