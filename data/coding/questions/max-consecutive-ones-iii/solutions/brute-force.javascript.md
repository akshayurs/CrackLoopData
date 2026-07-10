Start from the definition directly: try every possible starting index and extend the subarray to the right as far as the flip budget allows. Keep a running count of the zeros seen; the moment that count would exceed `k`, this starting point can go no further, so record the length and move on.

No cleverness, just an honest scan of every candidate window. It is quadratic, but it makes the invariant obvious — a window is valid exactly when it holds at most `k` zeros.

```javascript
function longestOnes(nums, k) {
    const n = nums.length;
    let best = 0;
    for (let start = 0; start < n; start++) {
        let zeros = 0;
        for (let end = start; end < n; end++) {
            if (nums[end] === 0) zeros++;
            if (zeros > k) break;
            best = Math.max(best, end - start + 1);
        }
    }
    return best;
}
```

## Why it works

For a fixed `start`, extending `end` rightward can only add elements, so the zero count is non-decreasing. Once it passes `k` the window is invalid and every longer window from this `start` is invalid too — hence the `break`. Every valid window is considered for some `start`, so the maximum length is found.

## Complexity

- Time: O(n^2) — each start index scans up to the end of the array.
- Space: O(1) — only counters are kept.
