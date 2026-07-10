Split the numbers into two halves around the median: a max-heap `lo` holding the smaller half, and a min-heap `hi` holding the larger half, kept the same size (or `lo` one larger). The median then always sits at the top of one or both heaps — no sorting needed.

`PriorityQueue` gives a min-heap by default, so `lo` is built with a reverse comparator to act as a max-heap. On every `addNum`, push into one heap and rebalance by moving the top of one to the other so the size invariant holds.

```java
import java.util.PriorityQueue;
import java.util.Collections;

class MedianFinder {
    private PriorityQueue<Integer> lo; // max-heap, smaller half
    private PriorityQueue<Integer> hi; // min-heap, larger half

    public MedianFinder() {
        lo = new PriorityQueue<>(Collections.reverseOrder());
        hi = new PriorityQueue<>();
    }

    public void addNum(int num) {
        lo.offer(num);
        hi.offer(lo.poll());
        if (hi.size() > lo.size()) {
            lo.offer(hi.poll());
        }
    }

    public double findMedian() {
        if (lo.size() > hi.size()) return lo.peek();
        return (lo.peek() + hi.peek()) / 2.0;
    }
}
```

## Why it works

Every value first goes into `lo`, then its largest member is immediately promoted to `hi` — this guarantees every element of `lo` is `<=` every element of `hi`. Rebalancing keeps the sizes equal or `lo` exactly one larger, so the median is either `lo`'s top (odd total) or the average of both tops (even total).

## Complexity

- Time: O(log n) per `addNum` (heap offer/poll); O(1) per `findMedian`.
- Space: O(n) — the two heaps together hold every number added.
