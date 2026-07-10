The direct reading of the problem: an `'O'` survives only if its connected region touches the border. So for every `'O'` cell, run an independent flood fill from that single cell and check whether it ever reaches row 0, the last row, column 0, or the last column. If it never does, that cell gets flipped.

This is wasteful — cells in the same region repeat almost the same traversal from different starting points — but it is the honest first pass before noticing the traversals can be shared.

```java
import java.util.*;

class Solution {
    private int m, n;

    public void solve(char[][] board) {
        if (board.length == 0 || board[0].length == 0) return;
        m = board.length;
        n = board[0].length;
        List<int[]> toFlip = new ArrayList<>();

        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (board[i][j] == 'O' && !touchesBorder(board, i, j)) {
                    toFlip.add(new int[]{i, j});
                }
            }
        }
        for (int[] cell : toFlip) board[cell[0]][cell[1]] = 'X';
    }

    private boolean touchesBorder(char[][] board, int sr, int sc) {
        Deque<int[]> stack = new ArrayDeque<>();
        boolean[][] seen = new boolean[m][n];
        stack.push(new int[]{sr, sc});
        seen[sr][sc] = true;
        boolean touches = false;
        int[][] dirs = {{1, 0}, {-1, 0}, {0, 1}, {0, -1}};

        while (!stack.isEmpty()) {
            int[] cur = stack.pop();
            int r = cur[0], c = cur[1];
            if (r == 0 || r == m - 1 || c == 0 || c == n - 1) touches = true;
            for (int[] d : dirs) {
                int nr = r + d[0], nc = c + d[1];
                if (nr >= 0 && nr < m && nc >= 0 && nc < n && board[nr][nc] == 'O' && !seen[nr][nc]) {
                    seen[nr][nc] = true;
                    stack.push(new int[]{nr, nc});
                }
            }
        }
        return touches;
    }
}
```

## Why it works

`touchesBorder` explores the full connected region reachable from `(sr, sc)` and reports whether any cell in it lies on an edge of the board. Collecting flips into `toFlip` before mutating avoids changing `board` mid-scan, which would corrupt later flood fills. Since every `'O'` in a captured region individually fails the border check, all of them end up in `toFlip` and get turned to `'X'`.

## Complexity

- Time: O((m·n)²) — in the worst case every `'O'` cell re-explores an entire region of size O(m·n).
- Space: O(m·n) — the stack and `seen` grid for a single flood fill.
