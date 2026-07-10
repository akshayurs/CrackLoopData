You don't actually need the full merged array — only where its middle falls. Imagine cutting both arrays into a "left half" and a "right half" so that, combined, the left halves hold exactly the first `⌈(m+n)/2⌉` elements. The median then depends only on the four values touching that cut: the two largest on the left and the two smallest on the right.

A partition is valid when every left element is `<=` every right element, which reduces to two checks across the arrays. Binary search the cut position in the *smaller* array (its size bounds the search), sliding left or right until the cross-conditions hold. Sentinels of `±∞` handle a cut at either edge.

```java
class Solution {
    public double findMedianSortedArrays(int[] nums1, int[] nums2) {
        int[] A = nums1, B = nums2;
        if (A.length > B.length) { A = nums2; B = nums1; }
        int m = A.length, n = B.length, total = m + n, half = (total + 1) / 2;
        int lo = 0, hi = m;
        while (lo <= hi) {
            int i = (lo + hi) / 2, j = half - i;
            long leftA = i > 0 ? A[i - 1] : Long.MIN_VALUE;
            long rightA = i < m ? A[i] : Long.MAX_VALUE;
            long leftB = j > 0 ? B[j - 1] : Long.MIN_VALUE;
            long rightB = j < n ? B[j] : Long.MAX_VALUE;
            if (leftA <= rightB && leftB <= rightA) {
                if (total % 2 == 1) {
                    return Math.max(leftA, leftB);
                }
                return (Math.max(leftA, leftB) + Math.min(rightA, rightB)) / 2.0;
            } else if (leftA > rightB) {
                hi = i - 1;
            } else {
                lo = i + 1;
            }
        }
        return 0.0;
    }
}
```

## Why it works

Fixing `i` elements of `A` on the left forces `j = half - i` elements of `B` on the left, so the left half always has the right size. The partition is correct exactly when `leftA <= rightB` and `leftB <= rightA` — meaning nothing on the left exceeds anything on the right. If `leftA > rightB`, `i` is too big, so search lower; otherwise `i` is too small. When balanced, the median is `max(left)` for odd totals, or the average of `max(left)` and `min(right)` for even ones. Boundary cuts use `±∞` sentinels so no index check is needed.

## Complexity

- Time: O(log(min(m, n))) — binary search over the smaller array's cut positions.
- Space: O(1) — only a handful of boundary values are kept.
