Rescanning the board for every candidate cell is wasted work — a column or diagonal is either occupied or it isn't, and that fact doesn't change until you place or remove a queen. Track it directly: one boolean array for used columns, and one each for the two diagonal families, offset so the `row - col` index never goes negative. A cell on diagonal `row - col` (constant along a "\" diagonal) or `row + col` (constant along a "/" diagonal) is under attack the instant either flag is already set.

Placing a queen becomes three flag flips; checking a cell becomes three O(1) array reads, so the search itself is still exponential but each step is now constant time instead of linear.

```cpp
#include <vector>
#include <string>
using namespace std;

class Solution {
public:
    vector<vector<string>> solveNQueens(int n) {
        vector<string> board(n, string(n, '.'));
        vector<bool> cols(n, false), diag1(2 * n, false), diag2(2 * n, false);
        vector<vector<string>> results;
        place(0, n, board, cols, diag1, diag2, results);
        return results;
    }

private:
    void place(int row, int n, vector<string>& board, vector<bool>& cols,
               vector<bool>& diag1, vector<bool>& diag2, vector<vector<string>>& results) {
        if (row == n) {
            results.push_back(board);
            return;
        }
        for (int col = 0; col < n; col++) {
            int d1 = row - col + n, d2 = row + col;
            if (cols[col] || diag1[d1] || diag2[d2]) continue;
            cols[col] = diag1[d1] = diag2[d2] = true;
            board[row][col] = 'Q';
            place(row + 1, n, board, cols, diag1, diag2, results);
            board[row][col] = '.';
            cols[col] = diag1[d1] = diag2[d2] = false;
        }
    }
};
```

## Why it works

Every queen occupies a unique row by construction (one queen is placed per recursive call), so only columns and diagonals need guarding. `row - col` (shifted by `n` to stay non-negative) is invariant for every cell on the same downward diagonal, and `row + col` for every cell on the same upward diagonal, so the flags are exactly the "already attacked" tests. Setting the flags on placement and clearing them on backtrack keeps them in sync with the current partial board, and the row-major, left-to-right column order is unchanged from the naive version.

## Complexity

- Time: O(n!) — the same search tree as the brute-force version, but each visit is O(1) instead of O(n).
- Space: O(n) — the three flag arrays and recursion depth are each bounded by O(n).
