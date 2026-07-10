You are given an array of integers `nums` of length `n` and an integer `target`. Pick exactly three distinct elements whose sum is as close to `target` as possible, and return that sum.

Closeness is measured by absolute difference: the sum `s` is better than `s'` when `|s - target| < |s' - target|`. You may assume each input has exactly one closest sum.

## Examples

```text
Input:  nums = [-1, 2, 1, -4], target = 1
Output: 2        # -1 + 2 + 1 = 2, which is distance 1 from the target
```

```text
Input:  nums = [0, 0, 0], target = 1
Output: 0        # the only triple sums to 0, distance 1
```

```text
Input:  nums = [1, 1, 1, 0], target = -100
Output: 2        # 1 + 1 + 0 = 2 is the smallest reachable sum
```

## Constraints

- 3 <= nums.length <= 500
- -1000 <= nums[i] <= 1000
- -10^4 <= target <= 10^4
- Exactly one closest sum exists.

## Follow-up

The obvious solution tries every triple in O(n³). Can you sort the array first and reach O(n²)?
