To hit O(1) space, drop the map and lean on a cancellation idea (the Boyer–Moore voting algorithm). Keep a single candidate and a counter. Each element either votes for the current candidate (increment) or against it (decrement); when the counter hits zero, adopt the current element as the new candidate.

The intuition: pair off each occurrence of the majority value with a different value and both cancel. Since the majority appears more than half the time, it cannot be fully cancelled — whatever survives is the answer.

```javascript
function majorityElement(nums) {
  let candidate = null;
  let count = 0;
  for (const x of nums) {
    if (count === 0) candidate = x;
    count += x === candidate ? 1 : -1;
  }
  return candidate;
}
```

## Why it works

Think of every non-candidate as cancelling one candidate vote. The true majority has strictly more than `n / 2` votes, so even if every other element cancels one of its votes, it still has a positive surplus left over. Whenever the count resets to zero the eliminated prefix contained equal numbers of the candidate and non-candidate values, so discarding it never removes the global majority.

## Complexity

- Time: O(n) — a single pass over the array.
- Space: O(1) — just the candidate and an integer counter.
