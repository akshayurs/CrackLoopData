Close in from both ends. As long as the characters match, keep moving the pointers toward the middle — that part is already palindromic. The moment they disagree, exactly one of two repairs must save the string: delete the left character or delete the right one.

So on the first mismatch, check whether the substring with the left character skipped is a palindrome, or the one with the right character skipped. If either holds, one deletion is enough; if neither does, no single deletion can fix it.

```cpp
#include <string>
using namespace std;

class Solution {
public:
    bool validPalindrome(string s) {
        int i = 0, j = (int)s.size() - 1;
        while (i < j) {
            if (s[i] != s[j]) {
                return isPal(s, i + 1, j) || isPal(s, i, j - 1);
            }
            i++;
            j--;
        }
        return true;
    }

private:
    bool isPal(const string& s, int i, int j) {
        while (i < j) {
            if (s[i++] != s[j--]) return false;
        }
        return true;
    }
};
```

## Why it works

Every matched pair before the first mismatch is fixed and correct, so no deletion should touch it. At the mismatch `s[i] != s[j]`, a valid palindrome can only be reached by removing one of those two characters — any other deletion leaves this pair broken. Verifying both remaining ranges covers both choices, and each is a plain palindrome check with no further deletions allowed.

## Complexity

- Time: O(n) — the outer scan is linear, and at most one branch triggers a single extra linear check.
- Space: O(1) — only index variables are used.
