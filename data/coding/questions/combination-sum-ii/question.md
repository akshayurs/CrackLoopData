You are given an array `candidates` of positive integers (it may contain duplicates) and a target integer `target`. Find every unique combination of numbers from `candidates` that adds up exactly to `target`.

Each number in `candidates` may be used **at most once** per combination (once per its position in the array, not once per distinct value). The same combination of values must not appear twice in the result. Return the combinations sorted: each combination's numbers in ascending order, and the list of combinations in ascending (lexicographic) order.

## Examples

```text
Input:  candidates = [10, 1, 2, 7, 6, 1, 5], target = 8
Output: [[1, 1, 6], [1, 2, 5], [1, 7], [2, 6]]
```

```text
Input:  candidates = [2, 5, 2, 1, 2], target = 5
Output: [[1, 2, 2], [5]]
```

```text
Input:  candidates = [2, 2], target = 8
Output: []
```

## Constraints

- 1 <= candidates.length <= 100
- 1 <= candidates[i] <= 50
- 1 <= target <= 30
