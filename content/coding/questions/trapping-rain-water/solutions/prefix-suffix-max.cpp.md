The brute force recomputes the same left and right maxima over and over. Precompute them once instead: `leftMax[i]` is the tallest bar at or before `i`, and `rightMax[i]` is the tallest at or after `i`. Both fill in a single sweep each.

With those tables ready, the water at every column is just `min(leftMax[i], rightMax[i]) - height[i]`, summed in a final linear pass.

```cpp
#include <vector>
#include <algorithm>
using namespace std;

class Solution {
public:
    int trap(vector<int>& height) {
        int n = (int)height.size();
        if (n == 0) return 0;
        vector<int> leftMax(n), rightMax(n);
        leftMax[0] = height[0];
        for (int i = 1; i < n; i++) leftMax[i] = max(leftMax[i - 1], height[i]);
        rightMax[n - 1] = height[n - 1];
        for (int i = n - 2; i >= 0; i--) rightMax[i] = max(rightMax[i + 1], height[i]);
        int total = 0;
        for (int i = 0; i < n; i++) total += min(leftMax[i], rightMax[i]) - height[i];
        return total;
    }
};
```

## Why it works

`leftMax` and `rightMax` capture exactly the two walls that bound the water above each column. Because they are built cumulatively, each entry reuses the previous result in O(1), turning the quadratic rescans into three linear passes while producing the identical per-column depth.

## Complexity

- Time: O(n) — three linear passes.
- Space: O(n) — two auxiliary arrays of size n.
