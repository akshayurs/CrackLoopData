We only need one value, not a fully ordered array, so sorting everything is wasteful. Instead, keep a min-heap that never holds more than `k` elements — the smallest of "the k largest seen so far" always sits at the root.

Push every number in, and whenever the heap grows past size `k`, pop the smallest. After scanning the whole array, exactly the k largest values remain in the heap, and the root is the smallest of them — which is precisely the k-th largest overall.

```python
import heapq

def kth_largest(nums, k):
    heap = []
    for n in nums:
        heapq.heappush(heap, n)
        if len(heap) > k:
            heapq.heappop(heap)
    return heap[0]
```

## Why it works

At every point the heap holds at most `k` elements, and it is trimmed by discarding the current minimum whenever it overflows. Anything that survives being the smallest of the "top k so far" must be among the true top k, so once every element has been offered, the heap contains exactly the k largest values, with the smallest of those — the answer — sitting at the root.

## Complexity

- Time: O(n log k) — each of the n pushes/pops costs O(log k) since the heap never exceeds size k.
- Space: O(k) — the heap holds at most k elements.
