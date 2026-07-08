Think of the answer as: the smaller of the two heads comes first, followed by the merge of everything that remains. That is a naturally recursive definition — pick the smaller head, then attach the merge of its tail with the other list to its `next`.

Each call decides exactly one node, so the recursion depth equals the total number of nodes.

```javascript
function mergeTwoLists(l1, l2) {
  if (l1 === null) return l2;
  if (l2 === null) return l1;
  if (l1.val <= l2.val) {
    l1.next = mergeTwoLists(l1.next, l2);
    return l1;
  }
  l2.next = mergeTwoLists(l1, l2.next);
  return l2;
}
```

## Why it works

The base cases handle an exhausted list: if one side is empty, the other is already a sorted suffix, so return it directly. Otherwise the node with the smaller value must lead the merged list; we fix it as the head and recurse on the rest. Using `<=` keeps the merge stable and never drops equal values. Because every node is chosen once as a head, the list is fully consumed.

## Complexity

- Time: O(m + n) — each node from both lists is handled by exactly one call.
- Space: O(m + n) — the call stack can grow to the total node count in the worst case.
