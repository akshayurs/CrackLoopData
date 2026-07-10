Re-sorting the whole collection every round is overkill — all that's ever needed is the current two largest values, and a heap gives those in O(log n). Java's `PriorityQueue` is a min-heap by default, so it is built with a reversed comparator to make it a max-heap.

Poll the two largest stones each round, smash them, and offer the remainder back if the stones weren't equal.

```java
import java.util.Collections;
import java.util.PriorityQueue;

class Solution {
    public int lastStoneWeight(int[] stones) {
        PriorityQueue<Integer> heap = new PriorityQueue<>(Collections.reverseOrder());
        for (int s : stones) heap.offer(s);
        while (heap.size() > 1) {
            int heaviest = heap.poll();
            int second = heap.poll();
            if (heaviest != second) {
                heap.offer(heaviest - second);
            }
        }
        return heap.isEmpty() ? 0 : heap.poll();
    }
}
```

## Why it works

The reversed comparator makes `poll` always return the largest remaining element, so two consecutive polls give the current two heaviest stones in O(log n) each. Offering the remainder back, only when the stones differ, keeps the heap representing the true multiset of stones after each smash, matching the problem's rules exactly.

## Complexity

- Time: O(n log n) — n insertions to build the heap, then O(1) poll/offer per round at O(log n) each.
- Space: O(n) — the heap holds the stones.
