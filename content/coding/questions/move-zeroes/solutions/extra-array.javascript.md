The simplest way to think about it: the answer is just "all the non-zero values, in order, followed by enough zeros to fill the rest." So build that list directly.

Filter out the non-zero elements into a fresh array, push zeros until it is back to full length, then copy the values back into `nums` in place.

```javascript
function moveZeroes(nums) {
    const result = nums.filter((n) => n !== 0);
    while (result.length < nums.length) result.push(0);
    for (let i = 0; i < nums.length; i++) nums[i] = result[i];
    return nums;
}
```

## Why it works

`filter` keeps the non-zero values in their original left-to-right order, so their relative positions are preserved. The number of pushed zeros equals the number that were dropped, so lengths match. Copying `result` back into `nums` mutates the original array the caller holds.

## Complexity

- Time: O(n) — one pass to filter, one pass to copy back.
- Space: O(n) — the temporary array holds up to n elements.
