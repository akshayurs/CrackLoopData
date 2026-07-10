The most direct way to find "the node `n` from the end" is to first find out how long the list is. Walk it once counting nodes, then convert that count into a position from the *front*: the node to remove sits at index `length - n` (0-indexed), and the node just before it sits at `length - n - 1`.

A dummy node in front of `head` avoids a special case when the head itself is the one being removed — you can always talk about "the node before the one to delete," even when that's the dummy.

```javascript
function removeNthFromEnd(head, n) {
  let length = 0;
  let node = head;
  while (node !== null) {
    length++;
    node = node.next;
  }

  const dummy = new ListNode(0, head);
  let prev = dummy;
  for (let i = 0; i < length - n; i++) {
    prev = prev.next;
  }

  prev.next = prev.next.next;
  return dummy.next;
}
```

## Why it works

After the first pass, `length` is the total node count, so the target sits `length - n` steps after the dummy. Walking `prev` that many steps lands it exactly one node before the target, regardless of whether the target is the head, the tail, or anywhere in between. Relinking `prev.next` past the target removes it, and returning `dummy.next` handles the case where the removed node was the original head.

## Complexity

- Time: O(L) — one pass to count, one pass to locate, where L is the list length.
- Space: O(1) — a fixed number of pointers plus the dummy node.
