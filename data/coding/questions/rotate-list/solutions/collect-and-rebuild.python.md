The most literal way to think about rotation is by value, not by pointer surgery. Walk the list once to copy every `val` into a plain array. Since rotating by the full length of the list gives back the same list, only `k % n` actually matters — reduce `k` first. The rotated order is then just "the last `k` values, followed by everything before them," which Python's slicing expresses directly.

Once the new order is known, throw away the original nodes and build a fresh chain from scratch. It's wasteful compared to reusing what you already have, but it's the obvious first pass.

```python
def rotate_right(head, k):
    values = []
    node = head
    while node:
        values.append(node.val)
        node = node.next
    n = len(values)
    if n == 0:
        return None

    k %= n
    rotated = values[-k:] + values[:-k]

    dummy = ListNode()
    tail = dummy
    for v in rotated:
        tail.next = ListNode(v)
        tail = tail.next
    return dummy.next
```

## Why it works

`values[-k:]` is the last `k` elements — the ones that should move to the front — and `values[:-k]` is everything before them, which keeps its relative order. Concatenating the two reproduces the rotated sequence exactly, and the trick works even when `k` is `0`: `values[-0:]` is the whole array and `values[:-0]` is empty, so `rotated` equals `values` unchanged. The final loop then just materializes that sequence as new nodes.

## Complexity

- Time: O(n) — one pass to read values, one pass to rebuild.
- Space: O(n) — the values array plus n freshly allocated nodes.
