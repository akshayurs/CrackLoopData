Given an unsorted array of integers `nums`, find the length of the longest run of values that are consecutive integers — meaning each value is exactly one more than the previous one. The values may appear in any order in the array, and duplicates should be treated as a single value.

Return the length of the longest such run.

## Examples

```text
Input:  nums = [100, 4, 200, 1, 3, 2]
Output: 4        # the run 1, 2, 3, 4 has length 4
```

```text
Input:  nums = [0, 3, 7, 2, 5, 8, 4, 6, 0, 1]
Output: 9        # 0, 1, 2, 3, 4, 5, 6, 7, 8 (the duplicate 0 counts once)
```

```text
Input:  nums = []
Output: 0        # no elements, no run
```

## Constraints

- 0 <= nums.length <= 10^5
- -10^9 <= nums[i] <= 10^9
- The runs are measured by value, not by position — order in the array is irrelevant.

## Follow-up

Sorting gives an easy O(n log n) answer. Can you reach O(n) time?
