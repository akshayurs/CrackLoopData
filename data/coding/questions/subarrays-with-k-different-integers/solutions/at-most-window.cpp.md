Counting subarrays with *exactly* `k` distinct values is awkward, but counting subarrays with *at most* `k` distinct values is a textbook sliding window: grow the right edge, and whenever the window holds more than `k` distinct values, shrink the left edge until it is valid again. For every right endpoint, the window length is exactly the number of valid subarrays ending there, so summing lengths gives the "at most `k`" total.

The trick is the identity `exactly(k) = atMost(k) - atMost(k - 1)`. Run the same helper twice and subtract — the difference cancels every subarray with fewer than `k` distinct values and leaves precisely those with `k`.

```cpp
#include <vector>
#include <unordered_map>
using namespace std;

class Solution {
public:
    int subarraysWithKDistinct(vector<int>& nums, int k) {
        return atMost(nums, k) - atMost(nums, k - 1);
    }

private:
    int atMost(vector<int>& nums, int m) {
        unordered_map<int, int> freq;
        int left = 0, total = 0;
        for (int right = 0; right < (int)nums.size(); right++) {
            freq[nums[right]]++;
            while ((int)freq.size() > m) {
                int y = nums[left];
                if (--freq[y] == 0) freq.erase(y);
                left++;
            }
            total += right - left + 1;
        }
        return total;
    }
};
```

## Why it works

`atMost(m)` keeps `[left, right]` as the longest window ending at `right` with no more than `m` distinct values; adding `right - left + 1` counts every subarray ending at `right`, because any shorter suffix is also valid. A subarray with `d` distinct values is counted by `atMost(k)` when `d <= k` and by `atMost(k - 1)` when `d <= k - 1`; subtracting leaves exactly those with `d == k`.

## Complexity

- Time: O(n) — each helper advances `left` and `right` at most n times, and we call it twice.
- Space: O(n) — the frequency map holds at most the distinct values in a window.
