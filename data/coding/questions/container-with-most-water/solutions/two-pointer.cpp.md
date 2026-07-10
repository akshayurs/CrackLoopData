Start with the widest possible container: one pointer at each end. This pair already maximizes the width, so any narrower container can only beat it by being taller. The wall that limits the current area is the shorter of the two, and moving the taller wall inward can never help — width shrinks and the height is still capped by the short wall. So always move the shorter wall inward, hunting for a taller line.

Each step discards the shorter wall, which cannot be part of any better container involving that side, so no candidate is missed while the pointers converge in a single pass.

```cpp
#include <vector>
#include <algorithm>
using namespace std;

class Solution {
public:
    int maxArea(vector<int>& heights) {
        int left = 0, right = (int)heights.size() - 1;
        int best = 0;
        while (left < right) {
            int area = min(heights[left], heights[right]) * (right - left);
            best = max(best, area);
            if (heights[left] < heights[right]) {
                left++;
            } else {
                right--;
            }
        }
        return best;
    }
};
```

## Why it works

The area is `min(leftWall, rightWall) * width`. Moving the taller wall keeps the height capped by the shorter wall while strictly reducing width, so it never improves the result — every container that used the shorter wall as a limiter has already been measured at its maximum width. Advancing the shorter wall is the only move that can raise the limiting height, so discarding it loses nothing. Both pointers together traverse the array once.

## Complexity

- Time: O(n) — each pointer moves inward at most n times total.
- Space: O(1) — two indices and the running maximum.
