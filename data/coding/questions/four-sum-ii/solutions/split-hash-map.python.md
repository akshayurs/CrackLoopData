Split the four arrays into two halves. Precompute every pairwise sum `a[i] + b[j]` and tally how often each sum occurs in a hash map. Then, for every pair from `c` and `d`, the tuple sums to zero exactly when `a[i] + b[j] == -(c[k] + d[l])`, so you just look up how many left-half pairs produce that complement.

This turns two of the four loops into O(1) map lookups: `n²` pairs on the left build the map, `n²` pairs on the right query it, and the stored count contributes all matching tuples at once.

```python
from collections import Counter

def four_sum_count(a, b, c, d):
    left = Counter(x + y for x in a for y in b)
    count = 0
    for z in c:
        for w in d:
            count += left.get(-(z + w), 0)
    return count
```

## Why it works

`left[s]` records how many `(i, j)` pairs give sum `s`. A full tuple sums to zero iff its right-half sum `c[k] + d[l]` cancels some left-half sum, i.e. `left` contains `-(c[k] + d[l])`. Adding that stored count folds in every matching `(i, j)` pair in one step, so no tuple is missed or double-counted.

## Complexity

- Time: O(n²) — one `n²` pass to build the map, one `n²` pass to query it.
- Space: O(n²) — the map holds up to n² distinct pairwise sums.
