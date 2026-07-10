The same idea in C++: a bitmask tracks which numbers are used, and `remaining` tracks how much is left to fill the current bucket. Numbers are sorted descending first so impossible cases fail fast, and an unordered_map memoizes on the combined `(mask, remaining)` state so repeated states are never re-explored.

```cpp
#include <vector>
#include <numeric>
#include <algorithm>
#include <unordered_map>
using namespace std;

class Solution {
public:
    bool canPartitionKSubsets(vector<int>& nums, int k) {
        int total = accumulate(nums.begin(), nums.end(), 0);
        if (total % k != 0) return false;
        target = total / k;
        sort(nums.begin(), nums.end(), greater<int>());
        this->nums = nums;
        n = (int)nums.size();
        if (nums[0] > target) return false;
        return dfs(0, target);
    }

private:
    vector<int> nums;
    int target;
    int n;
    unordered_map<long long, bool> memo;

    bool dfs(int mask, int remaining) {
        if (mask == (1 << n) - 1) return true;
        long long key = ((long long)mask << 20) | remaining;
        auto it = memo.find(key);
        if (it != memo.end()) return it->second;
        bool ok = false;
        for (int i = 0; i < n; i++) {
            if ((mask & (1 << i)) || nums[i] > remaining) continue;
            int nextRemaining = remaining - nums[i];
            if (nextRemaining == 0) nextRemaining = target;
            if (dfs(mask | (1 << i), nextRemaining)) {
                ok = true;
                break;
            }
        }
        memo[key] = ok;
        return ok;
    }
};
```

## Why it works

`mask` records exactly which numbers are already assigned; `remaining` is how much room is left in the bucket currently being filled. Trying index `i` only when it is unused and fits within `remaining` mirrors plain backtracking, but whenever a bucket exactly fills (`nextRemaining == 0`) we reset to a fresh `target` and start the next bucket. Reaching the full mask means a valid k-way partition was built. Memoizing on the packed `(mask, remaining)` key avoids recomputing states reached by different orderings of the same used set.

## Complexity

- Time: O(n * 2^n) — at most 2^n distinct masks, each doing O(n) work to try the next number.
- Space: O(2^n) — the memo map, keyed by mask and remaining.
