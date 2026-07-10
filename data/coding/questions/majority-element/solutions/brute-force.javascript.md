The definition says the answer appears more than half the time, so the most literal approach is to test each value directly: pick an element, count how often it occurs across the whole array, and return it once its count clears the `n / 2` bar.

No extra structures, no cleverness — just the honest baseline you would state first before reaching for something faster.

```javascript
function majorityElement(nums) {
  const n = nums.length;
  for (const candidate of nums) {
    let count = 0;
    for (const x of nums) {
      if (x === candidate) count++;
    }
    if (count > Math.floor(n / 2)) return candidate;
  }
  return -1;
}
```

## Why it works

Every distinct value in the array becomes a candidate at some point. Because a majority element is guaranteed to exist, exactly one candidate will have a count exceeding `n / 2`, and we return it the first time that condition holds. The trailing `return -1` is unreachable given the guarantee.

## Complexity

- Time: O(n²) — for each of the n candidates we scan all n elements.
- Space: O(1) — only a running counter, no auxiliary storage.
