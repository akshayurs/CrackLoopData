Because a subsequence must keep the original order, we can be greedy: walk through `t` once and try to match the characters of `s` from left to right. Keep a pointer into `s`; every time the current character of `t` equals the character `s` is waiting for, advance that pointer.

If the pointer reaches the end of `s`, every character was matched in order, so `s` is a subsequence. There is never a reason to skip a valid match — taking the earliest possible position for each character can only leave more of `t` available for the rest.

```cpp
#include <string>
using namespace std;

class Solution {
public:
    bool isSubsequence(string s, string t) {
        int i = 0;
        for (char c : t) {
            if (i < (int)s.size() && s[i] == c) {
                i++;
            }
        }
        return i == (int)s.size();
    }
};
```

## Why it works

The pointer `i` counts how many characters of `s` have been matched so far, always at the earliest positions in `t`. Matching greedily is safe: if some valid embedding exists, the leftmost-match strategy finds one too, since choosing an earlier index for a character never blocks a later one. When `i == s.size()` the whole of `s` has been consumed in order. An empty `s` returns `true` immediately because the loop never advances `i`.

## Complexity

- Time: O(n) — a single pass over `t`, where n = t.size().
- Space: O(1) — just one index.
