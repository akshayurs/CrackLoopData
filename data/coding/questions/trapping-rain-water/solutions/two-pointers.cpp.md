The prefix/suffix arrays can be dropped entirely. Keep two pointers walking inward from both ends, along with the best wall seen from each side. The key insight: at whichever side has the *shorter* running maximum, that side's wall alone decides the water level — the opposite side is guaranteed to hold at least as high, so the far max never matters.

So always advance the pointer on the smaller-wall side. If the current bar is below that side's running max, the gap fills with water; otherwise it raises the wall.

```cpp
#include <vector>
#include <algorithm>
using namespace std;

class Solution {
public:
    int trap(vector<int>& height) {
        int left = 0, right = (int)height.size() - 1;
        int leftMax = 0, rightMax = 0, total = 0;
        while (left < right) {
            if (height[left] < height[right]) {
                leftMax = max(leftMax, height[left]);
                total += leftMax - height[left];
                left++;
            } else {
                rightMax = max(rightMax, height[right]);
                total += rightMax - height[right];
                right--;
            }
        }
        return total;
    }
};
```

## Why it works

When `height[left] < height[right]`, the right side has a bar at least as tall as `height[left]`, so the true right max is `>= height[left]` and cannot be the limiting wall. That makes `leftMax` the sole cap at `left`, and `leftMax - height[left]` is exactly the trapped water there. The symmetric argument holds on the other branch. Each column is settled once as its pointer moves, so no lookahead is needed.

## Complexity

- Time: O(n) — each pointer moves inward at most n times total.
- Space: O(1) — four scalars, no auxiliary arrays.
