The definition talks about permutations, so the most literal solution is to generate every permutation of `1..n` and test each one against the divisibility rule.

There is no cleverness here — build permutations with in-place swaps, and whenever a full ordering is assembled, scan it once to check the rule at every position.

```javascript
function countArrangement(n) {
  const nums = Array.from({ length: n }, (_, i) => i + 1);
  let total = 0;

  function isBeautiful(arr) {
    for (let i = 0; i < arr.length; i++) {
      const pos = i + 1, val = arr[i];
      if (val % pos !== 0 && pos % val !== 0) return false;
    }
    return true;
  }

  function permute(k) {
    if (k === nums.length) {
      if (isBeautiful(nums)) total++;
      return;
    }
    for (let i = k; i < nums.length; i++) {
      [nums[k], nums[i]] = [nums[i], nums[k]];
      permute(k + 1);
      [nums[k], nums[i]] = [nums[i], nums[k]];
    }
  }

  permute(0);
  return total;
}
```

## Why it works

`permute` builds every ordering of `nums` by swapping each remaining value into the current slot `k` and recursing, then swapping back to restore the array for the next branch. Once `k` reaches the end, `nums` holds one full permutation, and `isBeautiful` checks the rule at every 1-indexed position.

## Complexity

- Time: O(n! * n) — n! permutations, each checked in O(n).
- Space: O(n) — recursion depth plus the reused `nums` array.
