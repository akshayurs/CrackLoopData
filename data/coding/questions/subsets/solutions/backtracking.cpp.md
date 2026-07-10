Think of building a subset one decision at a time: walk the array left to right, and at each index either take the element or skip it. Recording the current partial subset *at every step of the walk* — not just at the end — captures every prefix-consistent combination, because every subset is exactly the set of elements taken along one root-to-node path of that decision tree.

Passing a `start` index instead of a "used" flag per element avoids ever revisiting an earlier index, so each combination is built in increasing index order and produced exactly once — no duplicate subsets to filter out.

```cpp
#include <vector>
#include <algorithm>
using namespace std;

class Solution {
public:
    vector<vector<int>> subsets(vector<int>& nums) {
        vector<vector<int>> result;
        vector<int> path;
        backtrack(nums, 0, path, result);
        sort(result.begin(), result.end(), [](const vector<int>& a, const vector<int>& b) {
            if (a.size() != b.size()) return a.size() < b.size();
            return a < b;
        });
        return result;
    }

private:
    void backtrack(vector<int>& nums, int start, vector<int>& path, vector<vector<int>>& result) {
        result.push_back(path);
        for (int i = start; i < (int)nums.size(); i++) {
            path.push_back(nums[i]);
            backtrack(nums, i + 1, path, result);
            path.pop_back();
        }
    }
};
```

## Why it works

`backtrack(start)` first records the current `path` as a valid subset — including the empty one on the first call — then tries extending it with every element from `start` onward. Recursing with `i + 1` forbids picking an earlier index again, so the same set of values can never be assembled twice. `pop_back` after the recursive call restores `path` before the next sibling choice is tried, which is the "undo" step that makes it backtracking.

## Complexity

- Time: O(n * 2^n) — there are 2^n nodes in the recursion tree, and copying `path` at each costs up to O(n).
- Space: O(n * 2^n) for the output, plus O(n) recursion depth for `path` itself.
