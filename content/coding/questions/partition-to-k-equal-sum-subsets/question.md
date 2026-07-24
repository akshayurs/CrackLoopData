You are given an integer array `nums` and an integer `k`. Determine whether it is possible to split `nums` into `k` non-empty subsets whose sums are all equal — every element must be used, and each element belongs to exactly one subset.

## Examples

```text
Input:  nums = [4, 3, 2, 3, 5, 2, 1], k = 4
Output: true         # groups of sum 5 each, e.g. (5), (1,4), (2,3), (2,3)
```

```text
Input:  nums = [1, 2, 3, 4], k = 3
Output: false         # sum is 10, not divisible by 3
```

```text
Input:  nums = [2, 2, 2, 2, 3, 3], k = 2
Output: true         # (2,2,3) and (2,2,3), each sums to 7
```

## Constraints

- 1 <= k <= nums.length <= 16
- 1 <= nums[i] <= 10^4
- The sum of `nums` fits in a 32-bit integer.

## Follow-up

Can you prune the search enough to comfortably handle `nums.length == 16`?
