The same idea in C++: scan for the first empty cell, try each digit `1`-`9` after re-checking the row, column and box in full, and undo on failure.

```cpp
#include <vector>
using namespace std;

class Solution {
public:
    void solveSudoku(vector<vector<char>>& board) {
        backtrack(board);
    }

private:
    bool backtrack(vector<vector<char>>& board) {
        for (int r = 0; r < 9; r++) {
            for (int c = 0; c < 9; c++) {
                if (board[r][c] == '.') {
                    for (char ch = '1'; ch <= '9'; ch++) {
                        if (isValid(board, r, c, ch)) {
                            board[r][c] = ch;
                            if (backtrack(board)) return true;
                            board[r][c] = '.';
                        }
                    }
                    return false;
                }
            }
        }
        return true;
    }

    bool isValid(vector<vector<char>>& board, int r, int c, char ch) {
        for (int i = 0; i < 9; i++) {
            if (board[r][i] == ch || board[i][c] == ch) return false;
        }
        int br = 3 * (r / 3), bc = 3 * (c / 3);
        for (int i = br; i < br + 3; i++) {
            for (int j = bc; j < bc + 3; j++) {
                if (board[i][j] == ch) return false;
            }
        }
        return true;
    }
};
```

## Why it works

`backtrack` always resolves the first empty cell it finds, in row-major order. Each candidate digit that survives `isValid` is committed and the search recurses; `true` bubbling up means every remaining cell was also filled, so the board is complete. A dead end resets the cell to `'.'` and returns `false`, prompting the previous call to try its next digit. The guarantee of a unique solution means this exhaustive search always terminates successfully.

## Complexity

- Time: O(9^k) worst case, where k is the number of empty cells; each `isValid` call rescans a fixed 9+9+9 cells, an added constant factor since the board size never changes.
- Space: O(k) for the recursion stack, at most 81 for a fully empty board.
