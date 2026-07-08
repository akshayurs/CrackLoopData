You are given an array `nums` of length `n` where every value is an integer between `1` and `n` (inclusive). Some numbers in this range show up more than once, and as a result others never show up at all. Return a list of all the numbers in the range `[1, n]` that are missing from `nums`.

The returned numbers can be in any order.

## Examples

```text
Input:  nums = [4, 3, 2, 7, 8, 2, 3, 1]
Output: [5, 6]        # range is 1..8; 5 and 6 never appear
```

```text
Input:  nums = [1, 1]
Output: [2]           # range is 1..2; the second slot is taken by a duplicate 1
```

```text
Input:  nums = [2, 2, 2]
Output: [1, 3]        # range is 1..3; only 2 is present
```

## Constraints

- 1 <= n <= 10^5, where n = nums.length
- 1 <= nums[i] <= n

## Follow-up

Can you do it without allocating extra space for another data structure (the output list does not count) and in linear time?
