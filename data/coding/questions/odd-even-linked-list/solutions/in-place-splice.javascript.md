No copy is needed at all: the odd and even nodes are already interleaved in the list, so you can grow two chains — one for odd positions, one for even — by having each chain reach two nodes ahead and grab every other node as it passes. Once the even chain runs out, splice its head onto the tail of the odd chain.

Keep a pointer into each chain (`odd`, `even`) plus a fixed pointer to where the even chain started (`evenHead`), since that's the only way to find it again after the odd chain has stolen all its `next` pointers.

```javascript
function oddEvenList(head) {
  if (!head || !head.next) return head;
  let odd = head;
  let even = head.next;
  const evenHead = even;
  while (even && even.next) {
    odd.next = even.next;
    odd = odd.next;
    even.next = odd.next;
    even = even.next;
  }
  odd.next = evenHead;
  return head;
}
```

## Why it works

At every step `odd.next` is pointed at the node two ahead (skipping the even node in between), and the same is done for `even`, so the two chains advance in lockstep while consuming the original list exactly once. The loop stops as soon as `even` (or `even.next`) runs out, meaning every node has been assigned to one chain. Attaching `evenHead` to the end of the odd chain concatenates the two runs in the required order.

## Complexity

- Time: O(n) — each node's `next` pointer is rewritten once.
- Space: O(1) — only a few pointers are used; no extra array or nodes.
