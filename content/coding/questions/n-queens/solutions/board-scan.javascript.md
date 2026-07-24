Place queens one row at a time. Before dropping a queen into a cell, scan every queen already placed in earlier rows and reject the cell if it shares a column or either diagonal. This is the most literal reading of the rules — no bookkeeping beyond the board itself.

Once a row is filled successfully all the way to the last row, the current board is a valid layout; snapshot it and keep backtracking to find the rest.

```javascript
function solveNQueens(n) {
  const results = [];
  const board = Array.from({ length: n }, () => Array(n).fill("."));

  function isSafe(row, col) {
    for (let r = 0; r < row; r++) {
      const c = board[r].indexOf("Q");
      if (c === col || Math.abs(c - col) === row - r) return false;
    }
    return true;
  }

  function place(row) {
    if (row === n) {
      results.push(board.map((r) => r.join("")));
      return;
    }
    for (let col = 0; col < n; col++) {
      if (isSafe(row, col)) {
        board[row][col] = "Q";
        place(row + 1);
        board[row][col] = ".";
      }
    }
  }

  place(0);
  return results;
}
```

## Why it works

`isSafe` re-derives every earlier queen's column with `indexOf("Q")` and checks it against the candidate column and both diagonals (`Math.abs(c - col) === row - r` catches both diagonal directions at once). Backtracking undoes a placement the moment a row is finished exploring, so every combination of columns is tried and only fully safe boards are recorded — in row-major, left-to-right column order.

## Complexity

- Time: O(n! * n) — roughly n! placements are attempted, and each safety check rescans up to n earlier rows.
- Space: O(n^2) — the board plus recursion depth up to n.
