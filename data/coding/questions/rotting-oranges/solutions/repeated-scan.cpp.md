The most direct reading of the problem: simulate the minutes one at a time. On each minute, scan the whole grid, mark every fresh orange that touches a rotten one, then flip all of those marks to rotten at once — never rot mid-scan, or a fresh orange could rot twice in the same minute.

Keep going until a scan finds no fresh oranges left (done) or a scan finds fresh oranges but rots none of them (stuck forever).

```cpp
#include <vector>
using namespace std;

class Solution {
public:
    int orangesRotting(vector<vector<int>>& grid) {
        int rows = grid.size(), cols = grid[0].size();
        int dirs[4][2] = {{1, 0}, {-1, 0}, {0, 1}, {0, -1}};
        int minutes = 0;
        while (true) {
            bool freshLeft = false;
            vector<pair<int, int>> toRot;
            for (int r = 0; r < rows; r++) {
                for (int c = 0; c < cols; c++) {
                    if (grid[r][c] == 1) {
                        freshLeft = true;
                        for (auto& d : dirs) {
                            int nr = r + d[0], nc = c + d[1];
                            if (nr >= 0 && nr < rows && nc >= 0 && nc < cols && grid[nr][nc] == 2) {
                                toRot.push_back({r, c});
                                break;
                            }
                        }
                    }
                }
            }
            if (!freshLeft) return minutes;
            if (toRot.empty()) return -1;
            for (auto& cell : toRot) grid[cell.first][cell.second] = 2;
            minutes++;
        }
    }
};
```

## Why it works

Each full pass over the grid corresponds to exactly one minute, because `toRot` is collected first and applied only after the scan finishes — so newly-rotted cells never infect a neighbor within the same minute. The loop terminates either when no fresh orange remains (`freshLeft` is `false`) or when a pass changes nothing (`toRot` is empty), which means the remaining fresh oranges are unreachable.

## Complexity

- Time: O((rows * cols)²) — up to `rows * cols` minutes may be needed, and each minute rescans the whole grid.
- Space: O(rows * cols) — for the `toRot` vector built each minute.
