A permutation of `s1` is any string with the exact same multiset of characters. So the most direct check is: slide a window of length `s1.size()` across `s2`, and for each window ask whether its characters are a rearrangement of `s1`'s. Sorting both strings turns "same multiset" into "equal after sorting".

Compare every window's sorted form against the sorted `s1`. If any window matches, a permutation is present.

```cpp
#include <string>
#include <algorithm>
using namespace std;

class Solution {
public:
    bool checkInclusion(string s1, string s2) {
        int n = s1.size(), m = s2.size();
        if (n > m) return false;
        string target = s1;
        sort(target.begin(), target.end());
        for (int i = 0; i + n <= m; i++) {
            string window = s2.substr(i, n);
            sort(window.begin(), window.end());
            if (window == target) return true;
        }
        return false;
    }
};
```

## Why it works

Two strings are permutations of each other exactly when their sorted character sequences are identical. The loop considers every starting position where a length-`n` window fits, so if any substring of that length is a permutation of `s1`, it is found. The early `n > m` guard rules out the impossible case where `s1` is longer than `s2`.

## Complexity

- Time: O(m · n log n) — up to `m` windows, each sorted in O(n log n).
- Space: O(n) — the sorted window and target strings.
