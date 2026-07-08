You are given four integer arrays `a`, `b`, `c`, and `d`, all of the same length `n`. Count the number of index tuples `(i, j, k, l)` for which `a[i] + b[j] + c[k] + d[l] == 0`.

Every index ranges independently over `0` to `n - 1`, so the same value may be reused across arrays. Two tuples are different whenever any of their four indices differ, even if the chosen values are equal.

## Examples

```text
Input:  a = [1, 2], b = [-2, -1], c = [-1, 2], d = [0, 2]
Output: 2
# (0,0,0,1):  1 + (-2) + (-1) + 2 = 0
# (1,1,0,0):  2 + (-1) + (-1) + 0 = 0
```

```text
Input:  a = [0], b = [0], c = [0], d = [0]
Output: 1
# the single tuple (0,0,0,0) sums to 0
```

```text
Input:  a = [1, 2], b = [-1, -2], c = [0, 1], d = [-1, 0]
Output: 6
# multiple index combinations reach 0
```

## Constraints

- All four arrays have the same length `n`.
- 1 <= n <= 200
- -2^28 <= a[i], b[j], c[k], d[l] <= 2^28
- The answer fits in a 32-bit signed integer.

## Follow-up

The obvious solution tries every combination in O(n⁴). Can you cut it to O(n²) by splitting the four arrays into two halves?
