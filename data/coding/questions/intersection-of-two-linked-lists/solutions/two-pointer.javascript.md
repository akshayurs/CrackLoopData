The reason the brute force is slow is that it never accounts for the two lists possibly being different lengths — that mismatch is what forces it to keep re-scanning. Fix the length difference instead of comparing every pair.

Walk two pointers forward one step at a time, one starting at `headA` and the other at `headB`. Whenever a pointer runs off the end of its own list, redirect it to the *other* list's head instead of stopping. After at most one such switch each, both pointers will have traveled `lenA + lenB` steps in total by the time they reach the intersection — so they arrive there in lockstep, whether or not the lists share a node.

```javascript
function getIntersectionNode(headA, headB) {
  let pointerA = headA;
  let pointerB = headB;

  while (pointerA !== pointerB) {
    pointerA = pointerA !== null ? pointerA.next : headB;
    pointerB = pointerB !== null ? pointerB.next : headA;
  }

  return pointerA;
}
```

## Why it works

Let the unique prefix of `listA` have length `a` and the unique prefix of `listB` have length `b`, with a shared tail after that. `pointerA` travels `a + shared + b` nodes by the time it finishes its second pass through the combined path, and `pointerB` travels `b + shared + a` — the same total distance. Because both pointers cover an equal number of steps before reaching the shared tail, they land on the same node at the same time: the intersection, if one exists. If the lists never intersect, both pointers become `null` simultaneously after covering `a + b` steps each, and the loop ends with `pointerA` equal to `null`.

## Complexity

- Time: O(m + n) — each pointer traverses at most one full pass of each list.
- Space: O(1) — two pointers, no auxiliary storage.
