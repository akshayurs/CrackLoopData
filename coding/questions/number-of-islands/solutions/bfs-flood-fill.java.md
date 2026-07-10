The recursive flood fill can blow the call stack on a grid where one island spans hundreds of rows. Swap recursion for an explicit queue: when a new `'1'` is found, push it, then repeatedly poll a cell, mark it visited, and push its unvisited land neighbors until the queue drains.

The counting logic is identical to the DFS version — only the mechanics of "sink this island" change, from a call stack to a queue.

```java
import java.util.ArrayDeque;
import java.util.Deque;

class Solution {
    private static final int[][] DIRS = {{1, 0}, {-1, 0}, {0, 1}, {0, -1}};

    public int numIslands(char[][] grid) {
        int rows = grid.length, cols = grid[0].length;
        int count = 0;
        for (int r = 0; r < rows; r++) {
            for (int c = 0; c < cols; c++) {
                if (grid[r][c] == '1') {
                    count++;
                    sink(grid, r, c, rows, cols);
                }
            }
        }
        return count;
    }

    private void sink(char[][] grid, int sr, int sc, int rows, int cols) {
        Deque<int[]> queue = new ArrayDeque<>();
        queue.add(new int[]{sr, sc});
        grid[sr][sc] = '0';
        while (!queue.isEmpty()) {
            int[] cell = queue.poll();
            for (int[] d : DIRS) {
                int nr = cell[0] + d[0], nc = cell[1] + d[1];
                if (nr >= 0 && nr < rows && nc >= 0 && nc < cols && grid[nr][nc] == '1') {
                    grid[nr][nc] = '0';
                    queue.add(new int[]{nr, nc});
                }
            }
        }
    }
}
```

## Why it works

Every cell polled from the queue is expanded exactly once, and a cell is only ever added after being marked `'0'`, so no cell is enqueued twice. The queue drains precisely when every cell reachable from the starting land cell has been visited, which is the same connected component the DFS version would have covered — just explored breadth-first instead of depth-first.

## Complexity

- Time: O(rows * cols) — every cell is enqueued and dequeued at most once.
- Space: O(rows * cols) — worst case queue size if the whole grid is one island.
