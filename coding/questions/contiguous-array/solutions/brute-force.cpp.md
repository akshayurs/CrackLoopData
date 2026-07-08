The most direct reading of the problem: consider every subarray and keep the longest one that is balanced. Fix a start index, then extend the end one step at a time, tracking a running count of `0`s and `1`s so far.

Whenever the two counts match, the current window is balanced, so update the best length. Reusing the running counts as the window grows avoids recounting from scratch, but you still examine every start, so it stays quadratic.

```cpp
#include <vector>
#include <algorithm>
using namespace std;

class Solution {
public:
    int findMaxLength(vector<int>& nums) {
        int n = (int)nums.size();
        int best = 0;
        for (int i = 0; i < n; i++) {
            int zeros = 0, ones = 0;
            for (int j = i; j < n; j++) {
                if (nums[j] == 0) zeros++;
                else ones++;
                if (zeros == ones) best = max(best, j - i + 1);
            }
        }
        return best;
    }
};
```

## Why it works

The outer loop pins the start of the subarray; the inner loop stretches the end rightward, incrementing `zeros` or `ones` for each new element. Every contiguous subarray is covered exactly once by some `(i, j)` pair. A subarray is valid precisely when its `0` and `1` counts are equal, so each time that holds we record its length and keep the maximum.

## Complexity

- Time: O(n²) — every start pairs with every later end.
- Space: O(1) — just two counters and the running best.
