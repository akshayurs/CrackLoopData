The most direct reading of the problem: square every element, then sort the results. It ignores the fact that the input is already sorted, but it is the honest baseline you would state first before optimizing.

Squaring can reshuffle order because negatives closer to zero become small squares while large-magnitude negatives become large squares, so a final sort is what guarantees the required ordering.

```javascript
function sortedSquares(nums) {
    return nums.map((x) => x * x).sort((a, b) => a - b);
}
```

## Why it works

Each value's square is independent of the others, so computing all squares and then sorting produces exactly the non-decreasing sequence of squares the problem asks for. The numeric comparator is essential — the default sort would order the numbers lexicographically.

## Complexity

- Time: O(n log n) — squaring is O(n), the sort dominates.
- Space: O(n) — the output array of squares.
