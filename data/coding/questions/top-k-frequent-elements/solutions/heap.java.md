Sorting every distinct value is wasteful when `k` is small — you only care about the top few. Keep a min-heap of size `k` instead: push each value keyed by its count, and whenever the heap grows past `k`, poll the smallest. The heap always holds the `k` most frequent values seen so far, with the cheapest of them at the head ready to be evicted.

This trades the full O(n log n) sort for O(n log k), a clear win when `k` is much smaller than the number of distinct values.

```java
import java.util.HashMap;
import java.util.Map;
import java.util.PriorityQueue;

class Solution {
    public int[] topKFrequent(int[] nums, int k) {
        Map<Integer, Integer> counts = new HashMap<>();
        for (int n : nums) counts.merge(n, 1, Integer::sum);

        PriorityQueue<Integer> heap =
            new PriorityQueue<>((a, b) -> counts.get(a) - counts.get(b));
        for (int value : counts.keySet()) {
            heap.offer(value);
            if (heap.size() > k) heap.poll();
        }
        int[] result = new int[k];
        for (int i = 0; i < k; i++) result[i] = heap.poll();
        java.util.Arrays.sort(result);
        return result;
    }
}
```

## Why it works

The priority queue is ordered by count, so its head is always the least frequent value currently retained. Once every distinct value has been offered, anything less frequent than the top `k` has already been polled away, leaving precisely the `k` most frequent. With at most `k + 1` elements present, each heap operation costs O(log k). A final ascending sort of those `k` values gives a deterministic output order.

## Complexity

- Time: O(n log k) — counting is O(n); each of the up-to-n offers/polls costs O(log k); the final sort of the k results costs O(k log k), which does not change the dominant term.
- Space: O(n) — the map holds up to n entries; the heap holds k.
