Place queens one row at a time. Before dropping a queen into a cell, scan every queen already placed in earlier rows and reject the cell if it shares a column or either diagonal. This is the most literal reading of the rules — no bookkeeping beyond the board itself.

Once a row is filled successfully all the way to the last row, the current board is a valid layout; snapshot it and keep backtracking to find the rest.

```java
import java.util.ArrayList;
import java.util.List;

class Solution {
    private char[][] board;
    private int n;
    private List<List<String>> results;

    public List<List<String>> solveNQueens(int n) {
        this.n = n;
        board = new char[n][n];
        for (char[] row : board) java.util.Arrays.fill(row, '.');
        results = new ArrayList<>();
        place(0);
        return results;
    }

    private boolean isSafe(int row, int col) {
        for (int r = 0; r < row; r++) {
            int c = 0;
            while (board[r][c] != 'Q') c++;
            if (c == col || Math.abs(c - col) == row - r) return false;
        }
        return true;
    }

    private void place(int row) {
        if (row == n) {
            List<String> snapshot = new ArrayList<>();
            for (char[] r : board) snapshot.add(new String(r));
            results.add(snapshot);
            return;
        }
        for (int col = 0; col < n; col++) {
            if (isSafe(row, col)) {
                board[row][col] = 'Q';
                place(row + 1);
                board[row][col] = '.';
            }
        }
    }
}
```

## Why it works

`isSafe` re-derives every earlier queen's column by scanning the row for `'Q'` and checks it against the candidate column and both diagonals (`Math.abs(c - col) == row - r` catches both diagonal directions at once). Backtracking undoes a placement the moment a row is finished exploring, so every combination of columns is tried and only fully safe boards are recorded — in row-major, left-to-right column order.

## Complexity

- Time: O(n! * n) — roughly n! placements are attempted, and each safety check rescans up to n earlier rows.
- Space: O(n^2) — the board plus recursion depth up to n.
