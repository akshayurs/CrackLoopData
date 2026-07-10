Flatten the problem: tag every value with which list it came from, then sort all of those `(value, list)` pairs together. Any range that covers all `k` lists now corresponds to a contiguous window of this sorted sequence that contains every list tag at least once — a classic "smallest window with all tags" sliding-window problem.

Slide the window's right edge forward, and whenever all `k` tags are present, shrink from the left as far as possible while keeping that property, checking each valid window against the best range seen so far.

```javascript
function smallestRange(lists) {
  const merged = [];
  lists.forEach((lst, i) => lst.forEach((value) => merged.push([value, i])));
  merged.sort((a, b) => a[0] - b[0]);

  const k = lists.length;
  const count = new Map();
  let formed = 0;
  let left = 0;
  let best = [merged[0][0], merged[merged.length - 1][0]];

  for (let right = 0; right < merged.length; right++) {
    const [, tag] = merged[right];
    count.set(tag, (count.get(tag) || 0) + 1);
    if (count.get(tag) === 1) formed++;

    while (formed === k) {
      const lo = merged[left][0];
      const hi = merged[right][0];
      if (hi - lo < best[1] - best[0]) best = [lo, hi];
      const leftTag = merged[left][1];
      count.set(leftTag, count.get(leftTag) - 1);
      if (count.get(leftTag) === 0) formed--;
      left++;
    }
  }

  return best;
}
```

## Why it works

Sorting merges all `k` lists into one non-decreasing sequence while remembering each value's origin. A window covers every list exactly when its tags include all `k` list indices, so shrinking the window from the left while it stays valid finds the tightest such window. Because the sequence is sorted, the window's endpoints are the true `lo`/`hi` of the range, and the greedy shrink never skips a better answer.

## Complexity

- Time: O(N log N) — N is the total number of elements; dominated by the sort.
- Space: O(N) — the merged array and the tag-count map.
