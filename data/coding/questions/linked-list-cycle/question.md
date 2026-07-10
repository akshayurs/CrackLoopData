You are given the `head` of a singly linked list. Determine whether the list contains a cycle — that is, whether some node can be reached again by repeatedly following `next` pointers.

A cycle exists when a node's `next` pointer links back to an earlier node in the list, so a traversal would loop forever instead of reaching a `null` tail. Return `true` if there is a cycle and `false` otherwise.

To describe the input, the tests use an array of node values plus an integer `pos` — the index the tail's `next` points back to, or `-1` when the tail points to `null`. Note that `pos` is only a way to encode the input; it is not passed to your function.

## Examples

```text
Input:  values = [3, 2, 0, -4], pos = 1   # tail links back to the node at index 1
Output: true
```

```text
Input:  values = [1, 2], pos = 0          # tail links back to the head
Output: true
```

```text
Input:  values = [1], pos = -1            # single node, no cycle
Output: false
```

## Constraints

- 0 <= number of nodes <= 10^4
- -10^5 <= Node.val <= 10^5
- `pos` is -1 or a valid index into the list.

## Follow-up

Can you decide it using O(1) extra memory, without a set of visited nodes?
