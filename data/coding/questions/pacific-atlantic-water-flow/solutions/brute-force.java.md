The direct reading of the problem: for every single cell, simulate where its water can go. Run a DFS from that cell following only downhill-or-equal moves, and check whether the reachable set ever touches the top/left border (Pacific) and separately whether it touches the bottom/right border (Atlantic).

This retraces huge amounts of shared ground — cells near the middle of the grid get re-explored once per starting cell — but it mirrors the problem statement almost line for line, which makes it a solid first answer before optimizing.

```java
import java.util.*;

class Solution {
    private int m, n;
    private int[][] heights;

    public List<List<Integer>> pacificAtlantic(int[][] heights) {
        this.heights = heights;
        List<List<Integer>> result = new ArrayList<>();
        if (heights.length == 0 || heights[0].length == 0) return result;
        m = heights.length; n = heights[0].length;
        for (int r = 0; r < m; r++) {
            for (int c = 0; c < n; c++) {
                if (reaches(r, c, true) && reaches(r, c, false)) {
                    result.add(Arrays.asList(r, c));
                }
            }
        }
        return result;
    }

    private boolean reaches(int sr, int sc, boolean pacific) {
        boolean[][] seen = new boolean[m][n];
        Deque<int[]> stack = new ArrayDeque<>();
        stack.push(new int[]{sr, sc});
        seen[sr][sc] = true;
        boolean touched = isTarget(sr, sc, pacific);
        int[][] dirs = {{1, 0}, {-1, 0}, {0, 1}, {0, -1}};
        while (!stack.isEmpty()) {
            int[] cur = stack.pop();
            for (int[] d : dirs) {
                int nr = cur[0] + d[0], nc = cur[1] + d[1];
                if (nr >= 0 && nr < m && nc >= 0 && nc < n && !seen[nr][nc]
                        && heights[nr][nc] <= heights[cur[0]][cur[1]]) {
                    seen[nr][nc] = true;
                    stack.push(new int[]{nr, nc});
                    touched = touched || isTarget(nr, nc, pacific);
                }
            }
        }
        return touched;
    }

    private boolean isTarget(int r, int c, boolean pacific) {
        return pacific ? (r == 0 || c == 0) : (r == m - 1 || c == n - 1);
    }
}
```

## Why it works

Each DFS from a cell visits exactly the set of cells reachable by non-increasing steps, which is precisely the water-flow rule in the problem. A cell qualifies once its own reachable set includes at least one Pacific-border cell and at least one Atlantic-border cell — including itself. Iterating cells in row-major order keeps the output naturally sorted.

## Complexity

- Time: O(m^2 * n^2) — a DFS over up to m*n cells is run from every one of the m*n starting cells.
- Space: O(m * n) — the visited grid and stack for a single DFS.
