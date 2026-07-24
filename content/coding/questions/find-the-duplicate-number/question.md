You are given an array `nums` of `n + 1` integers where every value lies in the range `[1, n]`. Exactly one value is duplicated — it may appear two or more times — and every other value appears exactly once. Find and return that duplicated value.

You must not modify the array, and you may only read it (no sorting it in place).

## Examples

```text
Input:  nums = [1, 3, 4, 2, 2]
Output: 2
```

```text
Input:  nums = [3, 1, 3, 4, 2]
Output: 3
```

```text
Input:  nums = [2, 2, 2, 2, 2]
Output: 2        # the duplicate can repeat more than twice
```

## Constraints

- 1 <= n <= 10^5
- nums.length == n + 1
- 1 <= nums[i] <= n
- All integers in `nums` appear once, except one value which appears two or more times.
- The array must not be modified.

## Follow-up

Can you find the duplicate in O(n) time using only O(1) extra space?
