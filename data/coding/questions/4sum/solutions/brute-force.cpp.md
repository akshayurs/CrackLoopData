The honest baseline: examine every group of four distinct indices and keep those whose values sum to `target`. Four nested loops enumerate all combinations directly.

Sorting first means each combination `i < j < k < l` is already non-decreasing, so a `set<vector<int>>` both deduplicates and stores the quadruplets in ascending order for free. The sum is accumulated as a `long long` to avoid 32-bit overflow.

```cpp
#include <vector>
#include <algorithm>
#include <set>
using namespace std;

class Solution {
public:
    vector<vector<int>> fourSum(vector<int>& nums, int target) {
        sort(nums.begin(), nums.end());
        int n = nums.size();
        set<vector<int>> found;
        for (int i = 0; i < n; i++)
            for (int j = i + 1; j < n; j++)
                for (int k = j + 1; k < n; k++)
                    for (int l = k + 1; l < n; l++)
                        if ((long long) nums[i] + nums[j] + nums[k] + nums[l] == target)
                            found.insert({nums[i], nums[j], nums[k], nums[l]});
        return vector<vector<int>>(found.begin(), found.end());
    }
};
```

## Why it works

The loops walk strictly increasing indices, so each unordered quadruplet of positions is tried once. Sorting makes every stored vector non-decreasing, and `set<vector<int>>` discards duplicate value-groups while keeping them ordered, so iterating the set yields the canonical result. Casting to `long long` before adding prevents overflow.

## Complexity

- Time: O(n^4) — every quadruplet of indices is inspected.
- Space: O(m) — the set holds the m distinct matching quadruplets.
