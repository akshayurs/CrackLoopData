You are given a **circular** integer array `nums` (the element after the last one wraps around to the first). For every position, find its *next greater element* — the first value you encounter, scanning forward and wrapping around the end if needed, that is strictly larger than the current value. If no such value exists, use `-1`.

Return an array `result` where `result[i]` is the next greater element for `nums[i]`.

## Examples

```text
Input:  nums = [1, 2, 1]
Output: [2, -1, 2]      # for the last 1, wrap around to reach 2
```

```text
Input:  nums = [1, 2, 3, 4, 3]
Output: [2, 3, 4, -1, 4]
```

```text
Input:  nums = [5, 4, 3, 2, 1]
Output: [-1, 5, 5, 5, 5]
```

## Constraints

- 1 <= nums.length <= 10^4
- -10^9 <= nums[i] <= 10^9
- The array is circular: index `n-1` is followed by index `0`.

## Follow-up

The brute force rescans the array for every element. Can you answer all positions in a single linear pass?
