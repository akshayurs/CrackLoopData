A **sliding window** is a contiguous sub-range `[left, right]` over an array or string that you grow and shrink instead of recomputing from scratch. Rather than checking every sub-range with a nested loop — O(n²) or worse — you maintain running state (a sum, a count map, a set) as the window's edges move, so each element is added once and removed once.

The trick that makes it fast: moving the window by one step only changes two things — the element entering at `right` and the element leaving at `left`. You update your running state incrementally instead of rescanning the whole window, which is what collapses O(n·k) or O(n²) down to O(n).

There are two flavors:

- **Fixed-size window** — the width `k` is given up front (e.g. max average of a subarray of size k). Slide it one step at a time, updating the running total.
- **Variable-size window** — you grow `right` to bring the window toward validity, then shrink `left` while it stays valid (or push `left` forward while it stays *invalid*), tracking the best window seen.

A typical variable-window shape:

```
left = 0
state = empty tracker (sum, counts, distinct set, etc.)
for right in range(n):
    add element[right] to state
    while window is invalid:
        remove element[left] from state
        left += 1
    update answer using current window [left, right]
```

The window only ever moves forward — `left` and `right` each traverse the array at most once, giving O(n) total work even though it looks like two nested loops.
