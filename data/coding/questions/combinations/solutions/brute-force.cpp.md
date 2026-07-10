The most direct reading of the problem: every subset of `{1, ..., n}` is a candidate, so walk through all `2^n` of them and keep the ones with exactly `k` elements. A bitmask from `0` to `2^n - 1` is a compact way to represent "which numbers are in this subset" — bit `i` set means `i + 1` is included.

Because masks aren't visited in an order that matches sorted combinations, the collected list needs an explicit sort at the end to make the output deterministic.

```cpp
#include <vector>
#include <algorithm>
using namespace std;

class Solution {
public:
    vector<vector<int>> combine(int n, int k) {
        vector<vector<int>> result;
        for (int mask = 0; mask < (1 << n); mask++) {
            int bits = 0;
            for (int m = mask; m; m >>= 1) bits += m & 1;
            if (bits == k) {
                vector<int> combo;
                for (int i = 0; i < n; i++) {
                    if (mask & (1 << i)) combo.push_back(i + 1);
                }
                result.push_back(combo);
            }
        }
        sort(result.begin(), result.end());
        return result;
    }
};
```

## Why it works

Every subset of `{1, ..., n}` corresponds to exactly one `n`-bit mask, so iterating masks from `0` to `2^n - 1` enumerates every subset without duplicates or omissions. Counting set bits filters for size-`k` subsets, and decoding a mask's bits from low to high builds each combination already in increasing order. `sort` on the vector of vectors performs lexicographic comparison, which fixes the order *between* combinations since mask value does not correspond to it.

## Complexity

- Time: O(2^n * n) — every mask is inspected and decoded in O(n), plus a sort over the O(C(n, k)) matches.
- Space: O(n) — auxiliary space to decode a mask, excluding the returned combinations.
