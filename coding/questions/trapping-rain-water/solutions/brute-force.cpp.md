Start from the definition directly: the water resting above bar `i` is capped by the shorter of the tallest bar to its left and the tallest bar to its right, minus the bar's own height. If that difference is positive, it is the water held at `i`.

So for every position, scan left to find the highest bar seen so far and scan right for the highest bar ahead, then accumulate the trapped units one column at a time.

```cpp
#include <vector>
#include <algorithm>
using namespace std;

class Solution {
public:
    int trap(vector<int>& height) {
        int n = (int)height.size();
        int total = 0;
        for (int i = 0; i < n; i++) {
            int leftMax = 0;
            for (int l = 0; l <= i; l++) leftMax = max(leftMax, height[l]);
            int rightMax = 0;
            for (int r = i; r < n; r++) rightMax = max(rightMax, height[r]);
            total += min(leftMax, rightMax) - height[i];
        }
        return total;
    }
};
```

## Why it works

Water above column `i` can only rise as high as the lower of its two surrounding walls, `min(leftMax, rightMax)`. Subtracting `height[i]` gives the depth at that column, and this is always non-negative because both maxima include `height[i]` itself. Summing over every column yields the total volume.

## Complexity

- Time: O(n²) — each of the n columns rescans the array for its two maxima.
- Space: O(1) — only running totals are kept.
