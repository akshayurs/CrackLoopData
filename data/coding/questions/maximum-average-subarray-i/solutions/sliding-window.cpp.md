Neighbouring windows overlap in all but one element. Instead of re-adding `k` numbers each time, keep a running sum: when the window slides one step right, add the element entering on the right and subtract the one leaving on the left.

Compare raw sums while sliding (they all share the same divisor `k`) and only divide once at the end. A `long long` accumulator keeps the running sum exact, and deferring the division keeps the loop integer-only.

```cpp
#include <vector>
#include <algorithm>
using namespace std;

class Solution {
public:
    double maxAverage(vector<int>& nums, int k) {
        long long windowSum = 0;
        for (int i = 0; i < k; i++) windowSum += nums[i];
        long long best = windowSum;
        for (int i = k; i < (int)nums.size(); i++) {
            windowSum += nums[i] - nums[i - k];
            best = max(best, windowSum);
        }
        return (double)best / k;
    }
};
```

## Why it works

The priming loop sums the first `k` elements into `windowSum`. Each slide adds the incoming `nums[i]` and subtracts the outgoing `nums[i - k]`, an O(1) step that keeps `windowSum` equal to the current window's sum. Because all windows divide by the same `k`, the maximum sum yields the maximum average, computed with a single division at the end.

## Complexity

- Time: O(n) — a single linear pass.
- Space: O(1) — scalar accumulators only.
