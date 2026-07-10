You're given the head of a singly linked list. Numbering the nodes starting at 1, gather every node sitting at an odd position into one run, followed by every node at an even position — each group keeping its original relative order. Return the head of this regrouped list.

This is about rewiring the existing nodes, not sorting by value — a node's position in the list decides its group, not what it holds.

## Examples

```text
Input:  head = [1, 2, 3, 4, 5]
Output: [1, 3, 5, 2, 4]
```

```text
Input:  head = [2, 1, 3, 5, 6, 4, 7]
Output: [2, 3, 6, 7, 1, 5, 4]
```

```text
Input:  head = []
Output: []
```

## Constraints

- 0 <= number of nodes <= 10^4
- -10^6 <= Node.val <= 10^6

## Follow-up

Can you reorder the list in O(n) time using only O(1) extra space — no auxiliary array or new nodes?
