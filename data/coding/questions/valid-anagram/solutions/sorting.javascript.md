Two strings are anagrams exactly when their letters, laid out in a canonical order, are identical. Sorting is the simplest way to reach that canonical form: put both strings in sorted order and see if they match.

It is the honest baseline you would reach for first in an interview — no counting, no bookkeeping, just compare the sorted characters. A quick length check up front rules out the obvious non-anagrams before doing any work.

```javascript
function isAnagram(s, t) {
  if (s.length !== t.length) return false;
  const sort = (str) => str.split("").sort().join("");
  return sort(s) === sort(t);
}
```

## Why it works

If `t` is a rearrangement of `s`, then sorting both collapses every rearrangement to the same sequence of characters, so the sorted strings are equal. If they differ in any letter or in how many times a letter appears, the sorted forms diverge at some position and the comparison fails. The length guard is an early exit — strings of unequal length can never be anagrams.

## Complexity

- Time: O(n log n) — dominated by sorting both strings.
- Space: O(n) — splitting into character arrays allocates a copy of each string.
