The same bitmask idea in Java: three `int[9]` arrays track which digits are used in each row, column, and box, and a precomputed list of empty cells replaces re-scanning the board for the next blank.

```java
import java.util.*;

class Solution {
    public void solveSudoku(char[][] board) {
        int[] rows = new int[9], cols = new int[9], boxes = new int[9];
        List<int[]> empties = new ArrayList<>();

        for (int r = 0; r < 9; r++) {
            for (int c = 0; c < 9; c++) {
                if (board[r][c] == '.') {
                    empties.add(new int[]{r, c});
                } else {
                    int bit = 1 << (board[r][c] - '1');
                    rows[r] |= bit;
                    cols[c] |= bit;
                    boxes[(r / 3) * 3 + c / 3] |= bit;
                }
            }
        }
        backtrack(board, empties, 0, rows, cols, boxes);
    }

    private boolean backtrack(char[][] board, List<int[]> empties, int k,
                               int[] rows, int[] cols, int[] boxes) {
        if (k == empties.size()) return true;
        int r = empties.get(k)[0], c = empties.get(k)[1];
        int b = (r / 3) * 3 + c / 3;
        int used = rows[r] | cols[c] | boxes[b];
        for (int d = 1; d <= 9; d++) {
            int bit = 1 << (d - 1);
            if ((used & bit) != 0) continue;
            board[r][c] = (char) ('0' + d);
            rows[r] |= bit; cols[c] |= bit; boxes[b] |= bit;
            if (backtrack(board, empties, k + 1, rows, cols, boxes)) return true;
            board[r][c] = '.';
            rows[r] ^= bit; cols[c] ^= bit; boxes[b] ^= bit;
        }
        return false;
    }
}
```

## Why it works

`used = rows[r] | cols[c] | boxes[b]` merges the three constraints touching cell `(r, c)` into one integer in constant time; any clear bit is a digit safe to place there. Placing digit `d` sets that bit in all three masks so later cells immediately see the updated constraint, and a failed branch clears the same bit with XOR to restore the prior state exactly. Iterating the precomputed `empties` list by index means each recursive call jumps directly to the next cell that needs a value instead of rescanning the grid.

## Complexity

- Time: O(9^k) worst case, where k is the number of empty cells — same branching factor as brute force, but each validity check and update is O(1) bitwise work instead of an O(27) rescan.
- Space: O(1) extra for the three fixed-size mask arrays, plus O(k) for the recursion stack and the `empties` list.
