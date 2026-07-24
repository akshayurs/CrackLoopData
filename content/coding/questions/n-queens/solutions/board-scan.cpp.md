Place queens one row at a time. Before dropping a queen into a cell, scan every queen already placed in earlier rows and reject the cell if it shares a column or either diagonal. This is the most literal reading of the rules — no bookkeeping beyond the board itself.

Once a row is filled successfully all the way to the last row, the current board is a valid layout; snapshot it and keep backtracking to find the rest.

```cpp
#include <vector>
#include <string>
#include <cmath>
using namespace std;

class Solution {
public:
    vector<vector<string>> solveNQueens(int n) {
        vector<string> board(n, string(n, '.'));
        vector<vector<string>> results;
        place(0, n, board, results);
        return results;
    }

private:
    bool isSafe(int row, int col, vector<string>& board) {
        for (int r = 0; r < row; r++) {
            int c = board[r].find('Q');
            if (c == col || abs(c - col) == row - r) return false;
        }
        return true;
    }

    void place(int row, int n, vector<string>& board, vector<vector<string>>& results) {
        if (row == n) {
            results.push_back(board);
            return;
        }
        for (int col = 0; col < n; col++) {
            if (isSafe(row, col, board)) {
                board[row][col] = 'Q';
                place(row + 1, n, board, results);
                board[row][col] = '.';
            }
        }
    }
};
```

## Why it works

`isSafe` re-derives every earlier queen's column with `find('Q')` and checks it against the candidate column and both diagonals (`abs(c - col) == row - r` catches both diagonal directions at once). Backtracking undoes a placement the moment a row is finished exploring, so every combination of columns is tried and only fully safe boards are recorded — in row-major, left-to-right column order.

## Complexity

- Time: O(n! * n) — roughly n! placements are attempted, and each safety check rescans up to n earlier rows.
- Space: O(n^2) — the board plus recursion depth up to n.
