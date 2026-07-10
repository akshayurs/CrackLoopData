Instead of sorting everything up front, walk all `k` lists in lockstep with one pointer each, always advancing whichever list currently holds the smallest pointed-to value. A min-heap gives that minimum in O(log k) instead of scanning all `k` pointers, and tracking the running maximum alongside it turns every heap pop into one candidate range.

At every step the heap's minimum and the tracked maximum define a range that already touches all `k` lists — one element per list is on the "table" at all times — so shrinking is really just advancing the smallest pointer and re-measuring.

```java
import java.util.List;
import java.util.PriorityQueue;

class Solution {
    public int[] smallestRange(List<List<Integer>> lists) {
        PriorityQueue<int[]> heap = new PriorityQueue<>((a, b) -> a[0] - b[0]);
        int currentMax = Integer.MIN_VALUE;
        for (int i = 0; i < lists.size(); i++) {
            int value = lists.get(i).get(0);
            heap.offer(new int[]{value, i, 0});
            currentMax = Math.max(currentMax, value);
        }

        int[] best = {heap.peek()[0], currentMax};

        while (true) {
            int[] top = heap.poll();
            int value = top[0], listI = top[1], elemI = top[2];
            if (currentMax - value < best[1] - best[0]) best = new int[]{value, currentMax};

            if (elemI + 1 == lists.get(listI).size()) return best;

            int nextValue = lists.get(listI).get(elemI + 1);
            currentMax = Math.max(currentMax, nextValue);
            heap.offer(new int[]{nextValue, listI, elemI + 1});
        }
    }
}
```

## Why it works

The heap always holds exactly one element per list, so its minimum and the tracked maximum bound the tightest range currently touching every list. Popping the minimum and advancing that list's pointer is the only way to shrink the range further, since raising the low end past any other pointer would drop that list out of coverage. The moment a list runs out of elements, no smaller range can be completed, so the best range found so far is final.

## Complexity

- Time: O(N log k) — N is the total number of elements; each of the N heap operations costs O(log k).
- Space: O(k) — the heap holds exactly one entry per list.
