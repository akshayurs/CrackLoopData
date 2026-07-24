The same idea in Java: hold the stones in an `ArrayList<Integer>` and sort it before every smash so the two heaviest values sit at the end. Remove them, and if a remainder is left, add it back for the next round.

```java
import java.util.ArrayList;
import java.util.Collections;
import java.util.List;

class Solution {
    public int lastStoneWeight(int[] stones) {
        List<Integer> arr = new ArrayList<>();
        for (int s : stones) arr.add(s);
        while (arr.size() > 1) {
            Collections.sort(arr);
            int heaviest = arr.remove(arr.size() - 1);
            int second = arr.remove(arr.size() - 1);
            if (heaviest != second) {
                arr.add(heaviest - second);
            }
        }
        return arr.isEmpty() ? 0 : arr.get(0);
    }
}
```

## Why it works

Sorting ascending before each round puts the two largest weights at the tail of the list, so the two `remove` calls always take the current two heaviest stones. Re-inserting the difference (when the stones aren't equal) preserves the invariant for the next pass. The loop ends with at most one stone, which is the answer.

## Complexity

- Time: O(n² log n) — up to n rounds, each paying O(n log n) to re-sort.
- Space: O(n) — the working list of stones.
