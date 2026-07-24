You are given the `head` of a singly linked list containing `n` nodes, numbered `L0, L1, …, Ln-1` in list order. Rearrange the nodes in place so they follow the zig-zag pattern `L0, Ln-1, L1, Ln-2, L2, Ln-3, …`, alternating between the front and back of the original list.

You must reorder by relinking the existing nodes — do not clone nodes or copy values into new ones. Return the head of the reordered list.

## Examples

```text
Input:  head = [2, 4, 6, 8]
Output: [2, 8, 4, 6]
```

```text
Input:  head = [1, 3, 5, 7, 9]
Output: [1, 9, 3, 7, 5]
```

```text
Input:  head = [10]
Output: [10]
```

## Constraints

- 1 <= number of nodes <= 5 * 10^4
- 1 <= Node.val <= 1000

## Follow-up

Can you do it using only O(1) extra space, without copying node references into an auxiliary array?
