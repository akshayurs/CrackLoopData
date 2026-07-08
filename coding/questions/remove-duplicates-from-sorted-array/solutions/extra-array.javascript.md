The most direct reading of the problem: collect the distinct values, then write them back to the front of the array. Because the input is sorted, a value is new exactly when it differs from the last value you kept, so a single scan builds the unique list.

Copy that list back over the first slots of `nums` and return its length. It costs a second array, but it maps cleanly onto the problem statement.

```javascript
function removeDuplicates(nums) {
  const unique = [];
  for (const n of nums) {
    if (unique.length === 0 || unique[unique.length - 1] !== n) {
      unique.push(n);
    }
  }
  for (let i = 0; i < unique.length; i++) {
    nums[i] = unique[i];
  }
  return unique.length;
}
```

## Why it works

Duplicates in a sorted array are always adjacent, so comparing each element to the last one pushed is enough to filter repeats — `unique` ends up holding every distinct value in its original order. Writing those values back over `nums[0..k)` leaves the front of the array in the required state, and `k` is simply the count of distinct values.

## Complexity

- Time: O(n) — one pass to build the list, one pass to copy it back.
- Space: O(n) — the auxiliary array can hold up to n values.
