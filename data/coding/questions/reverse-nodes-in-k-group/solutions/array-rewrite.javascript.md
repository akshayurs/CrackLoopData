The safest way to reverse groups of k nodes without getting tangled in pointer edge cases is to sidestep pointer surgery entirely: read every node's value into a plain array, do the reversing there where indexing is trivial, then walk the original list once more and overwrite each node's value from the rebuilt array.

Split the array into chunks of size k, reverse only the chunks that are exactly k long, and copy a shorter trailing chunk through unchanged — then flatten everything back into one sequence before writing it into the list.

```javascript
function reverseKGroup(head, k) {
  const vals = [];
  for (let node = head; node; node = node.next) vals.push(node.val);

  const fullGroups = Math.floor(vals.length / k) * k;
  const rewritten = [];
  for (let start = 0; start < fullGroups; start += k) {
    rewritten.push(...vals.slice(start, start + k).reverse());
  }
  rewritten.push(...vals.slice(fullGroups));

  let node = head;
  for (const v of rewritten) {
    node.val = v;
    node = node.next;
  }
  return head;
}
```

## Why it works

`fullGroups` rounds the node count down to the nearest multiple of `k`, so every chunk `vals.slice(start, start + k)` taken before that point is exactly `k` long and safe to reverse. Whatever sits past `fullGroups` is the too-short tail, appended unchanged. Concatenating the reversed chunks with that untouched tail reproduces the exact node order the problem asks for, and writing those values back into the existing nodes — rather than allocating new ones — keeps `head` a valid reference to return.

## Complexity

- Time: O(n) — one pass to read values, one to rebuild the order, one to write them back.
- Space: O(n) — `vals` and `rewritten` each hold every node's value.
