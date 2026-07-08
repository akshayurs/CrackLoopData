Instead of rescanning each window, keep a heap that hands back the current maximum instantly. Push every element as `(value, index)` into a max-heap; the top is always the largest value seen so far.

The catch is that the top might sit *outside* the current window. Solve it with lazy deletion: before reading a window's answer, discard any entries whose index has slid off the left edge. Each element is pushed and popped at most once.

```java
import java.util.PriorityQueue;

class Solution {
    public int[] maxSlidingWindow(int[] nums, int k) {
        int n = nums.length;
        int[] result = new int[n - k + 1];
        PriorityQueue<int[]> heap = new PriorityQueue<>((a, b) -> b[0] - a[0]);
        for (int i = 0; i < n; i++) {
            heap.offer(new int[]{nums[i], i});
            if (i >= k - 1) {
                while (heap.peek()[1] <= i - k) heap.poll();
                result[i - k + 1] = heap.peek()[0];
            }
        }
        return result;
    }
}
```

## Why it works

The `PriorityQueue` orders entries by value descending, so `peek` returns the biggest value pushed so far. An entry is valid for the window ending at `i` only when its stored index exceeds `i - k`; stale tops are polled before the max is read. Because a stale entry is removed once and never returns, the peeked value is always the largest in-window element.

## Complexity

- Time: O(n log n) — each element is offered and polled at most once, each heap op is O(log n).
- Space: O(n) — the heap can hold up to n entries before stale ones are purged.
