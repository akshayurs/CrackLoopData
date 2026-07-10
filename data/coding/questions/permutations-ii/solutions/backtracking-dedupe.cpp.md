Rather than generating every arrangement and cleaning up afterward, avoid building duplicates at all. Sort the vector so equal values sit next to each other, then only let a repeated value start a new branch once the previous copy of that value has already been placed in the current path.

The pruning rule: at a given depth, skip index `i` if `nums[i] == nums[i - 1]` and the earlier copy is not currently in use. That fixes the relative order equal values can be placed in, which removes duplicate permutations at the source instead of filtering them out later.

```cpp
#include <vector>
#include <algorithm>
using namespace std;

class Solution {
public:
    vector<vector<int>> permuteUnique(vector<int>& nums) {
        sort(nums.begin(), nums.end());
        vector<bool> used(nums.size(), false);
        vector<int> current;
        vector<vector<int>> result;
        backtrack(nums, used, current, result);
        return result;
    }

private:
    void backtrack(vector<int>& nums, vector<bool>& used, vector<int>& current, vector<vector<int>>& result) {
        if (current.size() == nums.size()) {
            result.push_back(current);
            return;
        }
        for (int i = 0; i < (int)nums.size(); i++) {
            if (used[i]) continue;
            if (i > 0 && nums[i] == nums[i - 1] && !used[i - 1]) continue;
            used[i] = true;
            current.push_back(nums[i]);
            backtrack(nums, used, current, result);
            current.pop_back();
            used[i] = false;
        }
    }
};
```

## Why it works

Sorting groups equal values together. If two equal values are both available at the same depth, placing the later one before the earlier one has been used would reach a permutation already reachable by placing the earlier one first — so that branch is redundant and can be pruned without losing any distinct result. Because `nums` is sorted and indices are tried in increasing order, the recursion also emits results already in lexicographic order.

## Complexity

- Time: O(n! · n) worst case (all distinct values) — pruning only removes branches that would duplicate output; each surviving branch still costs O(n) to materialize.
- Space: O(n) for the recursion stack, `used`, and `current`, plus O(n! · n) for the collected output.
