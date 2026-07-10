Handle each query independently. For a value `x` from `nums1`, locate it in `nums2`, then walk rightward from that position looking for the first value larger than `x`. The first hit is the answer; running off the end means there is none, so record `-1`.

This mirrors the definition directly with two nested scans and no extra data structures.

```javascript
function nextGreaterElement(nums1, nums2) {
  const ans = [];
  for (const x of nums1) {
    const start = nums2.indexOf(x);
    let greater = -1;
    for (let j = start + 1; j < nums2.length; j++) {
      if (nums2[j] > x) {
        greater = nums2[j];
        break;
      }
    }
    ans.push(greater);
  }
  return ans;
}
```

## Why it works

Because the values are distinct, `indexOf(x)` pinpoints exactly where `x` sits. Scanning strictly to the right and stopping at the first larger value yields the next greater element by definition; if the scan finishes without a hit, `-1` correctly signals that none exists.

## Complexity

- Time: O(n * m) — for each of the n elements in `nums1`, locating it and scanning right each cost up to m, the length of `nums2`.
- Space: O(1) — only the output array, no auxiliary storage.
