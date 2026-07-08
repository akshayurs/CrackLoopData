You are given a sorted array of distinct integers `nums` and a `target` value. Return the index of `target` if it is present. If it is not, return the index where it would need to be inserted so the array stays sorted.

## Examples

```text
Input:  nums = [1, 3, 5, 6], target = 5
Output: 2        # 5 sits at index 2
```

```text
Input:  nums = [1, 3, 5, 6], target = 2
Output: 1        # 2 belongs between 1 and 3
```

```text
Input:  nums = [1, 3, 5, 6], target = 7
Output: 4        # 7 is larger than everything, goes at the end
```

## Constraints

- 1 <= nums.length <= 10^4
- -10^4 <= nums[i] <= 10^4
- nums is sorted in strictly increasing order.
- -10^4 <= target <= 10^4

## Follow-up

The linear scan is O(n). Can you do it in O(log n)?
