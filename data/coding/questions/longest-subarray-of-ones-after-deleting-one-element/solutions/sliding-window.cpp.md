Deleting one element and then joining `1`s is the same as finding the longest window that contains **at most one** `0` — that single `0` is the element we delete. Slide a window over the array and let it hold up to one zero; whenever a second zero enters, shrink from the left until only one remains.

For any valid window, the number of `1`s left after removing its single deleted slot is `window length - 1`. Because the deletion is mandatory, this `- 1` is always applied, which also gives the correct `n - 1` for an all-ones array.

```cpp
#include <vector>
#include <algorithm>
using namespace std;

class Solution {
public:
    int longestSubarray(vector<int>& nums) {
        int left = 0, zeros = 0, best = 0;
        for (int right = 0; right < (int)nums.size(); right++) {
            if (nums[right] == 0) zeros++;
            while (zeros > 1) {
                if (nums[left] == 0) zeros--;
                left++;
            }
            best = max(best, right - left);
        }
        return best;
    }
};
```

## Why it works

The window `[left, right]` is kept to at most one `0`. That zero (or, when the window is all ones, any one of the elements) is the mandatory deletion, so the surviving run of `1`s has length `right - left + 1 - 1 = right - left`. Tracking the maximum of `right - left` over every window therefore reports the best achievable run. Each index enters and leaves the window once, so the two pointers advance monotonically.

## Complexity

- Time: O(n) — each pointer moves forward at most n times.
- Space: O(1) — only a few counters.
