The most direct idea is to remember every node you have already visited. Walk the list one node at a time; before moving on, record the node itself (its identity, not its value) in a set. If you ever arrive at a node that is already in the set, you have looped back — that is a cycle. If instead you fall off the end into `None`, the list is acyclic.

Storing node identities rather than values matters: two different nodes can share the same value, so only object identity reliably signals that you have returned to a place you have been.

```python
def has_cycle(head):
    seen = set()
    node = head
    while node:
        if node in seen:
            return True
        seen.add(node)
        node = node.next
    return False
```

## Why it works

A finite list without a cycle is exhausted after visiting each node once, so the loop ends at `None` and returns `False`. If a cycle exists, traversal can never reach `None`; because the number of distinct nodes is finite, you must eventually revisit one already in `seen`, which returns `True`. Python sets key on object identity for these node objects, so distinct nodes never collide even with equal values.

## Complexity

- Time: O(n) — each node is inspected at most once.
- Space: O(n) — the set may hold every node.
