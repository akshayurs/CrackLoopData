The direct reading of the problem: for every single cell, simulate where its water can go. Run a DFS from that cell following only downhill-or-equal moves, and check whether the reachable set ever touches the top/left border (Pacific) and separately whether it touches the bottom/right border (Atlantic).

This retraces huge amounts of shared ground — cells near the middle of the grid get re-explored once per starting cell — but it mirrors the problem statement almost line for line, which makes it a solid first answer before optimizing.

```cpp
#include <vector>
using namespace std;

class Solution {
public:
    vector<vector<int>> pacificAtlantic(vector<vector<int>>& heights) {
        vector<vector<int>> result;
        if (heights.empty() || heights[0].empty()) return result;
        m = heights.size(); n = heights[0].size();
        for (int r = 0; r < m; r++) {
            for (int c = 0; c < n; c++) {
                if (reaches(heights, r, c, true) && reaches(heights, r, c, false)) {
                    result.push_back({r, c});
                }
            }
        }
        return result;
    }

private:
    int m, n;

    bool isTarget(int r, int c, bool pacific) {
        return pacific ? (r == 0 || c == 0) : (r == m - 1 || c == n - 1);
    }

    bool reaches(vector<vector<int>>& heights, int sr, int sc, bool pacific) {
        vector<vector<bool>> seen(m, vector<bool>(n, false));
        vector<pair<int, int>> stack{{sr, sc}};
        seen[sr][sc] = true;
        bool touched = isTarget(sr, sc, pacific);
        int dr[] = {1, -1, 0, 0}, dc[] = {0, 0, 1, -1};
        while (!stack.empty()) {
            auto [r, c] = stack.back();
            stack.pop_back();
            for (int i = 0; i < 4; i++) {
                int nr = r + dr[i], nc = c + dc[i];
                if (nr >= 0 && nr < m && nc >= 0 && nc < n && !seen[nr][nc]
                        && heights[nr][nc] <= heights[r][c]) {
                    seen[nr][nc] = true;
                    stack.push_back({nr, nc});
                    touched = touched || isTarget(nr, nc, pacific);
                }
            }
        }
        return touched;
    }
};
```

## Why it works

Each DFS from a cell visits exactly the set of cells reachable by non-increasing steps, which is precisely the water-flow rule in the problem. A cell qualifies once its own reachable set includes at least one Pacific-border cell and at least one Atlantic-border cell — including itself. Iterating cells in row-major order keeps the output naturally sorted.

## Complexity

- Time: O(m^2 * n^2) — a DFS over up to m*n cells is run from every one of the m*n starting cells.
- Space: O(m * n) — the visited grid and stack for a single DFS.
