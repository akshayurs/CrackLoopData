Reduce 4Sum to a familiar shape: sort the array, fix the two outer values with a double loop, then let a two-pointer sweep close the remaining pair in linear time. Sorting is what makes both the pointer logic and duplicate-skipping possible.

For each fixed `(i, j)`, `lo` starts just after `j` and `hi` at the end. If the four-way sum is too small, advancing `lo` raises it; too large, dropping `hi` lowers it; on a hit we record the quadruplet and step both pointers past any repeats. The sum is held in a `long long` so four billion-scale values cannot overflow.

```cpp
#include <vector>
#include <algorithm>
using namespace std;

class Solution {
public:
    vector<vector<int>> fourSum(vector<int>& nums, int target) {
        sort(nums.begin(), nums.end());
        int n = nums.size();
        vector<vector<int>> res;
        for (int i = 0; i < n - 3; i++) {
            if (i > 0 && nums[i] == nums[i - 1]) continue;
            for (int j = i + 1; j < n - 2; j++) {
                if (j > i + 1 && nums[j] == nums[j - 1]) continue;
                int lo = j + 1, hi = n - 1;
                while (lo < hi) {
                    long long total = (long long) nums[i] + nums[j] + nums[lo] + nums[hi];
                    if (total == target) {
                        res.push_back({nums[i], nums[j], nums[lo], nums[hi]});
                        lo++; hi--;
                        while (lo < hi && nums[lo] == nums[lo - 1]) lo++;
                        while (lo < hi && nums[hi] == nums[hi + 1]) hi--;
                    } else if (total < target) {
                        lo++;
                    } else {
                        hi--;
                    }
                }
            }
        }
        return res;
    }
};
```

## Why it works

On a sorted array the two-pointer sweep is exhaustive: moving `lo` only increases the sum and moving `hi` only decreases it, so no valid pair between them is skipped. The four guards ensure each distinct value combination is emitted once. Casting to `long long` before adding prevents overflow. Ascending outer values plus an inward pair scan give quadruplets in canonical order.

## Complexity

- Time: O(n^3) — two nested loops times a linear pointer sweep, after an O(n log n) sort.
- Space: O(1) — ignoring the output, only pointers and counters are used.
