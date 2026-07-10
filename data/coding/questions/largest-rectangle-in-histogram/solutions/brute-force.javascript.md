Fix each bar as the shortest one in the rectangle. From bar `i` at height `heights[i]`, extend as far left and as far right as every neighbouring bar is at least that tall — that span is the widest rectangle whose height is capped by bar `i`. Track the best area across all choices of `i`.

Because every rectangle is limited by its shortest bar, and each bar gets its turn as that limiter, no candidate rectangle escapes the search.

```javascript
function largestRectangleArea(heights) {
  const n = heights.length;
  let best = 0;
  for (let i = 0; i < n; i++) {
    let left = i;
    while (left > 0 && heights[left - 1] >= heights[i]) left--;
    let right = i;
    while (right < n - 1 && heights[right + 1] >= heights[i]) right++;
    best = Math.max(best, heights[i] * (right - left + 1));
  }
  return best;
}
```

## Why it works

For a fixed limiter `i`, the tallest rectangle of height `heights[i]` stretches until it meets a strictly shorter bar on each side. The width `right - left + 1` counts every bar in that run. The true maximal rectangle has some shortest bar, and the pass that fixes that bar as `i` rebuilds it exactly.

## Complexity

- Time: O(n²) — each bar may scan the whole array while expanding.
- Space: O(1) — only index and running-max variables.
