Two strings are anagrams exactly when their letters, laid out in a canonical order, are identical. Sorting is the simplest way to reach that canonical form: sort the characters of both strings and check that the results match.

It is the honest baseline you would reach for first in an interview — no counting, no bookkeeping, just compare the sorted characters. A quick length check up front rules out the obvious non-anagrams before doing any work.

```cpp
#include <string>
#include <algorithm>
using namespace std;

class Solution {
public:
    bool isAnagram(string s, string t) {
        if (s.size() != t.size()) return false;
        sort(s.begin(), s.end());
        sort(t.begin(), t.end());
        return s == t;
    }
};
```

## Why it works

If `t` is a rearrangement of `s`, then sorting both collapses every rearrangement to the same sequence of characters, so the sorted strings compare equal. If they differ in any letter or in how many times a letter appears, the sorted forms diverge at some position and the comparison fails. The length guard is an early exit — strings of unequal length can never be anagrams.

## Complexity

- Time: O(n log n) — dominated by sorting both strings.
- Space: O(1) extra — the strings are sorted in place (ignoring the by-value copies of the arguments).
