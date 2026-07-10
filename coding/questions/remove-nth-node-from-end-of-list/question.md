You are given the `head` of a singly linked list and an integer `n`. Remove the `n`th node counting from the **end** of the list, and return the head of the resulting list.

`n` is guaranteed to be a valid position — between 1 and the number of nodes in the list, inclusive.

## Examples

```text
Input:  head = [1, 2, 3, 4, 5], n = 2
Output: [1, 2, 3, 5]
```

```text
Input:  head = [1], n = 1
Output: []
```

```text
Input:  head = [1, 2], n = 1
Output: [1]
```

## Constraints

- The number of nodes is between 1 and 30.
- 0 <= Node.val <= 100
- 1 <= n <= number of nodes

## Follow-up

Can you do it in one pass through the list?
