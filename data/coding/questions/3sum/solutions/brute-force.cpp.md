The honest baseline: examine every combination of three distinct indices and keep the ones that sum to zero. The same three values can be reached through different index combinations, so we canonicalize each hit by sorting its three numbers and storing it in a `set`, which both de-duplicates and keeps the results ordered.

Because `std::set<vector<int>>` orders its elements lexicographically, copying it into a vector at the end already yields the required canonical order.

```cpp
#include <vector>
#include <set>
#include <algorithm>
using namespace std;

class Solution {
public:
    vector<vector<int>> threeSum(vector<int>& nums) {
        int n = (int)nums.size();
        set<vector<int>> found;
        for (int i = 0; i < n; i++)
            for (int j = i + 1; j < n; j++)
                for (int k = j + 1; k < n; k++)
                    if (nums[i] + nums[j] + nums[k] == 0) {
                        vector<int> t = {nums[i], nums[j], nums[k]};
                        sort(t.begin(), t.end());
                        found.insert(t);
                    }
        return vector<vector<int>>(found.begin(), found.end());
    }
};
```

## Why it works

Every unordered triple of indices is visited exactly once by the three nested loops. Sorting each zero-sum triple before inserting it collapses permutations of the same three values into one element, and `std::set` rejects the duplicates. Iterating the set in order produces triplets sorted lexicographically — exactly the canonical output.

## Complexity

- Time: O(n³) — every triple of indices is tested.
- Space: O(m) — the set holds the m unique triplets found.
