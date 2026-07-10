The brute-force re-sort is doing the same work repeatedly: as the prefix grows by one element, the set of "current top `k` values" barely changes. A min-heap of size `k` tracks exactly that set incrementally — push the new value, and if the heap now holds more than `k` values, evict the smallest. The heap's total is always the sum of the best `k` values seen so far.

Sorting by `nums2` descending first is unchanged: it guarantees that whichever element we are currently processing has the smallest `nums2` among everything considered, so it is the correct multiplier the moment the heap reaches size `k`.

```java
import java.util.Arrays;
import java.util.PriorityQueue;

class Solution {
    public long maxScore(int[] nums1, int[] nums2, int k) {
        int n = nums1.length;
        Integer[] idx = new Integer[n];
        for (int i = 0; i < n; i++) idx[i] = i;
        Arrays.sort(idx, (a, b) -> nums2[b] - nums2[a]);

        PriorityQueue<Integer> heap = new PriorityQueue<>();
        long total = 0, best = 0;
        for (int i = 0; i < n; i++) {
            int a = nums1[idx[i]];
            heap.offer(a);
            total += a;
            if (heap.size() > k) total -= heap.poll();
            if (heap.size() == k) best = Math.max(best, total * nums2[idx[i]]);
        }
        return best;
    }
}
```

## Why it works

At every step the heap holds the `k` largest `nums1` values among all pairs processed so far, and `total` is their sum — pushing then popping the minimum whenever the heap overflows keeps that invariant. Because the pairs are processed in descending `nums2` order, the current pair's `nums2` is the smallest multiplier available among everything seen, matching the pivot argument from the brute-force approach. Taking the max of `total * nums2[idx[i]]` at every point where the heap is full evaluates every valid pivot exactly once.

## Complexity

- Time: O(n log n) — one sort plus one heap push/pop per element.
- Space: O(n) — the heap holds at most `k` elements; the index array takes O(n).
