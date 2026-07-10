Drop the separate `visited` grid entirely — mark the current cell by overwriting it with a sentinel character while it is part of the path, then restore the original letter on the way back out. That removes an O(m·n) boolean array without changing what gets explored.

Before searching at all, count the letters in `word` and in `board`. If `word` needs more of some letter than the board has, no trace can possibly exist, so the search is skipped entirely — a cheap check that rejects many impossible cases in O(m·n) instead of paying for a failed DFS.

```cpp
#include <vector>
#include <string>
#include <array>
using namespace std;

class Solution {
public:
    bool exist(vector<vector<char>>& board, string word) {
        rows = board.size();
        cols = board[0].size();

        array<int, 128> counts{};
        for (auto& row : board) for (char ch : row) counts[ch]++;
        for (char ch : word) {
            if (--counts[(unsigned char)ch] < 0) return false;
        }

        for (int r = 0; r < rows; r++) {
            for (int c = 0; c < cols; c++) {
                if (dfs(board, word, r, c, 0)) return true;
            }
        }
        return false;
    }

private:
    int rows, cols;

    bool dfs(vector<vector<char>>& board, const string& word, int r, int c, int i) {
        if (i == (int)word.size()) return true;
        if (r < 0 || r >= rows || c < 0 || c >= cols || board[r][c] != word[i]) return false;

        char original = board[r][c];
        board[r][c] = '#';
        bool found = dfs(board, word, r + 1, c, i + 1) || dfs(board, word, r - 1, c, i + 1) ||
                     dfs(board, word, r, c + 1, i + 1) || dfs(board, word, r, c - 1, i + 1);
        board[r][c] = original;
        return found;
    }
};
```

## Why it works

Overwriting `board[r][c]` with `'#'` — a value that can never equal a letter of `word` — is equivalent to marking it visited, since the very next comparison in `dfs` rejects that cell for the rest of the current path. Restoring the original letter after the recursive calls return is the backtrack step, so sibling branches and later starting cells see the untouched board. The letter-count check is a necessary condition for a trace to exist: decrementing counts while scanning `word` and bailing the moment one goes negative rejects impossible cases in O(m·n + L) instead of paying for a failed DFS.

## Complexity

- Time: O(m · n · 4^L) worst case (O(m · n · 3^(L-1)) in practice, since the cell just entered from can't be revisited) — the frequency check adds only O(m · n + L).
- Space: O(L) — recursion depth only; the board is mutated in place instead of allocating a visited structure.
