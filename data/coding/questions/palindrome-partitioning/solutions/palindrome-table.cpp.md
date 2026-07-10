The brute-force approach re-scans a piece from scratch every time it wants to know whether that piece is a palindrome, and the same substring gets checked over and over across different branches. Instead, build a table once: `dp[l][r]` is true when `s[l..r]` is a palindrome. It fills in O(1) per cell using the fact that `s[l..r]` is a palindrome exactly when its endpoints match and the inside (`s[l+1..r-1]`) is also a palindrome.

With that table in hand, the same backtracking walk over cut points becomes a plain O(1) lookup instead of a fresh scan, so the only remaining cost is the work of actually building each partition.

```cpp
#include <string>
#include <vector>
#include <algorithm>
using namespace std;

class Solution {
public:
    vector<vector<string>> partition(string s) {
        int n = s.size();
        vector<vector<bool>> dp(n, vector<bool>(n, false));
        for (int r = 0; r < n; r++) {
            for (int l = r; l >= 0; l--) {
                if (s[l] == s[r] && (r - l < 2 || dp[l + 1][r - 1])) {
                    dp[l][r] = true;
                }
            }
        }

        vector<vector<string>> result;
        vector<string> path;
        backtrack(s, 0, dp, path, result);
        sort(result.begin(), result.end());
        return result;
    }

private:
    void backtrack(const string& s, int start, const vector<vector<bool>>& dp,
                    vector<string>& path, vector<vector<string>>& result) {
        if (start == (int)s.size()) {
            result.push_back(path);
            return;
        }
        for (int end = start; end < (int)s.size(); end++) {
            if (dp[start][end]) {
                path.push_back(s.substr(start, end - start + 1));
                backtrack(s, end + 1, dp, path, result);
                path.pop_back();
            }
        }
    }
};
```

## Why it works

Filling `dp` by increasing right endpoint (and for each, decreasing left endpoint) guarantees `dp[l + 1][r - 1]` is already known before `dp[l][r]` is computed, so each cell is a genuine O(1) decision from two smaller, already-solved subproblems. The backtracking step is unchanged in structure from the brute force — it still tries every cut point and only recurses when the piece is a palindrome — but the lookup replaces an O(n) scan, so the exponential work of enumerating partitions is no longer multiplied by a linear palindrome check.

## Complexity

- Time: O(n^2 + n * 2^n) — O(n^2) to build the table, plus O(1) per cut-point check across the up to 2^(n-1) partitions, each of length up to n.
- Space: O(n^2) — the palindrome table, plus O(n) for the recursion and current `path`.
