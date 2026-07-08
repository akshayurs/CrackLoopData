If at most one deletion is allowed, the simplest plan is to try every possibility. The string is already fine if it reads the same forwards and backwards; otherwise, remove one character at a time and re-check.

For each index, build the string without that character and test whether the result is a palindrome. If any single removal works — or the original was already a palindrome — the answer is `true`.

```cpp
#include <string>
using namespace std;

class Solution {
public:
    bool validPalindrome(string s) {
        if (isPal(s)) return true;
        for (int i = 0; i < (int)s.size(); i++) {
            string t = s.substr(0, i) + s.substr(i + 1);
            if (isPal(t)) return true;
        }
        return false;
    }

private:
    bool isPal(const string& t) {
        int i = 0, j = (int)t.size() - 1;
        while (i < j) {
            if (t[i++] != t[j--]) return false;
        }
        return true;
    }
};
```

## Why it works

"At most one deletion" means the candidate palindromes are exactly the original string plus the `n` strings obtained by dropping one character. Testing all of them is exhaustive, so a `true` answer is never missed. Each check walks inward from both ends comparing characters.

## Complexity

- Time: O(n²) — up to n deletions, each followed by an O(n) palindrome check.
- Space: O(n) — each trimmed copy takes linear space.
