Walk the vector from the front and stop at the first element that is greater than or equal to `target`. Because the vector is sorted, that position is exactly where `target` belongs — either it holds `target` itself, or it is the first slot large enough to sit ahead of it.

If no such element exists, every value was smaller than `target`, so it belongs at the very end.

```cpp
#include <vector>
using namespace std;

class Solution {
public:
    int searchInsert(vector<int>& nums, int target) {
        for (int i = 0; i < (int)nums.size(); i++) {
            if (nums[i] >= target) {
                return i;
            }
        }
        return (int)nums.size();
    }
};
```

## Why it works

The first index where `nums[i] >= target` is the answer in both cases: when `nums[i] == target` we return its index, and when `nums[i] > target` inserting before it keeps the order intact. Falling off the end means `target` is larger than all elements, so its insert position is `nums.size()`.

## Complexity

- Time: O(n) — a single pass over the vector.
- Space: O(1) — only an index is tracked.
