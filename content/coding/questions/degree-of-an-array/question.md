You are given a non-empty array of non-negative integers `nums`. The **degree** of the array is the largest number of times any single value appears in it.

Return the length of the **shortest contiguous subarray** of `nums` that has the same degree as the full array.

## Examples

```text
Input:  nums = [1, 2, 2, 3, 1]
Output: 2        # degree is 2 (both 1 and 2 appear twice); the two 2's sit next to each other -> [2, 2]
```

```text
Input:  nums = [1, 2, 2, 3, 1, 4, 2]
Output: 6        # degree is 3 (value 2 appears three times); shortest window covering all 2's is [2, 2, 3, 1, 4, 2]
```

```text
Input:  nums = [5]
Output: 1        # a single element has degree 1; the whole array already achieves it
```

## Constraints

- 1 <= nums.length <= 5 * 10^4
- 0 <= nums[i] <= 5 * 10^4

## Follow-up

Can you do it in one pass over the array, without first scanning to compute the degree separately?
