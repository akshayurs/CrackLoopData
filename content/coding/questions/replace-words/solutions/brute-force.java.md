Same literal approach in Java: split the sentence on spaces and, for each word, scan the whole dictionary for the shortest root that is a prefix of it.

Nothing is precomputed, so every word re-scans the full dictionary — a straightforward first draft before reaching for a trie.

```java
import java.util.List;

class Solution {
    public String replaceWords(List<String> dictionary, String sentence) {
        String[] words = sentence.split(" ");
        StringBuilder result = new StringBuilder();
        for (int w = 0; w < words.length; w++) {
            String word = words[w];
            String best = null;
            for (String root : dictionary) {
                if (word.startsWith(root) && (best == null || root.length() < best.length())) {
                    best = root;
                }
            }
            if (w > 0) result.append(" ");
            result.append(best != null ? best : word);
        }
        return result.toString();
    }
}
```

## Why it works

`best` holds the shortest root confirmed to prefix the current word via `startsWith`. Because every root is checked against every word, no valid match is missed, and the length comparison keeps only the shortest one. A word with no matching root is appended as-is.

## Complexity

- Time: O(w * r * L) — w words, r roots, up to L characters compared per `startsWith` call.
- Space: O(w) — the output builder, ignoring the input.
