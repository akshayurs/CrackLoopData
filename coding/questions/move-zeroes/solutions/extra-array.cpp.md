The simplest way to think about it: the answer is just "all the non-zero values, in order, followed by enough zeros to fill the rest." So build that up in a scratch vector.

Push each non-zero value into a fresh vector, resize it back to the original length (which fills the tail with zeros), then assign it back into `nums`.

```cpp
#include <vector>
using namespace std;

class Solution {
public:
    vector<int> moveZeroes(vector<int>& nums) {
        vector<int> result;
        for (int n : nums) {
            if (n != 0) result.push_back(n);
        }
        result.resize(nums.size(), 0);
        nums = result;
        return nums;
    }
};
```

## Why it works

Pushing keeps the non-zero values in their original order, preserving relative positions. `resize` grows the vector back to `n` and fills the new slots with `0`, which is exactly the count of zeros that were dropped. Assigning `result` back into `nums` mutates the caller's vector.

## Complexity

- Time: O(n) — one pass to fill, one pass to copy back.
- Space: O(n) — the scratch vector holds up to n elements.
