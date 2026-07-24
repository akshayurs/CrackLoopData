Flatten the problem: tag every value with which list it came from, then sort all of those `(value, list)` pairs together. Any range that covers all `k` lists now corresponds to a contiguous window of this sorted sequence that contains every list tag at least once — a classic "smallest window with all tags" sliding-window problem.

Slide the window's right edge forward, and whenever all `k` tags are present, shrink from the left as far as possible while keeping that property, checking each valid window against the best range seen so far.

```java
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

class Solution {
    public int[] smallestRange(List<List<Integer>> lists) {
        List<int[]> merged = new ArrayList<>();
        for (int i = 0; i < lists.size(); i++) {
            for (int value : lists.get(i)) merged.add(new int[]{value, i});
        }
        merged.sort((a, b) -> a[0] - b[0]);

        int k = lists.size();
        Map<Integer, Integer> count = new HashMap<>();
        int formed = 0, left = 0;
        int[] best = {merged.get(0)[0], merged.get(merged.size() - 1)[0]};

        for (int right = 0; right < merged.size(); right++) {
            int tag = merged.get(right)[1];
            count.merge(tag, 1, Integer::sum);
            if (count.get(tag) == 1) formed++;

            while (formed == k) {
                int lo = merged.get(left)[0];
                int hi = merged.get(right)[0];
                if (hi - lo < best[1] - best[0]) best = new int[]{lo, hi};
                int leftTag = merged.get(left)[1];
                count.merge(leftTag, -1, Integer::sum);
                if (count.get(leftTag) == 0) formed--;
                left++;
            }
        }
        return best;
    }
}
```

## Why it works

Sorting merges all `k` lists into one non-decreasing sequence while remembering each value's origin. A window covers every list exactly when its tags include all `k` list indices, so shrinking the window from the left while it stays valid finds the tightest such window. Because the sequence is sorted, the window's endpoints are the true `lo`/`hi` of the range, and the greedy shrink never skips a better answer.

## Complexity

- Time: O(N log N) — N is the total number of elements; dominated by the sort.
- Space: O(N) — the merged array and the tag-count map.
