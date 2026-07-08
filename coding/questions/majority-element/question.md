Given an array of integers `nums` of length `n`, one value appears more than `n / 2` times. Return that value.

You may assume the array is non-empty and that a majority element always exists, so you never have to handle the "no winner" case.

## Examples

```text
Input:  nums = [5, 5, 2]
Output: 5              # 5 appears 2 times out of 3 (> 3 / 2)
```

```text
Input:  nums = [1, 3, 3, 1, 3, 3, 4]
Output: 3              # 3 appears 4 times out of 7 (> 7 / 2)
```

```text
Input:  nums = [9]
Output: 9              # a single element is trivially the majority
```

## Constraints

- 1 <= nums.length <= 5 * 10^4
- -10^9 <= nums[i] <= 10^9
- A majority element (one appearing more than ⌊n / 2⌋ times) is guaranteed to exist.

## Follow-up

Can you find it in O(n) time using only O(1) extra space?
