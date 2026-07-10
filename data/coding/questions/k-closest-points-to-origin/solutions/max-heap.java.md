Sorting every point is wasteful when `k` is small — you only need to know the `k` smallest distances, not the full order of `n` of them. A max-heap capped at size `k` does exactly that: push points in, and whenever the heap grows past `k`, poll the farthest one out.

Java's `PriorityQueue` is a min-heap by default, so it is given a comparator that orders by *largest* distance first, turning it into a max-heap.

```java
import java.util.PriorityQueue;
import java.util.ArrayList;
import java.util.List;

class Solution {
    public int[][] kClosest(int[][] points, int k) {
        PriorityQueue<int[]> heap = new PriorityQueue<>(
            (a, b) -> Long.compare(dist(b), dist(a))
        );
        for (int[] p : points) {
            heap.offer(p);
            if (heap.size() > k) {
                heap.poll();
            }
        }
        List<int[]> result = new ArrayList<>(heap);
        result.sort((a, b) -> {
            long d = dist(a) - dist(b);
            if (d != 0) return Long.signum(d);
            if (a[0] != b[0]) return a[0] - b[0];
            return a[1] - b[1];
        });
        return result.toArray(new int[0][]);
    }

    private long dist(int[] p) {
        return (long) p[0] * p[0] + (long) p[1] * p[1];
    }
}
```

## Why it works

The heap always holds at most `k` points, with the farthest one accessible at the head. Offering a new point and polling whenever the size exceeds `k` always removes the true farthest among the `k + 1` candidates, so a closer point can never be wrongly discarded. Once every point is processed, the heap holds exactly the `k` nearest; the trailing sort imposes the required deterministic order.

## Complexity

- Time: O(n log k) — each offer/poll costs O(log k), plus O(k log k) for the final sort.
- Space: O(k) — the heap never holds more than k points.
