The most direct reading of the problem: there are `n - k + 1` windows of length `k`, so line them all up, add each one, and keep the biggest average you see.

Because every window is summed independently, the same neighbouring elements get added over and over — correct, but wasteful. A `long long` accumulator keeps the sum exact for large windows.

```cpp
#include <vector>
#include <algorithm>
#include <limits>
using namespace std;

class Solution {
public:
    double maxAverage(vector<int>& nums, int k) {
        double best = -numeric_limits<double>::infinity();
        for (int i = 0; i + k <= (int)nums.size(); i++) {
            long long windowSum = 0;
            for (int j = i; j < i + k; j++) windowSum += nums[j];
            best = max(best, (double)windowSum / k);
        }
        return best;
    }
};
```

## Why it works

`i` walks over every start where a full window of `k` still fits; the inner loop sums those `k` values. Casting to `double` before the division yields the real average, and `max` accumulates the largest one, seeded at `-infinity` so all-negative inputs stay correct.

## Complexity

- Time: O(n·k) — ~n windows, each summed in O(k).
- Space: O(1) — only scalar bookkeeping.
