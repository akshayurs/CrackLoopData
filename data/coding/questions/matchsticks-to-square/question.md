You are given an array `matchsticks`, where `matchsticks[i]` is the length of the `i`-th matchstick. Using **all** of the matchsticks exactly once (no breaking, no leftovers), determine whether you can arrange them into a single square. Return `true` if it is possible, `false` otherwise.

## Examples

```text
Input:  matchsticks = [1, 1, 2, 2, 2]
Output: True         # sides: {1,1}, {2}, {2}, {2} — each sums to 2
```

```text
Input:  matchsticks = [3, 3, 3, 3, 4]
Output: False        # no way to split into four equal-length sides
```

```text
Input:  matchsticks = [1, 1, 1, 1]
Output: True         # each stick is its own side, side length 1
```

## Constraints

- 1 <= matchsticks.length <= 15
- 1 <= matchsticks[i] <= 10^8
