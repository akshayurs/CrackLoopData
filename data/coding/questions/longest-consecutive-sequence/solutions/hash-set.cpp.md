Sorting is wasteful — we don't need the full order, only the ability to ask "is `x` present?" in O(1). Drop every value into an `unordered_set`, then walk the values and count a run only from its left end: a value `n` is a run start exactly when `n - 1` is absent. From each start, step forward while the next integer exists.

The trick that keeps this linear is starting only at run beginnings. Every value is visited by the outer loop once, and the inner walk touches each value at most once across the whole algorithm, so the total work is O(n) even though it looks nested.

```cpp
#include <vector>
#include <unordered_set>
#include <algorithm>
using namespace std;

class Solution {
public:
    int longestConsecutive(vector<int>& nums) {
        unordered_set<int> values(nums.begin(), nums.end());
        int best = 0;
        for (int n : values) {
            if (values.count(n - 1)) continue;
            int length = 1;
            while (values.count(n + length)) length++;
            best = max(best, length);
        }
        return best;
    }
};
```

## Why it works

The `values.count(n - 1)` guard ensures the inner `while` only fires from the smallest element of each run. That run is then walked exactly once; interior elements are skipped by the guard, so no value is counted twice. Because each run is traversed a single time in total, the combined length of all inner walks is at most n.

## Complexity

- Time: O(n) — each value is inserted into the set once and visited by the inner walk at most once.
- Space: O(n) — the set of all distinct values.
