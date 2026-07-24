Trade a little memory for a single pass. Walk the vector once, keeping a hash set of everything seen so far. Before recording a value, check whether it is already in the set — if so, that value is a duplicate.

The `unordered_set` gives O(1) membership tests, so we never need the nested loop or a sort; the answer often comes long before the vector ends. `insert` returns a pair whose `second` is `false` when the value already existed, folding the check and insert into one call.

```cpp
#include <vector>
#include <unordered_set>
using namespace std;

class Solution {
public:
    bool containsDuplicate(vector<int>& nums) {
        unordered_set<int> seen;
        for (int n : nums) {
            if (!seen.insert(n).second) {
                return true;
            }
        }
        return false;
    }
};
```

## Why it works

`seen` holds exactly the values encountered before the current one. `insert` adds `n` and reports `false` in its `.second` field if the value was already present — meaning we met it earlier in the vector, which is exactly a duplicate. If every insert is fresh, no value was ever seen twice.

## Complexity

- Time: O(n) — one pass; each set lookup and insert is O(1) on average.
- Space: O(n) — the set may hold every distinct value.
