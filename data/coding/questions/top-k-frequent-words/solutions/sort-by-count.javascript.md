The most direct plan: count how often each word shows up, then rank the distinct words by that count. A single comparator — frequency descending, word ascending — handles the ranking and the tie-break in one step.

Once the distinct words are ordered this way, the answer is just the first `k` of them.

```javascript
function topKFrequentWords(words, k) {
  const counts = new Map();
  for (const w of words) counts.set(w, (counts.get(w) || 0) + 1);

  const ordered = [...counts.keys()].sort((a, b) => {
    const diff = counts.get(b) - counts.get(a);
    return diff !== 0 ? diff : (a < b ? -1 : 1);
  });
  return ordered.slice(0, k);
}
```

## Why it works

The comparator first orders by descending frequency; when two words tie, it falls back to plain string comparison, which puts the alphabetically smaller word first — exactly the tie-break the problem requires. Slicing the first `k` entries of that ordering gives the correct answer.

## Complexity

- Time: O(n log n) — counting is O(n); sorting the up-to-n distinct words dominates.
- Space: O(n) — the map and the sorted array each hold up to n entries.
