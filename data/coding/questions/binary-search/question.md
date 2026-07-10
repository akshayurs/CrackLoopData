You are given an array of integers `nums` sorted in strictly increasing order and an integer `target`. Return the index of `target` inside `nums`, or `-1` if it is not present.

Your algorithm must run in `O(log n)` time.

## Examples

```text
Input:  nums = [-1, 0, 3, 5, 9, 12], target = 9
Output: 4        # nums[4] = 9
```

```text
Input:  nums = [-1, 0, 3, 5, 9, 12], target = 2
Output: -1       # 2 is not in nums
```

```text
Input:  nums = [5], target = 5
Output: 0
```

## Constraints

- 1 <= nums.length <= 10^4
- -10^4 <= nums[i], target <= 10^4
- All values in `nums` are unique and sorted in ascending order.

## Follow-up

The linear scan is O(n). Can you exploit the sorted order to reach O(log n)?
