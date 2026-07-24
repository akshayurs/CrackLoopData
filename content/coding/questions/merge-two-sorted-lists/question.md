You are given the heads of two singly linked lists `l1` and `l2`, each already sorted in non-decreasing order. Merge them into one sorted list by splicing together the existing nodes, and return the head of the merged list.

The result must reuse the original nodes (do not allocate a new node per value); only the `next` pointers should be rewired.

## Examples

```text
Input:  l1 = [1, 2, 4], l2 = [1, 3, 4]
Output: [1, 1, 2, 3, 4, 4]
```

```text
Input:  l1 = [], l2 = []
Output: []
```

```text
Input:  l1 = [], l2 = [0]
Output: [0]
```

## Constraints

- 0 <= number of nodes in each list <= 50
- -100 <= Node.val <= 100
- Both `l1` and `l2` are sorted in non-decreasing order.

## Follow-up

Can you do it in O(1) extra space, without recursion?
