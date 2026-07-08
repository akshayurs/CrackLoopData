You are given the head of a singly linked list `L0 → L1 → … → Ln-1 → Ln`. Reorder the nodes into the pattern `L0 → Ln → L1 → Ln-1 → L2 → Ln-2 → …`, interleaving nodes from the front and the back of the list.

You must rewire the existing nodes — do not create new nodes or change any node's value, only relink them. Return the head of the reordered list.

## Examples

```text
Input:  head = [1, 2, 3, 4]
Output: [1, 4, 2, 3]
```

```text
Input:  head = [1, 2, 3, 4, 5]
Output: [1, 5, 2, 4, 3]
```

```text
Input:  head = [1]
Output: [1]
```

## Constraints

- 1 <= number of nodes <= 5 * 10^4
- 1 <= Node.val <= 1000

## Follow-up

Can you do it in O(1) extra space, without copying the nodes into an auxiliary array?
