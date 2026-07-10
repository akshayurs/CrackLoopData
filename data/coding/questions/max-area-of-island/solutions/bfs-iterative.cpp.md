Recursive flood fill reads cleanly, but on a large all-land grid the call stack grows one frame per cell — a 50×50 grid is only 2,500 cells, yet the pattern doesn't scale safely to bigger inputs or languages with small default stacks. Swapping recursion for an explicit queue keeps the exact same flood-fill logic while bounding memory to what you allocate yourself.

Start a breadth-first search from every unvisited land cell, sinking cells to `0` the moment they're enqueued so nothing is queued twice, and count how many cells each search dequeues.

```cpp
#include <vector>
#include <queue>
#include <algorithm>
using namespace std;

class Solution {
public:
    int maxAreaOfIsland(vector<vector<int>>& grid) {
        int rows = grid.size(), cols = grid[0].size();
        int dr[4] = {1, -1, 0, 0};
        int dc[4] = {0, 0, 1, -1};
        int best = 0;

        for (int sr = 0; sr < rows; sr++) {
            for (int sc = 0; sc < cols; sc++) {
                if (grid[sr][sc] == 0) continue;

                grid[sr][sc] = 0;
                queue<pair<int, int>> q;
                q.push({sr, sc});
                int area = 0;
                while (!q.empty()) {
                    auto [r, c] = q.front();
                    q.pop();
                    area++;
                    for (int d = 0; d < 4; d++) {
                        int nr = r + dr[d], nc = c + dc[d];
                        if (nr >= 0 && nr < rows && nc >= 0 && nc < cols && grid[nr][nc] == 1) {
                            grid[nr][nc] = 0;
                            q.push({nr, nc});
                        }
                    }
                }
                best = max(best, area);
            }
        }
        return best;
    }
};
```

## Why it works

Marking a cell as visited (`grid[r][c] = 0`) at enqueue time, not at dequeue time, guarantees each cell enters the queue exactly once, so the loop terminates and `area` counts every cell in the component exactly once. Starting a fresh BFS from each still-unvisited land cell partitions the grid into its connected islands, and the running maximum over all of them is the answer.

## Complexity

- Time: O(m·n) — every cell is enqueued and dequeued at most once.
- Space: O(m·n) — the queue can hold up to every land cell in the worst case (one giant island).
