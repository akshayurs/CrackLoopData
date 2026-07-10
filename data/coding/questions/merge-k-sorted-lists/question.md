You are given an array `lists` holding the heads of `k` singly linked lists, where each list is already sorted in non-decreasing order. Combine all of their nodes into one linked list that is also sorted in non-decreasing order, and return its head.

## Examples

```text
Input:  lists = [[1, 4, 5], [1, 3, 4], [2, 6]]
Output: [1, 1, 2, 3, 4, 4, 5, 6]
```

```text
Input:  lists = []
Output: []
```

```text
Input:  lists = [[]]
Output: []
```

## Constraints

- k == lists.length
- 0 <= k <= 10^4
- 0 <= lists[i].length <= 500
- -10^4 <= lists[i][j] <= 10^4
- Each `lists[i]` is sorted in non-decreasing order.
- The total number of nodes across all lists does not exceed 10^4.

## Follow-up

The brute-force approach throws away the fact that each list is already sorted. Can you merge all k lists by only ever comparing their current fronts against each other?
