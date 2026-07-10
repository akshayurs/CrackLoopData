Put every word in a hash set, then check each word on its own: can this word be cut into pieces such that every piece is itself in the set, using at least two pieces? That is a word-break question, solved with a boolean DP over prefix lengths — `dp[j]` is true if the prefix of length `j` can be fully covered by dictionary pieces.

The only wrinkle is excluding the trivial "one piece" split, since a word obviously equals itself. We simply skip the split that would use the whole word as a single unbroken piece.

```python
def find_concatenated_words(words):
    word_set = set(words)
    result = []
    for word in words:
        n = len(word)
        dp = [False] * (n + 1)
        dp[0] = True
        for j in range(1, n + 1):
            for i in range(j):
                if not dp[i]:
                    continue
                if i == 0 and j == n:
                    continue
                if word[i:j] in word_set:
                    dp[j] = True
                    break
            if dp[n]:
                break
        if dp[n]:
            result.append(word)
    return sorted(result)
```

## Why it works

`dp[i]` means the prefix `word[:i]` can be assembled from words already in the set. To extend to `dp[j]`, we look for some earlier boundary `i` with `dp[i]` true and check whether the middle chunk `word[i:j]` is also a known word — if so `dp[j]` becomes true too. Skipping `i == 0 and j == n` blocks the single-piece "whole word" match, so `dp[n]` can only turn true through a genuine multi-word split.

## Complexity

- Time: O(n · L³) — n words, each doing an O(L²) DP where every transition slices and hashes an O(L) substring.
- Space: O(n · L) — the hash set stores every word.
