The most literal reading of "reversed" is: read off every value, then lay them back down in the opposite order. Walk the list once to copy each `val` into a plain array, then walk that array back to front, wiring up a brand-new chain of nodes as you go.

This sidesteps any pointer-rewiring puzzle entirely — the trade-off is that it throws away the original nodes and pays for a second array plus a full set of new nodes.

```javascript
function reverseList(head) {
  const values = [];
  let node = head;
  while (node) {
    values.push(node.val);
    node = node.next;
  }

  const dummy = new ListNode(0);
  let tail = dummy;
  for (let i = values.length - 1; i >= 0; i--) {
    tail.next = new ListNode(values[i]);
    tail = tail.next;
  }
  return dummy.next;
}
```

## Why it works

The first loop records the sequence of values in their original order. Walking the array from its last index down to `0` visits them tail-first, so appending a fresh node for each one, in that order, reconstructs the exact mirror image of the input. The `dummy` node just avoids special-casing the very first append.

## Complexity

- Time: O(n) — one pass to read the values, one pass to rebuild.
- Space: O(n) — the values array plus n freshly allocated nodes.
