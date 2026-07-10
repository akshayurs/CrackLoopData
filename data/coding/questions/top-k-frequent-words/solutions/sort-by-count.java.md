The most direct plan: count how often each word shows up, then rank the distinct words by that count. A single comparator — frequency descending, word ascending — handles the ranking and the tie-break in one step.

Once the distinct words are ordered this way, the answer is just the first `k` of them.

```java
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

class Solution {
    public List<String> topKFrequentWords(String[] words, int k) {
        Map<String, Integer> counts = new HashMap<>();
        for (String w : words) counts.merge(w, 1, Integer::sum);

        List<String> ordered = new ArrayList<>(counts.keySet());
        ordered.sort((a, b) -> {
            int diff = counts.get(b) - counts.get(a);
            return diff != 0 ? diff : a.compareTo(b);
        });
        return ordered.subList(0, k);
    }
}
```

## Why it works

The comparator first orders by descending frequency; when two words tie, it falls back to `String.compareTo`, which puts the alphabetically smaller word first — exactly the tie-break the problem requires. Taking the first `k` entries of that ordering gives the correct answer.

## Complexity

- Time: O(n log n) — counting is O(n); sorting the up-to-n distinct words dominates.
- Space: O(n) — the map and the sorted list each hold up to n entries.
