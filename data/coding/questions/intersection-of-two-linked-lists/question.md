You're given the heads of two singly linked lists, `listA` and `listB`. Somewhere along the way the two lists may merge and share the exact same chain of nodes all the way to the end. Find the node where they first come together and return it — or `null` (`None` in Python) if the two lists never share a node.

The check is about node identity, not node value: two separate nodes that happen to hold equal numbers are not an intersection. You must not modify either list's structure.

## Examples

```text
Input:  listA = [4, 1, 8, 4, 5]
        listB = [5, 6, 1, 8, 4, 5]
        (the lists share the same node objects from value 8 onward)
Output: 8
```

```text
Input:  listA = [2, 6, 4]
        listB = [1, 5]
Output: null
```

```text
Input:  listA = [1, 9, 1, 2, 4]
        listB = [3, 2, 4]
        (the lists share the same node objects from value 2 onward)
Output: 2
```

## Constraints

- 1 <= listA.length, listB.length <= 3 * 10^4
- 1 <= Node.val <= 10^9
- Neither list contains a cycle.
- If the lists intersect, the shared suffix is the same sequence of node objects in both, not merely equal values.

## Follow-up

Can you find the intersection in O(m + n) time using only O(1) extra memory?
