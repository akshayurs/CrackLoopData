Anagrams are defined entirely by *how many* of each letter appear — order is irrelevant. So instead of sorting, tally the letters: add one for every character in `s` and subtract one for every character in `t`. If the two strings match, every count cancels back to zero.

This replaces the O(n log n) sort with a single linear pass, using one map keyed by character. Any count that fails to return to zero means the strings are not anagrams.

```javascript
function isAnagram(s, t) {
  if (s.length !== t.length) return false;
  const counts = {};
  for (const ch of s) counts[ch] = (counts[ch] || 0) + 1;
  for (const ch of t) {
    if (!counts[ch]) return false;
    counts[ch] -= 1;
  }
  return true;
}
```

## Why it works

The first loop records how often each character occurs in `s`. The second loop spends those counts as it walks `t`: if a character is missing or already exhausted (`counts[ch]` is `0` or undefined), `t` has more of it than `s` does, so it cannot be an anagram. Because the lengths are equal, using up every count exactly means the two multisets of characters are identical.

## Complexity

- Time: O(n) — two linear passes, each map operation O(1) on average.
- Space: O(k) — where k is the number of distinct characters (at most 26 for lowercase English letters).
