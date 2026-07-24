You are given `k` lists of integers, each sorted in non-decreasing order. Find the smallest range `[lo, hi]` such that every list has at least one element that falls inside `[lo, hi]` (inclusive on both ends).

If more than one range has the smallest width `hi - lo`, return the one with the smallest `lo`.

## Examples

```text
Input:  lists = [[4, 10, 15, 24, 26], [0, 9, 12, 20], [5, 18, 22, 30]]
Output: [20, 24]        # 20 from list 2, 24 from list 1, 22 from list 3
```

```text
Input:  lists = [[1, 2, 3], [1, 2, 3], [1, 2, 3]]
Output: [1, 1]
```

```text
Input:  lists = [[10, 10], [11, 11]]
Output: [10, 11]
```

## Constraints

- 1 <= k <= 3500
- 1 <= lists[i].length <= 50
- -10^5 <= lists[i][j] <= 10^5
- lists[i] is sorted in non-decreasing order.

## Follow-up

Can you avoid rescanning all `k` lists for the current maximum on every step?
