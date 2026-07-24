Instead of rebuilding a whole vector of partial results at every digit, grow one combination at a time in a shared buffer. Pick a letter for the current digit, recurse into the next digit, and once the buffer is as long as `digits` record it. When the recursive call returns, undo the last choice ("backtrack") and try the next letter.

This produces the same combinations as brute-force expansion but never materializes intermediate partial vectors — only the final results and a single path buffer exist at once.

```cpp
#include <vector>
#include <string>
using namespace std;

class Solution {
public:
    vector<string> letterCombinations(string digits) {
        vector<string> result;
        if (digits.empty()) {
            return result;
        }
        string path;
        backtrack(digits, 0, path, result);
        return result;
    }

private:
    const vector<string> keypad = {"", "", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"};

    void backtrack(const string& digits, int index, string& path, vector<string>& result) {
        if (index == (int)digits.size()) {
            result.push_back(path);
            return;
        }
        const string& letters = keypad[digits[index] - '0'];
        for (char letter : letters) {
            path.push_back(letter);
            backtrack(digits, index + 1, path, result);
            path.pop_back();
        }
    }
};
```

## Why it works

`path` always holds the letters chosen for digits `0..index-1`. At depth `index == digits.size()`, `path` is one complete combination, so it is recorded. Trying every letter of the current digit before returning, and popping the last character after each recursive call, ensures every branch is explored and the buffer is restored for the sibling choice — so all `4^n` combinations are generated exactly once, none skipped, none duplicated.

## Complexity

- Time: O(4^n) — n is `digits.size()`; the recursion tree has one leaf per combination, and building each combination costs O(n).
- Space: O(n) beyond the output — the recursion depth and `path` buffer are bounded by `digits.size()`; the output vector itself holds all combinations.
