Explore every way of including or excluding each position: at index `i` you either take `candidates[i]` and recurse, or skip it and recurse. That walks every subset of the array, and any subset whose running sum lands exactly on the target gets recorded.

Duplicate values in the input mean different subsets of indices can produce the same list of numbers, so the raw hits need deduplication. Sorting the candidates first and inserting each hit into a `set<vector<int>>` handles both the dedup and the lexicographic ordering, since that's the container's default comparison.

```cpp
#include <vector>
#include <algorithm>
#include <set>
using namespace std;

class Solution {
public:
    vector<vector<int>> combinationSum2(vector<int>& candidates, int target) {
        sort(candidates.begin(), candidates.end());
        set<vector<int>> seen;
        vector<int> path;
        backtrack(candidates, 0, target, path, seen);
        return vector<vector<int>>(seen.begin(), seen.end());
    }

private:
    void backtrack(vector<int>& c, int i, int remaining, vector<int>& path, set<vector<int>>& seen) {
        if (remaining == 0) {
            seen.insert(path);
            return;
        }
        if (remaining < 0 || i == (int)c.size()) return;
        path.push_back(c[i]);
        backtrack(c, i + 1, remaining - c[i], path, seen);
        path.pop_back();
        backtrack(c, i + 1, remaining, path, seen);
    }
};
```

## Why it works

Every combination corresponds to exactly one path through the include/exclude decision tree over indices, so nothing valid is missed. Sorting the array up front means each recorded path already lists its numbers ascending; `set<vector<int>>` compares vectors lexicographically by default, so it both deduplicates repeated combinations and leaves the result already in the required order.

## Complexity

- Time: O(2^n · n log n) — every index is included or excluded, and each of the up to 2^n paths costs O(n log n) to insert/order in the tree.
- Space: O(2^n · n) — the set can hold up to 2^n combinations of length up to n.
