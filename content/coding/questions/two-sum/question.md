You are given an array of integers `nums` and an integer `target`. Return the indices of the two numbers that add up to `target`.

Each input has **exactly one** solution, and you may not use the same element twice. You can return the answer in any order.

## Examples

```text
Input:  nums = [2, 7, 11, 15], target = 9
Output: [0, 1]        # nums[0] + nums[1] = 2 + 7 = 9
```

```text
Input:  nums = [3, 2, 4], target = 6
Output: [1, 2]        # nums[1] + nums[2] = 2 + 4 = 6
```

```text
Input:  nums = [3, 3], target = 6
Output: [0, 1]
```

## Constraints

- 2 <= nums.length <= 10^4
- -10^9 <= nums[i] <= 10^9
- -10^9 <= target <= 10^9
- Exactly one valid pair exists.

## Follow-up

Can you solve it in a single pass — better than the O(n²) brute force?
