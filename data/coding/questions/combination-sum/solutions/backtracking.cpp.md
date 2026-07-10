Explore every way to build a running sum out of the candidates, one number at a time, and only judge a path once it bottoms out. To avoid counting `[2, 3]` and `[3, 2]` as different answers, only ever pick a candidate at or after the index you picked last — that forces each combination to come out non-decreasing.

This version does no bookkeeping beyond that index rule: it recurses into every candidate at every position and lets the remaining-sum check at the base case decide success or failure, even for branches that were already hopeless several calls earlier.

```cpp
#include <vector>
#include <algorithm>
using namespace std;

class Solution {
public:
    vector<vector<int>> combinationSum(vector<int>& candidates, int target) {
        sort(candidates.begin(), candidates.end());
        vector<vector<int>> result;
        vector<int> path;
        backtrack(candidates, target, 0, path, result);
        return result;
    }

private:
    void backtrack(vector<int>& candidates, int remaining, int start,
                    vector<int>& path, vector<vector<int>>& result) {
        if (remaining == 0) {
            result.push_back(path);
            return;
        }
        if (remaining < 0) {
            return;
        }
        for (int i = start; i < (int)candidates.size(); i++) {
            path.push_back(candidates[i]);
            backtrack(candidates, remaining - candidates[i], i, path, result);
            path.pop_back();
        }
    }
};
```

## Why it works

`backtrack` tries every candidate from `start` onward, pushing it onto `path` and recursing with the same index (reuse is allowed) and a smaller `remaining`. Restricting the next pick to index `start` or later means a combination is only ever built in one order, so no duplicate permutation of the same multiset is recorded. Sorting `candidates` first only affects the order combinations are discovered in, which keeps the output list itself sorted; every branch is still walked to completion or to a negative `remaining` before it is abandoned.

## Complexity

- Time: O(2^target) — in the worst case (small candidates, large target) the recursion tree branches at nearly every unit of remaining sum before the negative check prunes it.
- Space: O(target) — the recursion depth and `path` are bounded by how many times the smallest candidate divides into `target`.
