Given an array of positive integers `nums` and an integer `k`, count how many contiguous subarrays contain **exactly** `k` distinct integers. Such a subarray is sometimes called *good*.

A subarray is a non-empty run of consecutive elements. Return the total count as an integer.

## Examples

```text
Input:  nums = [1, 2, 1, 2, 3], k = 2
Output: 7
# [1,2] [2,1] [1,2] [2,1] [1,2,1] [2,1,2] [1,2,1,2]
```

```text
Input:  nums = [1, 2, 1, 3, 4], k = 3
Output: 3
# [1,2,1,3] [2,1,3] [1,3,4]
```

```text
Input:  nums = [1, 1, 1, 1], k = 1
Output: 10
# every one of the 10 subarrays has a single distinct value
```

## Constraints

- 1 <= nums.length <= 2 * 10^4
- 1 <= nums[i] <= nums.length
- 1 <= k <= nums.length

## Follow-up

The direct approach is O(n²). Can you reach O(n) time? Hint: counting subarrays with *exactly* `k` distinct values is hard, but counting those with *at most* `k` is a clean sliding window.
