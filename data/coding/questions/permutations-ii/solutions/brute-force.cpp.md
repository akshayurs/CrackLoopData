The same idea in C++: build every position-based arrangement of the vector, as if the values were all distinct, then let a set collapse the ones that repeat.

A recursive backtrack over indices produces all `n!` orderings. `std::set<vector<int>>` compares its keys element-wise, so inserting every finished permutation both deduplicates by value and keeps them sorted automatically — no separate sort step is needed.

```cpp
#include <vector>
#include <set>
using namespace std;

class Solution {
public:
    vector<vector<int>> permuteUnique(vector<int>& nums) {
        set<vector<int>> unique;
        vector<bool> used(nums.size(), false);
        vector<int> current;
        backtrack(nums, used, current, unique);
        return vector<vector<int>>(unique.begin(), unique.end());
    }

private:
    void backtrack(vector<int>& nums, vector<bool>& used, vector<int>& current, set<vector<int>>& unique) {
        if (current.size() == nums.size()) {
            unique.insert(current);
            return;
        }
        for (int i = 0; i < (int)nums.size(); i++) {
            if (used[i]) continue;
            used[i] = true;
            current.push_back(nums[i]);
            backtrack(nums, used, current, unique);
            current.pop_back();
            used[i] = false;
        }
    }
};
```

## Why it works

The backtrack picks every unused index at each depth, so it enumerates all `n!` position-based orderings regardless of repeated values. `std::set` orders keys by `operator<`, which for `vector<int>` is lexicographic comparison, and rejects an insert if an equal key already exists — so identical arrangements collapse into one entry, already sorted.

## Complexity

- Time: O(n! · n log(n!)) — n! permutations, each an O(n) comparison against an O(log(n!))-deep tree during insertion.
- Space: O(n! · n) — the set holds every distinct permutation.
