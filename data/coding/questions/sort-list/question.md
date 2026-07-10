You are given the head of a singly linked list. Sort the nodes by their values in ascending order and return the head of the sorted list.

You must reuse the existing nodes — do not build a brand-new list of copies.

## Examples

```text
Input:  head = [4, 2, 1, 3]
Output: [1, 2, 3, 4]
```

```text
Input:  head = [-1, 5, 3, 4, 0]
Output: [-1, 0, 3, 4, 5]
```

```text
Input:  head = []
Output: []
```

## Constraints

- The number of nodes in the list is in the range [0, 5 * 10^4].
- -10^5 <= Node.val <= 10^5

## Follow-up

Can you sort the list in O(n log n) time using only O(1) extra space — i.e. without an auxiliary array or a recursion stack?
