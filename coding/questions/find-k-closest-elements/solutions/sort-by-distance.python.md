The most direct reading of the problem: rank every element by how far it is from `x`, keep the best `k`, then put them back in order. The comparison key must encode both rules — first the distance `|a - x|`, and for ties the smaller value wins — so sort by the pair `(|a - x|, a)`.

Taking the first `k` of that ordering gives the closest set; a final ascending sort restores the required output order.

```python
def find_closest_elements(arr, k, x):
    by_distance = sorted(arr, key=lambda a: (abs(a - x), a))
    return sorted(by_distance[:k])
```

## Why it works

Sorting on `(abs(a - x), a)` implements the closeness rule exactly: closer elements come first, and equal-distance elements are ordered by value so the smaller one is preferred. The first `k` entries are therefore the `k` closest integers. Since the problem asks for them in ascending order, the closing `sorted` call reorders that slice by value.

## Complexity

- Time: O(n log n) — dominated by the distance sort over all n elements.
- Space: O(n) — the sorted copy of the array.
