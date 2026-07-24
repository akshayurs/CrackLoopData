Scan the board in row-major order for the first empty cell, then try digits `1`-`9` there. Before committing a digit, check its legality by re-scanning the whole row, the whole column, and the 3x3 box the cell belongs to. If a digit works, place it and recurse into the rest of the board; if the recursion later fails, undo the placement and try the next digit.

This is the most direct translation of the rules into code — no bookkeeping beyond the board itself, so it is the natural first draft in an interview before optimizing the validity check.

```javascript
function solveSudoku(board) {
  function isValid(r, c, ch) {
    for (let i = 0; i < 9; i++) {
      if (board[r][i] === ch || board[i][c] === ch) return false;
    }
    const br = 3 * Math.floor(r / 3), bc = 3 * Math.floor(c / 3);
    for (let i = br; i < br + 3; i++) {
      for (let j = bc; j < bc + 3; j++) {
        if (board[i][j] === ch) return false;
      }
    }
    return true;
  }

  function backtrack() {
    for (let r = 0; r < 9; r++) {
      for (let c = 0; c < 9; c++) {
        if (board[r][c] === '.') {
          for (const ch of '123456789') {
            if (isValid(r, c, ch)) {
              board[r][c] = ch;
              if (backtrack()) return true;
              board[r][c] = '.';
            }
          }
          return false;
        }
      }
    }
    return true;
  }

  backtrack();
  return board;
}
```

## Why it works

`backtrack` always resolves the first empty cell it finds. For each candidate digit that passes `isValid`, it commits the digit and recurses; `true` bubbling up means every later cell was also filled successfully, so the whole board is done. If none of the nine digits lead to a full solution, the cell is reset to `'.'` and the function reports failure so the caller — the cell filled just before it — tries its next candidate. Because a solution is guaranteed to exist, this exhaustive trial-and-undo eventually reaches the unique completed grid.

## Complexity

- Time: O(9^k) worst case, where k is the number of empty cells — each one may try up to 9 digits before backtracking; every `isValid` call rescans a fixed 9+9+9 cells, an added constant factor since the board size never changes.
- Space: O(k) for the recursion stack, at most 81 for a fully empty board.
