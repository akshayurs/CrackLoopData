Instead of rescanning the whole grid every minute, start a breadth-first search from *every* rotten orange at once, tagging each queued cell with the minute it rotted. Layer by layer, a BFS naturally spreads outward one minute at a time — exactly the way the infection spreads — so a single pass through the queue gives the answer.

Count the fresh oranges up front; every time the BFS rots one, decrement the count. If any are left when the queue empties, they were unreachable.

```cpp
#include <vector>
#include <queue>
#include <tuple>
using namespace std;

class Solution {
public:
    int orangesRotting(vector<vector<int>>& grid) {
        int rows = grid.size(), cols = grid[0].size();
        queue<tuple<int, int, int>> q;
        int fresh = 0;
        for (int r = 0; r < rows; r++) {
            for (int c = 0; c < cols; c++) {
                if (grid[r][c] == 2) q.push({r, c, 0});
                else if (grid[r][c] == 1) fresh++;
            }
        }

        int dirs[4][2] = {{1, 0}, {-1, 0}, {0, 1}, {0, -1}};
        int minutes = 0;
        while (!q.empty()) {
            auto [r, c, minute] = q.front();
            q.pop();
            minutes = max(minutes, minute);
            for (auto& d : dirs) {
                int nr = r + d[0], nc = c + d[1];
                if (nr >= 0 && nr < rows && nc >= 0 && nc < cols && grid[nr][nc] == 1) {
                    grid[nr][nc] = 2;
                    fresh--;
                    q.push({nr, nc, minute + 1});
                }
            }
        }

        return fresh == 0 ? minutes : -1;
    }
};
```

## Why it works

Seeding the queue with every rotten orange at minute 0 means the BFS explores in expanding "rings" of increasing minute count, matching how the real infection spreads simultaneously from all sources. Each cell is enqueued at most once — the moment it's marked rotten — so the final `minutes` is the largest minute stamp reached, and `fresh` reaching zero confirms every orange was infected rather than some being stranded behind empty cells.

## Complexity

- Time: O(rows * cols) — every cell is enqueued and processed at most once.
- Space: O(rows * cols) — the queue can hold every rotten cell at once.
