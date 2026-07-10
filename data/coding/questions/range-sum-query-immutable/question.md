You are given an integer array `nums` that never changes, and a list of `queries`. Each query is a pair `[left, right]` (both inclusive). For every query, return the sum of the elements from index `left` through index `right`.

Return the answers in the same order as the queries. Because the array is immutable but many queries may be asked, aim to answer each query quickly.

## Examples

```text
Input:  nums = [-2, 0, 3, -5, 2, -1], queries = [[0, 2], [2, 5], [0, 5]]
Output: [1, -1, -3]
        # [0,2] -> -2 + 0 + 3       = 1
        # [2,5] ->  3 - 5 + 2 - 1   = -1
        # [0,5] -> -2 + 0 + 3 - 5 + 2 - 1 = -3
```

```text
Input:  nums = [1, 2, 3, 4, 5], queries = [[1, 3]]
Output: [9]        # 2 + 3 + 4 = 9
```

```text
Input:  nums = [5], queries = [[0, 0]]
Output: [5]        # a single element
```

## Constraints

- 1 <= nums.length <= 10^4
- -10^5 <= nums[i] <= 10^5
- 0 <= left <= right < nums.length
- Up to 10^4 queries may be asked against the same array.

## Follow-up

The array is fixed but queries are frequent. Can you preprocess once so each query answers in O(1)?
