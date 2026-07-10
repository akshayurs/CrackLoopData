Trade memory for speed. Walk the array once, and for each number ask whether the value that completes the pair has already been seen. A `Map` answers that in O(1), removing the inner loop.

Record each value's index as you go, so the complement's later appearance yields both positions immediately.

```javascript
function twoSum(nums, target) {
  const seen = new Map();
  for (let i = 0; i < nums.length; i++) {
    const complement = target - nums[i];
    if (seen.has(complement)) {
      return [seen.get(complement), i];
    }
    seen.set(nums[i], i);
  }
  return [];
}
```

## Why it works

`seen` maps a value to the index where it appeared. For the current number, its partner must be `target - nums[i]`; if that partner is in `seen`, the pair is found. Recording the current value only *after* the check means an element is never paired with itself, and one pass is enough because a partner is always an earlier element.

## Complexity

- Time: O(n) — one pass; each `Map` lookup and insert is O(1) on average.
- Space: O(n) — the map holds up to n entries.
