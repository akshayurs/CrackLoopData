The most direct idea is to remember every node you have already visited. Walk the list one node at a time and add each node object to a `Set` before advancing. If you reach a node that is already in the set, the list has looped back on itself — a cycle. If you instead run off the end into `null`, there is no cycle.

A `Set` keyed on the node objects tracks identity, not value, so two distinct nodes that happen to hold the same value are never confused for one another.

```javascript
function hasCycle(head) {
  const seen = new Set();
  let node = head;
  while (node) {
    if (seen.has(node)) return true;
    seen.add(node);
    node = node.next;
  }
  return false;
}
```

## Why it works

Without a cycle, the traversal visits each node once and terminates at `null`, returning `false`. With a cycle, `null` is never reached; since there are finitely many nodes, some node must be encountered a second time, and `seen.has(node)` catches it. JavaScript `Set` compares objects by reference, so distinct nodes with equal values stay distinct.

## Complexity

- Time: O(n) — each node is visited at most once.
- Space: O(n) — the set can grow to the full list.
