The regrouping is really just a stable partition of the nodes by position. If you collect every node into a plain array first, splitting it into "odd-indexed" and "even-indexed" slices is trivial, and relinking the two runs back-to-back is a single pass over the combined order.

This trades the elegance of in-place pointer surgery for something easy to reason about: build the target order explicitly, then rewire `next` to match it.

```javascript
function oddEvenList(head) {
  if (!head) return head;
  const nodes = [];
  for (let node = head; node; node = node.next) nodes.push(node);
  const odd = nodes.filter((_, i) => i % 2 === 0);
  const even = nodes.filter((_, i) => i % 2 === 1);
  const ordered = odd.concat(even);
  for (let i = 0; i < ordered.length - 1; i++) {
    ordered[i].next = ordered[i + 1];
  }
  ordered[ordered.length - 1].next = null;
  return ordered[0];
}
```

## Why it works

Filtering by even array index (0-indexed) picks up every node at an odd position in the list, and the complementary filter picks up the even positions — each preserving original order. Concatenating them yields exactly the required ordering, and relinking consecutive entries reproduces that order as an actual list before the tail is capped with `null`.

## Complexity

- Time: O(n) — one pass to collect nodes, one to relink them.
- Space: O(n) — the arrays hold a reference per node.
