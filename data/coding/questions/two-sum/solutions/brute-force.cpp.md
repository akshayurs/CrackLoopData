The same idea in C++: two nested loops over the vector, returning the first pair that reaches the target. No auxiliary storage.

```cpp
#include <vector>
using namespace std;

class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        for (int i = 0; i < (int)nums.size(); i++) {
            for (int j = i + 1; j < (int)nums.size(); j++) {
                if (nums[i] + nums[j] == target) {
                    return {i, j};
                }
            }
        }
        return {};
    }
};
```

## Why it works

The outer loop fixes the first index; the inner loop scans every later index, so each unordered pair is tested exactly once. The first matching pair is returned immediately; the one-solution guarantee means the empty return is never reached.

## Complexity

- Time: O(n²) — about n²/2 pairs are checked.
- Space: O(1) — no extra structure.
