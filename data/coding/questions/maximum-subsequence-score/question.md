You are given two integer arrays `nums1` and `nums2`, both of length `n`, and an integer `k`. Choose a set of exactly `k` indices `I`. The **score** of that choice is `(sum of nums1[i] for i in I) * (minimum of nums2[i] for i in I)`. Return the maximum score achievable over every valid choice of `k` indices.

## Examples

```text
Input:  nums1 = [1, 3, 3, 2], nums2 = [2, 1, 3, 4], k = 3
Output: 12
# indices {0, 2, 3}: sum(nums1) = 1 + 3 + 2 = 6, min(nums2) = min(2, 3, 4) = 2, score = 6 * 2 = 12
```

```text
Input:  nums1 = [4, 2, 3, 1, 1], nums2 = [7, 5, 10, 9, 6], k = 1
Output: 30
# indices {2}: sum(nums1) = 3, min(nums2) = 10, score = 3 * 10 = 30
```

```text
Input:  nums1 = [2, 1, 4], nums2 = [3, 4, 2], k = 2
Output: 12
# indices {0, 2}: sum(nums1) = 2 + 4 = 6, min(nums2) = min(3, 2) = 2, score = 6 * 2 = 12
```

## Constraints

- 1 <= n == nums1.length == nums2.length <= 10^5
- 0 <= nums1[i], nums2[i] <= 10^5
- 1 <= k <= n
