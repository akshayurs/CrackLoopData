Instead of copying out a "remaining" vector at every step, permute the array in place. Walk a `start` pointer left to right; at each position, swap in every candidate that hasn't been placed yet (everything from `start` onward), recurse on the rest of the array, then swap back so the next candidate sees the original order.

This is classic backtracking: choose, explore, un-choose. No extra vector gets built until a full permutation is ready to be copied into the answer.

```cpp
#include <vector>
#include <algorithm>
using namespace std;

class Solution {
public:
    vector<vector<int>> permute(vector<int>& nums) {
        vector<vector<int>> result;
        backtrack(nums, 0, result);
        sort(result.begin(), result.end());
        return result;
    }

private:
    void backtrack(vector<int>& nums, int start, vector<vector<int>>& result) {
        if (start == (int)nums.size()) {
            result.push_back(nums);
            return;
        }
        for (int i = start; i < (int)nums.size(); i++) {
            swap(nums[start], nums[i]);
            backtrack(nums, start + 1, result);
            swap(nums[start], nums[i]);
        }
    }
};
```

## Why it works

`backtrack(start)` fixes the first `start` elements and tries every unused value in the remaining slice as the next one, via a swap with position `start`. Recursing on `start + 1` fills the rest; undoing the swap afterward restores `nums` so the loop's next iteration tries a different candidate from the same original state. When `start` reaches the vector's size, every position is fixed and `nums` holds one complete permutation, which is copied into `result`. Because the problem doesn't fix an output order, the result is sorted lexicographically before returning so it matches regardless of the order swaps happened to produce.

## Complexity

- Time: O(n · n!) — n! permutations are generated, each finished with an O(n) copy into `result`.
- Space: O(n) auxiliary — recursion depth n and in-place swaps, on top of the O(n · n!) needed to store the output itself.
