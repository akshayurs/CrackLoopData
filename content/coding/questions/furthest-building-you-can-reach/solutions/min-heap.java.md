Instead of re-deciding the whole ladder assignment from scratch at every step, commit greedily and let a min-heap correct course if needed. Every positive gap first "borrows" a ladder by going into a min-heap of size `ladders`. The moment the heap overflows, the smallest gap currently sitting in it is the least deserving of a free ladder, so it gets evicted and paid for with bricks instead.

```java
import java.util.*;

class Solution {
    public int furthestBuilding(int[] heights, int bricks, int ladders) {
        PriorityQueue<Integer> ladderClimbs = new PriorityQueue<>();
        for (int i = 0; i < heights.length - 1; i++) {
            int diff = heights[i + 1] - heights[i];
            if (diff <= 0) continue;
            ladderClimbs.offer(diff);
            if (ladderClimbs.size() > ladders) {
                bricks -= ladderClimbs.poll();
            }
            if (bricks < 0) return i;
        }
        return heights.length - 1;
    }
}
```

## Why it works

The heap always holds the `ladders` largest gaps seen so far among the ones "in flight." Whenever a new gap arrives and the heap is full, the smallest gap being considered is the correct one to demote to bricks, since keeping it over a larger gap could never be optimal. `bricks` is debited lazily as demotions happen, so the moment it goes negative, this exact prefix of the array is unreachable within budget.

## Complexity

- Time: O(n log l) — one heap push per building, one pop when it overflows the ladder capacity `l`.
- Space: O(l) — the heap never holds more than `ladders` elements.
