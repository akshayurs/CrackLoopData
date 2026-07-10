The three rules are independent, so the most direct approach is to check them one at a time: sweep the nine rows, then the nine columns, then the nine boxes. Each group is a collection of nine cells, and a group is legal exactly when its filled digits are all distinct.

Reduce every group to "does this list of digits contain a duplicate?" — drop the dots, then compare the number of digits against the size of a `Set` built from them. If they ever differ, the board is invalid.

```javascript
function isValidSudoku(board) {
  const groupOk = (cells) => {
    const digits = cells.filter((c) => c !== ".");
    return new Set(digits).size === digits.length;
  };

  for (let r = 0; r < 9; r++) {
    if (!groupOk(board[r])) return false;
  }
  for (let c = 0; c < 9; c++) {
    const col = [];
    for (let r = 0; r < 9; r++) col.push(board[r][c]);
    if (!groupOk(col)) return false;
  }
  for (let br = 0; br < 9; br += 3) {
    for (let bc = 0; bc < 9; bc += 3) {
      const box = [];
      for (let i = 0; i < 3; i++)
        for (let j = 0; j < 3; j++) box.push(board[br + i][bc + j]);
      if (!groupOk(box)) return false;
    }
  }
  return true;
}
```

## Why it works

A Sudoku filling is valid iff none of the 27 groups (9 rows + 9 columns + 9 boxes) repeats a digit. `groupOk` gathers the non-empty cells of one group and reports whether they are all unique. The three sweeps together cover exactly these 27 groups, so passing every one certifies the whole board; the first bad group returns `false` immediately.

## Complexity

For an `N×N` board (here `N = 9`):

- Time: O(N²) — each of the three sweeps touches all N² cells once.
- Space: O(N) — one temporary group of at most N digits exists at a time.
