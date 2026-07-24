You are given two non-empty linked lists, `l1` and `l2`, each representing a non-negative integer. The digits are stored in reverse order — the head node holds the ones digit — and each node holds a single digit (0-9). Add the two numbers and return the sum as a linked list, using the same reverse-digit convention.

Neither input list has a leading zero, except when the number itself is `0`.

## Examples

```text
Input:  l1 = [2, 4, 3], l2 = [5, 6, 4]
Output: [7, 0, 8]        # 342 + 465 = 807
```

```text
Input:  l1 = [0], l2 = [0]
Output: [0]
```

```text
Input:  l1 = [9, 9, 9, 9, 9, 9, 9], l2 = [9, 9, 9, 9]
Output: [8, 9, 9, 9, 0, 0, 0, 1]        # 9999999 + 9999 = 10009998
```

## Constraints

- The number of nodes in each list is between 1 and 100.
- 0 <= Node.val <= 9
- Neither list has a leading zero, except the number `0` itself.

## Follow-up

Can you produce the result in one pass over both lists, using no extra memory beyond the output?
