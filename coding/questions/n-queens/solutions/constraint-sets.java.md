Rescanning the board for every candidate cell is wasted work — a column or diagonal is either occupied or it isn't, and that fact doesn't change until you place or remove a queen. Track it directly: one boolean array for used columns, and one each for the two diagonal families, offset so the `row - col` index never goes negative. A cell on diagonal `row - col` (constant along a "\" diagonal) or `row + col` (constant along a "/" diagonal) is under attack the instant either flag is already set.

Placing a queen becomes three flag flips; checking a cell becomes three O(1) array reads, so the search itself is still exponential but each step is now constant time instead of linear.

```java
import java.util.ArrayList;
import java.util.List;

class Solution {
    private char[][] board;
    private boolean[] cols, diag1, diag2;
    private int n;
    private List<List<String>> results;

    public List<List<String>> solveNQueens(int n) {
        this.n = n;
        board = new char[n][n];
        for (char[] row : board) java.util.Arrays.fill(row, '.');
        cols = new boolean[n];
        diag1 = new boolean[2 * n];
        diag2 = new boolean[2 * n];
        results = new ArrayList<>();
        place(0);
        return results;
    }

    private void place(int row) {
        if (row == n) {
            List<String> snapshot = new ArrayList<>();
            for (char[] r : board) snapshot.add(new String(r));
            results.add(snapshot);
            return;
        }
        for (int col = 0; col < n; col++) {
            int d1 = row - col + n, d2 = row + col;
            if (cols[col] || diag1[d1] || diag2[d2]) continue;
            cols[col] = diag1[d1] = diag2[d2] = true;
            board[row][col] = 'Q';
            place(row + 1);
            board[row][col] = '.';
            cols[col] = diag1[d1] = diag2[d2] = false;
        }
    }
}
```

## Why it works

Every queen occupies a unique row by construction (one queen is placed per recursive call), so only columns and diagonals need guarding. `row - col` (shifted by `n` to stay non-negative) is invariant for every cell on the same downward diagonal, and `row + col` for every cell on the same upward diagonal, so the flags are exactly the "already attacked" tests. Setting the flags on placement and clearing them on backtrack keeps them in sync with the current partial board, and the row-major, left-to-right column order is unchanged from the naive version.

## Complexity

- Time: O(n!) — the same search tree as the brute-force version, but each visit is O(1) instead of O(n).
- Space: O(n) — the three flag arrays and recursion depth are each bounded by O(n).
