The most direct reading: if both inputs are already sorted, merging them the way you merge two piles of cards gives one sorted array. Once you have that, the median is just an index lookup — the middle element, or the mean of the two middle elements when the total length is even.

Walk both arrays with two pointers, always taking the smaller front element, until everything is consumed. Then read off the middle.

```python
def find_median_sorted_arrays(nums1, nums2):
    merged = []
    i = j = 0
    while i < len(nums1) and j < len(nums2):
        if nums1[i] <= nums2[j]:
            merged.append(nums1[i])
            i += 1
        else:
            merged.append(nums2[j])
            j += 1
    merged.extend(nums1[i:])
    merged.extend(nums2[j:])
    total = len(merged)
    mid = total // 2
    if total % 2 == 1:
        return float(merged[mid])
    return (merged[mid - 1] + merged[mid]) / 2.0
```

## Why it works

The merge preserves sorted order because at every step the smallest unused element across both arrays sits at one of the two pointers, and we always take it. After the loop, one array is exhausted and the leftover tail of the other is already in order, so appending it keeps the result sorted. Indexing the middle of a sorted array is the definition of the median.

## Complexity

- Time: O(m + n) — every element is copied once.
- Space: O(m + n) — the merged array holds all elements.
