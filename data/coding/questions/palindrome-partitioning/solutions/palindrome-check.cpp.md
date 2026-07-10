Explore every way to cut the string using backtracking: at each position, try every possible next piece, and only recurse into it if that piece is itself a palindrome. When the cut reaches the end of the string, the path taken so far is one valid partition.

Checking whether a candidate piece is a palindrome is done fresh every time with a simple two-pointer scan — no precomputation. Sorting the collected results at the end guarantees deterministic output.

```cpp
#include <string>
#include <vector>
#include <algorithm>
using namespace std;

class Solution {
public:
    vector<vector<string>> partition(string s) {
        vector<vector<string>> result;
        vector<string> path;
        backtrack(s, 0, path, result);
        sort(result.begin(), result.end());
        return result;
    }

private:
    bool isPalindrome(const string& s, int l, int r) {
        while (l < r) {
            if (s[l] != s[r]) return false;
            l++;
            r--;
        }
        return true;
    }

    void backtrack(const string& s, int start, vector<string>& path, vector<vector<string>>& result) {
        if (start == (int)s.size()) {
            result.push_back(path);
            return;
        }
        for (int end = start; end < (int)s.size(); end++) {
            if (isPalindrome(s, start, end)) {
                path.push_back(s.substr(start, end - start + 1));
                backtrack(s, end + 1, path, result);
                path.pop_back();
            }
        }
    }
};
```

## Why it works

Every partition of `s` corresponds to a sequence of cut points; the backtracking loop tries each possible next cut in increasing order and only commits to it when the resulting piece is a palindrome, so every branch it explores is a valid prefix of a legal partition. Popping the last element of `path` after each recursive call undoes the choice so sibling branches start clean. Because the recursion only ever records a complete partition when it consumes the whole string, no partial or invalid partition ever lands in `result`.

## Complexity

- Time: O(n^2 * 2^n) — there are up to 2^(n-1) ways to place cuts, and each palindrome check costs up to O(n).
- Space: O(n) — recursion depth and the current `path`, excluding the output.
