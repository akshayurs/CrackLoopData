There's no need to copy anything: the nodes you already have are exactly the nodes you need, just wired the wrong way. Walk the list once, and at each node flip its `next` pointer to point backward at the node you just left, instead of forward at the node you're about to visit.

Two running pointers do the work — one (`previous`) trails behind and marks the front of the reversed section built so far, the other (`current`) is the node being flipped. Before you overwrite `current.next`, you have to stash it somewhere, or the rest of the list becomes unreachable.

```javascript
function reverseList(head) {
  let previous = null;
  let current = head;
  while (current !== null) {
    const following = current.next;
    current.next = previous;
    previous = current;
    current = following;
  }
  return previous;
}
```

## Why it works

`previous` is always the head of the portion already reversed. Saving `following = current.next` preserves the link to the untouched remainder before `current.next = previous` bends the current node backward. Sliding both pointers forward advances the boundary by one node each iteration. Once `current` becomes `null`, `previous` is sitting on the former last node — the new head.

## Complexity

- Time: O(n) — every node is visited exactly once.
- Space: O(1) — a fixed handful of pointers, no matter how long the list is.
