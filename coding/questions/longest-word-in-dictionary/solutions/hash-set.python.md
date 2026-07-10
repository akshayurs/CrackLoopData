Drop every word into a set so membership checks are O(1), then test each word directly: it is buildable exactly when all of its proper prefixes also live in that set. Track the best answer seen so far, preferring a longer word or, on a length tie, the lexicographically smaller one.

This is the straightforward reading of the definition — no trie, just prefix slicing and a hash lookup for each one.

```python
def longest_word(words):
    word_set = set(words)
    best = ""
    for word in words:
        buildable = all(word[:i] in word_set for i in range(1, len(word)))
        if buildable and (len(word) > len(best) or (len(word) == len(best) and word < best)):
            best = word
    return best
```

## Why it works

A word is buildable only if every shorter prefix that would have been typed on the way to it is itself a word in the array. Checking `word[:i]` for every `i` from 1 up to (but not including) the full length verifies exactly that chain. Comparing candidates by length first, then lexicographically, reproduces the required tie-break rule.

## Complexity

- Time: O(n · L²) — n words, each with up to L prefixes, each prefix slice and lookup costing O(L).
- Space: O(n · L) — the hash set stores every word.
