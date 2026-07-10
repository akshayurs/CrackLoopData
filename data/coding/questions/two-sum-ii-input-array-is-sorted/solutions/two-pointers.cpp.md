Put one pointer at the start and one at the end, then let the sum steer them. If the sum is too small, the only way to grow it is to move the left pointer right (to a larger value); if it is too big, move the right pointer left. Each step discards a value that can never be part of the answer, so a single sweep suffices.

This is the payoff of a sorted input: no extra memory, no repeated searching — the two ends converge in linear time.

```cpp
#include <vector>
using namespace std;

class Solution {
public:
    vector<int> twoSum(vector<int>& numbers, int target) {
        int lo = 0, hi = (int)numbers.size() - 1;
        while (lo < hi) {
            int s = numbers[lo] + numbers[hi];
            if (s == target) {
                return {lo + 1, hi + 1};
            }
            if (s < target) {
                lo++;
            } else {
                hi--;
            }
        }
        return {};
    }
};
```

## Why it works

At any point, `numbers[lo]` is the smallest still-usable value and `numbers[hi]` the largest. If their sum is below `target`, pairing `numbers[hi]` with anything left of `lo` would only be smaller, so `numbers[lo]` cannot reach the target and is safely skipped. The symmetric argument retires `numbers[hi]` when the sum is too large. Every move eliminates exactly one element, and the guaranteed pair is met when the pointers close on it.

## Complexity

- Time: O(n) — each element is visited at most once as the pointers close in.
- Space: O(1) — two index variables.
