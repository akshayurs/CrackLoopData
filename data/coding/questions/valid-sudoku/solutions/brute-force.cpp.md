The three rules are independent, so the most direct approach is to check them one at a time: sweep the nine rows, then the nine columns, then the nine boxes. Each group is a collection of nine cells, and a group is legal exactly when its filled digits are all distinct.

Give each group a fresh `unordered_set` and try to insert every digit. `insert(...).second` is `false` when the value is already present, which is precisely the duplicate we are hunting; dots are skipped.

```cpp
#include <vector>
#include <unordered_set>
using namespace std;

class Solution {
public:
    bool isValidSudoku(vector<vector<char>>& board) {
        for (int r = 0; r < 9; r++) {
            unordered_set<char> seen;
            for (int c = 0; c < 9; c++)
                if (!add(seen, board[r][c])) return false;
        }
        for (int c = 0; c < 9; c++) {
            unordered_set<char> seen;
            for (int r = 0; r < 9; r++)
                if (!add(seen, board[r][c])) return false;
        }
        for (int br = 0; br < 9; br += 3) {
            for (int bc = 0; bc < 9; bc += 3) {
                unordered_set<char> seen;
                for (int i = 0; i < 3; i++)
                    for (int j = 0; j < 3; j++)
                        if (!add(seen, board[br + i][bc + j])) return false;
            }
        }
        return true;
    }

private:
    bool add(unordered_set<char>& seen, char ch) {
        return ch == '.' || seen.insert(ch).second;
    }
};
```

## Why it works

A Sudoku filling is valid iff none of the 27 groups (9 rows + 9 columns + 9 boxes) repeats a digit. Each group gets its own set, so a digit only clashes with others inside the same group; a failed `insert` flags that clash and aborts. Covering all 27 groups without a clash certifies the whole board.

## Complexity

For an `N×N` board (here `N = 9`):

- Time: O(N²) — each of the three sweeps touches all N² cells once.
- Space: O(N) — one set of at most N digits exists at a time.
