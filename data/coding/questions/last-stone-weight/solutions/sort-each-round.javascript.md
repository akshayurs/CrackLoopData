The same idea in JavaScript: keep a plain array and re-sort it every round to expose the two heaviest stones at the end. Smash them, and if a remainder is left, push it back in for the next round.

Simple to reason about, though the repeated sorting is wasteful once the array grows.

```javascript
function lastStoneWeight(stones) {
  const arr = [...stones];
  while (arr.length > 1) {
    arr.sort((a, b) => a - b);
    const heaviest = arr.pop();
    const second = arr.pop();
    if (heaviest !== second) {
      arr.push(heaviest - second);
    }
  }
  return arr.length ? arr[0] : 0;
}
```

## Why it works

Sorting before each smash puts the two largest values at the end of the array, so popping twice always retrieves the current two heaviest stones. Pushing back the difference (when the stones aren't equal) keeps the array valid for the next iteration. Once at most one stone remains, that value (or `0`) is the answer.

## Complexity

- Time: O(n² log n) — up to n rounds, each paying O(n log n) to re-sort.
- Space: O(n) — the working array of stones.
