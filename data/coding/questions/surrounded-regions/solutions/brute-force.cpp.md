The direct reading of the problem: an `'O'` survives only if its connected region touches the border. So for every `'O'` cell, run an independent flood fill from that single cell and check whether it ever reaches row 0, the last row, column 0, or the last column. If it never does, that cell gets flipped.

This is wasteful — cells in the same region repeat almost the same traversal from different starting points — but it is the honest first pass before noticing the traversals can be shared.

```cpp
#include <vector>
using namespace std;

class Solution {
public:
    void solve(vector<vector<char>>& board) {
        if (board.empty() || board[0].empty()) return;
        int m = board.size(), n = board[0].size();
        vector<pair<int, int>> toFlip;

        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (board[i][j] == 'O' && !touchesBorder(board, i, j, m, n)) {
                    toFlip.push_back({i, j});
                }
            }
        }
        for (auto& [i, j] : toFlip) board[i][j] = 'X';
    }

private:
    bool touchesBorder(vector<vector<char>>& board, int sr, int sc, int m, int n) {
        vector<vector<bool>> seen(m, vector<bool>(n, false));
        vector<pair<int, int>> stack = {{sr, sc}};
        seen[sr][sc] = true;
        bool touches = false;
        int dirs[4][2] = {{1, 0}, {-1, 0}, {0, 1}, {0, -1}};

        while (!stack.empty()) {
            auto [r, c] = stack.back();
            stack.pop_back();
            if (r == 0 || r == m - 1 || c == 0 || c == n - 1) touches = true;
            for (auto& d : dirs) {
                int nr = r + d[0], nc = c + d[1];
                if (nr >= 0 && nr < m && nc >= 0 && nc < n && board[nr][nc] == 'O' && !seen[nr][nc]) {
                    seen[nr][nc] = true;
                    stack.push_back({nr, nc});
                }
            }
        }
        return touches;
    }
};
```

## Why it works

`touchesBorder` explores the full connected region reachable from `(sr, sc)` and reports whether any cell in it lies on an edge of the board. Collecting flips into `toFlip` before mutating avoids changing `board` mid-scan, which would corrupt later flood fills. Since every `'O'` in a captured region individually fails the border check, all of them end up in `toFlip` and get turned to `'X'`.

## Complexity

- Time: O((m·n)²) — in the worst case every `'O'` cell re-explores an entire region of size O(m·n).
- Space: O(m·n) — the stack and `seen` grid for a single flood fill.
