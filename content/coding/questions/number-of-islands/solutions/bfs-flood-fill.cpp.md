The recursive flood fill can blow the call stack on a grid where one island spans hundreds of rows. Swap recursion for an explicit queue: when a new `'1'` is found, push it, then repeatedly pop the front cell, mark it visited, and push its unvisited land neighbors until the queue drains.

The counting logic is identical to the DFS version — only the mechanics of "sink this island" change, from a call stack to a queue.

```cpp
#include <vector>
#include <string>
#include <queue>
using namespace std;

class Solution {
public:
    int numIslands(vector<string>& grid) {
        int rows = grid.size(), cols = grid[0].size();
        int dirs[4][2] = {{1, 0}, {-1, 0}, {0, 1}, {0, -1}};
        int count = 0;
        for (int r = 0; r < rows; r++) {
            for (int c = 0; c < cols; c++) {
                if (grid[r][c] == '1') {
                    count++;
                    queue<pair<int, int>> q;
                    q.push({r, c});
                    grid[r][c] = '0';
                    while (!q.empty()) {
                        auto [cr, cc] = q.front();
                        q.pop();
                        for (auto& d : dirs) {
                            int nr = cr + d[0], nc = cc + d[1];
                            if (nr >= 0 && nr < rows && nc >= 0 && nc < cols && grid[nr][nc] == '1') {
                                grid[nr][nc] = '0';
                                q.push({nr, nc});
                            }
                        }
                    }
                }
            }
        }
        return count;
    }
};
```

## Why it works

Every cell popped from the queue is expanded exactly once, and a cell is only ever pushed after being marked `'0'`, so no cell is enqueued twice. The queue drains precisely when every cell reachable from the starting land cell has been visited, which is the same connected component the DFS version would have covered — just explored breadth-first instead of depth-first.

## Complexity

- Time: O(rows * cols) — every cell is enqueued and dequeued at most once.
- Space: O(rows * cols) — worst case queue size if the whole grid is one island.
