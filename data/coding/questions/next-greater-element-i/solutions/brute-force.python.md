Handle each query independently. For a value `x` from `nums1`, locate it in `nums2`, then walk rightward from that position looking for the first value larger than `x`. The first hit is the answer; running off the end means there is none, so record `-1`.

This mirrors the definition directly with two nested scans and no extra data structures.

```python
def next_greater_element(nums1, nums2):
    ans = []
    for x in nums1:
        start = nums2.index(x)
        greater = -1
        for j in range(start + 1, len(nums2)):
            if nums2[j] > x:
                greater = nums2[j]
                break
        ans.append(greater)
    return ans
```

## Why it works

Because the values are distinct, `nums2.index(x)` pinpoints exactly where `x` sits. Scanning strictly to the right and stopping at the first larger value yields the next greater element by definition; if the scan finishes without a hit, `-1` correctly signals that none exists.

## Complexity

- Time: O(n * m) — for each of the n elements in `nums1`, locating it and scanning right each cost up to m, the length of `nums2`.
- Space: O(1) — only the output array, no auxiliary storage.
