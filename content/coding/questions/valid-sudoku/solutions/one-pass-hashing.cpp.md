Instead of revisiting the grid three times, notice that every filled cell belongs to exactly one row, one column, and one box — and its box index is fully determined by its coordinates as `(r / 3) * 3 + c / 3`. So a single scan can update all three memberships at once.

Keep nine sets for rows, nine for columns, and nine for boxes. `unordered_set::insert` reports `.second == false` when the digit is already present, so a single short-circuited `||` over the three sets both tests and records membership.

```cpp
#include <vector>
#include <unordered_set>
using namespace std;

class Solution {
public:
    bool isValidSudoku(vector<vector<char>>& board) {
        unordered_set<char> rows[9], cols[9], boxes[9];
        for (int r = 0; r < 9; r++) {
            for (int c = 0; c < 9; c++) {
                char v = board[r][c];
                if (v == '.') continue;
                int b = (r / 3) * 3 + c / 3;
                if (!rows[r].insert(v).second ||
                    !cols[c].insert(v).second ||
                    !boxes[b].insert(v).second)
                    return false;
            }
        }
        return true;
    }
};
```

## Why it works

The box formula maps each cell to the index of the 3×3 block that contains it, so `boxes[b]` accumulates exactly the digits of that block. If inserting into `rows[r]` fails the digit already appeared in the row and we stop; otherwise it is now recorded and we test the column, then the box. When a check on the left fails, short-circuiting skips the remaining inserts, which is harmless because we are returning `false` anyway.

## Complexity

For an `N×N` board (here `N = 9`):

- Time: O(N²) — one pass over the N² cells, each doing O(1) set work.
- Space: O(N²) — the row, column, and box sets together retain every filled digit.
