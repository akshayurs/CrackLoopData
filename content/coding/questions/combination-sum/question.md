You are given an array of distinct positive integers `candidates` and a positive integer `target`. Return every unique combination of numbers from `candidates` that adds up to `target`. You may reuse the same number as many times as you like.

Two combinations are the same if they use the same numbers the same number of times, regardless of order — so each valid multiset should appear only once. Return the combinations sorted ascending internally, with the list of combinations itself in ascending (lexicographic) order.

## Examples

```text
Input:  candidates = [2, 3, 6, 7], target = 7
Output: [[2, 2, 3], [7]]
```

```text
Input:  candidates = [2, 3, 5], target = 8
Output: [[2, 2, 2, 2], [2, 3, 3], [3, 5]]
```

```text
Input:  candidates = [2], target = 1
Output: []
```

## Constraints

- 1 <= candidates.length <= 30
- 2 <= candidates[i] <= 40
- All elements of `candidates` are distinct.
- 1 <= target <= 40
