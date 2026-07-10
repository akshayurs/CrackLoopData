You are given an array of integers `nums` and an integer `k`. Call a contiguous subarray **nice** if it contains exactly `k` odd numbers.

Return the total count of nice subarrays.

## Examples

```text
Input:  nums = [1, 1, 2, 1, 1], k = 3
Output: 2        # [1, 1, 2, 1] and [1, 2, 1, 1] each hold exactly 3 odds
```

```text
Input:  nums = [2, 4, 6], k = 1
Output: 0        # there are no odd numbers at all
```

```text
Input:  nums = [2, 2, 2, 1, 2, 2, 1, 2, 2, 2], k = 2
Output: 16
```

## Constraints

- 1 <= nums.length <= 5 * 10^4
- 1 <= nums[i] <= 10^5
- 1 <= k <= nums.length

## Follow-up

The parity of each element is all that matters — can you turn this into a classic "subarrays summing to k" problem and solve it in one pass?
