Instead of rescanning each window, keep a heap that can hand back the current maximum instantly. Push every element as `(value, index)` into a max-heap; the top is always the largest value seen so far.

The catch is that the top might sit *outside* the current window. Solve it with lazy deletion: before reading the answer for a window, pop any entries whose index has fallen off the left edge. Each element is pushed and popped at most once.

```python
import heapq

def max_sliding_window(nums, k):
    heap = []
    result = []
    for i, n in enumerate(nums):
        heapq.heappush(heap, (-n, i))
        if i >= k - 1:
            while heap[0][1] <= i - k:
                heapq.heappop(heap)
            result.append(-heap[0][0])
    return result
```

## Why it works

Python's `heapq` is a min-heap, so values are negated to simulate a max-heap. The top entry is the biggest value among all pushed so far. An entry is valid for the window ending at `i` only if its index is greater than `i - k`; stale tops are popped before the max is read. Since a stale entry is removed once and never returns, the answer for each window is always the largest *in-window* value.

## Complexity

- Time: O(n log n) — each element is pushed and popped at most once, each heap op is O(log n).
- Space: O(n) — the heap can hold up to n entries before stale ones are purged.
