When many queries share the same `t`, the linear scan re-reads all of `t` every time — wasteful. Instead, preprocess `t` once into a map from each character to the sorted list of positions where it occurs. Then a query only touches positions relevant to `s`.

For each character of `s`, we need the earliest occurrence in `t` that comes *after* the position we matched last. Since each character's positions are sorted, a binary search (upper bound of the previous index) finds it in logarithmic time. If any character has no such later position, `s` cannot be embedded.

```cpp
#include <string>
#include <vector>
#include <unordered_map>
#include <algorithm>
using namespace std;

class Solution {
public:
    bool isSubsequence(string s, string t) {
        unordered_map<char, vector<int>> positions;
        for (int i = 0; i < (int)t.size(); i++) {
            positions[t[i]].push_back(i);
        }
        int prev = -1;
        for (char c : s) {
            auto it = positions.find(c);
            if (it == positions.end()) return false;
            const vector<int>& idxs = it->second;
            auto pos = upper_bound(idxs.begin(), idxs.end(), prev);
            if (pos == idxs.end()) return false;
            prev = *pos;
        }
        return true;
    }
};
```

## Why it works

`positions[c]` lists, in increasing order, every index of `c` in `t`. Maintaining `prev` (the index we last consumed), the next character must land at some index strictly greater than `prev`; `upper_bound` returns the first stored index that exceeds `prev`. Advancing to the smallest valid index is the greedy choice — the same reasoning as the two-pointer scan — so it never rejects an embeddable string. Missing character or exhausted positions means no valid match remains.

## Complexity

- Time: O(n + m·log n) — building the index over `t` (length n), then each of the m = s.size() characters does one binary search.
- Space: O(n) — every position of `t` is stored once.
