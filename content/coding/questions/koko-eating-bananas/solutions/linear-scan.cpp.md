The slowest workable speed lies between 1 and the largest pile — eating faster than the biggest pile never helps, since Koko can only touch one pile per hour. So the direct approach is to try every candidate speed from 1 upward and return the first that finishes in time.

For a given speed `k`, a pile of size `p` takes `ceil(p / k)` hours, and the total is the sum over all piles. Because a larger speed only ever reduces the total, the first speed that fits within `h` is the answer.

```cpp
#include <vector>
#include <algorithm>
using namespace std;

class Solution {
public:
    int minEatingSpeed(vector<int>& piles, int h) {
        int maxPile = *max_element(piles.begin(), piles.end());
        for (int k = 1; k <= maxPile; k++) {
            long long hours = 0;
            for (int p : piles) {
                hours += (p + k - 1) / k;
            }
            if (hours <= h) return k;
        }
        return maxPile;
    }
};
```

## Why it works

`(p + k - 1) / k` is integer ceiling division — exactly the hours Koko needs for one pile, since she cannot carry leftover eating into the next hour. The running sum uses `long long` to avoid overflow when many large piles accumulate. The total is non-increasing in `k`, so the upward scan returns the minimum feasible speed first; speed `maxPile` always works.

## Complexity

- Time: O(m · n) — up to m = max(piles) speeds, each an O(n) sum over the piles.
- Space: O(1) — only a running total is kept.
