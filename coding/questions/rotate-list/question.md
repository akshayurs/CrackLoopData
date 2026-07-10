You're given the head of a singly linked list and a non-negative integer `k`. Rotate the list to the right by `k` places — imagine repeatedly snipping off the last node and stitching it back on as the new first node, `k` times — and return the head of the resulting list.

## Examples

```text
Input:  head = [1, 2, 3, 4, 5], k = 2
Output: [4, 5, 1, 2, 3]
```

```text
Input:  head = [0, 1, 2], k = 4
Output: [2, 0, 1]        # k=4 on a 3-node list is the same as k=1
```

```text
Input:  head = [], k = 5
Output: []
```

## Constraints

- 0 <= number of nodes <= 500
- -100 <= Node.val <= 100
- 0 <= k <= 2 * 10^9

## Follow-up

Can you do it without allocating a fresh copy of every node?
