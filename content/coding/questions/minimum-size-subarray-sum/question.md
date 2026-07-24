You are given an array of positive integers `nums` and a positive integer `target`. Return the length of the **shortest contiguous subarray** whose elements sum to at least `target`.

If no such subarray exists, return `0`.

## Examples

```text
Input:  target = 7, nums = [2, 3, 1, 2, 4, 3]
Output: 2             # [4, 3] sums to 7 with just 2 elements
```

```text
Input:  target = 4, nums = [1, 4, 4]
Output: 1             # the single element 4 already reaches the target
```

```text
Input:  target = 11, nums = [1, 1, 1, 1, 1, 1, 1, 1]
Output: 0             # the whole array sums to 8 < 11
```

## Constraints

- 1 <= target <= 10^9
- 1 <= nums.length <= 10^5
- 1 <= nums[i] <= 10^4

## Follow-up

You can solve it in O(n) time. Can you also design an O(n log n) solution?
