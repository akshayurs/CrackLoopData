The most direct reading of the problem: try every pair `(i, j)` and XOR them, keeping the largest result seen. No bit tricks, no extra memory — just two nested loops.

It is the honest baseline you would state first in an interview, before reaching for a trie.

```python
def max_xor(nums):
    best = 0
    n = len(nums)
    for i in range(n):
        for j in range(i + 1, n):
            best = max(best, nums[i] ^ nums[j])
    return best
```

## Why it works

The outer loop fixes the first element; the inner loop pairs it with every later element, so every unordered pair is XORed exactly once. Tracking the running maximum guarantees the largest XOR across all pairs is returned once the loops finish.

## Complexity

- Time: O(n²) — every pair is XORed once.
- Space: O(1) — only a running maximum, no extra structure.
