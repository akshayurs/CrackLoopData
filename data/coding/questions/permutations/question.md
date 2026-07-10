Given an array `nums` of distinct integers, return **all possible permutations** of the array, in any order.

Since a set of `n` distinct numbers has `n!` orderings, your output should contain every one of them exactly once — no duplicates, none missing.

## Examples

```text
Input:  nums = [1, 2, 3]
Output: [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]
```

```text
Input:  nums = [0, 1]
Output: [[0, 1], [1, 0]]
```

```text
Input:  nums = [1]
Output: [[1]]
```

## Constraints

- 1 <= nums.length <= 6
- -10 <= nums[i] <= 10
- All integers in `nums` are distinct.

## Follow-up

Can you generate the permutations in-place, using only O(n) auxiliary space beyond the output itself?
