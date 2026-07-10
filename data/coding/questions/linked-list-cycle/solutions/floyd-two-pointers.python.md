You can decide the question with no extra memory by racing two pointers through the list at different speeds — Floyd's tortoise-and-hare. The slow pointer advances one node per step; the fast pointer advances two. If the list ends, the fast pointer reaches `None` and there is no cycle. But if there is a cycle, the fast pointer eventually laps the slow one inside the loop, and the two land on the same node.

Think of it as two runners on a track: on a straight road the faster one simply finishes, but on a circular track the faster one is guaranteed to catch the slower from behind.

```python
def has_cycle(head):
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow is fast:
            return True
    return False
```

## Why it works

If there is no cycle, `fast` or `fast.next` becomes `None` and the loop exits with `False`. If there is a cycle, both pointers are eventually inside it; each step the fast pointer closes the gap to the slow pointer by exactly one node, so the gap shrinks to zero and they meet. The meeting must happen before the gap could "skip past," since it changes by one per step — guaranteeing termination.

## Complexity

- Time: O(n) — the pointers meet within a constant factor of one pass.
- Space: O(1) — only two pointers are used.
