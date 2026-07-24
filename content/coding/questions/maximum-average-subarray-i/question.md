You are given an integer array `nums` and an integer `k`. Look at every contiguous block of exactly `k` elements and compute its average. Return the largest average among all such blocks.

The answer is accepted if it is within `10^-5` of the true maximum average.

## Examples

```text
Input:  nums = [1, 12, -5, -6, 50, 3], k = 4
Output: 12.75      # window [12, -5, -6, 50] has sum 51, average 51/4 = 12.75
```

```text
Input:  nums = [-1, -2, -3, -4], k = 2
Output: -1.5       # window [-1, -2] has the largest average
```

## Constraints

- 1 <= k <= nums.length <= 10^5
- -10^4 <= nums[i] <= 10^4

## Follow-up

Can you avoid recomputing each window's sum from scratch and answer in a single linear pass?
