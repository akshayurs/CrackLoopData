You are given an integer array `arr` and an integer `k`. Remove exactly `k` elements from `arr` (any `k` elements, one at a time), then return the smallest possible number of distinct values left in the array.

You get to choose which elements to remove, so pick removals that clear out entire values first — it is always better to wipe out a value that appears rarely than to chip away at one that appears often.

## Examples

```text
Input:  arr = [5, 5, 4], k = 1
Output: 1        # remove the single 4; only the value 5 remains
```

```text
Input:  arr = [4, 3, 1, 1, 3, 3, 2], k = 3
Output: 2        # remove 4 and 2 entirely (2 removals), then one 1 (1 more); 1 and 3 remain
```

```text
Input:  arr = [2, 2, 3, 3, 3, 3, 5, 5, 5, 2], k = 2
Output: 3        # every value appears >= 3 times, so 2 removals cannot clear any of them
```

## Constraints

- 1 <= arr.length <= 10^5
- 1 <= arr[i] <= 10^9
- 0 <= k <= arr.length
