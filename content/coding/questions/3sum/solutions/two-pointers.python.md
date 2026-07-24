Sort the array first. Once the numbers are ordered, fix the smallest member of the triplet with an index `i`, then hunt for the other two with a classic two-pointer sweep over the remaining suffix: a left pointer just after `i` and a right pointer at the end. If the running sum is too small move left rightward, if too large move right leftward, and when it hits zero record the triplet.

Sorting also makes de-duplication cheap: identical values sit next to each other, so we skip over repeats of `i`, and of both pointers after a match. Because we always emit `[nums[i], nums[left], nums[right]]` in increasing order and advance `i` upward, the triplets come out already in canonical order.

```python
def three_sum(nums):
    nums.sort()
    n = len(nums)
    result = []
    for i in range(n - 2):
        if nums[i] > 0:
            break
        if i > 0 and nums[i] == nums[i - 1]:
            continue
        left, right = i + 1, n - 1
        while left < right:
            total = nums[i] + nums[left] + nums[right]
            if total < 0:
                left += 1
            elif total > 0:
                right -= 1
            else:
                result.append([nums[i], nums[left], nums[right]])
                left += 1
                right -= 1
                while left < right and nums[left] == nums[left - 1]:
                    left += 1
                while left < right and nums[right] == nums[right + 1]:
                    right -= 1
    return result
```

## Why it works

With `nums[i]` fixed, we need two later numbers summing to `-nums[i]`. On a sorted suffix the two-pointer scan finds every such pair in one linear pass: increasing `left` only grows the sum and decreasing `right` only shrinks it, so no valid pair is ever skipped. Skipping equal neighbors for `i`, `left`, and `right` guarantees each distinct triplet is emitted once. Since `nums[i] <= nums[left] <= nums[right]` always holds and `i` scans upward, no post-sort of the output is needed.

## Complexity

- Time: O(n²) — the initial sort is O(n log n), then each of the n anchors drives an O(n) two-pointer pass.
- Space: O(1) — ignoring the output list and the in-place sort, only a few pointers are used.
