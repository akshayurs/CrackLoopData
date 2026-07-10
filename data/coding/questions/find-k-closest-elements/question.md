You are given an array `arr` sorted in ascending order, plus two integers `k` and `x`. Return the `k` integers from `arr` that are closest to `x`, listed in ascending order.

Closeness is measured by absolute difference: an integer `a` is closer to `x` than `b` when `|a - x| < |b - x|`. When two integers are the same distance from `x`, the **smaller** integer is considered closer.

## Examples

```text
Input:  arr = [1, 2, 3, 4, 5], k = 4, x = 3
Output: [1, 2, 3, 4]        # distances are 2,1,0,1,2 — drop the farthest (5)
```

```text
Input:  arr = [1, 2, 3, 4, 5], k = 4, x = -1
Output: [1, 2, 3, 4]        # x sits left of the array, take the smallest 4
```

```text
Input:  arr = [1, 1, 2, 3, 4, 5], k = 4, x = -1
Output: [1, 1, 2, 3]        # ties broken toward smaller values
```

## Constraints

- 1 <= k <= arr.length
- 1 <= arr.length <= 10^4
- arr is sorted in ascending order.
- -10^4 <= arr[i], x <= 10^4

## Follow-up

The result window is always a contiguous slice of `arr`. Can you locate its left edge in O(log(n - k)) time instead of scanning?
