The key insight: if a newer element is larger than older ones still in the window, those older ones can never be the maximum again — they are dominated. So maintain a deque of indices whose values are strictly decreasing from front to back. The front always holds the current window's maximum.

For each element, pop smaller values off the back before pushing its index, and drop the front once it slides out of the window. Every index enters and leaves the deque exactly once, giving linear time.

```python
from collections import deque

def max_sliding_window(nums, k):
    dq = deque()  # indices, values decreasing front→back
    result = []
    for i, n in enumerate(nums):
        while dq and nums[dq[-1]] <= n:
            dq.pop()
        dq.append(i)
        if dq[0] <= i - k:
            dq.popleft()
        if i >= k - 1:
            result.append(nums[dq[0]])
    return result
```

## Why it works

The deque holds indices in strictly decreasing value order, so `nums[dq[0]]` is the largest value among the candidates. Popping the back while it is `<= n` removes dominated elements — anything smaller than the incoming value and to its left is useless. The front is discarded once its index is `<= i - k`, i.e. no longer inside the window. Once the first full window is formed (`i >= k - 1`), the front is exactly that window's maximum.

## Complexity

- Time: O(n) — each index is appended and removed from the deque at most once.
- Space: O(k) — the deque never holds more than one window of indices.
