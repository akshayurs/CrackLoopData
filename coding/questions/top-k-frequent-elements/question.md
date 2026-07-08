You are given an integer array `nums` and an integer `k`. Return the `k` values that appear most often in the array, sorted in ascending order.

The answer is **guaranteed to be unique** — no two distinct values are tied in a way that makes the top `k` ambiguous.

## Examples

```text
Input:  nums = [1, 1, 1, 2, 2, 3], k = 2
Output: [1, 2]        # 1 appears 3 times, 2 appears twice, 3 once
```

```text
Input:  nums = [4, 4, 4, 5, 5, 6], k = 1
Output: [4]           # 4 is the single most frequent value
```

```text
Input:  nums = [7], k = 1
Output: [7]
```

## Constraints

- 1 <= nums.length <= 10^5
- -10^4 <= nums[i] <= 10^4
- 1 <= k <= number of distinct values in `nums`
- The set of top `k` frequent values is unique.

## Follow-up

Your algorithm should run faster than the O(n log n) cost of fully sorting the array. Can you reach O(n)?
