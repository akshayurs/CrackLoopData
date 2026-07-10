Flip the question around: instead of asking "does this region touch the border?" for every cell, start from the border itself. Any `'O'` reachable from a border cell can never be captured, so flood fill outward from every border `'O'` and mark everything you reach with a placeholder like `'#'`. Whatever is still `'O'` afterward was never reachable from the border, so it gets flipped to `'X'` — and every `'#'` gets restored back to `'O'`.

Each cell is visited a constant number of times across the whole algorithm, so the redundant re-traversal from the brute-force approach disappears entirely.

```java
import java.util.*;

class Solution {
    public void solve(char[][] board) {
        if (board.length == 0 || board[0].length == 0) return;
        int m = board.length, n = board[0].length;
        int[][] dirs = {{1, 0}, {-1, 0}, {0, 1}, {0, -1}};

        for (int i = 0; i < m; i++) {
            markSafe(board, i, 0, m, n, dirs);
            markSafe(board, i, n - 1, m, n, dirs);
        }
        for (int j = 0; j < n; j++) {
            markSafe(board, 0, j, m, n, dirs);
            markSafe(board, m - 1, j, m, n, dirs);
        }

        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (board[i][j] == 'O') board[i][j] = 'X';
                else if (board[i][j] == '#') board[i][j] = 'O';
            }
        }
    }

    private void markSafe(char[][] board, int sr, int sc, int m, int n, int[][] dirs) {
        if (board[sr][sc] != 'O') return;
        Deque<int[]> stack = new ArrayDeque<>();
        stack.push(new int[]{sr, sc});
        board[sr][sc] = '#';
        while (!stack.isEmpty()) {
            int[] cur = stack.pop();
            for (int[] d : dirs) {
                int nr = cur[0] + d[0], nc = cur[1] + d[1];
                if (nr >= 0 && nr < m && nc >= 0 && nc < n && board[nr][nc] == 'O') {
                    board[nr][nc] = '#';
                    stack.push(new int[]{nr, nc});
                }
            }
        }
    }
}
```

## Why it works

Any `'O'` connected to the border by a path of `'O'`s cannot be surrounded, so `markSafe` floods outward from every border `'O'` and stamps `'#'` on the whole reachable set. After that pass, an `'O'` still standing had no path to any border cell, so it belongs to a captured region and is flipped to `'X'`; the `'#'` cells are restored to `'O'` since they were only a temporary marker.

## Complexity

- Time: O(m·n) — each cell is pushed onto the stack at most once across all flood fills.
- Space: O(m·n) — the stack can hold up to every cell in the worst case (one giant border-connected region).
