Instead of rescanning each window, keep a heap that hands back the current maximum instantly. Push every element as `(value, index)` into a max-heap; the top is always the largest value seen so far.

The catch is that the top might sit *outside* the current window. Solve it with lazy deletion: before reading a window's answer, pop any entries whose index has slid off the left edge. Each element is pushed and popped at most once.

```cpp
#include <vector>
#include <queue>
#include <utility>
using namespace std;

class Solution {
public:
    vector<int> maxSlidingWindow(vector<int>& nums, int k) {
        int n = (int)nums.size();
        vector<int> result;
        priority_queue<pair<int, int>> heap; // (value, index)
        for (int i = 0; i < n; i++) {
            heap.push({nums[i], i});
            if (i >= k - 1) {
                while (heap.top().second <= i - k) heap.pop();
                result.push_back(heap.top().first);
            }
        }
        return result;
    }
};
```

## Why it works

`priority_queue<pair<int,int>>` orders by the pair's first field, so `top()` is the biggest value pushed so far (ties broken by index, which does not affect the value returned). An entry is valid for the window ending at `i` only when its index exceeds `i - k`; stale tops are popped before the max is read. Because a stale entry is removed once and never returns, `top().first` is always the largest in-window value.

## Complexity

- Time: O(n log n) — each element is pushed and popped at most once, each heap op is O(log n).
- Space: O(n) — the heap can hold up to n entries before stale ones are purged.
