Re-sorting the whole window every step throws away almost all of the previous work. Instead, keep the window split across two heaps: a max-heap `small` holding the lower half and a min-heap `large` holding the upper half, kept balanced in size so the median always sits at one (or both) of their tops.

The wrinkle is deletion — `PriorityQueue` doesn't support "remove this arbitrary value" efficiently. The trick is lazy deletion: when a number slides out of the window, record that it owes a removal in a `delayed` map, and only actually poll it once it would otherwise surface at the top. Sizes are still tracked exactly, so balancing and the median calculation stay correct even while stale values linger deeper in a heap. A small `DualHeap` helper keeps this state self-contained per call.

```java
import java.util.*;

class Solution {
    public double[] medianSlidingWindow(int[] nums, int k) {
        DualHeap dh = new DualHeap(k);
        double[] result = new double[nums.length - k + 1];
        for (int i = 0; i < nums.length; i++) {
            dh.insert(nums[i]);
            if (i >= k) dh.erase(nums[i - k]);
            if (i >= k - 1) result[i - k + 1] = dh.getMedian();
        }
        return result;
    }
}

class DualHeap {
    private final PriorityQueue<Integer> small = new PriorityQueue<>(Collections.reverseOrder());
    private final PriorityQueue<Integer> large = new PriorityQueue<>();
    private final Map<Integer, Integer> delayed = new HashMap<>();
    private final int k;
    private int smallSize = 0, largeSize = 0;

    DualHeap(int k) { this.k = k; }

    void insert(int num) {
        if (small.isEmpty() || num <= small.peek()) { small.offer(num); smallSize++; }
        else { large.offer(num); largeSize++; }
        balance();
    }

    void erase(int num) {
        delayed.merge(num, 1, Integer::sum);
        if (num <= small.peek()) { smallSize--; if (num == small.peek()) prune(small); }
        else { largeSize--; if (num == large.peek()) prune(large); }
        balance();
    }

    double getMedian() {
        return k % 2 == 1 ? small.peek() : ((long) small.peek() + large.peek()) / 2.0;
    }

    private void balance() {
        if (smallSize > largeSize + 1) { large.offer(small.poll()); smallSize--; largeSize++; prune(small); }
        else if (smallSize < largeSize) { small.offer(large.poll()); largeSize--; smallSize++; prune(large); }
    }

    private void prune(PriorityQueue<Integer> heap) {
        while (!heap.isEmpty() && delayed.getOrDefault(heap.peek(), 0) > 0) {
            int cnt = delayed.get(heap.peek()) - 1;
            if (cnt == 0) delayed.remove(heap.peek()); else delayed.put(heap.peek(), cnt);
            heap.poll();
        }
    }
}
```

## Why it works

`small` and `large` are kept the same size (or `small` one larger), so the median is always `small`'s top for odd `k`, or the average of both tops for even `k`. Lazy deletion keeps the heaps' logical sizes accurate — `smallSize`/`largeSize` reflect reality even before a stale entry is physically polled — so every balance and median read uses correct counts, and pruning only touches values that have actually become garbage.

## Complexity

- Time: O(n log k) — each insert, erase, and balance touches a heap of size O(k), and each element causes O(1) amortized heap operations overall.
- Space: O(k) — the two heaps together hold the current window (plus bounded stale entries awaiting cleanup).
