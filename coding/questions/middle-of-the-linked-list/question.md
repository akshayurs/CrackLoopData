You're given the head of a singly linked list. Find its middle node and return it. If the list has an even number of nodes, return the **second** of the two middle nodes.

## Examples

```text
Input:  head = [1, 2, 3, 4, 5]
Output: [3, 4, 5]        # 3 is the middle; the rest of the list follows it
```

```text
Input:  head = [1, 2, 3, 4, 5, 6]
Output: [4, 5, 6]        # two middles (3 and 4) exist; return the second one
```

```text
Input:  head = [1]
Output: [1]
```

## Constraints

- 1 <= number of nodes <= 100
- 1 <= Node.val <= 100

## Follow-up

Can you find the middle in a single pass, without first counting the length of the list?
