Instead of touching values, rewire the `next` pointers directly. A dummy node placed just before the head gives every pair — including the first — a uniform predecessor to reconnect through, so there's no special case for swapping the very first two nodes.

Keep a `prev` pointer sitting just before each pair. For the pair `(first, second)`, splice `second` in front of `first`: point `prev.next` at `second`, `first.next` at whatever came after `second`, and `second.next` at `first`. Then advance `prev` to `first`, which is now the tail of the swapped pair, and repeat on the next pair.

```javascript
function swapPairs(head) {
  const dummy = new ListNode(0);
  dummy.next = head;
  let prev = dummy;

  while (prev.next !== null && prev.next.next !== null) {
    const first = prev.next;
    const second = first.next;

    first.next = second.next;
    second.next = first;
    prev.next = second;

    prev = first;
  }

  return dummy.next;
}
```

## Why it works

Before each swap, `prev.next` is the correct start of the untouched remainder — either the dummy on the first iteration or the previous pair's now-trailing node. The three pointer reassignments thread `second` in front of `first` while preserving the link to the rest of the list. Advancing `prev` to `first` sets up the next pair with the same invariant, and the loop stops as soon as fewer than two nodes remain, correctly leaving a lone trailing node untouched.

## Complexity

- Time: O(n) — each node's pointers are rewired exactly once.
- Space: O(1) — a fixed handful of pointers, no matter how long the list is.
