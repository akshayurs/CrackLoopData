The most direct reading: try every pair `(i, j)` with `i < j` and check whether they sum to the target. It ignores the fact that the array is sorted, but it is the honest baseline you would state first before optimizing.

Because positions are 1-indexed, we add one to each loop counter when returning.

```python
def two_sum(numbers, target):
    n = len(numbers)
    for i in range(n):
        for j in range(i + 1, n):
            if numbers[i] + numbers[j] == target:
                return [i + 1, j + 1]
    return []
```

## Why it works

The outer loop fixes the first element; the inner loop scans every later element, so each unordered pair is examined exactly once. The moment a pair reaches `target` we return its 1-indexed positions, and the one-solution guarantee means we never fall through to the empty return.

## Complexity

- Time: O(n²) — about n²/2 pairs are checked.
- Space: O(1) — only loop counters, no extra structure.
