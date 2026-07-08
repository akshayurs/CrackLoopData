The reordering weaves nodes from the two ends toward the middle, but a singly linked list only lets you walk forward — you can't step backward to reach `Ln`. The simplest fix is to give up random access to the nodes by first dumping them into an array.

Once every node sits in an indexable list, keep a `left` pointer at the front and a `right` pointer at the back. Alternately append `nodes[left]` then `nodes[right]`, moving the pointers inward until they meet, and relink each node's `next` as you go.

```python
def reorder_list(head):
    if not head:
        return head
    nodes = []
    cur = head
    while cur:
        nodes.append(cur)
        cur = cur.next
    left, right = 0, len(nodes) - 1
    while left < right:
        nodes[left].next = nodes[right]
        left += 1
        if left == right:
            break
        nodes[right].next = nodes[left]
        right -= 1
    nodes[left].next = None
    return head
```

## Why it works

The target order `L0, Ln, L1, Ln-1, …` is exactly "front, back, next-front, next-back, …". Storing nodes in an array gives O(1) access to both ends, so the two-pointer sweep emits them in that order. The final node written gets its `next` set to `None` to terminate the list and avoid a cycle.

## Complexity

- Time: O(n) — one pass to collect, one pass to rewire.
- Space: O(n) — the array holds a reference to every node.
