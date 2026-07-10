You have the integers `1` through `n`. A permutation `perm` of these integers (1-indexed, so `perm[i]` sits in position `i`) is called a **beautiful arrangement** if, for every position `i` from `1` to `n`, at least one of these holds: `perm[i]` is divisible by `i`, or `i` is divisible by `perm[i]`. Given `n`, return how many beautiful arrangements exist.

## Examples

```text
Input:  n = 2
Output: 2
# [1, 2]: pos1 -> 1 % 1 == 0, pos2 -> 2 % 2 == 0
# [2, 1]: pos1 -> 2 % 1 == 0, pos2 -> 1 divides 2
```

```text
Input:  n = 1
Output: 1
# [1]: pos1 -> 1 % 1 == 0
```

```text
Input:  n = 6
Output: 36
```

## Constraints

- 1 <= n <= 15
