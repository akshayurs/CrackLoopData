You are given an array of integers `nums` that **may contain duplicates**. Return all distinct permutations of `nums`, in any order.

A permutation uses every element exactly once, but two permutations that look the same (same values in the same positions) count as one — duplicates in the input must not produce duplicate outputs.

## Examples

```text
Input:  nums = [1, 1, 2]
Output: [[1, 1, 2], [1, 2, 1], [2, 1, 1]]
```

```text
Input:  nums = [1, 2, 3]
Output: [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]
```

```text
Input:  nums = [2, 2, 1, 1]
Output: [[1, 1, 2, 2], [1, 2, 1, 2], [1, 2, 2, 1], [2, 1, 1, 2], [2, 1, 2, 1], [2, 2, 1, 1]]
```

## Constraints

- 1 <= nums.length <= 8
- -10 <= nums[i] <= 10
- Output order does not matter, but for this exercise the permutations are shown sorted lexicographically.
