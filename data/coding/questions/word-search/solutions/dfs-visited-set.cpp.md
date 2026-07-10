Try every starting cell and, from there, walk the board one letter at a time, only stepping to a neighbor that matches the next character of `word`. A `visited` grid keeps the current path from stepping on a cell twice; clearing a cell when a branch fails is what makes this backtracking rather than a plain walk.

This is the direct translation of the problem statement into code — no attempt yet to prune the search.

```cpp
#include <vector>
#include <string>
using namespace std;

class Solution {
public:
    bool exist(vector<vector<char>>& board, string word) {
        rows = board.size();
        cols = board[0].size();
        visited.assign(rows, vector<bool>(cols, false));

        for (int r = 0; r < rows; r++) {
            for (int c = 0; c < cols; c++) {
                if (dfs(board, word, r, c, 0)) return true;
            }
        }
        return false;
    }

private:
    int rows, cols;
    vector<vector<bool>> visited;

    bool dfs(vector<vector<char>>& board, const string& word, int r, int c, int i) {
        if (i == (int)word.size()) return true;
        if (r < 0 || r >= rows || c < 0 || c >= cols) return false;
        if (visited[r][c] || board[r][c] != word[i]) return false;

        visited[r][c] = true;
        bool found = dfs(board, word, r + 1, c, i + 1) || dfs(board, word, r - 1, c, i + 1) ||
                     dfs(board, word, r, c + 1, i + 1) || dfs(board, word, r, c - 1, i + 1);
        visited[r][c] = false;
        return found;
    }
};
```

## Why it works

`dfs(r, c, i)` succeeds if the board can spell the suffix of `word` starting at index `i`, beginning at `(r, c)`. It checks bounds and the current letter, then tries all four neighbors for the next character. Marking `visited[r][c]` true before recursing stops the path from doubling back on itself; resetting it to false right after the recursive calls return is the backtrack step, restoring the cell so a *different* path can still use it. Trying every cell as a start covers every possible trace.

## Complexity

- Time: O(m · n · 4^L) — up to m·n starting cells, each exploring up to 4 directions per one of L letters.
- Space: O(L) — the recursion stack holds at most one frame per letter of the current path (the visited grid is O(m·n) but reused across starts).
