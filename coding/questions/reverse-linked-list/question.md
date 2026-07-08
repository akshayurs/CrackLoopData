You are given the `head` of a singly linked list. Reverse the list so that the last node becomes the new head, and return the head of the reversed list.

The reversal must relink the existing nodes — you rearrange the `next` pointers rather than rebuilding the list from copied values.

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

Can you reverse the list both iteratively (O(1) extra space) and recursively?
