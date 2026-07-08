Sorting each string is more work than the problem needs. What actually defines an anagram group is the count of each of the 26 lowercase letters — not their order. So build a fixed 26-length count array for each string and use *that* as the key, skipping the O(k log k) sort entirely.

Serialize the counts into a string (e.g. `"1,0,0,...,1"`) so it can key a `Map`. Every anagram produces the same serialized counts, so the grouping matches the sort approach but each key costs only a linear pass over the string.

```javascript
function groupAnagrams(strs) {
  const buckets = new Map();
  for (const s of strs) {
    const counts = new Array(26).fill(0);
    for (const ch of s) {
      counts[ch.charCodeAt(0) - 97]++;
    }
    const key = counts.join(",");
    if (!buckets.has(key)) buckets.set(key, []);
    buckets.get(key).push(s);
  }
  return [...buckets.values()];
}
```

## Why it works

Two strings are anagrams if and only if their per-letter frequency vectors are equal, so the serialized 26-count string is a perfect canonical key. Building it scans the string once — no comparison sort. Identical vectors collide into one bucket; any difference in even a single letter's count yields a different key and a separate group.

## Complexity

- Time: O(n · k) — n strings, each scanned once in O(k); building the 26-length key is O(k + 26).
- Space: O(n · k) — the stored strings dominate; each key is a constant 26 entries.
