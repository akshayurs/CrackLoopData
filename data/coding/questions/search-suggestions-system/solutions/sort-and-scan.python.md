Sort the catalog once so matches for any prefix already come out in the right order. Then, for every prefix of `searchWord` (length 1, 2, 3, ...), walk the sorted list and collect the first three entries that start with it.

This redoes a linear scan for every prefix, so it re-examines products you already ruled out on the previous, shorter prefix — simple, but wasteful once the query gets long.

```python
def search_suggestions(products, search_word):
    products.sort()
    result = []
    prefix = ""
    for ch in search_word:
        prefix += ch
        matches = [p for p in products if p.startswith(prefix)][:3]
        result.append(matches)
    return result
```

## Why it works

Sorting the catalog once guarantees that any subset of matches, collected in list order, is already lexicographically sorted — so taking the first three matches is always the three smallest. Checking `startswith` against the growing prefix correctly narrows the candidate set at each step, and slicing to 3 caps the suggestion list as required.

## Complexity

- Time: O(n log n + m * n * L) — one sort, then for each of the `m` prefix lengths a full scan of `n` products with an O(L) prefix check.
- Space: O(n) — the sorted copy of `products` plus the output lists.
