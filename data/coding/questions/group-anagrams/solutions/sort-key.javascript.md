Anagrams share one property that survives rearrangement: sort their letters and they become identical. So the sorted form of a string is a fingerprint that every member of a group agrees on — `"eat"`, `"tea"`, and `"ate"` all sort to `"aet"`.

Use that fingerprint as a `Map` key. Walk the list once, sort each string to get its key, and push the original string into the bucket for that key. The buckets are the answer.

```javascript
function groupAnagrams(strs) {
  const buckets = new Map();
  for (const s of strs) {
    const key = s.split("").sort().join("");
    if (!buckets.has(key)) buckets.set(key, []);
    buckets.get(key).push(s);
  }
  return [...buckets.values()];
}
```

## Why it works

Two strings are anagrams exactly when their multisets of characters match, and sorting canonicalizes that multiset into a single comparable string. Strings with the same sorted key land in the same bucket; strings with different letters never collide. Because we push the original (unsorted) string, each group preserves the input words.

## Complexity

- Time: O(n · k log k) — for n strings of max length k, each sort costs O(k log k).
- Space: O(n · k) — every character is stored once across the buckets.
