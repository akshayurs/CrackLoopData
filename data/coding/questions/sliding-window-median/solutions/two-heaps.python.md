Re-sorting the whole window every step throws away almost all of the previous work. Instead, keep the window split across two heaps: a max-heap `small` holding the lower half and a min-heap `large` holding the upper half, kept balanced in size so the median always sits at one (or both) of their tops.

The wrinkle is deletion — heaps don't support "remove this arbitrary value" efficiently. The trick is lazy deletion: when a number slides out of the window, just record that it owes a removal in a `delayed` counter, and only actually pop it off a heap once it would otherwise surface at the top. Sizes are still tracked exactly, so balancing and the median calculation stay correct even while stale values linger deeper in a heap.

```python
import heapq

def median_sliding_window(nums, k):
    small, large = [], []  # small: max-heap (values negated), large: min-heap
    delayed = {}
    small_size = large_size = 0

    def prune(heap, is_small):
        while heap:
            top = -heap[0] if is_small else heap[0]
            if delayed.get(top, 0) > 0:
                delayed[top] -= 1
                if delayed[top] == 0:
                    del delayed[top]
                heapq.heappop(heap)
            else:
                break

    def balance():
        nonlocal small_size, large_size
        if small_size > large_size + 1:
            heapq.heappush(large, -heapq.heappop(small))
            small_size, large_size = small_size - 1, large_size + 1
            prune(small, True)
        elif small_size < large_size:
            heapq.heappush(small, -heapq.heappop(large))
            large_size, small_size = large_size - 1, small_size + 1
            prune(large, False)

    def insert(num):
        nonlocal small_size, large_size
        if not small or num <= -small[0]:
            heapq.heappush(small, -num)
            small_size += 1
        else:
            heapq.heappush(large, num)
            large_size += 1
        balance()

    def erase(num):
        nonlocal small_size, large_size
        delayed[num] = delayed.get(num, 0) + 1
        if num <= -small[0]:
            small_size -= 1
            if num == -small[0]:
                prune(small, True)
        else:
            large_size -= 1
            if num == large[0]:
                prune(large, False)
        balance()

    result = []
    for i, num in enumerate(nums):
        insert(num)
        if i >= k:
            erase(nums[i - k])
        if i >= k - 1:
            result.append(float(-small[0]) if k % 2 else (-small[0] + large[0]) / 2.0)
    return result
```

## Why it works

`small` and `large` are kept the same size (or `small` one larger), so the median is always `small`'s top for odd `k`, or the average of both tops for even `k`. Lazy deletion keeps the heaps' logical sizes accurate — `small_size`/`large_size` reflect reality even before a stale entry is physically popped — so every balance and median read uses correct counts, and pruning only ever touches values that have actually become garbage.

## Complexity

- Time: O(n log k) — each insert, erase, and balance touches a heap of size O(k), and each element causes O(1) amortized heap operations overall.
- Space: O(k) — the two heaps together hold the current window (plus bounded stale entries awaiting cleanup).
