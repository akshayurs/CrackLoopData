Since the array is sorted, the occurrences of the target form one contiguous block. Instead of scanning, run binary search twice: once biased toward the left to find the first index, and once biased toward the right to find the last index.

The trick is a single boundary-finding helper. When looking for the left edge, keep moving left even after a match; when looking for the right edge, keep moving right after a match. Each search costs O(log n), so the whole answer is logarithmic.

```javascript
function searchRange(nums, target) {
    function bound(isFirst) {
        let lo = 0, hi = nums.length - 1, ans = -1;
        while (lo <= hi) {
            const mid = Math.floor((lo + hi) / 2);
            if (nums[mid] === target) {
                ans = mid;
                if (isFirst) hi = mid - 1;
                else lo = mid + 1;
            } else if (nums[mid] < target) {
                lo = mid + 1;
            } else {
                hi = mid - 1;
            }
        }
        return ans;
    }
    return [bound(true), bound(false)];
}
```

## Why it works

Each call converges on a boundary: on a match we record `mid` but keep shrinking toward the desired side, so the last recorded index is the extreme occurrence. If the target is absent, no match is ever recorded and both calls return `-1`, giving `[-1, -1]`.

## Complexity

- Time: O(log n) — two binary searches, each halving the range.
- Space: O(1) — only a handful of indices.
