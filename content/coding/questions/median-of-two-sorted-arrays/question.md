You are given two sorted integer arrays `nums1` and `nums2` of sizes `m` and `n`. Return the median of the two arrays combined, treating them as one sorted sequence.

The median is the middle value of an odd-length sequence, or the average of the two middle values when the length is even. The result is a real number, so `2` is reported as `2.0` and a value halfway between `2` and `3` is `2.5`.

## Examples

```text
Input:  nums1 = [1, 3], nums2 = [2]
Output: 2.0        # merged = [1, 2, 3], middle element is 2
```

```text
Input:  nums1 = [1, 2], nums2 = [3, 4]
Output: 2.5        # merged = [1, 2, 3, 4], average of 2 and 3
```

```text
Input:  nums1 = [], nums2 = [1]
Output: 1.0        # merged = [1]
```

## Constraints

- 0 <= m, n <= 1000
- 1 <= m + n
- -10^6 <= nums1[i], nums2[i] <= 10^6
- Both `nums1` and `nums2` are sorted in non-decreasing order.

## Follow-up

The merge approach runs in O(m + n). Can you achieve O(log(m + n)) time?
