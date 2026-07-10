The same idea in C++: recurse over the array, and for each number try every bucket that still has room under the target sum. A full assignment wins if all buckets end up exactly at the target.

No memoization here — just the empty-bucket prune, which skips trying the same failed number in a second empty bucket.

```cpp
#include <vector>
#include <numeric>
using namespace std;

class Solution {
public:
    bool canPartitionKSubsets(vector<int>& nums, int k) {
        int total = accumulate(nums.begin(), nums.end(), 0);
        if (total % k != 0) return false;
        target = total / k;
        buckets.assign(k, 0);
        return backtrack(nums, 0);
    }

private:
    vector<int> buckets;
    int target;

    bool backtrack(vector<int>& nums, int i) {
        if (i == (int)nums.size()) {
            for (int b : buckets) {
                if (b != target) return false;
            }
            return true;
        }
        for (int j = 0; j < (int)buckets.size(); j++) {
            if (buckets[j] + nums[i] <= target) {
                buckets[j] += nums[i];
                if (backtrack(nums, i + 1)) return true;
                buckets[j] -= nums[i];
            }
            if (buckets[j] == 0) break;
        }
        return false;
    }
};
```

## Why it works

`buckets[j]` tracks the running sum of the j-th subset. A number is only placed where it fits under `target`, and a failed placement is undone before the next bucket is tried. The `if (buckets[j] == 0) break` prune skips redundant empty buckets, since a failed attempt in one empty bucket would fail identically in any other empty bucket. Success requires every bucket to land exactly on `target`.

## Complexity

- Time: O(k^n) — each of the n numbers can go into any of k buckets in the worst case.
- Space: O(k + n) — bucket sums plus the recursion stack.
