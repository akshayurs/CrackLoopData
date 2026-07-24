The most direct reading of the problem: every good subarray starts at some index `i` and extends to some later index `j`. So fix the start, grow the window one element at a time, and keep a running total — the instant that total becomes a multiple of `k` on a window of length two or more, we have our answer.

Growing the sum incrementally instead of re-adding a slice each time keeps the inner step O(1). We use a `long long` accumulator so the sum can't overflow while it builds up.

```cpp
#include <vector>
using namespace std;

class Solution {
public:
    bool checkSubarraySum(vector<int>& nums, int k) {
        int n = (int)nums.size();
        for (int i = 0; i < n; i++) {
            long long total = nums[i];
            for (int j = i + 1; j < n; j++) {
                total += nums[j];
                if (total % k == 0) {
                    return true;
                }
            }
        }
        return false;
    }
};
```

## Why it works

The outer loop pins the start index `i`; the inner loop extends the end index `j` from `i + 1` onward, so every window it tests already has length at least two. `total` accumulates `nums[i..j]` as `j` advances, and `total % k == 0` is exactly the "multiple of `k`" test. If any window passes we return immediately; if all starts are exhausted no good subarray exists.

## Complexity

- Time: O(n²) — for each start we scan every later end, about n²/2 windows.
- Space: O(1) — only the running total and loop counters.
