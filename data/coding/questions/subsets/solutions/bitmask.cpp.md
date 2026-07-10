Every subset of an `n`-element array corresponds to one of the `2^n` binary strings of length `n` — bit `i` set means "include `nums[i]`". Loop a counter from `0` to `2^n - 1` and read off its bits to build each subset directly, with no recursion at all.

It's the most mechanical way to enumerate a power set, and a good baseline before reaching for backtracking.

```cpp
#include <vector>
#include <algorithm>
using namespace std;

class Solution {
public:
    vector<vector<int>> subsets(vector<int>& nums) {
        int n = nums.size();
        vector<vector<int>> result;
        for (int mask = 0; mask < (1 << n); mask++) {
            vector<int> subset;
            for (int i = 0; i < n; i++) {
                if (mask & (1 << i)) subset.push_back(nums[i]);
            }
            result.push_back(subset);
        }
        sort(result.begin(), result.end(), [](const vector<int>& a, const vector<int>& b) {
            if (a.size() != b.size()) return a.size() < b.size();
            return a < b;
        });
        return result;
    }
};
```

## Why it works

Each of the `2^n` values of `mask` is a unique bit pattern, and each bit pattern selects a unique combination of elements — so the loop visits every subset exactly once. Sorting by length then contents afterward just fixes a canonical order; it doesn't change which subsets are found.

## Complexity

- Time: O(n * 2^n) — 2^n masks, each scanned in O(n) to build its subset (plus a sort).
- Space: O(n * 2^n) — the output holds all subsets, each up to length n.
