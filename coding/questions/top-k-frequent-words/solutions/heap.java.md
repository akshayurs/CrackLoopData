Sorting every distinct word costs O(n log n) even though only `k` of them are ever returned. A heap lets you pay for just the `k` extractions you need on top of a linear-time build.

Build a `PriorityQueue` whose comparator orders entries by frequency descending, word ascending, and construct it directly from the count map's entries — `PriorityQueue`'s collection constructor heapifies in linear time rather than inserting one at a time.

```java
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;
import java.util.PriorityQueue;

class Solution {
    public List<String> topKFrequentWords(String[] words, int k) {
        Map<String, Integer> counts = new HashMap<>();
        for (String w : words) counts.merge(w, 1, Integer::sum);

        PriorityQueue<Map.Entry<String, Integer>> heap = new PriorityQueue<>(
            (a, b) -> !a.getValue().equals(b.getValue())
                ? b.getValue() - a.getValue()
                : a.getKey().compareTo(b.getKey())
        );
        heap.addAll(counts.entrySet());

        List<String> result = new ArrayList<>();
        for (int i = 0; i < k; i++) result.add(heap.poll().getKey());
        return result;
    }
}
```

## Why it works

The comparator makes the queue's head always the current best candidate: higher count wins outright, and equal counts fall back to `String.compareTo`, matching the required alphabetical tie-break. `addAll` on a fresh `PriorityQueue` builds the heap in linear time, so only the `k` calls to `poll` cost a logarithm each.

## Complexity

- Time: O(n + k log n) — counting and building the heap from the up-to-n entries is O(n); each of the k polls costs O(log n).
- Space: O(n) — the map and the heap each hold up to n entries.
