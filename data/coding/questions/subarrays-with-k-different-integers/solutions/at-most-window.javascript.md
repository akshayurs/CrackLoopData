Counting subarrays with *exactly* `k` distinct values is awkward, but counting subarrays with *at most* `k` distinct values is a textbook sliding window: grow the right edge, and whenever the window holds more than `k` distinct values, shrink the left edge until it is valid again. For every right endpoint, the window length is exactly the number of valid subarrays ending there, so summing lengths gives the "at most `k`" total.

The trick is the identity `exactly(k) = atMost(k) - atMost(k - 1)`. Run the same helper twice and subtract — the difference cancels every subarray with fewer than `k` distinct values and leaves precisely those with `k`.

```javascript
function subarraysWithKDistinct(nums, k) {
  const atMost = (m) => {
    const freq = new Map();
    let left = 0, total = 0;
    for (let right = 0; right < nums.length; right++) {
      const x = nums[right];
      freq.set(x, (freq.get(x) || 0) + 1);
      while (freq.size > m) {
        const y = nums[left];
        freq.set(y, freq.get(y) - 1);
        if (freq.get(y) === 0) freq.delete(y);
        left++;
      }
      total += right - left + 1;
    }
    return total;
  };

  return atMost(k) - atMost(k - 1);
}
```

## Why it works

`atMost(m)` keeps `[left, right]` as the longest window ending at `right` with no more than `m` distinct values; adding `right - left + 1` counts every subarray ending at `right`, because any shorter suffix is also valid. A subarray with `d` distinct values is counted by `atMost(k)` when `d <= k` and by `atMost(k - 1)` when `d <= k - 1`; subtracting leaves exactly those with `d == k`.

## Complexity

- Time: O(n) — each helper advances `left` and `right` at most n times, and we call it twice.
- Space: O(n) — the frequency map holds at most the distinct values in a window.
