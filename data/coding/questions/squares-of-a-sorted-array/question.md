You are given an integer array `nums` sorted in **non-decreasing** order. Return a new array containing the square of each number, also sorted in non-decreasing order.

## Examples

```text
Input:  nums = [-4, -1, 0, 3, 10]
Output: [0, 1, 9, 16, 100]        # squares are [16, 1, 0, 9, 100], sorted
```

```text
Input:  nums = [-7, -3, 2, 3, 11]
Output: [4, 9, 9, 49, 121]
```

```text
Input:  nums = [-5, -3, -2, -1]
Output: [1, 4, 9, 25]
```

## Constraints

- 1 <= nums.length <= 10^4
- -10^4 <= nums[i] <= 10^4
- `nums` is sorted in non-decreasing order.

## Follow-up

Squaring then sorting is O(n log n). Can you produce the sorted result in O(n) time by exploiting the fact that the input is already sorted?
