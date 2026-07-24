You don't actually need the full merged array — only where its middle falls. Imagine cutting both arrays into a "left half" and a "right half" so that, combined, the left halves hold exactly the first `⌈(m+n)/2⌉` elements. The median then depends only on the four values touching that cut: the two largest on the left and the two smallest on the right.

A partition is valid when every left element is `<=` every right element, which reduces to two checks across the arrays. Binary search the cut position in the *smaller* array (its size bounds the search), sliding left or right until the cross-conditions hold. Sentinels of `±∞` handle a cut at either edge.

```python
def find_median_sorted_arrays(nums1, nums2):
    A, B = (nums1, nums2) if len(nums1) <= len(nums2) else (nums2, nums1)
    m, n = len(A), len(B)
    total = m + n
    half = (total + 1) // 2
    lo, hi = 0, m
    inf = float('inf')
    while lo <= hi:
        i = (lo + hi) // 2
        j = half - i
        left_a = A[i - 1] if i > 0 else -inf
        right_a = A[i] if i < m else inf
        left_b = B[j - 1] if j > 0 else -inf
        right_b = B[j] if j < n else inf
        if left_a <= right_b and left_b <= right_a:
            if total % 2 == 1:
                return float(max(left_a, left_b))
            return (max(left_a, left_b) + min(right_a, right_b)) / 2.0
        elif left_a > right_b:
            hi = i - 1
        else:
            lo = i + 1
    return 0.0
```

## Why it works

Fixing `i` elements of `A` on the left forces `j = half - i` elements of `B` on the left, so the left half always has the right size. The partition is correct exactly when `left_a <= right_b` and `left_b <= right_a` — meaning nothing on the left exceeds anything on the right. If `left_a > right_b`, `i` is too big, so search lower; otherwise `i` is too small. When balanced, the median is `max(left)` for odd totals, or the average of `max(left)` and `min(right)` for even ones.

## Complexity

- Time: O(log(min(m, n))) — binary search over the smaller array's cut positions.
- Space: O(1) — only a handful of boundary values are kept.
