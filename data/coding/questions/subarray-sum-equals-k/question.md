You are given an array of integers `nums` and an integer `k`. Return the number of **contiguous** subarrays whose elements sum to exactly `k`.

A subarray is a non-empty slice of consecutive elements. The values in `nums` may be negative, zero, or positive, so a longer subarray is not always a larger sum.

## Examples

```text
Input:  nums = [1, 1, 1], k = 2
Output: 2        # [1,1] at indices (0,1) and (1,2)
```

```text
Input:  nums = [1, 2, 3], k = 3
Output: 2        # [1,2] and [3]
```

```text
Input:  nums = [3, 4, -7, 1, 3, 3, 1, -4], k = 7
Output: 4        # [3,4], [3,4,-7,1,3,3], [1,3,3], [3,3,1] each sum to 7
```

## Constraints

- 1 <= nums.length <= 2 * 10^4
- -1000 <= nums[i] <= 1000
- -10^7 <= k <= 10^7

## Follow-up

The negative values rule out a sliding window. Can you still count every subarray in a single pass?
