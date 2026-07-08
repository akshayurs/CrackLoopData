The reordering weaves nodes from the two ends toward the middle, but a singly linked list only lets you walk forward — you can't step backward to reach `Ln`. The simplest fix is to give up random access to the nodes by first dumping them into an array.

Once every node sits in an indexable array, keep a `left` pointer at the front and a `right` pointer at the back. Alternately append `nodes[left]` then `nodes[right]`, moving the pointers inward until they meet, and relink each node's `next` as you go.

```javascript
function reorderList(head) {
  if (!head) return head;
  const nodes = [];
  for (let cur = head; cur; cur = cur.next) nodes.push(cur);
  let left = 0;
  let right = nodes.length - 1;
  while (left < right) {
    nodes[left].next = nodes[right];
    left += 1;
    if (left === right) break;
    nodes[right].next = nodes[left];
    right -= 1;
  }
  nodes[left].next = null;
  return head;
}
```

## Why it works

The target order `L0, Ln, L1, Ln-1, …` is exactly "front, back, next-front, next-back, …". Storing nodes in an array gives O(1) access to both ends, so the two-pointer sweep emits them in that order. The final node written gets its `next` set to `null` to terminate the list and avoid a cycle.

## Complexity

- Time: O(n) — one pass to collect, one pass to rewire.
- Space: O(n) — the array holds a reference to every node.
