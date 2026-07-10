You are given the head of a singly linked list and an integer `val`. Delete every node whose value equals `val`, and return the head of the resulting list.

The list may become empty, and `val` may not appear at all — both are valid outcomes.

## Examples

```text
Input:  head = [1, 2, 6, 3, 4, 5, 6], val = 6
Output: [1, 2, 3, 4, 5]
```

```text
Input:  head = [], val = 1
Output: []
```

```text
Input:  head = [7, 7, 7, 7], val = 7
Output: []
```

## Constraints

- 0 <= number of nodes <= 10^4
- 1 <= Node.val <= 50
- 0 <= val <= 50
