An anagram is defined purely by letter frequencies, so build a 26-slot count for `p` once and compare it against the count of every length-`|p|` window in `s`. Equal counts mean the window is an anagram of `p`.

This version recounts each window from scratch — the clearest baseline before the sliding-window optimization.

```cpp
#include <vector>
#include <string>
#include <array>
using namespace std;

class Solution {
public:
    vector<int> findAnagrams(string s, string p) {
        int m = p.size(), n = s.size();
        vector<int> result;
        if (m > n) return result;
        array<int, 26> target = countOf(p, 0, m);
        for (int i = 0; i + m <= n; i++) {
            if (countOf(s, i, i + m) == target) result.push_back(i);
        }
        return result;
    }
private:
    array<int, 26> countOf(const string& s, int lo, int hi) {
        array<int, 26> c{};
        for (int i = lo; i < hi; i++) c[s[i] - 'a']++;
        return c;
    }
};
```

## Why it works

`countOf` tallies how many of each of the 26 lowercase letters a slice contains. A substring is an anagram of `p` exactly when its tally equals `target`. Checking every window of width `m` finds all matches, and the left-to-right scan produces indices in ascending order.

## Complexity

- Time: O(n * m) — for each of the ~n start positions we build and compare a count over m characters.
- Space: O(1) — each count array holds 26 fixed slots.
