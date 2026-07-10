You're given the head of a singly linked list. Swap every two adjacent nodes — the 1st with the 2nd, the 3rd with the 4th, and so on — then return the new head. If the list has an odd number of nodes, the last one is left in place. You must rewire the actual nodes rather than just relabeling their values.

## Examples

```text
Input:  head = [1, 2, 3, 4]
Output: [2, 1, 4, 3]
```

```text
Input:  head = [1, 2, 3]
Output: [2, 1, 3]
```

```text
Input:  head = []
Output: []
```

## Constraints

- 0 <= number of nodes <= 100
- 0 <= Node.val <= 100
- You may not modify the values stored in the nodes — only the pointers between them.

## Follow-up

Can you do it in a single pass, using only O(1) extra space beyond the list itself?
