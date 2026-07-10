Flip the direction of the search. Instead of asking "where can water starting at cell X go?" for every cell, start from the oceans and ask "which cells could have sent water here?" Water flows downhill-or-equal, so walking backward from a border means moving to a neighbor whose height is greater than or equal to the current one.

Seed a BFS with every Pacific-border cell at once, and a separate BFS with every Atlantic-border cell at once. Each visits, in a single O(m*n) sweep, exactly the set of cells that can reach that ocean. The answer is the intersection of the two sets — no cell is ever re-explored across different starting points.

```java
import java.util.*;

class Solution {
    public List<List<Integer>> pacificAtlantic(int[][] heights) {
        List<List<Integer>> result = new ArrayList<>();
        if (heights.length == 0 || heights[0].length == 0) return result;
        int m = heights.length, n = heights[0].length;

        List<int[]> pacificStarts = new ArrayList<>(), atlanticStarts = new ArrayList<>();
        for (int c = 0; c < n; c++) {
            pacificStarts.add(new int[]{0, c});
            atlanticStarts.add(new int[]{m - 1, c});
        }
        for (int r = 0; r < m; r++) {
            pacificStarts.add(new int[]{r, 0});
            atlanticStarts.add(new int[]{r, n - 1});
        }

        boolean[][] pacific = bfs(heights, m, n, pacificStarts);
        boolean[][] atlantic = bfs(heights, m, n, atlanticStarts);

        for (int r = 0; r < m; r++) {
            for (int c = 0; c < n; c++) {
                if (pacific[r][c] && atlantic[r][c]) result.add(Arrays.asList(r, c));
            }
        }
        return result;
    }

    private boolean[][] bfs(int[][] heights, int m, int n, List<int[]> starts) {
        boolean[][] seen = new boolean[m][n];
        Deque<int[]> queue = new ArrayDeque<>();
        for (int[] s : starts) {
            if (!seen[s[0]][s[1]]) { seen[s[0]][s[1]] = true; queue.add(s); }
        }
        int[][] dirs = {{1, 0}, {-1, 0}, {0, 1}, {0, -1}};
        while (!queue.isEmpty()) {
            int[] cur = queue.poll();
            for (int[] d : dirs) {
                int nr = cur[0] + d[0], nc = cur[1] + d[1];
                if (nr >= 0 && nr < m && nc >= 0 && nc < n && !seen[nr][nc]
                        && heights[nr][nc] >= heights[cur[0]][cur[1]]) {
                    seen[nr][nc] = true;
                    queue.add(new int[]{nr, nc});
                }
            }
        }
        return seen;
    }
}
```

## Why it works

Reversing the flow condition (`>=` instead of `<=`) turns "can this cell send water to the ocean" into "can the ocean's backward search reach this cell," and the two are equivalent by symmetry of the adjacency relation. Since each BFS explores every cell at most once, running it from all border cells simultaneously still costs one pass over the grid instead of one pass per cell. Scanning rows then columns for the final result keeps it sorted without a separate sort step.

## Complexity

- Time: O(m * n) — each of the two BFS traversals visits every cell and edge at most once.
- Space: O(m * n) — the two visited grids and BFS queues.
