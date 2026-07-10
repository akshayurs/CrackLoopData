The most direct plan: count how often each word shows up, then rank the distinct words by that count. A single composite sort key — frequency descending, word ascending — handles the ranking and the tie-break in one step.

Once the distinct words are ordered this way, the answer is just the first `k` of them.

```python
from collections import Counter


def top_k_frequent_words(words, k):
    counts = Counter(words)
    ordered = sorted(counts, key=lambda word: (-counts[word], word))
    return ordered[:k]
```

## Why it works

Sorting by the tuple `(-counts[word], word)` puts higher-frequency words first, and for equal frequencies (equal `-counts[word]`), the ascending comparison on `word` naturally puts the alphabetically smaller word first — exactly the tie-break the problem requires. Slicing the first `k` entries of that ordering gives the correct answer.

## Complexity

- Time: O(n log n) — counting is O(n); sorting the up-to-n distinct words dominates.
- Space: O(n) — the counter and the sorted list each hold up to n entries.
