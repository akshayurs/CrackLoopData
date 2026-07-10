Sorting every distinct word costs O(n log n) even though only `k` of them are ever returned. A heap lets you pay for just the `k` extractions you need on top of a linear-time build.

Encode each word as `(-count, word)` so that Python's min-heap naturally pops in the order the problem wants: higher counts first, and for equal counts, the smaller string first (since flipping the sign of `count` doesn't touch the string comparison). Heapify once, then pop `k` times.

```python
import heapq
from collections import Counter


def top_k_frequent_words(words, k):
    counts = Counter(words)
    heap = [(-count, word) for word, count in counts.items()]
    heapq.heapify(heap)
    return [heapq.heappop(heap)[1] for _ in range(k)]
```

## Why it works

`heapq` is a min-heap over tuples, compared element-by-element. Negating the count turns "most frequent" into "smallest first," and since the first tuple element already differs whenever counts differ, the second element (`word`) only breaks ties — where ascending string order is exactly the alphabetical tie-break the problem asks for. `heapify` arranges all entries in linear time, so each of the `k` pops is the only work that costs a logarithm.

## Complexity

- Time: O(n + k log n) — counting and heapifying the up-to-n distinct words is O(n); each of the k pops costs O(log n).
- Space: O(n) — the counter and the heap each hold up to n entries.
