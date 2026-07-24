Feasibility is monotonic: if you can make `m` bouquets by day `d`, you can also make them on any later day, because flowers never un-bloom. That turns the problem into finding the smallest `d` for which the check passes — a classic binary search on the answer.

Search the day range `[min(bloomDay), max(bloomDay)]`. For a midpoint day, run the same linear feasibility check; if it succeeds, the answer is at most that day, so shrink the upper bound, otherwise raise the lower bound. Guard the impossible case with `m * k > n` first.

```cpp
#include <vector>
#include <algorithm>
using namespace std;

class Solution {
public:
    int minDays(vector<int>& bloomDay, int m, int k) {
        int n = (int)bloomDay.size();
        if ((long long)m * k > n) return -1;
        int lo = *min_element(bloomDay.begin(), bloomDay.end());
        int hi = *max_element(bloomDay.begin(), bloomDay.end());
        while (lo < hi) {
            int mid = lo + (hi - lo) / 2;
            if (canMake(bloomDay, mid, m, k)) hi = mid;
            else lo = mid + 1;
        }
        return lo;
    }

private:
    bool canMake(const vector<int>& bloomDay, int day, int m, int k) {
        int bouquets = 0, run = 0;
        for (int b : bloomDay) {
            if (b <= day) {
                if (++run == k) { bouquets++; run = 0; }
            } else {
                run = 0;
            }
        }
        return bouquets >= m;
    }
};
```

## Why it works

`canMake` counts bouquets by cutting one per full run of `k` adjacent bloomed flowers. Because feasibility flips from false to true exactly once as the day increases, the loop converges the window `[lo, hi]` onto that boundary — the first day the check passes. Since `m * k <= n`, the maximum bloom day is always feasible, so `lo` ends on a real answer.

## Complexity

- Time: O(n log(maxDay)) — O(log(maxDay)) binary-search steps, each an O(n) scan.
- Space: O(1) — only counters.
