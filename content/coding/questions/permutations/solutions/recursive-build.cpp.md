The most direct way to think about permutations: pick each element in turn to go first, then glue it onto every permutation of whatever's left. That "whatever's left" is a smaller version of the same problem, so the natural tool is recursion — with a single element as the base case.

It's a clean, honest first pass, though rebuilding a shorter vector at every step isn't free.

```cpp
#include <vector>
#include <algorithm>
using namespace std;

class Solution {
public:
    vector<vector<int>> permute(vector<int>& nums) {
        vector<vector<int>> result = helper(nums);
        sort(result.begin(), result.end());
        return result;
    }

private:
    vector<vector<int>> helper(vector<int>& arr) {
        if (arr.size() <= 1) {
            return {arr};
        }
        vector<vector<int>> perms;
        for (int i = 0; i < (int)arr.size(); i++) {
            vector<int> rest;
            for (int j = 0; j < (int)arr.size(); j++) {
                if (j != i) rest.push_back(arr[j]);
            }
            for (auto& p : helper(rest)) {
                vector<int> withHead = {arr[i]};
                withHead.insert(withHead.end(), p.begin(), p.end());
                perms.push_back(withHead);
            }
        }
        return perms;
    }
};
```

## Why it works

`helper` returns every permutation of `arr`. For each index `i`, `arr[i]` is fixed as the head and `rest` (everything else) is recursively permuted; prepending `arr[i]` to each sub-permutation accounts for every arrangement that starts with it. Looping `i` over every position covers every possible head, so nothing is missed and nothing repeats. Since the problem doesn't fix an output order, the result is sorted lexicographically before returning so it's identical no matter how the recursion built it up.

## Complexity

- Time: O(n² · n!) — there are n! permutations, and building `rest` costs O(n) at each of the roughly n · n! recursive calls.
- Space: O(n²) auxiliary — recursion depth n, each level holding an O(n)-sized vector, on top of the O(n · n!) needed to store the output itself.
