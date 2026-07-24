The key insight: if a newer element is larger than older ones still in the window, those older ones can never be the maximum again — they are dominated. So maintain a deque of indices whose values are strictly decreasing from front to back. The front always holds the current window's maximum.

For each element, pop smaller values off the back before pushing its index, and drop the front once it slides out of the window. Every index enters and leaves the deque exactly once, giving linear time.

```cpp
#include <vector>
#include <deque>
using namespace std;

class Solution {
public:
    vector<int> maxSlidingWindow(vector<int>& nums, int k) {
        int n = (int)nums.size();
        vector<int> result;
        deque<int> dq; // indices, values decreasing front→back
        for (int i = 0; i < n; i++) {
            while (!dq.empty() && nums[dq.back()] <= nums[i]) dq.pop_back();
            dq.push_back(i);
            if (dq.front() <= i - k) dq.pop_front();
            if (i >= k - 1) result.push_back(nums[dq.front()]);
        }
        return result;
    }
};
```

## Why it works

The deque holds indices in strictly decreasing value order, so `nums[dq.front()]` is the largest candidate value. Popping the back while it is `<= nums[i]` discards dominated elements — anything smaller than the incoming value and to its left is useless. The front is dropped once its index is `<= i - k`, i.e. no longer inside the window. Once the first full window forms (`i >= k - 1`), the front is exactly that window's maximum.

## Complexity

- Time: O(n) — each index is pushed and popped from the deque at most once.
- Space: O(k) — the deque never holds more than one window of indices.
