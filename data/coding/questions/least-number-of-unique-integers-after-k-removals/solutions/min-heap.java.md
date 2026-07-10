The brute-force scan is wasted work: once you know the counts, the removal order never changes — you always want to finish off the value with the smallest remaining count first. A `PriorityQueue` gives you that minimum in O(log u), so seed it with every value's count once, then keep popping and spending removals as long as `k` covers the current minimum.

```java
import java.util.HashMap;
import java.util.Map;
import java.util.PriorityQueue;

class Solution {
    public int findLeastNumOfUniqueInts(int[] arr, int k) {
        Map<Integer, Integer> counts = new HashMap<>();
        for (int num : arr) counts.merge(num, 1, Integer::sum);

        PriorityQueue<Integer> heap = new PriorityQueue<>(counts.values());
        int unique = heap.size();
        while (!heap.isEmpty() && k >= heap.peek()) {
            k -= heap.poll();
            unique--;
        }
        return unique;
    }
}
```

## Why it works

The heap always exposes the value that is cheapest to eliminate. If `k` is at least that count, removing it entirely is free and strictly reduces the unique count, so it's always safe to take. Once `k` is smaller than the heap's minimum, no remaining value can be fully cleared, so every value still in the heap must survive.

## Complexity

- Time: O(n log n) — building the counts is O(n); building and draining a heap of u values costs O(u log u).
- Space: O(n) — the count map and heap each hold up to n entries.
