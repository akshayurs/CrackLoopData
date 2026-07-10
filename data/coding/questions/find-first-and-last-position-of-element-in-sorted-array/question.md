You are given an array of integers `nums` sorted in non-decreasing order and a `target` value. Find the index of the first occurrence and the index of the last occurrence of `target` in the array.

Return the answer as a two-element array `[first, last]`. If `target` is not present, return `[-1, -1]`.

## Examples

```text
Input:  nums = [5, 7, 7, 8, 8, 10], target = 8
Output: [3, 4]        # 8 first appears at index 3 and last at index 4
```

```text
Input:  nums = [5, 7, 7, 8, 8, 10], target = 6
Output: [-1, -1]      # 6 is not in the array
```

```text
Input:  nums = [], target = 0
Output: [-1, -1]
```

## Constraints

- 0 <= nums.length <= 10^5
- -10^9 <= nums[i] <= 10^9
- `nums` is sorted in non-decreasing order.
- -10^9 <= target <= 10^9

## Follow-up

The array is sorted — can you achieve O(log n) time instead of scanning every element?
