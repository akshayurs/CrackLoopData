Scan every cell. Whenever you land on an unvisited `'1'`, you've found a new island — sink it entirely with a depth-first search that recursively visits its up/down/left/right neighbors, marking each visited cell as `'0'` so it's never counted again.

Because the flood fill consumes the whole island before the outer scan moves on, each connected blob of land triggers exactly one increment of the island counter.

```cpp
#include <vector>
#include <string>
using namespace std;

class Solution {
public:
    int numIslands(vector<string>& grid) {
        rows = grid.size();
        cols = grid[0].size();
        int count = 0;
        for (int r = 0; r < rows; r++) {
            for (int c = 0; c < cols; c++) {
                if (grid[r][c] == '1') {
                    count++;
                    sink(grid, r, c);
                }
            }
        }
        return count;
    }

private:
    int rows, cols;

    void sink(vector<string>& grid, int r, int c) {
        if (r < 0 || r >= rows || c < 0 || c >= cols || grid[r][c] != '1') return;
        grid[r][c] = '0';
        sink(grid, r + 1, c);
        sink(grid, r - 1, c);
        sink(grid, r, c + 1);
        sink(grid, r, c - 1);
    }
};
```

## Why it works

The outer double loop guarantees every cell is inspected. The first time it meets a `'1'` that hasn't already been erased, that cell must belong to an island the scan hasn't counted yet, so the counter increments once and `sink` erases every cell reachable from it via land moves — preventing the scan from ever re-counting the same island.

## Complexity

- Time: O(rows * cols) — every cell is visited by the outer loop once and sunk at most once.
- Space: O(rows * cols) — worst case recursion depth if the whole grid is one island.
