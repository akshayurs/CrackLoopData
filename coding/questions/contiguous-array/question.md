You are given a binary array `nums` containing only `0`s and `1`s. Return the length of the longest contiguous subarray that holds an equal number of `0`s and `1`s.

If no such subarray exists, return `0`.

## Examples

```text
Input:  nums = [0, 1]
Output: 2             # the whole array has one 0 and one 1
```

```text
Input:  nums = [0, 1, 0]
Output: 2             # [0, 1] or [1, 0] — length 2 is the best possible
```

```text
Input:  nums = [0, 0, 1, 0, 1, 1]
Output: 6             # the entire array has three 0s and three 1s
```

## Constraints

- 1 <= nums.length <= 10^5
- nums[i] is either 0 or 1.

## Follow-up

The obvious solution scans every subarray in O(n²). Can you do it in a single pass with O(n) time?
