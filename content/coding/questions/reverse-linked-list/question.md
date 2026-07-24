You're given the head of a singly linked list. Flip the direction every `next` pointer travels so the list reads back to front, then return the node that is now first — the one that used to be last.

## Examples

```text
Input:  head = [1, 2, 3, 4, 5]
Output: [5, 4, 3, 2, 1]
```

```text
Input:  head = [1, 2]
Output: [2, 1]
```

```text
Input:  head = []
Output: []
```

## Constraints

- 0 <= number of nodes <= 5000
- -5000 <= Node.val <= 5000

## Follow-up

Can you do it with only O(1) extra space, without allocating any new nodes?
