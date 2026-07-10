The most literal way to think about rotation is by value, not by pointer surgery. Walk the list once to copy every `val` into a plain array. Since rotating by the full length of the list gives back the same list, only `k % n` actually matters — reduce `k` first. The rotated order is then "the last `k` values, followed by everything before them," built with two array slices.

Once the new order is known, throw away the original nodes and build a fresh chain from scratch. It's wasteful compared to reusing what you already have, but it's the obvious first pass.

```javascript
function rotateRight(head, k) {
  const values = [];
  let node = head;
  while (node !== null) {
    values.push(node.val);
    node = node.next;
  }
  const n = values.length;
  if (n === 0) return null;

  k %= n;
  const rotated = values.slice(n - k).concat(values.slice(0, n - k));

  const dummy = new ListNode(0);
  let tail = dummy;
  for (const v of rotated) {
    tail.next = new ListNode(v);
    tail = tail.next;
  }
  return dummy.next;
}
```

## Why it works

`values.slice(n - k)` is the last `k` elements — the ones that should move to the front — and `values.slice(0, n - k)` is everything before them, in its original order. Concatenating the two reproduces the rotated sequence exactly, and it holds even when `k` is `0`: `slice(n)` is empty and `slice(0, n)` is the whole array, so `rotated` equals `values` unchanged. The final loop then materializes that sequence as new nodes.

## Complexity

- Time: O(n) — one pass to read values, one pass to rebuild.
- Space: O(n) — the values array plus n freshly allocated nodes.
