The most direct way to measure an island is to stand on a land cell and explore outward, counting every connected `1` you can reach. Recursion expresses that exploration naturally: visiting a cell means visiting its four neighbors too.

To avoid recounting cells, sink each visited land cell to `0` as you leave it, so the grid itself doubles as the visited set. Scan every cell as a potential island start and keep the largest area seen.

```cpp
#include <vector>
#include <algorithm>
using namespace std;

class Solution {
public:
    int maxAreaOfIsland(vector<vector<int>>& grid) {
        rows = grid.size();
        cols = grid[0].size();
        int best = 0;
        for (int r = 0; r < rows; r++) {
            for (int c = 0; c < cols; c++) {
                if (grid[r][c] == 1) {
                    best = max(best, dfs(grid, r, c));
                }
            }
        }
        return best;
    }

private:
    int rows, cols;

    int dfs(vector<vector<int>>& grid, int r, int c) {
        if (r < 0 || r >= rows || c < 0 || c >= cols || grid[r][c] == 0) {
            return 0;
        }
        grid[r][c] = 0;
        return 1 + dfs(grid, r + 1, c) + dfs(grid, r - 1, c)
                 + dfs(grid, r, c + 1) + dfs(grid, r, c - 1);
    }
};
```

## Why it works

`dfs(r, c)` returns 0 immediately for out-of-bounds or water cells, otherwise it claims the current cell (sinking it to `0`) and adds the areas returned by its four neighbors. Because visited land is zeroed out, no cell is ever counted twice, so summing the recursive calls yields exactly the size of the connected component containing `(r, c)`. Iterating over every cell guarantees every island gets a starting point, and tracking a running maximum finds the largest one.

## Complexity

- Time: O(m·n) — each cell is visited and sunk at most once.
- Space: O(m·n) — worst case the recursion stack holds every land cell (a grid that is entirely one island).
