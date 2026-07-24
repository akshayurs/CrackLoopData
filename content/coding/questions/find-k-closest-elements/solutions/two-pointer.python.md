A key observation: because `arr` is sorted, the `k` closest elements always form one contiguous block. So instead of ranking everything, start with the whole array as a candidate window and shrink it from the ends until only `k` elements remain.

At each step compare the two boundary elements. Whichever end is farther from `x` cannot belong to the answer, so discard it. On a tie, drop the right end — the left (smaller) value is preferred.

```python
def find_closest_elements(arr, k, x):
    left, right = 0, len(arr) - 1
    while right - left + 1 > k:
        if x - arr[left] > arr[right] - x:
            left += 1
        else:
            right -= 1
    return arr[left:right + 1]
```

## Why it works

The answer is a contiguous window, so the only real choice is where its edges land. Between the two current boundaries, the farther one is strictly worse than the closer one and worse than everything between them, so it is safe to drop. The tie condition uses a strict `>`, meaning equal distances discard the right end and keep the smaller-valued left element. When the window holds exactly `k` items it is returned as-is, already ascending.

## Complexity

- Time: O(n - k) — each iteration removes one element until k remain.
- Space: O(1) — only two pointers, ignoring the output slice.
