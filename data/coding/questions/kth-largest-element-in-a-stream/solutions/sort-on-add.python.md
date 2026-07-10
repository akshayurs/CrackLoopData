The simplest thing that could work: keep every number the stream has ever seen in a list. Each time `add` is called, drop the new value in, sort the whole list in descending order, and read off the element at index `k - 1`.

It never gets the ordering wrong, but re-sorting the entire history on every single call is wasteful once the stream grows long.

```python
class KthLargest:
    def __init__(self, k: int, nums: list[int]):
        self.k = k
        self.nums = list(nums)

    def add(self, val: int) -> int:
        self.nums.append(val)
        self.nums.sort(reverse=True)
        return self.nums[self.k - 1]
```

## Why it works

Sorting the list in descending order puts the largest value at index 0, the second largest at index 1, and so on — so the k-th largest always sits at index `k - 1`. Because we re-sort after every insertion, the answer reflects the full stream seen so far.

## Complexity

- Time: O(n log n) per call to `add`, where n is the number of elements seen so far.
- Space: O(n) — the list stores every value ever added.
