The first instinct is to sidestep pointers entirely: read every node's value into an array, swap adjacent entries in that array, then walk the list a second time and write the swapped values back into the existing nodes.

It produces the right output sequence, but it quietly breaks the rule that only pointers may change — the nodes themselves keep their original identity while their `val` fields get overwritten. It's a useful warm-up because it separates "get the order right" from "rewire the structure correctly," which the optimal approach has to solve at the same time.

```javascript
function swapPairs(head) {
  const values = [];
  for (let node = head; node !== null; node = node.next) {
    values.push(node.val);
  }

  for (let i = 0; i + 1 < values.length; i += 2) {
    [values[i], values[i + 1]] = [values[i + 1], values[i]];
  }

  let node = head;
  for (const v of values) {
    node.val = v;
    node = node.next;
  }

  return head;
}
```

## Why it works

The first pass captures the list's values in order. Swapping each even-indexed entry with its neighbor reproduces the pairwise-swapped sequence without touching any pointers. The second pass streams those values back into the original nodes in order, so the list's length and node count are untouched — only what each node holds changes.

## Complexity

- Time: O(n) — two linear passes over the list.
- Space: O(n) — the values array holds every node's value.
