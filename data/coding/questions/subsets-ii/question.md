You are given an integer array `nums` that may contain duplicate values. Return all possible subsets (the power set), with no duplicate subsets in the result. Each subset's elements must be sorted in ascending order, and the list of subsets itself must come back sorted lexicographically.

## Examples

```text
Input:  nums = [1, 2, 2]
Output: [[], [1], [1,2], [1,2,2], [2], [2,2]]
```

```text
Input:  nums = [0]
Output: [[], [0]]
```

```text
Input:  nums = [5, 5, 5]
Output: [[], [5], [5,5], [5,5,5]]
```

## Constraints

- 1 <= nums.length <= 10
- -10 <= nums[i] <= 10
