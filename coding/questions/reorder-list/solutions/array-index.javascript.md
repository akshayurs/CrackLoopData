A singly linked list can only be walked forward, but the target pattern keeps needing the *last* remaining node — something you can't reach without either reversing part of the list or giving yourself random access. The easiest way to get random access is to record every node in a plain array first.

Once the nodes sit in an indexable array, run two indices toward each other from both ends, splicing `next` pointers to alternate front, back, front, back, until they meet in the middle.

```javascript
function reorderList(head) {
  if (head === null) return head;
  const nodes = [];
  for (let node = head; node !== null; node = node.next) {
    nodes.push(node);
  }
  let lo = 0;
  let hi = nodes.length - 1;
  while (lo < hi) {
    nodes[lo].next = nodes[hi];
    lo += 1;
    if (lo === hi) break;
    nodes[hi].next = nodes[lo];
    hi -= 1;
  }
  nodes[lo].next = null;
  return head;
}
```

## Why it works

The desired order `L0, Ln-1, L1, Ln-2, …` is just "take from the front, then from the back, repeat" — exactly what a converging pair of indices over an array produces. Writing `nodes[lo].next = nodes[hi]` then `nodes[hi].next = nodes[lo]` stitches each pair together before the indices step inward. The loop stops the instant the two indices meet or cross, and the last node visited has its `next` forced to `null` so the list doesn't loop back on itself.

## Complexity

- Time: O(n) — one pass to collect nodes, one pass to relink them.
- Space: O(n) — the array stores a reference to every node.
