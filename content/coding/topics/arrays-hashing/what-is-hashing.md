A **hash map** (dictionary, `unordered_map`, `HashMap`) stores key → value pairs and answers "is this key present, and what is its value?" in **O(1)** average time. A **hash set** is the same idea without the value — membership in O(1).

That single superpower — constant-time lookup — is what turns a slow nested-loop scan into a single pass. Instead of asking "does any *other* element pair with me?" (O(n) per element), you remember what you have already seen and ask the map directly.

The classic trade is **space for time**: spend O(n) memory on the map to drop the running time from O(n²) to O(n).

A typical one-pass shape:

```
seen = empty map
for each element x at index i:
    if key_we_need(x) is in seen:
        return the match using seen[key_we_need(x)]
    record x in seen (value → i)
```

**Frequency counting** is the other half of the pattern: map each value to how many times it appears, then read answers straight off the counts — anagrams, majority element, and "top-K" all reduce to counting.
