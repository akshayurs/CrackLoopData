Take the problem literally: split the sentence into words, and for each word scan the entire dictionary looking for a root that is a prefix of it. Among all matching roots, keep the shortest one.

There is no preprocessing — every word pays the full cost of scanning every root, but the logic mirrors the problem statement almost line for line, which makes it a safe first pass.

```python
def replace_words(dictionary, sentence):
    result = []
    for word in sentence.split(" "):
        best = None
        for root in dictionary:
            if word.startswith(root) and (best is None or len(root) < len(best)):
                best = root
        result.append(best if best is not None else word)
    return " ".join(result)
```

## Why it works

For each word, `best` tracks the shortest root seen so far that is a genuine prefix of the word — `str.startswith` checks that directly. Because every root in the dictionary is tried, the loop can never miss a valid match, and the length comparison guarantees the final `best` is the shortest of them. Words with no matching root fall back to themselves.

## Complexity

- Time: O(w * r * L) — w words, r roots, and up to L character comparisons per `startswith` check.
- Space: O(w) — the output word list, ignoring the input.
