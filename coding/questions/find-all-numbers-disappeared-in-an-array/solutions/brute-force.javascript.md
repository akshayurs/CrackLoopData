The most literal reading of the problem: for every candidate value in `1..n`, walk the array and ask "is this value here?". Whatever you never find is missing.

It is the baseline you would state first — no auxiliary structure, just a membership scan per candidate.

```javascript
function findDisappearedNumbers(nums) {
  const n = nums.length;
  const missing = [];
  for (let value = 1; value <= n; value++) {
    let found = false;
    for (const x of nums) {
      if (x === value) {
        found = true;
        break;
      }
    }
    if (!found) missing.push(value);
  }
  return missing;
}
```

## Why it works

The answer set is defined directly against the range `[1, n]`, so we test each member of that range in turn. The inner loop is an honest linear search that stops at the first match; any value whose search fails never appears in `nums` and belongs in the result.

## Complexity

- Time: O(n²) — up to n candidates, each scanning up to n elements.
- Space: O(1) — ignoring the output list, only a flag and counters.
