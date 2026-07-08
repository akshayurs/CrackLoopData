Walk the list once, flipping each node's `next` pointer to point at the node you just came from. Keep a `prev` pointer that trails one step behind — it holds the growing reversed prefix. For each node you must stash its original `next` before overwriting it, or you'd lose the rest of the list.

When the walk ends, `prev` sits on the old last node, which is exactly the new head. This uses only a couple of pointers, so no extra space grows with the list.

```javascript
function reverseList(head) {
  let prev = null;
  let curr = head;
  while (curr !== null) {
    const next = curr.next;
    curr.next = prev;
    prev = curr;
    curr = next;
  }
  return prev;
}
```

## Why it works

`prev` always points to the head of the portion already reversed. Saving `next = curr.next` preserves the link into the not-yet-processed tail before `curr.next = prev` redirects the current node backward. Advancing `prev` and `curr` shifts the boundary forward by one. After the last node, `curr` is `null` and `prev` is the former tail — the new head.

## Complexity

- Time: O(n) — one pass over the list.
- Space: O(1) — a fixed set of pointers, regardless of length.
