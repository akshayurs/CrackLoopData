Flip the direction of the search. Instead of asking "where can water starting at cell X go?" for every cell, start from the oceans and ask "which cells could have sent water here?" Water flows downhill-or-equal, so walking backward from a border means moving to a neighbor whose height is greater than or equal to the current one.

Seed a BFS with every Pacific-border cell at once, and a separate BFS with every Atlantic-border cell at once. Each visits, in a single O(m*n) sweep, exactly the set of cells that can reach that ocean. The answer is the intersection of the two sets — no cell is ever re-explored across different starting points.

```cpp
#include <vector>
#include <queue>
using namespace std;

class Solution {
public:
    vector<vector<int>> pacificAtlantic(vector<vector<int>>& heights) {
        vector<vector<int>> result;
        if (heights.empty() || heights[0].empty()) return result;
        int m = heights.size(), n = heights[0].size();

        vector<pair<int, int>> pacificStarts, atlanticStarts;
        for (int c = 0; c < n; c++) {
            pacificStarts.push_back({0, c});
            atlanticStarts.push_back({m - 1, c});
        }
        for (int r = 0; r < m; r++) {
            pacificStarts.push_back({r, 0});
            atlanticStarts.push_back({r, n - 1});
        }

        auto pacific = bfs(heights, m, n, pacificStarts);
        auto atlantic = bfs(heights, m, n, atlanticStarts);

        for (int r = 0; r < m; r++) {
            for (int c = 0; c < n; c++) {
                if (pacific[r][c] && atlantic[r][c]) result.push_back({r, c});
            }
        }
        return result;
    }

private:
    vector<vector<bool>> bfs(vector<vector<int>>& heights, int m, int n,
                              vector<pair<int, int>>& starts) {
        vector<vector<bool>> seen(m, vector<bool>(n, false));
        queue<pair<int, int>> q;
        for (auto& s : starts) {
            if (!seen[s.first][s.second]) { seen[s.first][s.second] = true; q.push(s); }
        }
        int dr[] = {1, -1, 0, 0}, dc[] = {0, 0, 1, -1};
        while (!q.empty()) {
            auto [r, c] = q.front(); q.pop();
            for (int i = 0; i < 4; i++) {
                int nr = r + dr[i], nc = c + dc[i];
                if (nr >= 0 && nr < m && nc >= 0 && nc < n && !seen[nr][nc]
                        && heights[nr][nc] >= heights[r][c]) {
                    seen[nr][nc] = true;
                    q.push({nr, nc});
                }
            }
        }
        return seen;
    }
};
```

## Why it works

Reversing the flow condition (`>=` instead of `<=`) turns "can this cell send water to the ocean" into "can the ocean's backward search reach this cell," and the two are equivalent by symmetry of the adjacency relation. Since each BFS explores every cell at most once, running it from all border cells simultaneously still costs one pass over the grid instead of one pass per cell. Scanning rows then columns for the final result keeps it sorted without a separate sort step.

## Complexity

- Time: O(m * n) — each of the two BFS traversals visits every cell and edge at most once.
- Space: O(m * n) — the two visited grids and BFS queues.
