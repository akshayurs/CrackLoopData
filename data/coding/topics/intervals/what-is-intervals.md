An **interval** is a range `[start, end]` — a meeting time, a booked range, a numeric span. Interval problems ask you to merge, insert, count overlaps, or select a subset of ranges, and almost every one of them starts the same way: **sort by start (or end) time**.

Once sorted, overlap becomes a single comparison instead of a search: two intervals `a` and `b` (sorted by start) overlap exactly when `b.start <= a.end`. That one inequality is the engine behind merging, insertion, and counting — it turns an O(n²) all-pairs comparison into a single O(n log n) sorted sweep.

The core trade is the same as most sorting-based patterns: pay O(n log n) once to sort, then solve the rest in one linear pass while tracking a "current" interval (or a running count) as you sweep left to right.

A typical merge sweep:

```
sort intervals by start
result = [intervals[0]]
for each interval i starting from the second:
    last = result[-1]
    if i.start <= last.end:
        last.end = max(last.end, i.end)   # merge
    else:
        result.append(i)                  # no overlap, start new group
return result
```

Variants swap what you sort by and what you track: sort by **end** time to greedily pick the maximum number of non-overlapping intervals (activity selection); sweep both starts and ends as separate "events" (+1/-1) to count how many intervals are active at once (meeting rooms); or walk two sorted lists with two pointers to intersect them.
