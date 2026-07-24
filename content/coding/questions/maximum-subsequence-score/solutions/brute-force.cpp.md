Sort the pairs by `nums2` descending. Once sorted this way, the smallest `nums2` value inside any prefix is always the last element of that prefix — so if the chosen `k` indices are made to come from a prefix, that last element is automatically the multiplier. For each prefix long enough to hold `k` items, re-sort just that prefix's `nums1` values and add up the `k` largest.

It is wasteful to re-sort the same numbers over and over as the prefix grows, but it is the natural first attempt: check every candidate pivot directly.

```cpp
#include <vector>
#include <algorithm>
#include <numeric>
using namespace std;

class Solution {
public:
    long long maxScore(vector<int>& nums1, vector<int>& nums2, int k) {
        int n = nums1.size();
        vector<int> idx(n);
        iota(idx.begin(), idx.end(), 0);
        sort(idx.begin(), idx.end(), [&](int a, int b) { return nums2[a] > nums2[b]; });

        long long best = 0;
        for (int i = k - 1; i < n; i++) {
            vector<int> prefix;
            for (int j = 0; j <= i; j++) prefix.push_back(nums1[idx[j]]);
            sort(prefix.rbegin(), prefix.rend());
            long long sum = 0;
            for (int j = 0; j < k; j++) sum += prefix[j];
            best = max(best, sum * (long long)nums2[idx[i]]);
        }
        return best;
    }
};
```

## Why it works

Any valid `k`-index choice has some element with the smallest `nums2`; call its value `m`. Restricting attention to indices whose `nums2 >= m` and picking the `k` largest `nums1` among them can only help the sum without lowering the multiplier below `m`. Sorting by `nums2` descending turns "indices with `nums2 >= nums2[idx[i]]`" into exactly the prefix `idx[0..i]`, so scanning every possible pivot `i` and taking the best `k` `nums1` values from its prefix covers every optimal choice.

## Complexity

- Time: O(n² log n) — up to n prefixes, each re-sorted from scratch.
- Space: O(n) — the index array and a rebuilt prefix each iteration.
