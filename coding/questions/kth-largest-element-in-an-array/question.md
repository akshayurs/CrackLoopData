Given an integer array `nums` and an integer `k`, return the `k`-th largest element in the array — not the k-th distinct element, so duplicates count individually toward `k`.

You must solve it without fully sorting the array in the "obvious" O(n log n) way — think about how a heap can find just the one value you need.

## Examples

```text
Input:  nums = [3, 2, 1, 5, 6, 4], k = 2
Output: 5        # sorted desc: [6, 5, 4, 3, 2, 1] -> 2nd largest is 5
```

```text
Input:  nums = [3, 2, 3, 1, 2, 4, 5, 5, 6], k = 4
Output: 4        # sorted desc: [6, 5, 5, 4, 3, 3, 2, 2, 1] -> 4th largest is 4
```

```text
Input:  nums = [7, 7, 7], k = 1
Output: 7
```

## Constraints

- 1 <= k <= nums.length <= 10^5
- -10^4 <= nums[i] <= 10^4
- 1 <= k <= nums.length
